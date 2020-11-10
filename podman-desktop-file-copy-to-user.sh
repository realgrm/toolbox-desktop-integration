#!/bin/bash

# Método proposto:
# OBS: Isto é um esboço, não seguindo a linguagem

# variáveis iniciais
container_id="d0ed434fec06789afb233cd607dee2572efe8f30bf816c7edddc9372b4bd668f"
container_path="${HOME}/.local/share/containers/storage/overlay/${container_id}/"
desktop_source_path="${container_path}/diff/usr/share/applications/"
desktop_destination_path="${HOME}/.local/share/applications/"
icon_path="container_path/diff/usr/share/icons/hicolor/scalable/apps/"


# ------Detectar novo programa instalado------
# Verificar quando houver um novo arquivo em dektop_source_path 
# TRUE: Verificar arquivos com data de modificação nos últimos 5 minutos e guardar nome com extensão em desktop_source_name_ext_list
# OBS: 5 minutos pode ser alterado, escolhido valor alto, para caso sejam criados ou colados mais de um arquivo ao mesmo tempo e caso o script demore até 5min a ser acionado

# Para cada desktop_source_name_ext em desktop_source_name_ext_list 


# verificar se termina com .desktop
	# TRUE: verificar se já existe sua cópia em desktop_destination
		# TRUE: Verificar próximo
		# FALSE: Executar função copy_desktop_file
	# FALSE: verificar próximo 
	
# ------Alternativa: escolher arquivo manualmente------

# Abrir pasta origem
ls -o -tr ${desktop_source_path} | grep ".*\.desktop$" | awk '{print $5.$6,$7,$8}' | tail -15
echo "Últimos 15 alterados, copie e cole aqui o nome com extensão:"
#read desktop_filename
desktop_filename="firefox.desktop"
#xdg-open "${desktop_source_path}${desktop_filename}"


# ------Função copy_desktop_file------

# copiar para aplicações do usuário
desktop_destination_file="${desktop_destination_path}toolbox-${desktop_filename}"
cp "${desktop_source_path}${desktop_filename}" "${desktop_destination_file}"

echo "${desktop_source_path}"

# Comando de execução

before="Exec="
after="Exec=toolbox run "

sed -i "s|${before}|${after}|g" ${desktop_destination_file}

# Caminho para o ícone

before="Icon="
after="Icon=${icon_path}"

sed -i "s|${before}|${after}|g" ${desktop_destination_file}


# ------Fim da função------
