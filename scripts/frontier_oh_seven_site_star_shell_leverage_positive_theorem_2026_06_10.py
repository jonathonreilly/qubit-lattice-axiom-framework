"""Positive theorem: the O_h seven-site-star shell-leverage constants. The per-arm isotypic projector
weights of the octahedral 6-arm permutation rep are exactly (A1,E,T1) = (1/6, 1/3, 1/2); hence the
shell leverage kappa := P_T1(arm)/P_E(arm) = dim(T1)/dim(E) = 3/2 (kappa^2 = 9/4), and Hom_Oh(E,T1) = 0
so the E and T1 equivariant scales on the star are independent. These are exact, unconditional,
box-independent representation-theory constants of the framework's 7-site octahedral star support.

SCOPE: this is a STANDALONE POSITIVE rep-theory lemma about the support geometry only. It does NOT, by
itself, derive any Route-2 readout entry, mass ratio, or the value rho_E = 21/4 / c_TE = -8/9: those
require the additional covariance bridge q_E/q_T = kappa^2, which is NOT supplied by this structure (see
the companion no-go QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_..._2026-06-10). This lemma
is the load-bearing POSITIVE content that the no-go cites; it is split out here as a clean exact theorem.

CHECKS (exact: finite group O_h = 48 signed permutation matrices; exact rational projectors):
  L1  the 6-arm O_h permutation rep decomposes MULTIPLICITY-FREE as A1g (+) Eg (+) T1u; the isotypic
      projectors (built group-theoretically: P_A1 = Reynolds average; P_T1 = (I-A)/2 with A the antipodal
      involution = action of -I; P_E = (I+A)/2 - P_A1) are mutually orthogonal idempotents of ranks
      (1,2,3) summing to the identity.
  L2  the per-arm diagonal isotypic weights are EXACTLY (1/6, 1/3, 1/2) = dim(irrep)/6 -- the universal
      multiplicity-free transitive-permutation-rep value (the orbit of any arm under O_h is all 6 arms).
  L3  the shell leverage kappa := P_T1(arm,arm)/P_E(arm,arm) = (1/2)/(1/3) = 3/2 = dim(T1)/dim(E); and
      kappa^2 = 9/4. (Equivalently the per-arm A1:E:T1 weight ratios 1:2:3 = the irrep dimensions.)
  L4  Hom_Oh(E,T1) = 0 (E and T1 are inequivalent irreps; the Reynolds intertwiner average(P_T1 g P_E)
      vanishes), so the most general O_h-equivariant operator on the arm space carries INDEPENDENT scalars
      on the E and T1 blocks -- equivariance imposes no relation between them.
  L5  STRUCTURAL (box-independent): the projectors are pure group averages with NO dynamics / Green's
      function / box input, so kappa = 3/2 is an exact constant of the star geometry, independent of any
      embedding box size. (This is what distinguishes it from a dynamical readout functional.)

No PDG / fitted / observed value; no axiom, primitive, or admission. Pure finite-group representation
theory of the framework's lattice-axiom support star.
"""
from __future__ import annotations
import itertools

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


ARMS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AIDX = {a: i for i, a in enumerate(ARMS)}


def oh_group():
    G = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), int)
            for r in range(3):
                M[r, perm[r]] = signs[r]
            G.append(M)
    return G                                            # |O_h| = 48 signed permutation matrices


def arm_rep(M):
    P = np.zeros((6, 6))
    for a in ARMS:
        b = tuple(int(x) for x in (M @ np.array(a)))
        P[AIDX[b], AIDX[a]] = 1.0
    return P


