from flask import Flask, render_template 

app = Flask(__name__)


@app.route('/')
def hello_wolrd():
  return render_template('home.html')


print(__name__)

if __name__ == "__main__":
  app.run(debug=True)