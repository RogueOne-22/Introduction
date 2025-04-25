#!/bin/bash

#Navegación
cd
pwd
ls -l

#Crear Directorios
mkdir Practica_Linuxcp
cd Practica_Linux
mkdir Documentos
mkdir Backup
ls -l

#Navegación
cd Documentos
touch nota.txt 	
nano nota.txt
#"Hola este es mi primer archivo en Linux
cp 'nota.txt' /home/paula/Practica_Linux/Backup
mv nota.txt nota_final.txt

#Eliminar y ver contenido
cd
rm -r Backup
cat nota_final.txt

#Permisos
chmod 600 nota_final.txt
ls -l
chmod u+rw nota_final.txt

#Buscar y filtar
find ~ -name "nota_final.txt"
#Dentro del directorio Documentos 
grep -is Linux *.txt

#Procesos
htop 
q

Sleep 300&
Kill #PID

#paquetes
sudo apt install update
sudo apt install Cowsay

#Parte final
mkdir logs
cd Practica_Linux
cd Documentos
mkdir logs
ls
touch ejemplo.txt date
date > logs/fecha.txt
cowsay -f stegosaurus "Ejercicio completado!"








