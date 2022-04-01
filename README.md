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

Faça o clone deste projeto e realize o push em um repositório privado no [Github](https://github.com/), e nos dê acesso para que o código seja verificado. Por favor, lembre-se também de adicionar um documento README que descreve todos os procedimentos realizados por você para o teste. Quanto mais detalhes, melhor!

Os acessos ao repositório podem ser direcionado para os seguintes emails:

- antonio.filho@nuveo.ai
- francilio.araujo@nuveo.ai
- gilson.oliveira@nuveo.ai

**Um ponto importante**: você pode não conhecer todas as ferramentas, ou não fazer todos os passos, porém é muito importante que justifique as suas escolhas e raciocínios para ajudar na nossa avaliação.

Em caso de dúvidas, não hesite em entrar em contato conosco! :)
