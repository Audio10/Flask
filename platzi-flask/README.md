# 1. Fundamentos de Flask

## Hello World Flask

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

## Debugging en Flask

**Debugging:** es el proceso de identificar y corregir errores de programación.

Para activar el *debug mode* escribir lo siguiente en la consola:

```bash
export FLASK_DEBUG=1
echo $FLASK_DEBUG
```

## Request y Response

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

