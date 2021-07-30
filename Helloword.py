import sys
def hello(who):
    print('Hello World {}'.format(who))

who = sys.argv[1]
hello(who)
