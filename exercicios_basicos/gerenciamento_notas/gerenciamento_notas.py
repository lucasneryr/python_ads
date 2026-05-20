alunos = [
    {
    "Nome": "Alice",
    "Nota": [8.5, 9.2, 7.8],
    },
    {
    "Nome": "Bruno",
    "Nota": [7.2, 4.8, 7.5],
    },
    {
    "Nome": "Lucas",
    "Nota": [4.6, 2.9, 5.3]
    }
]

def calcular_media(notas):
    """
    Soma todas as notas do aluno e divide pela quantidade de notas.

    Args:
        notas: (list[float]): Lista de notas do aluno.
    
    Returns:
        float: Média das notas arredondadas para duas casas decimais.
    """
    media = sum(notas) / len("Nota")
    return round(media, 2)

def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se a média das notas do aluno está acima ou abaixo de 7

    Args
        media (float): Média das notas arredondadas para duas casas decimais.
        media_minima (float): Mínimo de média que aluno precisa para ser aprovado.
    
    Returns
        str: Retorna "Aprovado" ou "Reprovado" dependendo da média do aluno.
    """
    aprovacao = "Reprovado"
    if media >= media_minima:
        aprovacao = "Aprovado"
    else:
        return aprovacao

def gerar_relatorio(alunos): 
    """
    Gera um relatório que exibe nome, média e aprovação do aluno.

    Args:
        alunos (list[dict[str, str | str, list[float]]]): registro do nome e notas de cada aluno
    """
    for i in range(len(alunos)):
        media = calcular_media(alunos[i]["Nota"])
        print(f"Nome: {alunos[i]["Nome"]}") # Nome
        print(f"Média: {media}") # Média
        print(f"{verificar_aprovacao(media)}") # Aprovado / Reprovado
        print(f"{"=" * 20}")

gerar_relatorio(alunos)