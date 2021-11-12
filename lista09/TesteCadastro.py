from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lista09 import Dados


class TesteCadastro:

    def setup(self):
        self.driver = webdriver.Chrome('C:\\webdrivers\\chromedriver\\95\\chromedriver.exe')
        self.driver.maximize_window()
        # Importação das variáveis do arquivo Dados, pois assim dados pessoais não precisam ficar no código (LGPD):
        self.nome = Dados.nome
        self.senha = Dados.senha
        self.telefone = Dados.telefone

    def teardown(self):
        self.driver.quit()

    # Método Utilizado para Testar a Função de Cadastro:
    # Possui 2 Etapas manuais:
    # 1 - Colocar Captcha
    #       - Correto, automação prossegue
    #       - Incorreto, só colocar novamente e apertar no botão Criar Conta
    # 2 - Fechar Anúncio após clicar no assunto do e-mail (não é possível automatizar)
    def testar_cadastro(self):
        driver = self.driver
        driver.get('https://iterasys.com.br/')

        # Espera FluentWait usada no resto do código
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=NoSuchElementException)

        # Entrar na Pagina inicial da Iterasys
        wait.until(EC.title_is('Iterasys - Cursos de Teste e QA'))

        # clicar no botão de aceitar Cookies
        driver.find_element(By.CSS_SELECTOR, 'div.cc-compliance').click()

        # Entrar na página de cadastro
        driver.find_element(By.CSS_SELECTOR, 'li.cadastro_pg_inicial').click()

        # Salvar aba da iterasys (voltaremos nela depois)
        pagina_iterasys = driver.current_window_handle

        # Abrir aba do email temporário
        driver.switch_to.new_window('tab')
        driver.get('https://www.temporary-mail.net/')
        nova_pagina = 'Temporary mail - Temporary mail to receive email in 10 seconds'

        wait.until(EC.title_is(nova_pagina))
        pagina_email = driver.current_window_handle

        # Copiar e-mail temporário
        wait.until(EC.visibility_of_element_located((By.ID, 'active-mail')))
        self.email_temp = driver.find_element(By.ID, 'active-mail').get_attribute('data-clipboard-text')
        email_temp = self.email_temp
        print(f'\nE-mail utilizado: {email_temp}')

        # Voltar para a aba da iterasys e preencher os dados cadastrais:
        driver.switch_to.window(pagina_iterasys)

        campo_nome = driver.find_element(By.ID, 'nome')
        campo_nome.click()
        campo_nome.send_keys(self.nome)

        campo_telefone = driver.find_element(By.ID, 'telefone')
        campo_telefone.click()
        campo_telefone.send_keys(self.telefone)

        campo_email = driver.find_element(By.ID, 'email')
        campo_email.click()
        campo_email.send_keys(email_temp)

        campo_senha = driver.find_element(By.ID, 'senha')
        campo_senha.click()
        campo_senha.send_keys(self.senha)

        # Espera em loop para preencher o Captcha Manualmente (após 6 caracteres sai do Loop)
        campo_captcha = driver.find_element(By.ID, 'e-captcha').get_attribute('value')
        while len(campo_captcha) < 6:
            campo_captcha = driver.find_element(By.ID, 'e-captcha').get_attribute('value')
        print(f'O Captcha é: {campo_captcha}')

        # Clicar no botão Criar Conta
        driver.find_element(By.ID, 'btn_cadastro').click()

        # Caso o Captcha inserido esteja incorreto (para poder inserir novamente):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.alert')))
        captcha_incorreto = driver.find_element(By.CSS_SELECTOR, 'div.alert').text
        while True:
            if captcha_incorreto == 'Captcha incorreto, tente novamente!':
                captcha_incorreto = driver.find_element(By.CSS_SELECTOR, 'div.alert').text
                continue
            else:
                break

        # Checar texto de cadastro realizado
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'h4.alert-heading'), 'Cadastro Realizado com sucesso.'))

        # Fechar Aba Iterasys, e ir para a Aba do E-mail
        driver.close()
        driver.switch_to.window(pagina_email)
        wait.until(EC.title_is(nova_pagina))

        # Dar Refresh na página do E-mail para que ele apareça
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'i.fa-refresh')))
        driver.find_element(By.CSS_SELECTOR, 'i.fa-refresh').click()

        # Clicar no assunto do E-mail Temporário (E dar Refresh novamente, se ele ainda não tiver aparecido)
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.title-subject')))
                driver.find_element(By.CSS_SELECTOR, 'a.title-subject').click()
                print('cliquei no assunto')
                break
            except TimeoutException:
                driver.find_element(By.CSS_SELECTOR, 'i.fa-refresh').click()
                print('cliquei no refresh')
                continue

        # Caso apareça o anúncio do Google, o click no close deverá ser realizado manualmente:
        url_anuncio = driver.current_url
        if url_anuncio == 'https://www.temporary-mail.net/':
            wait.until(EC.url_to_be('https://www.temporary-mail.net/#google_vignette'))
        else:
            while url_anuncio == 'https://www.temporary-mail.net/#google_vignette':
                url_anuncio = driver.current_url

        # Checar se estamos com o email aberto:
        wait.until(EC.title_is('Content Of Email | Temporary mail - Temporary mail to receive email in 10 seconds'))

        # Coletar Link do botão de Confirmar Cadastro e carregar a página:
        confirmar_cadastro = driver.find_element(By.LINK_TEXT, 'Confirmar cadastro')
        link = confirmar_cadastro.get_attribute('href')
        print(f'o link é: {link}')
        driver.get(link)

        # Checar se a Confirmação do Cadastro foi Concluída:
        wait.until(EC.title_is('Iterasys - Cursos de Teste e QA'))
        texto_confirmacao = driver.find_element(By.CSS_SELECTOR, 'div.alert h4').text
        assert texto_confirmacao == "Confirmação concluída!"

    # Método criado para fazer o Login, ele é reutilizado em dois casos:
    # 1 - Para testar o Login após fazer o cadastro, com o mesmo e-mail usado no cadastro.
    # 2 - Para testar o Login com um e-mail que já está cadastrado a algum tempo.
    def login(self, email_temp):
        driver = self.driver
        driver.get('https://iterasys.com.br/')

        # Espera FluentWait usada no resto do código
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=NoSuchElementException)

        # Entrar na Pagina inicial da Iterasys
        wait.until(EC.title_is('Iterasys - Cursos de Teste e QA'))

        # Entrar na página de login
        driver.find_element(By.CSS_SELECTOR, 'li.login_header').click()
        wait.until(EC.title_is('Login - Iterasys'))

        # Preencher dados de Login:
        wait.until(EC.presence_of_element_located((By.ID, 'email')))
        campo_email = driver.find_element(By.ID, 'email')
        campo_email.click()
        campo_email.send_keys(email_temp)

        campo_senha = driver.find_element(By.ID, 'senha')
        campo_senha.click()
        campo_senha.send_keys(self.senha)

        # Clicar no Botão Entrar
        driver.find_element(By.ID, 'btn_login').click()
        wait.until(EC.url_to_be('https://iterasys.com.br/profile/'))

        # Checar se os campos do cadastro estão corretos:
        assert driver.find_element(By.ID, 'nome').get_attribute('value') == self.nome
        assert driver.find_element(By.ID, 'email').get_attribute('value') == email_temp

    # Teste do Cadastro + Login
    def testar_login_com_cadastro(self):
        # Executa-se o método de cadastrar
        self.testar_cadastro()
        # Recebe o e-mail usado para cadastro
        email_temp = self.email_temp
        # O utiliza para Login
        self.login(email_temp)

    # Teste do Login (já cadastrado)
    def testar_login_standalone(self):
        self.email = Dados.email
        self.login(self.email)

    # Teste do Logout (já cadastrado)
    def testar_logout(self):
        # Método de teste do Login:
        self.testar_login_standalone()
        driver = self.driver

        # Fazer o Logout:
        driver.find_element(By.CSS_SELECTOR, 'li.dropdown').click()
        driver.find_element(By.CSS_SELECTOR, 'li.li_logout').click()

        # Checar se está deslogado:
        assert driver.find_element(By.CSS_SELECTOR, 'li.login_header a').text == 'Login'
