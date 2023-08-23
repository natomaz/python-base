#!/usr/bin/env python3
"""Hello Word Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável lang devidamente configurada ex:

    export LANG=pt_BR
    
Execução:

    python3 hello.py
    ou
    ./hello.py #para utilizar esse é necessário digitar chmod +x hello.py no terminal 
"""
__version__="0.0.1"
__author__="NaTomaz"
__license__="Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5] #função usada p/ buscar o valor de uma variável específica - [:5] busca 5 primeiros caracteres

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)