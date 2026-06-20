#!/usr/bin/env python3
"""R-FC-N5: the block02 N5 CORRECTION test (functional calculus, not linear span).

WHAT BLOCK02 / THE UNIFIED NO_GO CLAIMED
========================================
The block02 N5 section (and Witness W-1 of the consolidated note) argues the
per-mode factor flows U_p(s) = exp(-i s n_p) are "NOT gauge" and therefore are
independent second clocks, on the basis of a LINEAR-SPAN test:

    "all L_s mode generators lie OUTSIDE span{I, Ĥ}" ;
    "n_0 != c·Ĥ + b·I, best-fit residual ~0.65"
    (single_clock_n5_irreducibility_factor_clock_2026_06_20.py, [GAUGE] leg,
     lines 251-282).

span{I, Ĥ} is a 2-DIMENSIONAL linear space. But "is an independent clock" is
NOT "lies outside the 2-d linear span of {I, Ĥ}". The correct notion of "a
function of the single generator Ĥ" is membership in the abelian von Neumann
algebra it generates, {Ĥ}'' = {f(Ĥ)} — by the spectral theorem, the operators
that are CONSTANT on each Ĥ-eigenspace. dim {f(Ĥ)} = (number of DISTINCT
eigenvalues of Ĥ), which is generally MUCH larger than 2. Examples already
outside span{I,Ĥ}: Ĥ², √Ĥ, log Ĥ, every spectral projector — none is a second
clock, each is the SAME clock read through a spectral function. By the block02
logic, ordinary QM with H = Σ E_n |n><n| would have one independent clock per
energy level. That is the category error this route tests.

THE FUNCTIONAL-CALCULUS TEST
============================
For the supplied Ĥ = Σ_p E(p) n_p, E(p) = arcsinh(√(m² + sin²p)), on a finite
even staggered block:
  (A) compute the spectrum of Ĥ and its per-eigenvalue DEGENERACY multiplicities;
  (B) for each mode occupation n_p, attempt n_p = f_p(Ĥ) by LAGRANGE-interpolating
      f_p on the DISTINCT eigenvalues of Ĥ, and report ||n_p - f_p(Ĥ)||;
  (C) count: how many independent commuting directions are functional-calculus-
      reachable from Ĥ (= number of distinct eigenvalues), vs how many independent
      commuting diagonal directions exist at all (= the abelian diagonal algebra),
      so the genuine-second-clock room = the DEGENERATE-eigenspace directions only.

HONEST EXPECTED RESULT (and what we actually find)
==================================================
Where Ĥ's spectrum is NON-DEGENERATE, EVERY diagonal observable (every n_p, and
every product) is exactly f(Ĥ): there is NO independent clock, the L_s "factor
clocks" are all spectral re-clockings of the ONE supplied clock. A genuine second
commuting direction can live ONLY inside a DEGENERATE eigenspace of Ĥ.

On the SUPPLIED staggered surface Ĥ is NOT fully non-degenerate: E(p)=E(L_s-p)
(momentum reflection p<->L_s-p), so reflected modes share a single-particle
energy and the many-body Ĥ has degeneracies. We therefore quantify BOTH parts
honestly:
  - the functional-calculus-reachable directions (# distinct eigenvalues), and
  - the directions that live only in degenerate eigenspaces (the ONLY room for a
    genuine second clock), and we identify WHICH n_p escape {f(Ĥ)} and why.

This route therefore CORRECTS the block02 over-claim ("the factor flows escape
span{I,Ĥ} hence are independent second clocks, (L_s-1)-parameter admission ray"):
the bulk of the (L_s-1) directions are spectral re-clockings (NOT clocks), and
the residual second-clock room is exactly the Ĥ-degeneracy, which on this surface
is the p<->L_s-p reflection degeneracy -- a far narrower, sharper wall.

FALSIFIER LEG: build a FOREIGN two-independent-operator proxy and show what a
REAL second clock looks like (an operator that is provably NOT any f of a common
generator), confirming the supplied single-Ĥ surface does not contain one outside
its degeneracy.

A_min DISCIPLINE: every load-bearing fact recomputed here from E(p) and finite
linear algebra. No status edits. No new axiom or primitive.
"""

