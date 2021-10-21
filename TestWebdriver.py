from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriver:

    # 1 - Preparativos - Antes do Teste
    def setup(self):
        # criar um objeto chamado "driver" e instancia-o como Selenium para o Browser Chrome
        # indicando onde está o seu chrome driver
        self.driver = webdriver.Chrome('C:\\webdrivers\\chromedriver\\95\\chromedriver.exe')
        # Definimos uma espera de até 3 segundos para qualquer elemento no teste
        # self.driver.implicitly_wait(3)
        # Maximizar janela
        self.driver.maximize_window()
        # Abre o site da iterasys
        self.driver.get("https://iterasys.com.br/")

    # 3 - Encerramento - Depois do Teste
    def teardown(self):
        self.driver.quit()

    # 2 - O teste em si
    def teste_consultar_curso(self):
        driver = self.driver
        # Clicar na caixa de pesquisa
        driver.find_element(By.ID, 'searchtext').click()
        # Limpar a caixa de pesquisa
        driver.find_element(By.ID, 'searchtext').clear()
        # Escrever 'mantis'
        driver.find_element(By.ID, 'searchtext').send_keys('Mantis')
        # Clicar na lupa
        driver.find_element(By.ID, 'btn_form_search').click()

        # Página 2
        # Checar nome do curso
        WebDriverWait(driver, 3).until(expected_conditions
                                       .text_to_be_present_in_element((By.CSS_SELECTOR, 'span.titulo'), 'Mantis'))
        assert driver.find_element(By.CSS_SELECTOR, 'span.titulo').text == 'Mantis'
        assert driver.find_element(By.CSS_SELECTOR, 'h3').text == 'Cursos › \"Mantis\"'

        # Clicar no botão "Matricule-se"
        driver.find_element(By.CSS_SELECTOR, '.comprar').click()
        assert driver.find_element(By.CSS_SELECTOR, '.item-title').text == 'Mantis'
        assert driver.find_element(By.CSS_SELECTOR, '.new-price').text == 'R$ 59,99'
