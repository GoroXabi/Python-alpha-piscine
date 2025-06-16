#!/bin/python3

def find_the_redheads(persons_dic):

	return list(filter(lambda name: persons_dic[name] == "red", persons_dic.keys()))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

