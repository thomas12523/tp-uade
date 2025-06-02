def checkString(string):
    """
    Descripción: Verifica si una cadena de texto no está vacía o tiene un espacio de relleno.
    Input: string es del tipo String que representa la cadena a verificar.
    Output: Devuelve True si la cadena no está vacía o no es un espacio de relleno, False en caso contrario.
    """
    if (string =='' or string==' '):
        return False
    return True

def checkDireccion(s):
    """
    Descripción: Verifica si una cadena de texto es una dirección válida.
    Input: s es del tipo String que representa la dirección a verificar.
    Output: Devuelve True si la cadena es una dirección válida, False en caso contrario."""
    if not checkString(s):
        return False
    if len(s)<3:
        return False
    if s[0]== ' ' or s[-1] == ' ':
        return False
    s = s.split()
    
    if not s[-1].isdigit():
        return False
    
    for palabra in s[:len(s)-2]:
        if not palabra.isalpha():
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

def checkEmail(email):
    """
    Descripción: Verifica si una cadena de texto es un correo electrónico válido.
    Input: email es del tipo String que representa el correo electrónico a verificar.
    Output: Devuelve True si la cadena es un correo electrónico válido, False en caso contrario.
    """
    if '@' not in email or '.' not in email:
        return False
    if email.count('@') != 1:
        return False
    
    email = email.split('@')
    if len(email[0]) < 1 or len(email[1]) < 3:
        return False
    if email[1][-4:]!='.com' and email[1][-4:]!='.org':
        return False
    if email[1][:-4] == '' or email[1][:-4].isnumeric():
        return False
    return True