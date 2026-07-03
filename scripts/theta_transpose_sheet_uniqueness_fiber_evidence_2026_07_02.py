#!/usr/bin/env python3
"""theta transpose-sheet uniqueness: three evidence angles.

For SU(3) staple triples (A, B, C) modulo diagonal conjugation, the 18 pair
data are tr A, tr B, tr C and the both-orientation composites tr(B^dag A),
tr(B A), tr(C^dag A), tr(C A), tr(C^dag B), tr(C B). A landed-in-flight
result: the 10 C-involving real constraints have a full-rank 10x8 Jacobian at
a generic point (local rigidity), and the simultaneous-transpose triple
preserves all 18 while flipping d = tr(ABC) - tr(ACB). Open sliver: is the
transpose sheet the ONLY global sheet? This runner gathers three
exact/evidence angles; the reviewer drafts the note from the numbers.

Sections:
  A. Expanded fiber search (evidence): fix (A, B), solve the 10 C-constraints
     over the full group C' = expi(t), classify every converged solution by
     the invariant vector (tr(A B C'), tr(A C' B)); look for a second branch.
  B. Both sheets locally rigid (exact): smallest singular value of the 10x8
     C-constraint Jacobian, at C0 and on the transpose sheet.
  C. No new even invariants at low multidegree (exact singlet multiplicities
     via the joint-null-space of the Gell-Mann generator action).

Expected close: TOTAL: PASS=8 FAIL=0
Checks: A1, A2, A3, B1, B2, C1, C2, C3 = 8.
"""

import numpy as np
from scipy.optimize import least_squares
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name} {detail}")


# ---------------------------------------------------------------------------
# Gell-Mann generators (Hermitian, trace-zero); su(3) basis lambda_a.
# ---------------------------------------------------------------------------
def gell_mann():
    L = []
    L.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))
    L.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))
    L.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0))
    return L


LAM = gell_mann()


def expi(t):
    """SU(3) element exp(i * sum_a t_a lambda_a) — spans the full group."""
    H = sum(t[a] * LAM[a] for a in range(8))
    return expm(1j * H)


# ---------------------------------------------------------------------------
# SU(3) sampling: QR of complex Gaussian, phase-fix diagonal, det-normalize.
# ---------------------------------------------------------------------------
def sample_su3(rng):
    z = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    q, r = np.linalg.qr(z)
    # phase-fix: make diagonal of r real-positive so q is deterministic
    ph = np.diag(r).copy()
    ph = ph / np.abs(ph)
    q = q * ph.conj()[np.newaxis, :]
    # det-normalize onto SU(3)
    d = np.linalg.det(q)
    q = q / d ** (1.0 / 3.0)
    return q


# ---------------------------------------------------------------------------
# C-involving pair data (10 real): tr C, tr(C^dag A), tr(C A),
# tr(C^dag B), tr(C B). Returns a length-10 real vector.
# ---------------------------------------------------------------------------
def pairdata_C(C, A, B):
    vals = [
        np.trace(C),
        np.trace(C.conj().T @ A),
        np.trace(C @ A),
        np.trace(C.conj().T @ B),
        np.trace(C @ B),
    ]
    out = []
    for v in vals:
        out.append(v.real)
        out.append(v.imag)
    return np.array(out, dtype=float)


def residual_factory(A, B, target):
    def resid(t):
        C = expi(t)
        return pairdata_C(C, A, B) - target
    return resid


def invariant_vector(A, B, C):
    """The odd-degree invariants that transpose flips: (tr(A B C), tr(A C B))."""
    return np.array([np.trace(A @ B @ C), np.trace(A @ C @ B)], dtype=complex)


