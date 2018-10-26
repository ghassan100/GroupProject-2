index.py
import sqlite3
import csv
@app.route('/uploadfile')
def uploadfile():
    return render_template('upload_files.html')

@app.route('/file_read', methods=['POST'])
def file_read():
    if request.method == 'POST':
       class csvrd(object):
          def csvFile(self):
            self.readFile('fm.csv')

          def readFile(self, filename):
            co = sql.connect("db/example.db")
            cur1 = co.cursor() 
            cur1.execute("""CREATE TABLE IF NOT EXISTS input_data(SID varchar,task varchar)""")
            filename.encode('utf-8')
            with open(filename) as f:
               reader = csv.reader(open(filename, "r"))
               for field in reader:
                    cur1.execute("INSERT INTO input_data VALUES (?,?);", field)
            co.commit()
            co.close()
return render_template('upload_success.html')
