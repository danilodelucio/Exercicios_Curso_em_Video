def formatacao(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


t1 = "Danilo"
t2 = "PYTHON PARA NUKE COMPOSITORS"

formatacao(t1)
formatacao(t2)
formatacao("TCL - TOOL COMAND LANGUAGE")