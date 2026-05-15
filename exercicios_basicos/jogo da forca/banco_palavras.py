import random

palavras_faceis = ["lua", "sol", "mar", "mel", "ceu", "pato", "gato",
                   "rato", "bola", "casa", "fogo", "copo", "mesa", "dado",
                   "flor", "mala", "bolo", "piso", "teto", "bala", "anel", "cama",
                   "muro", "dedo", "lata", "pote", "bicho", "cinto", "lousa",
                   "vento"]

palavras_medias = ["janela", "cadeado", "pipoca", "fazenda", "mercado", "espelho", 
                   "sorvete", "aviador", "cadeira", "desenho", "internet", "camiseta", 
                   "parafuso", "fantasia", "dinheiro", "telefone", "abacaxi", "montanha", 
                   "cachorro", "elefante", "passagem", "aventura", "computar", "bicicla", "soldado", 
                   "trabalho", "alimento", "chuveiro", "borracha", "armario"]

palavras_dificeis = ["abstrato", "xadrezista", "paradoxo",
                    "labirinto", "helicoptero", "metafora",
                    "ornitorrinco", "criptografia", "extraordinario",
                    "microscopio", "desenvolver", "arquipelago",
                    "invisibilidade", "circunferencia", "conhecimento",
                    "magnifico", "persistencia", "transmissao", "refrigerador",
                    "programador", "tempestade", "impressionar", "questionario",
                    "aventureiro", "eletricidade", "transformador", "sobrevivente",
                    "interrogacao", "computador", "desafiador"]

def selecionar_palavra (dificuldade):
    opcao_aleatoria = random.randint(0, 29)

    if dificuldade == 1:
        return palavras_faceis[opcao_aleatoria]
    elif dificuldade == 2:
        return palavras_medias[opcao_aleatoria]
    else: 
        return palavras_dificeis[opcao_aleatoria]

    