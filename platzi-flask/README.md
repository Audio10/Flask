# 1. Fundamentos de Flask

# Configuración de Flask

Estos son los conceptos principales que debes entender antes de hacer un Hello World en Flask:

- **virtualenv:** es una herramienta para crear entornos aislados de Python.

  ```
  virtualenv venv --python=python3.7
  ```

- **pip:** es el instalador de paquetes para Python.

- **requirements.txt:** es el archivo en donde se colocará todas las dependencias a instalar en nuestra aplicación.

  ```
  pip install -r requirements.txt 
  ```

- **FLASK_APP:** es la variable para identificar el archivo donde se encuentra la aplicación.

  Por lo cual se debe generar de esta forma desde consola ya que asi se tomara el archivo de entrada para la app.

  ```
  export FLASK_APP=main.py
  ```

  Y después ejecutamos flask run para correr el servidor.

  ```
  flask run
  ```

## Debugging en Flask.

**Debugging:** es el proceso de identificar y corregir errores de programación.

Para activar el *debug mode* escribir lo siguiente en la consola:

```bash
export FLASK_DEBUG=1
echo $FLASK_DEBUG
```

## Development mode.

Para activar el *development mode* debes escribir lo siguiente en la consola:

```bash
export FLASK_ENV=development
echo $FLASK_ENV
```

## Session.

SESSION:** es un intercambio de información interactiva semipermanente, también conocido como diálogo, una conversación o un encuentro, entre dos o más dispositivos de comunicación, o entre un ordenador y usuario.

Esta es usada en flask para encriptar y guardarla con una llave secreta para que se maneje la  información de maneja seguro.

Dentro de la app existe un diccionario llamado **config** en el cual mediante el identificador **SECRET_KEY** se  puede asignar un hash para el encriptado de la sesión.

```python
app.config['SECRET_KEY'] = 'SUPER SECRETO'
```

Después debemos importar **session**.

```python
from flask import session
```

Y para asignar un valor a la sesión se asigna mediante el diccionario de esta misma.

```python
session['user_ip'] = user_ip
```

Y para recuperarlo se ocupa get.

```python
user_ip = session.get('user_ip')
```

# Request y Response

**Logging:** es una grabación secuencial en un archivo o en una base de datos de todos los eventos que afectan a un proceso particular.

Se utiliza en muchos casos distintos, para guardar información sobre la actividad de sistemas variados.

Tal vez su uso más inmediato a nuestras actividades como desarrolladores web sería el *logging* de accesos al servidor web, que analizado da información del tráfico de nuestro sitio. Cualquier servidor web dispone de *logs* con los accesos, pero además, suelen disponer de otros *logs*, por ejemplo, de errores.

Los sistemas operativos también suelen trabajar con *logs*, por ejemplo para guardar incidencias, errores, accesos de usuarios, etc.

A través de el *logs* se puede encontrar información para detectar posibles problemas en caso de que no funcione algún sistema como debiera o se haya producido una incidencia de seguridad.

## Ciclos de Request y Response

**Request-Response:** es uno de los métodos básicos que usan las computadoras para comunicarse entre sí, en el que la primera computadora envía una solicitud de algunos datos y la segunda responde a la solicitud.

Por lo general, hay una serie de intercambios de este tipo hasta que se envía el mensaje completo.

**Por ejemplo:** navegar por una página web es un ejemplo de comunicación de *request-response*.

*Request-response* se puede ver como una llamada telefónica, en la que se llama a alguien y responde a la llamada; es decir hacemos una petición y recibimos una respuesta.

### Request

Sirve para hacer consultas, es necesario importar de flask **request** para poder usarlo. 

Ejemplo de como pedir una cookie mediante request.

```
user_ip = request.cookies.get('user_ip')
```

### make_response

Genera una respuesta.

```
response = make_response(redirect('/hello'))
```

### redirect

Redirecciona a una determinada ruta. Puede ser invocado desde **make_response**.

```
response = make_response(redirect('/hello'))
```

### Manejo de cookies.

Las cookies pueden ir inmersas en la **response** 

```python
response.set_cookie('user_ip', user_ip)
```

### EJEMPLO

```python
from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return 'Hello world Platz, your IP is {}'.format(user_ip)
```

# Uso de templates y archivos estáticos.



## Templates con Jinja 2.

Principalmente debemos crear una carpeta llamada **templates** en la cual vamos a guardar todos nuestros templates y macros.

