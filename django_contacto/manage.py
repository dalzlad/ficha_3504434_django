#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#Al proyecto realizado el jueves:
"""
1.**Agregar el código necesario para registrar un 
servicio, los atributos son:
id,nombre,precio,observaciones,estado
Debe crear una carpeta donde incluirá todo el código
del servicio.
2. **Agregar el código necesario para registrar un 
cliente, los atributos son:
id,numero_documento,nombre,apellidos,direccion,email
Debe crear una carpeta donde incluirá todo el código
del cliente.
Hora de revisión: 7:15 a.m
""" 