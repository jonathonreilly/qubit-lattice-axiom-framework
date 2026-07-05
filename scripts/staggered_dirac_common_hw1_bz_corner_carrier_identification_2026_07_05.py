"""Runner for the common hw=1 BZ-corner carrier identification bridge
(2026-07-05).

One concrete carrier — the finite periodic 2x2x2 framework representative
(C^8 site space, commuting translation unitaries U_mu, BZ-corner character
basis) — simultaneously realizes:

  K1  the construction itself (commuting order-2 permutation unitaries,
      +/-1 joint character eigenvalues);
  K2  (I1) the abstract Hamming hw grading and S_3/C_3 orbit facts of the
      substep3 bz-corner note, via the bijection k -> b(k) = k/pi;
  K3  (I2) the abstract AC_lambda triple (V_3, tau): U_mu restricted to the
      hw=1 character span IS the tau table (2a)-(2c), matrix-identically,
      with pairwise-distinct triples and diagonal commutant C^3;
  K4  (I3) the C_3[111] site rotation R: R U_mu R^-1 = U_sigma(mu) exactly,
      R preserves V and acts on the ordered character basis as the cyclic
      generator (regular Z/3 action);
  K5  consumed-scope text checks (AC_lambda out-of-scope disclaimer;
      momentum-type transitivity; species-reduction R4/R5 boundaries);
  K6  negative control: hw=2 is a distinct orbit, not blurred into V.

No check passes by literal stipulation. Expected: PASS=N FAIL=0.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AC_LAMBDA_PATH = DOCS / "STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md"
MOMENTUM_TYPE_PATH = DOCS / "FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md"
SPECIES_REDUCTION_PATH = DOCS / "STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
HAMMING_PATH = DOCS / "STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md"


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


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    sc = Scorecard()
    print("=== common hw=1 BZ-corner carrier identification ===\n")

    # ------------------------------------------------------------------ K1
    print("[K1] the concrete carrier\n")
    sites = list(itertools.product([0, 1], repeat=3))
    idx = {s: i for i, s in enumerate(sites)}

    def U(mu: int) -> sp.Matrix:
        M = sp.zeros(8, 8)
        for s in sites:
            t = list(s)
            t[mu] = (t[mu] + 1) % 2
            M[idx[s], idx[tuple(t)]] = 1  # (U f)(x) = f(x + e_mu)
        return sp.Matrix(M)

    Us = [U(0), U(1), U(2)]
    I8 = sp.eye(8)
    for mu in range(3):
        sc.check(f"U_{mu+1} is a permutation unitary of order 2", Us[mu] * Us[mu] == I8 and Us[mu].T * Us[mu] == I8)
    sc.check(
        "translations commute pairwise",
        all(Us[a] * Us[b] == Us[b] * Us[a] for a in range(3) for b in range(3)),
    )

    corners = list(itertools.product([0, 1], repeat=3))  # b(k) = k/pi

    def chi(b) -> sp.Matrix:
        return sp.Matrix([(-1) ** sum(bb * xx for bb, xx in zip(b, x)) for x in sites])

    char_ok = all(
        Us[mu] * chi(b) == ((-1) ** b[mu]) * chi(b) for b in corners for mu in range(3)
    )
    sc.check("every character chi_k is a joint eigenvector with eigenvalue e^{i k_mu} = (-1)^{b_mu}", char_ok)
    G = sp.Matrix([[ (chi(b1).T * chi(b2))[0, 0] for b2 in corners] for b1 in corners])
    sc.check("the 8 characters are orthogonal (complete joint basis)", G == 8 * sp.eye(8))

    # ------------------------------------------------------------------ K2
    print("\n[K2] (I1) Hamming leg\n")
    hw = {b: sum(b) for b in corners}
    levels = {k: sorted(b for b in corners if hw[b] == k) for k in range(4)}
    sc.check(
        "grading (|L_0|,|L_1|,|L_2|,|L_3|) = (1,3,3,1) on the concrete corner set",
        [len(levels[k]) for k in range(4)] == [1, 3, 3, 1],
    )
    sc.check(
        "hw=1 level = the three corner momenta {(pi,0,0),(0,pi,0),(0,0,pi)} (as bits)",
        levels[1] == [(0, 0, 1), (0, 1, 0), (1, 0, 0)],
    )
    perms = list(itertools.permutations([0, 1, 2]))
    sc.check(
        "S_3 coordinate action preserves hw on the concrete corners",
        all(hw[tuple(b[p[i]] for i in range(3))] == hw[b] for b in corners for p in perms),
    )
    sc.check(
        "S_3 is transitive on the concrete hw=1 level",
        all(
            any(tuple(b[p[i]] for i in range(3)) == b2 for p in perms)
            for b in levels[1] for b2 in levels[1]
        ),
    )

    # ------------------------------------------------------------------ K3
    print("\n[K3] (I2) AC_lambda leg\n")
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # ordered basis (c_1, c_2, c_3)
    tau = {a: {m: (-1 if m == a else 1) for m in range(3)} for a in range(3)}
    # U_mu restricted to V in the ordered character basis:
    restr = {mu: sp.diag(*[(-1) ** b[mu] for b in hw1]) for mu in range(3)}
    T_abstract = {mu: sp.diag(*[tau[a][mu] for a in range(3)]) for mu in range(3)}
    sc.check(
        "U_mu|_V = T_mu matrix-identically against eq (2a)-(2c) for all mu",
        all(restr[mu] == T_abstract[mu] for mu in range(3)),
    )
    triples = [tuple((-1) ** b[mu] for mu in range(3)) for b in hw1]
    sc.check(
        "the three joint eigenvalue triples are pairwise distinct",
        len(set(triples)) == 3,
        detail=f"triples = {triples}",
    )
    # commutant of {U_mu|_V} inside M_3 via nullspace of the stacked
    # commutator maps:
    Lbig = sp.zeros(27, 9)
    for mu in range(3):
        for a_ in range(3):
            for b_ in range(3):
                Eab = sp.zeros(3, 3)
                Eab[a_, b_] = 1
                comm = Eab * restr[mu] - restr[mu] * Eab
                for i in range(3):
                    for j in range(3):
                        Lbig[9 * mu + 3 * i + j, 3 * a_ + b_] = comm[i, j]
    ns = Lbig.nullspace()
    diag_only = all(
        all(sp.simplify(v[3 * i + j]) == 0 for i in range(3) for j in range(3) if i != j)
        for v in ns
    )
    sc.check(
        "commutant of {U_mu|_V} is exactly the diagonal algebra C^3 (dim 3, off-diagonals vanish)",
        len(ns) == 3 and diag_only,
        detail=f"commutant dim = {len(ns)}",
    )

    # ------------------------------------------------------------------ K4
    print("\n[K4] (I3) C_3 action leg\n")
    R = sp.zeros(8, 8)
    for s in sites:
        t = (s[2], s[0], s[1])  # cyclic coordinate rotation of the site
        R[idx[t], idx[s]] = 1
    R = sp.Matrix(R)
    sig = {0: 1, 1: 2, 2: 0}
    sc.check(
        "R U_mu R^-1 = U_sigma(mu) exactly for all mu",
        all(R * Us[mu] * R.inv() == Us[sig[mu]] for mu in range(3)),
    )
    # R maps the hw=1 characters cyclically: chi_(pi,0,0)->chi_(0,pi,0)->chi_(0,0,pi)->...
    images = []
    for a, b in enumerate(hw1):
        w = R * chi(b)
        match = [c for c, b2 in enumerate(hw1) if w == chi(b2)]
        images.append(match[0] if match else None)
    sc.check(
        "R preserves V and acts on the ordered character basis as the cyclic shift (c_1->c_2->c_3->c_1)",
        images == [1, 2, 0],
        detail=f"basis images = {images}",
    )
    C3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Rv = sp.zeros(3, 3)
    for a in range(3):
        Rv[images[a], a] = 1
    sc.check("R|_V equals the cyclic generator C of the abstract notes", sp.Matrix(Rv) == C3)
    sc.check(
        "the action is a regular Z/3: order 3 and no fixed basis vector",
        Rv**3 == sp.eye(3) and all(Rv[a, a] == 0 for a in range(3)),
    )

    # ------------------------------------------------------------------ K5
    print("\n[K5] consumed-scope text checks\n")
    ac = flat(AC_LAMBDA_PATH.read_text(encoding="utf-8"))
    sc.check(
        "AC_lambda note's own out-of-scope disclaimer present (the gap this bridge closes)",
        "make **no** claim that the framework's hw=1 carrier on the physical lattice substrate IS this 3-dim complex space"
        in ac,
    )
    mom = flat(MOMENTUM_TYPE_PATH.read_text(encoding="utf-8"))
    sc.check(
        "momentum-type note records distinct joint translation characters on the three hw=1 corners",
        "the three `hw=1` corners have distinct joint translation characters" in mom,
    )
    sc.check(
        "momentum-type note records the transitive C_3 permutation",
        "permutes them transitively" in mom,
    )
    spr = flat(SPECIES_REDUCTION_PATH.read_text(encoding="utf-8"))
    sc.check(
        "species-reduction (R4) boundary verbatim: taste factor not forced",
        "is **not** forced by the cited upstream" in spr,
    )
    sc.check(
        "species-reduction (R5) boundary verbatim: reduction realization not derived",
        "is **not** the same as a derivation that the framework's specific staggered-Dirac realization implements"
        in spr,
    )
    ham = flat(HAMMING_PATH.read_text(encoding="utf-8"))
    sc.check(
        "Hamming note supplies the abstract grading (1, 3, 3, 1)",
        "(1, 3, 3, 1)" in ham,
    )

    # ------------------------------------------------------------------ K6
    print("\n[K6] negative control\n")
    sc.check(
        "hw=2 level is a distinct 3-element set, disjoint from the hw=1 corner set",
        len(levels[2]) == 3 and not set(levels[2]) & set(levels[1]),
    )
    sc.check(
        "hw=2 characters carry a DIFFERENT eigenvalue pattern (two -1 components each)",
        all(sum(1 for mu in range(3) if (-1) ** b[mu] == -1) == 2 for b in levels[2]),
    )

    return sc.summary()


if __name__ == "__main__":
    raise SystemExit(main())