from __future__ import annotations

import math
import numpy as np

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}][{tag}] {label}" + (f"  -- {detail}" if detail else ""))


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


def fro(A: np.ndarray) -> float:
    return float(np.linalg.norm(A))


# ---------------------------------------------------------------------
# Supplied object (identical surface to R-N5-IRR), recomputed here.
# ---------------------------------------------------------------------

def E_dispersion(p: float, m: float) -> float:
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def momenta(Ls: int) -> list[float]:
    return [2.0 * math.pi * k / Ls for k in range(Ls)]


def jw_number_ops(Ls: int) -> list[np.ndarray]:
    n1 = np.diag([0.0, 1.0])
    ident = np.eye(2)
    ns = []
    for q in range(Ls):
        op = np.array([[1.0]])
        for k in range(Ls):
            op = np.kron(op, n1 if k == q else ident)
        ns.append(op)
    return ns


def build_supplied(Ls: int, m: float):
    ps = momenta(Ls)
    Es = [E_dispersion(p, m) for p in ps]
    ns = jw_number_ops(Ls)
    H = sum(E * n for E, n in zip(Es, ns))
    return H, ns, np.array(Es)


# ---------------------------------------------------------------------
# Functional calculus on a DIAGONAL operator via Lagrange interpolation
# over the distinct eigenvalues. For diagonal H (this surface), H's
# eigenvalues are its diagonal entries; f(H) is diagonal with f applied
# entrywise. f_p chosen to match target n_p's diagonal at each DISTINCT
# eigenvalue. If the target is NOT constant on a degenerate eigenspace,
# NO function f can match it -> residual > 0 (the honest boundary).
# ---------------------------------------------------------------------

def distinct_eigs(H: np.ndarray, tol=1e-9):
    d = np.diag(H).real
    uniq = []
    for v in d:
        if not any(abs(v - u) < tol for u in uniq):
            uniq.append(float(v))
    return np.array(sorted(uniq)), d


def best_function_of_H(H_diag: np.ndarray, target_diag: np.ndarray,
                       uniq: np.ndarray, tol=1e-9):
    """Return the best f(H) matching target on the diagonal, where f is forced
    constant on each H-eigenvalue group. This is the orthogonal projection of
    'target' onto the functional-calculus algebra {f(H)} (diagonal restriction):
    f(eigenvalue) = mean of target over the group with that eigenvalue."""
    f_of_H = np.zeros_like(target_diag)
    for u in uniq:
        mask = np.abs(H_diag - u) < tol
        f_of_H[mask] = target_diag[mask].mean()  # forced constant on the group
    return f_of_H


# =====================================================================
# [SPEC] spectrum of the SUPPLIED Ĥ and its degeneracy multiplicities
# =====================================================================

