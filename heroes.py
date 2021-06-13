import random
class Barbaro():
    def __init__(self):
        self.fuerza=3
        self.agilidad=1
        self.sabiduria=2
        self.dementia=0
        self.clase=1
        self.piso=1
        self.cuarto=0
        self.carga1=3
        self.carga2=1
        self.pociones=3
        self.exp=0
        self.nextLevel=100
        self.nivel=1
        self.nombre="Barbaro"
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self, enemy):
        rand=random.randint(1,100)
        esquivaDementia=int(self.dementia/10)*5
        dmgDementia=int(self.dementia/10)
        if rand>enemy.esquiva+esquivaDementia:
            damage=int(self.fuerza+((self.vidaMax-self.vida)/3))
            enemy.vida-=(damage+dmgDementia)
            print("\n\x1b[4;;42mHas hecho "+str(damage)+" + \x1b[1;31;45m"+str(dmgDementia)+"\x1b[4;;42m de daño!\x1b[m")
        else:
            print("\n\x1b[4;;41m"+enemy.nombre+" ha esquivado tu ataque!\x1b[m")
    def hechizo1(self, enemy):
        if self.carga1>0:
            enemy.estado="hemorragia"
            enemy.i=4
            self.carga1-=1
            print("\n\x1b[4;;42mHeriste profundamente a tu enemigo! Ha comenzado a sangrar!\x1b[m")
        else:
            print("Ya no tienes carga de esa habilidad!")
    def hechizo2(self, enemy):
        if self.carga2>0:
            enemy.vida=round(enemy.vida-(enemy.fuerza*3))
            self.vida=int(self.vida/2)
            print("\n\x1b[4;;42mHas sacrificado tu vida para dañar severamente al enemigo!\x1b[m")
            self.carga2-=1
        else:
            print("Ya no tienes carga de esa habilidad!")
    def pocion(self):
        if self.pociones>0:
            self.vida+=round(self.fuerza*3.33333)
            self.dementia-=10
            if self.dementia<0:
                self.dementia=0
            if self.vida>self.vidaMax:
                self.vida=self.vidaMax
            self.pociones=self.pociones-1
            print("\n\x1b[4;30;47mTe has curado "+str(round(self.fuerza*3.33333))+" pts de HP y reducido tu Dementia por 10pts!\x1b[m")
        else:
            print("\n\x1b[4;;41mPierdes el turno buscando una Poción que no tienes!!!\x1b[m")
    def levelUp(self):
        if self.exp>=self.nextLevel:
            atributo=input("Elige qué atributo subir en 1 punto; [F]uerza, [A]gilidad o [S]abiduría: ")
            if atributo=="f" or atributo=="F":
                self.fuerza+=1
            elif atributo=="a" or atributo=="A":
                self.agilidad+=1
            elif atributo=="s" or atributo=="S":
                self.sabiduria+=1
            else:
                self.levelUp()
            self.setLife(self.fuerza)
            self.setDodge(self.agilidad)
            self.setRevive(self.sabiduria)
            self.carga1=3
            self.carga2=1
            self.nivel+=1
            self.nextLevel=self.nextLevel*2
    def recuperar(self):
        self.vida=self.vidaMax
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0

