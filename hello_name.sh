#!/bin/bash
echo Please, enter your name and last name:

function saluta {
	echo "Hi, $1 $2"
}
read NAME LASTNAME
saluta $NAME $LASTNAME
