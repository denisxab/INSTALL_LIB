# INSTALL_LIB
##########################################

Automatic installation of Python libraries

Fill the dictionary list_libr type 'library name' : 'the command in the console(without pip install)'

"""python
import sys
import INSTALL_LIB
if not INSTALL_LIB.INSTALL_LIB({'all':{'requests':'requests'}}):sys.exit()
"""

#########################################

Автоматическая установка библиотек Python

Заполнить словарь list_libr по типу 'имя библиотеки' : 'команда в консоль(без pip install)'
