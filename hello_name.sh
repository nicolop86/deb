#!/bin/bash -x 
echo Please, enter your name and last name:

function saluta {
	echo "Hi, $1 $2"
}
read NAME LASTNAME
saluta $NAME $LASTNAME

echo -en "Come ti chiami?"
read NOME
echo "Il tuo nome è ${NOME=:`whoami`}"
echo "Tutto ok, ${NOME}?"

