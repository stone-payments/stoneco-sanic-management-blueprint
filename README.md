# Python Management Blueprint

Este repositório contém um projeto desenvolvido em Python3 :heart: para expor uma blueprint com os endpoints necessários das metas de engenharia de TI da Stone.

## Começando...

Estas instruções devem ser suficientes para replicar o ambiente de desenvolvimento para este projeto em seu computador. Caso estas instruções não sejam suficientes, por favor, simplesmente submeta um pull request para este projeto.

## Pré-Requisitos

Após clonar este projeto, para levantar o ambiente de desenvolvimento você vai precisar de Python 3.5.

## Criando um ambiente virtual e instalando dependências

```
python3 -m venv /path/to/new/virtual/environment
source venv/bin/activate
pip install -r requirements.txt
```

## Configurações

Para a configuração do projeto, é esperado que exista um arquivo json com tais informações. Este arquivo é esperado que se encontre no caminho definido pela variável de ambiente CONFIG_FILE_PATH.

Além disso, para que o retorno da saúde do projeto seja coerente, é necessário que cada dependência do projeto seja adicionada via método `register_resource` da classe `AppInfo`. Este método espera receber como argumento uma função que retorna `True` ou `False` de acordo com o estado da saúde da dependência.

## Rodando o projeto

Se tudo não deu errado até aqui, ao executar o arquivo `run.py` no seu computador, será levantada uma API de exemplo com os endpoints desejados devidamente configurados.

## Rodando os testes

Para rodar os testes de unidade, utilize o seguinte comando na raiz do projeto:

`nosetests tests/unit`

Para medir o coverage, utilize o seguinte comando na raiz do projeto:

`nosetests --with-coverage --cover-package=app`


## Feito com

Python 3.5.2

## Autores

Build with :heart: by Team Satisfação do Cliente!

## License

Copyright (C) 2018. Stone Pagamentos. All rights reserved.