from decenc import *
from datetime import datetime

hora = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")


# FUNÇÃO DE CRIPTOGRAFIA
def encoder(path_in,file_in,file_out):
    input = str(path_in+file_in)
    text = Encoder(input)
    # Codificando o texto   
    text.encode(size=(500, 500))
    # Vendo a imagem gerada
    text.show()
    # Salvando a imagem
    path_out = path_in
    output = str(path_out+file_out)
    text.save(output)

# FUNÇÃO DE DECRIPTOGRAFIA
def decoder(path_in,file_in):
    input = str(path_in+file_in)
    image = Decoder(input)
    # Decodificando a imagem
    image.decode()
    # Vendo o texto
    image.show()
    # Salvando o texto
    path_out = path_in
    file_out = "decode_file.txt"
    output = str(path_out+hora+"_"+file_out)
    image.save(output)

# MENU DE OPÇÕES
def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("\n[1] - Codificar")
        print("[2] - Decodificar")
        print("[0] - Sair")
        option = input("\nEscolha uma opção: ")
        if option == '1':
            path_in = input("Informe o diretório onde esta o arquivo [C:path/]: ")
            file_in = input("Informe o nome do arquivo [.txt]: ")
            file_out = input("Informe o nome do arquivo de saída [.png]: ")
            try:
                encoder(path_in,file_in,file_out)
                print('\033[32m'+"\nArquivo codificado com sucesso!"+'\033[0;0m')
                escolha = input("Deseja codificar outro arquivo? [S/N]: ")
                if escolha == 'S':
                    continue
                else:
                    break
            except:
                print('\033[31m'+"\nErro ao tentar codificar o arquivo!"+'\033[0;0m')
                print("Por favor, verifique que o diretorio e o arquivo esteja corretos.\n")

        elif option == '2':
            path_in = input("Informe o diretório onde esta o arquivo [C:path/]: ")
            file_in = input("Informe o nome do arquivo [.png]: ")
            try:
                decoder(path_in,file_in)
                print("\nArquivo decodificado com sucesso!")
                escolha = input("Deseja decodificar outro arquivo? [S/N]: ")
                if escolha == 'S':
                    continue
                else:
                    break
            except:
                print('\033[31m'+"\nErro ao tentar decodificar o arquivo!"+'\033[0;0m')
                print("Por favor, verifique que o diretorio e o arquivo esteja corretos.\n")

        elif option == '0':
            break
        else:
            print("\nOpção inválida!")

menu()