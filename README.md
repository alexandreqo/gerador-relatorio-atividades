# Gerador Relatório de Atividades

Este script tem como objetivo auxiliar na geração de relatórios de atividades de empresas terceirizadas no Banco do Brasil. O script recebe como parâmetros uma lista de hashes de commits e retorna um texto organizado por extensões, contendo todos os arquivos criados, modificados e deletados. Caso um arquivo seja criado e posteriormente modificado entre os hashes, as modificações não serão contabilizadas.

**Importante**: Este script foi testado apenas em ambientes Linux/WSL. Caso seja utilizado em sistemas Windows, pode ser necessário realizar adaptações.

Uso do script:
Supondo que você tenha salvo o script no diretorio /home
```
python3 /home/gerador-relatorio.py <hash-primeiro-commit> <hash-segundo-commit> <hash-terceiro-commit>
 ```
Exemplo:
```
python3 /home/gerador-relatorio.py bc895ad6a411683f5737d4a4b89e52f54cd2d68c 0983ca286f54935ae88bee331e9d82f05fe79386
```
Retorno:
```
_______________Arquivos Novos_______________
##Arquivos com extensao .html
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-detalhamento-validacao.html#bc895ad6
##Arquivos com extensao .js
diretorio/spec/src/app/services/validacao-service-spec.js#bc895ad6
diretorio/src/app/services/validacao-service.js#bc895ad6
_______________Arquivos Modificados_______________
##Arquivos com extensao .html
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html#0983ca28
diretorio/src/app/spas/fluxo-deploy/fluxo-deploy-app.html#0983ca28
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html#bc895ad6
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy.html#bc895ad6
##Arquivos com extensao .js
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js#bc895ad6
diretorio/spec/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller-spec.js#bc895ad6
diretorio/src/app/spas/fluxo-deploy/fluxo-deploy-app.js#bc895ad6
diretorio/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js#bc895ad6
```
**Importante:** Caso não deseje levantar manualmente todos os hashes dos commits, é possível utilizar o comando abaixo como exemplo. No exemplo abaixo geramos o relatorio com os commits do usuario c1317624 considerando todos os commits após a data 2024-12-01 (yyy=mm-dd) :

```
git log --author="c1317624" --after="2024-12-01" --format="%H" | tr '\n' ' ' | xargs python3 /usr/bin/gerador-relatorio-atividades.py
```

