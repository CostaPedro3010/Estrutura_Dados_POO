class Disciplina:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcularMedia(self) -> float:
        return (self.nota1 + self.nota2) / 2

    def exibirSituacao(self) -> str:
        media = self.calcularMedia()
        if media >= 6.0:
            return "Aprovado"
        elif media >= 4.0:
            return "Em Recuperação"
        else:
            return "Reprovado"
