# INSTALL_LIB
##########################################

Automatic installation of Python libraries

Fill the dictionary INSTALL_LIB.INSTALL_LIB({}) type 'library name' : 'the command in the console(without pip install)'

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

    
#########################################

Автоматическая установка библиотек Python

Заполнить словарь INSTALL_LIB.INSTALL_LIB({}) по типу 'имя библиотеки' : 'команда в консоль(без pip install)'

<h1>Проверка установленных библиотек</h1>

```python
import sys
import INSTALL_LIB
if not INSTALL_LIB.INSTALL_LIB({'all':{'requests':'requests'}}):sys.exit()
```

<h1>Fill pattern</h1>

```python
help(INSTALL_LIB.INSTALL_LIB)
```