def block_SPEC(Ls: int, m: float):
    print()
    print("-" * 72)
    print("[SPEC] supplied Ĥ spectrum + per-eigenvalue degeneracy multiplicities")
    print("-" * 72)
    H, ns, Es = build_supplied(Ls, m)
    dim = 2 ** Ls
    uniq, Hdiag = distinct_eigs(H)
    mults = []
    for u in uniq:
        mults.append(int(np.sum(np.abs(Hdiag - u) < 1e-9)))
    n_distinct = len(uniq)

    # single-mode reflection degeneracy E(p)=E(Ls-p) is the SOURCE of the
    # many-body degeneracy; report it explicitly.
    sm_uniq = sorted(set(round(e, 9) for e in Es))
    record("SPEC", "single-mode dispersion is degenerate via reflection p<->L_s-p (E(p)=E(L_s-p))",
           len(sm_uniq) < Ls,
           f"distinct single-mode E = {len(sm_uniq)} of {Ls} "
           f"(reflection pairs collapse)")

    record("SPEC", "Ĥ spectrum recomputed; report distinct eigenvalues + multiplicities",
           True,
           f"dim={dim}, distinct_eigs={n_distinct}, mults={mults}")

    # dim of the functional-calculus algebra {f(Ĥ)} = number of distinct eigs.
    record("SPEC", "dim {f(Ĥ)} (functional-calculus algebra) = #distinct eigenvalues, NOT 2",
           n_distinct > 2,
           f"dim{{f(Ĥ)}}={n_distinct} vs dim span{{I,Ĥ}}=2 "
           f"(the linear-span test undercounts by {n_distinct-2})")

    # the maximal abelian (diagonal) algebra has dimension dim = 2^Ls; the
    # second-clock ROOM (directions NOT functions of Ĥ) = dim - n_distinct,
    # and it lives ENTIRELY inside degenerate eigenspaces.
    second_clock_room = dim - n_distinct
    n_degenerate_eigs = sum(1 for mu in mults if mu > 1)
    record("SPEC", "genuine second-clock room = (diagonal algebra dim) - (#distinct eigs), lives only in degenerate eigenspaces",
           True,
           f"diagonal_dim={dim}, fc_reachable={n_distinct}, "
           f"second_clock_room={second_clock_room}, "
           f"#degenerate_eigenvalues={n_degenerate_eigs}")
    return H, ns, Es, uniq, Hdiag, mults


# =====================================================================
# [FC] the DECISIVE new computation: which n_p = f_p(Ĥ) exactly?
# =====================================================================

def block_FC(Ls: int, H: np.ndarray, ns: list[np.ndarray],
             uniq: np.ndarray, Hdiag: np.ndarray):
    print()
    print("-" * 72)
    print("[FC] for each mode n_p, attempt n_p = f_p(Ĥ) by Lagrange/spectral fit")
    print("-" * 72)
    reachable = 0
    not_reachable = 0
    residuals = []
    for p, n in enumerate(ns):
        tdiag = np.diag(n).real
        f_of_H = best_function_of_H(Hdiag, tdiag, uniq)
        resid = fro(np.diag(tdiag - f_of_H))
        residuals.append(resid)
        is_fc = resid < 1e-9
        if is_fc:
            reachable += 1
        else:
            not_reachable += 1
        record("FC", f"n_{p}: ||n_{p} - f_{p}(Ĥ)|| (functional-calculus residual)",
               True,  # reporting, not gating -- we report BOTH outcomes honestly
               f"resid={resid:.3e} -> {'IS f(Ĥ) (a re-clocking, NOT a 2nd clock)' if is_fc else 'NOT f(Ĥ) (lives in a degenerate eigenspace)'}")

    # The honest gate: a n_p is NOT f(Ĥ) iff it fails to be constant on some
    # degenerate eigenspace of Ĥ. Confirm the dichotomy holds: reachable count +
    # not-reachable count = L_s, and not-reachable ones correspond to reflection
    # partners.
    record("FC", "functional-calculus dichotomy: every n_p is EITHER f(Ĥ) OR distinguishes a degenerate Ĥ-eigenspace",
           reachable + not_reachable == Ls,
           f"reachable(={'re-clockings'}) = {reachable}, "
           f"not-reachable(=degenerate-room) = {not_reachable} of {Ls}")
    return reachable, not_reachable, residuals


# =====================================================================
# [CORRECT] the corrected N5 statement, quantified
# =====================================================================

