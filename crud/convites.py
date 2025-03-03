# Funções CRUD para convites
from database import supabase
from schemas import ConviteSchema
import uuid
from datetime import datetime

def get_convite(uuid: str):
    # Busca o convite pelo UUID
    response = supabase.table("convites").select("*").eq("id", uuid).single().execute()

    if not response.data:
        return None

    convite = response.data

    # Busca o aniversariante se houver um ID associado
    aniversariante_id = convite.get("aniversariante_id")
    if aniversariante_id:
        #print(f"🔎 Buscando aniversariante com ID: {aniversariante_id}")  # Depuração

        aniversariante_response = (
            supabase.table("aniversariantes")
            .select("nome")
            .eq("id", str(aniversariante_id))
            .maybe_single()
            .execute()
        )

        # Verifica se aniversariante_response não é None antes de acessar .data
        if aniversariante_response and aniversariante_response.data:
            convite["nome_aniversariante"] = aniversariante_response.data["nome"]
        else:
            #print(f"⚠ Nenhum aniversariante encontrado para ID {aniversariante_id}")
            convite["nome_aniversariante"] = "Desconhecido"
    else:
        convite["nome_aniversariante"] = "Não informado"

    return convite




def create_convite(convite: ConviteSchema):
    convite_data = convite.dict()
    convite_data["id"] = str(uuid.uuid4())
    #convite_data["created_at"] = datetime.utcnow()
    response = supabase.table("convites").insert(convite_data).execute()
    return response.data
