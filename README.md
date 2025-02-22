# FlashFocus

O **FlashFocus** é um aplicativo desenvolvido para aprimorar a velocidade de leitura e a compreensão de textos. Ele exibe palavras sequencialmente, destacando a letra central para facilitar a assimilação, e inclui um sistema de perguntas de múltipla escolha geradas automaticamente para testar a compreensão do usuário. Esta versão evolui o projeto original disponível em [FlashFocus (GitHub)](https://github.com/mdsjr/FlashFocus), agora reestruturado com uma arquitetura modular e desenvolvido no ambiente **PyCharm**.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Tkinter** e **customtkinter**: Para a interface gráfica moderna e personalizável.
- **Pillow**: Manipulação de imagens (ícones e logotipos).
- **pywin32**: Suporte à maximização da janela no Windows.
- **openai**: Integração com a API do ChatGPT para geração de perguntas.
- **python-dotenv** (opcional): Gerenciamento seguro de chaves de API via variáveis de ambiente.

## Funcionalidades
- Exibição sequencial de palavras com destaque na letra central em vermelho.
- Controle ajustável da velocidade de leitura via slider.
- Geração de perguntas de múltipla escolha (3 alternativas) com base no texto inserido, usando a API da OpenAI.
- Interface responsiva com botões intuitivos ("Iniciar", "Pausar", "Continuar", "Gerar Pergunta", "Verificar Resposta").
- Maximização automática da janela ao iniciar (otimizado para Windows).
- Estrutura modular para fácil manutenção e expansão.

## Estrutura do Projeto

<pre>
/FlashFocus
├── main.py                # Ponto de entrada do aplicativo
├── gui.py                 # Interface gráfica e lógica de exibição
├── text_processor.py      # Processamento e exibição sequencial de texto
├── quiz_generator.py      # Geração de perguntas via API da OpenAI
├── config.py              # Configurações e chaves (ex.: API_KEY)
└── assets/                # Recursos visuais
    ├── icon.ico           # Ícone da janela
    └── icon.png           # Logotipo exibido na interface
</pre>
    
## Pré-requisitos
- Python 3.11 ou superior
- Uma chave de API da OpenAI (obtida em [platform.openai.com](https://platform.openai.com/))

## Instalação e Execução
1. **Clone o repositório**:
   ```sh
   git clone https://github.com/mdsjr/FlashFocus-PyCharm.git
   cd FlashFocus-PyCharm

2. **Crie e ative um ambiente virtual**:
 ```sh
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

3. **Instale as dependências**:  
Crie um arquivo `requirements.txt` com:
 ```sh
customtkinter
Pillow
pywin32
openai
python-dotenv  # Opcional, para variáveis de ambiente
````
### Depois, instale com:
 ```sh
pip install -r requirements.txt
```
4. **Configure a chave da API**:
- Crie um arquivo `.env` na raiz do projeto:
```sh
API_KEY=sua_chave_da_openai_aqui
```
- Ou edite o `config.py` diretamente para incluir a chave fixa (menos seguro).

5. **Execute o aplicativo**:
   ```sh
   python main.py
   ````


## Instalação e Execução
1. Clone o repositório:
   ```sh
   git clone https://github.com/mdsjr/FlashFocus-PyCharm.git
   cd FlashFocus-PyCharm
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4.Crie um arquivo .env na raiz do projeto: 
```sh
API_KEY=sua_chave_da_openai_aqui
````

5. Execute o aplicativo:
   ```sh
   python main.py
   ```
## Uso
1. Insira ou edite o texto na caixa de texto.  
2. Use os botões "Iniciar", "Pausar" e "Continuar" para controlar a exibição sequencial do texto.  
3. Ajuste a velocidade de leitura com o slider.  
4. Clique em "Gerar Pergunta" para criar uma pergunta de múltipla escolha com base no texto.  
5. Selecione uma alternativa e clique em "Verificar Resposta" para testar sua compreensão.

## Gerando um Executável
Para transformar o projeto em um arquivo `.exe` (Windows):

1. Instale o `PyInstaller`:
```sh
pip install pyinstaller
```
2. Gere o executável incluindo o `.env`(se usado):
````sh
pyinstaller --add-data ".env;." --onefile main.py
````
3. O arquivo estará em `dist/main.exe.`

   

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas:
- Abra uma issue no GitHub.
- Envie um pull request com suas alterações.


## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

