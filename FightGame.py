import random

class RangeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

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

        while True:
            try:
                attack = int(raw_input('How do you want to attack? '))
                if not (attack >= 1 and attack <= 3):
                    raise RangeError('You can only enter the numbers 1 to 3.')
                break
            except ValueError:
                print 'You can only enter numbers!'
            except RangeError as e:
                print e.value

        self.attack = self.actions[attack-1];

        while True:
            try:
                defend = int(raw_input('How do you want to defend? '))
                if not (defend >= 1 and defend <= 3):
                    raise RangeError('You can only enter the numbers 1 to 3.')
                break
            except ValueError:
                print 'You can only enter numbers!'
            except RangeError as e:
                print e.value

        self.defense = self.actions[defend-1];

        self.action(other)

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Player'

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

player.name = str(raw_input('What is your name? '))

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
