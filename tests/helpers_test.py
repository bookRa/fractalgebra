# {'whole': '-1', 'numer': None, 'denom': None} -> valid
# {'whole': None, 'numer': None, 'denom': '/2'} -> invalid
# {'whole': None, 'numer': '-1', 'denom': None} -> convert to {'whole': '-1'}
# {'whole': None, 'numer': '-1', 'denom': '/2'} -> valid
# {'whole': '-1', 'numer': None, 'denom': '/2'} -> invalid
# {'whole': '-1', 'numer': '4', 'denom': None} -> invalid
# {'whole': '-1', 'numer': '-1', 'denom': '/-2'} -> valid