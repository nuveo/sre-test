# Teste para SRE

O principal objetivo deste teste é conseguir organizar a infraestrutura base da API disponibilizada (neste repositório) para consumo público, sendo executada no ambiente em nuvem AWS EKS.

Os níveis de entrega abaixo indicam quais os conhecimentos demonstrados para a resolução do problema. Pedimos que se atenha aos itens indicados para poder mostrar as suas capacidades técnicas para nós. Quanto mais itens estiverem cobertos na sua demonstração, maior será o nível considerado na sua avaliação.

_**Dica 1:**_ _Gostamos muito da descrição da solução de forma bem detalhada, além de também apreciar um código bem estruturado e raciocínio lógico._

_**Dica 2:**_ _Se você quiser reescrever a API e/ou arquitetura, fique à vontade, porém explique em detalhes a justificativa e qual o raciocínio aplicado._

_**Dica 3:**_  _Pontos de conhecimento avançado podem ser apresentados tanto em forma de código ou de forma demonstrativa, fazendo uma explicação do raciocínio. Aplique o que achar mais relevante para cada caso._

## Entrega básica
 - Criar o EKS e um repositório no ECR;
 - Adicionar uma zona sre-test.nuveo.ai no Route53;
 - Criar a API com uso de containers;
 - Manifestos para execução deste container no EKS;
 - Realizar o build e push do container para o ECR em um sistema de CI e realizar o deploy do mesmo para o EKS;
 - Fazer com que sre-test.nuveo.ai seja resolvido para a API;
 - Conhecimentos básicos sobre IaC;
 - Conhecimentos básico sobre Ingress;
 - Documentação de como executar o CI;

## Entrega intermediária
 - Itens contidos na Entrega básica;
 - Conhecimentos avançados sobre IaC;
 - Criar VPC por IaC;
 - Criar EKS e ECR por IaC;
 - Criar zona no Route53 por IaC;
 - IAM para execução do IaC;
 - Empacotar os manifestos kubernetes;
 - Conceitos e aplicações básicas de métricas da API;
 - Conhecimentos avançados sobre Ingress e Ingress controller;
 - Sugestões de melhoria da arquitetura;
 - Documentação de IaC;
 - Documentação das métricas;

## Entrega avançada
 - Itens contidos na Entrega básica e intermediária;
 - Conhecimentos avançados sobre Teste de fumaça da API;
 - Conhecimentos avançados sobre Teste de carga da API;
 - Conhecimentos avançados sobre Teste de resiliência da API;
 - Conhecimentos básicos sobre scan de segurança do container, do cluster e do código de infraestrutura;
 - Documentação do teste de fumaça;
 - Documentação do teste do código IaC;
 - Documentação do scan de segurança;
 
## Ferramentas sugeridas
 - Build de container: docker
 - Sistema de CI/CD: TravisCI, Jenkins ou Github Actions
 - IaC: Terraform, CloudFormation ou CDK
 - Empacotamento de manifestos: Kustomize ou Helm
 - Métricas: Prometheus stack
 - Ingress controller: nginx
 - Teste de fumaça: k6
 - Scan de segurança: Trivy, kube-bench, checkov ou tfsec

# Campos da API

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

Faça o clone deste projeto e realize o push em um repositório privado no [Github](https://github.com/), e nos dê acesso para que o código seja verificado. Por favor, lembre-se também de adicionar um documento README que descreve todos os procedimentos realizados por você para o teste, incluindo raciocínios e lógica que foi pensada. Quanto mais detalhes, melhor!

Os acessos ao repositório podem ser direcionado para os seguintes emails:

- diego.gonzales@nuveo.ai
- francilio.araujo@nuveo.ai

**Um ponto importante**: você pode não conhecer todas as ferramentas, ou não fazer todos os passos, porém é muito importante que justifique as suas escolhas e raciocínios para ajudar na nossa avaliação.

Em caso de dúvidas, não hesite em entrar em contato conosco! :nerd_face:
