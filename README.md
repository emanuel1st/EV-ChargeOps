# EV ChargeOps

## Integrantes

###### _Emanuel Rocha Monteiro_ - _RM569895_

## Introdução

## Frente 1 - Contexto e Problema

### Infraestrutura de Recarga Compartilhada

A infraestrutura de recarga compartilhada permite que vários usuários utilizem os mesmos carregadores de veículos elétricos em locais como condomínios, empresas e universidades. Esse modelo utiliza sistemas de gerenciamento para controlar o acesso, registrar o consumo individual e garantir uma distribuição eficiente da energia entre os usuários.

Com o crescimento da frota de veículos elétricos no Brasil, a demanda por pontos de recarga aumenta constantemente. Nesse cenário, a recarga compartilhada surge como uma solução prática e econômica, embora ainda existam desafios relacionados à capacidade da infraestrutura elétrica, aos custos de adaptação e à criação de modelos justos de cobrança e rateio do consumo.

### Funcionamento de uma Sessão de Recarga

Uma sessão de recarga de veículo elétrico gera diversos dados que permitem acompanhar todo o processo de carregamento. Entre as principais informações registradas estão a identificação do usuário, o carregador utilizado, o consumo total de energia em quilowatt-hora (kWh), a potência utilizada durante a sessão e o tempo total de recarga. Esses dados possibilitam monitorar o uso da infraestrutura e entender os padrões de consumo dos usuários.

Além das informações de consumo, também são registrados os horários de início e término da sessão, os níveis de carga da bateria antes e após a recarga, os valores utilizados para cobrança e o custo total da operação. O sistema ainda pode armazenar informações sobre falhas, interrupções e o status de comunicação do equipamento. Esses registros são fundamentais para realizar cobranças justas, gerar relatórios de utilização e garantir uma gestão eficiente dos carregadores compartilhados.

### Modelos de Negócio

Existem diferentes modelos de cobrança utilizados em infraestruturas de recarga de veículos elétricos. Os mais comuns são a cobrança por kWh consumido, em que o usuário paga pela quantidade de energia utilizada; a cobrança por tempo de conexão, baseada na duração da sessão de recarga; e a tarifa fixa, que aplica um valor único por sessão independentemente do consumo. Além desses modelos, algumas redes também oferecem planos de assinatura mensal ou disponibilizam recargas gratuitas como estratégia para atrair clientes.

No Brasil, a cobrança por tempo e por kWh já é amplamente utilizada em eletropostos públicos, estacionamentos e condomínios. Em países com maior maturidade na mobilidade elétrica, como Estados Unidos e países da Europa, também são adotados modelos semelhantes, incluindo tarifas por energia consumida, por tempo de uso e mensalidades. Entre os modelos existentes, a cobrança por kWh é considerada uma das mais justas, pois relaciona diretamente o valor pago à quantidade de energia efetivamente consumida pelo veículo.

### Opção A - Análise de Mercado

#### ChargePoint

##### Problema que resolve:
A ChargePoint oferece uma solução para gerenciamento de estações de recarga de veículos elétricos em ambientes públicos, corporativos e residenciais, permitindo o controle do uso e do consumo de energia pelos usuários.

##### Principais funcionalidades:

- Monitoramento remoto das estações de recarga;
- Controle de acesso de usuários;
- Relatórios de consumo e utilização;
- Gestão de pagamentos e cobranças;
- Aplicativo para localização e uso dos carregadores.

##### Modelo de negócio:
Venda de carregadores e oferta de serviços de software para monitoramento e gestão da infraestrutura de recarga.

##### Limitações:
Alguns recursos avançados dependem de assinatura da plataforma e a solução pode apresentar custos elevados para instalações de pequeno porte.

#### Wallbox Pulsar Plus

##### Problema que resolve:
A Wallbox busca simplificar o gerenciamento da recarga de veículos elétricos em residências, condomínios e empresas, oferecendo controle inteligente do carregamento e do consumo energético.

##### Principais funcionalidades:

- Controle da recarga por aplicativo móvel;
- Programação de horários de carregamento;
- Monitoramento do consumo de energia;
- Ajuste de potência conforme a disponibilidade elétrica;
- Acompanhamento em tempo real das sessões.

