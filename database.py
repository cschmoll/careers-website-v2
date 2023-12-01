import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['DB_CONNECTION_STRING'])

Session = sessionmaker(bind=engine)

def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))

    jobs = []
    for element in result.all():
      jobs.append(element._mapping)

    return jobs

def load_job_from_db(id):
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs where id = :val"), {'val': id})

    jobs = []
    for element in result.all():
      jobs.append(element._mapping)

    return jobs


#with engine.connect() as connection:
  # nur noch zu Dokuzwecken enthalten, wird nicht mehr genutzt
  #result = connection.execute(text("select * from jobs"))
  #print("Type result: ", type(result))
  #result_all = result.all()
  #print("Type result_all: ", type(result_all))
  #print("result_all: ", result_all)
  #for element in result_all:
    # Gib jedes Element mit der print-Funktion aus
    #print("Type of element: ", type(element))
    #print("element.mapping :", element._mapping)
    #if 'title' in element._mapping:
      #print("Column 'title': %s" % element._mapping['title'])
    #for item in element._mapping.items():
      #print("item; ", item)
      #print("type of item: ", type(item))
