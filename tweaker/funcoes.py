import subprocess
import webbrowser
import os
from plyer import notification
import ctypes

# Função para abrir links
def abrirGit():
    webbrowser.open("https://github.com/keka06")

def abrirIg():
    webbrowser.open("https://www.instagram.com/yzkaua__/")
  
def abrirPix():
    caminho_arquivo = r'C:\kekaapp\qr\Pix do Keka.html'
    webbrowser.open(caminho_arquivo)

# Função para exibir uma notificação nativa
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # A notificação desaparecerá após 10 segundos
    )

def show_message(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)  # 0x40 -> Informação, 0x1 -> Botão OK

# Função para rodar o script como administrador
def run_script_as_admin(script_path):
    try:
        if os.path.isfile(script_path):
            if script_path.endswith('.reg'):
                comando = f"regedit /s \"{script_path}\""
                subprocess.run(comando, check=True, shell=True)
                
                # Exibir a mensagem quando o registro for aplicado
                show_message("Registro Importado", f"O arquivo de registro foi importado com sucesso: {script_path}")
                show_notification("Conclusão", f"Registro importado com sucesso: {script_path}")

            elif script_path.endswith('.ps1'):
                comando = f"powershell -ExecutionPolicy Bypass -File \"{script_path}\""
                subprocess.run(comando, check=True, shell=True)
                show_notification("Conclusão", f"Script PowerShell executado com sucesso: {script_path}")
            
            elif script_path.endswith('.cmd') or script_path.endswith('.bat'):
                comando = f"start cmd /c \"{script_path}\""
                subprocess.run(comando, check=True, shell=True)
                show_notification("Conclusão", f"Script .cmd ou .bat executado com sucesso: {script_path}")

            else:
                show_notification("Erro", f"Erro: Tipo de arquivo desconhecido: {script_path}")
        else:
            show_notification("Erro", f"Erro: O arquivo '{script_path}' não foi encontrado.")
    except subprocess.CalledProcessError as e:
        show_notification("Erro", f"Erro ao executar o script: {script_path}")

# Caminhos para os scripts
def debloat():
    debloatPS = r"C:\tweaker\Debloat\Windows10DebloaterGUI.ps1"
    run_script_as_admin(debloatPS)

def debloatCT():
    ct = r"C:\tweaker\Debloat\CTScript.ps1"
    run_script_as_admin(ct)

def restorePoint():
    resPoint = r"C:\tweaker\Debloat\res.cmd"
    run_script_as_admin(resPoint)

# Limpeza de arquivos
def limparLog():
    limpLog = r"C:\tweaker\Windows\Limpeza\Excluir arquivos de log.cmd"
    run_script_as_admin(limpLog)

def limparTemp():
    limpTemp = r"C:\tweaker\Windows\Limpeza\Excluir arquivos temporário.cmd"
    run_script_as_admin(limpTemp)

# Serviços do Windows
def powerPlan():
    powerPlan = r"C:\tweaker\Windows\Serviços\Ativar Maximo Desempenho.bat"
    run_script_as_admin(powerPlan)

def trim():
    trimP = r"C:\tweaker\Windows\Serviços\Ativar Trim.bat"
    run_script_as_admin(trimP)

def services1():
    servicos1 = r"C:\tweaker\Windows\Serviços\Desativar os Serviços mais Desnecessários.bat"
    run_script_as_admin(servicos1)

def services2():
    servicos2 = r"C:\tweaker\Windows\Serviços\Desativar Serviços Desnecessários.bat"
    run_script_as_admin(servicos2)

def timerResolution():
    timerOff = r"C:\tweaker\Windows\Serviços\Melhorar Latência (Timer Resolution).bat"
    run_script_as_admin(timerOff)

def ramOptimizer():
    otimizarRam = r"C:\tweaker\Windows\Serviços\Otimizar Memoria ram.bat"
    run_script_as_admin(otimizarRam)

# Configurações do Windows
def windowsSettings():
    winConfig = r"C:\tweaker\Windows\Serviços\Otimizar Todas as Configurações do Windows.bat"
    run_script_as_admin(winConfig)

def tweaksEssenciais():
    tweakE = r"C:\tweaker\Windows\Serviços\Tweaks Essenciais.bat"
    run_script_as_admin(tweakE)

def fps():
    moreFps = r"C:\tweaker\Windows\+FPS.reg"
    run_script_as_admin(moreFps)

def allGpu():
    allgpu = r"C:\tweaker\Windows\allGPU.bat"
    run_script_as_admin(allgpu)

def bcdedit():
    bcdt = r"C:\tweaker\Windows\BCD Tweaks.cmd"
    run_script_as_admin(bcdt)

def compactWin():
    compact = r"C:\tweaker\Windows\Compactação Básica do Sistema.cmd"
    run_script_as_admin(compact)

def disableUAC():
    uac = r"C:\tweaker\Windows\Desativar UAC.reg"
    run_script_as_admin(uac)

def nvidiaGpu():
    nvidia = r"C:\tweaker\Windows\NvidiaGPU.bat"
    run_script_as_admin(nvidia)

def configWinReg():
    winReg = r"C:\tweaker\Windows\Otimize TODAS as configurações do Windows.reg"
    run_script_as_admin(winReg)

def executar_regedits_sistema():
    regedit_files = [
        r"C:\tweaker\Regedits\Sistema\Aumentar Frequência da CPU & GPU.reg",
        r"C:\tweaker\Regedits\Sistema\Aumentar Taxa de Transmissão de Dados (Internet).reg",
        r"C:\tweaker\Regedits\Sistema\Desativar o Gerenciador de mapas.reg",
        r"C:\tweaker\Regedits\Sistema\Desativar PowerThrottling.reg",
        r"C:\tweaker\Regedits\Sistema\Desativar Prefetch.reg",
        r"C:\tweaker\Regedits\Sistema\Desativar serviços de diagnóstico e telemetria.reg",
        r"C:\tweaker\Regedits\Sistema\Desativar serviços extras desnecessários.reg",
        r"C:\tweaker\Regedits\Sistema\Desativar Superfetch.reg",
        r"C:\tweaker\Regedits\Sistema\Diminuir Processos.reg",
        r"C:\tweaker\Regedits\Sistema\Otimizações Basicas do Registro.reg",
        r"C:\tweaker\Regedits\Sistema\Tweaks Necessários.reg"
    ]
    
    # Executa cada arquivo .reg da lista
    for reg_file in regedit_files:
        run_script_as_admin(reg_file)

    # Exibe a mensagem final
    show_message("Conclusão", "Todos os regedits foram aplicados com sucesso!")