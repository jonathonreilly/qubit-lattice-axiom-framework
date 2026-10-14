"""Panel D, qinfo lens. Tiny arithmetic only (no arrays).
(1) Proton-decay floor on the grid scale when fermion number is conserved only mod 4 (X2):
    dim-6 qqql with coefficient C/Lambda^2, Lambda = 1/a.
(2) Per-site register tally for each route, with and without a local fermion->qubit encoding.
(3) Approximate-GW (finite-n) register cost from F2's Zolotarev rates.
Inputs are labelled comparator (recalled) where not from the packet.
"""
import math
GeV_to_inv_s = 1.519e24     # 1 GeV = 1.519e24 s^-1 (hbar)
yr = 3.156e7
# --- (1) proton decay p -> e+ pi0 from (C/Lambda^2) qqql  [comparator: standard chiral-Lagrangian estimate, recalled]
m_p, f_pi, alphaH, DF = 0.938, 0.130, 0.0144, 1.27   # GeV, GeV, GeV^3, D+F
bound_yr = 2.4e34                                    # Super-K p->e+pi0 (comparator, recalled)
def tau_yr(Lam_over_sqrtC):
    G = m_p*alphaH**2*(1+DF)**2/(32*math.pi*f_pi**2*Lam_over_sqrtC**4)
    return 1.0/(G*GeV_to_inv_s)/yr
lo, hi = 1e10, 1e20
for _ in range(200):
    mid = math.sqrt(lo*hi)
    lo, hi = (mid, hi) if tau_yr(mid) < bound_yr else (lo, mid)
Lmin = hi
print("(1) proton decay: need Lambda/sqrt|C| >= %.2e GeV (tau(1e16)=%.1e yr)" % (Lmin, tau_yr(1e16)))
for name, C in [("C=1 (no suppression)",1.0),("C=eps^2, eps=0.13 (X2 link channel, one leakage per light pair)",0.13**2),
                ("C=W*eps^4, eps=0.13",0.13**4),("C=W*eps^4, eps=0.02",0.02**4)]:
    print("    %-62s 1/a >= %.1e GeV" % (name, Lmin*math.sqrt(C)))
print("    margin at 1/a = M_Pl=1.22e19 GeV, C=1: tau/bound = %.1e" % (tau_yr(1.22e19)/bound_yr))
# --- (2) register per Z^3 cell
# fermion modes per cell (packet numbers) ; local encodings in 3D cost ~2-3 qubits per mode (comparator: Verstraete-Cirac ~2, BK-superfast ~3 on cubic)
routes = {
 "one qubit (axiom literal)": 1,
 "SM gauge multiplets only, 1 gen, staggered-type (3 colour x ... min on-site rep)": None,
 "X2 walker package (2 x 16), all 3 generations": 32,
 "KS/staggered 16-carrier (F6:147)": 16,
 "C5 gravity root (panel F: ~22.5 Dirac fields x 4)": 90,
 "F4/X1 slab 3x16x4xL, L=4..6": (3*16*4*4, 3*16*4*6),
}
print("(2) fermion modes per cell -> qubits with a local 3D encoding (x2..x3)")
for k,v in routes.items():
    if v is None: continue
    if isinstance(v, tuple):
        print("    %-55s modes %d..%d  qubits ~%d..%d" % (k, v[0], v[1], 2*v[0], 3*v[1]))
    else:
        print("    %-55s modes %d  qubits ~%d..%d" % (k, v, 2*v, 3*v))
# minimum on-site content forced by exact on-site gauge invariance (rep theory):
# per generation, mode-space must carry Q(3,2)=6, u(3)=3, d(3)=3, L(2)=2, e=1, nu=1 -> 16 complex modes per Weyl component
print("    exact on-site G_SM forces the mode space at a cell to contain every multiplet: >= 16 modes per Weyl component per generation")
# --- (3) finite-n GW: Zolotarev ~2.4-3.0 decades per pole (F2 T3b/c), ~2 aux Dirac per pole
for delta_exp in (35, 88):
    for rate in (2.4, 3.0):
        n = math.ceil(delta_exp/rate)
        aux = 2*n
        modes_gen = 16*4*(1+aux)    # 16 projected Dirac fields x 4 spinor comps x (1+aux)
        print("(3) delta=1e-%d rate %.1f: n=%d poles, ~%d aux Dirac/field, ~%d modes/cell/gen, ~%d for 3 gen"
              % (delta_exp, rate, n, aux, modes_gen, 3*modes_gen))
