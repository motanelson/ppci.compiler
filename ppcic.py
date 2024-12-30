from io import StringIO
from ppci.api import cc, link, objcopy
import os
import io

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


def compile_c_to_binary():
    # Solicitar o nome do arquivo ao usuário
    file_name = input("Digite o nome do arquivo C (com extensão .c): ").strip()

    if not os.path.exists(file_name):
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        return

    # Verificar extensão do arquivo
    if not file_name.endswith('.c'):
        print("Erro: Certifique-se de fornecer um arquivo com extensão .c.")
        return

    # Definir nomes dos arquivos intermediários e do binário
    obj_file = file_name.replace('.c', '.o')
    linked_file = file_name.replace('.c', '.elf')
    binary_file = file_name.replace('.c', '.bin')

    try:
        # Etapa 1: Compilação
        print("Compilando o código C...")
        source_file =""
        with open(file_name, 'r') as source:
            source_file = io.StringIO(source.read())
        obj = cc(source_file , 'x86_64')  # Alvo: x86_64
        print(obj)
        
        with open(obj_file, 'w') as obj_out:
            obj.save(obj_out)
        print(f"Arquivo objeto gerado: {obj_file}")
        
        # Etapa 2: Linkagem
        print("Linkando o arquivo objeto...")
        objs=link([obj], "link.ld", 'x86_64')

        with open(linked_file, 'w') as linked_out:
            objs.save(linked_out)
        print(f"Arquivo ELF gerado: {linked_file}")
        
        # Etapa 3: Conversão para binário
        print("Convertendo para binário...")
        
        
        
       
    except Exception as e:
        print(f"Erro durante o processo: {e}")

if __name__ == "__main__":
    print("\033c\033[43;30m")
    compile_c_to_binary()

