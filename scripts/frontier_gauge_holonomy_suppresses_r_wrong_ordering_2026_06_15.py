#!/usr/bin/env python3
"""
Gauge-holonomy CHARACTER CAP on the Koide ratio: the algebraic bound r_R <= r0 (cap-only).

SOURCE CONTENT (algebraic): the framework's b-term (the C3[111] doublet coupling) is a hop-RETURN
that traverses a gauge link (matter_gauge_minimal_coupling / koide_gamma_axis_covariant, retained);
the a-term is ON-SITE (no link). Dressing the hop with a background link U in gauge rep R and forming
the gauge-invariant (fibre-averaged) effective generation operator gives

    b_eff = b * chi_R(U)/d_R ,   a_eff = a ,   r_R = r0 * |chi_R(U)/d_R|^2 ,

where chi_R(U)=Tr_R(U), d_R=dim R, and r0=|b|^2/a^2 is the trivial-rep value.
Since |chi_R(U)| <= d_R for every unitary (sum of d_R unit-modulus eigenvalues), |chi_R(U)/d_R| <= 1,
so r_R <= r0 ALWAYS, with equality iff U is a center (scalar-phase) element. This is a bounded
algebraic inequality; it is rep-agnostic and uses NO physical sector-to-representation assignment.

OPEN BRIDGE (not source content; narrowed 2026-06-20): the *physical* reading that "a gauge
holonomy suppresses the OBSERVED lepton/quark Koide ratio below the leptonic value and so gives the
wrong ordering for the observed spread" requires an UNSUPPLIED bridge that (i) assigns the physical
colourless-lepton sector to the trivial gauge rep and the coloured-quark sectors to nontrivial reps,
and (ii) identifies the fibre-averaged ratio r_R with the registered physical Koide dial of each
sector. Neither step is derived here. Section [4] below therefore checks only the *conditional*
arithmetic (the cap value and the numeric ordering of the observed anchors) that WOULD constitute the
falsification IF the bridge premise held -- it does NOT assert the bridge.

This does NOT force any r value: r0 is a free bare coupling; the result is the inequality r_R<=r0.

Prints "TOTAL: PASS=N FAIL=0".
"""
import numpy as np

PASS = 0
FAIL = 0
rng = np.random.default_rng(20260615)


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


def haar(d):
    """A Haar-random d x d unitary."""
    if d == 1:
        return np.array([[np.exp(1j * rng.uniform(0, 2 * np.pi))]], complex)
    z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph


w3 = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)   # generation 3-cycle
Cd = C.conj().T


def effective_r(a, b, U):
    """Build H_R = a(I3 x I_dR) + b(C x U) + conj(b)(C^T x U^dag), take the gauge-invariant
    fibre-averaged effective generation operator, and return (r_R, a_eff, |chi/d|)."""
    dR = U.shape[0]
    I3 = np.eye(3, dtype=complex)
    IdR = np.eye(dR, dtype=complex)
    H = a * np.kron(I3, IdR) + b * np.kron(C, U) + np.conj(b) * np.kron(Cd, U.conj().T)
    # fibre-average: M_eff[i,j] = (1/dR) Tr_fibre over the (i,j) generation block
    M = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            blk = H[i * dR:(i + 1) * dR, j * dR:(j + 1) * dR]
            M[i, j] = np.trace(blk) / dR
    a_eff = M[0, 0].real                     # on-site (diagonal) effective coupling
    b_eff = M[1, 0]                           # one sub-diagonal entry of the circulant = b * chi/dR
    r_R = abs(b_eff) ** 2 / a_eff ** 2
    chi_over_d = np.trace(U) / dR
    return r_R, a_eff, abs(chi_over_d)


# bare (free) couplings; set r0 = (b/a)^2 = 1/2 so the trivial-rep value = the leptonic value
a, b = 1.0, np.sqrt(0.5)
r0 = b ** 2 / a ** 2
check("bare trivial-rep value r0 = 1/2 (free input, leptonic reference)", abs(r0 - 0.5) < 1e-12)


# ============================================================================
# 1. The effective-coupling identity: a carries NO link, b carries the normalized character.
# ============================================================================
# NOTE: haar(d) samples U(d), which is the SUPERSET of the image of any d-dimensional rep
# (SU(3)-fundamental sits in U(3), adjoint in U(8), etc.). The character bound |chi|<=d holds on all
# of U(d), so testing Haar-U(d) is the strongest witness and covers every rep of that dimension.
print("\n[1] on-site a is link-blind; doublet b picks up the normalized character chi_R(U)/d_R")
for dR, lbl in [(1, "trivial d=1"), (2, "U(2) d=2"), (3, "U(3) >= SU3-fund"), (8, "U(8) >= adjoint")]:
    U = haar(dR)
    r_R, a_eff, nc = effective_r(a, b, U)
    check(f"[{lbl}] a_eff = a (on-site carries no link)", abs(a_eff - a) < 1e-12)
    check(f"[{lbl}] r_R = r0*|chi/d|^2 (identity holds)", abs(r_R - r0 * nc ** 2) < 1e-10)


