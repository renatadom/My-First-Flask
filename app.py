from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'technique': 'Oil Painting on Canvas', #title
    'size': 'min 100x100 cm', #location
    'price': 'min 1500€  max 10000€' # salary
  },
  { 
    'id': 2,
    'technique': 'Acrylic Painting on Board', #title
    'size': 'min 30x30 cm', #location
    'price': 'min 150€  max 10000€' # salary
  },
  {
    'id': 3,
    'technique': 'Water-Colour on Paper', #title
    'size': 'min 15x15 cm', #location
    'price': 'min 25€' # salary
  }, 
  {
  'id': 4,
  'technique': 'Pastel on Paper', #title
  'size': 'min 30x30 cm', #location
},
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'RenataDOM Art')

@app.route("api/jobs")
def list_jobs():
	return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
