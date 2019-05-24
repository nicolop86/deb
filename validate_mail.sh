#!/bin/bash
read email
if [[ $email =~ [[:graph:]]+@[[:alnum:]]+\.[[:alpha:]]+ ]]; then
    echo "$email è un indirizzo email valido!"
else
    echo "$email NON è un indirizzo email valido!"
fi
