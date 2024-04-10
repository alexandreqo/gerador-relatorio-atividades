import subprocess
import sys
import os

inputArgs = sys.argv[1:]
arquivosNovos = []
arquivosModificados = []
dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

for i in inputArgs:
    command_git_show = ['git', 'show', i, '--name-status', '--pretty=oneline', '--abbrev-commit', '--diff-filter=A']
    command_awk = ['awk', '{print $2}']
    command_awk_skip_first = ['awk', '{if(NR>1)print}']

    git_show_result = subprocess.run(command_git_show, capture_output=True, text=True).stdout
    awk_result = subprocess.run(command_awk, input=git_show_result, capture_output=True, text=True).stdout
    awk_skip_first_result = subprocess.run(command_awk_skip_first, input=awk_result, capture_output=True, text=True).stdout

    result = awk_skip_first_result.splitlines()
    print(result)
    if len(result) > 0:
        arquivosNovos += [foldername + '/' + x + '#' + i[:10] for x in result]

for i in inputArgs:
    command_git_show = ['git', 'show', i, '--name-status', '--pretty=oneline', '--abbrev-commit', '--diff-filter=M']
    command_awk = ['awk', '{print $2}']
    command_awk_skip_first = ['awk', '{if(NR>1)print}']

    git_show_result = subprocess.run(command_git_show, capture_output=True, text=True).stdout
    awk_result = subprocess.run(command_awk, input=git_show_result, capture_output=True, text=True).stdout
    awk_skip_first_result = subprocess.run(command_awk_skip_first, input=awk_result, capture_output=True, text=True).stdout

    result = awk_skip_first_result.splitlines()
    if len(result) > 0:
        for modificado in set([foldername + '/' + x + '#' + i[:10] for x in result]):
            if modificado.split('#')[0] not in [x.split('#')[0] for x in arquivosModificados]:
                arquivosModificados.append(modificado)

arquivosNovos = list(set(arquivosNovos))
arquivosModificados = list(set(arquivosModificados))

for novo in arquivosNovos:
    for modificado in arquivosModificados:
        if novo.split('#')[0] == modificado.split('#')[0]:
            arquivosModificados.remove(modificado)

arquivosNovos.sort(key=lambda f: os.path.splitext(f)[1])
arquivosModificados.sort(key=lambda f: os.path.splitext(f)[1])

print('_______________Arquivos Novos_______________')
extensao_anterior = ''
for x in arquivosNovos:
    extensao = os.path.splitext(x)[1].split('#')[0]
    if extensao != extensao_anterior:
        extensao_anterior = extensao
        print('##Arquivos com extensao ' + extensao_anterior)
    print(x)

print('_______________Arquivos Modificados_______________')
extensao_anterior = ''
for x in arquivosModificados:
    extensao = os.path.splitext(x)[1].split('#')[0]
    if extensao != extensao_anterior:
        extensao_anterior = extensao
        print('##Arquivos com extensao ' + extensao_anterior)
    print(x)
