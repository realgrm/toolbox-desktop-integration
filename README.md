# podman-desktop-file-copy-to-user

### !! EM CONSTRUÇÃO !!

## Objetivo
Criar um script que automatize a criação de um atalho (arquivo desktop) na máquina real sempre que for instalado um programa novo no Fedora Silverblue através do toolbox (podman). Será utilizado o processo manual abaixo como base.

## Processo Manual
Pesquisando, descobri que os conteiners da toolbox (podman) ficam em ~/.local/share/containers

Então instalei o blender na toolbox para fazer um teste. Verifiquei que os locais de destino são os seguintes:

- Pasta do arquivo desktop:  
/home/realgrm/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/applications/blender.desktop

- Pasta do ícone:  
/home/realgrm/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/icons/hicolor/scalable/apps/blender.svg

- Então copiei o arquivo desktop renomeando para:  
/home/realgrm/.local/share/applications/toolbox-blender.desktop

No conteúdo do arquivo, modifiquei: 

- A linha do nome do aplicativo  
De: Name=Blender  
Para: Name=Blender (container)

- A linha do comando de execução  
De: Exec=blender %f  
Para: Exec=toolbox run blender %f  

- A linha de definição de ícone:  
De: Icon=blender  
Para: Icon=/home/realgrm/Documents/Links/Fedora Container/usr/share/icons/hicolor/scalable/apps/blender.svg 

## Imagens

#### Arquivo Origem:
![desktop_source](https://user-images.githubusercontent.com/23300290/98545368-252a1e00-2274-11eb-8380-f3c894af5df0.png)

#### Arquivo Destino:
![desktop_destination](https://user-images.githubusercontent.com/23300290/98545365-24918780-2274-11eb-8053-0851b496abdc.png)

#### Menu Libre:
![image](https://user-images.githubusercontent.com/23300290/98615903-6f45ea80-22da-11eb-84a4-cd5f2c7e72cd.png)

#### Overview:
Aplicação rodando e aparecendo na Dash   
![image](https://user-images.githubusercontent.com/23300290/98615310-0ca01f00-22d9-11eb-853a-f9b45b307b42.png)

#### Show Applications:
Aplicação na Dash indica que está rodando, porém nas aplicações não aparece indicador abaixo do ícone  
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)