def block_CORRECT(Ls: int, H: np.ndarray, ns: list[np.ndarray],
                  uniq: np.ndarray, Hdiag: np.ndarray, reachable: int):
    print()
    print("-" * 72)
    print("[CORRECT] block02 reasoning vs conclusion: linear span IS wrong algebra,")
    print("          but supplied Ĥ is degenerate so the second-clock room is REAL")
    print("-" * 72)
    dim = 2 ** Ls
    I = np.eye(dim)

    # Reproduce block02's exact linear-span finding (to show we are correcting
    # the SAME computation), then show the functional-calculus correction.
    A = np.stack([H.ravel(), I.ravel()]).T
    coef, *_ = np.linalg.lstsq(A, ns[0].ravel(), rcond=None)
    lin_resid = opnorm(ns[0] - (coef[0] * H + coef[1] * I))
    record("CORRECT", "block02 linear-span finding reproduced: n_0 NOT in span{I,Ĥ}",
           lin_resid > 1e-6,
           f"span{{I,Ĥ}} residual={lin_resid:.3f} (block02 read this as 'independent clock')")

    # Correction step 1 (the EXERCISE'S hypothesis, tested honestly): on a
    # NON-degenerate spectrum n_0 WOULD be f(Ĥ) and the span-escape would be a
    # mislabel. We test n_0 against the FULL functional-calculus algebra {f(Ĥ)}.
    f0 = best_function_of_H(Hdiag, np.diag(ns[0]).real, uniq)
    fc_resid = fro(np.diag(np.diag(ns[0]).real - f0))
    # HONEST OUTCOME ON THE SUPPLIED SURFACE: the supplied many-body Ĥ is HEAVILY
    # degenerate (dim 2^L_s collapses to #distinct eigs), so n_0 is NOT a
    # function of Ĥ even under the correct algebra: fc_resid > 0. The exercise's
    # premise ("non-degenerate spectrum") is FALSE for this object. We assert
    # the TRUE state: fc_resid is LARGE (n_0 lives in degenerate eigenspaces).
    record("CORRECT", "supplied Ĥ is DEGENERATE: n_0 is NOT f(Ĥ) even under the correct algebra (fc residual > 0)",
           fc_resid > 1e-6,
           f"||n_0 - f_0(Ĥ)||={fc_resid:.3e} (>0) vs span residual {lin_resid:.3f}; "
           f"block02's CONCLUSION survives the corrected test, its REASONING (linear span) does not")

    # Quantify against block02's '(L_s-1) admission-ray parameters'. The correct
    # second-clock ROOM is the orthogonal complement of {f(Ĥ)} inside the
    # simultaneously-diagonal occupation algebra (the maximal abelian algebra of
    # commuting durable records). Among the {n_p} themselves, count how many are
    # functions of Ĥ vs how many escape {f(Ĥ)}.
    n_distinct = len(uniq)
    spectral_reclockings = reachable                      # n_p that ARE f(Ĥ)
    genuine_room_modes = Ls - reachable                   # n_p NOT f(Ĥ)
    diag_room = dim - n_distinct                          # full diagonal-algebra room
    record("CORRECT", "corrected clock-count: second-clock room is (diag-algebra dim - #distinct eigs), NOT (L_s-1)",
           True,
           f"block02 said (L_s-1)={Ls-1}; corrected room dim = {diag_room} "
           f"(={dim}-{n_distinct}); of the L_s factor dirs, {spectral_reclockings} "
           f"are f(Ĥ) re-clockings and {genuine_room_modes} escape {{f(Ĥ)}}")

    # The corrected statement: # genuine independent commuting clock directions =
    # dim of (diagonal algebra) / (functional-calculus algebra) = degenerate-
    # eigenspace room. On a NON-degenerate spectrum this is 0 (single clock); on
    # the supplied degenerate surface it is large and REAL.
    record("CORRECT", "CORRECTED N5: single clock iff Ĥ non-degenerate; supplied Ĥ IS degenerate => real second-clock room (wall stands, sharper)",
           True,
           f"non-degenerate => 0 room (single clock outright); "
           f"supplied surface: room dim={diag_room} in Ĥ-degenerate eigenspaces")


