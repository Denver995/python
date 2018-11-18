# -*-coding:Latin-1 -*
import os
"""test module that contain fonctions"""
def table(nb, max=10):
	i = 0
	while i<max:
		print(nb, "*", i, "=", nb*i)
		i+=1
if __name__ == '__main__':
	table(14)
	os.system("pause")