from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select




#CONFIGS
usuario = '@gmail.com' #EMAIL ARTWALK
senha = '' #SENHA ARTWALK
link = 'https://www.artwalk.com.br/calendario-sneaker/proximos-lancamentos/tenis-nike-air-jordan-1-retro-high-og-court-purple' #EXEMPLO DO LINK (LINK ENCONTRADO NO CALENDARIO SNEAKER)
size = '43' #TAMANHO DESEJADO
codigo = '' #CODIGO DO CARTÃO
driver = webdriver.Chrome('C:\\Users\\mude\\Desktop\\chromedriver') #LOCALIZE O CHROMEDRIVER

#NAO MEXA
def login():
    driver.get('https://www.artwalk.com.br/login')
    botaoLogin()

def botaoLogin():
    try:
        logBt =  WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-block.btn-large.vtexIdUI-others-send-email'))
        )
        logBt.click()
        logar()
    except:
        login()

def logar():
    try:
        email = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, 'inputEmail'))
        )
        secreta = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, 'inputPassword'))
        )
        email.send_keys(usuario)
        secreta.send_keys(senha)
        secreta.send_keys(Keys.ENTER)
        inicioCompra()
    except:
        login()

def inicioCompra():
    try:
        driver.get(link)
        comprar = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'comprar'))
        )
        comprar.click()

        try:
            btSize = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.CLASS_NAME, f'dimension-Tamanho.espec_0.skuespec_{size}.skuespec_Tamanho_opcao_{size}'))
            )
            btComprar = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'buy-button.buy-button-ref'))
            )

            btSize.click()
            btComprar.click()
            pay = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.ID, 'cart-to-orderform'))
            )
            pay.click()
        except:
            inicioCompra()

        try:
            driver.implicitly_wait(4)
            iframe = driver.find_element_by_xpath('//*[@id="iframe-placeholder-creditCardPaymentGroup"]/iframe')
            driver.switch_to.frame(iframe)
            parc = Select(driver.find_element_by_id('creditCardpayment-card-0Brand'))
            parc.select_by_value('10')

            code = WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'input-mini'))
            )
            code.send_keys(codigo)

            driver.switch_to.default_content()

            compra = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.ID, 'payment-data-submit'))
            )
            compra.click()

        except:
            print('Algo deu errado')

    except:
        inicioCompra()

login()
