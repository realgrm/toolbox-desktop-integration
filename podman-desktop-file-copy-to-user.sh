#!/bin/bash

# Método proposto:
# OBS: Isto é um esboço, não seguindo a linguagem

# variáveis iniciais
user=realgrm
container_id = d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f
desktop_source_path = "home/" && user && "local/share/containers/storage/overlay/" && container_id &&"/diff/usr/share/applications/"
desktop_destination_path = "home/" && user && "local/share/applications/"
icon_link_path: "/home/" && user && "/.local/share/containers/storage/overlay/d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f/diff/usr/share/icons/hicolor/scalable/apps/"

# ------Detectar novo programa instalado------
# Verificar quando houver um novo arquivo em dektop_source_path 
# TRUE: Verificar arquivos com data de modificação nos últimos 5 minutos e guardar nome com extensão em desktop_source_name_ext_list
# OBS: 5 minutos pode ser alterado, escolhido valor alto, para caso sejam criados ou colados mais de um arquivo ao mesmo tempo e caso o script demore até 5min a ser acionado

# Para cada desktop_source_name_ext em desktop_source_name_ext_list 
desktop_destination = desktop_destination_path && "toolbox-" && desktop_source_name_ext

# verificar se termina com .desktop
	# TRUE: verificar se já existe sua cópia em desktop_destination
		# TRUE: Verificar próximo
		# FALSE: Executar função copy_desktop_file
	# FALSE: verificar próximo 
	
# ------Alternativa: escolher arquivo manualmente------

# Abrir pasta origem
xdg-open desktop_source_path

# Utilizar zenith para pedir o usuário o nome do arquivo (sem extensão), com resultado a variavel desktop_source_name

# Com isto definir o arquivo de origem e destino (com o prefixo toolbox-)
desktop_source = desktop_source_path && desktop_source_name && ".desktop"
desktop_destination = desktop_destination_path && "toolbox-" && desktop_source_name && ".desktop"

# Executar função copy_desktop_file

# ------Função copy_desktop_file------

# copiar para aplicações do usuário
cp desktop_source desktop_destination

# Dentro do arquivo, mudar linha de execução
# Procurar por "\nExec=" e substituir por "Exec= toolbox run"

# Dentro do arquivo, mudar linha de ícone
# Extrair nome do ícone e atribuir a icon_name
# Definir destino do ícone
icon_link = icon_link_path && icon_name && ".svg"
# Substituir linha por "Icon=" && icon_link

# Salvar arquivo destino?

# ------Fim da função------
