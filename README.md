# Teste para SRE

## Escalabilidade da aplicação.

O desafio consiste em uma API que foi desenvolvida, porém ela precisa estar rodando no Google Cloud Platform (Não se preocupe, daremos acesso a um projeto para você) e a mesma API pode ser melhorada, caso você identifique pontos para tal.

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

## Instruções de entrega

**Obrigatório**:

- Realizar o deploy da aplicação em Produção e a mesma estar funcional em um DNS público.

**Pontos de avaliação**:

- Colocar a aplicação em container;
- Rodar a aplicação em um orquestrador de containers.
- A infraesturutura tem que estar em código;
- Deverá estar implementado em pipeline de CI/CD.
- A API tem pontos de melhoria, se você identificar algo pode implementar a vontade;

**Importante**

Não é necessário implementar todos os pontos listados acima, afinal de contas o objetivo é colocar a API no ar, porém eles serão considerados na sua avaliação.

**Entrega**

Faça o clone deste projeto e realiza o push em um repositório no [Gitlab](https://about.gitlab.com/) ou [Bitbucket](https://bitbucket.org/). E nos dê acesso para que o código seja verificado e também deverá constar no README todos os procedimentos realizados por você para o teste.