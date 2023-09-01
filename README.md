# projetoifood
-------
<h2>Projeto 1 banco de dados</h2>
<p>Este banco de dados para e-commerce consiste em quatro tabelas principais:</p>
<ol>
  <li>Usuário (User): Armazena informações sobre os clientes que utilizam a plataforma, como nome, email e endereço. Cada usuário tem um ID único como chave primária.</li>
  <li>Categoria (Category): Categorias de produtos que são usadas para organizar os itens no site. Cada categoria tem um nome e um ID único como chave primária.</li>
  <li>Produto (Product): Contém informações detalhadas sobre os produtos disponíveis para compra, como nome, descrição, preço e a categoria à qual pertencem. Cada produto tem um ID único como chave primária e uma chave estrangeira que referencia a categoria à qual pertence.</li>
  <li>Pedido (Order): Registra informações sobre os pedidos feitos pelos usuários, incluindo o ID do usuário que fez o pedido, a data do pedido e o status do pedido. Cada pedido tem um ID único como chave primária e uma chave estrangeira que referencia o usuário que fez o pedido.</li>
  <li>Item do Pedido (OrderItem): Registra os itens individuais incluídos em cada pedido, juntamente com a quantidade e o preço unitário. Cada item de pedido tem um ID único como chave primária e chaves estrangeiras que relacionam o item ao pedido correspondente e ao produto associado.</li>
</ol>


<p>Além disso, foram fornecidas consultas SQL de exemplo para demonstrar como recuperar informações do banco de dados, filtrar dados com base em critérios específicos, calcular atributos derivados, ordenar resultados e realizar junções entre tabelas para obter uma visão mais completa dos dados.</p>
---------
<h2>Projeto 2 banco de dados</h2>
<p>Neste projeto, foi criado um banco de dados para atender às necessidades de uma oficina mecânica. O processo envolveu a criação de um esquema lógico com base em um modelo ER (Entidade-Relacionamento) conceitual, seguido pela implementação desse esquema em SQL e a realização de consultas complexas para demonstrar as funcionalidades do banco de dados. Aqui está um resumo do processo:</p>


<h3>Esquema Lógico:</h3>
<ol>
<li>Entidades principais</li>
  <ul>
    <li>Cliente: Armazena informações sobre os clientes da oficina, incluindo nome, endereço e número de telefone.</li>
    <li>Veículo: Contém detalhes dos veículos pertencentes aos clientes, como marca, modelo e ano.</li>
    <li>Serviço: Registra informações sobre os serviços oferecidos pela oficina, incluindo descrição e preço.</li>
    <li>Ordem de Serviço: Registra os pedidos de serviço feitos pelos clientes, incluindo a data de entrada, a data de saída prevista e o status da ordem.</li>
  </ul>
<li>Relacionamentos:</li>
  <ul>
    <li>Cliente -> Veículo: Um cliente pode ter vários veículos, criando um relacionamento um-para-muitos entre Cliente e Veículo.</li>
    <li>Veículo -> Ordem de Serviço: Um veículo pode estar associado a várias ordens de serviço, criando um relacionamento um-para-muitos entre Veículo e Ordem de Serviço.</li>
    <li><Serviço -> Ordem de Serviço: Um serviço pode ser associado a várias ordens de serviço, criando um relacionamento um-para-muitos entre Serviço e Ordem de Serviço./li>
  </ul>
</ol>



--------

<h2>Desafio Banco fonecido pelo Bootcamp Ifood utilizando Python.</h2>
<p>Linguagem utilizada</p> 
<img align="center" alt="gui-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

Nos foi fornecido um desafio de criar um banco com instruções de comando simples. Pensando na minha prática e necessidade de estudo optei por criá-lo um tanto diferente, utilizei POO para construção deste projeto. Esta ideia surgiu devido ao curso de outra plataforma solicitar a mesma atividade então optei por suprir ambas necessidades. A ideia por trás deste código é utilizar getters e setter mesmo não sendo necessários, praticar a ideia de herança, abstração entre outros pontos atingidos durante a construção deste código. Ele não gera um extrato em si. Porém checa a existência e correspôndencia de uma conta x agência x cliente. O código também permite saque e depósito de valores no sistema. 

<p>A alteração do idioma no código na classe Bank ocorre por conta da minha confusão ao setar variáveis e utiliza-las durante o código.</p> 
