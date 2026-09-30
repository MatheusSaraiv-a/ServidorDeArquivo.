"""Uploader simples: envie arquivos do celular para o seu computador."""
import os
import socket

from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
PORT = 8000

os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024**3  # limite de 2 GB por envio


def unique_name(filename):
    """Sanitiza o nome e evita sobrescrever arquivos existentes."""
    name = secure_filename(filename) or "arquivo"
    base, ext = os.path.splitext(name)
    candidate, i = name, 1
    while os.path.exists(os.path.join(UPLOAD_DIR, candidate)):
        candidate = f"{base}_{i}{ext}"
        i += 1
    return candidate


def local_ip():
    """Descobre o IP do computador na rede local."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/upload")
def upload():
    files = request.files.getlist("files")
    if not files:
        return jsonify(error="Nenhum arquivo enviado"), 400
    saved = []
    for f in files:
        if not f.filename:
            continue
        name = unique_name(f.filename)
        f.save(os.path.join(UPLOAD_DIR, name))
        saved.append(name)
    return jsonify(saved=saved)


@app.get("/files")
def list_files():
    items = []
    for name in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR, name)
        if os.path.isfile(path) and not name.startswith("."):
            st = os.stat(path)
            items.append({"name": name, "size": st.st_size, "modified": st.st_mtime})
    items.sort(key=lambda x: x["modified"], reverse=True)
    return jsonify(items)


@app.get("/download/<path:name>")
def download(name):
    return send_from_directory(UPLOAD_DIR, name, as_attachment=True)


@app.delete("/files/<path:name>")
def delete(name):
    path = os.path.join(UPLOAD_DIR, secure_filename(name))
    if os.path.isfile(path):
        os.remove(path)
        return jsonify(deleted=name)
    return jsonify(error="Arquivo não encontrado"), 404


if __name__ == "__main__":
    ip = local_ip()
    print("\n  Uploader rodando!")
    print(f"  No computador: http://localhost:{PORT}")
    print(f"  No celular:    http://{ip}:{PORT}  (mesmo Wi-Fi)\n")
    app.run(host="0.0.0.0", port=PORT)
