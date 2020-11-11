# podman-desktop-file-copy-to-user

### !! UNDER CONSTRUCTION !!

## Goal
Create a script that automates the creation of a shortcut (desktop file) on the real machine whenever a new program is installed on Fedora Silverblue through the toolbox (podman).  
The manual process below will be used as the basis.

## Manual Process
Searching, I found that the containers of the toolbox (podman) are in ~/.local/share/containers


So I installed blender in the toolbox to do a test.  I have verified that the destination locations are as follows:

- Desktop file folder:  
~/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/applications/blender.desktop

- Icon folder:  
~/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/icons/hicolor/scalable/apps/blender.svg

- So I copied the desktop file renaming it to:  
~/.local/share/applications/toolbox-blender.desktop

In the content of the file, I modified:

- The application name line
From: Name=Blender
To: Name=Blender (container)

- The execution command line
From: Exec=blender% f
To: Exec=toolbox run blender% f

- The icon definition line:
From: Icon=blender
To: Icon=/home/realgrm/Documents/Links/Fedora Container/usr/share/icons/hicolor/scalable/apps/blender.svg 

 ## Images

#### Source File:
![desktop_source](https://user-images.githubusercontent.com/23300290/98545368-252a1e00-2274-11eb-8380-f3c894af5df0.png)

#### Destination file:
![desktop_destination](https://user-images.githubusercontent.com/23300290/98545365-24918780-2274-11eb-8053-0851b496abdc.png)

#### Menu Libre:
![image](https://user-images.githubusercontent.com/23300290/98615903-6f45ea80-22da-11eb-84a4-cd5f2c7e72cd.png)

#### Overview:
App os running and in the Dash   
![image](https://user-images.githubusercontent.com/23300290/98615310-0ca01f00-22d9-11eb-853a-f9b45b307b42.png)

#### Show Applications:
App icon in Dash indicates that it is running, however in the Apo Grid there is no indicator below the icon
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)


# Em português do Brasil (pt-br)

### !! EM CONSTRUÇÃO !!

## Objetivo
Criar um script que automatize a criação de um atalho (arquivo desktop) na máquina real sempre que for instalado um programa novo no Fedora Silverblue através do toolbox (podman).  
Será utilizado o processo manual abaixo como base.


## Processo Manual
Pesquisando, descobri que os conteiners da toolbox (podman) ficam em ~/.local/share/containers

Então instalei o blender na toolbox para fazer um teste. Verifiquei que os locais de destino são os seguintes:

- Pasta do arquivo desktop:  
~/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/applications/blender.desktop

- Pasta do ícone:  
~/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/icons/hicolor/scalable/apps/blender.svg

- Então copiei o arquivo desktop renomeando para:  
~/.local/share/applications/toolbox-blender.desktop

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
Aplicação na Dash indica que está rodando, porém nas Grade de aplicativos não aparece indicador abaixo do ícone  
![image](https://user-images.githubusercontent.com/23300290/98615618-d616d400-22d9-11eb-8fce-3e3d3c09ffaa.png)
