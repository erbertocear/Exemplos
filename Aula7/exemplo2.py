print("Bem-vind@s a Faculdade Católica da Paraíba")
user = input("Crie o nome do seu usuário: ")
password = input("Crie a sua senha: ")
#No momento do cadastro
while user == password:
    print("### Digite uma senha diferente do seu user ###")
    password = input("Crie a sua senha: ")
    if password != user:
        confirmesenha = input("Confirme a sua senha: ")
        while confirmesenha != password:
            print("As senhas não conferem!")
            confirmesenha = input("Confirme a sua senha: ")

print(user, " Você está logado no sistema")
