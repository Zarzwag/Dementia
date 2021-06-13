import os
from random import randint

########################################FUNCIONES########################################
def Menu():
    continuar=input("Seguro que deseas continuar? S/N\n")
    if continuar == "S" or continuar == "s":
        ##EJECUTAR EL JUEGO (Elegir clase?)
        print("Continuando...")
        return 1
    elif continuar == "N" or continuar == "n":
        ##SALIR DEL JUEGO
        print("Saliendo...")
        exit()
    else:
        print("Elige una opción válida, debilucho")
        os.system("clear")
        return Menu()

def eligeClase():
    ##Barbaro = 1 Pasivo: Cada pt HP que le falte, hace +0.5 de daño
    ##Arquero = 2 Pasivo: Cada ataque tiene 25% probabilidad de hcaer doble daño
    ##Brujo == 3 Pasivo: Recupera la mitad del daño en HP
    os.system("clear")
    print("Cada clase tiene tres atributos; Fuerza, Agilidad y Sabiduría. Y cada clase tiene un atributo principal, que es con lo que hace daño.\n")
    print("Fuerza; Aumenta la cantidad de HP máxima que puedes tener. (5HP/pt)")
    print("Agilidad; Aumenta la probabilidad de esquivar los ataques enemigos. (5%/pt)")
    print("Sabiduría; Aumenta la probabilidad de resistir un golpe fatal. (8%/pt)")
    print("\n1]Bárbaro:")
    print("Fuerza bruta, entre más lastimado esté, más daño hace.")
    print("Habilidades: Hemorragia, Berserker")
    print("Inicia con 3 Pociones")
    print("\n\x1b[1mAtributos:\x1b[m\n\x1b[1;31mFuerza: 3\n\x1b[mAgilidad: 1\nSabiduria: 2")
    print("\n2]Explorador:")
    print("Agilidad cegadora, probabilidad de hacer daño crítico.")
    print("Habilidades: Flecha Helada, Apuntar y Disparar")
    print("Inicia con 2 Pociones")
    print("\n\x1b[1mAtributos:\x1b[m\nFuerza: 2\n\x1b[1;32mAgilidad: 3\n\x1b[mSabiduria: 1")
    print("\n3]Brujo:")
    print("Sabiduría oscura, cada ataque absorbe HP enemiga, puede sobrepasar por 5pts su HP máxima.")
    print("Habilidades: Ritual de Sangre, Traspasar Alma")
    print("Inicia con 1 Pocion")
    print("\n\x1b[1mAtributos:\x1b[m\nFuerza: 1\nAgilidad: 2\n\x1b[1;34mSabiduria: 3\x1b[m")
    clase=input("\nElige tu clase: ")
    if clase == "1":
        os.system("clear")
        print("Has elegido la senda de la Fuerza Bruta...")
        return '1'
    elif clase == "2":
        os.system("clear")
        print("Has elegido la senda de la Agilidad Cegadora...")
        return '2'
    elif clase == "3":
        os.system("clear")
        print("Has elegido la senda de la Sabiduría Oscura...")
        return '3'
    else:
        return eligeClase()
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
def Combate(enemigo,fue,agi,sab,player,atk,enemHp,magic,magic2,timer,timer2,hechizos):
    enemSu=sab*8
    propSu=player[2]*8
    while player[3]>0 and enemHp>0:
        print("\nCombate contra: "+enemigo+"!!!")
        print("\x1b[1;31mHP Enemiga: "+str(enemHp)+"/?")
        print("\x1b[1;32mHP Propia: "+str(player[3])+"/"+str(player[0]*5))
        print("\n\x1b[1;31;47mFuerza:"+str(player[0])+" ("+str(player[0]*5)+"HP Máxima)")
        print("\x1b[1;32;47mAgilidad:"+str(player[1])+" ("+str(player[1]*5)+"% Esquivar Ataque)")
        print("\x1b[1;34;47mSabiduría:"+str(player[2])+" ("+str(player[2]*8)+"% Sobrevivir Golpe Fatal)")
        print("\n\x1b[mLista de comandos:")
        if player[4]==1:
            print("[A]tacar: usa tu FUERZA para atacar al enemigo. Pasivo: +1daño por cada 3pts HP faltante")
        elif player[4]==2:
            print("[A]tacar: usa tu AGILIDAD para atacar al enemigo. Pasivo: 25% de hacer x1.5 daño (Redon. hacia abajo)")
        else:
            print("[A]tacar: usa tu SABIDURIA para atacar al enemigo. Pasivo: 1/2 del daño regresa como HP (Redon. hacia abajo)")
        print("[H]abilidad: despliega la lista de habilidades para usar")
        print("[P]oción: usar una poción para recuperar 2/3 de tu HP Máxima. Pociones: "+str(hechizos[2])+"\n")
        acc=input("Que deseas hacer?: ")
        os.system("clear")
        if magic2==4:
            response="dispara"
            magic2=0
        elif magic2==6:
            if timer2>0:
                response="concentra"
                timer2=timer2-1
            else:
                response="traspasa"
                magic2=0
        else:
            response=Accion(acc,agi,sab,player)
        if response=="hit":
            if player[4]==1:
                damage=int(player[0]+(((player[0]*5)-player[3])/3))
                enemHp=enemHp-damage
                print("\n\x1b[4;;42mHas hecho "+str(damage)+" de daño!\x1b[m")
            elif player[4]==2:
                random=randint(1,4)
                if random == 1:
                    enemHp=enemHp-int((player[1]*1.5))
                    print("\n\x1b[4;;42mGolpe Crítico!!! Has hecho "+str(int(player[1]*1.5))+" de daño!\x1b[m")
                else:
                    enemHp=enemHp-player[1]
                    print("\n\x1b[4;;42mHas hecho "+str(player[1])+" de daño!\x1b[m")
            else:
                enemHp=enemHp-player[2]
                player[3]=int(player[3]+(player[2]/2))
                if player[3]>((player[0]*5)+5):
                    player[3]=((player[0]*5)+5)
                print("\n\x1b[4;;42mHas hecho "+str(player[2])+" de daño y absorbido "+str(int(player[2]/2))+" pts de HP!\x1b[m")
        elif response=="miss":
            print("\n\x1b[4;;41m"+enemigo+" ha esquivado tu ataque!\x1b[m")
        elif response=="cure":
                if hechizos[2]>0:
                    player[3]=round(player[3]+(player[0]*3.33333))
                    if player[4]!=3:
                        if player[3]>(player[0]*5):
                            player[3]=(player[0]*5)
                    else:
                        if player[3]>((player[0]*5)+5):
                            player[3]=((player[0]*5)+5)
                    hechizos[2]=hechizos[2]-1
                    print("\n\x1b[4;30;47mTe has curado "+str(round(player[0]*3.33333))+" pts de HP!\x1b[m")
                else:
                    print("\n\x1b[4;;41mPierdes el turno buscando una Poción que no tienes!!!\x1b[m")

        ###############################HECHIZOS############################
        elif response=="H" or response=="h":
            if player[4]!=1:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[0]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic=1
                timer=4
                hechizos[0]=hechizos[0]-1
                print("\n\x1b[4;;42mHeriste profundamente a tu enemigo! Ha comenzado a sangrar!\x1b[m")
        elif response=="B" or response=="b":
            if player[4]!=1:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[1]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic2=2
                hechizos[1]=hechizos[1]-1
                print("\n\x1b[4;;42mHas sacrificado tu vida para dañar severamente al enemigo!\x1b[m")
        elif response=="F" or response=="f":
            if player[4]!=2:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[0]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic=3
                timer=2
                hechizos[0]=hechizos[0]-1
                print("\n\x1b[4;;42mHas tirado una flecha helada! El enemigo pierde dos turnos!\x1b[m")
        elif response=="A" or response=="a":
            if player[4]!=2:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[1]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic2=4
                hechizos[1]=hechizos[1]-1
                print("\n\x1b[4;;42mEmpiezas a apuntar al punto crítico del enemigo...!\x1b[m")
        elif response=="R" or response=="r":
            if player[4]!=3:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[0]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic=5
                hechizos[0]=hechizos[0]-1
                print("\n\x1b[4;;42mSacrificas 2pts de HP para completar el ritual y hacer 5pts de daño al enemigo!\x1b[m")
        elif response=="T" or response=="t":
            if player[4]!=3:
                print("Parece que no te has concentrado lo suficiente, esa habilidad no existe")
            elif hechizos[1]==0:
                print("Ya no tienes carga de esa habilidad!")
            else:
                magic2=6
                timer2=1
                hechizos[1]=hechizos[1]-1
                print("\n\x1b[4;;42mEmpiezas a concentrar tu poder en transferirte el alma enemiga...!\x1b[m")
        elif response=="dispara":
            enemHp=enemHp-(player[1]*4)
            print("\n\x1b[4;;42mHas dado directo en la yugular!!! Causando "+str(player[1]*4)+" de daño!!!\x1b[m")
        elif response=="concentra":
            print("\n\x1b[4;;42mSigues concentrándote en el alma enemiga...\x1b[m")
        elif response=="traspasa":
            print("\n\x1b[4;;42mHas traspasado el alma del enemigo a la tuya!!! Recuperas "+str(enemHp)+"pts de HP!!!\x1b[m")
            player[3]=player[3]+enemHp
            if player[3]>((player[0]*5)+5):
                player[3]=((player[0]*5)+5)
            enemHp=0
        else:
            print("\n\x1b[4;;41mConcéntrate más! Has elegido una opción que no existe!!! (Pierdes Turno)\x1b[m")
        ##############################HEMORRAGIA, BERSERKER y RITUAL DE SANGRE######################
        if magic==1:
            if timer>0:
                enemHp=enemHp-2
                timer=timer-1
                print("El Enemigo sangra por 2pts de daño!")
            else:
                magic=0
                print("Ha parado el sangrado del enemigo!")
        if magic2==2:
            player[3]=round(player[3]/2)
            enemHp=round(enemHp-(fue*3))
            magic2=0
        if magic==5:
            player[3]=player[3]-2
            enemHp=enemHp-5
            magic=0
        ##############################TURNO ENEMIGO#######################
        if enemHp<=0:
            random=randint(1,100)
            if enemSu>=random:
                enemHp=2
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 2 pts de HP\x1b[m")
                return Combate(enemigo,fue,agi,sab,player,atk,enemHp,magic,magic2,timer,timer2,hechizos)
            else:
                print("\n\x1b[1;30;43mEnemigo Derrotado!\x1b[m")
                break
        else:
            if magic==3:
                if timer>0:
                    responseIA="congelado"
                    timer=timer-1
                else:
                    magic=0
            else:
                responseIA=enemAccion(fue,agi,sab,player,enemHp,player[3])
            if responseIA=="hit":
                if atk==1:
                    player[3]=player[3]-fue
                    print("\x1b[1;;42mTe han atacado por "+str(fue)+" pts de daño!\x1b[m")
                elif atk==2:
                    player[3]=player[3]-agi
                    print("\x1b[1;;42mTe han atacado por "+str(agi)+" pts de daño!\x1b[m")
                else:
                    player[3]=player[3]-sab
                    print("\x1b[1;;42mTe han atacado por "+str(sab)+" pts de daño!\x1b[m")
            elif responseIA=="miss":
                print("\x1b[1;30;47mLograste esquivar su ataque!!\x1b[m")
            elif responseIA=="cure":
                enemHp=round(enemHp+((fue*5)/3))
                if enemHp>=(fue*5):
                    enemHp=fue*5
                print("\x1b[1;;45mEl enemigo se ha curado "+str(fue*2)+" pts de Hp!\x1b[m")
            elif responseIA=="congelado":
                print("\x1b[1;30;47mEl enemigo está congelado!! No puede hacer nada!!\x1b[m")
    if player[3]<=0:
        random=randint(1,100)
        if propSu>=random:
            player[3]=2
            print("\x1b[1;30;47mTu sabiduria te ha ayudado a aguantar un golpe letal! Recuperas 2 pts de HP\x1b[m")
            return Combate(enemigo,fue,agi,sab,player,atk,enemHp,magic,magic2,timer,timer2,hechizos)
        else:
            print("\x1b[1;;45mHas muerto! Game Over\x1b[m")
            exit()
    return player[3]
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
def Accion(acc,agi,sab,player):
    if acc=="atacar" or acc=="Atacar" or acc=="a" or acc=="A":
            enemEv=agi*5
            random=randint(1,100)
            if enemEv<=random:
                return "hit"
            else:
                return "miss"
    elif acc=="pocion" or acc=="Pocion" or acc=="p" or acc=="P":
        return "cure"
    elif acc=="habilidad" or acc=="Habilidad" or acc=="h" or acc=="H":
        if player[4]==1:
            print("Habilidades de Guerrero:\n")
            print("[H]emorragia (2pt daño al principio del turno enemigo, durante 4 turnos) CARGAS: "+str(hechizos[0]))##TRES CARGAS
            print("[B]erserker (Sacrifica 50% HP actual, inflinge 60% de daño de la HPmax enemiga) CARGAS: "+str(hechizos[1]))##UNA CARGA
            skill=input("Elige Habilidad: ")
            os.system("clear")
            return skill
        if player[4]==2:
            print("Habilidades de Explorador:\n")
            print("[F]lecha de Hielo (El enemigo pierde tres turnos) CARGAS: "+str(hechizos[0]))##DOS CARGAS
            print("[A]puntar y Disparar (En el siguiente turno inflinges CUADRUPLE daño) CARGAS: "+str(hechizos[1]))##UNA CARGA
            skill=input("Elige Habilidad: ")
            os.system("clear")
            return skill
        if player[4]==3:
            print("Habilidades de Brujo:\n")
            print("[R]itual de Sangre (5pt daño, pero sacrificas 2pt HP) CARGAS: "+str(hechizos[0]))##CINCO CARGAS
            print("[T]raspasar Alma (En dos turnos absorbes TODA la vida del enemigo, matándolo inmediatamente) CARGAS: "+str(hechizos[1]))##UNA CARGA
            skill=input("Elige Habilidad: ")
            os.system("clear")
            return skill
    else:
        return "what"
#######################################################################################
#######################################################################################
def enemAccion(fue,agi,sab,player,enemHp,propHp):
    mitadHp=round((fue*5)/2)
    mitadPropHp=round(((player[0]*5)/2))
    if enemHp>=mitadHp and propHp>=mitadPropHp:
        propEv=player[1]*5
        random=randint(1,100)
        if propEv<=random:
            return "hit"
        else:
            return "miss"
    if enemHp>=mitadHp and propHp<mitadPropHp:
        propEv=player[1]*5
        random=randint(1,100)
        if propEv<=random:
            return "hit"
        else:
            return "miss"
    if enemHp<mitadHp and propHp<mitadPropHp:
        propEv=player[1]*5
        random=randint(1,100)
        randomAtk=randint(1,3)
        if randomAtk==2 or randomAtk==3:
            if propEv<=random:
                return "hit"
            else:
                return "miss"
        else:
            return "cure"
    if enemHp<mitadHp and propHp>=mitadPropHp:
        randomAtk=randint(1,3)
        if randomAtk==1 or randomAtk==2:
            propEv=player[1]*5
            random=randint(1,100)
            if propEv<=random:
                return "hit"
            else:
                return "miss"
        else:
            return "cure"

def levelUp(player):
    atributo=input("Elige qué atributo subir en 1 punto; [F]uerza, [A]gilidad o [S]abiduría: ")
    if atributo == "F" or atributo=="f":
        player[0]=player[0]+1
        player[3]=player[3]+5
        if player[4]!=3:
            if player[3]>(player[0]*5):
                player[3]=(player[0]*5)
        else:
            if player[3]>((player[0]*5)+5):
                player[3]=((player[0]*5)+5)
    elif atributo == "A" or atributo=="a":
        player[1]=player[1]+1
    elif atributo == "S" or atributo=="s":
        player[2]=player[2]+1
    else:
        os.system("clear")
        print("Elige un Atributo válido")

        levelUp(player)

########################################CODIGO########################################
os.system("clear")
print("~~~~~~~~~~~~~~Bienvenido a DEMENTIA~~~~~~~~~~~~~~\n")
print("DEMENTIA es un juego tipo roguelike, lo tienes que pasar de una vez o atenerte a perder todo tu progreso.\n")
print("La muerte aquí es \x1b[1;31;45m"+"PERMANENTE\n\x1b[m")


#######Definiendo Atributos######
atributos=[]##Fuerza(HPmax=n*5),Agilidad(Evasion= n*5%),Sabiduria(SobrevivirFatal= n*8%),Exp,HPinicial(Fue*5),Clase
hechizos=[]##CargasHechizo1,CargasHechizo2

if Menu() == 1:
    claseJugador=eligeClase()

if claseJugador=="1":
    atributos=[3,1,2,15,1]
    hechizos=[2,1,3]
elif claseJugador=="2":
    atributos=[2,3,1,10,2]
    hechizos=[2,1,2]
    print("")
else:
    atributos=[1,2,3,5,3]
    hechizos=[3,2,1]
#####################################Iniciando la Historia######
##########################################
########################################################
############################################
print("\nEl pueblo de Bourke te ha contratado para investigar varias desapariciones")
print("Todas las pistas te guían al alcantarillado, donde inicia tu aventura...")
print("Despues de investigar un poco, un chillido llama tu atención")
print("Tu mirada alcanza a distinguir una enorme figura humanoide, pero al poner más atención...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Resulta ser un Hombre-Rata!")

atributos[3]=Combate("Hombre-Rata",1,5,0,atributos,1,4,0,0,0,0,hechizos)##Nombre,Fue,Agi,Sab,Player,Atr con el que ataca,hp,hechizo1,hechizo2,timer,timer2,cargas

print("Al final has logrado vencer")
print("Una infestación de Hombres-Rata podría ser lo que ocasiona las desapariciones...")
print("Pero estos no suelen dañar a las personas de la superficie, después de todo, ellas son las que tiran el desperdicio del que suelen alimentarse...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Continuas tu viaje por las alcantarillas, miles de chillidos te rodean y puedes escuchar el movimiento de miles de patas")
print("Pero de repente de entre las sombras, se te abalanza un Hombre-Rata Bárbaro, con una enorme Hacha de Guerra en Mano!!")

atributos[3]=Combate("Bárbaro-Rata",2,1,1,atributos,1,8,0,0,0,0,hechizos)

print("Bárbaros-Rata, los soldados de primera línea de cualquier colonia de Hombres-Rata... pero pareciera que este solo defendía su territorio...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Conforme te vas adentrando a las alcantarillas, cada vez es más claro que las Ratas llevan poco tiempo aquí")
print("Como si estuvieran huyendo de algo mucho más peligroso...")
print("Al seguir explorando, un fétido holor a pobredumbre abruma tus sentidos...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Puedes entonces ver que el origen de dicho olor es una enorme y enferma rata. Una Necro-Rata!!!")

atributos[3]=Combate("Necro-Rata",2,5,3,atributos,3,5,0,0,0,0,hechizos)

print("Al explorar te encuentras con unas extrañas runas en las paredes, se te quedan grabadas en la cabeza y algo en ti ha cambiado")

levelUp(atributos)

continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Al asesinar a esa Necro-Rata, miles y miles de chillidos y pasos empiezan a correr hacia algún punto en específico de la alcantarilla")
print("Pareciera que están huyendo hacia algún lugar donde se sienten seguros...")
print("Al seguir los pasos, llegas a un enorme cuarto, donde montañas de basura y desechos son apilados")
print("Y ahí sobre un gran trono de basura...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Te encuentras cara a cara con el principe rata!")

atributos[3]=Combate("Principe-Rata",3,6,4,atributos,3,12,0,0,0,0,hechizos)

print("Al momento de dar el golpe de gracia al Principe-Rata, miles de chillidos suenan en la infinita oscuridad...")
print("Parece que por el momento, los hombres rata ya no son una molestia. Tomas un descanso corto y recuperas 2 Cargas de Habilidad Básica y 3 pts de vida...")

atributos[3]=atributos[3]+3
hechizos[0]=hechizos[0]+2

continuar=input("Presiona Enter Para Continuar...")
print("Las alcantarillas llegan a lo más profundo del pueblo, hasta llegar a un enorme agujero")
print("Solo puedes percibir el asqueroso olor que emana desde el fondo... Es momento de entrar")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
############################################################################################
########################################DUNGEON#############################################
############################################################################################
print("Llegas a alguna clase de estructura por debajo de las alcantarillas, las paredes no son naturales")
print("Al dar vuelta en una esquina, un sonido extraño intenta escabullirse por tu espalda, volteas y...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Te encuentras frente a frente con un Esqueleto Pícaro!!")

atributos[3]=Combate("Esqueleto Pícaro",3,5,2,atributos,1,11,0,0,0,0,hechizos)

print("La victoria es tuya!")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Qué demonios fue eso? Los muertos no reviven solo porque sí...")
print("Será acaso la obra de algún nigromante?")
print("La única manera de saberlo es seguir explorando...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Al continuar por los pasillos de este oscuro lugar, te empiezas a sentir observado...")
print("Al revisar tu espalda, no ves más que una infinidad de sombras danzantes, creadas por la poca luz que ofrece tu antorcha...")
print("Cada vez te sientes más vigilado, la tensión te enloquece. Hasta que de pronto sientes un helado aliento en la nuca...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Volteas y te encuentras con una Sombra Animada! Extremadamente difíciles de golpear, pero bastante débiles")

atributos[3]=Combate("Sombra Animada",1,14,2,atributos,3,5,0,0,0,0,hechizos)

print("Tus ataques convencionales apenas y podían afectar a la sombra, pero lo lograste...")
print("Pareciera que esta bestia estaba guardando un cofre... veamos que hay dentro...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Oh no! Al abrir el cofre, tu mano queda pegada. Del filo de la apertura salen un monoton de dientes filosos...")
print("Una enorme lengua y un par de brazos intentan atraparte!")
print("De milagro logras zafarte! Pero es momento de enfrentarte a un Mimic!")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")

atributos[3]=Combate("Mimic",3,2,5,atributos,2,11,0,0,0,0,hechizos)

continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Al fin, en el fondo del supuesto cofre, que ahora yace muerto, encuentras...")
print("Parece un libro de conocimiento arcano!")

levelUp(atributos)

print("Con estos nuevos conocimientos, esperas poder hacerle frente a los retos que están por venir...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("También parece un buen lugar para descansar... Recuperas 3pts de HP y 1 carga de Habilidad Superior!")

atributos[3]=atributos[3]+3
hechizos[1]=hechizos[1]+1

continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Este lugar parece bastante antiguo, pero ningun texto habla de su existencia")
print("Sientes que detrás de la siguiente puerta hay alguna presencia maligna, pareciera que está arrastrando algo...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Abres la puerta y es un Esqueleto de Gigante, con un enorme mazo!!")

atributos[3]=Combate("Giga-Esqueleto",4,0,4,atributos,3,18,0,0,0,0,hechizos)

print("Logras destrozar el cráneo de este gigante enemigo!")
print("Por el momento tendrás que dejar este extraño calabozo... Tu atención se centra en la entrada de una enorme cueva...")
print("Pareciera que de aquí emanaba el asqueroso olor de hace un rato...")
print("No queda de otra mas que entrar...")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("Puedes sentir la agobiante humedad conforme vas adentrándote en la cueva... Nada de esto figura en los mapas del pueblo...")
print("A lo lejos se escucha el agua correr... Será el mar? O algún río subterráneo?")
print("Y también... Un... llanto? De una niña? Será acaso que...")
print("De pronto el llanto calla, y eres enfrentado por el espíritu de dicha niña!")
continuar=input("Presiona Enter Para Continuar...")
os.system("clear")
print("'Ho-hola? Vienes a re-rescatarme? Creo que e-estoy muerta... No puedo ir al otro mu-mundo...'")
print("'Solo quiero ven-venganza... contra aquel que to-tomó mi vida... Me ayudarías?'")
print("Es momento de decidir...")
decision=input("[A]yudar al espíritu o [M]andar al otro mundo a esta abominación: ")
while decision!="a" and decision!="A" and decision!="m" and decision!="M":
    decision=input("[A]yudar al espíritu o [M]andar al otro mundo a esta abominación: ")

if decision=="m" or decision=="M":
    print("El espíritu se da cuenta de tus intenciones...")
    print("'TE ARREPENTIRAS DE ESTO!!!'")
    atributos[3]=Combate("Espíritu Infantil",4,10,0,atributos,1,15,0,0,0,0,hechizos)
    print("Al derrotar a la aparición, su esencia se transforma en tres cargas para tu Habilidad Basica")
    hechizos[0]=hechizos[0]+3
    karma=-1
else:
    print("'Fui asesinada por un enorme lobo huargo, te guiaré hasta él...'")
    continuar=input("Presiona Enter Para Continuar...")
    os.system("clear")
    print("Después de un rato de seguir a la niña, llegas a lo que parece un callejón sin salida")
    print("Ahí en el fondo de la cueva, se encuentra un enorme Lobo Huargo")
    print("Sin siquiera hacer un ruido, se da cuenta de tu presencia y está listo para pelear!!")
    atributos[3]=Combate("Lobo Huargo",5,2,5,atributos,2,25,0,0,0,0,hechizos)
    print("Al derrotar a semejante bestia, el espiritu de la niña empieza a desaparecer...")
    print("'Gracias...'")
    print("Al irse, deja atrás 2 pociones!")
    hechizos[2]=hechizos[2]+2