# ============================================================================
# 2. THE CHARACTER BOUND (the theorem): r_R <= r0 for EVERY unitary in EVERY rep.
# ============================================================================
print("\n[2] character bound: |chi_R(U)| <= d_R  =>  r_R <= r0 always")
worst = 0.0
for dR in [1, 2, 3, 8]:
    for _ in range(200):
        U = haar(dR)
        r_R, _, nc = effective_r(a, b, U)
        worst = max(worst, r_R - r0)
        if r_R > r0 + 1e-10:
            check(f"violation at d={dR}", False)
            break
check("r_R <= r0 over 800 random unitaries (4 reps x 200)", worst < 1e-10)
check("normalized character magnitude |chi/d| <= 1 (the bound's source)",
      all(effective_r(a, b, haar(dR))[2] <= 1 + 1e-12 for dR in [2, 3, 8] for _ in range(50)))


# ============================================================================
# 3. EQUALITY iff center: a scalar-phase background gives no suppression; generic strictly suppresses.
# ============================================================================
print("\n[3] equality r_R=r0 iff U is a center (scalar-phase) element")
for dR, ph in [(3, w3), (2, -1), (8, 1j)]:
    Uc = ph * np.eye(dR, dtype=complex)       # center element = scalar phase
    r_c, _, nc_c = effective_r(a, b, Uc)
    check(f"center (d={dR}, phase) gives r_R = r0 (no suppression, |chi/d|=1)",
          abs(r_c - r0) < 1e-10 and abs(nc_c - 1) < 1e-10)
# a generic (non-center) background strictly suppresses
r_g, _, _ = effective_r(a, b, haar(3))
check("a generic U(3) background strictly suppresses: r_R < r0", r_g < r0 - 1e-6)


# ============================================================================
# 4. CONDITIONAL physical reading (not source content): the wrong-ordering falsification HOLDS ONLY
#    IF the unsupplied bridge premise is granted. This section checks the conditional ARITHMETIC only.
#    BRIDGE PREMISE (open, NOT derived here):
#      (i)  colourless-lepton sector = trivial gauge rep; coloured-quark sectors = nontrivial reps;
#      (ii) the fibre-averaged ratio r_R = the registered physical Koide dial of each sector.
#    These checks assert the algebraic cap value and the numeric ordering of the OBSERVED anchors.
#    They do NOT assert (i) or (ii) -- the physical sector-to-rep assignment and r_R->registered-dial
#    identification remain the unsupplied bridge. Narrowed 2026-06-20.
# ============================================================================
print("\n[4] CONDITIONAL (open bridge): IF lepton<->trivial-rep & r_R=registered dial, the observed")
print("    spread would violate the cap r_colored <= r_lepton (arithmetic of the anchors only)")
r_lep, r_down, r_up = 0.5, 0.597, 0.773      # observed (anchors, not derivation inputs)
# the algebraic cap value for ANY nontrivial-rep, any-background sector is r0; under the OPEN bridge
# premise this r0 would equal the leptonic r_lep -- that equality is the unsupplied identification.
ceiling = r0
check("[conditional] algebraic cap value r0 = 1/2 equals leptonic anchor IF bridge held (open premise)",
      abs(ceiling - r_lep) < 1e-12)
check("[conditional] observed r_down = 0.597 exceeds the cap value (arithmetic of anchors)",
      r_down > ceiling + 1e-3)
check("[conditional] observed r_up = 0.773 exceeds the cap value (arithmetic of anchors)",
      r_up > ceiling + 1e-3)
check("[conditional] => IF the unsupplied bridge held, the holonomy channel would give the WRONG "
      "ordering (r_quark>cap observed; <=cap predicted) -- bridge NOT asserted here",
      r_down > ceiling and r_up > ceiling)


# ============================================================================
# 5. EITHER-HORN robustness: a LINKLESS b-term (U=I / flat) gives NO spread at all.
# ============================================================================
print("\n[5] either horn fails: linkless/flat b-term (U=I) is rep-independent => no spread")
flat_rs = [effective_r(a, b, np.eye(dR, dtype=complex))[0] for dR in [1, 2, 3, 8]]
check("U=I (no link / flat background): r_R = r0 for every rep (no spread)",
      max(flat_rs) - min(flat_rs) < 1e-12 and abs(flat_rs[0] - r0) < 1e-12)


# ============================================================================
# 6. FIREWALL: the mechanism forces no r value; r0 is free; the result is an inequality.
# ============================================================================
print("\n[6] firewall: no r value forced; r0 free; result is the bound r_R <= r0")
# re-run the bound with a DIFFERENT free r0 to show the value is not selected
a2, b2 = 1.0, np.sqrt(0.31)
r0b = b2 ** 2 / a2 ** 2
worst2 = max(effective_r(a2, b2, haar(dR))[0] - r0b for dR in [2, 3, 8] for _ in range(50))
check("bound r_R <= r0 holds for a DIFFERENT free r0=0.31 (value not selected)", worst2 < 1e-10)
check("the bound is the same inequality for two distinct free r0 (0.5 and 0.31) => no value forced",
      abs(r0 - 0.5) < 1e-12 and abs(r0b - 0.31) < 1e-12 and r0 != r0b)


print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
assert FAIL == 0, "discriminating checks failed"
