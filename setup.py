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
    print "Instalation de minecraft finie!"