# ---------------------------------------------------------------------------
# Section A. Expanded fiber search.
# ---------------------------------------------------------------------------
def fiber_search(A, B, C0, rng, n_inits):
    """Solve the 10 C-constraints over the FULL group C' = expi(t) from
    n_inits fixed random inits; return the converged solutions, each with
    its invariant vector (tr(A B C'), tr(A C' B)), plus the original orbit's
    invariant vector and the list of refutations (solutions whose pair data
    match but whose invariant vector differs)."""
    target = pairdata_C(C0, A, B)
    orig_inv = invariant_vector(A, B, C0)

    inits = [rng.standard_normal(8) * 1.5 for _ in range(n_inits)]
    resid = residual_factory(A, B, target)

    converged = []  # (t, C, invariant_vector)
    for t0 in inits:
        sol = least_squares(
            resid, t0, method="lm",
            xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=6000,
        )
        r = resid(sol.x)
        if np.max(np.abs(r)) < 1e-9:
            C = expi(sol.x)
            converged.append((sol.x, C, invariant_vector(A, B, C)))

    # Refutations: converged solution whose invariant vector differs from
    # the original orbit's (pair data match by construction of the solve).
    refutations = [inv for (_, _, inv) in converged
                   if np.max(np.abs(inv - orig_inv)) >= 1e-6]
    return converged, orig_inv, refutations


# ---------------------------------------------------------------------------
# Section B. Both sheets locally rigid: 10x8 Jacobian smallest singular value.
# ---------------------------------------------------------------------------
def c_constraint_jacobian(A, B, C0):
    """Numerical Jacobian d[pairdata_C(expi(t) applied at C0)]/dt at t=0,
    for the parametrization C(t) = expi(t) @ C0 (tangent to the fiber)."""
    base = pairdata_C(C0, A, B)
    J = np.zeros((10, 8), dtype=float)
    eps = 1e-6
    for a in range(8):
        t = np.zeros(8)
        t[a] = eps
        Cp = expi(t) @ C0
        t[a] = -eps
        Cm = expi(t) @ C0
        J[:, a] = (pairdata_C(Cp, A, B) - pairdata_C(Cm, A, B)) / (2 * eps)
    return J


# ---------------------------------------------------------------------------
# Section C. Singlet multiplicities via Gell-Mann generator null spaces.
# Generators on the fundamental 3: G_a = lambda_a / 2 (Hermitian).
# On the antifundamental 3bar: -conj(lambda_a)/2.
# The joint kernel of the summed action on the tensor product gives the
# number of trivial reps (singlet multiplicity).
# ---------------------------------------------------------------------------
def gen_fund():
    return [LAM[a] / 2.0 for a in range(8)]


def gen_antifund():
    return [-np.conj(LAM[a]) / 2.0 for a in range(8)]


def kron_action(gens_list):
    """For a tensor product of factors with generator lists in gens_list,
    build the 8 total generators acting on the tensor space
    (sum of I x ... x G_a x ... x I) and return the dim of their joint kernel."""
    n_factors = len(gens_list)
    dims = [g[0].shape[0] for g in gens_list]
    total_dim = int(np.prod(dims))
    tot_gens = []
    for a in range(8):
        Ga = np.zeros((total_dim, total_dim), dtype=complex)
        for f in range(n_factors):
            mats = []
            for g in range(n_factors):
                if g == f:
                    mats.append(gens_list[g][a])
                else:
                    mats.append(np.eye(dims[g], dtype=complex))
            term = mats[0]
            for m in mats[1:]:
                term = np.kron(term, m)
            Ga = Ga + term
        tot_gens.append(Ga)
    # Joint kernel dimension = null space of the stacked generator action.
    stacked = np.vstack(tot_gens)
    sv = np.linalg.svd(stacked, compute_uv=False)
    tol = 1e-8 * max(stacked.shape) * sv[0]
    rank = int(np.sum(sv > tol))
    null_dim = total_dim - rank
    return null_dim


