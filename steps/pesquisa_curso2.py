from pytest_bdd import scenario, given, when, then, parsers


@scenario('../features/pesquisa_curso2.feature', 'Pesquisar Curso ao Clicar na Lupa')
def test_pesquisa_curso():
    pass


@given('que acesso o site da Iterasys')
def que_acesso_o_site_da_iterasys():
    pass


@when(parsers.parse('pesquiso pelo curso "{curso}"'), target_fixture="curso")
def pesquiso_pelo_curso(curso):
    assert curso == 'Mantis'


@when('clico na lupa')
def clico_na_lupa():
    pass


@then(parsers.parse('exibe o curso "{curso}" na pagina de resultados'))
def exibe_o_curso_na_pagina_de_resultados(curso):
    assert curso == 'Mantis'


@when('clico no botao Matricule-se')
def clico_no_botao():
    pass


@then(parsers.parse('exibe a pagina do carrinho com o curso "{curso}" e o preco de "{preco}"'), target_fixture='preco')
def exibe_a_pagina_do_carrinho_e_valida(curso, preco):
    assert curso == 'Mantis'
    assert preco == 'R$ 59,99'
