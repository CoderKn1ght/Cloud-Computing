from flask import Flask, render_template, request
import pypyodbc

app = Flask(__name__)
app.secret_key = "Secret"

connection = pypyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:cloudtestdb.database.windows.net,1433;Database=cloudtest;Uid=shashank@cloudtestdb;Pwd=Cloud@6331;")
cursor = connection.cursor()


@app.route('/')
def hello_world():
  results = cursor.execute("Select Course# from classes group by Course#")
  courses = [row[0] for row in results]
  return render_template('index.html',courses=courses);

@app.route('/Hello')
def hello():
    return "Hello World"


@app.route('/get_sections', methods=['GET', 'POST'])
def get_sections():
  course = request.form['Course#']
  results = cursor.execute("Select * from classes where Course#="+course)
  return render_template('sections.html',results=results,course=course)


if __name__ == '__main__':
  app.run(debug=True)
