
try:
    with open('fdsfsa', 'r') as f:
        pass
except IOError as e:
    print 'IOError'
    print e

with open('nowrite', 'w') as f:
    pass

