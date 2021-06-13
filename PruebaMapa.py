import os
import random
import pickle
import time
import heroes
import monster

class Nivel():
    def __init__(self, piso):
        self.piso=piso
        self.i=0
        self.cuartos=[]
        #Codigo de cuartos M=Monstruo, T=Tesoro, F=Fogata, A=Escaleras arriba, B=Escaleras aBajo
        if self.piso == 1:
            self.pool=['M', 'M', 'M', 'M', 'M', 'M', 'M', 'T', 'T', 'T', 'T', 'T', 'F', 'F']
            random.shuffle(self.pool)
            while self.i<7:
                self.cuartos.append(self.pool[self.i])
                self.i=self.i+1
            self.cuartos.append('A')
            self.cuartos.append('B')
            self.cuartos.append('F')
            random.shuffle(self.cuartos)
            random.shuffle(self.cuartos)
            self.mascara=['?','?','?','?','?','?','?','?','?','?']
        if self.piso == 2:
            self.pool=['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'F', 'F']
            random.shuffle(self.pool)
            while self.i<12:
                self.cuartos.append(self.pool[self.i])
                self.i=self.i+1
            self.cuartos.append('A')
            self.cuartos.append('B')
            self.cuartos.append('F')
            random.shuffle(self.cuartos)
            random.shuffle(self.cuartos)
            self.mascara=['?','?','?','?','?','?','?','?','?','?','?','?','?','?','?']
        if self.piso == 3:
            self.pool=['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'F', 'F', 'F', 'F', 'F']
            random.shuffle(self.pool)
            while self.i<18:
                self.cuartos.append(self.pool[self.i])
                self.i=self.i+1
            self.cuartos.append('A')
            self.cuartos.append('B')
            random.shuffle(self.cuartos)
            random.shuffle(self.cuartos)
            self.mascara=['?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?']


def menu():
    print("~~~~~~~~~~~~~~Bienvenido a \x1b[1;31;45mDEMENTIA\x1b[m~~~~~~~~~~~~~~\n")
    print("1] Nuevo Juego\n2] Cargar Juego\n3] Tutorial\n4] Salir")
    opc=input("\nTeclea el numero de opción que desees, y pulsa Enter: ")
    if opc == "1":
         return nuevo()
    elif opc == "2":
        return "load"
    elif opc == "3":
        tutorial()

def nuevo():
    os.system("clear")
    print("1]Bárbaro:")
    print("Fuerza bruta, entre más lastimado esté, más daño hace.")
    print("Habilidades: Hemorragia, Berserker")
    print("Inicia con 3 Pociones")
    print("\n\x1b[1mAtributos:\x1b[m\n\x1b[1;31mFuerza: 3\n\x1b[mAgilidad: 1\nSabiduria: 2")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("2]Arquera:")
    print("Agilidad cegadora, probabilidad de hacer daño crítico.")
    print("Habilidades: Flecha Helada, Apuntar y Disparar")
    print("Inicia con 2 Pociones")
    print("\n\x1b[1mAtributos:\x1b[m\nFuerza: 2\n\x1b[1;32mAgilidad: 3\n\x1b[mSabiduria: 1")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("3]Brujo:")
    print("Sabiduría oscura, cada ataque absorbe HP enemiga, puede sobrepasar por 5pts su HP máxima.")
    print("Habilidades: Ritual de Sangre, Traspasar Alma")
    print("Inicia con 1 Pocion")
    print("\n\x1b[1mAtributos:\x1b[m\nFuerza: 1\nAgilidad: 2\n\x1b[1;34mSabiduria: 3\x1b[m")
    opc = input("\nTeclea el número de opción que desees, y pulsa Enter: ")
    if opc == "1":
        return "barb"
    elif opc == "2":
        return "arqu"
    elif opc == "3":
        return "bruj"


def loadPlayer():
    f2 = open ('archivo1.dem', 'rb')
    player = pickle.load(f2)
    f2.close()
    return player
def loadMap(opc):
    if opc == 1:
        f3 = open ('archivo2.dem', 'rb')
        map = pickle.load(f3)
        f3.close()
    elif opc == 2:
        f3 = open ('archivo3.dem', 'rb')
        map = pickle.load(f3)
        f3.close()
    elif opc == 3:
        f3 = open ('archivo4.dem', 'rb')
        map = pickle.load(f3)
        f3.close()
    return map


def tutorial():
    os.system("clear")
    print("DEMENTIA es un juego tipo roguelike, lo tienes que pasar sin morir, y cada nivel es generado aleatoriamente.\n")
    print("El juego se guarda automáticamente cada que entras a un cuarto, por lo que no debes preocuparte por cerrar el juego.")
    print("La muerte aquí es \x1b[1;31;45mPERMANENTE\x1b[m, por lo que tu juego guardado se borrará al morir.")
    print("Todos tienen tres atributos; Fuerza, Agilidad y Sabiduría. Y cada héroe/enemigo tiene un atributo principal, que es con lo que atacará normalmente.\n")
    print("Fuerza; Aumenta la cantidad de HP máxima que puedes tener. (5HP/pt)")
    print("Agilidad; Aumenta la probabilidad de esquivar los ataques enemigos. (5%/pt)")
    print("Sabiduría; Aumenta la probabilidad de resistir un golpe fatal. (8%/pt)")
    print("También existe la \x1b[1;31;45mDEMENTIA\x1b[m, que aumentará poco a poco mientras avanzas por los cuartos. Mientras más suba, más probabilidades tienes de fallar")
    print("un ataque, pero también aumentará tu daño al atacar. El problema es que al llegar a 100, perderás completamente la cordura y el juego terminará")

def save(player, nivel1, nivel2, nivel3):
    #datos = [player.fuerza, player.agilidad, player.sabiduria, player.clase]
    f = open('archivo1.dem', 'wb')
    archivo1= pickle.dump(player, f)
    f.close()
    f = open('archivo2.dem', 'wb')
    archivo2= pickle.dump(nivel1, f)
    f.close()
    f = open('archivo3.dem', 'wb')
    archivo3= pickle.dump(nivel2, f)
    f.close()
    f = open('archivo4.dem', 'wb')
    archivo4= pickle.dump(nivel3, f)
    f.close()

def showMap(player, nivelActual, nivel1, nivel2, nivel3):
    player.dementia+=nivelActual.piso
    if player.dementia>=100:
        muerte(player)
    os.system("clear")
    save(player, nivel1, nivel2, nivel3)
    nivelActual.mascara[player.cuarto]=nivelActual.cuartos[player.cuarto]
    print(nivelActual.mascara)
    print("\nTe encuentras en el CUARTO "+str(player.cuarto+1)+" del PISO "+str(player.piso)+", el cual es un: "+str(nivelActual.cuartos[player.cuarto]))
    print("\nEres un "+player.nombre+", nivel "+str(player.nivel)+"\nExp: "+str(player.exp)+"/"+str(player.nextLevel))
    print("\x1b[1;32mHP Propia: "+str(player.vida)+"/"+str(player.vidaMax))
    print("\n\x1b[1;31;47mFuerza:"+str(player.fuerza)+" ("+str(player.vidaMax)+"HP Máxima)")
    print("\x1b[1;32;47mAgilidad:"+str(player.agilidad)+" ("+str(player.esquiva)+"% Esquivar Ataque)")
    print("\x1b[1;34;47mSabiduría:"+str(player.sabiduria)+" ("+str(player.revivir)+"% Sobrevivir Golpe Fatal)\x1b[m")
    esquivaDementia=int(player.dementia/10)*5
    dmgDementia=int(player.dementia/10)
    print("\x1b[1;31;45mDementia: "+str(player.dementia)+"/100 (+"+str(dmgDementia)+"pts daño extra/+"+str(esquivaDementia)+"% fallar ataque.)\x1b[m")
    print("\nLeyenda:\nA: Escalera Hacia Arriba\nB: Escalera Hacia Abajo\nM: Probabilidad de Monstruo\nT: Tesoros\nF: Fogatas de Recuperación\nX: Fogatas Apagadas/Tesoros Saqueados\nV: Cuarto Vacío")
    opc=input("Hacia qué lado quieres moverte? [A]Izquierda o [D]Derecha: ")
    if opc=="A" or opc=="a":
        if player.cuarto==0:
            showMap(player, nivelActual, nivel1, nivel2, nivel3)
        else:
            player.cuarto=player.cuarto-1
    elif opc=="D" or opc=="d":
        if (nivelActual.piso==1 and player.cuarto!=9) or (nivelActual.piso==2 and player.cuarto!=14) or (nivelActual.piso==3 and player.cuarto!=19):
            player.cuarto=player.cuarto+1
        else:
            showMap(player, nivelActual, nivel1, nivel2, nivel3)
    if nivelActual.cuartos[player.cuarto]=="M":
        nivelActual.cuartos[player.cuarto]="V"
        enemy=getEnemigo(nivelActual)
        print(enemy.nombre)
        combate(player, enemy, nivelActual, nivel1, nivel2, nivel3)
    elif nivelActual.cuartos[player.cuarto]=="T":
        print("Estás frente a un Tesoro")
    elif nivelActual.cuartos[player.cuarto]=="F":
        print("Estás frente a una Fogata")
        descansar=input("Deseas recuperar tus fuerzas (HP: Al máximo, Hechizo 1: +2 cargas, Pociones: +1 y Dementia: -30)? Esto repoblará los cuartos de enemigos y dejará inútil esta fogata, [S]í/[N]o: ")
        if descansar=="S" or descansar=="s":
            player.recuperar()
            i=0
            while i < len(nivelActual.cuartos):
                if nivelActual.cuartos[i]=="V":
                    nivelActual.cuartos[i]="M"
                    nivelActual.mascara[i]=nivelActual.cuartos[i]
                i+=1
            nivelActual.cuartos[player.cuarto] = "X"
            print(nivelActual.cuartos)
            input("Esperando...")
    elif nivelActual.cuartos[player.cuarto]=="A":
        print("Estás frente a unas Escaleras Hacia Arriba")
        escalera=input("Deseas subir un piso? [S]í/[N]o: ")
        if escalera=="s" or escalera=="S":
            if player.piso==1:
                print("La salida está bloqueada...")
            elif player.piso==2:
                player.piso=1
                player.cuarto=nivel1.cuartos.index('B')
                showMap(player, nivel2, nivel1, nivel2, nivel3)
            elif player.piso==3:
                player.piso=2
                player.cuarto=nivel2.cuartos.index('B')
                showMap(player, nivel3, nivel1, nivel2, nivel3)
    elif nivelActual.cuartos[player.cuarto]=="B":
        print("Estás frente a unas Escaleras Hacia Abajo")
        escalera=input("Deseas bajar un piso? [S]í/[N]o: ")
        if escalera=="s" or escalera=="S":
            if player.piso==1:
                player.piso=2
                player.cuarto=nivel2.cuartos.index('A')
                showMap(player, nivel2, nivel1, nivel2, nivel3)
            elif player.piso==2:
                player.piso=3
                player.cuarto=nivel3.cuartos.index('A')
                showMap(player, nivel3, nivel1, nivel2, nivel3)
    elif nivelActual.cuartos[player.cuarto]=="X":
        print("Aquí solía haber una Fogata de Recuperación...")

    else:
        print("Te encuentras en un cuarto vacío... por ahora.")
    showMap(player, nivelActual, nivel1, nivel2, nivel3)

def getEnemigo(nivel):
    i=0
    if nivel.piso == 1:
        enemyTable=[35,35,20,10]
        choice=random.randint(0,100)
        print(choice)
        while choice>enemyTable[i]:
            choice=choice-enemyTable[i]
            i=i+1
        if i==0:
            enemy=monster.Ratman()
        elif i==1:
            enemy=monster.Skeleton()
        elif i==2:
            enemy=monster.Golem()
        elif i==3:
            enemy=monster.Necrorat()
    elif nivel.piso == 2:
        enemyTable=[40,30,20,10]
        choice=random.randint(0,100)
        print(choice)
        while choice>enemyTable[i]:
            choice=choice-enemyTable[i]
            i=i+1
        if i==0:
            enemy=monster.Skeleton()
        elif i==1:
            enemy=monster.Explosive()
        elif i==2:
            enemy=monster.Sombra()
        elif i==3:
            enemy=monster.Acolyte()
    return enemy

def combate(player, enemy, nivel, nivel1, nivel2, nivel3):
    os.system("clear")
    if player.vida<=0:
        muerte(player)
    if player.dementia>=100:
        muerte(player)
    print("\nCombate contra: "+enemy.nombre+"!!!")
    print("\x1b[1;31;47mHP Enemiga: "+str(enemy.vida)+"/"+str(enemy.vidaMax))
    print("\x1b[1;32;47mHP Propia: "+str(player.vida)+"/"+str(player.vidaMax))
    print("\n\x1b[m\x1b[1;31mFuerza:"+str(player.fuerza)+" ("+str(player.vidaMax)+"HP Máxima)")
    print("\x1b[1;32mAgilidad:"+str(player.agilidad)+" ("+str(player.esquiva)+"% Esquivar Ataque)")
    print("\x1b[1;34mSabiduría:"+str(player.sabiduria)+" ("+str(player.revivir)+"% Sobrevivir Golpe Fatal)")
    esquivaDementia=int(player.dementia/10)*5
    dmgDementia=int(player.dementia/10)
    print("\x1b[1;31;45mDementia: "+str(player.dementia)+"/100 (+"+str(dmgDementia)+"pts daño extra/+"+str(esquivaDementia)+"% fallar ataque.)\x1b[m")
    print("\n\x1b[mLista de comandos:")
    if player.nombre=="Barbaro":
        print("[1] Atacar: usa tu FUERZA para atacar al enemigo. Pasivo: +1daño por cada 3pts HP faltante")
        print("[2] Hemorragia (2pt daño al principio del turno enemigo, durante 4 turnos) CARGAS: "+str(player.carga1))##TRES CARGAS
        print("[3] Berserker (Sacrifica 50% HP actual, inflinge 60% de daño de la HPmax enemiga) CARGAS: "+str(player.carga2))##UNA CARGA
    elif player.nombre=="Arquera":
        print("[1] Atacar: usa tu AGILIDAD para atacar al enemigo. Pasivo: 25% de hacer x1.5 daño (Redon. hacia abajo)")
        print("[2] Flecha de Hielo (El enemigo pierde tres turnos) CARGAS: "+str(player.carga1))##DOS CARGAS
        print("[3] Apuntar y Disparar (En el siguiente turno inflinges CUADRUPLE daño) CARGAS: "+str(player.carga2))##UNA CARGA
    elif player.nombre=="Brujo":
        print("[1] Atacar: usa tu SABIDURIA para atacar al enemigo. Pasivo: el daño regresa como HP, puedes sobrepasar tu HP Máxima por 5 pts")
        print("[2] Ritual de Sangre (5pt daño, pero sacrificas 2pt HP) CARGAS: "+str(player.carga1))##CINCO CARGAS
        print("[3] Traspasar Alma (En dos turnos absorbes TODA la vida del enemigo, matándolo inmediatamente) CARGAS: "+str(player.carga2))##UNA CARGA
    elif player.nombre=="Paladin":
        print("[1] Atacar: usa tu FUERZA para atacar al enemigo. Pasivo: Cada turno quemas al enemigo con tu Aura Sagrada por "+str(player.auraSagrada)+" de daño.")
        print("[2] Rezo Sacro (Pierdes el turno en aumentar tu Aura Sagrada en +2) CARGAS: "+str(player.carga1))##CINCO CARGAS
        print("[3] Castigo Divino (Ataque normal + x2 Aura Sagrada. Regresa tu Aura Sagrada a 1.) CARGAS: "+str(player.carga2))##UNA CARGA
    elif player.nombre=="Asesina":
        print("[1] Atacar: usa tu AGILIDAD para atacar al enemigo. Pasivo: ???")
    elif player.nombre=="Bardo":
        print("[1] Atacar: usa tu SABIDURIA para atacar al enemigo. Pasivo: ???")
    print("[4] Poción: usar una poción para recuperar 2/3 de tu HP Máxima y reducir tu Dementia en -10. Pociones: "+str(player.pociones)+"\n")
    if player.estado=="preparando" or player.estado=="preparando2":
        player.hechizo2(enemy)
    else:
        acc=input("¿Qué deseas hacer?: ")
        if acc=="1":
            player.atacar(enemy)
        elif acc=="2":
            player.hechizo1(enemy)
        elif acc=="3":
            player.hechizo2(enemy)
        elif acc=="4":
            player.pocion()
        else:
            combate(player, enemy, nivel, nivel1, nivel2, nivel3)
    time.sleep(1)
    enemy.pensar(player)
    time.sleep(2)
    if enemy.vida>0:
        combate(player, enemy, nivel, nivel1, nivel2, nivel3)
    else:
        player.exp+=enemy.exp
        player.levelUp()
        showMap(player, nivel, nivel1, nivel2, nivel3)

def muerte(player):
    if player.vida<=0:
        print("\x1b[1;;45mTu HP ha llegado a 0! Has muerto! Se borrarán tus guardados...\x1b[m")
    elif player.dementia>=100:
        print("\x1b[1;;45mTu Dementia ha llegado a 100! Has muerto! Se borrarán tus guardados...\x1b[m")
    os.remove("archivo1.dem")
    os.remove("archivo2.dem")
    exit()

os.system("clear")
inicio=menu()
if inicio=="barb":
    player=heroes.Barbaro()
    nivel1 = Nivel(1)
    nivel2 = Nivel(2)
    nivel3 = Nivel(3)
    player.cuarto=nivel1.cuartos.index('A')
    showMap(player, nivel1, nivel1, nivel2, nivel3)
elif inicio=="arqu":
    player=heroes.Arquera()
    nivel1 = Nivel(1)
    nivel2 = Nivel(2)
    nivel3 = Nivel(3)
    player.cuarto=nivel1.cuartos.index('A')
    showMap(player, nivel1, nivel1, nivel2, nivel3)
elif inicio=="bruj":
    player=heroes.Brujo()
    nivel1 = Nivel(1)
    nivel2 = Nivel(2)
    nivel3 = Nivel(3)
    player.cuarto=nivel1.cuartos.index('A')
    showMap(player, nivel1, nivel1, nivel2, nivel3)
elif inicio=="load":
    player=loadPlayer()
    nivel1=loadMap(1)
    nivel2=loadMap(2)
    nivel3=loadMap(3)
    if player.piso == 1:
        showMap(player, nivel1, nivel1, nivel2, nivel3)
    elif player.piso == 2:
        showMap(player, nivel2, nivel1, nivel2, nivel3)
    elif player.piso == 3:
        showMap(player, nivel3, nivel1, nivel2, nivel3)
