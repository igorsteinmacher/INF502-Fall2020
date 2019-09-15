Montains = {'K2':8.611,'Everest':8.848,'Makalu':8.485,'Nanga Parbat':8.126,'Lhotse':8.516}

def list_montains(montains):
    for key,value in Montains.items():
        print(key,'is',value,'m tall')

def list_montains_ordered(montains,order):
    if (order):
        for key,value in sorted(Montains.items()):
            print(key,'is',value,'m tall')
    else:
        for key,value in Montains.items():
            print(key,'is',value,'m tall')


#ist_montains(Montains)

print("\n\n\n")  # 3 line breaks

list_montains_ordered(Montains,True)

print("\n\n\n")  # 3 line breaks

list_montains_ordered(Montains,False)


