# Gerador Relatorio de atividades

Este script auxilia na geração de relatorio de atividades de empresas terceirizadas no Banco do Brasil.
O script recebe como parametros a chave do usuario e uma data, retornando um texto organizado por extensões com todos os arquivos criados, modificados e deletados, se um arquivo entre os hashes for criado e depois modificado, as modificações não serão contabilizadas.

Dentro do repositorio:

```
python3 /home/gerador-relatorio.py  <chave-usuario> <data>

 ```
 Exemplo:
```
python3 /home/gerador-relatorio.py  c12345678 2022-09-01
```
Retorno: 
```
_______________Arquivos Novos_______________
##Arquivos com extencao .java
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/exceptions/ChavesMonitoradasSistemaTest.java#04264b956c
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/MensagemDaoMock.java#620412715e
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/MensagemServiceMock.java#620412715e
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/MensagemServiceTest.java#620412715e
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/rest/Op6889254v1Test.java#735abef4a7
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/mock/MensagemServiceMock.java#735abef4a7
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/health/StartupHealthCheck.java#735abef4a7
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/health/HealthCheckTest.java#735abef4a7
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/service/MensagemServiceTest.java#735abef4a7
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/mock/MensagemDaoMock.java#735abef4a7
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/dao/MensagemDaoTest.java#735abef4a7
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/dao/MensagemDao.java#acd73d893a
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/models/MensagemEntity.java#acd73d893a
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/services/MensagemService.java#acd73d893a
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/exceptions/GenericException.java#d0ee4b6bd4
_______________Arquivos Modificados_______________
swf-consultar-mensagens-iso/.classpath#b46630269e
##Arquivos com extencao .java
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/exceptions/ChavesMonitoradasSistema.java#d0ee4b6bd4
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/exceptions/ErrosSistema.java#d0ee4b6bd4
swf-consultar-mensagens-iso/src/main/java/br/com/bb/swf/rest/Op6889254v1.java#d275c80e9f
swf-consultar-mensagens-iso/src/test/java/br/com/bb/swf/Op6889254v1Test.java#eb3c40a836
##Arquivos com extencao .properties
swf-consultar-mensagens-iso/src/main/resources/application.properties#1048233d3c
##Arquivos com extencao .sql
swf-consultar-mensagens-iso/src/test/resources/scripts/carga_testes.sql#04264b956c
##Arquivos com extencao .xml
swf-consultar-mensagens-iso/pom.xml#8db2e0992e
##Arquivos com extencao .yaml
swf-consultar-mensagens-iso/run/docker-compose.yaml#a88e23107b

```
