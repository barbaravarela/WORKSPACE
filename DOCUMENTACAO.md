# COMANDOS DO DJANGO

1. `pip install django` -> Instala o Django no projeto
2. `django-admin startproject nome_do_projeto .` -> Cria um novo projeto em Django
3. `python manage.py runserver` -> Sobe o servidor
4. `python manage.py startapp nome_do_app` -> Cria um novo app
5. `python manage.py migrate` -> Realiza as migrações (ativa) do projeto
6. `python manage.py createsuperuser` -> Cria um novo super usuário
7. `python manage.py changepassword nome_do_usuario` -> Altera a senha caso você esqueça
8. `python manage.py makemigrations` -> Cria/gera um novo pacote de migração (útil para novo app e alteração no BD)

# TAGS DO DJANGO HTML

1. {% load static %} -> Habilita o static no arquivo. Cada template que usa `{% static %}` precisa ser carregado.
2. {% block title %} -> Insere o título da aba. As páginas filhas trocam.
3. {% block header %} -> O header público (logo + entrar). O `base_logado.html` troca por inteiro.
4. {% block header_actions %} -> Só o botão "entrar". O `login.html` esvazia o bloco.
5. {% include ... %} -> Insere as mensagens e/ou bloco de código.
6. {% block content %} -> O miolo da página, cada filha vai ter seu próprio <main>.

## TAGS DE ROTA
1. {% url 'sistema:medico-list' %} -> Fica nos templates e se refere a uma lista de médiocs que está no app sistema.
2. {% url 'sistema:medico-update' medico.pk %} -> Utilização no template com parâmetro para update do médico.
3. {% url url_voltar %} -> url_voltar é o nome de uma variável que guarda uma lógica de retorno à página anterior.
4. redirect('sistema:medico-list') -> Fica numa view e informa que, quando uma ação for realizada, o usuário será redirecionado.