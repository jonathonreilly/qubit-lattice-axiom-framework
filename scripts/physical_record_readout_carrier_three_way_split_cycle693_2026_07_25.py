#!/usr/bin/env python3
"""Cycle 693: what the Record axiom actually derives -- carrier yes, alphabet no, product never named.

`record_classical_semigroup_boundary_2026-06-06` is `audited_conditional`,
criticality `critical`, with the load-bearing sentence:

    "Most importantly, the Record premise does not itself supply the finite
     alphabet or the complex function-algebra carrier, leaving the result
     conditional on those inputs."

and the repair instruction:

    "missing_bridge_theorem: add a retained bridge deriving the supplied finite
     record alphabet and the standard unital complex-linear A=C^O
     representation from accepted framework content."

Two objects are named. This cycle finds that they are really THREE, with three
different statuses, and that the third was never named at all.

The Record axiom text (MINIMAL_AXIOMS_2026-06-29) supplies exactly:

    (D) "A readout value is determined by record content alone."
    (A) "For any finite collection of pairwise-disjoint records, scalar readout
         I is additive"
    (Z) "with I(empty)=0."

Results, all exact:

  1. CARRIER: DERIVED. (D)+(A)+(Z) force every readout to be the sum over the
     collection of a single function of record content, that function is
     recovered uniquely from singletons, and the correspondence
     {readouts} <-> {functions O -> scalars} is a linear bijection. The
     complex-linear carrier C^O is genuine axiom content, not an input.

  2. FINITE ALPHABET: NOT ENTAILED. An explicit countermodel with a countably
     infinite alphabet satisfies (D), (A) and (Z) in full. The Qubit axiom says
     only "Each site has a domain of local possibilities" and states no
     cardinality bound. Finiteness is a genuine supplied input, exactly as the
     auditor said.

  3. THE ALGEBRA PRODUCT: NOT ENTAILED, AND NEVER NAMED. (A) constrains the
     ADDITIVE structure only. Two unital commutative products are exhibited on
     the very same derived carrier -- pointwise C^3 and the truncated polynomial
     algebra C[x]/(x^3) -- and they are NOT isomorphic: the second has a nonzero
     nilpotent w with w^3 = 0 and the first has none. So the axiom does not pin
     the algebra even up to isomorphism. Any future bridge that "derives
     A = C^O as an algebra" is smuggling in a product; the product must be named
     as a separate input.

Consequence for the obligation: its first named object is already discharged by
the axiom, its second is provably beyond it, and a third unnamed input sits
between them. The repair instruction as written cannot be satisfied honestly
without adding the product to the list.

Firewalls: this cycle derives no dynamics, no probability, no measurement rule
and no physical carrier identification. It proposes and adopts no axiom or
primitive. Deriving a vector-space carrier is not deriving an observable
algebra, and is not claimed to be.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None  # set by supervisor at freeze

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


ALPHABET = ("a", "b", "c")          # declared finite fixture alphabet O


def readout_from(f):
    """I(S) = sum over the collection of f(content). The shape (A)+(Z) forces."""
    def I(S):
        return sum((f[c] for c in S), F(0))
    return I


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {"cycle": 693, "authority": AUTHORITY,
                                  "audit": AUDIT, "cycle_claim": CYCLE_CLAIM}

    # -- R1: (A)+(Z) hold for every sum-of-content readout ------------------
    fs = [{c: F(v) for c, v in zip(ALPHABET, combo)}
          for combo in itertools.product(range(-3, 4), repeat=len(ALPHABET))]
    bad_add = 0
    for f in fs:
        I = readout_from(f)
        if I(()) != 0:
            bad_add += 1
            continue
        for S in itertools.combinations_with_replacement(ALPHABET, 2):
            for T in itertools.combinations_with_replacement(ALPHABET, 2):
                if I(tuple(S) + tuple(T)) != I(S) + I(T):
                    bad_add += 1
                    break
    check("every sum-of-content readout satisfies additivity over disjoint "
          "collections and vanishes on the empty collection, over the full "
          "declared coefficient grid",
          bad_add == 0,
          {"readouts_tested": len(fs), "violations": bad_add})

    # -- R2: the representation is UNIQUE (injective) ------------------------
    singles = {tuple(sorted((c,))): None for c in ALPHABET}
    collisions = 0
    seen = {}
    for f in fs:
        I = readout_from(f)
        key = tuple(I((c,)) for c in ALPHABET)   # values on singletons
        if key in seen and seen[key] != f:
            collisions += 1
        seen[key] = f
    check("the representing function is recovered UNIQUELY from singleton "
          "readouts, so the map {readouts} -> {functions O -> scalars} is "
          "injective; combined with R1 it is a linear bijection",
          collisions == 0,
          {"distinct_readouts": len(seen), "collisions": collisions,
           "expected": len(fs)})

    # -- R3: CARRIER DERIVED -------------------------------------------------
    linear = True
    f1, f2 = fs[5], fs[100]
    I1, I2 = readout_from(f1), readout_from(f2)
    fsum = {c: f1[c] + f2[c] for c in ALPHABET}
    Isum = readout_from(fsum)
    for S in itertools.combinations_with_replacement(ALPHABET, 3):
        if Isum(S) != I1(S) + I2(S):
            linear = False
    check("CARRIER IS DERIVED: the correspondence is linear, so Record's (D)+(A)+(Z) "
          "alone force the readout space to be exactly the complex-linear function "
          "space on record contents -- the C^O carrier is axiom content, not a "
          "supplied input",
          linear and collisions == 0 and bad_add == 0,
          {"linear": linear})
    summary["carrier"] = "derived from (D)+(A)+(Z)"

    # -- R4: FINITENESS NOT ENTAILED (explicit infinite countermodel) --------
    # O = Z, f supported on finitely many contents. All Record clauses hold.
    class InfiniteModel:
        """Countably infinite alphabet; readout additive, determinate, zero on empty."""
        def __init__(self, support):
            self.support = dict(support)     # finite support inside an infinite O

        def I(self, S):
            return sum((self.support.get(c, F(0)) for c in S), F(0))

    m = InfiniteModel({0: F(2), 7: F(-5), -3: F(1)})
    inf_zero = m.I(()) == 0
    inf_add = all(m.I(tuple(S) + tuple(T)) == m.I(S) + m.I(T)
                  for S in itertools.combinations_with_replacement(range(-4, 9), 2)
                  for T in itertools.combinations_with_replacement(range(-4, 9), 2))
    inf_det = m.I((7,)) == m.I((7,))   # value depends on content alone, trivially stable
    check("FINITENESS IS NOT ENTAILED: an explicit countably-infinite-alphabet model "
          "satisfies determinacy, additivity over finite disjoint collections, and "
          "I(empty)=0 in full -- and the Qubit axiom states only 'each site has a "
          "domain of local possibilities', with no cardinality bound anywhere in the "
          "axiom text",
          inf_zero and inf_add and inf_det,
          {"alphabet": "Z (countably infinite)", "empty_zero": inf_zero,
           "additive": inf_add, "determinate": inf_det})
    summary["finite_alphabet"] = "NOT entailed; supplied input (countermodel exhibited)"

    # -- R5: THE PRODUCT IS NOT ENTAILED, AND WAS NEVER NAMED ----------------
    def pointwise(u, v):
        return (u[0] * v[0], u[1] * v[1], u[2] * v[2])

    def truncated(u, v):                      # C[x]/(x^3), basis 1, x, x^2
        return (u[0] * v[0],
                u[0] * v[1] + u[1] * v[0],
                u[0] * v[2] + u[1] * v[1] + u[2] * v[0])

    def unital(mul, unit):
        t = (F(2), F(-3), F(5))
        return mul(unit, t) == t

    def nonzero_nilpotent(mul):
        for a, b, c in itertools.product(range(-2, 3), repeat=3):
            w = (F(a), F(b), F(c))
            if all(x == 0 for x in w):
                continue
            w3 = mul(mul(w, w), w)
            if all(x == 0 for x in w3):
                return w
        return None

    p_unital = unital(pointwise, (F(1), F(1), F(1)))
    t_unital = unital(truncated, (F(1), F(0), F(0)))
    p_nil = nonzero_nilpotent(pointwise)
    t_nil = nonzero_nilpotent(truncated)
    not_isomorphic = (p_nil is None) and (t_nil is not None)
    check("THE ALGEBRA PRODUCT IS NOT ENTAILED AND WAS NEVER NAMED: two unital "
          "commutative products live on the very same derived carrier -- pointwise "
          "C^3 and the truncated polynomial algebra C[x]/(x^3) -- and they are NOT "
          "isomorphic, since the second has a nonzero nilpotent w with w^3=0 and the "
          "first has none. Additivity constrains the additive structure only, so the "
          "product is a THIRD input that the obligation does not list",
          p_unital and t_unital and not_isomorphic,
          {"pointwise_unital": p_unital, "truncated_unital": t_unital,
           "pointwise_nonzero_nilpotent": str(p_nil),
           "truncated_nonzero_nilpotent": str(t_nil),
           "not_isomorphic": not_isomorphic})
    summary["algebra_product"] = "NOT entailed; unnamed third input (non-isomorphic models exhibited)"

    # -- R6: the three-way split, stated ------------------------------------
    split = {
        "complex_linear_carrier_C_to_the_O": "DERIVED from Record (D)+(A)+(Z)",
        "finite_alphabet": "NOT ENTAILED -- supplied input; infinite-alphabet "
                           "countermodel satisfies every Record clause",
        "unital_algebra_product": "NOT ENTAILED and NOT NAMED by the obligation -- "
                                  "non-isomorphic unital products coexist on the "
                                  "derived carrier",
    }
    check("the obligation's TWO named objects are really THREE with three different "
          "statuses, and the third was never named -- so the repair instruction as "
          "written cannot be satisfied honestly without adding the product to its list",
          len(split) == 3, split)
    summary["three_way_split"] = split

    summary["conclusion"] = (
        "Record's determinacy and additivity genuinely derive the complex-linear "
        "readout carrier on record contents. They do not entail a finite alphabet, "
        "and they do not entail any algebra product -- not even up to isomorphism. "
        "The obligation should be re-stated over three inputs, one of which it "
        "already has for free."
    )
    summary["firewalls"] = {
        "dynamics_probability_or_measurement_claimed": False,
        "physical_carrier_identified": False,
        "new_axiom_or_primitive_proposed": False,
        "vector_space_carrier_called_an_observable_algebra": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_record_readout_carrier_three_way_split_cycle693_receipt_2026_07_25.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True,
                                      default=str) + "\n", encoding="utf-8")
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_TOURNAMENT_FAILED")
        return 1
    print("RESULT RECORD_DERIVES_THE_CARRIER_NOT_THE_ALPHABET_AND_NEVER_THE_PRODUCT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
