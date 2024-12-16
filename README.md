Gestión de Pedidos Restaurantes | Prueba Técnica Quick

Este README describe el proceso para configurar tu entorno de desarrollo en Ubuntu para trabajar con Docker y pyenv, y realizar una instalación de Python 3.12.7.
1. Actualizar el sistema y preparar dependencias

# Actualizar el índice de paquetes
sudo apt update

# Instalar certificados y curl para descargar paquetes de Docker
sudo apt-get install ca-certificates curl

# Crear el directorio para las llaves de Docker
sudo install -m 0755 -d /etc/apt/keyrings

# Descargar la clave GPG de Docker
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Dar permisos de lectura a la clave GPG
sudo chmod a+r /etc/apt/keyrings/docker.asc

2. Agregar el repositorio de Docker

# Agregar el repositorio de Docker a tu lista de fuentes
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Actualizar el índice de paquetes después de agregar el repositorio de Docker
sudo apt-get update

3. Instalar Docker

# Instalar Docker y los componentes necesarios
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

4. Instalar pyenv para gestionar versiones de Python

# Descargar e instalar pyenv
curl https://pyenv.run | bash

5. Configuración de pyenv en el shell

# Agregar la configuración de pyenv a .bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Recargar el archivo .bashrc para aplicar los cambios
source ~/.bashrc

6. Instalar Python 3.12.7 con pyenv


# Instalar Python 3.12.7 con pyenv
pyenv install 3.12.7

# Establecer Python 3.12.7 como la versión global
pyenv global 3.12.7

# Recargar el archivo .bashrc para aplicar los cambios
source ~/.bashrc

Con estos pasos, tendrás configurado tu entorno con Docker y Python 3.12.7, listo para comenzar el desarrollo de la prueba técnica de gestión de pedidos para restaurantes.
