## Pré-requisitos:
* Python 3.6.
* node
* mysql-client
* git
* ssh (e configurado no github>>settings>>SSH and GPG keys) 


## para o back:
Se possivel trabalhar com env:
* python3 (ou python) -m venv env
* source env/bin/activate (linux) ou env\Scripts\activate (windows)
* pip install -r requirements.txt

No django, abstrai-se a manipulação de tabelas no banco. Colocamos os atributos de cada tabela no api.tutorials.models.py. Há comandos específicos pra foreign keys e outras complexidades, só olhar a documentação. Ao modificar os models, precisa migrar as alteraçoes pro banco:
* python3 (ou python) api/manage.py makemigrations
* python3 (ou python) api/manage.py migrate
Outros lugares que precisamos mexer:
* api.tutorials.serializers.py
* api.tutorials.urls.py (endereços para expor a API)
* api.tutorials.views.py (comportamento de cada verbo HTTP para cada url exposta)

Uma vez que a migração esteja feita, podemos subir nossa API localmente (geralmente vai pro http://127.0.0.1:8000/):
* python3 api/manage.py runserver

Importante: o django vai se comunicar com o banco através de host e porta constante na parte "DATABASES" no api.popcao.settings.py. O default do MySQL é host http://127.0.0.1 e porta 3306.


## para o front:
Preparar a instalação do javascript:
* npm install (existe um arquivo package.json que é semelhante ao requirements.txt do Python/pip)

Dá pra subir localmente de duas formas:
* estando dentro da pasta front, apertar o "Go live" no canto inferior direito do VSCode (sobe em http://127.0.0.1:5500/index.html)
* tambem dentro da pasta front, dar um _npm start_ na linha de comando (sobe em http://127.0.0.1:8081/)
Nesses endereços é possível ver a aplicação no navegador.

from django.db import connection
connection.connect()