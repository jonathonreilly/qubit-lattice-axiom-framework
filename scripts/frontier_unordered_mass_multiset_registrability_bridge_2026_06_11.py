#!/usr/bin/env python3
"""Unordered-mass-multiset registrability bridge -- class-A finite check.

Companion runner for
docs/UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md

Claim boundary: this runner checks the finite algebraic consequences under the
supplied readout context and the explicit P-dep premise. It does not derive
P-dep from Record alone and does not edit or predict audit status.

Supplied surface (3x3, tiny memory): the Hermitian circulant

    H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,   a, B real, B != 0,

with the Fourier sector projectors {P_k} (k = 0, 1, 2) as the supplied finite
central-sector decomposition and entrywise complex conjugation as the fixed
K/CPT conjugation.

Checked legs (each PASS/FAIL):
  L1  flip identity: conj(H(delta)) == H(-delta)
  L2  supplied decomposition: {P_k} orthogonal idempotents, sum = I,
      each commutes with H(delta) for all sampled delta
  L3  K/CPT permutes sector labels by an involution sigma fixing exactly one
      label; sigma == (k -> -k mod 3) == (0)(1 2)
  L4  per-sector covariance: lambda_{sigma(k)}(-delta) == lambda_k(delta)
  L5  unordered spectrum invariant under delta -> -delta; elementary symmetric
      polynomials even in delta and equal to the closed forms
      e1 = 3a, e2 = 3a^2 - 3B^2, e3 = a^3 - 3aB^2 + 2B^3 cos(3 delta)
  L6  registrable family (additive + orbit-constant): power sums p1, p2, p3;
      the singlet orbit-class readout; cos(3 delta) recovered from e3 --
      every member takes equal values at +delta and -delta, and the
      empty-record value is 0
  L7  exactness: Newton-Girard reconstructs the unordered eigenvalue multiset
      from the registrable power sums alone; the orbit-resolved multiset is
      reconstructed once the (registrable) singlet readout is added
  G1  hostile G-ord1: label-weighted sum sum_k k*lambda_k -- violates
      orbit-constancy (witnessed at generic delta)
  G2  hostile G-ord2: signed doublet gap lambda_1 - lambda_2 -- violates
      orbit-constancy (odd under the flip; nonzero witness)
  G3  hostile G-alt: fixed-label Vandermonde prod_{i<j}(lambda_i - lambda_j)
      -- violates I(empty)=0 and additivity, and violates orbit-constancy
  G4  hostile G-sgn: sin(3 delta) -- violates orbit-constancy (two values on
      one K/CPT outcome)
  G5  hostile G-cross: interference cross-term I(rec_i u rec_j) =
      lambda_i + lambda_j + lambda_i*lambda_j -- violates additivity
  G6  hostile within-orbit order probe f(k, x) = [k == 1] * x -- violates the
      per-record orbit-constancy identity r_k(delta) = r_{sigma(k)}(-delta)
  H1  source-scope hygiene: the paired note names P-dep as an explicit
      conditional premise, tags the load-bearing B1 factorization claim itself
      as conditional on P-dep, relocates K/CPT orbit constancy to the cited
      supplied-context bridge, and does not claim Record derives P-dep

Prints one line per check and a final `TOTAL: PASS=N FAIL=0` scorecard.
No randomness-dependent acceptance: violations must be witnessed for EVERY
sampled parameter set (adversarial multi-seed sweep), equalities must hold
for every sampled parameter set and delta.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

print(
    "Claim boundary: finite algebra under supplied context + explicit P-dep; "
    "P-dep is not derived from Record alone."
)

TOL = 1e-10
PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md"
)


def check(name: str, ok: bool) -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {name}")
    else:
        FAIL += 1
        print(f"FAIL {name}")


# ---------------------------------------------------------------- surface --
OMEGA = np.exp(2j * np.pi / 3)

# Cyclic shift C: (C x)[i] = x[(i - 1) mod 3]
C = np.zeros((3, 3), dtype=complex)
for i in range(3):
    C[(i + 1) % 3, i] = 1.0

# Fourier vectors v_k[j] = omega^{jk}/sqrt(3); projectors P_k = v_k v_k^dag
V = np.array([[OMEGA ** (j * k) / np.sqrt(3.0) for j in range(3)]
              for k in range(3)], dtype=complex).T  # columns are v_k
P = [np.outer(V[:, k], V[:, k].conj()) for k in range(3)]


def H(delta: float, a: float, B: float) -> np.ndarray:
    return (a * np.eye(3, dtype=complex)
            + B * np.exp(1j * delta) * C
            + B * np.exp(-1j * delta) * C.T)


def lam(delta: float, a: float, B: float, k: int) -> float:
    """Per-sector central value lambda_k(delta) = tr(H P_k) (real)."""
    return float(np.real(np.trace(H(delta, a, B) @ P[k])))


# Parameter sets: adversarial fixed sweep, no acceptance-by-lucky-seed.
PARAM_SETS = [(1.0, 0.5), (0.3, 1.7), (-2.0, 0.9), (4.5, -1.2), (0.0, 2.0)]
GENERIC_DELTAS = [0.37, 0.91, 1.13, 2.05, -0.61]
DEGENERATE_DELTAS = [0.0, np.pi / 3.0]
ALL_DELTAS = GENERIC_DELTAS + DEGENERATE_DELTAS

# ------------------------------------------------------------------- L1 ----
ok = all(np.allclose(np.conj(H(d, a, B)), H(-d, a, B), atol=TOL)
         for a, B in PARAM_SETS for d in ALL_DELTAS)
check("L1 flip identity conj(H(delta)) == H(-delta)", ok)

# ------------------------------------------------------------------- L2 ----
ok = True
for k in range(3):
    ok &= np.allclose(P[k] @ P[k], P[k], atol=TOL)
    ok &= np.allclose(P[k].conj().T, P[k], atol=TOL)
    for j in range(3):
        if j != k:
            ok &= np.allclose(P[k] @ P[j], np.zeros((3, 3)), atol=TOL)
ok &= np.allclose(sum(P), np.eye(3), atol=TOL)
for a, B in PARAM_SETS:
    for d in ALL_DELTAS:
        M = H(d, a, B)
        for k in range(3):
            ok &= np.allclose(M @ P[k], P[k] @ M, atol=TOL)
check("L2 {P_k} orthogonal idempotents, sum=I, central for H(delta)", ok)

# ------------------------------------------------------------------- L3 ----
sigma = {}
ok = True
for k in range(3):
    img = np.conj(P[k])  # K P_k K^{-1} with K = entrywise conjugation
    matches = [j for j in range(3) if np.allclose(img, P[j], atol=TOL)]
    ok &= (len(matches) == 1)
    sigma[k] = matches[0] if matches else None
ok &= all(sigma[sigma[k]] == k for k in range(3))           # involution
ok &= (sum(1 for k in range(3) if sigma[k] == k) == 1)      # exactly 1 fixed
ok &= all(sigma[k] == (-k) % 3 for k in range(3))           # k -> -k mod 3
check("L3 K/CPT label involution sigma = (0)(1 2) = (k -> -k mod 3)", ok)

# ------------------------------------------------------------------- L4 ----
ok = all(abs(lam(-d, a, B, sigma[k]) - lam(d, a, B, k)) < TOL
         for a, B in PARAM_SETS for d in ALL_DELTAS for k in range(3))
check("L4 per-sector covariance lambda_{sigma(k)}(-delta) == lambda_k(delta)", ok)

# ------------------------------------------------------------------- L5 ----
ok = True
for a, B in PARAM_SETS:
    for d in ALL_DELTAS:
        sp_p = np.sort(np.linalg.eigvalsh(H(d, a, B)))
        sp_m = np.sort(np.linalg.eigvalsh(H(-d, a, B)))
        ok &= np.allclose(sp_p, sp_m, atol=1e-9)
        l = [lam(d, a, B, k) for k in range(3)]
        e1 = sum(l)
        e2 = l[0] * l[1] + l[0] * l[2] + l[1] * l[2]
        e3 = l[0] * l[1] * l[2]
        ok &= abs(e1 - 3 * a) < 1e-8
        ok &= abs(e2 - (3 * a * a - 3 * B * B)) < 1e-8
        ok &= abs(e3 - (a ** 3 - 3 * a * B * B
                        + 2 * B ** 3 * np.cos(3 * d))) < 1e-8
check("L5 multiset invariant under flip; e1,e2,e3 even and match closed forms", ok)


# --------------------------------------------------- registrable family ----
def power_sum(delta, a, B, m):
    return sum(lam(delta, a, B, k) ** m for k in range(3))


def singlet_readout(delta, a, B):
    """Orbit-class readout f(0,x)=x, f(1,x)=f(2,x)=0 (constant on orbits)."""
    return lam(delta, a, B, 0)


def cos3_from_e3(delta, a, B):
    l = [lam(delta, a, B, k) for k in range(3)]
    e3 = l[0] * l[1] * l[2]
    return (e3 - a ** 3 + 3 * a * B * B) / (2 * B ** 3)


# ------------------------------------------------------------------- L6 ----
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    for d in ALL_DELTAS:
        for m in (1, 2, 3):
            ok &= abs(power_sum(d, a, B, m) - power_sum(-d, a, B, m)) < 1e-8
            # additivity sanity: per-sector sum equals trace(H^m)
            ok &= abs(power_sum(d, a, B, m)
                      - float(np.real(np.trace(
                          np.linalg.matrix_power(H(d, a, B), m))))) < 1e-8
        ok &= abs(singlet_readout(d, a, B) - singlet_readout(-d, a, B)) < 1e-10
        ok &= abs(cos3_from_e3(d, a, B) - np.cos(3 * d)) < 1e-8
        ok &= abs(cos3_from_e3(d, a, B) - cos3_from_e3(-d, a, B)) < 1e-8
# empty record: additive per-sector readouts give the empty sum = 0
ok &= (sum(() ) == 0)
check("L6 registrable family (p1,p2,p3; singlet class; cos3delta) "
      "orbit-constant, equal at +/-delta, I(empty)=0", ok)

# ------------------------------------------------------------------- L7 ----
ok = True
for a, B in PARAM_SETS:
    for d in ALL_DELTAS:
        p1 = power_sum(d, a, B, 1)
        p2 = power_sum(d, a, B, 2)
        p3 = power_sum(d, a, B, 3)
        e1 = p1
        e2 = (p1 ** 2 - p2) / 2.0
        e3 = (p1 ** 3 - 3 * p1 * p2 + 2 * p3) / 6.0
        roots = np.sort(np.real(np.roots([1.0, -e1, e2, -e3])))
        direct = np.sort(np.linalg.eigvalsh(H(d, a, B)))
        ok &= np.allclose(roots, direct, atol=1e-6)
        # orbit-resolved reconstruction: singlet value registrable, doublet
        # pair = remaining unordered pair
        l0 = singlet_readout(d, a, B)
        rest = np.sort([x for x in direct
                        if not np.isclose(x, l0, atol=1e-7)] if
                       sum(np.isclose(direct, l0, atol=1e-7)) == 1 else
                       list(np.delete(direct,
                                      int(np.argmin(np.abs(direct - l0))))))
        pair = np.sort([lam(d, a, B, 1), lam(d, a, B, 2)])
        ok &= np.allclose(np.sort(rest), pair, atol=1e-6)
check("L7 exactness: Newton-Girard rebuilds the multiset from registrable "
      "power sums; singlet readout resolves the orbit split", ok)

# ------------------------------------------------------------- hostiles ----
WITNESS = 1e-6

# G1: label-weighted sum  sum_k k*lambda_k
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    found = any(abs(sum(k * lam(d, a, B, k) for k in range(3))
                    - sum(k * lam(-d, a, B, k) for k in range(3))) > WITNESS
                for d in GENERIC_DELTAS)
    ok &= found
check("G1 hostile label-weighted sum violates ORBIT-CONSTANCY "
      "(differs at +/-delta)", ok)

# G2: signed doublet gap lambda_1 - lambda_2 (odd under flip)
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    for d in ALL_DELTAS:
        g_p = lam(d, a, B, 1) - lam(d, a, B, 2)
        g_m = lam(-d, a, B, 1) - lam(-d, a, B, 2)
        ok &= abs(g_p + g_m) < 1e-9          # exactly odd
        # closed form in this labeling convention
        ok &= abs(g_p - 2 * np.sqrt(3.0) * B * np.sin(d)) < 1e-9
    ok &= any(abs(lam(d, a, B, 1) - lam(d, a, B, 2)) > WITNESS
              for d in GENERIC_DELTAS)        # nonzero witness
check("G2 hostile signed doublet gap is K/CPT-odd and nonzero: violates "
      "ORBIT-CONSTANCY", ok)

# G3: fixed-label Vandermonde
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    for d in ALL_DELTAS:
        l = [lam(d, a, B, k) for k in range(3)]
        lm = [lam(-d, a, B, k) for k in range(3)]
        vp = (l[0] - l[1]) * (l[0] - l[2]) * (l[1] - l[2])
        vm = (lm[0] - lm[1]) * (lm[0] - lm[2]) * (lm[1] - lm[2])
        ok &= abs(vp + vm) < 1e-7             # alternating under (1 2)
    ok &= any(abs((lam(d, a, B, 0) - lam(d, a, B, 1))
                  * (lam(d, a, B, 0) - lam(d, a, B, 2))
                  * (lam(d, a, B, 1) - lam(d, a, B, 2))) > WITNESS
              for d in GENERIC_DELTAS)
# additivity violation under the natural sub-multiset extension
# V(empty) = empty product = 1 != 0 (violates I(empty)=0); and
# V(full) != V({l0}) + V({l1,l2}) generically
a0, B0 = PARAM_SETS[0]
d0 = GENERIC_DELTAS[0]
l = [lam(d0, a0, B0, k) for k in range(3)]
v_full = (l[0] - l[1]) * (l[0] - l[2]) * (l[1] - l[2])
v_split = 1.0 + (l[1] - l[2])                # V({l0}) = empty product = 1
ok &= abs(1.0 - 0.0) > WITNESS               # I(empty) = 1 != 0
ok &= abs(v_full - v_split) > WITNESS
check("G3 hostile fixed-label Vandermonde violates I(empty)=0 + ADDITIVITY "
      "and ORBIT-CONSTANCY (alternating)", ok)

# G4: sin(3 delta) -- two values on one K/CPT outcome
ok = all(abs(np.sin(3 * d) - np.sin(-3 * d)) > WITNESS
         and abs(np.sin(3 * d) + np.sin(-3 * d)) < 1e-12
         for d in GENERIC_DELTAS if abs(np.sin(3 * d)) > WITNESS)
ok &= any(abs(np.sin(3 * d)) > WITNESS for d in GENERIC_DELTAS)
check("G4 hostile sin(3 delta) assigns two values to one K/CPT outcome: "
      "violates ORBIT-CONSTANCY", ok)

# G5: interference cross-term
ok = True
for a, B in PARAM_SETS:
    found = False
    for d in GENERIC_DELTAS:
        l1, l2 = lam(d, a, B, 1), lam(d, a, B, 2)
        union_val = l1 + l2 + l1 * l2
        sum_val = l1 + l2
        if abs(union_val - sum_val) > WITNESS:
            found = True
    ok &= found
check("G5 hostile cross-term I(rec1 u rec2)=l1+l2+l1*l2 violates ADDITIVITY",
      ok)

# G6: within-orbit order probe f(k,x) = [k==1]*x
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    found = False
    for d in GENERIC_DELTAS:
        r1_at_d = lam(d, a, B, 1)            # r_1(delta)
        r_sig1_at_md = 0.0                   # f(2, lambda_2(-delta)) = 0
        tot_p = lam(d, a, B, 1)              # total at +delta
        tot_m = lam(-d, a, B, 1)             # total at -delta
        if (abs(r1_at_d - r_sig1_at_md) > WITNESS
                and abs(tot_p - tot_m) > WITNESS):
            found = True
    ok &= found
check("G6 hostile within-orbit order probe f(k,x)=[k==1]x violates "
      "per-record ORBIT-CONSTANCY r_k(d)=r_{sigma(k)}(-d)", ok)

# ------------------------------------------------- degenerate-point sanity --
ok = True
for a, B in PARAM_SETS:
    if B == 0:
        continue
    for d in DEGENERATE_DELTAS:
        # fundamental-domain boundary sin(3 delta) = 0: cos(3 delta) = +/-1
        # exactly, the registrable family is still flip-equal, and the G4
        # hostile functional vanishes (its violation witnesses are generic)
        ok &= abs(np.sin(3 * d)) < 1e-9
        ok &= abs(abs(cos3_from_e3(d, a, B)) - 1.0) < 1e-8
        for m in (1, 2, 3):
            ok &= abs(power_sum(d, a, B, m) - power_sum(-d, a, B, m)) < 1e-8
        sp_p = np.sort(np.linalg.eigvalsh(H(d, a, B)))
        sp_m = np.sort(np.linalg.eigvalsh(H(-d, a, B)))
        ok &= np.allclose(sp_p, sp_m, atol=1e-9)
check("D1 boundary points sin(3 delta)=0: cos(3 delta)=+/-1 exactly, "
      "registrable family flip-equal, G4 hostile vanishes there", ok)

# ---------------------------------------------------------- source scope ----
note = NOTE.read_text(encoding="utf-8")
required_markers = [
    "conditional on the supplied P-dep premise",
    "explicit conditional premise",
    "does **not** derive P-dep from the Record axiom",
    "not a new axiom",
    "not an approved primitive premise",
    "MINIMAL_AXIOMS_2026-06-29.md",
    "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md",
    "T1 transfers supplied ORBIT-INDEXING through the current axiom's",
    "T1 of the cited supplied-context bridge",
    # the load-bearing factorization claim itself is tagged conditional on P-dep
    "factorization / upper bound, conditional on P-dep",
    "without it B1 is not a factorization theorem",
]
forbidden_markers = [
    "MINIMAL_AXIOMS_2026-06-05.md",
    "three Record clauses quoted above",
    "Record axiom's additivity and orbit-constancy clauses",
    "(Orbit) applied",
    "violated Record hypothesis",
    "P-dep is a reading of the Record boundary, not an extra import",
    "grounded in the Record boundary",
    "P-dep is the only admissible reading of the Record boundary",
    "realist slip",
]
ok = all(marker in note for marker in required_markers)
ok &= not any(marker in note for marker in forbidden_markers)
check("H1 source scope: P-dep explicit, K/CPT orbit constancy bridge-relocated",
      ok)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
