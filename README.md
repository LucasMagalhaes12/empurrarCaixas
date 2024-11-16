# Empurrar Caixas

<!-- ## Introdução: -->

<!-- ![Gameplay](res/empurraCaixas) -->

## Instalando dependências:
### Instalar a venv python:

    sudo apt install python3-venv
    
Criar ambiente virtual:
    
    python3 -m venv venv
    
para ativar:
    
    source venv/bin/activate
    
para desativar:
    
    deactivate

### Instalando biblioteca cairo:

Com o ambiente virtual python ativado, instale a biblioteca cairo através do pip:
    
    pip install pycairo

talvez seja necessário instalar as dependências de cairo antes de instalar o cairo com o pip:

    sudo apt install libcairo2-dev

## Executar Game:
Dentro da pasta do projeto e com o ambiente venv ativado:

    python3 src/main.py