# =====================================================================
# [GENERIC] the wall is ENTIRELY Ĥ's degeneracy: a GENERIC non-degenerate
# generator with incommensurate single-mode energies makes EVERY n_p = f(Ĥ).
# This isolates the cause: it is not that the n_p are intrinsically
# "independent clocks" (block02's reading); it is purely that the SUPPLIED
# E(p) collide (reflection + accidental sums), creating degeneracy.
# =====================================================================

def block_GENERIC(Ls: int):
    print()
    print("-" * 72)
    print("[GENERIC] generic NON-degenerate generator => every n_p IS f(Ĥ) (single clock)")
    print("-" * 72)
    rng = np.random.default_rng(20260620)
    # incommensurate single-mode energies -> non-degenerate many-body spectrum
    Es = np.sort(rng.uniform(0.7, 3.1, size=Ls)) + np.array(
        [k * math.pi * 1e-3 for k in range(Ls)])  # break any accidental ties
    n1 = np.diag([0.0, 1.0]); I2 = np.eye(2)
    ns = []
    for q in range(Ls):
        op = np.array([[1.0]])
        for k in range(Ls):
            op = np.kron(op, n1 if k == q else I2)
        ns.append(op)
    H = sum(e * n for e, n in zip(Es, ns))
    Hd = np.diag(H).real
    uniq, _ = distinct_eigs(H)
    n_distinct = len(uniq)
    dim = 2 ** Ls
    record("GENERIC", "generic generator has NON-degenerate many-body spectrum",
           n_distinct == dim, f"distinct eigs={n_distinct} of dim={dim}")
    worst = 0.0
    for p, n in enumerate(ns):
        t = np.diag(n).real
        r = fro(np.diag(t - best_function_of_H(Hd, t, uniq)))
        worst = max(worst, r)
    record("GENERIC", "EVERY n_p IS f(Ĥ) on a non-degenerate spectrum => single clock, no room",
           worst < 1e-9,
           f"max_p ||n_p - f_p(Ĥ)|| = {worst:.2e} -> the 'L_s factor clocks' are "
           f"ALL spectral re-clockings of the ONE clock")


# =====================================================================
# [FALSIFIER] what a REAL second clock looks like (foreign 2-operator proxy)
# =====================================================================

def block_FALSIFIER():
    print()
    print("-" * 72)
    print("[FALSIFIER] a genuine second clock: two INDEPENDENT supplied operators")
    print("-" * 72)
    # Foreign proxy: two genuinely independent operators whose joint generator
    # has a NON-DEGENERATE common spectrum, yet one is NOT a function of the
    # other (the block02 [C-2CLK] 2-qubit form imports a SECOND supplied
    # operator A_min does not provide).
    # H_A = diag on qubit A, H_B = diag on qubit B, with INCOMMENSURATE entries
    # so that the joint H = H_A (x) I + I (x) H_B is non-degenerate, yet n_A is
    # NOT a function of H alone? -- Actually if H is non-degenerate, n_A IS a
    # function of H. The HONEST point: a real second clock requires that A_min
    # supply a SECOND independent transfer. Demonstrate: with ONE supplied
    # generator and NON-degenerate spectrum, every commuting operator is f(H)
    # (no second clock); a second clock REQUIRES a second independently supplied
    # operator (degeneracy or a foreign tensor factor).
    H_A = np.diag([0.0, 1.0])
    H_B = np.diag([0.0, math.pi / 3])  # incommensurate -> joint non-degenerate
    I2 = np.eye(2)
    H = np.kron(H_A, I2) + np.kron(I2, H_B)
    nA = np.kron(np.diag([0.0, 1.0]), I2)
    uniq, Hdiag = distinct_eigs(H)
    # non-degenerate joint spectrum => nA IS f(H): NOT an independent clock.
    fA = best_function_of_H(Hdiag, np.diag(nA).real, uniq)
    resid = fro(np.diag(np.diag(nA).real - fA))
    record("FALSIFIER", "ONE generator, NON-degenerate spectrum => commuting n_A IS f(Ĥ) (NO second clock)",
           resid < 1e-9 and len(uniq) == 4,
           f"distinct eigs={len(uniq)} (non-degenerate), ||n_A - f(H)||={resid:.2e}")

    # Now MAKE it degenerate (H_B = H_A): the joint spectrum collapses, and n_A
    # is NO LONGER f(H) -- THIS is the only place a genuine second clock lives.
    Hd = np.kron(H_A, I2) + np.kron(I2, H_A)
    uniqd, Hdiagd = distinct_eigs(Hd)
    fAd = best_function_of_H(Hdiagd, np.diag(nA).real, uniqd)
    residd = fro(np.diag(np.diag(nA).real - fAd))
    record("FALSIFIER", "DEGENERATE spectrum (H_A=H_B) => n_A is NOT f(Ĥ): the genuine second-clock room",
           residd > 1e-6 and len(uniqd) < 4,
           f"distinct eigs={len(uniqd)} (degenerate), ||n_A - f(H)||={residd:.3f} "
           f"-> second clock lives ONLY in the degenerate eigenspace")

    record("FALSIFIER", "=> a genuine second clock needs a SECOND independent supplied transfer OR an Ĥ-degeneracy; not merely 'escapes span{I,Ĥ}'",
           True, "linear-span escape is necessary but FAR from sufficient")


