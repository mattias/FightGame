import random

class Character:
    actions = ['upper', 'middle', 'lower']

    def __init__(self):
        self.name = 'Character'
        self.hp = 100
        self.defense = self.actions[random.randint(0,2)]
        self.attack = self.actions[random.randint(0,2)]

    def action(self, other):
        if self.attack != other.defense:
            attack_power = random.randint(5,10)
            other.hp -= attack_power
            print self.name,'hit',other.name,'for',attack_power,'hp!'
            print self.name,'attacked with',self.attack,'!'
            print other.name,'tried to block with',self.defense,'.'
        else:
            print other.name,'successfully blocked',self.name,'\'s', self.attack,'attack!'

    def askForAction(self, other):
        print '1 -> upper'
        print '2 -> middle'
        print '3 -> lower'

        attack = 0
        while not (attack >= 1 and attack <= 3):
            attack = int(raw_input('How do you want to attack? '))

        self.attack = self.actions[attack-1];

        defend = 0
        while not (defend >= 1 and defend <= 3):
            defend = int(raw_input('How do you want to defend? '))

        self.defense = self.actions[defend-1];

        self.action(other)

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Mattias'

class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Powerful Enemy'
        self.hp = 200

    def decideAction(self, other):
        self.defense = self.actions[random.randint(0,2)]
        self.attack = self.actions[random.randint(0,2)]
        self.action(other)

player = Player()
enemy = Enemy()

print 'Player:'
print player.name
print player.hp
print 'versus'
print 'Enemy:'
print enemy.name
print enemy.hp

def we_do_not_have_a_winner(player, enemy):
    if player.hp <= 0:
        return False

    if enemy.hp <= 0:
        return False

    return True

def who_is_the_winner(player, enemy):
    if player.hp <= 0:
        congratulations_winner(enemy)

    if enemy.hp <= 0:
        congratulations_winner(player)

def congratulations_winner(character):
    print "Congratulations",character.name,", you are the winner!"

while we_do_not_have_a_winner(player, enemy):
    player.askForAction(enemy)
    print
    enemy.decideAction(player)
    print
    print 'Player hp:',player.hp,'Enemy hp:',enemy.hp
    print

who_is_the_winner(player, enemy)
