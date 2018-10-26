
function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(`/samples/${sample}`).then(function(data) {
  // d3.json(`/samples/Jam`).then(function(data) {

    // @TODO: Build a Bubble Chart using the sample data
    var x_values = data.ID;
    var y_values = data.Transaction;
    // var m_size = data.Transaction;
    // var m_colors = data.otu_ids; 
    // var t_values = data.otu_labels;

    var trace1 = {
      x: x_values,
      y: y_values,
      // text: t_values,
      mode: 'markers',
      // marker: {
      //   color: m_colors,
      //   size: m_size
      // } 
    };

    var data = [trace1];

    var layout = {
      xaxis: { title: "ID"},
    };

    Plotly.newPlot('bubble', data, layout);
    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).

    d3.json(`/samples/${sample}`).then(function(data) { 
    // d3.json(`/samples/Jam`).then(function(data) {  
      var pie_values = data.ID;
      var pie_labels = data.Transaction;
      // var pie_hover = data.otu_labels.slice(0,10);

      var data = [{
        values: pie_values,
        labels: pie_labels,
        // hovertext: pie_hover,
        type: 'pie'
      }];
  
        Plotly.newPlot('pie', data);
  
    });
  });   
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/days").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    // buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  // buildMetadata(newSample);
}

// Initialize the dashboard
init();
