import json, random
from flask import Flask, render_template, jsonify
from database import engine, load_jobs_from_db, load_job_from_db, Session
from models import Base, Jobs

#https://careers-website-v2.cschmoll.repl.co/
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

  session = Session()

  jobs = []
  #jobs = load_jobs_from_db()
  #jobs = session.query(Jobs).all()
  for job in session.query(Jobs).all():
    jobs.append(job.to_dict())

  return render_template('home.html', jobs=jobs)
  #return render_template('home.html', jobs=JOBS, company_name='Christof' )


@app.route("/job/<int:job_id>")
def show_job(job_id):

  #  jobs = load_jobs_from_db()

  session = Session()

  job = session.query(Jobs).filter(Jobs.id == job_id).first()
  selected_job = job.to_dict()
  #job = [job for job in jobs if job['id'] == job_id]
  #if len(job) == 0:
  if job is None:
    return "Not Found", 404
  else:
    #job = job[0]

    return render_template('job.html',
                           job=selected_job)


@app.route("/api/jobs")
def list_jobs():

  session = Session()

  jobs = []

  for job in session.query(Jobs).all():
    jobs.append(job.to_dict())

  #jobs = load_jobs_from_db()
  #return jsonify(JOBS)
  return jsonify(jobs)


if __name__ == '__main__':
  #app.run(host='0.0.0.0', debug=True, port=random.randint(2000, 9000))
  app.run(host='0.0.0.0', debug=True)
  #app.run(host='0.0.0.0', port=random.randint(2000, 9000))  # Dubugger