EJEMPLO DE TEMPLATE "hello.html"

**NOTA:** Para llamar variables enviadas por parametros, metodos constructores de templates padres, macros y redireccionamientos mediante href.

Para usar el **href** siempre dentro de los templates, porque el direccionamiento no es mediante rutas sino mediate funciones usando la siguiente sintaxis **url_for('funcion_que_contiene_la_ruta')**.

```jinja2
{% extends 'base.html' %}
{% import 'macros.html' as macros %}

{% block title %}
    {{ super() }}
    Bienvenido
{% endblock  %}

{% block content %}
    {% if user_ip %}
        <h1>Hello World Platzi, tu IP es {{ user_ip }}</h1>
    {% else %}
        <a href="{{ url_for('index') }}"> Ir a inicio</a>
    {% endif %}
    
    <ul>
        {% for todo in todos %}
            {{ macros.render_todo(todo)}}
        {% endfor %}
    </ul>
{% endblock %}
```

Despues desde nuestro **main.py** o en el endpoint determinado generamos una funcion que va a renderizar este template. 

**NOTA:** Es muy importante haber importado de flash **render_template**, dentro del ejemplo se especifica que para enviar datos a un template se puede enviar mediante un diccionario denominado context y utilizando la expansión ( ** ) para no tener que acceder dentro del template como **context['user_ip']** sino como **user_ip** nadamas.

```python
@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context)
```

**Estructuras de control**

**Iteración:** es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.

Un ejemplo de iteración sería el siguiente:

```jinja2
{% for key, segment in segment_details.items() %}
        <tr>
                <td>{{ key }}td>
                <td>{{ segment }}td>
        tr>
{% endfor %}  
```

En este ejemplo estamos iterando por cada *segment_details.items()* para mostrar los campos en una tabla `{{ key }}` `{{ segment }}` de esta forma dependiendo de cuantos *segment_details.items()* haya se repetirá el código.



## Herencia de templates.

**Macro:** son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra *macro* se vería de la siguiente manera:

```jinja2
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
    {% endif %}
{% endmacro %}
```

Un ejemplo de uso de macros en Flask:

```jinja2
{% from "macros.html" import nav_link with context %}
<!DOCTYPE html>
<html lang="en">
    <head>
    {% block head %}
        <title>My application</title>
    {% endblock %}
    </head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        </ul>
    {% block body %}
    {% endblock %}
    </body>
</html>
```

Como podemos observar en la primera línea estamos llamando a *macros.html* que contiene todos nuestros *macros*, pero queremos uno en específico así que escribimos `import nav_link` para traer el *macro* deseado y lo renderizamos de esta manera en nuestro menú `{{ nav_link('home', 'Home') }}`.



## Manejo de archivos estaticos.

Se debe crear un nuevo directorio denominado **static** donde se deben guardar los archivos css e imagenes.

### CSS

Donde el css se invoca de esta forma:

```jinja2
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">
```

### Imagenes.

```jinja2
<img src="{{ url_for('static', filename='images/platzi.png') }}"
                     style="max-width: 48px"
                     alt="Platzi logo">
```



## EJEMPLO COMPLETO

**Macro para representar los items de la lista de todos.**

```jinja2
{% macro render_todo(todo) %}
    <li>Descripcion: {{ todo }} </li>
{% endmacro %}
```



**Base.html**

Base va a ser el archivo base para extender el mismo dentro de otras vistas. En esta se va a importar el css.

En este ejemplo se importa de igualforma **flash-bootstrap** es por eso que la semantica esta dividida en bloques. Donde estenderemos head de bootstrap para cargar los estilos.

```jinja2
{% extends 'bootstrap/base.html' %}

{% block head %}
    {{ super() }}     

    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">
    <title>
        {% block title %} Flask Platzi | {% endblock %}
    </title>
{% endblock head %}

{% block body %}
    
    {% block navbar %}
        {% include 'navbar.html' %}
    {% endblock navbar %}
    
    
    {% block content %}
    
    {% endblock  %}
    
{% endblock body %}
```



**Navbar**

El navbar va a ser incluido dentro del base.html mediante el include que permite inyectar bloques de codigo de otros archivos dentro de otros.

