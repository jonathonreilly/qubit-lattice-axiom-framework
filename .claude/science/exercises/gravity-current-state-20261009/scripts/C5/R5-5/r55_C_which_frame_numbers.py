"""R5-5 (C): which-frame phase written by one propagating quantum, using R4-1's refereed per-realization deviation as coupling.
Inputs (R4-1 refereed + this probe's A):
  R_l = P*(l/a)^3 : relative per-realization deviation at field scale l (R4-1: limsup R_l (a/l)^3 > 0; P measured on finite windows,
                    log-periodic; values used: 4-shell {1,2,3,4} P ~ 4.2 (2.87e4 at l=19); smooth-f L=3 P ~ 2.0e-3; flat L=4 P ~ 5.9e-4).
  frame gradient  : rms[eps(u)-eps(u')] ~ sqrt(2) R_l d/xi_F, xi_F ~ 0.4-0.6 (A), i.e. ~3 R_l d for d << xi_F.
BRIDGES (stated, not derived; R4-1 is an off-shell Gaussian operator test, its referee: 'not yet a direct observable'):
  B1 (massless, eikonal):  branch phase difference Phi(d) = [3 d R_l] * k c T / 2,     l = 1/k  (k = 2 pi/lambda)
  B2 (massive, rest-frame phase): Phi(d) = [3 d R_l] * M c^2 tau / (2 hbar),          l = lambda_C = hbar/(M c)
One quantum resolves the frame to d_1 = distance at which Phi = 1 rad.
"""
import numpy as np
hbar = 1.054571817e-34; c = 2.99792458e8; lP = 1.616255e-35; u_ = 1.66053907e-27
mp = 1.67262192e-27; me = 9.1093837e-31; Gpc = 3.0857e25
Ps = {"4-shell{1,2,3,4} P=4.2": 4.2, "smooth-f L=3 P=2e-3": 2.0e-3, "flat L=4 P=5.9e-4": 5.9e-4}
cases_massless = [("optical photon 500 nm, 1 m lab arm", 500e-9, 1.0/c),
                  ("optical photon 500 nm, 1 Gpc (quasar/GRB)", 500e-9, Gpc/c),
                  ("radio 21 cm, 1 Gpc", 0.21, Gpc/c),
                  ("gamma 1 GeV (1.24e-15 m), 1 Gpc", 1.24e-15, Gpc/c)]
cases_massive = [("electron, tau = 1 ns (biprism)", me, 1e-9, 1),
                 ("neutron, tau = 0.1 ms (crystal interferometer)", mp, 1e-4, 1),
                 ("Cs-133 atom, 70 s (sum over 133 nucleons)", mp, 70.0, 133),
                 ("25 kDa molecule, 7 ms (sum over nucleons)", mp, 7e-3, 25000)]
for a in (lP, 1e-19):
    print(f"\n######## lattice spacing a = {a:.3e} m")
    for name, P in Ps.items():
        print(f"  kernel {name}")
        for lab, lam, T in cases_massless:
            k = 2*np.pi/lam; l = 1/k
            R = P*(l/a)**3
            Phi1 = 3*R*k*c*T/2              # per unit frame distance
            print(f"    {lab:45s}: l/a = {l/a:9.2e}, R_l = {R:9.2e}, Phi per unit d = {Phi1:9.2e} rad, d_1 = {1/Phi1:9.2e}")
        for lab, M, tau, N in cases_massive:
            lC = hbar/(M*c); R = P*(lC/a)**3
            Phi1 = N*3*R*M*c**2*tau/(2*hbar)
            print(f"    {lab:45s}: lC/a = {lC/a:9.2e}, R_lC = {R:9.2e}, Phi per unit d = {Phi1:9.2e} rad, d_1 = {1/Phi1:9.2e}")
# kernel-scale needed for a single quantum NOT to resolve the frame at d ~ xi_F (Phi(xi_F) < 1), under the illustrative
# P ~ (a/l_k)^4.5 (R4-1 E fit, L<=4; extrapolation barred, illustration only)
print("\n######## illustration only (R4-1 fit P ~ 0.32 (l_k/a)^-4.5, extrapolation barred): kernel scale l_k at which one quantum")
print("         writes < 1 rad between frames a distance xi_F = 0.5 apart")
for a in (lP,):
    for lab, lam, T in cases_massless:
        k = 2*np.pi/lam; l = 1/k
        need_P = 1/(3*0.5*(l/a)**3*k*c*T/2)
        lk = a*(need_P/0.32)**(-1/4.5)
        print(f"    {lab:45s}: P needed {need_P:9.2e} -> l_k ~ {lk:9.2e} m  (l = {l:.2e} m)")
    for lab, M, tau, N in cases_massive:
        lC = hbar/(M*c)
        need_P = 1/(N*3*0.5*(lC/a)**3*M*c**2*tau/(2*hbar))
        lk = a*(need_P/0.32)**(-1/4.5)
        print(f"    {lab:45s}: P needed {need_P:9.2e} -> l_k ~ {lk:9.2e} m  (lambda_C = {lC:.2e} m)")
# comparator: Pikovski et al. time-dilation coupling, branch energy difference = E_int * g dx / c^2
g = 9.81; dx = 1e-6
print(f"\ncomparator (Pikovski et al. 2015 mechanism): branch phase-rate difference per unit rest energy = g dx/c^2 = {g*dx/c**2:.2e} (dx = 1 um);")
print(f"  here (B2) per unit rest energy and unit frame distance = 3 R_lC, e.g. nucleon at a=l_P, flat L=4 kernel: {3*5.9e-4*(hbar/(mp*c)/lP)**3:.2e}")
