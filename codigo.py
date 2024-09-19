import pyautogui
import pandas
import time



pyautogui.PAUSE = 0.5

try:
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
except Exception as e:
    print(f"Erro ao abrir o Chrome: {e}")
    raise
  
try:
    pyautogui.click(x=453, y=56)
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")
except Exception as e:
    print(f"Erro ao acessar o site: {e}")
    raise
    
time.sleep(3)

try:
    pyautogui.click(x=874, y=408)
    pyautogui.hotkey("ctrl","a")
    pyautogui.write("vgalvao.work2@gmail.com")
    
    pyautogui.press("tab")
    pyautogui.write("123456")
    pyautogui.click(x=962, y=565)
except Exception as e:
    print(f"Erro ao fazer login: {e}")
    raise
  
time.sleep(3)

try:
    tabela = pandas.read_csv("produtos.csv")
    print(tabela)
except FileNotFoundError:
    print(f"Erro: O arquivo 'produtos.csv' não foi encontrado.")
    raise
  
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    raise

for linha in tabela.index:
    try:
        pyautogui.click(x=893, y=285)
        codigo = str(tabela.loc[linha, "codigo"])
        pyautogui.write(codigo)
        
        marca = str(tabela.loc[linha, "marca"])
        pyautogui.press("tab")
        pyautogui.write(marca)
        
        tipo = str(tabela.loc[linha, "tipo"])
        pyautogui.press("tab")
        pyautogui.write(tipo)
        
        categoria = str(tabela.loc[linha, "categoria"])
        pyautogui.press("tab")
        pyautogui.write(categoria)
        
        preco = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.press("tab")
        pyautogui.write(preco)
        
        custo = str(tabela.loc[linha, "custo"])
        pyautogui.press("tab")
        pyautogui.write(custo)
        
        pyautogui.press("tab")
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            pyautogui.write(obs)
        
        pyautogui.press("tab")
        pyautogui.press("enter")
        
        pyautogui.scroll(5000)
    except Exception as e:
        print(f"Erro ao processar a linha {linha}: {e}")
        break