class Arquera():
    def __init__(self):
        self.fuerza=2
        self.agilidad=3
        self.sabiduria=1
        self.dementia=0
        self.clase=2
        self.piso=1
        self.cuarto=0
        self.carga1=2
        self.carga2=1
        self.pociones=2
        self.exp=0
        self.nextLevel=100
        self.nivel=1
        self.nombre="Arquera"
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self, enemy):
        rand=random.randint(1,100)
        esquivaDementia=int(self.dementia/10)*5
        dmgDementia=int(self.dementia/10)
        if rand>enemy.esquiva+esquivaDementia:
            rand=random.randint(1,4)
            if rand == 1:
                enemy.vida-=(int(self.agilidad*1.5)+dmgDementia)
                print("\n\x1b[4;;42mGolpe Crítico!!! Has hecho "+str(int(self.agilidad*1.5))+" + \x1b[1;31;45m"+str(dmgDementia)+"\x1b[4;;42m de daño!\x1b[m")
            else:
                enemy.vida-=(self.agilidad+dmgDementia)
                print("\n\x1b[4;;42mHas hecho "+str(self.agilidad)+" + \x1b[1;31;45m"+str(dmgDementia)+"\x1b[4;;42m de daño!\x1b[m")
        else:
            print("\n\x1b[4;;41m"+enemy.nombre+" ha esquivado tu ataque!\x1b[m")
    def hechizo1(self, enemy):
        if self.carga1>0:
            enemy.estado="congelado"
            enemy.i=3
            self.carga1-=1
            print("\n\x1b[4;;42mHas tirado una flecha helada! El enemigo pierde tres turnos!\x1b[m")
        else:
            print("Ya no tienes carga de esa habilidad!")
    def hechizo2(self, enemy):
        if self.estado=="":
            if self.carga2>0:
                print("\n\x1b[4;;42mEmpiezas a apuntar al punto crítico del enemigo...!\x1b[m")
                self.estado="preparando"
                self.carga2-=1
            else:
                print("Ya no tienes carga de esa habilidad!")
        elif self.estado=="preparando":
                print("\n\x1b[4;;42mHas dado directo en la yugular!!! Causando "+str(self.agilidad*4)+" de daño!!!\x1b[m")
                enemy.vida-=self.agilidad*4
                self.estado=""
    def pocion(self):
        if self.pociones>0:
            self.vida+=round(self.fuerza*3.33333)
            self.dementia-=10
            if self.dementia<0:
                self.dementia=0
            if self.vida>self.vidaMax:
                self.vida=self.vidaMax
            self.pociones=self.pociones-1
            print("\n\x1b[4;30;47mTe has curado "+str(round(self.fuerza*3.33333))+" pts de HP y reducido tu Dementia por 10pts!\x1b[m")
        else:
            print("\n\x1b[4;;41mPierdes el turno buscando una Poción que no tienes!!!\x1b[m")
    def levelUp(self):
        if self.exp>=self.nextLevel:
            atributo=input("Elige qué atributo subir en 1 punto; [F]uerza, [A]gilidad o [S]abiduría: ")
            if atributo=="f" or atributo=="F":
                self.fuerza+=1
            elif atributo=="a" or atributo=="A":
                self.agilidad+=1
            elif atributo=="s" or atributo=="S":
                self.sabiduria+=1
            else:
                self.levelUp()
            self.setLife(self.fuerza)
            self.setDodge(self.agilidad)
            self.setRevive(self.sabiduria)
            self.carga1=3
            self.carga2=1
            self.nivel+=1
            self.nextLevel=self.nextLevel*2
    def recuperar(self):
        self.vida=self.vidaMax
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0

