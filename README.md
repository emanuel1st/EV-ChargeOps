# EV ChargeOps

## Integrantes

###### _Emanuel Rocha Monteiro_ - _RM569895_

## Introdução

O crescimento da mobilidade elétrica tem impulsionado a adoção de veículos elétricos em todo o mundo, incluindo o Brasil. Com o aumento da frota desses veículos, cresce também a necessidade de expandir e modernizar a infraestrutura de recarga, especialmente em ambientes compartilhados como condomínios residenciais, edifícios corporativos e campus universitários. Nesses locais, o gerenciamento das sessões de recarga, a identificação dos usuários e a cobrança individual do consumo tornam-se desafios importantes para garantir uma operação eficiente e justa.

Nesse contexto, surge o **EV ChargeOps**, uma plataforma desenvolvida para transformar os dados gerados pelas sessões de recarga em informações úteis para usuários e gestores. A proposta busca integrar monitoramento, controle de consumo, rateio automatizado e recursos de inteligência artificial em uma única solução, proporcionando maior transparência, eficiência operacional e apoio à tomada de decisões. Este documento apresenta os resultados das pesquisas realizadas na Sprint 01, abordando o contexto do problema, aspectos regulatórios e técnicos, arquitetura da solução proposta e o planejamento para a fase de desenvolvimento da Sprint 02.

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

#### Open Charge Map API

A Open Charge Map API é uma plataforma aberta que disponibiliza informações sobre estações de recarga de veículos elétricos em diversos países, permitindo a integração desses dados em aplicativos e sistemas de gestão. Por meio de requisições em formatos como JSON, a API fornece informações detalhadas sobre a localização dos carregadores, incluindo endereço, coordenadas geográficas, operador responsável e regras de acesso. Também disponibiliza dados técnicos como potência do carregador, quantidade de conectores, tipos de tomadas disponíveis e informações sobre tarifas ou custos de utilização. Além disso, a plataforma conta com recursos colaborativos que permitem o compartilhamento de comentários, avaliações, fotos e registros de uso feitos pelos próprios usuários, contribuindo para a atualização e confiabilidade das informações disponíveis.

No EV ChargeOps, essa API poderia ser utilizada para exibir carregadores próximos aos usuários, auxiliar no planejamento de novas instalações e fornecer informações complementares sobre a infraestrutura de recarga existente na região.

#### ANEEL Open Data

O Portal de Dados Abertos da ANEEL disponibiliza informações públicas sobre o setor elétrico brasileiro, permitindo que empresas, pesquisadores e desenvolvedores utilizem esses dados para análises, estudos e desenvolvimento de soluções. A plataforma reúne dezenas de conjuntos de dados relacionados à geração, distribuição e comercialização de energia elétrica, incluindo informações sobre usinas, capacidade instalada, redes de distribuição, subestações, inspeções, manutenção da infraestrutura elétrica e componentes tarifários. Além disso, o portal oferece dados sobre o mercado de energia, como informações fornecidas pelas distribuidoras e indicadores do setor, possibilitando a realização de análises estratégicas e o acompanhamento da evolução da infraestrutura energética no país.

Esses dados poderiam ser utilizados pelo EV ChargeOps para gerar análises energéticas, comparar padrões de consumo e produzir relatórios gerenciais que auxiliem gestores na tomada de decisão sobre a infraestrutura de recarga.

## Frente 3 - Arquitetura e IA

### Arquitetura Proposta

A plataforma EV ChargeOps será composta por quatro camadas principais. A primeira é a camada física, formada pelos carregadores de veículos elétricos, responsáveis por realizar a recarga e registrar dados como consumo de energia, duração da sessão e potência utilizada. A segunda é a camada de conectividade, composta pelas interfaces de comunicação do carregador, como Wi-Fi, LAN, Bluetooth e RS-485, que permitem a transmissão dos dados para sistemas externos e plataformas de monitoramento.

A terceira é a camada de aplicação, responsável pelo processamento das informações recebidas. Nessa camada estarão o banco de dados, as regras de negócio, o sistema de cálculo de rateio e os recursos de inteligência artificial utilizados para análise e previsão de consumo. Por fim, a camada de apresentação será composta pelas interfaces utilizadas pelos gestores e usuários, permitindo acompanhar sessões de recarga, consultar relatórios, visualizar cobranças e acessar informações sobre o consumo de energia.

