# Gerador Relatorio de atividades

Esste auxilia na geração de relatorio de atividades de empresas terceirizadas no Banco do Brasil, retornando um texto com arquivos criados e modificados que estão entre o primeiro e ultimo commit fornecidos nos argumentos.
Se o arquivo foi criado e então modificado, o modificado será eliminado da listagem.
Os arquivos são retornados organizados através da extensão do arquivo.

Este script auxilia na geração de relatorio de atividades de empresas terceirizadas no Banco do Brasil.
O script recebe como parametros uma lista de hashs de commits e retorna um texto organizado por extensões com todos os arquivos criados, modificados e deletados, se um arquivo entre os hashes for criado e depois modificado, as modificações não serão contabilizadas.

Dentro do repositorio:

```
python3 /home/gerador-relatorio.py  <hash-primeiro-commit> <hash-segundo-commit>
 <hash-terceiro-commit>
 ```
 Exemplo:
```
python3 /home/gerador-relatorio.py  bc895ad6a411683f5737d4a4b89e52f54cd2d68c 0983ca286f54935ae88bee331e9d82f05fe79386
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
