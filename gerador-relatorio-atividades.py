import subprocess
import sys
import os

inputArgs = sys.argv
arquivosNovos = []
arquivosModificados = []
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

commits = subprocess.check_output('git log  --author={} --after={} --pretty=format:%h --abbrev=10'.format(inputArgs[1:][0],inputArgs[1:][1])).decode().splitlines()
for commit in commits:
    result = subprocess.check_output('git diff-tree --no-commit-id --diff-filter=A --name-only -r '+commit ).decode().splitlines()
    if len(result) >0:
        arquivosNovos = arquivosNovos + list(map(lambda x: foldername + '/' + x + '#' + i[0:10], result))

for commit in commits:
    result = subprocess.check_output('git diff-tree --no-commit-id --diff-filter=M --name-only -r '+commit ).decode().splitlines()
    if len(result) >0:
        for modificado in set(list(map(lambda x: foldername + '/' + x + '#' + i[0:10], result))):
            if list(map(lambda x: x.split('#')[0], arquivosModificados)).count(modificado.split('#')[0]) == 0:
                arquivosModificados.append(modificado)

arquivosNovos = list(set(arquivosNovos))
arquivosModificados = list(set(arquivosModificados))

for novo in arquivosNovos:
    try:
        for modificado in arquivosModificados:
            if novo.split('#')[0] == modificado.split('#')[0]:
                arquivosModificados.remove(modificado)
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