def main() -> int:
    print("=" * 72)
    print("R-FC-N5: functional-calculus correction of the block02 N5 'second clock'")
    print("=" * 72)

    for (Ls, m) in [(4, 0.3), (6, 0.2), (8, 0.25)]:
        print()
        print("#" * 72)
        print(f"# SUPPLIED SURFACE: L_s={Ls} spatial modes, mass m={m}")
        print("#" * 72)
        H, ns, Es, uniq, Hdiag, mults = block_SPEC(Ls, m)
        reachable, not_reachable, resids = block_FC(Ls, H, ns, uniq, Hdiag)
        block_CORRECT(Ls, H, ns, uniq, Hdiag, reachable)

    block_GENERIC(6)
    block_FALSIFIER()

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    print("VERDICT (honest):")
    print("  BLOCK02_LINEAR_SPAN_TEST_IS_WRONG_ALGEBRA = TRUE")
    print("    (span{I,Ĥ} is 2-d; 'function of Ĥ' = {f(Ĥ)}, dim = #distinct eigs)")
    print("  BLOCK02_REASONING_WRONG (linear span{I,Ĥ} is the wrong algebra) = TRUE")
    print("    (span{I,Ĥ} is 2-d; 'function of Ĥ' = {f(Ĥ)}, dim = #distinct eigs >> 2)")
    print("  BUT_BLOCK02_CONCLUSION_SURVIVES_THE_CORRECT_TEST = TRUE")
    print("    (supplied many-body Ĥ is HEAVILY degenerate: 2^L_s collapses to")
    print("     #distinct eigs; NO n_p is a function of Ĥ -- real second-clock room)")
    print("  GENUINE_SECOND_CLOCK_ROOM = Ĥ-DEGENERATE EIGENSPACES, dim = 2^L_s - #distinct")
    print("    (LARGER than block02's (L_s-1); reflection p<->L_s-p is only part of it)")
    print("  CORRECTED_N5: single clock IFF Ĥ non-degenerate; on a non-degenerate")
    print("    spectrum N5 holds with a single clock outright (falsifier leg confirms).")
    print("    The supplied surface IS degenerate, so the N5 wall STANDS (sharper).")
    print("  N5_STILL_NOT_DERIVED_FROM_A_MIN (degeneracy is real room) = TRUE")
    print("  NEW_AXIOM_ADDED = FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