### Fluxo dos Dados

O fluxo de dados inicia quando o usuário se identifica e conecta seu veículo ao carregador. Durante a sessão, o equipamento registra informações como horário de início, horário de término, potência utilizada, energia consumida em kWh e identificação do usuário. Esses dados são transmitidos por meio das interfaces de comunicação para a plataforma de gerenciamento, onde ficam armazenados em um banco de dados.

Após o armazenamento, as informações passam pelas regras de negócio do sistema, que realizam o cálculo do consumo individual e geram os valores que serão utilizados na cobrança. Nesse processo, a inteligência artificial pode ser utilizada para identificar padrões de utilização, prever demandas futuras de energia e detectar possíveis anomalias ou comportamentos fora do padrão. Após o processamento, as informações são disponibilizadas no dashboard da plataforma e utilizadas para a geração da fatura individual de cada usuário.

### Modelo de Rateio

A equipe propõe um modelo de rateio baseado no consumo individual de energia, utilizando como principal variável a quantidade de energia consumida em quilowatt-hora (kWh) durante cada sessão de recarga. O valor da fatura será calculado multiplicando-se o total de kWh consumidos pela tarifa de energia aplicada pelo condomínio ou pela administradora do sistema. Caso necessário, poderá ser adicionada uma taxa fixa destinada à manutenção da infraestrutura de recarga.

Em situações excepcionais, o sistema adotará regras específicas para garantir justiça na cobrança. Em sessões interrompidas, será cobrado apenas o valor correspondente à energia efetivamente consumida até o momento da interrupção. Usuários que não realizarem nenhuma recarga durante o mês não terão cobrança de consumo. Nos casos em que uma mesma unidade possuir dois ou mais veículos cadastrados, o sistema somará o consumo de todas as sessões vinculadas àquela unidade para gerar uma única fatura mensal. Isso garante transparência, simplicidade na cobrança e distribuição justa dos custos entre os usuários da infraestrutura compartilhada.

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

## Plano para a Sprint 02 – Desenvolvimento e Prototipação

A Sprint 02 será dedicada ao desenvolvimento da solução proposta na fase de pesquisa e documentação. O objetivo será transformar os conceitos definidos na Sprint 01 em um protótipo funcional capaz de registrar sessões de recarga, calcular o consumo individual dos usuários e gerar informações para gestão da infraestrutura compartilhada.

Inicialmente, será realizada a modelagem e implementação do banco de dados, definindo as entidades necessárias para armazenar informações de usuários, unidades, carregadores, sessões de recarga e faturas. Em seguida, será desenvolvido o back-end da aplicação, responsável pelo processamento dos dados, aplicação das regras de negócio e cálculo do rateio individual de consumo.

Na etapa seguinte, será realizada a integração com os dados do carregador GoodWe ou com dados simulados, permitindo registrar informações como consumo de energia, duração das sessões e identificação dos usuários. Após isso, será implementado o módulo responsável pela geração das cobranças e relatórios de utilização da infraestrutura.

Por fim, serão desenvolvidas as interfaces da plataforma para gestores e usuários, permitindo acompanhar sessões de recarga, consultar históricos de consumo e visualizar valores cobrados. Também será criada uma funcionalidade baseada em inteligência artificial para análise de padrões de utilização e previsão de consumo futuro. A sprint será concluída com testes, ajustes finais e preparação do material para apresentação e vídeo pitch do projeto.

## Referências

### Infraestrutura de Recarga e Mobilidade Elétrica

