import numpy as np, sys
sys.path.insert(0, '.')
from rge import *
# (1) SU(4) normalisation and the lane's Y = B-L on the left-handed surface
T15 = np.diag([1, 1, 1, -3])/(2*np.sqrt(6))
BmL = np.diag([1/3, 1/3, 1/3, -1.0])
print("tr T15^2 =", np.trace(T15@T15), " (canonical 1/2)")
print("T15 / (B-L) =", np.diag(T15)/np.diag(BmL), " sqrt(3/8) =", np.sqrt(3/8))
# lane Y = (1/3)P_sym - P_anti on C^2 (x) C^4 : same eigenvalues as B-L on the 4 (x2)
Y = np.kron(np.eye(2), BmL)
print("lane Y eigenvalues (with multiplicity):", sorted(np.round(np.diag(Y), 4)), " ; Tr Y =", np.trace(Y))
# (2) coupling of the unbroken combination Y' = T3R + sqrt(2/3) T15 : 1/g'^2 = sum c_i^2 / g_i^2
for g4, gR in ((1.0, 0.5), (1.0, 1e9), (0.5, 0.5)):
    c = np.array([1.0, np.sqrt(2/3)]); gi = np.array([gR, g4])
    print(f"g4={g4}, gR={gR}: g'^2 = {1/np.sum(c**2/gi**2):.4f}  (formula 1/(1/gR^2+(2/3)/g4^2) = {1/(1/gR**2+(2/3)/g4**2):.4f})")
# (3) SU(4) alone (no SU(2)_R): Y' = (B-L)/2 = sqrt(2/3) T15  ->  g'^2 = (3/2) g4^2
up = up_from_mz(MPL, 2)
for g4sq in (1.0, 0.25):
    gp2 = 1.5*g4sq
    y = down_from_mpl(gp2, 0.25, up, MZ, 2); o = observables(y)
    print(f"SU(4) only, g4^2={g4sq}: g'^2(M_Pl)={gp2}: sin2(MZ)={o['s2']:.4f}, 1/aem(MZ)={o['aem_inv']:.1f}")
# (4) the needed pair in SM terms, and required g4^2 for exact sin2 at gL^2=gR^2=SM-extrapolated g2^2
o = observables(up)
need_gp2 = o['gp2']; g2sq = o['g22']
need_inv = 1/need_gp2 - 1/g2sq              # = (2/3)/g4^2 if gR^2 = g2^2
print(f"SM-extrapolated (g2^2, gY^2)=({g2sq:.4f}, {need_gp2:.4f}); with gR^2=gL^2=g2^2 the PS relation needs (2/3)/g4^2 = {need_inv:.3f} -> g4^2 = {(2/3)/need_inv:.3f}")
# (5) SU(3) real need: g3^2(M_Pl) SM-extrapolated vs lane g4^2 = 1
print(f"SM-extrapolated g3^2 = {o['g32']:.4f} versus lane g3^2 = 1  (factor {1/o['g32']:.2f})")
