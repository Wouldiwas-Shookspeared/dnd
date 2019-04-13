from random import randint
from tkinter import *

def AC_change(event):
    i = randint(1, 20)
    i += 10
    AC_novi.set(str(i))

def condition_change(event):
    i = randint(0, 11)
    kondicije = ["blinded", "charmed", "deafened", "frightened", "grappled", "incapacitated", "paralysed", "petrified", "poisoned", "prone", "restraiend", "stunned"]
    condition_novi.set(kondicije[i])

def damage_change(event):
    i = randint(0, 11)
    damagi = ["acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic", "piercing", "poison", "psychic", "slashing", "thunder"]
    damage_novi.set(damagi[i])

def save_change(event):
    i = randint(1, 10) + randint(1, 20)
    save_novi.set(str(i))

def ability_change(event):
    i = randint(1, 10) + randint(1, 4) + randint(1, 20)
    ability_novi.set(str(i))

def claw_change(event):
    i = randint(1, 20) + randint(1, 10)
    claw_novi.set(str(i))
    Damage()

def spines_change(event):
    i = randint(1, 20) + randint(1, 10)
    spines_novi.set(str(i))
    Damage()

def new_round(event):
    AC_change(event)
    condition_change(event)
    damage_change(event)
    save_change(event)
    ability_change(event)
    claw_change(event)
    spines_change(event)

def Damage():
    i, j = 0, randint(1, 4)
    suma = 0
    while i < j:
        suma += randint(1, 6)
        i += 1
        
    Damage_novi.set(str(suma))
    
    
root = Tk()

AC_novi = StringVar()
AC_novi.set('10')
condition_novi = StringVar()
condition_novi.set('blinded')
damage_novi = StringVar()
damage_novi.set("acid")
save_novi = StringVar()
save_novi.set("10")
ability_novi = StringVar()
ability_novi.set("0")
claw_novi = StringVar()
claw_novi.set("0")
spines_novi = StringVar()
spines_novi.set("0")
Damage_novi = StringVar()
Damage_novi.set("0")

ime = Label(root, font = ('arial', 20, 'bold'), text = "Randemon", bg = "red", width = 50, fg = "black").grid(row=0, columnspan = 4, sticky = W)
monster_type_alignment = Label(root, font = ('arial', 8, 'italic'), text = "medium fiend, annoying evil", width = 140).grid(row = 1, columnspan = 4, sticky = W)

#armor

armor = Label(root, font = ('arial', 12), text = "Armor class:")
AC = Label(root, font = ('arial', 12, 'bold'), textvariable = AC_novi, bg = "#eee", bd = 0, justify = RIGHT)
AC_novi_napad = Button(root, text = "New attack")
AC_novi_napad.bind("<Button-1>", AC_change)

armor.grid(row = 2, sticky = E)
AC.grid(row = 2, column = 1)
AC_novi_napad.grid(row = 2, column = 2)

#HP

health = Label(root, font = ('arial', 12), text = "HP:")
HP = Label(root, font = ('arial', 12, 'bold'), text = "50", width = 0, bg = "#eee", bd = 0, justify = RIGHT)
health.grid(row = 3, sticky = E)
HP.grid(row = 3, column = 1)

#Condition

condition = Label(root, font = ('arial', 12), text = "Condition immunity: ")
Condition = Label(root, font = ('arial', 12, 'bold'), textvariable = condition_novi, bg = "#eee", bd = 0, justify = RIGHT)
condition.grid(row = 4, sticky = E)
Condition.grid(row = 4, column = 1)

#Damage

damage = Label(root, font = ('arial', 12), text = "Damage immunity: ")
Damage_var = Label(root, font = ('arial', 12, 'bold'), textvariable = damage_novi, bg = "#eee", bd = 0, justify = RIGHT)
damage.grid(row = 5, sticky = E)
Damage_var.grid(row = 5, column = 1)

language = Label(root, font = ('arial', 12), text = "Languages:").grid(row=6, sticky = E)
languagi = Label(root, font = ('arial', 12), text = "Abyssal").grid(row=6, column = 1)

#Saving throw

save = Label(root, font = ('arial', 12), text = "Saving throw:")
save_roll = Label(root, font = ('arial', 12, 'bold'), textvariable = save_novi, bg = "#eee", bd = 0, justify = RIGHT)
save_novi_napad = Button(root, text = "New save")
save_novi_napad.bind("<Button-1>", save_change)

save.grid(row = 7, sticky = E)
save_roll.grid(row = 7, column = 1)
save_novi_napad.grid(row = 7, column = 2)

#Ability check modifier

ability = Label(root, font = ('arial', 12), text = "Ability check modifier:")
ability_roll = Label(root, font = ('arial', 12, 'bold'), textvariable = ability_novi, bg = "#eee", bd = 0, justify = RIGHT)
ability_novi_napad = Button(root, text = "New ability check")
ability_novi_napad.bind("<Button-1>", ability_change)

ability.grid(row = 8, sticky = E)
ability_roll.grid(row = 8, column = 1)
ability_novi_napad.grid(row = 8, column = 2)

#Claw

actions = Label(root, font = ('arial', 16), text = "Actions:").grid(row=9, sticky = E)
claw = Label(root, font = ('arial', 12), text = "Claw").grid(row=10, sticky = E)
melee = Label(root, font = ('arial', 12), text = "5 feet").grid(row=10, column = 1)

#Claw hit

claw_hit = Label(root, font = ('arial', 12), text = "Attack roll:")
claw_roll = Label(root, font = ('arial', 12, 'bold'), textvariable = claw_novi, bg = "#eee", bd = 0, justify = RIGHT)
claw_novi_napad = Button(root, text = "New hit")
claw_novi_napad.bind("<Button-1>", claw_change)

claw_hit.grid(row = 11, sticky = E)
claw_roll.grid(row = 11, column = 1)
claw_novi_napad.grid(row = 11, column = 2)

#Spines

spines = Label(root, font = ('arial', 12), text = "Spines").grid(row=12, sticky = E)
range = Label(root, font = ('arial', 12), text = "60 feet").grid(row=12, column = 1)

#Spines hit

spines_hit = Label(root, font = ('arial', 12), text = "Attack roll:")
spines_roll = Label(root, font = ('arial', 12, 'bold'), textvariable = spines_novi, bg = "#eee", bd = 0, justify = RIGHT)
spines_novi_napad = Button(root, text = "New hit")
spines_novi_napad.bind("<Button-1>", spines_change)

spines_hit.grid(row = 13, sticky = E)
spines_roll.grid(row = 13, column = 1)
spines_novi_napad.grid(row = 13, column = 2)

#Damage

Damage_natpis = Label(root, font = ('arial', 12), text = "Damage:")
Damage_roll = Label(root, font = ('arial', 12, 'bold'), textvariable = Damage_novi, bg = "#eee", bd = 0, justify = RIGHT)

Damage_natpis.grid(row = 14, sticky = E)
Damage_roll.grid(row = 14, column = 1)

#Nova runda

nova_runda = Button(root, text = "New round")
nova_runda.bind("<Button-1>", new_round)
nova_runda.grid(row=15)

root.mainloop()
