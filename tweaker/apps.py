import subprocess
import os

# Função genérica para executar um executável com privilégios de administrador
def execute_exe_as_admin(exe_path):
    # Verifica se o arquivo existe antes de tentar executá-lo
    if os.path.isfile(exe_path):
        print(f"Executando o arquivo '{exe_path}' como administrador.")
        try:
            # Executa o arquivo com privilégios elevados
            subprocess.run(
                ["powershell", "-Command", f"Start-Process '{exe_path}' -Verb RunAs"],
                check=True
            )
            print(f"Arquivo '{exe_path}' executado com privilégios de administrador.")
        except subprocess.CalledProcessError:
            print(f"Erro: Não foi possível executar '{exe_path}' como administrador.")
    else:
        print(f"Erro: O arquivo '{exe_path}' não foi encontrado.")

# Funções específicas para cada arquivo executável com caminhos definidos
def execute_autoruns():
    execute_exe_as_admin("C:\\tweaker\\Programas\\AutoRuns.exe")

def execute_msi():
    execute_exe_as_admin("C:\\tweaker\\Programas\\MSI Util V3.exe")

def execute_pwrset():
    execute_exe_as_admin("C:\\tweaker\\Programas\\PowerSettingsExplorer.exe")

def execute_temp():
    execute_exe_as_admin("C:\\tweaker\\Programas\\Temp Cleaner.exe")

def execute_unpark():
    execute_exe_as_admin("C:\\tweaker\\Programas\\unparkcpu.exe")

def execute_uwt4():
    execute_exe_as_admin("C:\\tweaker\\Programas\\uwt4.exe")

def execute_deviceCleanup():
    execute_exe_as_admin("C:\\tweaker\\Programas\\DeviceCleanup.exe")

def execute_wub():
    execute_exe_as_admin("C:\\tweaker\\Programas\\Wub.exe")

def execute_dism():
    execute_exe_as_admin("C:\\tweaker\\Programas\\Dism++x64.exe")
