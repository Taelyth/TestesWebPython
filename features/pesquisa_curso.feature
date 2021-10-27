# language: pt
  Funcionalidade: Pesquisa Curso
    Consulta de cursos pelo site da Iterasys
    Cenario: Pesquisar Curso ao Clicar na Lupa
      Dado que acesso o site da Iterasys
      Quando pesquiso pelo curso "Mantis"
      E clico na lupa
      Entao exibe o curso "Mantis" na pagina de resultados
      Quando clico no botao "Matricule-se"
      Entao exibe a pagina do carrinho com o curso "Mantis" e o preco de "R$ 59,99"