<h1>DJANGO DEX</h1>

<h2>Descrição</h2>

<p>Django Dex é uma aplicação web escrita em Python usando o framework Django. A aplicação permite visualizar os
    monstrinhos contidos na Nacional Dex até o numero 809, podendo visualizar suas especificidades e linha evolutiva</p>

<h2>Instalação</h2>

<p>Para instalar a Django Dex, siga as etapas abaixo:</p>

<ol>

<li>Clone o repositório do projeto em sua máquina local:</li>
    <pre>git clone https://github.com/mts-lucas/django-dex.git</pre>

<li>Navegue para o diretório do projeto:</li>
    <pre>cd django-dex</pre>

<li>Crie um ambiente virtual para isolar as dependências do projeto:</li>
    <pre>python -m venv venv</pre>

<li>Ative o ambiente virtual:</li>
<ul>
    <li>No Windows:</li>
    <pre>venv\Scripts\activate</pre>
    <li>No Linux/MacOS:</li>
    <pre>source venv/bin/activate</pre>
</ul>

<li>Instale as dependências do projeto:</li>
<pre>pip install -r requirements.txt</pre>

<li>Gere sua SECRET_KEY a partir do seguinte comando no terminal:</li>
<pre>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
</pre>

<li>Crie um arquivo .env na raiz do diretório do projeto e adicione sua SECRET_KEY:</li>
<pre>SECRET_KEY=sua-secret-key-aqui</pre>

<li>Faça as migrações do banco de dados:</li>
<pre>python manage.py migrate</pre>

<li>Crie um superusuário para acessar a interface administrativa:</li>
<pre>python manage.py createsuperuser</pre>

<li>Inicie o servidor de desenvolvimento:</li>
<pre>python manage.py runserver</pre>

<li>Abra o navegador e acesse o endereço http://localhost:8000 para acessar a aplicação.</li>
</ol>

<p>Observação: Certifique-se de manter sua SECRET_KEY segura e nunca a compartilhe publicamente.</p>


<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.</p>