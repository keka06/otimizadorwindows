from funcoes import *
from apps import *
from customtkinter import *
from PIL import Image, ImageTk
import os

set_appearance_mode("dark")
set_default_color_theme("green")
janela = CTk()
janela.title("OptimizerByKeka")
janela.geometry("940x480")
janela.resizable(False,False)

'''icon = os.path.join(sys.path[0], "icone3.ico")
janela.iconbitmap(icon)'''

#########fonte principal
fonte_geral = "ebrima"
colorB = "#410076"
colorHb = "#280049"

#########adicionar imagem
current_dir = os.path.dirname(__file__)

# Define os caminhos das imagens usando os.path.join
git_path = os.path.join(current_dir, "img", "git.png")
ig_path = os.path.join(current_dir, "img", "ig.png")
pix_path = os.path.join(current_dir, "img", "pix.png")
play_path = os.path.join(current_dir, "img", "play3.png")

# Abre e redimensiona as imagens
git = Image.open(git_path)
git = git.resize((50, 50))
git_tk = ImageTk.PhotoImage(git)

ig = Image.open(ig_path)
ig = ig.resize((52, 50))
ig_tk = ImageTk.PhotoImage(ig)

pix = Image.open(pix_path)
pix = pix.resize((50, 50))
pix_tk = ImageTk.PhotoImage(pix)

play = Image.open(play_path)
play = play.resize((16, 20))
play_tk = ImageTk.PhotoImage(play)

titulo = CTkLabel(janela, text="Basic Tweaker", font=("Bahnschrift",30,"bold"),text_color="#8e7cc3")
titulo.pack(pady=(15,0))

# Criação da aba principal
aba_principal = CTkTabview(janela)
aba_principal.pack(padx=20, pady=15, fill="both", expand=True)

# Adiciona as abas principais
aba_principal.add("Inicio")
aba_principal.add("Debloat")
aba_principal.add("Windows")
aba_principal.add("Programas")

#aba inicio
keka = CTkLabel(aba_principal,text="© 2024 Kauã.",font=("calibri",10.5))
keka.place(x=3,y=378)

t1Frame = CTkFrame(aba_principal.tab("Inicio"), fg_color="#3c3c3c")
t1Frame.pack(pady=15)

t1 = CTkLabel(t1Frame, text="Otimizador criado por mim (keka)\nafim de melhorar o desempenho do seu computador.", font=(fonte_geral,14))
t1.pack(padx=30,pady=5)

botaoGit = CTkButton(aba_principal.tab("Inicio"), image=git_tk,
                     text="Acesse meu GitHub  ",
                     font=("",16,"bold"),
                     fg_color=colorB,
                     hover_color=colorHb,
                     border_width=3,
                     border_color=colorHb,
                     width=250,height=35,
                     command=abrirGit
                     )
botaoGit.pack(pady=(5,15))

botaoIg = CTkButton(aba_principal.tab("Inicio"),
                    image=ig_tk,
                    text="Siga-me no Instagram  ",
                    font=("Arial",16,"bold"),
                    fg_color=colorB,
                    hover_color=colorHb,
                    border_width=3,
                    border_color=colorHb,
                    width=250,height=35,
                    command=abrirIg
                    )
botaoIg.pack(pady=(0,15))

botaoPix = CTkButton(aba_principal.tab("Inicio"), image=pix_tk,
                     compound="left",
                     text="Me apoie",
                     font=("Arial",16,"bold"),
                     fg_color=colorB,
                     hover_color=colorHb,
                     border_width=3,
                     border_color=colorHb,
                     width=250,
                     height=35,
                     command=abrirPix,
                     )
botaoPix.pack(pady=(0,15))

#aba debloat
resText = CTkLabel(aba_principal.tab("Debloat"), text="\nCriar ponto de restauração")
resText.pack(padx=5,pady=10)

resButton = CTkButton(aba_principal.tab("Debloat"),text="Executar", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command = restorePoint)
resButton.pack(padx=5,pady=0)

debloatText = CTkLabel(aba_principal.tab("Debloat"), text="Debloat windows")
debloatText.place(x=295,y=110)

debloatButton = CTkButton(aba_principal.tab("Debloat"), text="Executar", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=debloat)
debloatButton.place(x=275,y=140)

ctText = CTkLabel(aba_principal.tab("Debloat"), text="Chris Titus Script")
ctText.place(x=495,y=110)

ctButton = CTkButton(aba_principal.tab("Debloat"),text="Executar", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=debloatCT)
ctButton.place(x=475,y=140)

texto3="NOTA: É importante criar um ponto de restauração\ncaso não fique satisfeito com os resultados."

notas3Fundo = CTkFrame(aba_principal.tab("Debloat"), fg_color="#3c3c3c",width=200,height=50)
notas3Fundo.place(x=265,y=280)