- [PUC Minas – Estudo sobre veículos elétricos e infraestrutura de recarga](https://bib.pucminas.br/pergamumweb/vinculos/0000b5/0000b5c6.pdf)
- [Elétricos App – Pontos de recarga públicos em 2026: custos e segurança](https://eletricos.app/noticias/pontos-recarga-publicos-2026-custos-seguranca)
- [CNN Brasil – Setor de carros elétricos enfrenta desafios de infraestrutura para crescer](https://www.cnnbrasil.com.br/economia/setor-de-carros-eletricos-enfrenta-desafios-de-infraestrutura-para-crescer/)
- [Tegra Incorporadora – Carro elétrico e condomínios: infraestrutura de recarga](https://www.tegraincorporadora.com.br/blog/dicasedecor/carro-eletrico-e-condominio-predios-com-infraestrutura-de-recarga)

### Modelos de Cobrança e Rateio

- [Voltbras – Tudo sobre a cobrança de recargas de carros elétricos no Brasil](https://voltbras.com/tudo-sobre-a-cobranca-de-recargas-de-carros-eletricos-no-brasil/)

### Regulamentação e ANEEL

- [LegisWeb – Resolução Normativa ANEEL nº 1000/2021](https://www.legisweb.com.br/legislacao/?id=490988)
- [Atos Oficiais – Texto da Resolução Normativa nº 1000/2021](https://atosoficiais.com.br/aneel/resolucao-normativa-n-1000-2021-estabelece-as-regras-de-prestacao-do-servico-publico-de-distribuicao-de-energia-eletrica-revoga-as-resolucoes-normativas-aneel-no-414-de-9-de-setembro-de-2010-no-470-de-13-de-dezembro-de-2011-no-901-de-8-de-dezembro-de-2020-e-da-outras-providencias?origin=instituicao)
- [ANEEL – Resolução 1000: direitos sobre energia elétrica](https://www.gov.br/aneel/pt-br/assuntos/campanhas/resolucao-1000-da-aneel-seus-direitos-sobre-energia-eletrica-agora-num-so-lugar-2022)
- [Voltera – Tudo sobre a ANEEL](https://blog.voltera.com.br/tudo-sobre-a-aneel/)

### GoodWe HCA G2 e Plataforma SEMS

- [GoodWe Brasil – Carregador HCA G2](https://br.goodwe.com/carregadores-hca-g2-goodwe)
- [GoodWe Brasil – HCA EV Charger](https://br.goodwe.com/hca-evcharger)
- [Manual de Instruções HCA G2](https://gfx3.senetic.com/akeneo-catalog/6/7/4/f/674f179a09124e654cbc41cb6612408467e39150_Instru____es_de_uso.pdf)
- [Canal Solar – GoodWe HCA G2 Electric Vehicle Charging](https://canalsolar.com.br/en/goodwe-hca-g2-electric-vehicle-charging/)
- [GoodWe – SEMS Portal User Manual](https://en.goodwe.com/Ftp/EN/Downloads/User%20Manual/GW_SEMS%20Portal-User%20Manual-EN.pdf)
- [GoodWe Community – SEMS API Documentation](https://community.goodwe.com/static/images/2022-11-08281223.pdf;jsessionid=726F7F4BB3CF930E5C1AACD82142805B)
- [GoodWe Community – Open API Guide](https://community.goodwe.com/static/images/2024-08-20597794.pdf;jsessionid=4AE5B640659703459137E5AEE71D221A)
- [OpenHAB – Integração SEMS Portal](https://www.openhab.org/addons/bindings/semsportal/)

### Open Charge Map API

- [Open Charge Map – API Oficial](https://www.openchargemap.org/develop/api)
- [DLT Hub – Open Charge Map Source](https://dlthub.com/context/source/open-charge-map)
- [MCP Market – Open Charge Map API](https://mcpmarket.com/server/open-charge-map-1)
- [Public API – Open Charge Map](https://publicapi.dev/open-charge-map-api)
- [Microsoft Learn – Open Charge Map Connector](https://learn.microsoft.com/en-us/connectors/openchargemapip/)

### Dados Abertos da ANEEL

- [ANEEL – Novos conjuntos de dados abertos](https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/dados-abertos-aneel-disponibiliza-novos-conjunto-de-dados)
- [ANEEL – Dados do BDGD, SIGET e SAMP](https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/conjuntos-de-dados-do-bdgd-siget-e-samp-estao-disponiveis-no-portal-de-dados-abertos-da-aneel)
- [Portal de Dados Abertos da ANEEL](https://dadosabertos.aneel.gov.br/dataset/?tags=tarifa+de+uso+do+sistema+de+distribui%C3%A7%C3%A3o)
- [ANEEL Open Data ArcGIS](https://dadosabertos-aneel.opendata.arcgis.com/)
