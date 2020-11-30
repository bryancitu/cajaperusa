# funciones extra de la aplicacion users (generando el codigo para la confirmacion del email)

import random
import string

def code_generator(size=10, chars=string.ascii_uppercase + string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))