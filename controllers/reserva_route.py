from flask import Blueprint, request, jsonify
from models.reserva_model import Reserva
from database import db
import requests
from config import GERENCIAMENTO_API_URL

reserva_bp = Blueprint("reservas", __name__)


def verificar_turma(turma_id):
    try:
        resp = requests.get(f"{GERENCIAMENTO_API_URL}{turma_id}")
        return resp.status_code == 200
    except Exception as e:
        print(f"Erro ao verificar turma: {e}")
        return False

@reserva_bp.route("/criar", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")

    if not verificar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

@reserva_bp.route("/listar", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])

@reserva_bp.route("/filtrar/<int:id>", methods=["GET"])
def obter_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    return jsonify({
        "id": reserva.id,
        "turma_id": reserva.turma_id,
        "sala": reserva.sala,
        "data": reserva.data,
        "hora_inicio": reserva.hora_inicio,
        "hora_fim": reserva.hora_fim
    })

@reserva_bp.route("/atualizar/<int:id>", methods=["PUT"])
def atualizar_reserva(id):
    dados = request.json
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    turma_id = dados.get("turma_id")
    if not verificar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva.turma_id = turma_id
    reserva.sala = dados.get("sala")
    reserva.data = dados.get("data")
    reserva.hora_inicio = dados.get("hora_inicio")
    reserva.hora_fim = dados.get("hora_fim")

    db.session.commit()

    return jsonify({"mensagem": "Reserva atualizada com sucesso"})

@reserva_bp.route("/deletar/<int:id>", methods=["DELETE"])
def deletar_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    db.session.delete(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva deletada com sucesso"})