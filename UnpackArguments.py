#!/usr/bin/python3.5
def compose_sentence(sub, verb='is', comp='red'):
	"""This function builds up simple sentences"""
	print(sub, verb, comp)

d={'sub':'Tom', 'verb':'has','comp':'a dog'}

compose_sentence(**d)

