# TestesWebPython
Projeto criado para acompanhar as aulas do curso [Formação em Teste de Software][Iterasys] em **Python** utilizando **Selenium**.

Neste projeto é possível rodar testes **web** localmente.

Ele foi criado para treinamento de funções do Selenium em um sistema de venda de cursos e cadastro.

---

### Pré-Requisitos
Esse projeto possui pré requisitos diferentes dependendo do código que será executado.

URL usada nos testes: [Iterasys]

---

`TestWebdriver.py`

É necessário colocar o chromedriver no seguinte diretório: `C:\\webdrivers\chromedriver\{versão}\chromedriver.exe` e alterar a `{versão}` no código conforme o necessário.

---

`TesteCadastro.py`

1 - Adicionar chromedriver da mesma forma que explicado acima.

2 - Alterar os Dados Cadastrais usados no teste no arquivo `Dados.py` (os que estão atualmente são um exemplo utilizado nos testes de login e cadastro).

3 - Durante o teste `testar_cadastro` existem 2 pausas na automação:

- A primeira pausa ocorre após preencher os dados cadastrais no site, pois existe um captcha que deve ser digitado manualmente.
- A segunda pausa está após o cadastro ao verificar o e-mail de confirmação, onde poderá aparecer um anúncio que deverá ser clicado em fechar de forma manual.

---

Para executar os scripts as seguintes bibliotecas deverão ser instaladas:

```
pytest
pytest-bdd
selenium
```

---

### Glossário

`features` Diretório para armazenar dois arquivos de BDD `.feature`, sendo que um deles foi feito para testar o uso do Pytest-BDD usando a versão Community do Pycharm.

`steps` Arquivo `.py` onde é executado o arquivo `.feature` para teste do Pytest-BDD

`TestWebdriver.py` Arquivo para teste simples em Selenium, usado na aula.

`lista09` Diretório do exercício realizado como treinamento que possui os arquivos abaixo:

`Dados.py` Arquivo com dados cadastrais usados nos testes do `TesteCadastro.py`

`TesteCadastro.py` Script que possui 4 testes, sendo eles:

- `testar_cadastro` onde é realizado o cadastro no site com um e-mail temporário.
- `testar_login_com_cadastro` onde é realizado o login com o cadastro feito com o teste acima.
- `testar_login_standalone` teste de login com um cadastro já realizado anteriormente e preenchido no arquivo `Dados.py`.
- `testar_logout` teste de logout utilizando o `testar_login_standalone`.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/

<!-- imagens -->
[Iterasys-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)