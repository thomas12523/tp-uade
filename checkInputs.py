def checkString(string):
    """
    Descripción: Verifica si una cadena de texto no está vacía o tiene un espacio de relleno.
    Input: string es del tipo String que representa la cadena a verificar.
    Output: Devuelve True si la cadena no está vacía o no es un espacio de relleno, False en caso contrario.
    """
    if (string.isempty() or string==' '):
        return False
    return True

def checkInt(value):
    """
    Descripción: Verifica si un valor es un número entero.
    Input: value es del tipo String que representa el valor a verificar.
    Output: Devuelve True si el valor es un número entero, False en caso contrario.
    """
    return value.isdigit()

def checkTelefono(string):
    """
    Descripción: Verifica si una cadena de texto es un número de teléfono válido.
    Input: string es del tipo String que representa el número de teléfono a verificar.
    Output: Devuelve True si la cadena es un número de teléfono válido (10 dígitos), False en caso contrario.
    """
    return string.isnumeric() and len(string) == 10