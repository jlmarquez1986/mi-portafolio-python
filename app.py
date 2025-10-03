from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal (página de inicio)
@app.route('/')
def home():
    """Renderiza la plantilla principal del portfolio."""
    # Puedes pasar datos dinámicos a la plantilla aquí,
    # como una lista de proyectos, pero por ahora es estático.
    return render_template('index.html')

# Define una ruta para el código de estado 404 (página no encontrada)
@app.errorhandler(404)
def page_not_found(error):
    """Maneja los errores 404."""
    # Podrías crear una plantilla 404.html, pero usaremos la misma para simplificar.
    return render_template('index.html'), 404

# Ejecuta la aplicación si el archivo se ejecuta directamente
if __name__ == '__main__':
    # 'debug=True' permite que el servidor se reinicie automáticamente al guardar cambios
    # y muestra mensajes de error detallados. Útil en desarrollo.
    app.run(debug=True)