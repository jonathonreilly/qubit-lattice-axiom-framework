"""
T233 - the bridge: the record field's own massless content determines G.

R85/R132/R135 : 1/G is ADDITIVE in field content, with G_ind = 12 pi tau0 per
                REAL SCALAR.  A Dirac fermion counts as 2 (one Dirac gives
                G = 6 pi tau0 = 12 pi tau0 / 2).
R72/R76       : with 4 tastes x 2 per Dirac = 8, G = (3/2) pi tau0.  And R76
                states the open item explicitly: "fixing G in terms of field
                content makes the content the only free thing left."
R151          : the ordered record field's massless content is SIX real
                Goldstone modes (SU(4) -> U(3), 15 - 9 = 6 = dim CP^3).

So the framework's own field content now determines G.
"""
import numpy as np
pi = np.pi

def G_of(N):      # 1/G = N/(12 pi tau0)   in units of tau0
    return 12*pi/N

print("   content                                  N    G/tau0     G")
for name, N in (("R72's assumption: 4 tastes x 2/Dirac", 8),
                ("one Dirac fermion (R76 cross-check)", 2),
                ("R151: the record field's 6 Goldstones", 6)):
    print(f"   {name:38s} {N:3d}  {G_of(N):8.4f}   {G_of(N)/pi:.4g} pi tau0")

print(f"\n   cross-check of the additivity convention:")
print(f"     one Dirac -> G = {G_of(2)/pi:.4g} pi tau0   (R76 states 6 pi tau0)")
print(f"     4 tastes  -> G = {G_of(8)/pi:.4g} pi tau0   (R72 states 1.5 pi tau0)")

G8, G6 = G_of(8), G_of(6)
print(f"\n   ratio G(6 Goldstones)/G(R72's 8) = {G6/G8:.6f}  (= 8/6 = 4/3)")
print(f"   ell_P scales as sqrt(G):  factor {np.sqrt(G6/G8):.6f}  (= sqrt(4/3))")
lp8 = 0.45
print(f"   R73 gives ell_P = {lp8}a for N=8;  for N=6 that becomes "
      f"{lp8*np.sqrt(G6/G8):.4f}a")
tau0 = lp8**2/G8
print(f"\n   tau0 from ell_P^2 = G at N=8:  tau0 = {tau0:.5f} a^2")
print(f"   the SAME tau0 at N=6 gives ell_P = {np.sqrt(G6*tau0):.4f} a  "
      f"(consistent: G and ell_P^2 move together at fixed tau0)")
print(f"\n   => the framework's own matter content fixes  G = 2 pi tau0,")
print(f"      i.e. ell_P ~ 0.52 a rather than 0.45 a.")
