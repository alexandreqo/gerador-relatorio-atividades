import subprocess
import sys
import os
import re 
from bdb import set_trace


inputArgs = sys.argv
arquivosNovos = []
arquivosModificados = []


def ordenadorPorExtencao(e):
    set_trace()
    m = re.search('(\b\.\b)(?!.*\1).*', e)
    print('teste')
    if m:
        print(m.group(1))
        return m.group(1)
    return ''
for i in inputArgs[0:]:
    result = subprocess.run(['git show '+i+' --name-status --pretty=oneline --abbrev-commit --diff-filter=A '], capture_output=True, text=True,shell=True).stdout.splitlines() 
    if len(result) >0:
        del result[0]    
        arquivosNovos = arquivosNovos + result
    
      
    

for i in inputArgs[0:]:
    result = subprocess.run(['git show '+i+' --name-status --pretty=oneline --abbrev-commit --diff-filter=M '], capture_output=True, text=True,shell=True).stdout.splitlines() 
    if len(result) >0:
        del result[0]    
        arquivosModificados = arquivosModificados + result 

    
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
    extencao = os.path.splitext(x)[1]
    if extencao != extencaoAnterior:
        extencaoAnterior = extencao ;
        print('##Arquivos com extencao ' + extencaoAnterior)
    print(x)


print('_______________Arquivos Modificados_______________')
extencaoAnterior = ''
for x in arquivosModificados:
    extencao = os.path.splitext(x)[1]
    if extencao != extencaoAnterior:
        extencaoAnterior = extencao ;
        print('##Arquivos com extencao ' + extencaoAnterior)
    print(x)

#[print(x) for x in arquivosNovos]

#print('Arquivos Modificados')

#[print(x) for x in arquivosModificados]
