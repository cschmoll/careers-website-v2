from flask import Flask, render_template, jsonify
from database import engine, load_jobs_from_db

#https://careers-website.cschmoll.repl.co/
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Dehli, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'San Franciso, USA'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Dehli, India',
        'salary': 'Rs. 20,00,000'
    },
]


@app.route("/")
def hello_world():

  jobs = load_jobs_from_db()

  return render_template('home.html', jobs=jobs, company_name='Christof')
  #return render_template('home.html', jobs=JOBS, company_name='Christof' )


@app.route("/api/jobs")
def list_jobs():

  #return jsonify(JOBS)
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
