# keylogger-simples

Keylogger educacional extremamente simples, criado para fins acadêmicos na disciplina de Teste de Software. O script registra palavras digitadas no teclado local e salva o resultado em um arquivo de texto para análise.

> ⚠️ **Aviso legal**
>
> O uso de keyloggers pode ser ilegal ou antiético em diversas jurisdições. Este projeto é fornecido exclusivamente para estudo e testes controlados em equipamentos próprios ou com consentimento explícito do proprietário. O autor e contribuintes não se responsabilizam por qualquer uso indevido.

## Como funciona

- Utiliza a biblioteca `keyboard` para monitorar eventos de tecla.
- Ignora teclas modificadoras e de controle (ex.: `Shift`, `Ctrl`, `Alt`).
- Armazena os caracteres digitados na variável `palavra_atual` até que a tecla `space` seja pressionada.
- Ao detectar `space`, salva a palavra completa em `data.txt` e reinicia o buffer.
- A captura permanece ativa até que a tecla `Esc` seja pressionada.

```11:24:keylogger.py
palavra_atual = ""  # guarda a palavra enquanto é digitada

def salvar(event):
    global palavra_atual
    if event.name in IGNORAR:
        return
    if event.name == "space":
        if palavra_atual:
            with open(ARQUIVO, "a") as f:
                f.write(palavra_atual + "\n")
            palavra_atual = ""
    else:
        palavra_atual += event.name
```

## Pré-requisitos

- Python 3.8 ou superior.
- Permissões de administrador (necessárias no Windows para que a biblioteca `keyboard` funcione corretamente).
- Biblioteca `keyboard` instalada:

```bash
pip install keyboard
```

## Execução

1. Clone o repositório ou baixe os arquivos.
2. (Opcional) Crie e ative um ambiente virtual.
3. Instale as dependências conforme indicado acima.
4. Execute o script:

```bash
python keylogger.py
```

5. Digite algumas palavras no teclado. Cada palavra separada por espaço será registrada.
6. Pressione `Esc` para encerramento seguro.

## Estrutura de saída

- As palavras capturadas são armazenadas, uma por linha, no arquivo `data.txt` localizado na raiz do projeto.
- Cada linha representa uma palavra completa, sem espaços extras.
- O arquivo é criado automaticamente se não existir.

## Personalização

- **Arquivo de destino**: altere a constante `ARQUIVO` em `keylogger.py` para definir outro caminho.
- **Teclas ignoradas**: ajuste o conjunto `IGNORAR` para incluir ou remover teclas específicas.
- **Delimitador de palavras**: modifique a condição que verifica `event.name == "space"` para registrar com outro delimitador (por exemplo, `enter`).

## Limitações conhecidas

- Pode não funcionar em sistemas que bloqueiam hooks globais de teclado.
- No macOS e em algumas distribuições Linux, pode ser necessário executar com privilégios elevados e habilitar permissões de acessibilidade.
- Não registra teclas pressionadas antes do script iniciar.

## Segurança e ética

- Use apenas em ambientes controlados e com autorização.
- Armazene e descarte `data.txt` com cuidado, pois contém informações sensíveis.
- Considere criptografar ou excluir os dados após o uso.

## Próximos passos sugeridos

- Adicionar testes automatizados para o fluxo de captura de dados (ex.: simulação de eventos de teclado).
- Implementar logs estruturados ou exportação em outros formatos (CSV/JSON).
- Criar uma interface para configurações (teclas ignoradas, arquivo de saída, delimitador).

## Licença

Este projeto não especifica uma licença. Antes de publicar versões modificadas, defina explicitamente uma licença adequada ou mantenha o uso restrito ao âmbito acadêmico.
