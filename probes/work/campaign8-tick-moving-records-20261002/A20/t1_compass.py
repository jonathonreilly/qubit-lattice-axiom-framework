"""Task 1 checks.
(a) compass gates exp(-i th X0X1) [x-bond] and exp(-i th Y0Y2) [y-bond] commute up to phase iff th in (pi/2)Z.
(b) the Clifford angle th=pi/4: Heisenberg images differ with order (exact Pauli algebra).
(c) th=pi/2: product over ALL bonds acts as identity automorphism (each sigma^b_x anticommutes with 4 bond terms).
(d) star family S_x = prod_a sigma^a_{x+e_a} sigma^a_{x-e_a}: pairwise commuting, exactly O-covariant with signs.
"""
import numpy as np
import itertools
from grp import named
from pauli import P, rotate

I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
def kron(*ms):
    out = np.array([[1.0]])
    for m in ms:
        out = np.kron(out, m)
    return out

A = kron(X, X, I2)       # sites (0, 1=+e_x, 2=+e_y)
B = kron(Y, I2, Y)
def expP(Pm, th):
    return np.cos(th) * np.eye(8) - 1j * np.sin(th) * Pm

print("(a) up-to-phase commutation residual min_lambda ||GaGb - lambda GbGa|| :")
for th in [0.0, 0.3, np.pi / 4, 1.0, np.pi / 2, 2.0, np.pi]:
    Ga, Gb = expP(A, th), expP(B, th)
    M1, M2 = Ga @ Gb, Gb @ Ga
    lam = np.vdot(M2.flatten(), M1.flatten()) / np.vdot(M2.flatten(), M2.flatten())
    print(f"   th={th:.4f}  lambda={lam:.3f}  residual={np.linalg.norm(M1 - lam * M2):.2e}")

# (b) exact Heisenberg images at pi/4: Ad_{C_A}(Q) = i Q A if {Q,A}=0 else Q
def ad_cliff(Agen, Q):
    return Q if Q.commutes(Agen) else P(1) * Q * Agen
Ap = P.single((0, 0, 0), 0) * P.single((1, 0, 0), 0)
Bp = P.single((0, 0, 0), 1) * P.single((0, 1, 0), 1)
Q = P.single((0, 0, 0), 2)
print("(b) pi/4: Ad_A Ad_B (Z0) =", ad_cliff(Ap, ad_cliff(Bp, Q)), "   Ad_B Ad_A (Z0) =", ad_cliff(Bp, ad_cliff(Ap, Q)))

# (c) count anticommuting bond terms touching sigma^b_0
e = np.eye(3, dtype=int)
bonds = []
for a in range(3):
    for s in [0, -1]:
        x = tuple(s * e[a]); y = tuple((s + 1) * e[a])
        bonds.append(P.single(x, a) * P.single(y, a))
for b in range(3):
    n = sum(1 for t in bonds if not t.commutes(P.single((0, 0, 0), b)))
    print(f"(c) sigma^{'xyz'[b]}_0 anticommutes with {n} compass bond terms (even -> fixed by the pi/2 product)")

# (d) star family
def star(x):
    p = P()
    for a in range(3):
        p = p * P.single(tuple(int(c) for c in np.add(x, e[a])), a) * P.single(tuple(int(c) for c in np.subtract(x, e[a])), a)
    return p
S0 = star((0, 0, 0))
bad = [d for d in itertools.product(range(-3, 4), repeat=3) if not S0.commutes(star(d))]
print("(d) offsets d (|d|_inf<=3) with [S_0, S_d] != 0:", bad)
O = named()["all"]
nfix = sum(1 for R in O if rotate(S0, R) == S0)
print(f"(d) rotations fixing S_0 exactly (with sign): {nfix}/24 ; S_0 hermitian: {S0.is_hermitian()} ; S_0 = {S0}")
