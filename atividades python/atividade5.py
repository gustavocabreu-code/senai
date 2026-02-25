computador=0
soma=0
while computador < 4:
    computador+=1
    nota = float(input(f"insira a {computador} nota"))
    soma+=nota

media= soma/computador
print ("a media das notas: ",media)
if media >= 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")
     



