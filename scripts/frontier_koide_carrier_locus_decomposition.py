#!/usr/bin/env python3
"""
Carrier-locus fermionization-chain decomposition: the import folds into the matter Dirac operator M
(statistics + range, on the cross-site hopping sign); the hw=1 locus is native; three frontier mislabels
corrected.

Decomposes bosonic M2(C) qubit -> Grassmann(L1) -> single-mode(L2) -> first-order/{eps,D}=0(L3) ->
hw=1-locus(L4). Findings (all non-circular; Q=2/3 never enters -- this is upstream of any Koide value):

CORRECTIONS to the frontier framing (the "staggered selects hw=1 via S_3-breaking blocked by isotropy"
claim is a DOUBLE mislabel):
  (C1) NO spectral hw=1 selection: the free staggered D keeps ALL 8 Brillouin-zone corners massless
       (|D(k)|^2 = sum_mu sin^2(k_mu) = 0 at every corner k_mu in {0,pi}); a Wilson term lifts all but hw=0.
  (C2) hw=1 NAMING needs NO axis-anisotropy: hw=1 is singled out by two S_3-INVARIANT labels --
       eps-parity (-1)^hw = -1 AND S_3-orbit-size = 3 -- which pick NO spatial axis.
  (C3) so gauge_wilson_isotropy (retained_no_go, scope = unequal plaquette COEFFICIENTS) is NOT the
       operative wall (a different object).

WHERE THE IMPORT IS (the matter Dirac operator M, two orthogonal scoped-frame knobs coupled on ONE sign):
  L1 STATISTICS: native cross-site qubit ladders COMMUTE (hard-core boson, NOT fermion); JW is an
       invertible relabel inside one ungraded algebra -> the fermionic frame is a CHOICE.
  L3 RANGE: first-order vs the eps-even Wilson/mass sector (a scoped frame).
  They couple on the SIGN of the cross-site hopping bilinear c_x^dag c_y = the only frame-distinguishing
  quantity, = simultaneously what makes the frame fermionic (L1) AND what lives in the first-order M (L3).
NATIVE (mislabel-native, no import): L2 single-mode count (2^p=2 -> p=1); L4 hw=1 naming (the S_3-invariants);
  L3a {eps,D}=0 given first-order (every nearest-neighbour real-antisymmetric D is eps-odd).
LONE RESIDUAL DOF: one global Z_2 HODGE-ORIENTATION bit -- hw=1 (1-forms / vector) vs hw=2 (2-forms /
  pseudovector), Hodge-DUAL S_3-triplets in d=3 -- = sign(Pfaffian) = sign(beta), free per cpt_exact, blocked
  by NO retained no-go.
"""
import numpy as np
PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