notas3 = CTkLabel(notas3Fundo,text=texto3, font=("consolas", 13))
notas3.pack(padx=15,pady=5)

#aba windows
windows_frame = CTkTabview(aba_principal.tab("Windows"))
windows_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Adiciona as abas secundárias Outros, Limpeza, Serviços
windows_frame.add("Outros")
windows_frame.add("Limpeza")
windows_frame.add("Serviços")

#aba outros
uacButton = CTkButton(windows_frame.tab("Outros"), text="Desativar UAC", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=disableUAC)
uacButton.place(x=160,y=25)

bcdButton = CTkButton(windows_frame.tab("Outros"), text="BCD Tweaks", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=bcdedit)
bcdButton.place(x=360,y=25)

fpsButton = CTkButton(windows_frame.tab("Outros"), text="+FPS (regedit)",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=fps)
fpsButton.place(x=560,y=25)

allGpuButton = CTkButton(windows_frame.tab("Outros"), text="all GPU Tweaks", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=allGpu)
allGpuButton.place(x=260,y=85)

nvidiaGpuButton = CTkButton(windows_frame.tab("Outros"), text="Nvidia GPU Tweaks", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=nvidiaGpu)
nvidiaGpuButton.place(x=460, y=85)

configWinRegButton = CTkButton(windows_frame.tab("Outros"), text="Config. Win (regedit)",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=configWinReg)
configWinRegButton.place(x=260,y=145)

compactWinButton = CTkButton(windows_frame.tab("Outros"), text="Compactar Windows",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=compactWin)
compactWinButton.place(x=460,y=145)

texto1 = "NOTAS: 'Compactar Windows' é a compactação básica\nleva até 10 minutos pra ser concluída.\n\n'Nvidia GPU' mexe com arquivos .reg\ne as configurações do painel Nvidia."

notas1Fundo = CTkFrame(windows_frame.tab("Outros"), fg_color="#3c3c3c",width=200,height=50)
notas1Fundo.place(x=240,y=200)

notas1 = CTkLabel(notas1Fundo,text=texto1,font=("consolas", 13))
notas1.pack(padx=20,pady=5)

#aba limpeza
limparLogButton = CTkButton(windows_frame.tab("Limpeza"),text="Limpar arquivos de log", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=limparLog)
limparLogButton.pack(padx=10,pady=25)

limparTempButton = CTkButton(windows_frame.tab("Limpeza"),text="Limpar arquivos temporários",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=limparTemp)
limparTempButton.pack(padx=10,pady=10)

#aba serviços
powerPlanButton = CTkButton(windows_frame.tab("Serviços"), text="Plano de energia", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=powerPlan)
powerPlanButton.place(x = 105,y=25)

trimButton = CTkButton(windows_frame.tab("Serviços"), text="Ativar trim", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=trim)
trimButton.place(x=275, y=25)

servicos1Button = CTkButton(windows_frame.tab("Serviços"), text="Desativar Serviços 1",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=services1)
servicos1Button.place(x=445,y=25)

services2Button = CTkButton(windows_frame.tab("Serviços"), text="Desativar Serviços 2", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=services2)
services2Button.place(x=615,y=25)

timerResolutionButton = CTkButton(windows_frame.tab("Serviços"), text="Melhorar latência",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=timerResolution)
timerResolutionButton.place(x=105, y=100)

ramOptimizerButton = CTkButton(windows_frame.tab("Serviços"), text="Otimizar Ram",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=ramOptimizer)
ramOptimizerButton.place(x=275,y=100)

winSettingsButton = CTkButton(windows_frame.tab("Serviços"), text="Config. do win",font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb, command=windowsSettings)
winSettingsButton.place(x=445,y=100)

tweaksButton = CTkButton(windows_frame.tab("Serviços"), text="Tweaks Essenciais", font=(fonte_geral,14),fg_color=colorB, hover_color=colorHb,command=tweaksEssenciais)
tweaksButton.place(x=615,y=100)

texto2="NOTAS: 'Plano de energia' adiciona um novo plano de energia.\npara melhor desempenho\n\n'Melhorar Latência' ativa o timer resolution.\n\n'Ativar Trim' melhora o desempenho de\nHDs e SSDs."

notas2Fundo = CTkFrame(windows_frame.tab("Serviços"), fg_color="#3c3c3c",width=200,height=50)
notas2Fundo.place(x=200,y=170)

notas2 = CTkLabel(notas2Fundo,text=texto2, font=("consolas",13))
notas2.pack(padx=20,pady=5)

#aba programas
programas_fundo = CTkScrollableFrame(aba_principal.tab("Programas"),fg_color="#2b2b2b", width=560,height=500)
programas_fundo.pack()

autorunsFrame = CTkFrame(programas_fundo,fg_color="#3c3c3c")
autorunsFrame.place(x=60,y=10)

autoRunsText = CTkLabel(autorunsFrame,text="AutoRuns", font=(fonte_geral,17,"bold"))
autoRunsText.pack(padx=6,pady=1)

autoRunsButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_autoruns)
autoRunsButton.place(x=20,y=10)

msiUtilFrame = CTkFrame(programas_fundo,fg_color="#3c3c3c")
msiUtilFrame.place(x=60, y=70)

msiUtilText = CTkLabel(msiUtilFrame,text="MSI Util v3", font=(fonte_geral,15,"bold"))
msiUtilText.pack(padx=6,pady=1)

msiUtilButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_msi)
msiUtilButton.place(x=20, y=70)

powerSettingsFrame = CTkFrame(programas_fundo, fg_color="#3c3c3c")
powerSettingsFrame.place(x=65, y=130)

powerSettingsText = CTkLabel(powerSettingsFrame,text="Power Settings Explorer", font=(fonte_geral,15,"bold"))
powerSettingsText.pack()

PowerSettingsButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_pwrset)
PowerSettingsButton.place(x=20, y=130)

tempFrame = CTkFrame(programas_fundo, fg_color="#3c3c3c")
tempFrame.place(x=60,y=190)

tempText = CTkLabel(tempFrame,text="Temp Cleaner", font=(fonte_geral,15,"bold"))
tempText.pack(padx=6,pady=1)

tempButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_temp)
tempButton.place(x=20,y=190)

unparkframe = CTkFrame(programas_fundo, fg_color="#3c3c3c")
unparkframe.place(x=340,y=10)

unparkText = CTkLabel(unparkframe,text="Unpark Cpu", font=(fonte_geral,15,"bold"))
unparkText.pack(padx=5,pady=1)

unparkButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_unpark)
unparkButton.place(x=300,y=10)

uwt4Frame = CTkFrame(programas_fundo,fg_color="#3c3c3c")
uwt4Frame.place(x=340,y=70)

uwt4Text = CTkLabel(uwt4Frame, text = "Ultimate Windows Tweaker",font=(fonte_geral,15,"bold"))
uwt4Text.pack(padx=6,pady=1)

uwt4Button = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_uwt4)
uwt4Button.place(x=300,y=70)

deviceCleanerFrame = CTkFrame(programas_fundo, fg_color="#3c3c3c")
deviceCleanerFrame.place(x=340,y=130)

deviceCleanerText = CTkLabel(deviceCleanerFrame, text = "Device Cleanup",font=(fonte_geral,15,"bold"))
deviceCleanerText.pack(padx=6,pady=1)

deviceCleanerButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_deviceCleanup)
deviceCleanerButton.place(x=300,y=130)

wubFrame = CTkFrame(programas_fundo, fg_color="#3c3c3c")
wubFrame.place(x=340,y=190)

wubText = CTkLabel(wubFrame, text = "Windows Update Blocker",font=(fonte_geral,15,"bold"))
wubText.pack(padx=6,pady=1)

wubButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_wub)
wubButton.place(x=300,y=190)

dismFrame = CTkFrame(programas_fundo, fg_color="#3c3c3c")
dismFrame.pack(pady=(260,0))

dismText = CTkLabel(dismFrame, text = "Dism++",font=(fonte_geral,15,"bold"))
dismText.pack(padx=6,pady=1)

dismButton = CTkButton(programas_fundo,text="",image=play_tk,fg_color="#2b2b2b", hover_color="#2b2b2b",width=32,height=32,command=execute_dism)
dismButton.place(x=207,y=260)

def adicionar_texto():
    texto = "Auto Runs: programa usado para desabilitar vários serviços ao iniciar owindows.\n\nMSI Util V3: utilize para ativar o modo MSI na placa de vídeo (modo MSImelhora a comunicação entre a placa de vídeo e o computador).\n\nPower Settings Explorer: exibe configurações de energia ocultas do \nWindows, pode ser configurada nas opções de energia.\n\nTemp Cleaner: limpa arquivos temporários.\n\nUnpark CPU: ativação de núcleos \"Parqueados\" para economizar energia.\n\nUWT4: ferramenta para mudar algumas configurações de registro do \nwindows afim de ganhar desempenho.\n\nDevice Cleanup Tool: remova entradas do gerenciador de dispositivos quesão salvas no registro, isso são apenas arquivos temporários.\n\nWindows Update Blocker: bloqueia permanentemente as atualizações \ndo windows com apenas um clique (também reverte isso com apenas um \nclique).\n\nDISM++: Permite excluir diversos arquivos temporários, log, desinstalardrivers e aplicativos instalados na sua máquina."
    text_box.insert("end", texto)

# Cria a caixa de texto com tamanho definido
text_box = CTkTextbox(programas_fundo, font=("consolas",11),width=450, height=340)  # Defina o tamanho desejado aqui
text_box.pack(pady=(50,0))

text_box.bind("<Button-1>", lambda event: "break")
adicionar_texto()

janela.mainloop()
