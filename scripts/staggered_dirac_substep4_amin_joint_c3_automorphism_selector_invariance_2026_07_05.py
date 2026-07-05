"""Runner for the A_min joint-C3 automorphism / selector-invariance bridge
(2026-07-05).

Verifies, with exact sympy arithmetic and mechanical text checks:

  S1  the live axiom memo supplies proper cubic rotations, covariance, the
      no-privilege clauses, and the Qualification choice clause (verbatim);
  S2  sigma (x->y->z->x) is a proper cubic rotation: GL(3,Z), det +1,
      order 3, orthogonal, nearest-neighbor preserving;
  S3  sigma maps the hw=1 corner momentum set to itself cyclically and
      matches the carrier relabeling;
  S4  exact intertwining C^{-1} T_mu C = T_{sigma^{-1}(mu)} and joint
      tau-table equivariance;
  S5  exhaustive word sweep: every word in {T_1,T_2,T_3,C,C^2} up to
      length 4 has sigma-covariant labeled readout; conjugation
      multiplicativity gives the extension to all words;
  S6  a sigma-invariant function on the transitive corner orbit is
      constant, so no derivable selector fixes a bijection;
  S7  negative control: an added C_3-breaking operator is NOT
      sigma-covariant;
  S8  the labeling no-go note states the invariant this bridge supports.

No check passes by literal stipulation. Expected: PASS=N FAIL=0.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
MEMO_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NO_GO_PATH = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"


class Scorecard:
    def __init__(self) -> None:
        self.passes: list[str] = []
        self.fails: list[str] = []

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        msg = f"  {'PASS' if ok else 'FAIL'}  {label}"
        if detail:
            msg += f" :: {detail}"
        print(msg)
        (self.passes if ok else self.fails).append(label)

    def summary(self) -> int:
        print("\n=== SCORECARD ===")
        print(f"  PASS={len(self.passes)} FAIL={len(self.fails)}")
        for f in self.fails:
            print(f"  FAILED: {f}")
        return 0 if not self.fails else 1


def main() -> int:
    sc = Scorecard()
    print("=== A_min joint-C3 automorphism / selector-invariance bridge ===\n")

    # ------------------------------------------------------------------ S1
    print("[S1] axiom memo verbatim surface\n")
    memo = MEMO_PATH.read_text(encoding="utf-8")
    for quote in [
        "standard translations, and proper cubic rotations",
        "No site is privileged. Sites are distinguished by the supplied "
        "lattice structure alone.",
        "covariant under lattice\ntranslations and proper cubic rotations",
        "No possibility is privileged.",
        "a law may not\ndepend on a choice not fixed by the supplied "
        "structure, unless that choice is\nadmitted",
    ]:
        flat = " ".join(quote.split())
        memo_flat = " ".join(memo.split())
        sc.check(
            f"memo supplies (verbatim): '{flat[:64]}...'",
            flat in memo_flat,
        )
    # Record axiom is stated without any axis reference:
    record_block = memo.split("### Record / Fixed Reality")[1].split("##")[0]
    sc.check(
        "Record axiom text carries no axis reference",
        all(tok not in record_block for tok in ["x-axis", "y-axis", "z-axis", "T_1", "T_2", "T_3", "axis"]),
    )

    # ------------------------------------------------------------------ S2
    print("\n[S2] sigma is a proper cubic rotation of Z^3\n")
    # sigma: x -> y -> z -> x as a matrix on coordinates (e_x -> e_y etc.)
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    sc.check("P is integer with det = +1 (proper, in GL(3,Z))", P.det() == 1)
    sc.check("P is orthogonal (P^T P = I)", sp.simplify(P.T * P - I3) == sp.zeros(3, 3))
    sc.check("P has order 3 (P^3 = I, P != I)", P**3 == I3 and P != I3)
    # nearest-neighbor steps are permuted among themselves:
    steps = [sp.Matrix([1, 0, 0]), sp.Matrix([-1, 0, 0]),
             sp.Matrix([0, 1, 0]), sp.Matrix([0, -1, 0]),
             sp.Matrix([0, 0, 1]), sp.Matrix([0, 0, -1])]
    mapped = [P * s for s in steps]
    sc.check(
        "P permutes the 6 nearest-neighbor steps (adjacency preserved)",
        sorted(map(tuple, (tuple(m) for m in mapped))) == sorted(map(tuple, (tuple(s) for s in steps))),
    )
    # P fixes the [111] direction (it is the C_3[111] rotation):
    v111 = sp.Matrix([1, 1, 1])
    sc.check("P fixes [1,1,1] (rotation about the body diagonal)", P * v111 == v111)

    # ------------------------------------------------------------------ S3
    print("\n[S3] corner action matches the carrier relabeling\n")
    sigma = {1: 2, 2: 3, 3: 1}
    corners = {1: sp.Matrix([sp.pi, 0, 0]), 2: sp.Matrix([0, sp.pi, 0]), 3: sp.Matrix([0, 0, sp.pi])}
    ok = all(P * corners[alpha] == corners[sigma[alpha]] for alpha in [1, 2, 3])
    sc.check("P maps corner momentum k_alpha to k_sigma(alpha) for all alpha", ok)
    hw1_set = sorted(tuple(corners[a]) for a in corners)
    hw1_mapped = sorted(tuple(P * corners[a]) for a in corners)
    sc.check("P maps the hw=1 corner momentum set to itself", hw1_set == hw1_mapped)

    # ------------------------------------------------------------------ S4
    print("\n[S4] exact carrier intertwining\n")
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    tau = {1: {1: -1, 2: 1, 3: 1}, 2: {1: 1, 2: -1, 3: 1}, 3: {1: 1, 2: 1, 3: -1}}
    T = {mu: sp.diag(tau[1][mu], tau[2][mu], tau[3][mu]) for mu in [1, 2, 3]}
    sigma_inv = {v: k for k, v in sigma.items()}
    for mu in [1, 2, 3]:
        sc.check(
            f"C^-1 T_{mu} C = T_{sigma_inv[mu]} (= T_sigma^-1({mu})) exactly",
            C.inv() * T[mu] * C == T[sigma_inv[mu]],
        )
    sc.check(
        "joint tau-table equivariance: tau^sigma(a)_sigma(m) = tau^a_m for all a, m",
        all(tau[sigma[a]][sigma[m]] == tau[a][m] for a in [1, 2, 3] for m in [1, 2, 3]),
    )

    # ------------------------------------------------------------------ S5
    print("\n[S5] exhaustive word sweep (length <= 4) + homomorphism extension\n")
    # Generators of the derived operator structure on the carrier, and the
    # axis-relabeled generators. Phi relabels: T_mu -> T_sigma(mu), C -> C.
    gens = {"T1": T[1], "T2": T[2], "T3": T[3], "C": C, "C2": C * C}
    gens_relabeled = {"T1": T[sigma[1]], "T2": T[sigma[2]], "T3": T[sigma[3]], "C": C, "C2": C * C}
    # Intertwining at generator level: relabeled(g) = C g C^{-1} for each g.
    gen_intertwined = all(
        gens_relabeled[k] == C * gens[k] * C.inv() for k in gens
    )
    sc.check(
        "generator-level intertwining: Phi(g) = C g C^-1 for every generator (T_mu and C alike)",
        gen_intertwined,
    )
    sc.check(
        "homomorphism extension: conjugation is multiplicative, so Phi(w) = C w C^-1 for EVERY word w",
        gen_intertwined
        and all(
            C * (gens[k1] * gens[k2]) * C.inv() == (C * gens[k1] * C.inv()) * (C * gens[k2] * C.inv())
            for k1 in gens for k2 in gens
        ),
    )
    # Exhaustive sweep: every word up to length 4, labeled readout profile
    # (diagonal in the corner basis) is sigma-covariant:
    #   diag(Phi(w))[sigma(alpha)] == diag(w)[alpha].
    n_words = 0
    sweep_ok = True
    for length in range(1, 5):
        for combo in itertools.product(gens.keys(), repeat=length):
            w = I3
            w_rel = I3
            for k in combo:
                w = w * gens[k]
                w_rel = w_rel * gens_relabeled[k]
            for alpha in [1, 2, 3]:
                if sp.simplify(w_rel[sigma[alpha] - 1, sigma[alpha] - 1] - w[alpha - 1, alpha - 1]) != 0:
                    sweep_ok = False
            n_words += 1
    sc.check(
        "word sweep: labeled readout of every word (length <= 4) is sigma-covariant",
        sweep_ok,
        detail=f"{n_words} words checked",
    )

    # ------------------------------------------------------------------ S6
    print("\n[S6] selector consequence on the transitive orbit\n")
    # sigma acts transitively on {1,2,3}:
    orbit = {1}
    for _ in range(3):
        orbit |= {sigma[x] for x in orbit}
    sc.check("sigma is transitive on the corner index set", orbit == {1, 2, 3})
    # A sigma-invariant function f (f(sigma(a)) = f(a)) on a transitive orbit
    # is constant. Verified exhaustively over all functions {1,2,3} -> {1,2,3}:
    invariant_fns = [
        f for f in itertools.product([1, 2, 3], repeat=3)
        if all(f[sigma[a] - 1] == f[a - 1] for a in [1, 2, 3])
    ]
    sc.check(
        "every sigma-invariant function on the orbit is constant (exhaustive over 27 functions)",
        all(len(set(f)) == 1 for f in invariant_fns) and len(invariant_fns) == 3,
        detail=f"invariant functions found: {invariant_fns}",
    )
    sc.check(
        "hence no sigma-invariant (A_min-derivable) selector fixes a bijection to a labeled 3-set",
        all(len(set(f)) < 3 for f in invariant_fns),
    )
    # pi_A vs pi_B are sigma-related:
    pi_A = {1: 1, 2: 2, 3: 3}
    pi_B = {a: pi_A[sigma[a]] for a in [1, 2, 3]}
    sc.check("pi_B = pi_A o sigma and pi_B != pi_A (the no-go's counter-model pair)", pi_B != pi_A)

    # ------------------------------------------------------------------ S7
    print("\n[S7] negative control\n")
    H_break = sp.diag(1, 0, 0)
    sc.check(
        "negative control: added C_3-breaking H_break = diag(1,0,0) is NOT a fixed point of the joint action",
        not (C * H_break * C.inv() == H_break),
        detail="conjugation moves it; only ADDED (admitted) structure can break the orbit",
    )
    sc.check(
        "negative control sanity: H_break's labeled readout profile is non-constant (it would select)",
        len({H_break[i, i] for i in range(3)}) > 1,
    )

    # ------------------------------------------------------------------ S8
    print("\n[S8] consumer linkage\n")
    no_go = NO_GO_PATH.read_text(encoding="utf-8")
    sc.check(
        "labeling no-go states the orbit-equivariance invariant this bridge supports",
        "orbit-equivariance invariant" in no_go,
    )
    sc.check(
        "labeling no-go names the P1/P2/P3 closure surface (the admitted routes outside this bridge's scope)",
        "P1" in no_go and "P2" in no_go and "P3" in no_go,
    )

    return sc.summary()


if __name__ == "__main__":
    raise SystemExit(main())
