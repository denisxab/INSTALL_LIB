# -*- coding: utf-8 -*-
import os
import re


def insatll_lib(name:str):
	command = f'pip install {name}'
	cash_text = re.findall(re.compile('[^\n-- ]+'),os.popen(command).read())

	if cash_text[0] == 'Requirement':
		return True

	elif cash_text[0] == 'Collecting':
		return False

def chek_libs(list_libr:dict):
	ASD = os.popen('pip list').read()
	cash_text = re.findall(re.compile('[^\n-- ]+'), ASD)
	return_list = {'ERROR':[]}

	for x in list_libr.items():

		if x[0] in cash_text[2:]:
			continue
			
		if not x[0] in cash_text[2:]:
			res = (insatll_lib(f'{x[1]}'))
			if not res:
				return_list['ERROR'].append({x[0]:x[1]})

	os.system('cls')
	
	if return_list['ERROR'] == []:
		return True

	if return_list['ERROR'] != []:
		return return_list

def main():

	list_libr = {
				'pyperclip':'pyperclip',
				'selenium':'selenium',
				'requests':'requests',
				'win32api':'pypiwin32',
				'pypiwin32':'pypiwin32',
				'Pillow':'Pillow',
				'mss':'mss',
				'opencv-python':'opencv-python',
				'numpy':'numpy',
				'pytesseract':'pytesseract',
				}

	return chek_libs(list_libr)


if __name__ == '__main__':
	print(main())
	input()

