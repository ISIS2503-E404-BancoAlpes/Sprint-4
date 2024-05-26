from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Cliente

@app.route('/')
def index():
    return "Bienvenido al microservicio de clientes!"

@app.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)

@app.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        nuevo_cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('listar_clientes'))
    return render_template('nuevo_cliente.html')
