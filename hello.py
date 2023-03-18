from flask import Flask, render_template, jsonify 

app = Flask(__name__)


JOBS = [
   {
     'id': 1,
     'title': 'Data Analyst',
     'location': 'Bengaluru, Idia',
     'salary': 'Rs. 10,00,000'
   },
   
     {
     'id': 2,
     'title': 'Data Scientist',
     'location': 'Bengaluru, Idia',
     'salary': 'Rs. 15,00,000'
   },
     
      {
     'id': 3,
     'title': 'Frontend Engineer',
     'location': 'Bengaluru, Idia',
     'salary': 'Rs. 12,00,000'
   },
      
      {
     'id': 4,
     'title': 'Backend Engineer',
     'location': 'San Francisco',
     'salary': '120,000'
   },  
   
  
]

@app.route('/')
def hello_wolrd():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  


print(__name__)

if __name__ == "__main__":
  app.run(debug=True)