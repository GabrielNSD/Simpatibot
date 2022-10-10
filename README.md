# Simpatibot

Esta é a Simpatibot, uma bot para telegram que adiciona os luxos compartilhados no grupo à uma playlist colaborativa no Spotify.

## Packager

A Simpatibot usa o [poetry](https://python-poetry.org/) como packager.  

### Como usar o poetry

1. Instale o poetry em seu SO  
   Linux/OSx/ bashwindows:  
   `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`  
   Windows PowerShell:  
   `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`  

   [Documentação completa](https://python-poetry.org/docs/)

2. No diretório do bot, execute o comando:  
   `poetry install`

## Dependências

- python 3.8  
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- dotenv
- requests

## Contribuindo

1. Faça um fork deste repositório

2. Crie um branch para editar o que achar pertinente  
    `git checkout -b nome-do-branch main`

3. Faça seus commits

4. Abra um PR após testar sua solução

## Executando a Simpatibot

1. Insira as chaves de API no arquivo .env (ver .env.example)

2. Execute o comando:  
`poetry run python script.py`

## API's

- [Spotify](https://developer.spotify.com/documentation/)

## ToDo List

- Finalizar implementação da autenticação do Spotify via Token com refresh automático.