##### Modelo de negócio:
Comercialização de carregadores inteligentes e serviços digitais para monitoramento e gerenciamento das recargas.

##### Limitações:
Algumas funcionalidades dependem de conexão constante com a internet e podem exigir integração com outros sistemas para utilização completa.

#### Zaptec

##### Problema que resolve:
A Zaptec é voltada para ambientes com múltiplos usuários, como condomínios e estacionamentos compartilhados, oferecendo gerenciamento centralizado e distribuição eficiente da energia disponível.

##### Principais funcionalidades:

Balanceamento inteligente de carga;
Controle individual de usuários;
Monitoramento remoto;
Relatórios detalhados de utilização;
Gestão de múltiplos carregadores simultaneamente.

##### Modelo de negócio:
Venda de equipamentos e licenciamento da plataforma de gerenciamento e monitoramento.

##### Limitações:
Pode exigir infraestrutura específica para aproveitar todos os recursos disponíveis e possui maior dependência do ecossistema da própria fabricante.

#### Análise Comparativa

Após a análise das soluções estudadas, foi possível observar que todas possuem funcionalidades voltadas para o monitoramento das sessões de recarga, controle de usuários e acompanhamento do consumo de energia. Além disso, oferecem ferramentas que facilitam a gestão da infraestrutura e permitem maior controle sobre a utilização dos carregadores.

Entretanto, identificou-se que muitas dessas soluções são focadas principalmente na operação dos equipamentos e na cobrança das recargas. Com base nessa análise, a proposta do EV ChargeOps é combinar o gerenciamento das sessões de recarga com um sistema de rateio transparente e recursos de inteligência artificial capazes de gerar previsões de consumo, identificar padrões de utilização e fornecer informações estratégicas para gestores e usuários da infraestrutura compartilhada.

## Frente 2 - Base Regulatória e Técnica

### Resolução ANEEL 1000/2021

A Resolução Normativa ANEEL nº 1.000/2021 estabelece as regras gerais do fornecimento de energia elétrica no Brasil e inclui diretrizes importantes para a operação de pontos de recarga de veículos elétricos. A norma permite a exploração comercial da recarga dentro da própria unidade consumidora, inclusive com possibilidade de cobrança de terceiros, sem que isso seja caracterizado como atividade de distribuição de energia. Além disso, a ANEEL não define valores máximos ou tabelamento para esse serviço, deixando o preço da recarga livre para negociação entre as partes envolvidas.

Outro ponto relevante da norma é o incentivo à padronização e interoperabilidade dos sistemas, especialmente em equipamentos de uso compartilhado ou não exclusivamente privado. Isso inclui a recomendação de utilização de protocolos abertos de comunicação, permitindo integração entre diferentes fabricantes e plataformas de gestão. Também é exigido que instalações de carregadores sigam as normas técnicas da distribuidora local, principalmente em casos de aumento de carga ou adequações na infraestrutura elétrica, podendo haver necessidade de comunicação prévia para garantir a segurança e conformidade do sistema elétrico.

### Carregador GoodWe HCA G2

O carregador GoodWe HCA G2 possui diversas interfaces de comunicação que permitem sua integração com sistemas de gestão de energia e monitoramento remoto, especialmente por meio da plataforma SEMS+. As conexões Wi-Fi e LAN (Ethernet) são responsáveis por ligar o equipamento à internet, permitindo o acompanhamento em tempo real das sessões de recarga, consumo de energia, status do carregador e configuração de funcionalidades como agendamento de carga e atualização remota de firmware. Além disso, essas conexões permitem que o sistema otimize o uso de energia, priorizando, quando disponível, a energia proveniente de fontes renováveis como sistemas fotovoltaicos.

Outra interface importante é o Bluetooth, utilizado principalmente para configuração inicial do equipamento e controle local via aplicativo, sendo útil em situações em que ainda não há conexão com a internet. Já a comunicação RS-485 possibilita integração direta e física com outros componentes do sistema energético, como inversores, baterias e medidores inteligentes, permitindo uma gestão mais precisa da energia e geração de relatórios detalhados de consumo. Por fim, a tecnologia RFID é utilizada para controle de acesso dos usuários, garantindo que apenas pessoas autorizadas iniciem sessões de recarga, além de permitir o registro individualizado do consumo para fins de controle e cobrança.

