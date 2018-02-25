# -*- coding: utf-8 -*-
import sys

from permutation_cipher import PermutationCipher
from permutation_key_provider import PermutationKeyProvider
from table_permutation_cipher import TablePermutationCipher
from table_permutation_key_provider import TablePermutationKeyProvider

print "Обработка и защита данных"
print "Студент группы ПО(м)-71"
print "Горбач Александр"
print "Лабораторная работа №1"
print "Методы перестановки"

print "------------------------------------"
print "Шифрование методом перестановки c одним ключом"

data = u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕВИЧ"

print "Исходные данные: ", data
cipher1 = PermutationCipher(PermutationKeyProvider("permutation_key.json"))

cipher_data = cipher1.encrypt(data)
print "Зашифрованные данные: ", cipher_data

decrypt_data = cipher1.decrypt(cipher_data)
print "Расшифрованные данные: ", decrypt_data

print
print "------------------------------------"
print "Шифрование методом перестановки c двумя ключами"

data = u"ГОРБАЧ_АЛЕКСАНДР_ВИТАЛЬЕВИЧ"

print "Исходные данные: ", data
cipher2 = TablePermutationCipher(TablePermutationKeyProvider("table_permutation_key.json"))

cipher_data = cipher2.encrypt(data)
print "Зашифрованные данные: ", cipher_data

decrypt_data = cipher2.decrypt(cipher_data)
print "Расшифрованные данные: ", decrypt_data