class Brujo():
    def __init__(self):
        self.fuerza=1
        self.agilidad=2
        self.sabiduria=3
        self.dementia=0
        self.clase=3
        self.piso=1
        self.cuarto=0
        self.carga1=5
        self.carga2=1
        self.pociones=1
        self.exp=0
        self.nextLevel=100
        self.nivel=1
        self.nombre="Brujo"
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self, enemy):
        rand=random.randint(1,100)
        esquivaDementia=int(self.dementia/10)*5
        dmgDementia=int(self.dementia/10)
        if rand>enemy.esquiva+esquivaDementia:
            enemy.vida-=(self.sabiduria+dmgDementia)
            self.vida+=self.sabiduria
            if self.vida>self.vidaMax+5:
                self.vida=self.vidaMax+5
            print("\n\x1b[4;;42mLe has robado al enemigo "+str(self.sabiduria)+"pts de vida!!  + \x1b[1;31;45m"+str(dmgDementia)+"\x1b[4;;42m de daño!!\x1b[m")
        else:
            print("\n\x1b[4;;41m"+enemy.nombre+" ha esquivado tu ataque!\x1b[m")
    def hechizo1(self, enemy):
        if self.carga1>0:
            self.vida-=2
            enemy.vida-=5
            self.carga1-=1
            print("\n\x1b[4;;42mSacrificas 2pts de HP para completar el ritual y hacer 5pts de daño al enemigo!\x1b[m")
        else:
            print("Ya no tienes carga de esa habilidad!")
    def hechizo2(self, enemy):
        if self.estado=="":
            if self.carga2>0:
                print("\n\x1b[4;;42mEmpiezas a concentrar tu poder en transferirte el alma enemiga...!\x1b[m")
                self.estado="preparando"
                self.carga2-=1
            else:
                print("Ya no tienes carga de esa habilidad!")
        elif self.estado=="preparando":
            print("\n\x1b[4;;42mSigues concentrando tu poder en transferirte el alma enemiga...!\x1b[m")
            self.estado="preparando2"
        elif self.estado=="preparando2":
                print("\n\x1b[4;;42mHas traspasado el alma del enemigo a la tuya!!! Recuperas "+str(enemy.vida)+"pts de HP!!!\x1b[m")
                self.vida+=enemy.vida
                enemy.vida=0
                if self.vida>self.vidaMax:
                    self.vida=self.vidaMax
                self.estado=""
    def pocion(self):
        if self.pociones>0:
            self.vida+=round(self.fuerza*3.33333)
            self.dementia-=10
            if self.dementia<0:
                self.dementia=0
            if self.vida>self.vidaMax+5:
                self.vida=self.vidaMax+5
            self.pociones=self.pociones-1
            print("\n\x1b[4;30;47mTe has curado "+str(round(self.fuerza*3.33333))+" pts de HP y reducido tu Dementia por 10pts!\x1b[m")
        else:
            print("\n\x1b[4;;41mPierdes el turno buscando una Poción que no tienes!!!\x1b[m")
    def levelUp(self):
        if self.exp>=self.nextLevel:
            atributo=input("Elige qué atributo subir en 1 punto; [F]uerza, [A]gilidad o [S]abiduría: ")
            if atributo=="f" or atributo=="F":
                self.fuerza+=1
            elif atributo=="a" or atributo=="A":
                self.agilidad+=1
            elif atributo=="s" or atributo=="S":
                self.sabiduria+=1
            else:
                self.levelUp()
            self.setLife(self.fuerza)
            self.setDodge(self.agilidad)
            self.setRevive(self.sabiduria)
            self.carga1=3
            self.carga2=1
            self.nivel+=1
            self.nextLevel=self.nextLevel*2
    def recuperar(self):
        self.vida+=self.vidaMax
        if self.vida>self.vidaMax+5:
            self.vida=self.vidaMax+5
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0

class Paladin():
    def __init__(self):
        self.fuerza=3
        self.agilidad=1
        self.sabiduria=2
        self.dementia=0
        self.clase=1
        self.piso=1
        self.cuarto=0
        self.nombre="Paladin"
        self.exp=0
        self.nextLevel=100
        self.nivel=1
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self,sabiduria):
        return sabiduria
    def recuperar(self):
        self.vida=self.vidaMax
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0
class Asesina():
    def __init__(self):
        self.fuerza=2
        self.agilidad=3
        self.sabiduria=1
        self.dementia=0
        self.clase=2
        self.piso=1
        self.cuarto=0
        self.exp=0
        self.nextLevel=100
        self.nivel=1
        self.nombre="Asesina"
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self,sabiduria):
        return sabiduria
    def recuperar(self):
        self.vida=self.vidaMax
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0

class Bardo():
    def __init__(self):
        self.fuerza=1
        self.agilidad=2
        self.sabiduria=3
        self.dementia=0
        self.clase=3
        self.piso=1
        self.cuarto=0
        self.exp=0
        self.nextLevel=100
        self.nombre="Bardo"
        self.nivel=1
        self.estado=""
        self.setLife(self.fuerza)
        self.setDodge(self.agilidad)
        self.setRevive(self.sabiduria)
    def setLife(self, fuerza):
        self.vida=fuerza*5
        self.vidaMax=fuerza*5
    def setDodge(self, agilidad):
        self.esquiva=agilidad*5
    def setRevive(self, sabiduria):
        self.revivir=sabiduria*8
    def atacar(self,sabiduria):
        return sabiduria
    def recuperar(self):
        self.vida=self.vidaMax
        self.carga1+=2
        self.pociones+=1
        self.dementia-=30
        if self.dementia<0:
            self.dementia=0
