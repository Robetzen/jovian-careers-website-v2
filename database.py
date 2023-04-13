import sqlalchemy
from sqlalchemy  import create_engine, text

db_connection_string = "mysql+pymysql://ths2foh978slwyq2p9kg:pscale_pw_TWs5KenEcWYhcfIVs4On2v8jtBLBwazE5iN9Ub8S1EV@us-east.connect.psdb.cloud/webproject?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
    "ssl":{
         "ssl_ca": "/etc/ssl/cert.pem"
    }
})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())