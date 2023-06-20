from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)


# Список продуктов
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

# Обработка 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка 500
@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# Получение всех продутков
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})
  
  
# Получение продукта по id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
  if len(products) == 0:
    abort(404)
  for i in products:
    if i['id'] == product_id:
      product = i
      break
  return jsonify({'product': product})


# Добавление нового продукта с атоматической генерацией шв
@app.route('/products/', methods=['POST'])
def create_products():
  if not request.json or not 'name' in request.json:
    abort(400)
  product = {
    'id': products[-1]['id'] + 1,
    'name': request.json['name'],
    'dscr': request.json.get('dscr', ""),
  }  
  products.append(product)
  return jsonify({'product': product}), 201

# Удаление продукта
@app.route('/products/delete/<int:product_id>', methods=['GET'])
def delete_product(product_id):
  if len(products) == 0:
    abort(404)
  for i in range(0, len(products)):
    if products[i]['id'] == product_id:
      products.pop(i)
      break
    return f'Complete deleting {product_id} product'
@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    # returning string
    return "<html>\
                <body>\
                    <h1>Rest-Service_Day2</h1>\
                </body>\
            </html>"

app.run(debug = True) 
