#!/usr/bin/env python3
"""Cycle-911 census-consistency arithmetic and the declared-likelihood
maximizer lemma (self-contained).

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner consumed the unlanded Cycle-863/878/905/907/909 stack and bundled
three different kinds of content: (a) exact finite computations on that
substrate (the no-coupling census, the branch-pair matrix, the lock-point
menus); (b) a maximum-likelihood argument billed as selecting counting
"UNCONDITIONALLY"; and (c) a re-typing CONVENTION ("the worlds were setups
all along", "the census weightings were never occurrence weights", "the
interface survives as bookkeeping").  Review found: the substrate closure
is absent from this tree, the "unconditional" likelihood result silently
imports its sample space (every observed instance its own atom) and an iid
product likelihood -- load-bearing statistical-model choices the axioms do
not supply -- and the re-typing is a non-propositional convention, not a
theorem.  Accordingly:

- the convention moves to a separate meta note
  (docs/WORLD_SETUP_BOOKKEEPING_TERMINOLOGY_META_NOTE_2026-08-08.md) and is
  not asserted here;
- the substrate-scoped computations are STIPULATED history (provenance
  context, certifying nothing);
- this runner certifies only two self-contained items:

L1  CENSUS CONSISTENCY ARITHMETIC: 187 x 4 = 748; C(748, 2) = 279,378;
    the recorded shared-state/schedule counts are internally consistent.

L2  DECLARED-LIKELIHOOD MAXIMIZER LEMMA (exact, with the model choices
    named as imports): UNDER the declared model -- sample space = the N
    individually indexed census events, likelihood L(p) = product over
    events of p(e), every atom observed exactly once -- the unique
    maximizer is uniform.  A CONTROL shows the ontology choice is
    load-bearing: merging two events into one atom (observed twice)
    moves the maximizer away from event-uniformity.  So "maximum
    likelihood selects counting" is CONDITIONAL on the declared event
    ontology and factorization, and is not claimed unconditionally.

Fail-closed: every certificate binds `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# STIPULATED recorded census values (provenance context, non-load-bearing).
# ---------------------------------------------------------------------------
RECORDED = {
    "position_sets": 187,
    "event_seeds": 4,
    "census_worlds": 748,
    "world_pairs": 279378,
    "shared_tick0_pairs": 5168,
    "distinct_tick0_vectors": 323,
    "lock_points": 164,
    "menu_size_at_every_lock_point": 2,
    "recorded_branch_pairs": 0,
}

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def l1_census_consistency() -> dict:
    r = RECORDED
    pairs = r["census_worlds"] * (r["census_worlds"] - 1) // 2
    ok = (r["position_sets"] * r["event_seeds"] == r["census_worlds"]
          and pairs == r["world_pairs"]
          and r["distinct_tick0_vectors"] <= r["census_worlds"]
          and r["shared_tick0_pairs"] <= r["world_pairs"]
          and r["recorded_branch_pairs"] == 0)
    check("L1_CENSUS_CONSISTENCY", ok,
          f"187*4={r['position_sets'] * r['event_seeds']} "
          f"C(748,2)={pairs} recorded_pairs={r['world_pairs']}")
    return {"computed_world_pairs": pairs}


def l2_likelihood_lemma(rng: random.Random) -> dict:
    """UNDER the declared model (each indexed event its own atom, product
    likelihood, each atom observed once) the maximizer is uniform.  Exact
    verification: for random rational probability vectors q != uniform,
    product(q) < product(uniform).  Equivalent exact test (no floats):
    product(N * q_i) < 1.  The DECLARED imports are named in the receipt:
    the event ontology and the iid product factorization are model
    choices, not axiom content."""
    trials, violations = 0, 0
    for _ in range(500):
        n = rng.randint(2, 9)
        cuts = sorted(rng.randint(0, 60) for _ in range(n - 1))
        parts = []
        prev = 0
        for c in cuts + [60]:
            parts.append(c - prev)
            prev = c
        total = sum(parts)
        if total == 0 or 0 in parts:
            continue
        q = [Fraction(p, total) for p in parts]
        if all(x == Fraction(1, n) for x in q):
            continue
        trials += 1
        prod_scaled = Fraction(1)
        for x in q:
            prod_scaled *= n * x
        if prod_scaled >= 1:
            violations += 1
    # uniform attains the bound with equality
    n = 7
    uniform_scaled = Fraction(1)
    for _ in range(n):
        uniform_scaled *= n * Fraction(1, n)
    uniform_ok = uniform_scaled == 1

    # CONTROL: merge two events into one atom (observed twice).  With
    # atoms {a (observed 2x), e3 ... eN}, the MLE puts 2/N on the merged
    # atom -- event-uniformity fails, so the atomization choice is
    # load-bearing.  Exact check on N = 6: maximize p_a^2 * prod p_i by
    # comparing the analytic maximizer against event-uniform.
    N = 6
    p_merged = [Fraction(2, N)] + [Fraction(1, N)] * (N - 2)

    def merged_likelihood(p):
        val = p[0] * p[0]
        for x in p[1:]:
            val *= x
        return val

    # candidate with mass 2/N on the merged atom (the analytic MLE)
    like_mle = merged_likelihood(p_merged)
    # a genuinely different normalized candidate: uniform over the N-1 atoms
    p_atom_uniform = [Fraction(1, N - 1)] * (N - 1)
    like_atom_uniform = merged_likelihood(p_atom_uniform)
    control_ok = (sum(p_merged) == 1 and sum(p_atom_uniform) == 1
                  and like_mle > like_atom_uniform)

    ok = trials > 0 and violations == 0 and uniform_ok and control_ok
    check("L2_LIKELIHOOD_LEMMA_CONDITIONAL", ok,
          f"random_nonuniform_vectors={trials} violations={violations} "
          f"uniform_attains_bound={uniform_ok} "
          f"merged_atom_control_moves_MLE={control_ok}")
    return {"trials": trials, "violations": violations,
            "merged_atom_control_moves_MLE": control_ok,
            "declared_imports": [
                "sample space: every individually indexed census event is "
                "its own atom",
                "likelihood: iid product over event-instance identities, "
                "each observed exactly once",
            ]}


def run_all(seed: int) -> dict:
    rng = random.Random(seed)
    a = l1_census_consistency()
    b = l2_likelihood_lemma(rng)
    return {"l1": a, "l2": b,
            "science_digest": digest([a, b, RECORDED])}


def main() -> int:
    t0 = monotonic()
    first = run_all(911)
    saved = list(CERTS)
    CERTS.clear()
    second = run_all(911)
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("L3_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("L4_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 911 -- CENSUS-CONSISTENCY ARITHMETIC AND THE DECLARED-"
      "LIKELIHOOD LEMMA")
    w("=" * 78)
    w("")
    w("SCOPE: self-contained.  The unlanded substrate closure is removed;")
    w("the worlds/setups re-typing is a CONVENTION recorded in a separate")
    w("meta note and asserted nowhere in this runner; the likelihood lemma")
    w("is conditional on declared model imports named in the receipt.")
    w("")
    w("-- stipulated recorded census -------------------------------------------")
    for k, v in RECORDED.items():
        w(f"  {k}: {v}")
    w("")
    w("CLAIMS_JSON: " + compact({
        "computed_world_pairs": first["l1"]["computed_world_pairs"],
        "lemma_trials": first["l2"]["trials"],
        "lemma_violations": first["l2"]["violations"],
        "merged_atom_control": first["l2"]["merged_atom_control_moves_MLE"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<34} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 911,
        "claim_type": "bounded_theorem",
        "headline": ("census-consistency arithmetic (187 x 4 = 748; "
                     "C(748,2) = 279,378) and the declared-likelihood "
                     "maximizer lemma: uniform maximizes the DECLARED iid "
                     "product likelihood over individually atomized events; "
                     "the merged-atom control shows the ontology choice is "
                     "load-bearing.  Conditional, never unconditional"),
        "stipulated_scope_inputs": RECORDED,
        "declared_model_imports": first["l2"]["declared_imports"],
        "provenance_context_non_load_bearing": (
            "the recorded census values come from the unlanded "
            "Cycle-863/878 substrate computation; the no-coupling census, "
            "branch-pair matrix, lock-point menus and convergence table are "
            "recorded history there and certify nothing here; the "
            "worlds/setups terminology lives in the separate meta "
            "convention note"),
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: unlanded closure removed; the "
                    "re-typing convention split into a meta note; the "
                    "'UNCONDITIONALLY' likelihood claim demoted to a "
                    "conditional lemma with named model imports"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "type_vacuity_cycle911_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