```jinja2
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button"
                    class="navbar-toggle"
                    data-toggle="collapse"
                    data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="{{ url_for('index') }}">
                <img src="{{ url_for('static', filename='images/platzi.png') }}"
                     style="max-width: 48px"
                     alt="Platzi logo">
            </a>
        </div>

        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="{{ url_for('index') }}">Inicio</a></li>
                <li><a href="https://platzi.com" target="_blank">Platzi</a></li>
            </ul>
        </div>
    </div>
</div>
```



**Hello.html**

Dentro de hello.html se va extender de base el cual ya tiene bootstrap y el css inyectado. Dentro de base hay un bloque llamado content, donde va a estar el bloque content que se especifica en este archivo.

```jinja2
{% extends 'base.html' %}
{% import 'macros.html' as macros %}

{% block title %}
    {{ super() }}
    Bienvenido
{% endblock  %}

{% block content %}
    {% if user_ip %}
        <h1>Hello World Platzi, tu IP es {{ user_ip }}</h1>
    {% else %}
        <a href="{{ url_for('index') }}"> Ir a inicio</a>
    {% endif %}
    
    <ul>
        {% for todo in todos %}
            {{ macros.render_todo(todo)}}
        {% endfor %}
    </ul>
{% endblock %}
```

# Configurar páginas de error

## Códigos de error:

**100:** no son errores sino mensajes informativos. Como usuario nunca los verás, sino que entre bambalinas indica que la petición se ha recibido y se continúa el proceso.

**200:** estos códigos también indican que todo ha ido correctamente. La petición se ha recibido, se ha procesado y se ha devuelto satisfactoriamente. Por tanto, nunca los verás en tu navegador, pues significan que todo ha ido bien.

**300:** están relacionados con redirecciones. Los servidores usan estos códigos para indicar al navegador que la página o recurso que han pedido se ha movido de sitio. Como usuario, no verás estos códigos, aunque gracias a ellos una página te podría redirigir automáticamente a otra.

**400:** corresponden a errores del cliente y con frecuencia sí los verás. Es el caso del conocido error 404, que aparece cuando la página que has intentado buscar no existe. Es, por tanto, un error del cliente (la dirección web estaba mal).

**500:** mientras que los códigos de estado 400 implican errores por parte del cliente (es decir, de parte tuya, tu navegador o tu conexión), los errores 500 son errores desde la parte del servidor. Es posible que el servidor tenga algún problema temporal y no hay mucho que puedas hacer salvo probar de nuevo más tarde.

## EJEMPLO.

Dentro de flask los errores se manejan mediante el decorador **@app.errorhandler(código_Error)**

**Dentro de main.py**

Se genera una funcion con el decorador y se retorna el render de esta y por medio del contexto se envia el error.

```python
@app.errorhandler(404)
def not_fount(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def error_server(error):
    return render_template('500.html', error=error)
```



**404.html**

Ahora dentro del archivo a renderizar para el error se extiende del base. Se extiende el bloque del titulo y dentro del content se inyecta el contenido que se mostrara al usuario.

```jinja2
{% extends 'base.html' %}

{% block title %}
{{ super() }}
    404
{% endblock  %}

{% block content %}
    <h1>Lo sentimos no encontramos lo que buscabas</h1>
    <p>{{ error }}</p>
{% endblock content %}  
```

# Extenciones de Flask.

## Flask Bootstrap

**Framework:** es un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular que sirve como referencia, para enfrentar y resolver nuevos problemas de índole similar.

**Instalacion**

Dentro de nuestro archivo **requirements.txt** agregamos flask-bootstrap y lo instalamos con pip.

```
flask-bootstrap
```

Despues dentro de nuestro archivo **base.html** debemos extender **bootstrap/base.html**. De forma que debemos adaptar los bloques a la convencion que ocupa bootstrap.

```jinja2
{% extends 'bootstrap/base.html' %}

{% block head %}
    {{ super() }}     

    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">
    <title>
        {% block title %} Flask Platzi | {% endblock %}
    </title>
{% endblock head %}

{% block body %}
    
    {% block navbar %}
        {% include 'navbar.html' %}
    {% endblock navbar %}
    
    
    {% block content %}
    
    {% endblock  %}
{% endblock body %}
```

# Implementación de Flask-Bootstrap y Flask-WTF

Flask-WTF es una librería que sirve para renderear y validar forms en Python.

Agregar flask-wtf al **requeriments.txt**

```python
flask-wtf
```

## Imports

**main.py**

```python
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired
```

