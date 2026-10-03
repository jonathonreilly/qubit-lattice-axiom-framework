"""A = star involution, B = second cube-r2 involution; product AB: range, trace, growth; pickle symbols."""
import itertools, pickle
import numpy as np
from cliff_lines import affine_solutions
from cliff_enum import check
from cliff_poly import from_vecs, mmul, radius, trace, is_identity

pts, idx, Bs, L3, part, hom = affine_solutions("cube", 2)
L33 = (L3.astype(int) @ L3) % 2
sols = {}
for s in itertools.product([0, 1], repeat=len(hom)):
    coeff = part.astype(int).copy()
    for si, hv in zip(s, hom):
        if si:
            coeff = (coeff + hv) % 2
    f = (coeff @ Bs.astype(int)) % 2; h = (L33 @ f) % 2
    if all(check(f, h, pts, 2)):
        sols[s] = from_vecs(f, h, pts)
A = sols[(1, 0, 0, 0, 0, 0, 0, 0, 0)]
B = sols[(0, 0, 0, 0, 1, 0, 1, 0, 0)]
pickle.dump(A, open("Mz_A.pkl", "wb")); pickle.dump(B, open("Mz_B.pkl", "wb"))
AB = mmul(A, B); BA = mmul(B, A)
pickle.dump(AB, open("Mz_AB.pkl", "wb"))
print("A^2 = 1:", is_identity(mmul(A, A)), " B^2 = 1:", is_identity(mmul(B, B)), " AB == BA:", AB == BA)
print("radius(AB) =", radius(AB), " trace(AB) terms:", len(trace(AB)), " supports:", [len(AB[i][j]) for i in range(2) for j in range(2)])
P = AB
for t in range(1, 9):
    sup = len(P[0][0] | P[1][0])   # sites where alpha^t(X_0) is non-identity (X-part or Z-part)
    print(f"  t={t}: radius((AB)^t)={radius(P)}  |supp alpha^t(X_0)|={sup}")
    P = mmul(P, AB)
