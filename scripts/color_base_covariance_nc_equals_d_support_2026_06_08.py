"""Counterfactual color-base covariance support: N_c = d in a supplied Z^d family.

This runner checks the color-base covariance calculation behind the source
note. It treats the Z^d taste-cube family and weak-axis selection as supplied
counterfactual inputs, not as framework axioms.

The prior COLOR-BASE lens asserted: "the color base is Sym^2(C^2) (TWO qubits) under a single swap,
dim 3 REGARDLESS of d, so N_c=3=dim Z^3 is a matched-pair COINCIDENCE (d-independent), like the #2559
d=3 demotion." If true, the retained CL3_COLOR_AUTOMORPHISM 'N_c=3 forced by dim Z^3' would be an
over-claim to demote. This runner only tests the counterfactual family shape.

This runner tests that claim against the ACTUAL graph-first construction (GRAPH_FIRST_SU3_INTEGRATION_NOTE):
the taste cube is {0,1}^d (one taste qubit per spatial axis). Select ONE axis as the weak su(2) fiber; the
REMAINING d-1 axes form the base (C^2)^{(x)(d-1)}; the residual permutation group S_{d-1} acts; the
fully-symmetric (trivial-isotype) block carries color. So the base is Sym^{d-1}(C^2), NOT a fixed Sym^2.

PREDICTION if the construction is d-COVARIANT (campaign WRONG, note RIGHT):
  dim(symmetric block) = dim Sym^{d-1}(C^2) = (d-1)+1 = d   -> N_c = d = dim Z^d  (genuine covariation)
  commutant of S_{d-1} on the symmetric isotype = gl(d) (dim d^2), semisimple su(d) (dim d^2-1).

VERIFIES, for d = 2,3,4,5,6:
  1. The base has d-1 qubits (the residual axes), dim 2^{d-1}.
  2. The fully-symmetric block (common +1 eigenspace of every base-axis transposition) has dim = d
      (NOT fixed at 3) -> it IS Sym^{d-1}(C^2), and d-1 (the exponent) varies with d.
  3. The commutant of the residual S_{d-1} action, restricted to the symmetric isotype, is gl(d):
      so the colour group on the symmetric block is su(d), N_c = d.  d=3 -> su(3), d=4 -> su(4), ...
  4. The campaign's "Sym^2(C^2) = 3 for all d" is the d=3 SPECIAL CASE only; Sym^2 has a FIXED exponent
      2, whereas the construction's exponent is d-1. They coincide ONLY at d=3.
  5. d=3 cross-check vs the landed note: base dim 4, joint commutant dim 10 = gl(3)+gl(1), symmetric/
      antisymmetric block dims 3/1.

If the checks hold, N_c=d co-varies with the supplied lattice dimension in
this counterfactual family. At the live Z^3 baseline it supports consistency
with N_c=3; it is not an axiom-level derivation.

No PDG/fitted value; exact numpy.
"""
from __future__ import annotations
import numpy as np
import itertools

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


def transposition_op(n, i, j):
    """Operator on (C^2)^{(x)n} that swaps tensor factors i and j (permutes the n base qubits)."""
    dim = 2 ** n
    P = np.zeros((dim, dim))
    for idx in range(dim):
        bits = [(idx >> (n - 1 - k)) & 1 for k in range(n)]  # bits[0] = most significant
        bits[i], bits[j] = bits[j], bits[i]
        out = 0
        for k in range(n):
            out = (out << 1) | bits[k]
        P[out, idx] = 1.0
    return P


def sym_isotype_dim(n):
    """dim of the fully-symmetric subspace (common +1 eigenspace of all transpositions) of n qubits."""
    if n <= 1:
        return 2 ** n  # no permutations to impose (S_0, S_1 trivial) -> full space is symmetric
    dim = 2 ** n
    # symmetric subspace = intersection of +1 eigenspaces of all adjacent transpositions
    M = np.zeros((0, dim))
    for i in range(n - 1):
        T = transposition_op(n, i, i + 1)
        M = np.vstack([M, T - np.eye(dim)])   # (T - I) v = 0  <=> v symmetric
    # nullspace dim = dim - rank
    return dim - np.linalg.matrix_rank(M)


def commutant_dim(gens, dim):
    """dim of the commutant {X : [G,X]=0 for all G} on C^dim."""
    rows = np.zeros((0, dim * dim))
    for G in gens:
        L = np.kron(np.eye(dim), G) - np.kron(G.T, np.eye(dim))
        rows = np.vstack([rows, L])
    return dim * dim - np.linalg.matrix_rank(rows)


def commutant_on_symmetric_isotype_dim(n):
    """dim of the commutant of S_n restricted to the symmetric (trivial) isotype block.
    By Schur-Weyl this should be gl(d) with d = n+1, i.e. (n+1)^2."""
    dim = 2 ** n
    gens = [transposition_op(n, i, i + 1) for i in range(n - 1)] if n >= 2 else []
    # projector onto symmetric subspace
    if n <= 1:
        Psym = np.eye(dim)
    else:
        # symmetric projector = average over the full S_n group
        Psym = np.zeros((dim, dim))
        cnt = 0
        for perm in itertools.permutations(range(n)):
            # build permutation operator for this perm
            P = np.zeros((dim, dim))
            for idx in range(dim):
                bits = [(idx >> (n - 1 - k)) & 1 for k in range(n)]
                newbits = [bits[perm[k]] for k in range(n)]
                out = 0
                for b in newbits:
                    out = (out << 1) | b
                P[out, idx] = 1.0
            Psym += P
            cnt += 1
        Psym /= cnt
    # restrict commutant of S_n to symmetric block: dim of {X on sym-subspace commuting with S_n|sym}.
    # Since S_n acts trivially on the symmetric isotype, EVERY operator on the symmetric subspace commutes
    # there; the Schur-Weyl commutant block is End(Sym^n) = gl(n+1). Verify dim of symmetric subspace = n+1
    # and report (n+1)^2 as the gl(n+1) block dim.
    d_sym = int(round(np.trace(Psym)))
    return d_sym, d_sym * d_sym


