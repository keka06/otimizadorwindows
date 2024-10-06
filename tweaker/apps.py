import subprocess
import os

def execute_autoruns():
    caminho_bat = r"C:\kekaapp\.bat\autoruns.bat"
    subprocess.run(caminho_bat, check=True)

def execute_msi():
    caminho_bat = r"C:\kekaapp\.bat\msiutil.bat"
    subprocess.run(caminho_bat, check=True)

def execute_pwrset():
    caminho_bat = r"C:\kekaapp\.bat\powersettings.bat"
    subprocess.run(caminho_bat, check=True)

def execute_temp():
    caminho_bat = r"C:\kekaapp\.bat\tempcleaner.bat"
    subprocess.run(caminho_bat, check=True)

def execute_unpark():
    caminho_bat = r"C:\kekaapp\.bat\unparkcpu.bat"
    subprocess.run(caminho_bat, check=True)

def execute_uwt4():
    caminho_bat = r"C:\kekaapp\.bat\uwt4.bat"
    subprocess.run(caminho_bat, check=True)

def execute_deviceCleanup():
    caminho_bat = r"C:\kekaapp\.bat\cleanup.bat"
    subprocess.run(caminho_bat, check=True)

def execute_wub():
    caminho_bat = r"C:\kekaapp\.bat\wub.bat"
    subprocess.run(caminho_bat, check=True)

def execute_dism():
    caminho_bat = r"C:\kekaapp\.bat\dism.bat"
    subprocess.run(caminho_bat, check=True)
