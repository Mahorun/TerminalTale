class Froggit: #Unhealable
    human = False
    name = "Froggit"
    health = 20
    damage = [2 ,3]
    alive = True
    name = "Froggit" 

class Frisk: #Healable
    human = True
    color = "red"
    name = ""
    health = 20
    maxhp = 20
    damage = [4 ,5]
    healAmount = [2, 3, 4, 5] 
    tp = 0
    alive = True
    defense = 0
    shines = False

class Clover: #Healable
    human = True
    color = "yellow"
    health = 20
    alive = True
    name = ""
    maxhp = 20
    healAmount = [4, 4]
    tp = 0
    alive = True
    defense = 5
    normalShotDamage = 5
    BIGshotDamage = 16