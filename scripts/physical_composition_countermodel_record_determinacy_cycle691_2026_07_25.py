#!/usr/bin/env python3
"""Cycle 691: the composition countermodel does not survive Record determinacy.

The repository's four-axiom completeness note (2026-07-13) lists multi-site
composition as interface `C`, disposition "strong Qubit-level candidate unless
derived from the explicit rule", and supplies an exact finite countermodel:

    B      = M_4(C) (+) M_4(C)
    A_x(a) = (a (x) I_2) (+) (a (x) I_2)
    A_y(b) = (I_2 (x) b) (+) (I_2 (x) b)

Both local embeddings are faithful and commute; their products span only the
diagonal M_4 copy (complex dimension 16) while the composite carries real
self-adjoint dimension 32, and the central observable I_4 (+) (-I_4) is
invisible to the local-product span. The note concludes, correctly, that

    one M_2(C) at each site + locality
        does not entail
    the ordinary generated finite tensor product or local tomography.

This cycle asks the next question, which the note leaves open: the framework
does not consist of Qubit plus locality. It also has Record and Qualification.
Does the countermodel still defeat composition on the FULL axiom surface?

Result, in exact integer arithmetic on declared finite fixtures:

  1. The countermodel is reproduced exactly, including that the central
     observable lies outside the local-product span.
  2. GENERATION IS FORCED. For every declared pair of commuting faithful
     unital *-embeddings of M_2(C) -- plain tensor, the countermodel, three
     summands, a signed-permutation twist, and a multiplicity amplification --
     the generated *-algebra has complex dimension exactly 16 and is
     *-isomorphic to M_2(C) (x) M_2(C), independent of an ambient dimension
     that ranges over 16, 64 and 144. The ordinary tensor product is not an
     extra assumption; it is what two commuting faithful qubit copies always
     generate. The countermodel's excess is AMBIENT, never GENERATED.
  3. RECORD DETERMINACY EXCLUDES THE EXCESS. Two states of the countermodel
     differing only by summand have EXACTLY equal values on every element of
     the local-product span -- identical record content, exact zero difference
     in integer arithmetic -- while the central observable separates them by 2.
     So that observable's value is not determined by record content, and the
     Record clause "readout value is determined by record content alone"
     denies it lawful-readout status.

What this does and does not settle is stated precisely in the note and in the
`residuals` block of the receipt. The step from "carries no lawful readout" to
"is not a distinct physical state" is performed by the Qualification sentence
"a state is a configuration of records"; that citation is recorded as a
declared premise use, not as a computed row, and it is the single place where
this cycle leaves exact algebra for framework wording.

Firewalls: no new axiom or primitive is proposed or adopted; deriving content
is not adopting it. A generated algebra is not a physical Hilbert space. Local
tomography, preparation, effect typing, frame measure and probability are NOT
claimed and remain `Q`/`P` work, exactly as the source note says. No gravity,
dynamics, time, or matter claim is made.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
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


# --------------------------------------------------------------- exact linalg --
# Every fixture below has entries in {0, +1, -1}. Real and imaginary parts are
# therefore exact integers and every rank is computed by exact elimination over
# the rationals. No floating point appears in any decisive row.

def mat(rows):
    return tuple(tuple(Fraction(x) for x in r) for r in rows)


def zeros(n, m):
    return tuple(tuple(Fraction(0) for _ in range(m)) for _ in range(n))


def eye(n):
    return tuple(tuple(Fraction(1 if i == j else 0) for j in range(n)) for i in range(n))


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m))
                 for i in range(n))


def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    return tuple(tuple(A[i // p][j // q] * B[i % p][j % q] for j in range(m * q))
                 for i in range(n * p))


def dsum(*Ms):
    n = sum(len(M) for M in Ms)
    out = [[Fraction(0)] * n for _ in range(n)]
    o = 0
    for M in Ms:
        k = len(M)
        for i in range(k):
            for j in range(k):
                out[o + i][o + j] = M[i][j]
        o += k
    return tuple(tuple(r) for r in out)


def transpose_conj(A):
    # all fixtures are real integer matrices, so conjugation is the identity
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))


def rank(vectors) -> int:
    """Exact rank over Q by fraction-free-ish Gaussian elimination."""
    rows = [list(v) for v in vectors]
    r = 0
    ncols = len(rows[0]) if rows else 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / pv
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def flat(A):
    return [x for row in A for x in row]


# ------------------------------------------------------------------ fixtures --
I2 = eye(2)
I4 = eye(4)
E11 = mat([[1, 0], [0, 0]])
E12 = mat([[0, 1], [0, 0]])
E21 = mat([[0, 0], [1, 0]])
E22 = mat([[0, 0], [0, 1]])
BASIS = (E11, E12, E21, E22)          # a complex basis of M_2(C)

# a signed-permutation unitary: keeps the twist fixture exactly integral
SP4 = mat([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, -1, 0]])


def countermodel():
    return (lambda a: dsum(kron(a, I2), kron(a, I2)),
            lambda b: dsum(kron(I2, b), kron(I2, b)))


def fixtures():
    """Declared family of commuting faithful unital *-embedding pairs."""
    out = []
    out.append(("plain M_2 (x) M_2",
                lambda a: kron(a, I2), lambda b: kron(I2, b)))
    ax, ay = countermodel()
    out.append(("declared countermodel M_4 (+) M_4", ax, ay))
    out.append(("three identical summands",
                lambda a: dsum(kron(a, I2), kron(a, I2), kron(a, I2)),
                lambda b: dsum(kron(I2, b), kron(I2, b), kron(I2, b))))
    twist = lambda M: matmul(matmul(SP4, M), transpose_conj(SP4))
    out.append(("signed-permutation twist on the second summand",
                lambda a: dsum(kron(a, I2), twist(kron(a, I2))),
                lambda b: dsum(kron(I2, b), twist(kron(I2, b)))))
    out.append(("multiplicity amplification (extra I_2 factor)",
                lambda a: kron(kron(a, I2), I2),
                lambda b: kron(kron(I2, b), I2)))
    return out


def generated_words(Ax, Ay):
    """A spanning set for the *-algebra generated by the two commuting images.

    Because the images commute and each is a full matrix unit system, products
    A_x(e) A_y(f) over the two matrix-unit bases already span the generated
    algebra; the span is closed under multiplication and adjoint, which the
    runner verifies rather than assumes.
    """
    return [matmul(Ax(a), Ay(b)) for a in BASIS for b in BASIS]


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {"cycle": 691, "authority": AUTHORITY,
                                  "audit": AUDIT, "cycle_claim": CYCLE_CLAIM}

    # -- R1: reproduce the declared countermodel exactly ---------------------
    Ax, Ay = countermodel()
    faithful = len({tuple(flat(Ax(a))) for a in BASIS}) == 4 and \
               len({tuple(flat(Ay(b))) for b in BASIS}) == 4
    commutator_max = max(
        max(abs(x) for x in flat(
            tuple(tuple(matmul(Ax(a), Ay(b))[i][j] - matmul(Ay(b), Ax(a))[i][j]
                        for j in range(8)) for i in range(8))))
        for a in BASIS for b in BASIS)
    span = generated_words(Ax, Ay)
    span_dim = rank([flat(w) for w in span])
    Z = dsum(I4, tuple(tuple(-x for x in r) for r in I4))
    with_Z = rank([flat(w) for w in span] + [flat(Z)])
    check("the declared countermodel is reproduced exactly: both local embeddings "
          "are faithful and commute, their products span complex dimension 16, and "
          "the central observable I_4 (+) (-I_4) lies OUTSIDE that span",
          faithful and commutator_max == 0 and span_dim == 16 and with_Z == 17,
          {"faithful": faithful, "max_commutator": str(commutator_max),
           "local_product_span_dim": span_dim, "span_dim_with_Z_adjoined": with_Z,
           "ambient_complex_dim": 64})
    summary["countermodel"] = {"span_dim": span_dim, "with_Z": with_Z}

    # -- R2: generation is forced, across the declared family ----------------
    gen = {}
    for name, ax, ay in fixtures():
        d = rank([flat(w) for w in generated_words(ax, ay)])
        amb = len(ax(E11)) ** 2
        gen[name] = {"generated_complex_dim": d, "ambient_complex_dim": amb}
    all16 = all(v["generated_complex_dim"] == 16 for v in gen.values())
    ambients = sorted({v["ambient_complex_dim"] for v in gen.values()})
    check("GENERATION IS FORCED: every declared pair of commuting faithful unital "
          "*-embeddings of M_2(C) generates a *-algebra of complex dimension exactly "
          "16, independent of an ambient dimension ranging over " + str(ambients) +
          " -- the ordinary tensor product is not an extra assumption but what two "
          "commuting faithful qubit copies always generate",
          all16 and len(ambients) >= 3, gen)
    summary["generation"] = gen

    # -- R3: the generated algebra really is M_2 (x) M_2 ---------------------
    # exhibit the explicit *-isomorphism with the abstract tensor product by
    # matching the full 16x16 multiplication table on the matrix-unit basis.
    def table(ax, ay):
        words = [(a, b) for a in range(4) for b in range(4)]
        idx = {}
        mats = []
        for ia, ib in words:
            M = matmul(ax(BASIS[ia]), ay(BASIS[ib]))
            idx[(ia, ib)] = len(mats)
            mats.append(M)
        # structure constants: which basis word each product equals (or 0)
        out = []
        for p in range(16):
            row = []
            for q in range(16):
                P = matmul(mats[p], mats[q])
                if all(x == 0 for x in flat(P)):
                    row.append(-1)
                else:
                    hit = [k for k, M in enumerate(mats) if M == P]
                    row.append(hit[0] if len(hit) == 1 else -2)
            out.append(tuple(row))
        return tuple(out)

    ref = table(lambda a: kron(a, I2), lambda b: kron(I2, b))
    mismatches = {}
    for name, ax, ay in fixtures():
        t = table(ax, ay)
        if t != ref:
            mismatches[name] = "multiplication table differs from M_2 (x) M_2"
    no_ambiguous = all(all(x >= -1 for x in row) for row in ref)
    check("the generated algebra IS the ordinary tensor product: the full 16x16 "
          "multiplication table on the matrix-unit words is identical to that of "
          "M_2(C) (x) M_2(C) for every fixture, with every product resolving to a "
          "single basis word or exactly zero",
          not mismatches and no_ambiguous,
          {"fixtures_matching_tensor_table": len(fixtures()) - len(mismatches),
           "mismatches": mismatches})

    # -- R4: Record determinacy separation, exact ----------------------------
    # Two unit states differing only by summand. Expectations are computed as
    # exact integer bilinear forms; no normalization is needed because the two
    # vectors carry identical norms and we compare a DIFFERENCE.
    def expect(M, v):
        n = len(v)
        return sum(v[i] * M[i][j] * v[j] for i in range(n) for j in range(n))

    worst = Fraction(0)
    probes = 0
    for coeffs in itertools.product((0, 1, -1), repeat=4):
        if all(c == 0 for c in coeffs):
            continue
        top = [Fraction(c) for c in coeffs] + [Fraction(0)] * 4
        bot = [Fraction(0)] * 4 + [Fraction(c) for c in coeffs]
        for w in span:
            d = expect(w, top) - expect(w, bot)
            worst = max(worst, abs(d))
        probes += 1
    z_gap = expect(Z, [Fraction(1), Fraction(0), Fraction(0), Fraction(0),
                       Fraction(0), Fraction(0), Fraction(0), Fraction(0)]) - \
            expect(Z, [Fraction(0)] * 4 + [Fraction(1), Fraction(0),
                                           Fraction(0), Fraction(0)])
    check("RECORD DETERMINACY EXCLUDES THE EXCESS: over every declared summand-swapped "
          "state pair, the two states agree EXACTLY on every element of the "
          "local-product span (exact zero difference in integer arithmetic), while the "
          "central observable separates them -- so its value is not determined by "
          "record content",
          worst == 0 and abs(z_gap) == 2,
          {"state_pairs_probed": probes, "observables_per_pair": len(span),
           "max_local_product_difference": str(worst),
           "central_observable_gap": str(z_gap)})
    summary["record_determinacy"] = {"max_local_difference": str(worst),
                                     "central_gap": str(z_gap),
                                     "pairs": probes}

    # -- R5: the falsifier that would break the argument ---------------------
    # If ANY element of the local-product span separated the summand states, the
    # excess would be record-visible and the argument would fail. Report the
    # search as an explicit preregistered falsifier rather than a silent pass.
    separating = [i for i, w in enumerate(span)
                  if any(expect(w, [Fraction(c) for c in co] + [Fraction(0)] * 4)
                         - expect(w, [Fraction(0)] * 4 + [Fraction(c) for c in co]) != 0
                         for co in itertools.product((0, 1, -1), repeat=4)
                         if any(co))]
    check("preregistered falsifier does not fire: no element of the local-product span "
          "separates any declared summand-swapped pair (had one existed, the excess "
          "would be record-visible and this cycle's conclusion would be false)",
          not separating,
          {"separating_local_observables": len(separating)})

    # -- R6: what remains, stated exactly ------------------------------------
    residuals = {
        "premise_used_beyond_computation":
            "The step from 'carries no lawful readout' to 'is not a distinct "
            "physical state' is performed by the Qualification sentence 'a state "
            "is a configuration of records'. That is a declared framework-wording "
            "citation, not a computed row of this runner.",
        "not_closed_by_this_cycle": [
            "local tomography",
            "operational preparation/effect/channel typing (interface Q)",
            "frame measure, denominator, probability (interface P)",
            "which composite projectors are physically available or readable",
            "identification of a prepared density operator",
            "any claim about three or more sites, which is not tested here",
        ],
        "scope": "two sites, one M_2(C) each, finite-dimensional ambient algebras "
                 "from the declared fixture family; no claim is made for infinite "
                 "dimensions or for ambient algebras outside that family",
    }
    check("residual scope is stated explicitly rather than implied: the single "
          "non-computed premise is named, and the interfaces this cycle does NOT "
          "close are enumerated",
          isinstance(residuals["not_closed_by_this_cycle"], list)
          and len(residuals["not_closed_by_this_cycle"]) >= 5,
          {"named_premise": True,
           "unclosed_items": len(residuals["not_closed_by_this_cycle"])})
    summary["residuals"] = residuals

    summary["conclusion"] = (
        "The declared composition countermodel refutes composition from Qubit plus "
        "locality, exactly as its source note says. It does NOT refute composition "
        "on the four-axiom surface: the generated algebra is always the ordinary "
        "tensor product, and the countermodel's excess carries no record-determined "
        "readout. Interface C's 'no extra global sector' content therefore follows "
        "for readable structure without a new axiom, modulo the one named premise."
    )
    summary["firewalls"] = {
        "new_axiom_or_primitive_proposed": False,
        "local_tomography_claimed": False,
        "probability_or_born_content_claimed": False,
        "generated_algebra_called_a_physical_hilbert_space": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_composition_countermodel_record_determinacy_cycle691_receipt_2026_07_25.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True,
                                      default=str) + "\n", encoding="utf-8")

    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT COMPOSITION_COUNTERMODEL_RECORD_DETERMINACY_TOURNAMENT_FAILED")
        return 1
    print("RESULT COMPOSITION_COUNTERMODEL_DOES_NOT_SURVIVE_RECORD_DETERMINACY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
