from walks import *
S = nn_support()
print("nn support entries:", S.sum())
for ci in range(4):
    D = class_D(ci)
    C = commutant_basis(list(D.values()))
    B = covariant_basis(D)
    Bn = covariant_basis(D, S)
    # commutant of shifted action Dp = INV D INV
    Cp = commutant_basis([INV @ x @ INV for x in D.values()])
    print(ci, "comm dim", len(C), "covariant dim (27 offsets)", len(B), "nn-covariant dim", len(Bn))
