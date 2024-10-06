import subprocess
import os

def execute_autoruns():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "autoruns.bat")
    subprocess.run(caminho_bat, check=True)

def execute_msi():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "msiutil.bat")
    subprocess.run(caminho_bat, check=True)

def execute_pwrset():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "powersettings.bat")
    subprocess.run(caminho_bat, check=True)

def execute_temp():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "tempcleaner.bat")
    subprocess.run(caminho_bat, check=True)

def execute_unpark():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "unparkcpu.bat")
    subprocess.run(caminho_bat, check=True)

def execute_uwt4():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "uwt4.bat")
    subprocess.run(caminho_bat, check=True)

def execute_deviceCleanup():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "cleanup.bat")
    subprocess.run(caminho_bat, check=True)

def execute_wub():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "wub.bat")
    subprocess.run(caminho_bat, check=True)

def execute_dism():
    caminho_bat = os.path.join("C:", os.sep, "kekaapp", ".bat", "dism.bat")
    subprocess.run(caminho_bat, check=True)
