# podman-desktop-file-copy-to-user

### !! EM CONSTRUÇÃO !!

## Objetivo
Criar um script que automatize a criação de um atalho (arquivo desktop) na máquina real sempre que for instalado um programa novo no Fedora Silverblue através do toolbox (podman). Será utilizado o processo manual abaixo como base.

## Processo Manual
Pesquisando, descobri que os conteiners da toolbox (podman) ficam em ~/.local/share/containers

Então instalei o blender na toolbox para fazer um teste. Verifiquei que os locais de destino são os seguintes:

Pasta do arquivo desktop:
/home/realgrm/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/applications/blender.desktop

Pasta do ícone:
/home/realgrm/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/icons/hicolor/scalable/apps/blender.svg

Então copiei o arquivo desktop renomeando para:
/home/realgrm/.local/share/applications/toolbox-blender.desktop

No conteúdo do arquivo, modifiquei a linha de execução
De: Exec=blender %f
Para: Exec=toolbox run blender %f

E de ícone
De:Icon=blender
Para:Icon=/home/realgrm/Documents/Links/Fedora Container/usr/share/icons/hicolor/scalable/apps/blender.svg

## Imagens

#### Arquivo Origem:
![desktop_source](https://user-images.githubusercontent.com/23300290/98545368-252a1e00-2274-11eb-8380-f3c894af5df0.png)

#### Arquivo Destino:
![desktop_destination](https://user-images.githubusercontent.com/23300290/98545365-24918780-2274-11eb-8053-0851b496abdc.png)

#### Menu Libre:
![desktop-menulibre](https://user-images.githubusercontent.com/23300290/98501705-becedc80-222e-11eb-8ae8-3fd64bad47d4.png)
