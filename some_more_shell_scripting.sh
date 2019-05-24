#!/bin/bash 
aggiungi_utente(){
	echo "Nome utente: $1"
	echo "Cognome utente: $2"
	echo "Username: $3"
	((ID++))	
	return $ID  
}
ID=0
aggiungi_utente Nick Politi nick
echo "ID value $?"

function_scope()
{
	echo "Function parameters are: $@"
	x=2
}
echo "Function parameters are: $@"
x=1
echo "x value is $x"
function_scope Goofy Donald Mickey
echo "x value is $x"