def main():
    global PASS, FAIL
    rng = np.random.default_rng(7)

    F = gen_fund()
    Fbar = gen_antifund()

    # ---- Section A ----
    A0 = sample_su3(rng)
    B0 = sample_su3(rng)
    C0 = sample_su3(rng)
    conv1, orig_inv1, refut1 = fiber_search(A0, B0, C0, rng, n_inits=60)
    n1 = len(conv1)

    # A1: search coverage gate — at least 15 of 60 inits converge.
    check(
        "A1 (fiber search coverage, draw1)",
        n1 >= 15,
        f"n_converged={n1} of 60 inits (gate >= 15)",
    )

    # A2: every converged solution's invariant vector (tr(A B C'), tr(A C' B))
    # matches the original orbit — NO second branch. A differing vector is a
    # REFUTATION (report the full vectors prominently).
    a2_ok = (n1 > 0) and (len(refut1) == 0)
    if a2_ok:
        a2_detail = (
            f"all {n1} solutions match orig invariant "
            f"(tr(A B C'), tr(A C' B))={np.round(orig_inv1, 6)}; "
            f"no second branch found"
        )
    else:
        a2_detail = (
            f"REFUTATION (draw1): {len(refut1)} solution(s) match the 10 pair "
            f"constraints but DIFFER in the invariant vector! "
            f"orig={orig_inv1} ; differing={refut1}"
        )
    check("A2 (fiber invariant classification, draw1)", a2_ok, a2_detail)

    # A3: repeat A1-A2 for a SECOND independent (A, B) draw with 30 inits.
    A1m = sample_su3(rng)
    B1m = sample_su3(rng)
    C1m = sample_su3(rng)
    conv2, orig_inv2, refut2 = fiber_search(A1m, B1m, C1m, rng, n_inits=30)
    n2 = len(conv2)
    a3_ok = (n2 >= 8) and (len(refut2) == 0)
    if a3_ok:
        a3_detail = (
            f"n_converged={n2} of 30 inits (gate >= 8); all match orig "
            f"invariant {np.round(orig_inv2, 6)}; no second branch found"
        )
    elif len(refut2) > 0:
        a3_detail = (
            f"REFUTATION (draw2): {len(refut2)} solution(s) match the 10 pair "
            f"constraints but DIFFER in the invariant vector! "
            f"orig={orig_inv2} ; differing={refut2}"
        )
    else:
        a3_detail = f"insufficient coverage: n_converged={n2} of 30 (gate >= 8)"
    check("A3 (fiber search + classification, draw2)", a3_ok, a3_detail)

    # ---- Section B ----
    thr = 1e-2
    J = c_constraint_jacobian(A0, B0, C0)
    sv = np.linalg.svd(J, compute_uv=False)
    smin = float(sv[-1])
    check(
        "B1 (C-constraint Jacobian rigid at C0)",
        smin > thr,
        f"smallest singular value={smin:.6e} (gate > {thr})",
    )

    # Transpose sheet: (A^T, B^T, C0^T), constraints built from (A^T, B^T).
    AT, BT, CT = A0.T, B0.T, C0.T
    Jt = c_constraint_jacobian(AT, BT, CT)
    svt = np.linalg.svd(Jt, compute_uv=False)
    smin_t = float(svt[-1])
    check(
        "B2 (transpose sheet Jacobian rigid)",
        smin_t > thr,
        f"smallest singular value={smin_t:.6e} (gate > {thr})",
    )

    # ---- Section C ----
    # C1: (1,1,1) in (F, F, F) -> tensor 3x3x3, dimension = 1 (epsilon channel).
    d1 = kron_action([F, F, F])
    check(
        "C1 ((1,1,1) F F F invariant dim)",
        d1 == 1,
        f"computed dim={d1} (expected 1: epsilon channel)",
    )

    # C2: 3 x 3bar x 3 x 3bar (A ten Abar ten B ten Bbar) -> dim = 2.
    d2 = kron_action([F, Fbar, F, Fbar])
    check(
        "C2 (3 x 3bar x 3 x 3bar invariant dim)",
        d2 == 2,
        f"computed dim={d2} (expected 2: delta-delta pairings, all pair-generated)",
    )

    # C3: 3 x 3 x 3bar x 3bar (A A B^dag-type mixed quartic) -> dim = 2.
    d3 = kron_action([F, F, Fbar, Fbar])
    check(
        "C3 (3 x 3 x 3bar x 3bar invariant dim)",
        d3 == 2,
        f"computed dim={d3} (expected 2: same conclusion, pair-generated)",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
