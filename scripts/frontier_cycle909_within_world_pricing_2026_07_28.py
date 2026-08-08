#!/usr/bin/env python3
"""Cycle-909 within-world constraint arithmetic at a STIPULATED carrier table.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner consumed a census substrate (Cycle-863/878/902/905/906/907 artifacts)
that is not landed on origin/main and is absent from this tree, and promoted
its declared finite recipe census into universal negatives ("nothing native
reaches 613", "more search is provably useless", "two independent
purchases").  Per the review findings that whole surface is withdrawn here:

- the input closure is now EMPTY: every quantity this runner uses is an
  in-file STIPULATED definition (declared scope input), and the unlanded
  census lineage is provenance context only, certifying nothing;
- the retained claims are exactly the reviewer-verified bounded cores:
  the factorization 19003 = 31 * 613; the necessary DENOMINATOR LEMMA for
  fixed world sums (a filter, not a completeness theorem); the exact
  per-site sum-of-two-squares identities; and the six-fold degree-2
  ambiguity WITHIN the declared two-layer arithmetic representation;
- no claim is made about "all recipes", "all transforms", or any future
  constraint; no no-go is stated.

Everything below is exact integer/Fraction arithmetic, deterministic, and
fail-closed: every certificate binds its `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# STIPULATED scope inputs (declared definitions, NOT landed facts).
# Provenance context (non-load-bearing): these values were recorded by an
# earlier full-checkout computation whose substrate (the Cycle-863/878/907
# census stack) is not landed on origin/main; they enter here as explicit
# stipulations of a finite table, and every theorem below is conditional on
# exactly this table.
# ---------------------------------------------------------------------------
STIPULATED = {
    "atom_labels": ["everything_else", "position_1", "position_2",
                    "position_3"],
    "degree0_column": [15600, 2910, 492, 1],
    "degree2_column": [1728, 264, 108, 0],
    "atom_sites": [12, 6, 6, 1],
    "recorded_layer_pairs": [[36, 2], [22, 1], [9, 1], [1, 0]],
}

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def factorize(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


def two_square_reps(n: int) -> list[tuple[int, int]]:
    """All (p, q) with p >= q >= 0 and p*p + q*q == n."""
    reps = []
    q = 0
    while 2 * q * q <= n:
        rest = n - q * q
        p = int(rest ** 0.5)
        for cand in (p - 1, p, p + 1):
            if cand >= q and cand * cand == rest:
                reps.append((cand, q))
        q += 1
    return sorted(set(reps))


def section_a_factorization() -> dict:
    c0 = STIPULATED["degree0_column"]
    c2 = STIPULATED["degree2_column"]
    scale0 = sum(c0)
    f0 = factorize(scale0)
    # reduced orbit-profile denominators for the degree-2 column
    s2 = sum(c2)
    fr2 = [Fraction(v, s2) for v in c2] if s2 else []
    den2 = 1
    for f in fr2:
        den2 = lcm2(den2, f.denominator) if f.denominator else den2
    f2 = factorize(den2)
    ok = (scale0 == 19003 and f0 == {31: 1, 613: 1}
          and den2 == 175 and f2 == {5: 2, 7: 1})
    check("A_FACTORIZATION",
          ok,
          f"scale0={scale0}={f0} reduced_degree2_denominator={den2}={f2}")
    return {"scale0": scale0, "scale0_factors": f0,
            "degree2_reduced_denominator": den2,
            "degree2_denominator_factors": f2}


def section_b_table_consistency() -> dict:
    c0, c2 = STIPULATED["degree0_column"], STIPULATED["degree2_column"]
    sites = STIPULATED["atom_sites"]
    per0 = [Fraction(a, s) for a, s in zip(c0, sites)]
    per2 = [Fraction(a, s) for a, s in zip(c2, sites)]
    integral = all(f.denominator == 1 for f in per0 + per2)
    ok = integral and [int(f) for f in per0] == [1300, 485, 82, 1] \
        and [int(f) for f in per2] == [144, 44, 18, 0]
    check("B_TABLE_CONSISTENCY", ok,
          f"per_site_degree0={[str(f) for f in per0]} "
          f"per_site_degree2={[str(f) for f in per2]}")
    return {"per_site_degree0": [int(f) for f in per0],
            "per_site_degree2": [int(f) for f in per2]}


def section_c_denominator_lemma(rng: random.Random) -> dict:
    """NECESSARY DENOMINATOR LEMMA (filter, not completeness).

    For integers a_w >= 0 and positive world sums S_w, the reduced
    denominator of  x = sum_w a_w / S_w  divides lcm(S_w).  Hence if a
    candidate profile on those FIXED world sums must hit a target value
    c/scale in lowest terms, then scale | lcm(S_w) is NECESSARY.  This
    eliminates candidate profiles with those already-chosen sums; it says
    NOTHING about other functions of a census, other sums, or future
    constraints, and no such claim is made.
    """
    trials, failures = 0, []
    for _ in range(4000):
        k = rng.randint(1, 8)
        sums = [rng.randint(1, 900) for _ in range(k)]
        nums = [rng.randint(0, 900) for _ in range(k)]
        x = sum(Fraction(a, s) for a, s in zip(nums, sums))
        L = 1
        for s in sums:
            L = lcm2(L, s)
        trials += 1
        if L % x.denominator != 0:
            failures.append((nums, sums))
    # planted controls: a sum family whose lcm carries both 31 and 613 CAN
    # meet a /19003 target; one whose lcm lacks 613 CANNOT.
    good = [31 * 613, 4, 6]
    bad = [31, 4, 6]
    Lg = 1
    for s in good:
        Lg = lcm2(Lg, s)
    Lb = 1
    for s in bad:
        Lb = lcm2(Lb, s)
    witness = Fraction(1, 31 * 613) == Fraction(1, good[0])
    control_ok = (Lg % 19003 == 0) and (Lb % 19003 != 0) and witness
    ok = not failures and control_ok
    check("C_DENOMINATOR_LEMMA", ok,
          f"randomized_instances={trials} violations={len(failures)} "
          f"planted_pass_lcm_divisible={Lg % 19003 == 0} "
          f"planted_fail_lcm_divisible={Lb % 19003 == 0}")
    return {"randomized_instances": trials, "violations": len(failures),
            "statement": "reduced denominator of sum(a_w/S_w) divides "
                         "lcm(S_w); necessary filter on FIXED world sums "
                         "only"}


def section_d_two_squares() -> dict:
    per0 = [1300, 485, 82, 1]
    per2 = [144, 44, 18, 0]
    recorded = [tuple(p) for p in STIPULATED["recorded_layer_pairs"]]
    rows, all_ok = [], True
    rep_counts = []
    for c0v, c2v, (p, q) in zip(per0, per2, recorded):
        identity_ok = (p * p + q * q == c0v) and (2 * p * q == c2v)
        reps = two_square_reps(c0v)
        rep_counts.append(len(reps))
        rows.append({"per_site_degree0": c0v, "per_site_degree2": c2v,
                     "recorded_pair": [p, q], "identity_holds": identity_ok,
                     "all_representations": [list(r) for r in reps],
                     "distinct_2pq_values": sorted({2 * a * b
                                                    for a, b in reps})})
        all_ok &= identity_ok and (p, q) in reps
    ambiguity = 1
    for c in rep_counts:
        ambiguity *= c
    ok = all_ok and rep_counts == [3, 2, 1, 1] and ambiguity == 6
    check("D_TWO_SQUARES_IDENTITIES", ok,
          f"identities_hold={all_ok} representation_counts={rep_counts} "
          f"admissible_degree2_columns={ambiguity}")
    return {"rows": rows, "representation_counts": rep_counts,
            "admissible_degree2_columns_in_representation": ambiguity}


def section_e_nonuniqueness(sec_d: dict) -> dict:
    """WITHIN the declared two-layer arithmetic representation (c0 = s(p^2 +
    q^2), c2 = 2spq), the degree-0 column does not determine the degree-2
    column: atoms with several (p, q) representations force several distinct
    2pq values.  This is a representation-scoped non-uniqueness statement
    ONLY; it is NOT a theorem of universal carrier independence, and no
    claim about "all census transforms" is made or implied."""
    multi = [r for r in sec_d["rows"] if len(r["all_representations"]) > 1]
    genuinely_distinct = all(len(r["distinct_2pq_values"]) > 1 for r in multi)
    ok = len(multi) >= 1 and genuinely_distinct \
        and sec_d["admissible_degree2_columns_in_representation"] > 1
    check("E_REPRESENTATION_SCOPED_NONUNIQUENESS", ok,
          f"atoms_with_multiple_representations={len(multi)} "
          f"each_with_distinct_2pq={genuinely_distinct}")
    return {"atoms_with_multiple_representations": len(multi),
            "scope": "the declared two-layer arithmetic representation only"}


def run_all(seed: int) -> dict:
    rng = random.Random(seed)
    a = section_a_factorization()
    b = section_b_table_consistency()
    c = section_c_denominator_lemma(rng)
    d = section_d_two_squares()
    e = section_e_nonuniqueness(d)
    return {"a": a, "b": b, "c": c, "d": d, "e": e,
            "science_digest": digest([a, b, c, d, e, STIPULATED])}


def main() -> int:
    t0 = monotonic()
    first = run_all(909)
    saved = list(CERTS)
    CERTS.clear()
    second = run_all(909)
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("F_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("G_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 909 -- WITHIN-WORLD CONSTRAINT ARITHMETIC AT A STIPULATED TABLE")
    w("=" * 78)
    w("")
    w("SCOPE: input closure EMPTY.  Every quantity is an in-file stipulated")
    w("definition; the unlanded census lineage is provenance context only.")
    w("No universal negative, no exhaustiveness claim, no no-go is stated.")
    w("")
    w("-- stipulated table -----------------------------------------------------")
    for k, v in STIPULATED.items():
        w(f"  {k}: {v}")
    w("")
    w("-- results --------------------------------------------------------------")
    w("  degree-0 scale factorization: 19003 = "
      + " * ".join(f"{p}^{e}" if e > 1 else str(p)
                   for p, e in sorted(first['a']['scale0_factors'].items())))
    w(f"  degree-2 reduced denominator: "
      f"{first['a']['degree2_reduced_denominator']}"
      f" = {first['a']['degree2_denominator_factors']}")
    w(f"  denominator lemma: {first['c']['statement']}")
    w(f"    randomized instances: {first['c']['randomized_instances']}, "
      f"violations: {first['c']['violations']}")
    w("  per-site two-square identities and representation ambiguity:")
    for r in first["d"]["rows"]:
        w(f"    c0={r['per_site_degree0']:>5} c2={r['per_site_degree2']:>4} "
          f"pair={r['recorded_pair']} identity={r['identity_holds']} "
          f"reps={r['all_representations']}")
    w(f"  admissible degree-2 columns within the representation: "
      f"{first['d']['admissible_degree2_columns_in_representation']}")
    w("")
    w("CLAIMS_JSON: " + compact({
        "scale0_factors": first["a"]["scale0_factors"],
        "degree2_reduced_denominator":
            first["a"]["degree2_reduced_denominator"],
        "per_site_degree0": first["b"]["per_site_degree0"],
        "per_site_degree2": first["b"]["per_site_degree2"],
        "representation_counts": first["d"]["representation_counts"],
        "admissible_degree2_columns":
            first["d"]["admissible_degree2_columns_in_representation"],
        "lemma_violations": first["c"]["violations"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<40} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 909,
        "claim_type": "bounded_theorem",
        "headline": ("within-world constraint arithmetic at a stipulated "
                     "carrier table: 19003 = 31 * 613; a necessary "
                     "denominator filter for fixed world sums; exact "
                     "per-site sum-of-two-squares identities; six-fold "
                     "degree-2 ambiguity WITHIN the declared two-layer "
                     "representation.  No universal negative is claimed."),
        "stipulated_scope_inputs": STIPULATED,
        "provenance_context_non_load_bearing": (
            "the table values were recorded by an earlier full-checkout "
            "computation on the unlanded Cycle-863/878/902/905/906/907 "
            "census stack; that lineage certifies nothing here"),
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: unlanded input closure removed; "
                    "universal negatives and 'two purchases' withdrawn; "
                    "bounded cores retained with fail-closed certificates"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "within_world_pricing_cycle909_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
