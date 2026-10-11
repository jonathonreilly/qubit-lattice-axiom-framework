# Seagull (tadpole) feed of a z=3 lattice graviton's spatial self-coupling into its z=1 (speed) coefficient.
# Lattice units a = 1, M_P = 1 (a^-1 = M_Pl). Graviton (one TT-like scalar component, canonical up to M_P):
#   Euclidean quadratic form: omega_hat^2 + p_hat^2 + C p_hat^6, C = (M_P/M*)^4 = L^4.
# Seagull from the z=3 term (coefficient C, 4 of 6 derivatives on loop legs) shifts the k^2 coefficient by
#   delta = C * Int_BZ d^3p/(2pi)^3 p_hat^4 * G(p),  G = Int domega/(2pi) 1/(omega_hat^2 + A(p)),  A = p_hat^2 + C p_hat^6
# (O(1) combinatorial factors dropped: suggested power counting, one component).
#  discrete time (Z^4 tick, omega in BZ, omega_hat = 2 sin(omega/2)):  G = 1/sqrt(A(A+4))
#  continuous time (Z^3 x R):                                         G = 1/(2 sqrt(A))
import numpy as np
n = 96
ks = (np.arange(n) + 0.5) * 2*np.pi/n - np.pi
kx, ky, kz = np.meshgrid(ks, ks, ks, indexing='ij')
p2 = 4*(np.sin(kx/2)**2 + np.sin(ky/2)**2 + np.sin(kz/2)**2)
print(" L=M_P/M*      C=L^4       delta_disc     delta_cont     cont/(L^2)")
for L in [1, 10, 1e2, 1e3, 1e4, 1e6, 8.14e8]:
    C = float(L)**4
    A = p2 + C*p2**3
    Gd = 1/np.sqrt(A*(A+4))
    Gc = 1/(2*np.sqrt(A))
    dd = C*np.mean(p2**2*Gd)   # mean over BZ = Int d^3p/(2pi)^3
    dc = C*np.mean(p2**2*Gc)
    print(f"{L:10.3e} {C:12.3e} {dd:14.5e} {dc:14.5e} {dc/L**2:12.5f}")
print("Expected: delta_disc -> const = mean(1/p_hat^2) =", np.mean(1/p2), "(Watson-type BZ integral, ~0.25)")
