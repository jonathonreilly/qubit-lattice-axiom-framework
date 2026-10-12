#!/usr/bin/env python3
"""R7-2 numbers: hyperbolic honeycombs, dS entropy / N-bound counts, CKN,
dS/CFT complex weights, graviton polarization counts.
Constants are standard (CODATA / Planck 2018 central values, quoted from memory
and labelled COMPARATOR in the report)."""
import numpy as np
from math import pi, sqrt, log, log10, acosh

print("=== 1. Regular hyperbolic honeycombs {p,q,r}: edge length in curvature units ===")
def honeycomb(p, q, r):
    m = np.full((4, 4), 2.0)
    m[0, 1] = m[1, 0] = p
    m[1, 2] = m[2, 1] = q
    m[2, 3] = m[3, 2] = r
    G = -np.cos(pi / m)
    np.fill_diagonal(G, 1.0)
    ev = np.linalg.eigvalsh(G)
    Gi = np.linalg.inv(G)
    # vertex P_i is opposite mirror i; <v_i,v_k> = Gi[i,k]
    def dist(i, k):
        c = abs(Gi[i, k]) / sqrt(Gi[i, i] * Gi[k, k])
        return acosh(c)
    half_edge = dist(0, 1)
    return ev, Gi[0, 0], 2 * half_edge

for (p, q, r) in [(4, 3, 4), (5, 3, 4), (4, 3, 5), (3, 5, 3), (5, 3, 5)]:
    ev, g00, e = honeycomb(p, q, r)
    sig = "".join("+" if x > 1e-12 else ("-" if x < -1e-12 else "0") for x in ev)
    if (p, q, r) == (4, 3, 4):
        print(f"{{{p},{q},{r}}}: Gram eigen-signature {sig} (Euclidean, degenerate) -> Z^3, edge free")
        continue
    # vertex figure {q,r}: number of edges at a vertex
    vf_edges = {(3, 4): 6, (3, 5): 12, (5, 3): 20, (4, 3): 8, (3, 3): 4}[(q, r)]
    print(f"{{{p},{q},{r}}}: signature {sig}; vertex figure {{{q},{r}}} -> {vf_edges} neighbours/site;"
          f" edge length a = {e:.6f} * (curvature radius)")

print("\nZ^3 = {4,3,4} has vertex figure {3,4} (octahedron, 6 neighbours, site stabilizer O_h).")
print("{5,3,4} has the SAME vertex figure {3,4}: 6 neighbours, octahedral site stabilizer;")
print("its cells are dodecahedra, 4 around each edge.  It has no translation subgroup Z^3.")

lP = 1.616255e-35       # m
c = 2.99792458e8
H0 = 67.36 * 1e3 / 3.0857e22   # s^-1 (Planck 2018 TT,TE,EE+lowE+lensing)
OmL = 0.6847
Lam = 3 * H0**2 * OmL / c**2
print(f"\nLambda_obs = 3 H0^2 Omega_L / c^2 = {Lam:.4e} m^-2 ; Lambda*lP^2 = {Lam*lP**2:.4e}")

_, _, e534 = honeycomb(5, 3, 4)
ell = lP / e534
LamAdS = -3 / ell**2
print(f"\n{{5,3,4}} at edge = l_P: curvature radius = {ell:.3e} m; as an AdS4 bulk Lambda = {LamAdS:.3e} m^-2"
      f" = {LamAdS/Lam:.3e} x Lambda_obs (wrong sign, |ratio| 10^{log10(abs(LamAdS/Lam)):.1f})")
RH = c / H0
for Ok in [2e-3, 5e-3]:
    Rcurv_min = RH / sqrt(Ok)
    print(f"  spatial-curvature bound |Omega_K| < {Ok}: curvature radius > {Rcurv_min:.3e} m;"
          f" {{5,3,4}} at l_P misses it by 10^{log10(Rcurv_min/ell):.1f} in radius")
print("  DESI DR2 (TESTS:2993): 10^3 Omega_K = 2.3 +- 1.1 -> same order.")

