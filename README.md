
# Gestión de Pedidos Restaurantes | Prueba Técnica Quick

Este README describe el proceso para configurar tu entorno de desarrollo y incializar enfocado en Ubuntu, para trabajar con Docker y pyenv, y realizar una instalación de Python 3.12.7.


## Instalacion

1. Instalar Docker

```
    sudo apt update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
```

```
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    sudo apt-get update
```

 - [Docker Instalacion oficial](https://docs.docker.com/engine/install/ubuntu/)

2. Intalacion pyenv y python

```
    curl https://pyenv.run | bash

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

    source ~/.bashrc

    pyenv install 3.12.7
    pyenv global 3.12.7

    source ~/.bashrc
```

## Inicializacion

1. Por primera vez

```
    docker compose down --volumes  --remove-orphans
    docker compose up --build;

    docker compose -f docker-compose.yml run backend python manage.py migrate
```

2. Segunda vez
   
```
    docker compose up
```
