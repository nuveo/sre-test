# Teste para SRE

## Campos da API

|Name|Type|Description|
|-|-|-|
|id|id|payment unique identifier|
|status|Enum(inserted, consumed)|payment status status|
|data|JSONB|payment input|
|payment|float(XX.XXX,XX)|value of payment

## Endpoints

|Verb|URL|Description|
|-|-|-|
|POST|/create|insert a payment on database|
|PUT|/update/{id}|update status from specific payment|
|GET|/list|list all payments|
|DELETE|/delete/{id}|delete a specific payment|
|GET|/status|healthcheck of API|

## Entrega

Faça o clone deste projeto e realize o push em um repositório privado no [Gitlab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/) ou [Github](https://github.com/), e nos dê acesso para que o código seja verificado e também deverá constar no README todos os procedimentos realizados por você para o teste. Favor dar acesso aos seguintes emails:

- pery.lemke@nuveo.ai
- matheus.almeida@nuveo.ai

Um ponto importante, você pode não conhecer todas as ferramentas, ou não fazer todos os passos, somente justifique as escolhas para nossa avaliação.

Em caso de dúvidas, não hesite em entrar em contato conosco! :)