print("\n=== 2. de Sitter entropy, N-bound, qubit counts ===")
R = sqrt(3 / Lam)
S = pi * R**2 / lP**2           # = 3 pi /(Lambda lP^2), nats
Nq = S / log(2)
print(f"R_dS = sqrt(3/Lambda) = {R:.4e} m ; R/l_P = {R/lP:.4e}")
print(f"S_dS = 3 pi/(Lambda l_P^2) = {S:.4e} nats ; qubits N_q = S/ln2 = {Nq:.4e}")
print(f"check: 3*pi/(Lam lP^2) = {3*pi/(Lam*lP**2):.4e}")
print(f"area per qubit on the horizon: A/N_q = 4 ln2 l_P^2 = {4*log(2):.4f} l_P^2 -> spacing {sqrt(4*log(2)):.4f} l_P")
V = 4 * pi / 3 * R**3
print(f"Planck-spaced Z^3 sites in the static patch: V/l_P^3 = {V/lP**3:.4e} ; ratio to N_q = 10^{log10(V/lP**3/Nq):.2f}")
amin = (V / Nq) ** (1 / 3)
print(f"N-bound on a volume-filling qubit lattice: a >= (V/N_q)^(1/3) = {amin:.3e} m (= {amin/1e-15:.2f} fm)")
print("  compare collider contact/locality bound ~1e-19 m (TESTS X1: ~4e-20 m): excluded by >= 4 decades")
print("Bousso/AXIOM_FIRST_BEKENSTEIN note C3 writes S_dS = pi/(G Lambda); correct 4D value is 3 pi/(G Lambda):"
      f" pi/(Lam lP^2) = {pi/(Lam*lP**2):.4e} vs {3*pi/(Lam*lP**2):.4e}")

print("\n=== 3. CKN (Cohen-Kaplan-Nelson) cutoffs with L = c/H0 ===")
hbarc_GeVm = 1.97327e-16   # GeV m
MP = 1.22089e19            # GeV (non-reduced Planck mass)
L_GeVinv = RH / hbarc_GeVm
LamUV_ent = (MP**2 / L_GeVinv) ** (1 / 3)
LamUV_bh = sqrt(MP / L_GeVinv)
print(f"entropy form  L^3 Lam_UV^3 < (L M_P)^2 : Lam_UV < {LamUV_ent:.3e} GeV (length {hbarc_GeVm/LamUV_ent:.2e} m)")
print(f"BH form       L^3 Lam_UV^4 < L M_P^2   : Lam_UV < {LamUV_bh:.3e} GeV = {LamUV_bh*1e12:.2f} meV")
rho_bh = LamUV_bh**4
rho_L = 3 * (H0 * 6.582e-25)**2 * (MP**2) / (8 * pi) * OmL  # GeV^4, rho_L = Lambda M_P^2/(8 pi)
print(f"  CKN rho ~ Lam_UV^4 = {rho_bh:.3e} GeV^4 ; observed rho_Lambda = {rho_L:.3e} GeV^4 ; ratio {rho_bh/rho_L:.2f}")

print("\n=== 4. Count restatements of Lambda's size ===")
V4 = 6.389e242   # R4-5 past cone in l_P^4 (TESTS:2939)
print(f"R4-5 past-cone 4-volume V4 = {V4:.3e} l_P^4 ; 1/sqrt(V4) = {1/sqrt(V4):.3e} ; Lambda l_P^2 = {Lam*lP**2:.3e}")
print(f"S_dS = {S:.3e} ; sqrt(V4) = {sqrt(V4):.3e} ; ratio S/sqrt(V4) = {S/sqrt(V4):.2f}")
print(f"(l_dS/l_P)^2 = {(R/lP)**2:.3e}  [dS/CFT: |c_T| ~ l^2/G ~ N]")

print("\n=== 5. dS4/CFT3 weights Delta = 3/2 +- sqrt(9/4 - m^2 l^2) ===")
hbarc_eVm = 1.97327e-7
mth = 1.5 * hbarc_eVm / R
print(f"complex (principal-series) weights for m > 3/(2 l_dS): m_th c^2 = {mth:.3e} eV")
for name, m_eV in [("nu (0.05 eV)", 0.05), ("electron", 0.51099895e6), ("proton", 938.272e6), ("Higgs", 125.25e9)]:
    ml = m_eV * R / hbarc_eVm
    print(f"  {name:12s}: m l_dS = {ml:.3e} -> Im Delta = {sqrt(ml**2-2.25):.3e}")

print("\n=== 6. Propagating graviton polarizations D(D-3)/2 ===")
for D in [2, 3, 4, 5]:
    n = D * (D - 3) // 2
    print(f"  D = {D}: {max(n,0)} (formula {n})")
print("Explicit HaPPY ({5,4} tiling: AdS3), DSSYK (dS2/dS3), TT-bar+Lambda2 (dS3) all sit at D <= 3: no gravitational waves.")
