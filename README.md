# INSTALL_LIB
##########################################

Automatic installation of Python libraries

Fill the dictionary list_libr type 'library name' : 'the command in the console(without pip install)'

<h1>Test Programm install Libs</h1>
```python
import sys
import INSTALL_LIB
if not INSTALL_LIB.INSTALL_LIB({'all':{'requests':'requests'}}):sys.exit()
```

<h1>Fill pattern</h1>
```python
help(INSTALL_LIB.INSTALL_LIB)
```
{
'all': {'requests': 'requests'},   # all для всех платформ
'64bit': {'requests': 'requests'}, # Windows 64bit
'32bit': {'requests': 'requests'}, # Windows 32bit
'linux': {'requests': 'requests'}, # Linux
'darwin': {'requests': 'requests'} # MacOS
}
    
#########################################

Автоматическая установка библиотек Python

Заполнить словарь list_libr по типу 'имя библиотеки' : 'команда в консоль(без pip install)'
