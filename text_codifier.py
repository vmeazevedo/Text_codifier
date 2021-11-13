from decenc import *
from datetime import datetime
from pyfiglet import figlet_format

hora = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

# FUNÇÃO DE CRIPTOGRAFIA
def encoder(path_in,file_in,file_out):
    input = str(path_in+file_in)
    text = Encoder(input)
    # Codificando o texto   
    text.encode(size=(300, 300))
    print('\033[32m'+"\nArquivo codificado com sucesso!"+'\033[0;0m')
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
    print('\033[32m'+"\nArquivo decodificado com sucesso!"+'\033[0;0m')
    # Salvando o texto
    path_out = path_in
    file_out = "decode_file.txt"
    output = str(path_out+hora+"_"+file_out)
    image.save(output)


def logo():
    print("========================================================")
    print(figlet_format("Text Codifier°", font="standard"))
    print("========================================================")

# MENU DE OPÇÕES
def menu():
    while True:
        logo()
        print("[1] - Codificar")
        print("[2] - Decodificar")
        print("[0] - Sair")
        print("====================")
        option = input("\nEscolha uma opção: ")
        if option == '1':
            path_in = input("Diretório do arquivo [C:path/]: ")
            file_in = input("Nome do arquivo [.txt]: ")
            file_out = input("Nome do arquivo de saída [.png]: ")
            try:
                encoder(path_in,file_in,file_out)
                break
            except:
                print('\033[31m'+"\nErro ao tentar codificar o arquivo!"+'\033[0;0m')
                print("Por favor, verifique que o diretorio e o arquivo esteja corretos.\n")

        elif option == '2':
            path_in = input("Diretório do arquivo [C:path/]: ")
            file_in = input("Nome do arquivo [.png]: ")
            try:
                decoder(path_in,file_in)
                break
            except:
                print('\033[31m'+"\nErro ao tentar decodificar o arquivo!"+'\033[0;0m')
                print("Por favor, verifique que o diretorio e o arquivo esteja corretos.\n")

        elif option == '0':
            break
        else:
            print("\nOpção inválida!")

menu()
