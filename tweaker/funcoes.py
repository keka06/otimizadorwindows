import subprocess
import webbrowser
import os

# Obtém o diretório atual do arquivo Python
current_dir = os.path.dirname(__file__)

def abrirGit():
    webbrowser.open("https://github.com/keka06")

def abrirIg():
    webbrowser.open("https://www.instagram.com/yzkaua__/")
  
def abrirPix():
    caminho_arquivo = (r'C:\kekaapp\qr\Pix do Keka.html')

    webbrowser.open(caminho_arquivo)

############################DEBLOAT
def debloat():
    debloatPS = os.path.join(current_dir, "1 - Debloat", "Windows10DebloaterGUI.ps1")
    comando = ["powershell", "-ExecutionPolicy", "Bypass", "-File", debloatPS]
    subprocess.run(comando, check=True)

def debloatCT():
    ct = os.path.join(current_dir, "1 - Debloat", "CTScript.ps1")
    comando = ["powershell", "-ExecutionPolicy", "Bypass", "-File", ct]
    subprocess.run(comando, check=True)

def restorePoint():
    resPoint = os.path.join(current_dir, "1 - Debloat", "res.cmd")
    subprocess.run([resPoint], check=True)

###########################LIMPEZA
def limparLog():
    limpLog = os.path.join(current_dir, "2 - Windows", "Limpeza", "Excluir arquivos de log.cmd")
    subprocess.run([limpLog], check=True)

def limparTemp():
    limpTemp = os.path.join(current_dir, "2 - Windows", "Limpeza", "Excluir arquivos temporário.cmd")
    subprocess.run([limpTemp], check=True)

###########################SERVIÇOS
def powerPlan():
    powerPlan = os.path.join(current_dir, "2 - Windows", "Serviços", "Ativar Maximo Desempenho.bat")
    subprocess.run([powerPlan], check=True)

def trim():
    trimP = os.path.join(current_dir, "2 - Windows", "Serviços", "Ativar Trim.bat")
    subprocess.run([trimP], check=True)

def services1():
    servicos1 = os.path.join(current_dir, "2 - Windows", "Serviços", "Desativar os Serviços mais Desnecessários.bat")
    subprocess.run([servicos1], check=True)

def services2():
    servicos2 = os.path.join(current_dir, "2 - Windows", "Serviços", "Desativar Serviços Desnecessários.bat")
    subprocess.run([servicos2], check=True)

def timerResolution():
    timerOff = os.path.join(current_dir, "2 - Windows", "Serviços", "Melhorar Latência (Timer Resolution).bat")
    subprocess.run([timerOff], check=True)

def ramOptimizer():
    otimizarRam = os.path.join(current_dir, "2 - Windows", "Serviços", "Otimizar Memoria ram.bat")
    subprocess.run([otimizarRam], check=True)

##############################WINDOWS
def windowsSettings():
    winConfig = os.path.join(current_dir, "2 - Windows", "Serviços", "Otimizar Todas as Configurações do Windows.bat")
    subprocess.run([winConfig], check=True)

def tweaksEssenciais():
    tweakE = os.path.join(current_dir, "2 - Windows", "Serviços", "Tweaks Essenciais.bat")
    subprocess.run([tweakE], check=True)

def fps():
    moreFps = os.path.join(current_dir, "2 - Windows", "+FPS.reg")
    subprocess.run(['regedit', '/s', moreFps], check=True)

def allGpu():
    allgpu = os.path.join(current_dir, "2 - Windows", "allGPU.bat")
    subprocess.run([allgpu], check=True)

def bcdedit():
    bcdt = os.path.join(current_dir, "2 - Windows", "BCD Tweaks.cmd")
    subprocess.run([bcdt], check=True)

def compactWin():
    compact = os.path.join(current_dir, "2 - Windows", "Compactação Básica do Sistema.cmd")
    subprocess.run([compact], check=True)

def disableUAC():
    uac = os.path.join(current_dir, "2 - Windows", "Desativar UAC.reg")
    subprocess.run(['regedit', '/s', uac], check=True)

def nvidiaGpu():
    nvidia = os.path.join(current_dir, "2 - Windows", "NvidiaGPU.bat")
    subprocess.run([nvidia], check=True)

def configWinReg():
    winReg = os.path.join(current_dir, "2 - Windows", "Otimize TODAS as configurações do Windows.reg")
    subprocess.run(['regedit', '/s', winReg], check=True)
