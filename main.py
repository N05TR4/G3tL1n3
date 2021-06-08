from requests import get, exceptions

def check_connection():
    try:
        get('https://www.xvideoss.com', timeout = 4)
        print('Estado Activo')

    except exceptions.ConnectionError:
        print('Estado Inactivo')


check_connection()
