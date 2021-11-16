Feature: Pesquisa Curso 2
    Consulta de cursos pelo site da Iterasys
    Scenario: Pesquisar Curso ao Clicar na Lupa
      Given que acesso o site da Iterasys
      When pesquiso pelo curso "Mantis"
      And clico na lupa
      Then exibe o curso "Mantis" na pagina de resultados
      When clico no botao Matricule-se
      Then exibe a pagina do carrinho com o curso "Mantis" e o preco de "R$ 59,99"