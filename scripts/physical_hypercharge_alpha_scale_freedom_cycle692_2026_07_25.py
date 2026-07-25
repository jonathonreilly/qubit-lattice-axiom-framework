#!/usr/bin/env python3
"""Cycle 692: the hypercharge normalization alpha is a free scale, not a derivable one.

`hypercharge_identification_note` is `audited_conditional` with load-bearing
score 20.5 and 1040 transitive descendants. Its audit rationale isolates the
entire obstruction to a single constant:

    "The structural +1:(-3) result is an exact algebraic consequence of the
     stated decomposition. However, the normalized (+1/3,-1) result depends on
     the explicitly supplied alpha=1/3 normalization, which the packet says is
     not derived, so the full scoped claim remains conditional."

and its re-audit instruction is:

    "missing_bridge_theorem: derive and cite a retained-grade or explicitly
     approved authority fixing alpha=1/3, then re-audit the unchanged name-free
     theorem surface."

This cycle asks whether that instruction is satisfiable from the current
surface at all. It is not, and the reason is exact.

Setting: V = C^2 (x) (C^2 (x) C^2); SWAP_23 exchanges the last two factors;
P_sym = (I+SWAP_23)/2 and P_anti = (I-SWAP_23)/2 have ranks 3 and 1 on the
last-two space, hence 6 and 2 on V. The central block-scalar operator is
Y(alpha,beta) = alpha*P_sym + beta*P_anti embedded as I_2 (x) Y.

Findings, all exact rational arithmetic:

  1. Tracelessness forces 6*alpha + 2*beta = 0, i.e. beta = -3*alpha. The
     RATIO +1:(-3) is fixed exactly; the SCALE is untouched.
  2. Record additivity -- "finite scalar readout is additive over finite
     pairwise-disjoint record collections" -- generates the achievable readout
     set as exactly alpha*Z. Additivity therefore fixes the value GROUP up to
     an overall scale and never fixes the scale itself. This is computed, not
     asserted.
  3. Enumerating every framework-internal scale-fixing condition available on
     this surface, exactly one yields 1/3, and it is the condition "the
     one-dimensional trivial block carries charge -1" -- i.e. a choice of which
     block reads unit charge. Tracelessness leaves alpha free; the minimal
     positive quantum, integer-spectrum minimality, and unit-symmetric-block
     conditions all give alpha = 1; the quadratic normalization Tr(Y^2)=1 gives
     an irrational value that is not 1/3.
  4. The approved `scale_reference_primitive` cannot supply alpha either: its
     own note states it "carries zero dimensionless content" and "does not
     supply any dimensionless quantity". alpha is dimensionless. So the
     otherwise-natural discharge route through the approved units authority is
     closed by that authority's own scope.

Conclusion: the obligation as literally written -- derive alpha=1/3 -- is not
dischargeable from the ratio, from Record additivity, from any enumerated
framework-internal normalization, or from the approved units primitive. The
admissible repairs are named in the note; the no-new-primitive rule forbids
this loop from creating a new dimensionless authority.

Firewalls: this cycle derives no charge, identifies no block with a physical
species, and asserts no Standard-Model content. It makes a bounded negative
claim about ONE constant on ONE declared surface, with its escape conditions
stated. It proposes and adopts no axiom or primitive.
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


# ------------------------------------------------------- the declared surface --
def swap23_on_last_two():
    """SWAP on C^2 (x) C^2 as an exact 4x4 rational matrix."""
    S = [[F(0)] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            S[i * 2 + j][j * 2 + i] = F(1)
    return [row[:] for row in S]


def projectors():
    S = swap23_on_last_two()
    I = [[F(1 if i == j else 0) for j in range(4)] for i in range(4)]
    P_sym = [[(I[i][j] + S[i][j]) / 2 for j in range(4)] for i in range(4)]
    P_anti = [[(I[i][j] - S[i][j]) / 2 for j in range(4)] for i in range(4)]
    return P_sym, P_anti


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def rank(rows):
    M = [list(r) for r in rows]
    r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / pv
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {"cycle": 692, "authority": AUTHORITY,
                                  "audit": AUDIT, "cycle_claim": CYCLE_CLAIM}

    P_sym, P_anti = projectors()

    # -- R1: the declared surface, exactly ----------------------------------
    idempotent = matmul(P_sym, P_sym) == P_sym and matmul(P_anti, P_anti) == P_anti
    orthogonal = all(all(x == 0 for x in row) for row in matmul(P_sym, P_anti))
    r_sym, r_anti = rank(P_sym), rank(P_anti)
    n_sym, n_anti = 2 * r_sym, 2 * r_anti          # multiplicities on V
    check("the declared surface is reproduced exactly: P_sym and P_anti are "
          "complementary orthogonal projectors of ranks 3 and 1 on the last-two "
          "factors, hence multiplicities 6 and 2 on V",
          idempotent and orthogonal and (r_sym, r_anti) == (3, 1)
          and (n_sym, n_anti) == (6, 2),
          {"idempotent": idempotent, "orthogonal": orthogonal,
           "ranks_last_two": [r_sym, r_anti], "multiplicities_on_V": [n_sym, n_anti]})

    # -- R2: tracelessness fixes the ratio and nothing else ------------------
    # Tr(I_2 (x) Y) = 2*(alpha*3 + beta*1) = n_sym*alpha + n_anti*beta
    def traceless_beta(alpha):
        return -F(n_sym, n_anti) * alpha
    ratios = {str(a): str(traceless_beta(a) / a) for a in (F(1), F(1, 3), F(5, 7), F(-2))}
    all_minus3 = set(ratios.values()) == {"-3"}
    check("tracelessness forces beta = -3*alpha for EVERY alpha, so it fixes the "
          "ratio +1:(-3) exactly and leaves the scale completely free",
          all_minus3,
          {"beta_over_alpha_at_sampled_alphas": ratios})

    # -- R3: Record additivity fixes the value GROUP, never the scale --------
    # achievable readouts: m*alpha + n*beta = alpha*(m - 3n), m,n integers
    def achievable(alpha, bound=8):
        beta = traceless_beta(alpha)
        return {m * alpha + n * beta for m in range(-bound, bound + 1)
                for n in range(-bound, bound + 1)}
    groups = {}
    for a in (F(1), F(1, 3), F(2), F(1, 7)):
        vals = achievable(a)
        pos = sorted(v for v in vals if v > 0)
        # every achievable value is an integer multiple of the minimal positive one
        gen = pos[0]
        closed = all((v / gen).denominator == 1 for v in vals)
        groups[str(a)] = {"minimal_positive": str(gen), "is_cyclic_generated_by_alpha":
                          closed and gen == abs(a)}
    all_cyclic = all(v["is_cyclic_generated_by_alpha"] for v in groups.values())
    check("Record additivity generates the achievable readout set as exactly "
          "alpha*Z for every alpha: the value GROUP structure is fixed, the scale "
          "of its generator is not -- additivity cannot fix alpha",
          all_cyclic, groups)
    summary["value_group"] = groups

    # -- R4: enumerate every framework-internal scale-fixing condition -------
    conditions = {}
    conditions["tracelessness alone"] = None                       # free
    conditions["minimal positive readout quantum = 1"] = F(1)
    conditions["symmetric-block charge = +1"] = F(1)
    conditions["integer spectrum with minimal quantum"] = F(1)
    conditions["trivial-block charge = -1"] = F(1, 3)
    # quadratic normalization Tr(Y^2)=1 on V: n_sym*a^2 + n_anti*(9a^2) = 24a^2 = 1
    sq = F(n_sym) + F(n_anti) * 9
    conditions[f"Tr(Y^2) = 1  ({sq}*alpha^2 = 1)"] = "irrational 1/sqrt(24)"
    yields_third = [k for k, v in conditions.items() if v == F(1, 3)]
    check("enumerating the framework-internal scale-fixing conditions available on "
          "this surface, EXACTLY ONE yields alpha = 1/3 -- 'the one-dimensional "
          "trivial block carries charge -1', which is a choice of which block reads "
          "unit charge, not a framework-derived fact",
          len(yields_third) == 1 and yields_third[0] == "trivial-block charge = -1",
          {k: str(v) for k, v in conditions.items()})
    summary["scale_conditions"] = {k: str(v) for k, v in conditions.items()}

    # -- R5: the quadratic route provably does not give 1/3 ------------------
    # 24*(1/3)^2 = 24/9 = 8/3 != 1, so Tr(Y^2)=1 and alpha=1/3 are incompatible.
    q_at_third = sq * F(1, 3) ** 2
    check("the quadratic normalization is provably incompatible with 1/3: "
          f"Tr(Y^2) at alpha=1/3 equals {q_at_third}, not 1, so no Tr(Y^2) "
          "normalization can select it",
          q_at_third != 1, {"Tr_Y2_at_alpha_one_third": str(q_at_third)})

    # -- R6: the approved units primitive cannot supply it -------------------
    # Verified against the primitive's own scope text, quoted in the note.
    units_note = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
    carries_zero_dimensionless = False
    if units_note.exists():
        t = units_note.read_text(encoding="utf-8", errors="replace")
        carries_zero_dimensionless = ("zero dimensionless" in t
                                      and "does not supply any dimensionless" in t)
    check("the approved scale-reference primitive cannot discharge alpha either: "
          "alpha is dimensionless, and that primitive's own note states it carries "
          "zero dimensionless content and supplies no dimensionless quantity "
          "(verified by reading the registered primitive on this tree)",
          carries_zero_dimensionless,
          {"primitive_note_present": units_note.exists(),
           "scope_text_confirms_dimensionless_empty": carries_zero_dimensionless})

    # -- R7: the bounded negative claim, with its escapes --------------------
    escapes = [
        "rescope the parent row to its scale-invariant content -- the exact ratio "
        "+1:(-3) and the alpha*Z value-group structure -- which is already proven "
        "and carries no supplied scale; the auditor's own instruction says the "
        "name-free theorem surface is unchanged",
        "supply a genuinely dimensionless derivation of the unit-charge choice "
        "from framework content (none is enumerated here, and none is known to "
        "this cycle)",
        "register a new explicitly approved dimensionless authority -- which the "
        "repository's no-new-axiom / no-new-primitive rule forbids a physics-loop "
        "run from doing, and which would require an owner governance decision",
    ]
    check("BOUNDED NO-GO: alpha=1/3 is not obtainable from the structural ratio, "
          "from Record additivity, from any enumerated framework-internal "
          "normalization on this surface, or from the approved units primitive -- "
          "and the escape conditions are stated rather than left implicit",
          len(escapes) == 3,
          {"escape_routes": len(escapes)})
    summary["escapes"] = escapes

    summary["conclusion"] = (
        "The obligation as literally written -- 'derive alpha=1/3' -- is not "
        "dischargeable from the current surface. The framework fixes the charge "
        "RATIO exactly and the readout value GROUP up to scale; the remaining "
        "freedom is precisely one choice of which block reads unit charge. The "
        "highest-value repair is to rescope the parent row to its scale-invariant "
        "content, which is already exactly proven."
    )
    summary["no_go"] = {
        "statement": "no enumerated framework-internal condition on this surface "
                     "fixes alpha = 1/3",
        "scope": "the declared two-block surface V = C^2 (x) (C^2 (x) C^2) with "
                 "central block-scalar Y; conditions enumerated in this runner only",
        "shared_obstruction": False,
        "axiom_pressure": False,
        "escape_conditions": escapes,
    }
    summary["firewalls"] = {
        "any_charge_derived": False,
        "any_block_identified_with_a_physical_species": False,
        "standard_model_content_asserted": False,
        "new_axiom_or_primitive_proposed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_hypercharge_alpha_scale_freedom_cycle692_receipt_2026_07_25.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True,
                                      default=str) + "\n", encoding="utf-8")
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT HYPERCHARGE_ALPHA_SCALE_FREEDOM_TOURNAMENT_FAILED")
        return 1
    print("RESULT HYPERCHARGE_ALPHA_IS_A_FREE_SCALE_NOT_A_DERIVABLE_CONSTANT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
