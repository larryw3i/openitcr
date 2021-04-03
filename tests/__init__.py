import os

def test_0():
    for (dirpath, dirnames, filenames) in os.walk('./openitcr'):
        for f in filenames:
            if f.endswith('.py'):
                os.system( f'python3 ./{dirpath}/{f}' )
    pass