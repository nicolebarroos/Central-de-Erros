# Central de Erros
## Api Rest | Projeto Prático AceleraDev | Codenation

![Api](https://user-images.githubusercontent.com/35440249/87815852-ba745300-c83c-11ea-830d-97980b45b213.PNG)

![admin](https://user-images.githubusercontent.com/35440249/87876879-4effc200-c9b1-11ea-9e97-6e9717531c60.PNG)


### Objetivo:

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações

### Instalação:

>git clone https://github.com/Nicolenewsoft/Central-de-Erros.git

### Virtualenv:

>cd central_erros

>pip3 install virtualenv

>virtualenv venv -p python3

>source venv/bin/activate 

### Dependências:

>(venv) pip install -r requirements.txt

### Configurando:
>(venv) python manage.py migrate

>(venv) python manage.py createsuperuser

### Ativando o sistema
>python manage.py runserver

### Informações sobre rotas, autenticação e parâmetros, consulte a documentação via Postman:
[Documentação Postman](https://web.postman.co/collections/11755710-351523bb-050c-435b-8bf7-8e1857e918a5?version=latest&workspace=71e5c54c-7aa9-4739-8bc3-c518376b6765#d59fd70e-0e50-483e-876b-00b6582b869d)
