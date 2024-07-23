# Sistema de Avaliação de Disciplinas

Este projeto implementa uma classe `Disciplina` que permite calcular a média das notas de um aluno em uma disciplina e determinar sua situação (Aprovado, Em Recuperação ou Reprovado) com base na média.

## Estrutura do Projeto

- `escola.py`: Contém a definição da classe `Disciplina`.
- `main.py`: Script principal que interage com o usuário para coletar dados, calcular a média e exibir a situação do aluno.

## Classe Disciplina

A classe `Disciplina` possui os seguintes métodos:

- `__init__(self, nome: str, nota1: float, nota2: float)`: Inicializa a disciplina com o nome e as duas notas do aluno.
- `calcularMedia(self) -> float`: Retorna a média aritmética das duas notas do aluno.
- `exibirSituacao(self) -> str`: Retorna a situação do aluno com base na média:
  - "Aprovado" se a média for maior ou igual a 6.0.
  - "Em Recuperação" se a média for maior ou igual a 4.0 e menor que 6.0.
  - "Reprovado" se a média for menor que 4.0.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone o repositório ou baixe os arquivos `escola.py` e `main.py`.

3. Execute o script `main.py`:
````
Pergunta para o Usuário:

Digite o nome da disciplina: Matemática
Digite a primeira nota (0.0 a 10.0): 8.0
Digite a segunda nota (0.0 a 10.0): 6.0
````
````
Resposta do Programa:
 
Disciplina: Matemática
Notas: 8.0, 6.0
Média: 7.00
Situação: Aprovado