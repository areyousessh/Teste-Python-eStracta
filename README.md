
# Teste Backend eStracta

Foi proposta a criação de uma Api utilizando Python e Flask aonde tivesse 4 endpoints sendo eles

- /GET -> Aonde fosse chamada uma lista com todas as empresas e que fosse possivel realizar uma paginação com limite de itens por pagina, ordenação e limite de registros
  Ordenação: Adicione o parâmetro sort_by na URL para especificar o campo pelo qual deseja ordenar. Por exemplo, para ordenar pelo campo "nome_fantasia", acesse /companies?sort_by=nome_fantasia.
  Paginação: Adicione os parâmetros page e per_page na URL para controlar a página atual e o número de registros por página, respectivamente. Por exemplo, para mostrar a página 2 com 20 registros por        página, acesse /companies?page=2&per_page=20.
  Os valores padrão para page e per_page são 1 e 10, respectivamente, se você não fornecer esses parâmetros.

- /POST -> Aonde fosse possivel registrar uma nova empresa em que os campos fossem obrigatórios e o model da empresa deveria conter : CNPJ, Nome Razão, Nome Fantasia, CNAE

- /EDIT -> Aonde fosse possivel alterar uma empresa existente mas somente os campos Nome Fantasia e CNAE 

- /DELETE -> Aonde fosse possivel deletar uma empresa utilizando como parametro seu cnpj



### Como testar a aplicação


-  Clonando ele através do comando git clone
-  Ative o virtual env rodando o comando nome_do_ambiente\Scripts\activate caso esteja no windows e source nome_do_ambiente/bin/activate no linux e macOS
-  Executar um pip install -r requirements.txt para instalar as dependencias necessárias
-  Para rodar o projeto utilize o comando python main.py e caso esteja utilizando macOS ou Linux python3 main.py.

- Após isso você precisará do Insomnia e pode consegui-lo em https://insomnia.rest/download
- Instalando ele você pode clicar em create / import / choose a file e selecionar o arquivo insomnia_workspace.json que esta dentro do repositório e clicar em scan e depois import


Se aplicação já estiver rodando você deve ser capaz de executar requests

Todas as informações necessárias dos dados cadastrados das empresas estão no arquivo db.py que é um pequeno dicionário/lista de itens mockados para teste da API 
