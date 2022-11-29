from setuphelpers import *

uninstallkey = []

installerURL = "https://launcher.mojang.com/download/MinecraftInstaller.msi"

def install():
    print "On lance l'installation de Minecraft"
    if iswin64():
        #argument pris sur https://github.com/TheCakeIsNaOH/chocolatey-packages/tree/master/minecraft-launcher
        run(r'"MinecraftInstaller.msi" /qn /norestart /l*v ') 
    else():
        print "Architecture non supportée"
    print "On lance le launcher pour le mettre à jour"
    run(r'"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe" --help') #on utilise l'option --help pour avoir uniquement l'update
    print "Instalation de minecraft finie!"

