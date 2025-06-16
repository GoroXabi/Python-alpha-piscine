#!/bin/python3

def array_of_names(persons_dic):
	return [(name.capitalize() + " " + surname.capitalize()) for name, surname in persons.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
