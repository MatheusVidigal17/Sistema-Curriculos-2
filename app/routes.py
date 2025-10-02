from flask import Blueprint, jsonify, request
from .models import Usuario, Curriculo
from .database import db

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return jsonify({"message": "API de Currículos funcionando!"})

@bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = request.json
    novo_usuario = Usuario(nome=data["nome"])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"id": novo_usuario.id, "nome": novo_usuario.nome})

@bp.route("/usuarios/<int:id>/curriculos", methods=["POST"])
def criar_curriculo(id):
    data = request.json
    novo_curriculo = Curriculo(
        usuario_id=id,
        dados_pessoais=data.get("dados_pessoais", ""),
        experiencias=data.get("experiencias", ""),
        formacoes=data.get("formacoes", ""),
        habilidades=data.get("habilidades", "")
    )
    db.session.add(novo_curriculo)
    db.session.commit()
    return jsonify({"id": novo_curriculo.id, "usuario_id": id})
