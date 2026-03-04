#!/bin/bash

# Comprobar si se ha pasado un argumento
if [ -z "$1" ]; then
    echo "Uso: $0 <url_acortada>"
    exit 1
fi

# 1. curl -I: Obtiene solo las cabeceras (headers) de la URL.
# 2. curl -s: Activa el modo silencioso para que no muestre la barra de progreso.
# 3. grep -i "location:": Busca la línea que contiene la URL de destino.
# 4. cut -d ' ' -f 2: Corta la línea por el espacio y toma el segundo campo (la URL).
# 5. cut -d $'\r' -f 1: Corta la línea por el retorno de carro y toma el primer campo (la URL).

# curl -I -s "$1" | grep -i "location:" | cut -d ' ' -f 2
curl -I -s "$1" | grep -i "location:" | cut -d ' ' -f 2 | cut -d $'\r' -f 1