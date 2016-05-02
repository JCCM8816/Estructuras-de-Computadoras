#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Tarea1.py
#  
#  Copyright 2016 Jose Carlos <jose.cortesmora@ucr.ac.cr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import math
import sys
from random import randint

# binario(string) recibe un string hexadecimal y 
# lo transforma a binario

def binario(hex_string):
	num_bits = len(hex_string)*4
	binario = bin(int(hex_string, 16))[2:].zfill(num_bits)
	return (binario)

# cache(T_offset, T_index, n_bancos, n_bloques): 
# Es una función que simula el comportamiento de una memoria
# cache con caracteristicas no-write allocate, write through
# y reemplazo aleatorio. Devuelve la cantidad de Hits y Misses obtenidos 

def cache(T_offset, T_index, n_bancos, n_bloques):
	
	Mcache = [[0 for i in range(n_bancos)] for i in range(n_bloques)]  # Memoria Cache inicializada en cero
	hit = 0
	miss = 0
	
	# Apertura y lectura del archivo. Se obtinen los valores del tag y
	# del index
	for archivo in open("aligned.trace"):
		linea = archivo.split()
		hex_string = linea[0]
		Dir_bloque = binario(hex_string) # Conversión hexadecimal - binario
		T_tag=(len(Dir_bloque) - T_offset - T_index)
		tag = Dir_bloque[0:T_tag] # Obtención del Tag
		indext = Dir_bloque[T_tag:]
		index = indext[0:T_index] # Obtención del Index
		mask = 0
	# Mascara utilizada para convertir el index de binario a decimal
		for i in range(T_index):
			mask = 1 + (mask * 2)
			
		index = int(index) & mask  # Conversión binario a decimal del index
		
	# Cache No-write allocate, write through y reemplazo aleatorio: Si 
	# se encuentra la dirección en memoria en la cache, se incrementa
	# el contador de hits. En caso de que no se encuentre, se incrementa
	# el contador de misses y se almacena la dirección en la cache de 
	# manera aleatoria. Este comportamiento es tanto para lecturas como 
	# para escrituras.
		
		for i in range(n_bancos):
			if (Mcache[index][i] == tag):
				hit =hit + 1  # Aumento contador hits
				break
			else:
				if(i == (n_bancos-1)):
					miss = miss + 1 # Aumento contador misses
					Mcache[index][randint(0,i)]=tag  # Reemplazo aleatorio
					
	return(hit,miss)  # Devuelve la cantidad de Hits y Misses obtenidos


def main():
	
	# Control de errores: Cantidad de argumentos erroneo
	if ( len(sys.argv) < 4 ):
		print "NUMERO INCORRECTO DE ARGUMENTOS!!!"
		sys.exit()

	# Lectura de los argumentos
	asoc=sys.argv[1]
	Tcache=int(sys.argv[2])
	Tbloque=int(sys.argv[3])
	
	# Control de errores: Tamaños de Cache y Bloque erroneos
	if((Tcache & Tcache-1)!= 0):
		print("TAMAÑO DE CACHE NO ES UNA POTENCIA DE 2, FAVOR INTENTE CON UN VALOR 2^n")
		sys.exit()
	if((Tbloque & Tbloque-1)!= 0):
		print("TAMAÑO DEL BLOQUE NO ES UNA POTENCIA DE 2, FAVOR INTENTE CON UN VALOR 2^n")
		sys.exit()	
	
	# Obtención del tamaño del offset
	T_offset= int(math.log(Tbloque,2))
	
	# Selección de la asociativilidad e inicializa los valores del tamaño del index 
	# numero de bancos y numeros de bloques, los cuales son necesarios para llamar la
	# la funcion cache
	#
	# Asociatividad Directo
	if(asoc=="Directo"):
		T_index = int(math.log((Tcache/Tbloque),2))
		n_bancos = 1
		n_bloques = Tcache/Tbloque
		(hit,miss) = cache(T_offset,T_index,n_bancos, n_bloques) #Llama a la función cache
		print hit, ",", miss
	else: 
		# Asociatividad 2-way
		if (asoc=="2-way"):
			T_index = int(math.log((Tcache/(Tbloque*2)),2))
			n_bancos = 2
			n_bloques = Tcache/(Tbloque*2)
			(hit,miss) = cache(T_offset,T_index,n_bancos, n_bloques) #Llama a la función cache
			print hit,",", miss
		else:
			#Asociatividad 4-way
			if (asoc=="4-way"):
				T_index = int(math.log((Tcache/(Tbloque*4)),2)) 
				n_bancos = 4
				n_bloques = Tcache/(Tbloque*4)
				(hit,miss) = cache(T_offset,T_index,n_bancos, n_bloques) #Llama a la función cache
				print hit,",", miss
			else:
				print("ASOCIATIVIDAD NO RECONOCIDA")
				sys.exit()
	
	return 0

if __name__ == '__main__':
	main()

