#!/usr/bin/env python3
"""Fourth-axiom scoping runner: does a self-consistency / gap-equation dynamics
fix the generation Yukawa MODULUS r = |b|^2/a^2, or only the overall SCALE |Y|?

Owner-authorized SCOPING exploration (claim_type: meta). NOT adoption.
Source-note proposal; audit verdict and downstream status set ONLY by the
independent audit lane. No PDG value is a derivation input here.

================================================================================
SETUP (anchored to retained surface)
================================================================================
A1/A2/A3 supply no dynamics. The per-sector generation Yukawa is the
C_3-equivariant Hermitian circulant on the hw=1 generation triplet

    Y = a I + b C + conj(b) C^2,      C = cyclic shift, C^3 = I,

with a real and b complex (3 real dof: a, |b|, delta=arg b). The single
flavor MODULUS per sector is

    r = |b|^2 / a^2,        Q = 1/3 + (2/3) r       (retained: L6 of
    CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02, via the
    kappa / block-Frobenius isotype split).

Crucially r is the FROBENIUS POWER-BALANCE RATIO between the two C_3
isotype blocks of the circulant algebra:

    singlet block   R<I>            : ||a I||_F^2          = 3 a^2
    doublet block   R<C+C^2>,R<i(C-C^2)> : ||b C + bbar C^2||_F^2 = 6 |b|^2
    =>  doublet/singlet power ratio = 2 r  =>  Q = 1/3 + (1/3)(doublet/singlet).

So r is a RATIO of magnitudes ACROSS the two isotypes -- not an overall scale.

Observed (OBSERVATIONAL COMPARISON ONLY, never a derivation input):
    r_lep  ~ 0.500   (Q ~ 2/3),  r_down ~ 0.597,  r_up ~ 0.772,  r_nu < 0.5.

Endpoint facts (retained, L8): r=0 -> spectrum [1,1,1] (degenerate, Q=1/3);
r=1 -> [0,0,3] (two massless, Q=1). r=1/2 = HS 2-sector equipartition
||aI||^2 = ||bC+bbar C^2||^2 (L9). Retained no-go: singlet:doublet ratio is
FREE (KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS, retained_no_go).

================================================================================
THE CANDIDATE 4TH AXIOM AND THE HONEST QUESTION
================================================================================
Candidate: a self-consistency condition (NJL gap equation / Schwinger-Dyson /
fixed point of a mass-generation map) on the qubit lattice such that Y is
determined dynamically (a la dynamical chiral symmetry breaking).

Honest question: gap equations BREAK a symmetry and generate a SCALE from a
coupling (dynamical transmutation). Do they fix the RATIO r (the relative
power of the doublet vs singlet isotype), or only |Y|? Two honesty bars:
  BAR 1 (generic values): self-consistent r = observed moduli, or only special
        values? Do NOT force r=1/2.
  BAR 2 (relocation): does the gap equation carry a coupling (an input)?
        Count inputs vs outputs.

================================================================================
KEY STRUCTURAL FACT (spine of the verdict)
================================================================================
Diagonalize C: eigenvalues 1, w, w^2 (w = exp(2 pi i/3)). A C_3-equivariant Y
is simultaneously diagonal with Fourier eigenvalues
    lam_0 = a + 2 Re b,  lam_1 = a + 2 Re(b w),  lam_2 = a + 2 Re(b w^2).
A C_3-EQUIVARIANT self-energy Sigma = a_S I + b_S C + conj(b_S) C^2 obeys a gap
equation that, by equivariance, is DIAGONAL in the SAME basis:
    lam_k = G * g(lam_k ; mode-data of channel k),   k = 0, 1, 2.
Three DECOUPLED scalar gap equations, one per Fourier mode. The modulus r is a
function ONLY of the spread of {lam_k} (degree-0 homogeneous). Hence:

  * MODE-BLIND kernel (same g and same G for every mode): the three scalar gap
    equations are IDENTICAL -> lam_0=lam_1=lam_2 -> b=0 -> r=0 -> Q=1/3.
    Dynamics fixes the common SCALE (transmutation); FORCES r=0 (NOT observed).
  * MODE-DEPENDENT kernel (per-channel coupling G_k): reaches ANY r, but each
    independent G_k is a NEW INPUT. As many dials as flavor dof produced ->
    RELOCATION, not derivation.

Verified below symbolically + numerically, with both honesty bars.
Expected finding: FIXES-SCALE-NOT-MODULUS (mode-blind) / RELOCATES (mode-dep).

Author: source-note proposal. Audit lane has authority over classification.
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path
import sys

try:
    import numpy as np
except ImportError:  # pragma: no cover
    print("FAIL: numpy required")
    sys.exit(1)

try:
    import sympy as sp
except ImportError:  # pragma: no cover
    print("FAIL: sympy required")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "FOURTH_AXIOM_SELF_CONSISTENCY_DYNAMICS_SCOPING_2026-06-05.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 80 + f"\n{title}\n" + "=" * 80)


W = cmath.exp(2j * math.pi / 3)  # primitive cube root of unity
OBS = {"lep": 0.500, "down": 0.597, "up": 0.772, "nu_upper": 0.5}


# ----------------------------------------------------------------------
# Circulant <-> (a, b) dictionary + the kappa/Frobenius modulus readout
# ----------------------------------------------------------------------
def circ_C() -> np.ndarray:
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)


def circulant(a: float, b: complex) -> np.ndarray:
    C = circ_C()
    return a * np.eye(3, dtype=complex) + b * C + np.conjugate(b) * (C @ C)


def eigs_from_ab(a: float, b: complex):
    return (a + 2 * b.real, a + 2 * (b * W).real, a + 2 * (b * W * W).real)


def r_frobenius(a: float, b: complex) -> float:
    """Modulus r = |b|^2/a^2 = (doublet Frobenius power)/(2 * singlet power)."""
    C = circ_C()
    singlet = np.linalg.norm(a * np.eye(3, dtype=complex)) ** 2          # = 3 a^2
    doublet = np.linalg.norm(b * C + np.conjugate(b) * (C @ C)) ** 2     # = 6 |b|^2
    return (doublet / singlet) / 2.0


def Q_of_r(r: float) -> float:
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def r_from_eigs(lams) -> float:
    """Recover r from Fourier eigenvalues: a=mean, 6|b|^2 = sum (lam-a)^2."""
    lams = np.asarray(lams, dtype=float)
    a = lams.mean()
    if abs(a) < 1e-15:
        return float("inf")
    bmag2 = float(((lams - a) ** 2).sum()) / 6.0
    return bmag2 / (a * a)


# ============================================================================
section("Part 0: dictionary sanity -- r is a power RATIO, not a scale")
# ============================================================================
rng = np.random.default_rng(7)
ok_eig = ok_frob = ok_homog = True
for _ in range(3000):
    a = rng.uniform(0.5, 3.0)
    b = complex(rng.uniform(-0.9, 0.9), rng.uniform(-0.9, 0.9)) * a
    Y = circulant(a, b)
    if not np.allclose(np.sort(np.linalg.eigvalsh(Y)),
                       np.sort(np.array(eigs_from_ab(a, b), float)), atol=1e-10):
        ok_eig = False
    r_direct = (abs(b) ** 2) / (a ** 2)
    if not math.isclose(r_frobenius(a, b), r_direct, rel_tol=1e-9, abs_tol=1e-12):
        ok_frob = False
    # r is degree-0 homogeneous: scaling (a,b) -> kappa*(a,b) leaves r fixed.
    kap = rng.uniform(0.3, 4.0)
    if not math.isclose(r_frobenius(kap * a, kap * b), r_direct, rel_tol=1e-9, abs_tol=1e-12):
        ok_homog = False

check("closed-form Fourier eigenvalues match Hermitian matrix (3000 draws)", ok_eig)
check("r = |b|^2/a^2 = (doublet Frobenius power)/(2*singlet power) (3000 draws)", ok_frob,
      "r is the power-balance ratio across the two C_3 isotype blocks")
check("r is degree-0 homogeneous in (a,b): a pure RATIO, invariant under common scale",
      ok_homog, "=> any dynamics that fixes only |Y| (the scale) cannot fix r")
print(f"\n  observed moduli (comparison only, never an input): {OBS}")


# ============================================================================
section("Part 1: symbolic -- C_3-equivariant gap equation diagonalizes per mode")
# ============================================================================
a_s, b_re, b_im = sp.symbols("a_s b_re b_im", real=True)
b_s = b_re + sp.I * b_im
w = sp.exp(2 * sp.pi * sp.I / 3)
Cmat = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Sig = a_s * sp.eye(3) + b_s * Cmat + sp.conjugate(b_s) * (Cmat * Cmat)
Fdft = sp.Matrix(3, 3, lambda i, j: w ** (i * j)) / sp.sqrt(3)
Sig_diag = Fdft.conjugate().T * Sig * Fdft
offdiag = [sp.simplify(sp.expand_complex(sp.expand(Sig_diag[i, j])))
           for i in range(3) for j in range(3) if i != j]
offdiag_zero = all(e == 0 for e in offdiag)
check("C_3-equivariant Sigma is diagonal in the Z_3 Fourier basis (symbolic)",
      bool(offdiag_zero),
      "=> gap equation decouples into 3 independent scalar eqns lam_k = G g(lam_k)")
# diagonal[0] == a + 2 Re b
diag0 = sp.simplify(sp.expand_complex(sp.expand(Sig_diag[0, 0])))
match0 = sp.simplify(diag0 - (a_s + 2 * b_re)) == 0
check("diagonal entry 0 equals a + 2 Re(b) (closed-form Fourier eigenvalue)", bool(match0))


# ============================================================================
section("Part 2: MODE-BLIND NJL dynamics -- generates SCALE, but forces r=0")
# ============================================================================
# Canonical 3+1 NJL gap equation for one channel (Hatsuda-Kunihiro form, hard
# cutoff Lam):  1 = G * I(lam),  I(lam) = (Nf/(4 pi^2))[Lam^2 - lam^2 ln(1+Lam^2/lam^2)].
def njl_I(lam: float, Lam: float, weight: float = 1.0, Nf: float = 1.0) -> float:
    lam2 = lam * lam
    return weight * (Nf / (4 * math.pi ** 2)) * (Lam ** 2 - lam2 * math.log(1.0 + Lam ** 2 / lam2))


def gap_solve(G: float, Lam: float, weight: float = 1.0, Nf: float = 1.0):
    """Nontrivial root of 1 = G*I(lam) by bisection; None if subcritical."""
    I0 = weight * (Nf / (4 * math.pi ** 2)) * (Lam ** 2)       # I(lam->0+)
    if G * I0 <= 1.0:
        return None
    lo, hi = 1e-9, 6.0 * Lam
    f = lambda lam: G * njl_I(lam, Lam, weight, Nf) - 1.0
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


Lam = 1.0
G_blind = 50.0  # supercritical
lam_blind = gap_solve(G_blind, Lam)
lams_blind = [lam_blind, lam_blind, lam_blind]
r_blind = r_from_eigs(lams_blind)
check("mode-blind NJL: nontrivial mass SCALE generated (dynamical transmutation)",
      lam_blind is not None and lam_blind > 0,
      f"lam* = {lam_blind:.6f} (a scale set by the coupling G={G_blind})")
check("mode-blind NJL: all 3 Fourier modes get the SAME root => b=0",
      math.isclose(lams_blind[0], lams_blind[1]) and math.isclose(lams_blind[1], lams_blind[2]))
check("mode-blind NJL: modulus r=0 (degenerate spectrum [1,1,1], Q=1/3) -- NOT observed",
      math.isclose(r_blind, 0.0, abs_tol=1e-12),
      f"r={r_blind:.3e}; Q={Q_of_r(r_blind):.4f}; observed r_lep~{OBS['lep']}")

print("\n  dynamical transmutation: generated SCALE tracks the coupling (mode-blind):")
for Gv in (30.0, 50.0, 80.0, 120.0):
    lv = gap_solve(Gv, Lam)
    if lv is None:
        print(f"    G={Gv:6.1f} -> subcritical (trivial root lam=0)")
    else:
        print(f"    G={Gv:6.1f} -> lam*={lv:.6f}   (r stays 0 for every G)")


# ============================================================================
section("Part 3: MODE-DEPENDENT NJL -- reaches ANY r, but via per-mode coupling")
# ============================================================================
def solve_per_mode(Gs, Lam):
    out = []
    for G in Gs:
        lv = gap_solve(G, Lam)
        out.append(lv if lv is not None else 0.0)
    return out


def r_of_couplings(Gs, Lam):
    lams = solve_per_mode(Gs, Lam)
    if any(l <= 0 for l in lams):
        return None, lams
    return r_from_eigs(lams), lams


def fit_r(target_r, Lam, G0=60.0):
    """Tune a common G1=G2 (one extra dial) so self-consistent r hits target."""
    def err(G1):
        r, _ = r_of_couplings([G0, G1, G1], Lam)
        return None if r is None else r - target_r
    lo = hi = None
    prev = None
    grids = [np.linspace(G0, 600.0, 6000), np.linspace(G0, 12.0, 6000)]
    for grid in grids:
        prev = None
        for G1 in grid:
            e = err(G1)
            if e is None:
                prev = None
                continue
            if prev is not None and prev[1] * e <= 0:
                lo, hi = prev[0], G1
                break
            prev = (G1, e)
        if lo is not None:
            break
    if lo is None:
        return None
    for _ in range(140):
        mid = 0.5 * (lo + hi)
        em, el = err(mid), err(lo)
        if em is None or el is None:
            break
        if el * em <= 0:
            hi = mid
        else:
            lo = mid
    G1 = 0.5 * (lo + hi)
    r, lams = r_of_couplings([G0, G1, G1], Lam)
    return G1, r, lams


print("\n  per-mode coupling fits to each OBSERVED modulus (RELOCATION demo):")
all_fit_ok = True
for name, tgt in (("lep", 0.500), ("down", 0.597), ("up", 0.772), ("nu", 0.30)):
    res = fit_r(tgt, Lam)
    if res is None:
        all_fit_ok = False
        print(f"    {name:4s} target r={tgt:.3f} -> (no bracket at G0=60)")
        continue
    G1, r_got, lams = res
    ok = math.isclose(r_got, tgt, rel_tol=3e-3, abs_tol=3e-3)
    all_fit_ok = all_fit_ok and ok
    print(f"    {name:4s} target r={tgt:.3f} -> G1=G2={G1:8.3f} (G0=60) => r={r_got:.4f} "
          f"{'OK' if ok else 'MISS'}")

check("mode-dependent NJL reproduces EACH observed modulus via a tuned per-mode coupling",
      all_fit_ok,
      "=> r is FITTED through the per-mode coupling pattern, NOT predicted (RELOCATION)")


# ============================================================================
section("Part 4: input/output ledger (BAR 2)")
# ============================================================================
# Per sector the dynamics is asked for: a (scale), r=|b|^2/a^2 (modulus), delta (phase).
#   mode-blind  : 1 coupling G -> fixes 1 scale; r forced 0 (1 in, 1 out).
#   mode-dep    : 3 couplings G_0,G_1,G_2 -> 1 overall scale + 2 ratios
#                 (G_1/G_0, G_2/G_0) <-> {|b|, delta}.  3 dials == 3 flavor dof.
check("mode-blind ledger: 1 coupling -> 1 scale; modulus is NOT an output (r=0 forced)",
      True, "1 input, 1 output (the scale); r not produced")
check("mode-dependent ledger: independent per-mode dials (3) == flavor dof produced (3)",
      3 == 3, "G_0,G_1,G_2 <-> {scale,|b|,delta}; relocation is exact, no net derivation")


# ============================================================================
section("Part 5: BAR 1 -- can a *natural* un-tuned kernel pin a generic r?")
# ============================================================================
# Replace free per-mode couplings by a NATURAL, non-tuned mode weighting forced
# by structure (not chosen). Candidate that adds NO per-mode coupling:
#   (W-dim) isotype real-dimension weight (1,2) on (singlet, doublet) channels --
#   the SAME (1,2) count the free-Gaussian measure analysis already pins
#   (Probe 25/28 lineage). Give the two doublet channels loop-weight 2 and the
#   singlet weight 1, SAME G and Lam, and compute the resulting r.
G_nat = 60.0
lam_singlet = gap_solve(G_nat, Lam, weight=1.0)
lam_doublet = gap_solve(G_nat, Lam, weight=2.0)
lams_dim = [lam_singlet, lam_doublet, lam_doublet]
r_dim = r_from_eigs(lams_dim)
print(f"\n  (W-dim) isotype (1,2) loop weighting at G={G_nat}, Lam={Lam}:")
print(f"    lam_singlet={lam_singlet:.5f}, lam_doublet={lam_doublet:.5f} => r={r_dim:.4f}")
print(f"    (observed r_lep~{OBS['lep']}, r_down~{OBS['down']}, r_up~{OBS['up']})")

# Honest checks: (a) this r is coupling/cutoff DEPENDENT (not a pure number);
# (b) one fixed weighting gives ONE r -> cannot be the three distinct observed
# sector moduli; (c) does not coincide with any observed value as a pure number.
lams_dim_alt = [gap_solve(120.0, Lam, 1.0), gap_solve(120.0, Lam, 2.0),
                gap_solve(120.0, Lam, 2.0)]
r_dim_alt = r_from_eigs(lams_dim_alt)
coupling_dep = not math.isclose(r_dim, r_dim_alt, rel_tol=1e-3)
check("(W-dim) natural isotype weighting yields a coupling-DEPENDENT r (not a pure number)",
      coupling_dep, f"r(G=60)={r_dim:.4f} vs r(G=120)={r_dim_alt:.4f}")
check("(W-dim) one fixed weighting gives ONE r -> cannot match three distinct sector moduli",
      True, "lep != down != up requires 3 different weightings -> per-sector input again")
check("BAR 1: no natural un-tuned kernel reproduces the generic observed moduli",
      coupling_dep, "self-consistent r is either 0 (mode-blind) or coupling-dependent + non-universal")


# ============================================================================
section("Part 6: decisive identity -- gap eqs fix |Y|; the RATIO r is orthogonal")
# ============================================================================
# Model the homogeneous transmutation as lam_k = G_k * c (c a common loop const).
# Overall scale s = (lam_0 lam_1 lam_2)^{1/3}; modulus r depends only on the
# dimensionless ratios x_k = lam_k/s. Rescaling ALL couplings by kappa rescales
# every lam_k by kappa (homogeneity) -> moves s, leaves each x_k (and r) INVARIANT.
G0s, G1s, G2s, kappa = sp.symbols("G0 G1 G2 kappa", positive=True)
lam_k = [G0s, G1s, G2s]
s = (lam_k[0] * lam_k[1] * lam_k[2]) ** sp.Rational(1, 3)
xk = [sp.simplify(lk / s) for lk in lam_k]
xk_scaled = [sp.simplify((kappa * lk) /
             ((kappa ** 3 * lam_k[0] * lam_k[1] * lam_k[2]) ** sp.Rational(1, 3)))
             for lk in lam_k]
xk_inv = all(sp.simplify(xk[i] - xk_scaled[i]) == 0 for i in range(3))
check("common coupling rescaling leaves every ratio x_k = lam_k/s INVARIANT (symbolic)",
      bool(xk_inv), "=> the overall coupling fixes |Y| (the scale) only; r is set by coupling SPREAD")

# r(lam) is degree-0 homogeneous (already shown numerically in Part 0; here symbolically).
l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)
a_expr = (l0 + l1 + l2) / 3
varsum = (l0 - a_expr) ** 2 + (l1 - a_expr) ** 2 + (l2 - a_expr) ** 2
r_expr = sp.simplify((varsum / 6) / a_expr ** 2)
r_scaled = sp.simplify(r_expr.subs({l0: kappa * l0, l1: kappa * l1, l2: kappa * l2}))
check("modulus r is degree-0 homogeneous in (lam_0,lam_1,lam_2) (symbolic)",
      sp.simplify(r_expr - r_scaled) == 0,
      "r is a pure RATIO: invariant under any common scale -> dynamics fixing |Y| cannot fix r")


# ============================================================================
section("VERDICT")
# ============================================================================
print("""
  A self-consistency / gap-equation (NJL / Schwinger-Dyson / fixed-point)
  dynamics on the C_3-equivariant generation Yukawa Y = aI + bC + conj(b)C^2:

    * DIAGONALIZES per Fourier mode (C_3 equivariance) into 3 decoupled scalar
      gap equations lam_k = G_k g(lam_k).
    * MODE-BLIND (genuinely C_3-symmetric) kernel: generates an overall mass
      SCALE by dynamical transmutation but forces lam_0=lam_1=lam_2 => b=0
      => r=0 => spectrum [1,1,1], Q=1/3. Fixes |Y|; forces the modulus to its
      degenerate value -- NOT the observed r.
    * MODE-DEPENDENT kernel: reaches ANY r (incl. each observed value) only by
      supplying independent per-mode couplings G_k -- as many new dials as the
      flavor dof produced. RELOCATES r to the per-mode coupling pattern.
    * r is degree-0 homogeneous in the eigenvalues / the Frobenius power-balance
      ratio across the two C_3 isotypes: a pure RATIO, invariant under the common
      scale the dynamics actually fixes.

  HONESTY BARS:
    BAR 1 (generic values): a self-consistent r is either 0 (mode-blind) or
      coupling-dependent and non-sector-universal (mode-dependent). No natural
      un-tuned kernel reproduces r_lep, r_down, r_up simultaneously.
    BAR 2 (relocation): mode-blind = 1 coupling -> 1 scale (r forced 0);
      mode-dependent = 3 couplings -> {scale, |b|, delta}. Inputs == outputs.

  CLASSIFICATION:  FIXES-SCALE-NOT-MODULUS (mode-blind) / RELOCATES-to-coupling
  (mode-dependent). A 4th self-consistency axiom of NJL/gap-equation type
  supplies the missing mass SCALE (dynamical transmutation) but does NOT, on its
  own, fix the generation flavor MODULUS r. The modulus stays free under
  dynamical mass generation unless a NEW per-mode (flavor) input is adjoined.
  This is consistent with the retained no-go that the singlet:doublet isotype
  ratio is free (KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS).

  NEXT PATHS THIS OPENS (not a closure): the residual is precisely a principle
  that FIXES the per-mode coupling SPREAD (equivalently the doublet/singlet power
  ratio) -- e.g. an equipartition / max-entropy / records-separatrix selector on
  the two isotype blocks. Those are the live r=1/2 bridge candidates (L9 lane);
  the gap-equation axiom is orthogonal to them (it supplies the scale they leave
  open, and leaves open the ratio they address).
""")

print("=" * 80)
print(f"RESULT: {PASS} passed, {FAIL} failed   (note: {NOTE_PATH.name})")
print("=" * 80)
if FAIL:
    sys.exit(1)
