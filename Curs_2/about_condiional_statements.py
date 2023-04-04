# Flow control - sunt folosite pentru a lua decizii. Practic se evalueaza daca o conditie este indeplinita (este
# adevarata). Daca este indeplinita, se executa ceva, daca nu este indeplinita, atunci se executa altceva.
#
# De exemplu mergem la bancomat sa scoatem bani si avem urmatorul flow: (voi scrie in pseudocod sa se inteleaga)
# 1. Prima data bagam cardul si ni se cere codul pin. Noi il introducem.
# Se face urmatoarea verificare:
# daca(si) pin corect:
#         executa_instructiune1: redirectioneaza catre alege suma
#         executa_instructiune2: alege suma
#         # din nou se va face o verificare daca aveti suma respectiva in cont
#  daca(si) suma_disponibila_in_cont:
#               executa_intructiune3: primeste_bani
#         altfel(else):
#            executa_instructiune4: afiseaza "Sold insuficient, alege alta suma"
#         ..................
# altfel(else):
#         executa_instructiune5: afiseaza "Pinul este gresit"
#
#
#
#
# ------------------------
# < Dacă > Syntaxa:
#
# dacă <expresie>:
#     <instructiune1>
# ------------------------
# <Dacă altceva> Syntaxa:
# dacă <expresie>:
#     <instructiune1>
# altfel:
#     <instructiune2>
#
# -------------------------
# <nested if else> Exemplu
# dacă <expresie>:
#  dacă<expresie>:
#         <instructiune1>
#  altfel:
#         <instructiune2>
# altfel:
#     <instructiune3>
# --------------------------
# <dacă elif altceva> Syntaxa
# dacă <expresie>:
#     <instructiune1>
# elif <expresie>:
#     <instructiune2>
# elif <expresie>:
#     <instructiune3>
# altfel:
#     <instructiune4>
