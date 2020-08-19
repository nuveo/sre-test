# Teste para SRE

## Escalabilidade da aplicação.

O desafio consiste em uma API que foi desenvolvida, porém ela precisa estar rodando no [Google Cloud Platform](https://cloud.google.com) e a mesma API pode ser melhorada, caso você identifique pontos para tal.

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

**Objetivo**

- Queremos apenas executar seu código na nossa infraestrutura no [Google Cloud Platform](https://cloud.google.com) e ver sua aplicação funcionar.

**Pontos de avaliação**:

- "Containerizar" a API (Sugestão: [Docker](https://docs.docker.com/));
- Rodar a aplicação em um orquestrador de containers (Sugestão: [Kubernetes](https://kubernetes.io/pt/docs/home/) e [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine));
- A infraesturutura tem que estar em código (Sugestão: [Terraform](https://www.terraform.io/docs/providers/google/));

**Pontos extras**

- A API tem pontos de melhoria, se você identificar algo pode implementar a vontade.

**Importante**

Não é necessário implementar todos os pontos listados acima, afinal de contas o objetivo é colocar a API no ar, porém eles serão considerados na sua avaliação.

**Entrega**

Faça o clone deste projeto e realiza o push em um repositório privado no [Gitlab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/) ou [Github](https://github.com/). E nos dê acesso para que o código seja verificado e também deverá constar no README todos os procedimentos realizados por você para o teste.