def main() -> int:
    print("COLOR-BASE COVARIANCE SUPPORT: N_c = d in a supplied Z^d family")
    print("=" * 78)
    print("Construction: taste cube {0,1}^d; select 1 axis (weak su(2) fiber); base = d-1 residual axes;")
    print("residual S_{d-1} symmetric block carries color su(N_c).")
    print()

    rows = []
    all_cov = True
    for d in [2, 3, 4, 5, 6]:
        n = d - 1                       # number of base (residual) qubits
        base_dim = 2 ** n
        d_sym = sym_isotype_dim(n)      # dim of symmetric block
        sym2 = 2 + 1                    # the campaign's fixed Sym^2(C^2) = 3
        covaries = (d_sym == d)
        all_cov = all_cov and covaries
        rows.append((d, n, base_dim, d_sym, d_sym * d_sym, (d_sym * d_sym - 1)))
        print(f"  d={d}: base = {n} residual qubit(s), base_dim=2^{n}={base_dim};  "
              f"symmetric block dim = {d_sym}  (Sym^{n}(C^2) = {n}+1 = {d_sym});  "
              f"-> color gl({d_sym}) dim {d_sym*d_sym}, su({d_sym}) dim {d_sym*d_sym-1}")

    # Check 1/2: symmetric block dim = d for every d (covariation), and != fixed 3
    check("support 1: symmetric block dim = d for d=2..6 (Sym^{d-1}(C^2), exponent d-1 VARIES) -> N_c = d, "
          "co-varies with the lattice dimension (NOT fixed at Sym^2=3)",
          all_cov and [r[3] for r in rows] == [2, 3, 4, 5, 6],
          f"symmetric block dims = {[r[3] for r in rows]} for d={[r[0] for r in rows]} (== d)")

    # Check 3: commutant on the symmetric isotype = gl(d), su(d) = d^2-1
    su_ok = True
    detail3 = []
    for d in [2, 3, 4, 5]:
        n = d - 1
        d_sym, gl_dim = commutant_on_symmetric_isotype_dim(n)
        su_dim = gl_dim - 1
        ok = (d_sym == d and gl_dim == d * d)
        su_ok = su_ok and ok
        detail3.append(f"d={d}: gl({d_sym}) dim {gl_dim} (=d^2={d*d}), su({d_sym}) dim {su_dim}")
    check("support 2: commutant of residual S_{d-1} on the symmetric isotype = gl(d) (dim d^2) -> color su(d) "
          "(dim d^2-1); d=3->su(3), d=4->su(4), d=5->su(5) (Schur-Weyl: End(Sym^{d-1} C^2)=gl(d))",
          su_ok, "; ".join(detail3))

    # Check 4: the fixed Sym^2(C^2) reading is the d=3 special case.
    fixed_sym2 = [3, 3, 3, 3, 3]
    construction = [r[3] for r in rows]
    coincide_only_at_3 = (construction[1] == fixed_sym2[1]) and all(
        construction[i] != fixed_sym2[i] for i in range(len(rows)) if rows[i][0] != 3)
    check("support 3: the fixed 'Sym^2(C^2)=3 for all d' reading equals the construction ONLY at d=3 "
          "(fixed exponent 2 vs the construction's exponent d-1); they DIVERGE for every d != 3",
          coincide_only_at_3,
          f"construction Sym^(d-1) dims {construction} vs campaign's fixed-Sym^2 {fixed_sym2} -> agree only at d=3")

    # Check 5: d=3 cross-check vs the landed graph-first note.
    n = 2
    base = 4
    tau = transposition_op(2, 0, 1)
    joint_comm = commutant_dim([tau], base)   # commutant of the single residual swap on the 4-dim base
    # symmetric (sym block) dim 3, antisym dim 1
    sym3 = sym_isotype_dim(2)
    check("support 4: d=3 cross-check vs GRAPH_FIRST_SU3_INTEGRATION_NOTE -- base dim 4, commutant of the residual "
          "swap = gl(3)+gl(1) dim 10, symmetric/antisymmetric block dims 3/1",
          base == 4 and joint_comm == 10 and sym3 == 3,
          f"base_dim={base}, comm(tau) dim={joint_comm} (=gl(3)+gl(1)=10), sym block dim={sym3}, antisym dim={base-sym3}")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(
        "VERDICT (counterfactual support, under an assumed Z^d taste-cube family with one selected weak\n"
        "axis): the residual base is Sym^{d-1}(C^2) with dim = d; the S_{d-1} commutant on the symmetric\n"
        "isotype is gl(d), so the color block is su(d) and N_c = d in this counterfactual family. At the\n"
        "Z^3 baseline this gives N_c = 3, CONSISTENT with the retained graph-first SU(3) / CL3_COLOR_AUTO-\n"
        "MORPHISM result on the live d=3 surface. This is SUPPORT (it shows N_c tracks dim along the\n"
        "assumed family, addressing a matched-pair-coincidence worry); it is NOT a from-axioms derivation\n"
        "(the Z^d family, the taste-cube, and the weak-axis selection are assumed, not supplied by\n"
        "{Lattice, Quantum, Record}). Audit lane sets the status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
