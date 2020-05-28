#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matea Fax
#
# Created:     28.05.2020
# Copyright:   (c) Matea Fax 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from vjezba_9.Mine.Polje import Polje


p = Polje(5,2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
        print(k, end = '|')
    print()

print('\n*** test 2 ***')
print('*** rezultat varira zbog slucajnog izbora mina koristenjem random modula ***')
p = Polje(5,2)
for red in p._Polje__kvadrati:
    for k in red:
        k.otkrij()
print(p)
