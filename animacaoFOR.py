

def FuncaoTempo(tempo):
    import time, sys

    for i in range(tempo,0, -1):
          sys.stdout.write("\r{}".format(i))
          sys.stdout.flush()
          time.sleep(1)

    print ("\nFim")







