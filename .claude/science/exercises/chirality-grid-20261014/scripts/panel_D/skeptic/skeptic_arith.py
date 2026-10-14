"""Panel D skeptic: two back-of-envelope rows (suggested-grade arithmetic only).
(1) Option D1(a): if a physical 'site' is a cubic block of b^3 axiom sites (one qubit each),
    what b holds each route's per-site content, with and without a local fermion->qubit
    encoding overhead (assumed ~3 qubits per complex fermion mode on Z^3, e.g. qubits on
    the 3 edges per vertex, Bravyi-Kitaev-superfast style; an assumption, not a derivation)?
(2) X2's 'fermion number only mod 4': a Delta F = 4 channel such as p -> e+ pi0 (quarks and
    leptons counted alike: F goes 3 -> -1). If it is mediated at dimension 6 by a Planck-scale
    sector, tau ~ hbar * Lambda^4 / m_p^5 with O(1) coefficients.
"""
import math
routes = {"X2 corner package (walker C2 x Spin(10) 16)": 32,
          "minimal onsite SMG (4 staggered = 16 Weyl)": 16,
          "F4 inflow slab (~10^3 fermion qubits, 3 gens)": 1000}
for name, modes in routes.items():
    for overhead in (1, 3):
        q = modes * overhead
        b = math.ceil(round(q ** (1/3), 9))
        print(f"{name:48s} modes={modes:5d} overhead={overhead} qubits={q:5d} block b={b:2d} (b^3={b**3})")
hbar_GeVs = 6.582e-25
m_p = 0.938272
yr = 3.156e7
for Lam in (1.22e19, 2.4e18, 1e16):
    Gamma = m_p**5 / Lam**4
    tau_yr = hbar_GeVs / Gamma / yr
    print(f"Lambda={Lam:.2e} GeV: tau(p->e+pi0, dim-6, O(1) coeff) ~ {tau_yr:.1e} yr; bound ~2.4e34 yr; margin {tau_yr/2.4e34:.1e}")
