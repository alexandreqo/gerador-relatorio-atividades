# Gerador Relatorio de atividades

Este projeto tem por objetivo auxiliar na geração de relatorio de atividades, ele retorna os arquivos criados e modificados através dos commits fornecidos como parametros.
Se o arquivo foi criado e então modificado, o modificado será eliminado da listagem.
Os arquivos são retornados organizados através da extenção do arquivo.

# Exemplo
```
python3 /home/stefanini/bin/gerador-relatorio.py  bc895ad6a411683f5737d4a4b89e52f54cd2d68c 0983ca286f54935ae88bee331e9d82f05fe79386
```
Retorno: 

_______________Arquivos Novos_______________
##Arquivos com extencao .html
A	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-detalhamento-validacao.html
##Arquivos com extencao .js
A	spec/src/app/services/validacao-service-spec.js
A	src/app/services/validacao-service.js
_______________Arquivos Modificados_______________
##Arquivos com extencao .html
M	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html
M	src/app/spas/fluxo-deploy/fluxo-deploy-app.html
M	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/modais/modal-erros-validacao.html
M	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy.html
##Arquivos com extencao .js
M	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js
M	spec/src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller-spec.js
M	src/app/spas/fluxo-deploy/fluxo-deploy-app.js
M	src/app/spas/fluxo-deploy/implantacao-jobs-datastage/solicitacao/solicitacao-deploy-controller.js
