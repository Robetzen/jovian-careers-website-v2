from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_wolrd():
  return "Hello world"


print(__name__)

if __name__ == "__main__":
  app.run()