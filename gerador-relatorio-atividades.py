import subprocess
import sys
import os
import re 

inputArgs = sys.argv
arquivosNovos = []
arquivosModificados = []
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

for i in inputArgs[0:]:
    result = subprocess.run(['git show '+i+' --name-status --pretty=oneline --abbrev-commit --diff-filter=A | awk \'{print $2}\' |  awk \'{if(NR>1)print}\''], capture_output=True, text=True,shell=True).stdout.splitlines()
    if len(result) >0:
        arquivosNovos = arquivosNovos + list(map(lambda x: foldername + '/' + x + '#' + i[0:8], result))

for i in inputArgs[0:]:
    result = subprocess.run(['git show '+i+' --name-status --pretty=oneline --abbrev-commit --diff-filter=M | awk \'{print $2}\' |  awk \'{if(NR>1)print}\'' ], capture_output=True, text=True,shell=True).stdout.splitlines()
    if len(result) >0:
        arquivosModificados = arquivosModificados + list(map(lambda x: foldername + '/' + x + '#' + i[0:8], result))

arquivosNovos = list(set(arquivosNovos))
arquivosModificados = list(set(arquivosModificados))

for novo in arquivosNovos:
    try:
        arquivosModificados.remove(novo)
    except ValueError:
        pass

arquivosNovos.sort(key=lambda f: os.path.splitext(f)[1])
arquivosModificados.sort(key=lambda f: os.path.splitext(f)[1])


print('_______________Arquivos Novos_______________')
extencaoAnterior = ''
for x in arquivosNovos:
    extencao = os.path.splitext(x)[1].split('#')[0]
    if extencao != extencaoAnterior:
        extencaoAnterior = extencao ;
        print('##Arquivos com extencao ' + extencaoAnterior)
    print(x)


print('_______________Arquivos Modificados_______________')
extencaoAnterior = ''
for x in arquivosModificados:
    extencao = os.path.splitext(x)[1].split('#')[0]
    if extencao != extencaoAnterior:
        extencaoAnterior = extencao ;
        print('##Arquivos com extencao ' + extencaoAnterior)
    print(x)