### API SEMS Portal

A API do portal GoodWe SEMS fornece dados operacionais e métricas de desempenho dos dispositivos conectados, incluindo carregadores de veículos elétricos (EV), ampliando o ecossistema originalmente focado em inversores solares. Por meio de endpoints específicos, como o EvChargerDetail, é possível acessar informações em tempo real sobre o funcionamento do carregador, permitindo monitoramento remoto e integração com sistemas externos de gestão de energia.

Entre os principais dados disponibilizados estão o status do carregador (como ocioso, carregando ou aguardando veículo), a potência instantânea de carregamento (kW) e a energia total entregue durante a sessão (kWh). A API também fornece dados detalhados de sessões de recarga, incluindo histórico de uso, eventos operacionais e relatórios de desempenho diário, permitindo uma análise completa do comportamento de utilização dos carregadores. O acesso a essas informações requer uma conta corporativa na plataforma SEMS e autorização para uso da API oficial da GoodWe.

### Opção C - APIs Complementares

## Frente 3 - Arquitetura e IA

### Arquitetura Proposta

### Fluxo dos Dados

### Modelo de Rateio

### Opção A: Benchmarking de Modelos de Rateio

Em condomínios que utilizam carregadores compartilhados, o princípio mais comum é que apenas os usuários que utilizam o serviço paguem pela energia consumida, sem geração de lucro sobre o fornecimento, apenas reembolso do custo da energia. Para isso, é necessário medir de forma precisa o consumo de cada sessão e associar esse uso a um morador específico.

Na prática, isso é feito principalmente de duas formas: por sistemas de gestão inteligente, nos quais o usuário é identificado via aplicativo ou RFID e o consumo em kWh é registrado automaticamente e cobrado posteriormente; ou por medição individualizada, com o uso de um medidor dedicado ao ponto de recarga, que registra o consumo total do equipamento para posterior divisão ou cobrança conforme o uso.

#### Modelo 1 – Rateio por consumo individual via sistema inteligente (app/RFID)

Nesse modelo, cada usuário é identificado digitalmente ao iniciar a recarga, e o sistema registra exatamente o consumo de energia (kWh) por sessão. Esses dados são enviados para uma plataforma que consolida os valores e realiza a cobrança proporcional ao uso.

##### Vantagens:

- Cobrança precisa e proporcional ao consumo real;
- Alta transparência para os usuários;
- Automação do processo de cobrança;
- Escalável para muitos usuários e carregadores.

##### Limitações:

- Depende de infraestrutura tecnológica (software + conectividade);
- Requer integração com o carregador e sistema de autenticação;
- Pode ter custo inicial mais alto de implementação.

#### Modelo 2 – Medição individualizada por medidor físico

Nesse modelo, um medidor de energia é instalado exclusivamente para o ponto de recarga ou para o sistema de carregadores do condomínio. O consumo total é registrado e posteriormente rateado entre os usuários conforme regras definidas pelo condomínio.

##### Vantagens:

- Simplicidade de entendimento e implementação;
- Funciona mesmo sem sistemas digitais avançados;
- Boa confiabilidade na medição de energia.

##### Limitações:

- Não permite rastreamento detalhado por usuário;
- Menor controle sobre sessões individuais;
- Rateio pode se tornar menos justo em casos de uso desigual.
- Comparação e escolha do modelo

#### Comparação e escolha do modelo
A análise dos modelos mostra que sistemas baseados em identificação do usuário e medição individual por sessão são mais eficientes e justos, pois permitem rastrear exatamente quanto cada pessoa consumiu. Já o modelo baseado em medidor físico, apesar de simples, perde granularidade e dificulta a individualização do consumo.

Para o EV ChargeOps, será adotado o modelo de rateio por consumo individual via sistema inteligente (app/RFID), pois ele se integra diretamente com a proposta da plataforma, permite automação do processo de cobrança e possibilita a aplicação de inteligência artificial para análise de consumo, previsões e detecção de padrões de uso.

## Plano da Sprint 02

## Referências
