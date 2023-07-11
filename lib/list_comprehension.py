#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if n % 2 == 0]
    return even_list

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return sentence_list
    else:
        exlclamation_list = [f"{s}!" for s in sentence_list]
        return exlclamation_list
    