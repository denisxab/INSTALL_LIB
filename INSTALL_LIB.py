# -*- coding: utf-8 -*-
import os
import re
import pip._internal.utils.misc as pip
import sys

#########################################
def insatll_lib(name: str):
    command = f'pip install {name}'
    cash_text = re.findall(re.compile('[^\n-- ]+'), os.popen(command).read())

    if cash_text[0] == 'Requirement':
        return True

    elif cash_text[0] == 'Collecting':
        return False


def chek_libs(list_libr: dict):
    # ASD = os.popen('pip list').read()
    # cash_text = re.findall(re.compile('[^\n-- ]+'), ASD)

    installed_packages_list = sorted(
        ["%s" % i.key for i in pip.get_installed_distributions()])
    return_list = {'ERROR': []}

    for x in list_libr.items():

        if x[0] in installed_packages_list:
            continue

        if not x[0] in installed_packages_list:
            res = (insatll_lib(f'{x[1]}'))
            if not res: 
                return_list['ERROR'].append({x[0]: x[1]})

    # os.system('cls')
    return True if not return_list['ERROR'] else return_list


#########################################

# Заполнить list_libr


def main_64():  # Windows x64

    list_libr = {
        'requests': 'requests',
    }

    return chek_libs(list_libr)


def main_32():  # Windows x32
    list_libr = {
        'requests': 'requests',
    }
    return chek_libs(list_libr)


def main_linux():  # Linux
    list_libr = {
        'requests': 'requests',
    }
    return chek_libs(list_libr)


def main_darwin():  # MacOS
    list_libr = {
        'requests': 'requests',
    }
    return chek_libs(list_libr)

def main ():
    """
    Устанавливайте разные библиотеки для разных платформ
    ----------------------------------------------------
    Install different libraries for different platforms
    """

    if sys.platform == 'win32':  # Windows
        import platform

        if platform.architecture()[0] == '64bit':  # Windows x64
            res = main_64()

        if platform.architecture()[0] == '32bit':  # Windows x32
            res = main_32()

    elif sys.platform == 'linux':  # Linux
        res = main_linux()

    elif sys.platform == 'darwin':  # MacOS
        res = main_darwin()

    print(res)

if __name__ == '__main__':
    main()
    input()
