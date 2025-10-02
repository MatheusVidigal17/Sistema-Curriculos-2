from .database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)

class Curriculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    dados_pessoais = db.Column(db.Text)
    experiencias = db.Column(db.Text)
    formacoes = db.Column(db.Text)
    habilidades = db.Column(db.Text)

    usuario = db.relationship("Usuario", backref="curriculos")
