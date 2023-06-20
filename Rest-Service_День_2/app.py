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


# Добавление нового продукта с атоматической генерацией id
@app.route('/products/new/name=<string:product_name>/description=<string:product_dscr>', methods=['GET'])
def create_products(product_name, product_dscr):
  product = {
    'id': products[-1]['id'] + 1,
    'name': product_name,
    'dscr': product_dscr,
  }  
  products.append(product)
  return jsonify({'Response': 'Successful product addition', 'product': product}), 201

# Обновление существующего продутка
@app.route('/products/update/<int:product_id>/name=<string:product_name>/description=<string:product_dscr>', methods=['GET'])
def update(product_id, product_name, product_dscr):
  for i in range(0, len(products)):
    if products[i]['id'] == product_id:
      if product_name != '':
        products[i]['name'] = product_name
      if product_dscr != '':
        products[i]['product_dscr'] = product_dscr
  return jsonify({'Response': 'Successful product update', 'product': product}), 201
# http://127.0.0.1:5000/products/new/name='Butter'/description='Slippy Butter'
# http://127.0.0.1:5000/products/update/product_id=2/name='Bad Butter'/description=''
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
