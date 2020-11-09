# podman-desktop-file-copy-to-user

### Resumo:
Sempre que for instalado um programa novo Fedora Silverblue através do toolbox, criar atalho na máquina real.

### Teste inicial
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

### Imagens

#### Arquivo Origem:


#### Arquivo Destino:



### Objetivo:
Automatizar o processo manual acima para cada aplicativo instalado através da toolbox do Fedora Silverblue na imagem do conteiner do Podman
