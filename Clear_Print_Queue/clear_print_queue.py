import os
import subprocess

def clear_print_queue():
    print("Parando o serviço de spooler de impressão...")
    os.system("net stop spooler")
    
    print("Limpando a fila de impressão...")
    folder = r'C:\Windows\System32\spool\PRINTERS'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'Falha ao apagar {file_path}. Razão: {e}')
    
    print("Reiniciando o serviço de spooler de impressão...")
    os.system("net start spooler")
    print("Fila de impressão limpa com sucesso.")
    input("Pressione qualquer tecla para finalizar...")

if __name__ == "__main__":
    clear_print_queue()
