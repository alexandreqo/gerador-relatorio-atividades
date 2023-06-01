# Gerador Relatorio de atividades

Este script tem como objetivo auxiliar na geração de relatórios de atividades de empresas terceirizadas no Banco do Brasil. O script recebe como parâmetros uma lista de hashes de commits e retorna um texto organizado por extensões, contendo todos os arquivos criados, modificados e deletados. Caso um arquivo seja criado e posteriormente modificado entre os hashes, as modificações não serão contabilizadas.

Uso do script:
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
