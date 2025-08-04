from flask import *

import mysql.connector

#Conexión a la base de datos

conexion = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = 'root',
  database = 'vet' 
)
cursor = conexion.cursor()

app = Flask(__name__)

#página principal
@app.route('/')
def index():
  return render_template('index.html')

  #menu pedidos
@app.route('/pedidos')
def pedidos(): 
  query = "SELECT * FROM pedidos"
  cursor.execute(query)
  pedidos = cursor.fetchall()
  return render_template('pedidos.html', pedidos=pedidos)

#menu clientes
@app.route('/clientes')
def clientes():
  query = "SELECT * FROM clientes"
  cursor.execute(query)
  clientes = cursor.fetchall()
  return render_template('clientes.html', clientes=clientes)

#menu productos
@app.route('/productos')
def productos():
  query = "SELECT * FROM producto"
  cursor.execute(query)
  productos = cursor.fetchall()
  return render_template('productos.html', productos=productos)

  
#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------


@app.route('/agregar_clientes', methods= ['POST'])
def agregar_clientes():
  #Obtengo los datos del formulario
  nombre = request.form.get('nombre')
  telefono = request.form.get('telefono')
  direccion = request.form.get('direccion')
  fecha_registro = request.form.get('fecha_registro')

  #Los agrego en la base de datos
  query = 'INSERT INTO clientes (nombre, telefono, direccion, fecha_registro) VALUES (%s, %s, %s, %s)'
  cursor.execute(query, (nombre, telefono, direccion, fecha_registro))
  conexion.commit()
  return redirect(url_for('clientes'))

@app.route('/modificar_clientes', methods=['POST'])
def modificar_clientes():
  #Obtener ID
  id_cliente = request.form.get('ID')

  #Obtener campos modificados
  nombre = request.form.get('nombre')
  telefono = request.form.get('telefono')
  direccion = request.form.get('direccion')
  fecha_registro = request.form.get('fecha_registro')

  #Ejecutar SQL
  query = 'UPDATE clientes SET nombre = %s, telefono = %s, direccion = %s, fecha_registro = %s WHERE id_cliente = %s' 
  cursor.execute(query, (nombre, telefono, direccion, fecha_registro, id_cliente))
  return redirect(url_for ('clientes'))

@app.route('/eliminar_clientes', methods=['POST'])
def eliminar_clientes():
    # Obtener ID
    id_cliente = request.form.get('ID')

    try:
        # Consulta en la base de datos para eliminar el cliente
        query = 'DELETE FROM clientes WHERE id_cliente = %s'
        cursor.execute(query, (id_cliente,))
        conexion.commit()
    except mysql.connector.errors.IntegrityError:
        # Manejo del error de integridad
        return "Error: No se puede eliminar el cliente porque tiene pedidos asociados."
    
    return redirect(url_for('clientes'))





#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------






@app.route('/agregar_productos', methods= ['POST'])
def agregar_productos():
  #Obtengo los datos del formulario
  nombre = request.form.get('nombre')
  precio = request.form.get('precio')
  cantidad = request.form.get('cantidad')
  fecha_creacion = request.form.get('fecha_creacion')

  #Los agrego en la base de datos
  query = 'INSERT INTO producto (nombre, precio, cantidad, fecha_creacion) VALUES (%s, %s, %s, %s)'
  cursor.execute(query, (nombre, precio, cantidad, fecha_creacion))
  conexion.commit()
  return redirect(url_for('productos'))


@app.route('/modificar_productos', methods=['POST'])
def modificar_productos():
  #Obtener ID
  id_producto = request.form.get('ID')

  #Obtener campos modificados
  nombre = request.form.get('nombre')
  precio = request.form.get('precio')
  cantidad = request.form.get('cantidad')
  fecha_creacion = request.form.get('fecha_creacion')

  #Ejecutar SQL
  query = 'UPDATE Producto SET nombre = %s, precio = %s, cantidad = %s, fecha_creacion = %s WHERE id_producto = %s' 
  cursor.execute(query, (nombre, precio, cantidad, fecha_creacion, id_producto))
  return redirect(url_for ('productos'))

@app.route('/eliminar_productos', methods = ['POST'])
def eliminar_productos():
  #Obtener ID
  id_producto = request.form.get('ID')

  #Query en la base de datos para eliminar el producto de ese ID
  query = 'DELETE FROM producto WHERE '+id_producto+' = producto.id_producto'
  cursor.execute(query)
  conexion.commit()
  return redirect(url_for('productos'))





#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------





@app.route('/agregar_pedidos', methods= ['POST'])
def agregar_pedidos():
  #Obtengo los datos del formulario
  id_pedido = request.form.get('id_pedido')
  id_cliente = request.form.get('id_cliente')
  fecha_pedido = request.form.get('fecha_pedido')
  total = request.form.get('total')
  estado = request.form.get('estado')
  
  #Los agrego en la base de datos
  query = 'INSERT INTO pedidos (id_cliente, fecha_pedido, total, estado, id_pedido) VALUES (%s, %s, %s, %s, %s)'
  cursor.execute(query, (id_cliente, fecha_pedido, total, estado, id_pedido))
  conexion.commit()
  return redirect(url_for('pedidos'))

@app.route('/modificar_pedidos', methods=['POST'])
def modificar_pedidos():
  #Obtener ID
  id_pedido = request.form.get('ID')

  #Obtener campos modificados
  id_pedido = request.form.get('id_pedido')
  id_cliente = request.form.get('id_cliente')
  fecha_pedido = request.form.get('fecha_pedido')
  total = request.form.get('total')
  estado = request.form.get('estado')

  #Ejecutar SQL
  query = 'UPDATE pedidos SET id_cliente = %s, fecha_pedido = %s, total= %s, estado= %s WHERE id_pedido = %s' 
  cursor.execute(query, (id_cliente, fecha_pedido, total, estado, id_pedido))
  return redirect(url_for ('pedidos'))

@app.route('/eliminar_pedidos', methods = ['POST'])
def eliminar_pedidos():
  #Obtener ID
  id_pedido = request.form.get('id_pedido')

  #Query en la base de datos para eliminar el producto de ese ID
  query = 'DELETE FROM pedidos WHERE '+str(id_pedido)+' = pedidos.id_pedido'
  cursor.execute(query)
  conexion.commit()
  return redirect(url_for('pedidos'))


if __name__ == '__main__':
  app.run(debug=True)