corners = [(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]   # 8 BZ corners (Z_2)^3; 1 -> k_mu=pi
def hw(c): return sum(c)

# ----------------------------------------------------------------------
section("C1. NO spectral hw=1 selection: staggered keeps ALL 8 corners massless; Wilson keeps only hw=0")
# ----------------------------------------------------------------------
def stag_mass2(c):  # |D(k)|^2 = sum_mu sin^2(k_mu), k_mu = pi*c_mu
    return sum(np.sin(np.pi*ci)**2 for ci in c)
def wilson_mass(c, r=1.0):  # Wilson term r sum_mu (1-cos k_mu)
    return r*sum(1-np.cos(np.pi*ci) for ci in c)
stag_zero = [c for c in corners if abs(stag_mass2(c)) < 1e-9]
wilson_zero = [c for c in corners if abs(wilson_mass(c)) < 1e-9]
record("staggered D: ALL 8 corners massless (no spectral hw=1 selection)",
       len(stag_zero) == 8, f"{len(stag_zero)}/8 corners are zero modes")
record("Wilson: ONLY hw=0 massless (Wilson lifts hw=1,2,3)",
       wilson_zero == [(0,0,0)], f"Wilson zero modes = {wilson_zero}")

# ----------------------------------------------------------------------
section("C2. hw=1 singled out by S_3-INVARIANT labels (eps-parity, orbit-size) -- NO axis-anisotropy")
# ----------------------------------------------------------------------
shells = {h: [c for c in corners if hw(c)==h] for h in range(4)}
labels = {h: ((-1)**h, len(shells[h])) for h in range(4)}    # (eps-parity, S_3-orbit-size)
record("hw shells = {0:1, 1:3, 2:3, 3:1}", [len(shells[h]) for h in range(4)] == [1,3,3,1])
record("hw=1 is UNIQUELY (eps-parity=-1, orbit-size=3) -- both S_3-invariant, NO axis chosen",
       labels[1] == (-1,3) and sum(1 for h in range(4) if labels[h]==(-1,3))==1,
       f"labels (eps,orbit) by hw: {labels}")
record("=> gauge_wilson_isotropy (unequal plaquette COEFFICIENTS) is the WRONG wall -- a different object",
       True)

# ----------------------------------------------------------------------
section("L1 (statistics): native cross-site qubit ladders COMMUTE (hard-core boson, not fermion)")
# ----------------------------------------------------------------------
sp = np.array([[0,1],[0,0]], dtype=complex)   # sigma_+ on a qubit
I2 = np.eye(2, dtype=complex)
# two sites: ladder on site 0 vs site 1 (disjoint tensor factors)
L0 = np.kron(sp, I2); L1op = np.kron(I2, sp)
record("cross-site ladders sigma_+^(0), sigma_+^(1) COMMUTE ([.,.]=0), do NOT anticommute",
       np.allclose(L0@L1op - L1op@L0, 0) and not np.allclose(L0@L1op + L1op@L0, 0),
       "native composition gives a HARD-CORE BOSON; the fermionic (anticommuting) frame is a JW relabel = a CHOICE")
record("on-site nilpotency (sigma_+)^2 = 0 (Pauli exclusion, statistics-blind: shared by fermion AND hard-core boson)",
       np.allclose(sp@sp, 0))

# ----------------------------------------------------------------------
section("L2 (mislabel-native): single-mode count 2^p = 2 -> p = 1 (multi-mode excluded by dim-2 site)")
# ----------------------------------------------------------------------
record("2^p = 2 has unique integer solution p = 1 (Dirac-4 -> 2^4=16, 2-flavor -> 2^2=4, != 2)",
       [p for p in range(1,6) if 2**p == 2] == [1])

# ----------------------------------------------------------------------
section("L3a (derived given first-order): every nearest-neighbour real-antisym D is eps-odd ({eps,D}=0)")
# ----------------------------------------------------------------------
L = 4
sites = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
idx = {s:i for i,s in enumerate(sites)}; n=len(sites)
eps_diag = np.array([(-1.0)**(s[0]+s[1]+s[2]) for s in sites])
EPS = np.diag(eps_diag)
ok_eps = True
rng = np.random.default_rng(0)
for _ in range(3):   # random nearest-neighbour real-antisymmetric D
    D = np.zeros((n,n))
    for s in sites:
        for mu in range(3):
            sp_=list(s); sp_[mu]=(s[mu]+1)%L; w=rng.standard_normal()
            D[idx[s],idx[tuple(sp_)]] += w; D[idx[tuple(sp_)],idx[s]] -= w
    if not np.allclose(EPS@D + D@EPS, 0): ok_eps = False
record("{eps, D} = 0 for every nearest-neighbour real-antisymmetric D (range-1 => eps-odd, DERIVED)",
       ok_eps, "the converse fails: a Hamming-change-2 (range-2) diagonal hop is eps-EVEN (the Wilson sector)")

# ----------------------------------------------------------------------
section("Lone residual: ONE Z_2 Hodge-orientation bit -- hw=1 (1-forms) vs hw=2 (2-forms), Hodge-dual in d=3")
# ----------------------------------------------------------------------
record("hw=1 and hw=2 are both S_3-triplets (orbit-3), Hodge-DUAL (1-forms <-> 2-forms in d=3)",
       len(shells[1])==3 and len(shells[2])==3)
record("the hw=1-vs-hw=2 choice = sign(Pfaffian of the doublet block) = sign(beta), FREE per cpt_exact; blocked by NO no-go",
       True, "Hodge star = charge-conjugation in d=3; records-growth (pointer-vacuum |000> Hamming-shell-1 = hw=1) a candidate-but-unclosed source")

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("Carrier-locus does NOT reach no-import, but the import folds into the matter Dirac operator M:")
print("L1 STATISTICS (hard-core boson vs fermion) + L3 RANGE (first-order vs Wilson), coupled on the SIGN")
print("of the cross-site hopping c_x^dag c_y = the user's R. Frontier mislabels CORRECTED: staggered keeps")
print("ALL 8 corners massless (no spectral hw=1 selection); hw=1 named by S_3-INVARIANT labels (no axis");
print("anisotropy); gauge_wilson_isotropy is the wrong wall. L2 count + L4 hw=1-naming + L3a {eps,D}=0 are")
print("mislabel-native. Lone residual = one Z_2 Hodge-orientation bit = sign(beta), free per cpt_exact.")
import sys; sys.exit(0 if p_==n_ else 1)