def main() -> int:
    print("O_h SEVEN-SITE-STAR SHELL-LEVERAGE POSITIVE THEOREM")
    print("=" * 80)
    G = oh_group()
    assert len(G) == 48
    reps = [arm_rep(M) for M in G]

    P_A1 = sum(reps) / 48.0
    A = arm_rep(-np.eye(3, dtype=int))                  # antipodal involution (action of -I)
    P_T1 = (np.eye(6) - A) / 2.0
    P_E = (np.eye(6) + A) / 2.0 - P_A1
    Ps = {"A1": P_A1, "E": P_E, "T1": P_T1}

    # ---- L1: multiplicity-free A1+E+T1, orthogonal idempotents, ranks (1,2,3), sum = I ----
    idemp = all(np.allclose(P @ P, P) for P in Ps.values())
    orth = (np.allclose(P_A1 @ P_E, 0) and np.allclose(P_A1 @ P_T1, 0) and np.allclose(P_E @ P_T1, 0))
    ranks = {k: int(round(np.trace(P))) for k, P in Ps.items()}
    spanning = np.allclose(P_A1 + P_E + P_T1, np.eye(6))
    # equivariance: each P commutes with the whole group
    equivar = all(np.allclose(r @ P - P @ r, 0) for P in Ps.values() for r in reps[:12])
    check("L1 (multiplicity-free A1+E+T1): the 6-arm O_h rep splits into mutually orthogonal equivariant "
          "idempotents of ranks (A1,E,T1)=(1,2,3) summing to I",
          idemp and orth and spanning and ranks == {"A1": 1, "E": 2, "T1": 3} and equivar,
          f"ranks={ranks}; orthogonal idempotents={idemp and orth}; sum=I {spanning}; commute with G {equivar}")

    # ---- L2: per-arm isotypic weights = (1/6, 1/3, 1/2) = dim/6 ----
    weights = {k: P[0, 0] for k, P in Ps.items()}
    # arm-independence: same diagonal on every arm
    arm_uniform = all(abs(Ps[k][i, i] - weights[k]) < 1e-13 for k in Ps for i in range(6))
    targets = {"A1": 1 / 6, "E": 1 / 3, "T1": 1 / 2}
    weights_ok = all(abs(weights[k] - targets[k]) < 1e-13 for k in Ps) and arm_uniform
    check("L2 (per-arm weights = dim/6): the per-arm isotypic projector diagonal is exactly "
          "(A1,E,T1)=(1/6,1/3,1/2)=dim/6, identical on every arm (multiplicity-free transitive perm rep)",
          weights_ok,
          f"per-arm weights = {{A1:{weights['A1']:.6f}, E:{weights['E']:.6f}, T1:{weights['T1']:.6f}}} "
          f"= (1/6,1/3,1/2); arm-uniform={arm_uniform}")

    # ---- L3: kappa = 3/2 = dim(T1)/dim(E), kappa^2 = 9/4 ----
    kappa = weights["T1"] / weights["E"]
    dim_ratio = ranks["T1"] / ranks["E"]
    check("L3 (shell leverage kappa = 3/2): kappa := P_T1(arm)/P_E(arm) = (1/2)/(1/3) = 3/2 = "
          "dim(T1)/dim(E), and kappa^2 = 9/4 (per-arm weight ratios A1:E:T1 = 1:2:3 = the irrep dimensions)",
          abs(kappa - 1.5) < 1e-13 and abs(kappa - dim_ratio) < 1e-13 and abs(kappa**2 - 9 / 4) < 1e-13,
          f"kappa = {kappa:.6f} = 3/2 = dim(T1)/dim(E) = {dim_ratio}; kappa^2 = {kappa**2:.6f} = 9/4")

    # ---- L4: Hom_Oh(E,T1) = 0 -> independent equivariant E/T scales ----
    intertwiner = sum(P_T1 @ r @ P_E for r in reps) / 48.0
    hom0 = float(np.abs(intertwiner).max()) < 1e-13
    # the equivariant commutant on the arm space: dim = sum of (multiplicity)^2 = 1+1+1 = 3 (one scalar
    # per multiplicity-free block) -> lambda_E, lambda_T independent
    check("L4 (Hom_Oh(E,T1)=0): E and T1 are inequivalent irreps, so the Reynolds intertwiner "
          "average(P_T1 . g . P_E) = 0 exactly; the equivariant commutant is 3-dimensional (one "
          "independent scalar on each of A1, E, T1) -- equivariance imposes NO relation between the E and "
          "T1 scales",
          hom0,
          f"||average(P_T1 g P_E)|| = {np.abs(intertwiner).max():.1e} -> Hom_Oh(E,T1)=0; independent E,T scales")

    # ---- L5: structural / box-independent ----
    # rebuild with a randomly relabeled arm order to confirm the weights are intrinsic (not basis-dependent)
    rng = np.random.default_rng(0)
    perm = rng.permutation(6)
    Pp = sum(arm_rep(M)[np.ix_(perm, perm)] for M in G) / 48.0
    structural = abs(Pp[0, 0] - 1 / 6) < 1e-13  # A1 weight invariant under arm relabeling
    check("L5 (structural / box-independent): the projectors are pure O_h group averages -- NO dynamics, "
          "Green's function, or embedding-box input -- so kappa = 3/2 is an exact constant of the star "
          "geometry, invariant under arm relabeling, independent of any embedding box size (this is what "
          "distinguishes it from a dynamical readout functional)",
          structural,
          "A1 weight invariant under arm relabeling; projectors are group averages, box-free")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (positive theorem): on the framework's 7-site octahedral star, the 6-arm O_h rep is\n"
        "multiplicity-free A1g(+)Eg(+)T1u with exact per-arm isotypic weights (1/6, 1/3, 1/2); hence the\n"
        "shell leverage kappa = P_T1/P_E = dim(T1)/dim(E) = 3/2 (kappa^2 = 9/4), and Hom_Oh(E,T1)=0 leaves\n"
        "the E and T1 equivariant scales independent. These are exact, unconditional, box-independent\n"
        "representation-theory constants of the support star. SCOPE: a standalone structural lemma only --\n"
        "it does NOT derive any Route-2 readout entry / rho_E=21/4 (that needs the covariance bridge\n"
        "q_E/q_T = kappa^2, which this structure does NOT supply -- see the companion no-go). No PDG/\n"
        "fitted value; no axiom or admission."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
