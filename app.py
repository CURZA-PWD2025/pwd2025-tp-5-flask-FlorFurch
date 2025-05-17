from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    nombre = "Florencia Furch"
    descripcion = "Hola, soy una diseñadora gráfica, intentando aprender a programar en Python y Flask." 
    return f"<h1>Nombre: {nombre}</h1><p>Descripción: {descripcion}</p>"

@app.route("/productos")
def listar_productos():
    resultado = ""
    for producto in productos:
        resultado += f"ID: {producto['id']} - Descripción: {producto['descripcion']} - Categoría ID: {producto['categoria_id']}<br>"
    return resultado

@app.route("/categorias")
def listar_categorias():
    resultado = ""
    for categoria in categorias:
        resultado += f"ID: {categoria['id']} - Descripción: {categoria['descripcion']}<br>"
    return resultado
    

if __name__ == "__main__":
    app.run(debug=True)