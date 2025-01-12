aluno= []
alunos = []
while True:
    aluno.append(input("Nome: "))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    alunos.append(aluno[:])
    aluno.clear()
    saida = input("Quer continuar? (S/N)")
    if saida in "Nn":
        break
print("------------------------")
print(f"{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}")
print("------------------------")
for i, j in enumerate(alunos):
    print(f"{i:<4}{alunos[i][0]:<10} {(alunos[i][1]+alunos[i][2])/2:>8.1f}")
print("------------------------")

while True:
    numero = int(input("Mostrar notas de qual aluno? (99 interrompe) "))
    if numero == 99:
        break
    print(f"Notas de {alunos[numero][0]} são [{alunos[numero][1]}, {alunos[numero][2]}]")
    
