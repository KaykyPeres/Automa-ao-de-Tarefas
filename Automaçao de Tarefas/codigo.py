import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5 

# abrir o navegador (edge) 

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Fazer login
# selecionar o campo de email
pyautogui.click(x=877, y=356)
pyautogui.write("EmailTeste@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("pythonlegal")
pyautogui.click(x=957, y=517) # clique no botao de login
time.sleep(3)

# Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar os produtos repetindo o processo de cadastro até o fim 
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=842, y=241)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    
5.0     
