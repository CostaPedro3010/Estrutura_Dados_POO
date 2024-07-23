from escola import Disciplina

def main():
    nome_disciplina = input("Digite o nome da disciplina: ")
    nota1 = float(input("Digite a primeira nota (0.0 a 10.0): "))
    nota2 = float(input("Digite a segunda nota (0.0 a 10.0): "))

    disciplina = Disciplina(nome_disciplina, nota1, nota2)
    media = disciplina.calcularMedia()
    situacao = disciplina.exibirSituacao()

    print(f"\nDisciplina: {nome_disciplina}")
    print(f"Notas: {nota1}, {nota2}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()