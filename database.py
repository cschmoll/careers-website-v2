import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://careersv2_user:1VllDv0yWPA2C4pV6tqqMLgKQyHuhjv5@dpg-cl76m2qvokcc73bvdve0-a.frankfurt-postgres.render.com/careersv2"
)

def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))

    jobs = []
    for element in result.all():
      # Gib jedes Element mit der print-Funktion aus
      jobs.append(element._mapping)

    return jobs

with engine.connect() as connection:
  # nur noch zu Dokuzwecken enthalten, wird nicht mehr genutzt 
  result = connection.execute(text("select * from jobs"))
  print("Type result: ", type(result))
  result_all = result.all()
  print("Type result_all: ", type(result_all))
  print("result_all: ", result_all)
  for element in result_all:
    # Gib jedes Element mit der print-Funktion aus
    print("Type of element: ", type(element))
    print("element.mapping :", element._mapping)
    if 'title' in element._mapping:
      print("Column 'title': %s" % element._mapping['title'])
    for item in element._mapping.items():
      print("item; ", item)
      print("type of item: ", type(item))
