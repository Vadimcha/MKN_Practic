from flask import Flask, jsonify, abort

app = Flask(__name__)
# home route

products = [
  {
    'id': 0,
    'name': 'Milk',
    'dscr': 'Milky milk',
  },
  {
    'id': 1,
    'name': 'Bread',
    'dscr': 'Tasty bread',
  },
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})
  
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
  if len(products) == 0:
    abort(404)
  for i in products:
    if i['id'] == product_id:
      product = i
      break
  return jsonify({'product': product})

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    # returning string
    return "<html>\
                <body>\
                    <h3><u>Hello World!</u></h3>\
                </body>\
            </html>"

app.run(debug = True) 