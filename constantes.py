import os
from dotenv import load_dotenv

load_dotenv()

ALTURA_MAPA = int(os.getenv("ALTURA_MAPA", 600))
LARGURA_MAPA = int(os.getenv("LARGURA_MAPA", 900))

NUM_AGENTES = int(os.getenv("NUM_AGENTES", 20))
FPS = int(os.getenv("FPS", 60))

VELOCIDADE_AGENTE = float(os.getenv("VELOCIDADE_AGENTE", 200))
