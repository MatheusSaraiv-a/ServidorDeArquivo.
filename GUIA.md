# Passo a passo: criar o Uploader e publicar no GitHub

## Como funciona

```
[Celular] --Wi-Fi--> [Seu PC rodando app.py] --> pasta uploads/
```

O PC roda um servidor web (Flask). O celular abre a página no navegador e envia os arquivos.
**Os dois precisam estar na mesma rede Wi-Fi.**

---

## Parte 1 — Preparar o ambiente

### 1. Instale o Python
Baixe em https://www.python.org/downloads/ (versão 3.9+).
No Windows, marque **"Add Python to PATH"** no instalador.

Teste no terminal:
```bash
python --version
```
(No Mac/Linux pode ser `python3`.)

### 2. Instale o Git
Baixe em https://git-scm.com/downloads e teste:
```bash
git --version
```

### 3. Crie uma conta no GitHub
https://github.com (grátis).

---

## Parte 2 — Criar o projeto

### 4. Crie a pasta e a estrutura
```bash
mkdir file-uploader
cd file-uploader
mkdir templates uploads
```

Estrutura final:
```
file-uploader/
├── app.py               <- servidor (Flask)
├── requirements.txt     <- dependências
├── .gitignore           <- o que o Git deve ignorar
├── README.md
├── templates/
│   └── index.html       <- página que abre no celular
└── uploads/
    └── .gitkeep         <- mantém a pasta no Git
```

### 5. Adicione os arquivos
Copie o conteúdo de `app.py`, `templates/index.html`, `requirements.txt` e `.gitignore`
para os lugares indicados acima.

### 6. Crie o ambiente virtual e instale o Flask
```bash
python -m venv venv
```
Ative:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

Instale:
```bash
pip install -r requirements.txt
```

---

## Parte 3 — Testar

### 7. Rode o servidor
```bash
python app.py
```
Vai aparecer algo como:
```
No computador: http://localhost:8000
No celular:    http://192.168.0.15:8000  (mesmo Wi-Fi)
```

### 8. Teste no computador
Abra `http://localhost:8000`, envie um arquivo e confira se ele aparece em `uploads/`.

### 9. Teste no celular
1. Conecte o celular no **mesmo Wi-Fi** do PC.
2. Abra o navegador e digite o endereço "No celular" mostrado no terminal.
3. Toque na área de upload, escolha fotos/arquivos e envie.

### 10. Se o celular não abrir a página
- **Firewall do Windows:** quando aparecer o aviso ao rodar o Python, clique em **Permitir acesso** (rede privada).
  Se perdeu o aviso: Painel de Controle → Firewall → "Permitir um aplicativo" → Python.
- **Rede diferente:** confirme que PC e celular estão no mesmo Wi-Fi (não use dados móveis nem Wi-Fi de convidados).
- **Isolamento de clientes:** alguns roteadores/redes públicas bloqueiam a comunicação entre dispositivos.
- **IP errado:** no Windows use `ipconfig`, no Mac/Linux `ifconfig` ou `ip a` para ver o IP do PC.

---

## Parte 4 — Publicar no GitHub

### 11. Configure o Git (só na primeira vez)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

### 12. Inicialize o repositório
Dentro da pasta do projeto:
```bash
git init
git add .
git status
```
Confira: a pasta `venv/` e os arquivos dentro de `uploads/` **não** devem aparecer (o `.gitignore` cuida disso).

### 13. Faça o primeiro commit
```bash
git commit -m "Primeira versão do uploader"
git branch -M main
```

### 14. Crie o repositório no GitHub
1. Acesse https://github.com/new
2. Nome: `file-uploader`
3. Deixe **sem** README, .gitignore ou licença (já temos localmente).
4. Clique em **Create repository**.

### 15. Conecte e envie
Copie a URL do repositório e rode (troque `SEU-USUARIO`):
```bash
git remote add origin https://github.com/SEU-USUARIO/file-uploader.git
git push -u origin main
```

O GitHub não aceita mais a senha da conta no terminal. Ao pedir login:
- Use o navegador quando o Git abrir a janela de autenticação, **ou**
- Crie um Personal Access Token em GitHub → Settings → Developer settings → Personal access tokens, e use-o como senha.

### 16. Pronto
Atualize a página do repositório no GitHub: seus arquivos estarão lá.

---

## Parte 5 — Atualizações futuras

Sempre que mudar algo no código:
```bash
git add .
git commit -m "Descreva o que mudou"
git push
```

## Quem clonar o projeto usa assim
```bash
git clone https://github.com/SEU-USUARIO/file-uploader.git
cd file-uploader
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## Dicas de segurança
- Não tem senha: use só em rede confiável e nunca abra a porta 8000 no roteador para a internet.
- Se quiser acessar de fora de casa, use uma VPN como Tailscale em vez de expor a porta.
- Nunca suba arquivos pessoais para o GitHub: por isso `uploads/` está no `.gitignore`.

## Ideias para evoluir
- Senha/PIN de acesso
- QR Code no terminal para abrir no celular sem digitar o IP
- Limitar tipos de arquivo
- Pré-visualização de imagens
