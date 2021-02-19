# Teste para SRE

## Desafio: Do MVP até a Produção!

A startup XPTO desenvolveu um MVP da sua aplicação que é uma API feita em [Python](https://docs.python.org/3/), usando o framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) e um banco de dados [SQLite](https://www.sqlite.org/index.html) para atender a demanda.

O MVP foi aprovado, e a XPTO recebeu um aporte financeiro para lançar o produto no mercado, e você foi contratado para ser o primeiro SRE do time de Engenharia.

E para sua primeira tarefa, você deve migrar essa aplicação que está no [Heroku](https://www.heroku.com/) para a [AWS](https://aws.amazon.com/).

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

- O principal objetivo é você conseguir implementar essa API na [Amazon Web Services](https://docs.aws.amazon.com/) e rodando em uma URL válida.

**Pontos de avaliação**:

***Entrega Básica***

- "Containerizar" a API (Sugestão: [Docker](https://docs.docker.com));
- Rodar a aplicação em um orquestrador de containers (Sugestão: [Kubernetes](https://kubernetes.io/pt/docs/home/) e [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine));
- A infraestrutura (Redes e Servidores) deve estar em código (Sugestão: [Terraform](https://www.terraform.io/docs/providers/google)).

Esses são os pontos básicos que a XPTO espera na entrega, caso você ache melhor não fazer um dos pontos citados e/ou utilizar outra ferramenta do que as que foram sugeridas, favor justificar o porquê.

***Entrega Intermediária***

Compreende os itens da Entrega Básica e mais os seguintes:

- O deploy da aplicação/infra deverá estar em um pipeline de CI/CD (Sugestões: [Jenkins](https://www.jenkins.io/), [TravisCI](https://travis-ci.org/), [Spinnaker](https://spinnaker.io/));
- Implementação dos charts do Kubernetes com [Helm](https://helm.sh/);
- Ajustar a API para o padrão [REST](https://medium.com/@wssilva.willian/design-de-api-rest-9807a5b16c9f);
- Implementar um outro sistema gerenciador de banco de dados (Sugestão: [PostgreSQL](https://www.postgresql.org/docs/))

Com essa entrega começamos a pensar em um ambiente mais automatizado e mais flexível, caso você ache melhor não fazer um dos pontos citados e/ou utilizar outra ferramenta do que as que foram sugeridas, favor justificar o porquê.

***Entrega Avançada***

Compreende os itens da Entrega Básica e Intermediária, e mais os seguintes:

- Implementação de testes de Infraestrutura (Sugestões: [Molecule](http://molecule.readthedocs.io), [Terratest](https://terratest.gruntwork.io/));
- Implementação de um serviço de Observability (Sugestões: [Prometheus](https://www.prometheus.io/docs/introduction/overview/), [Grafana](https://grafana.com/docs/)).
- Identificação e correção dos possíveis gargalos que a API possui;
- Separação em ambientes (Produção, Homologação, Dev, etc.)

Esta é a entrega completa que a empresa, caso você ache melhor não fazer um dos pontos citados e/ou utilizar outra ferramenta do que as que foram sugeridas, favor justificar o porquê.

*Observação*: Se no ponto de correção dos gargalos, se você quiser reescrever a API em outra linguagem, pode ficar à vontade, só pedimos para justificar o porquê da escolha. 

**Importante**

Os pontos de avalição são itens **obrigatórios** para entrega. Os aspectos avaliados em seu teste serão:

- Qualidade do código de infra;
- Documentação do seu teste;
- O custo envolvido na infra;

**Entrega**

Faça o clone deste projeto e realize o push em um repositório privado no [Gitlab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/) ou [Github](https://github.com/), e nos dê acesso para que o código seja verificado e também deverá constar no README todos os procedimentos realizados por você para o teste. Favor dar acesso aos seguintes emails:

- pery.lemke@nuveo.ai
- matheus.almeida@nuveo.ai

Um ponto importante, você pode não conhecer todas as ferramentas, ou não fazer todos os passos, somente justifique as escolhas para nossa avaliação.

Em caso de dúvidas, não hesite em entrar em contato conosco! :)
