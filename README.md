# File Uploader

Um sistema de upload de arquivos que transforma o computador em um servidor local. Com ele, você envia fotos, vídeos e documentos do celular para o PC (ou de um PC para outro) pelo navegador, usando apenas o Wi-Fi de casa. Não precisa de cabo, aplicativo nem serviço em nuvem.

## Funcionalidades
 
- Envio de vários arquivos de uma vez
- Barra de progresso individual para cada arquivo
- Arrastar e soltar (no computador) ou tocar para escolher (no celular)
- Lista dos arquivos salvos no computador, com download e exclusão
- Interface responsiva, pensada para celular, com modo escuro automático
- Limite de 2 GB por envio

## Tecnologias e ferramentas usadas
 
Servidor - **Python 3** (Linguagem do back-end)

Framework web - **Flask** (Rotas HTTP e servidor)

Utilitários - **Werkzeug** - Limpar nomes de arquivo com segurança 

Front-end - **HTML, CSS e JavaScript puro** (Interface, sem frameworks nem bibliotecas externas)

Comunicação - **XMLHttpRequest** e **Fetch API** (Envio com progresso e leitura da lista)