- Donde importaremos FlaskForm y crearemos una clase que extienda de esta misma.
- Importamos los fields para el formulario.
- Importamos DataRequired que valida la forma antes de enviarla al servidor.

## Creación de form

Se crea una clase que extiende de FlaskForm que será nuestro formulario.

Para validar los campos debemos anexar el parámetro **validatos** al cual sele asigna una lista de validadores en este caso una instancia de **DataRequired** que sera el encargado de validad.

**main.py**

```python
class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    subtmi = SubmitField('Enviar')
```

Después agregamos la **loginform** al contexto de la función que la valla a ocupar en este caso hello().

Dentro de esta función en el decorador se agrega el parámetro methods en el cual se especifican los metodos http que va a aceptar.

Agregaremos una variable **login_form** que va a hacer referencia a la forma. Y se enviara a la **sesion** el **username**.

Utilizamos **validate_on_submit()** que es un metodo de **FlaskForm** que lo que hace es detectar cuando mandas un post y valida la forma dividiendo la función en 2 cuando usen **get** envía el template con la forma, pero si hacen un post y la forma es valida se envía un **redirect** al index.

```python
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        flash('Nombre de usuario registrado con exito!')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)
    
```

**hello.html**

Para inyectar formas rápidamente se puede ocupar **bootstrap/wtf.html**

```jinja2
{% import 'bootstrap/wtf.html' as wtf %}


<div class="container">
        <!-- <form action="{{ url_for('hello')}}" method="POST">
            {{login_form.username}}
            {{login_form.username.label}}
        </form> -->

        {{ wtf.quick_form(login_form)}}
    </div>
```

## Flash (mensajes emergentes)

importamos flash.

```
from flask import flash
```

**base.html**

Donde get_flashed_messages() es una función que contiene todos los flashes.

**Nota**: Es muy importante heredar los **scripts** de bootstrap al final del body, sino no se podrá interactuar de maneja correcta el flash.

```jinja2
{% extends 'bootstrap/base.html' %}

{% block head %}
    {{ super() }}     

    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">
    <title>
        {% block title %} Flask Platzi | {% endblock %}
    </title>
{% endblock head %}

{% block body %}
    
    {% block navbar %}
        {% include 'navbar.html' %}
    {% endblock navbar %}
    
    {% for message in get_flashed_messages() %}
        <div class="alert alert-success alert-dismissible">
            <button type="button" 
                    data-dismiss="alert" 
                    class="close">&times;</button>
            {{ message }}
        </div>
    {% endfor %}
    
    {% block content %}
    
    {% endblock  %}

    {% block scripts %}
        {{ super() }}
    {% endblock %}
{% endblock body %}
```

# Pruebas básicas con Flask-testing

La etapa de pruebas se denomina *testing* y se trata de una investigación exhaustiva, no solo técnica sino también empírica, que busca reunir información objetiva sobre la calidad de un proyecto de software, por ejemplo, una aplicación móvil o un sitio web.

El objetivo del *testing* no solo es encontrar fallas sino también aumentar la confianza en la calidad del producto, facilitar información para la toma de decisiones y detectar oportunidades de mejora.

## imports

```
import unittest
```

## Creación

Creamos un comando con el decorador **@app.cli.command()** el cual se va a encargar de buscar todos los tests mediante el TestLoader.

Y mediante unittest va a correr todos los tests que se encuentran en el archivo denominado tests.

**main.py**

```
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
```

**tests.py**

Donde nuestra clase **MainTest** extendera de **TestCase** y se debe implementar el método **create_app** que retorna una aplicación sobre la cual se van a hacer las pruebas.

```python
from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        #Asignando ambiente de testing
        app.config['TESTING'] = True
        #Asignacion de no uso de tokkens porque no hay sesion activa.
        app.config['WTF CSRF ENABLED'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
        
    def test_hello_get(self):
        response =  self.client.get(url_for('hello'))
        self.assert200(response)
        
    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        
        self.assertRedirects(response, url_for('index'))
```

# App Factory (Configuración de carpetas)

Básicamente lo que se hace es establecer las carpetas de esta forma.

![1570128712349](C:\Users\claud\AppData\Roaming\Typora\typora-user-images\1570128712349.png)

# Uso de Blueprints

Es como una pequeña aplicación de flask que tiene rutas, vistas y templates pero debe ser importada dentro de una aplicación de flask para funcionar.

