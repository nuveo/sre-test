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
- A infraestrutura deve que estar em código (Sugestão: [Terraform](https://www.terraform.io/docs/providers/google/));
- O deploy da aplicação/infra deverá estar em um pipeline de CI/CD (Sugestões: [Jenkins](https://www.jenkins.io/) e [TravisCI](https://travis-ci.org/))

**Pontos extras**

- A API tem pontos de melhoria, se você identificar algo pode implementar a vontade.

**Importante**

Os pontos de avalição são itens **obrigatórios** para entrega. Os aspectos avaliados em seu teste serão:

- Qualidade do código de infra;
- Qualidade do descritivo para o seu teste;
- O custo envolvido na infra;

**Entrega**

Faça o clone deste projeto e realize o push em um repositório privado no [Gitlab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/) ou [Github](https://github.com/), e nos dê acesso para que o código seja verificado e também deverá constar no README todos os procedimentos realizados por você para o teste.

Em caso de dúvidas, não hesite em entrar em contato conosco! :)