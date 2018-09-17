# Downloads extension list for VSCode from github and creates a bash script to install the extentions

import requests
import os

fileName = "vscodeExtensions.sh"
url = 'https://raw.githubusercontent.com/MatthewJDavis/configs/master/vscode/extension-installs.txt'

try:
    f = open(fileName,"w")
except OSError:
    print('cannot create', fileName)

f.write("#! /bin/bash\n")
response = requests.get(url)
f.write(str(response.text))
f.close()

os.chmod(fileName,0o755)