import random
class Ratman():
    def __init__(self):
        self.fuerza=1
        self.agilidad=1
        self.sabiduria=2
        self.clase=1
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=2
        self.exp=10
        self.nombre="Hombre Rata"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.vida>(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida<(player.vidaMax/2 and self.pociones>0):
                rand=random.randint(1,3)
                if rand>=2:
                    self.pocion()
                else:
                    self.atacar(player)
            elif self.vida>(self.vidaMax/2) and player.vida<(player.vidaMax/2) and self.pociones>0:
                rand=random.randint(1,3)
                if rand>=2:
                    self.atacar(player)
                else:
                    self.pocion()
            else:
                self.atacar(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.fuerza
            print("\x1b[1;;42mTe han atacado por "+str(self.fuerza)+" pts de daño!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
    def pocion(self):
        print("El Enemigo ha utilizado una de sus pociones para curarse 15pts de HP!!")
        self.vida=self.vida+15
        if self.vida>self.vidaMax:
            self.vida=self.vidaMax
        self.pociones=self.pociones-1
class Skeleton():
    def __init__(self):
        self.fuerza=2
        self.agilidad=1
        self.sabiduria=3
        self.clase=2
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=2
        self.exp=20
        self.nombre="Esqueleto Viviente"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.vida>(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida<(player.vidaMax/2 and self.pociones>0):
                rand=random.randint(1,3)
                if rand>=2:
                    self.pocion()
                else:
                    self.atacar(player)
            elif self.vida>(self.vidaMax/2) and player.vida<(player.vidaMax/2) and self.pociones>0:
                rand=random.randint(1,3)
                if rand>=2:
                    self.atacar(player)
                else:
                    self.pocion()
            else:
                self.atacar(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.fuerza
            print("\x1b[1;;42mTe han atacado por "+str(self.fuerza)+" pts de daño!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
    def pocion(self):
        print("El Enemigo ha utilizado una de sus pociones para curarse 15pts de HP!!")
        self.vida=self.vida+15
        if self.vida>self.vidaMax:
            self.vida=self.vidaMax
        self.pociones=self.pociones-1
class Golem():
    def __init__(self):
        self.fuerza=3
        self.agilidad=1
        self.sabiduria=1
        self.clase=1
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=2
        self.exp=30
        self.nombre="Golem de Barro"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.vida>(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida>(player.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2) and player.vida<(player.vidaMax/2 and self.pociones>0):
                rand=random.randint(1,3)
                if rand>=2:
                    self.pocion()
                else:
                    self.atacar(player)
            elif self.vida>(self.vidaMax/2) and player.vida<(player.vidaMax/2) and self.pociones>0:
                rand=random.randint(1,3)
                if rand>=2:
                    self.atacar(player)
                else:
                    self.pocion()
            else:
                self.atacar(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.fuerza
            print("\x1b[1;;42mTe han atacado por "+str(self.fuerza)+" pts de daño!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
    def pocion(self):
        print("El Enemigo ha utilizado una de sus pociones para curarse 15pts de HP!!")
        self.vida=self.vida+15
        if self.vida>self.vidaMax:
            self.vida=self.vidaMax
        self.pociones=self.pociones-1
class Necrorat():
    def __init__(self):
        self.fuerza=3
        self.agilidad=2
        self.sabiduria=4
        self.clase=2
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=3
        self.exp=60
        self.nombre="Necro-Rata"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.vida>((2*self.vidaMax)/3):
                self.ritualSangre(player)
            elif self.vida<((2*self.vidaMax)/3) and self.vida>(self.vidaMax/3):
                self.atacar(player)
            elif self.vida<(self.vidaMax/3) and player.vida<(player.vidaMax/3):
                rand=random.randint(1,3)
                if rand>=2:
                    self.atacar(player)
                else:
                    self.pocion()
            elif self.vida<(self.vidaMax/3) and player.vida>(player.vidaMax/3):
                self.atacar(player)
            else:
                self.ritualSangre(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.agilidad
            self.vida+=2
            print("\x1b[1;;42mTe han atacado por "+str(self.agilidad)+" pts de daño! Y la Necro-Rata absorbe 2pt de HP!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
    def pocion(self):
        print("El Enemigo ha utilizado una de sus pociones para curarse 15pts de HP!!")
        self.vida=self.vida+15
        if self.vida>self.vidaMax:
            self.vida=self.vidaMax
        self.pociones=self.pociones-1
    def ritualSangre(self, player):
        print("La Necro-Rata sacrifica 3pt de HP, para inflingirte 3pt de daño!!!")
        self.vida-=3
        player.vida-=3
class Explosive():
    def __init__(self):
        self.fuerza=3
        self.agilidad=0
        self.sabiduria=1
        self.clase=1
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=0
        self.exp=25
        self.nombre="Bestia Explosiva"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0 and self.estado2!="finish":
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.estado2=="preparo":
                print("El próximo turno, la bestia explotará!!")
                self.estado2="explode"
            elif self.estado2=="explode":
                print("La bestia ha explotado! Un montón de sangre y liquidos viles caen sobre ti!!")
                print("Te daña por 10pts, y genera 15pts de Dementia en ti!!")
                player.vida-=10
                player.dementia+=15
                self.vida=0
                self.estado2="finish"
                self.pensar(player)
            elif self.vida>(self.vidaMax/2):
                self.atacar(player)
            elif self.vida<(self.vidaMax/2):
                self.estado2="preparo"
                print("La Bestia Explosiva comienza a inflarse... parece que se prepara para explotar!!")
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.sabiduria
            print("\x1b[1;;42mLa Bestia Explosiva escupe un ácido que te quema por "+str(self.sabiduria)+" pts de daño!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
class Sombra():
    def __init__(self):
        self.fuerza=1
        self.agilidad=8
        self.sabiduria=2
        self.clase=1
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=0
        self.exp=35
        self.nombre="Sombra"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            else:
                self.atacar(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.fuerza
            print("\x1b[1;;42mTe han atacado por "+str(self.sabiduria)+" pts de daño!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
class Acolyte():
    def __init__(self):
        self.fuerza=4
        self.agilidad=2
        self.sabiduria=5
        self.clase=2
        self.vida=self.fuerza*5
        self.vidaMax=self.fuerza*5
        self.esquiva=self.agilidad*5
        self.revivir=self.sabiduria*8
        self.estado=""
        self.estado2=""
        self.i=0
        self.pociones=3
        self.exp=60
        self.nombre="Acólito Dementia"
    def pensar(self, player):
        if self.estado=="hemorragia" and self.i>0:
            self.vida=self.vida-2
            self.i=self.i-1
            print("El Enemigo sangra por 2pts de daño!")
        if self.vida<=0:
            rand=random.randint(1,100)
            if rand<=self.revivir:
                self.vida=3
                print("\x1b[1;;45mEl enemigo ha aguantado un golpe letal! Recupera 3 pts de HP\x1b[m")
        if self.vida>0:
            if self.estado=="congelado" and self.i>0:
                self.i-=1
                print("El Enemigo se encuentra congelado! Pierde el turno!")
            elif self.vida>(self.vidaMax/3):
                rand=random.randint(1,3)
                if rand>=2:
                    self.flagelacion(player)
                else:
                    self.atacar(player)
            elif self.pociones>0:
                self.pocion()
            else:
                self.flagelacion(player)
        else:
            print("\n\x1b[1;30;43mEl "+self.nombre+" ha sido Derrotado!\x1b[m")
    def atacar(self, player):
        rand=random.randint(1,100)
        if rand>player.esquiva:
            player.vida=player.vida-self.agilidad
            self.vida+=2
            print("\x1b[1;;42mEl Acólito te encaja su Daga Impía por "+str(self.agilidad)+" pts de daño! También aumenta tu Dementia en 2pts!!\x1b[m")
        else:
            print("\x1b[1;30;47mLograste esquivar el ataque de "+self.nombre+"!!\x1b[m")
    def pocion(self):
        print("El Enemigo ha utilizado una de sus pociones para curarse 15pts de HP!!")
        self.vida=self.vida+15
        if self.vida>self.vidaMax:
            self.vida=self.vidaMax
        self.pociones=self.pociones-1
    def flagelacion(self, player):
        print("El Acólito comienza a flagelarse sufriendo 3pt de daño, para aumentar en 5pts tu dementia!!!")
        self.vida-=3
        player.dementia+=5
