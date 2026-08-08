#!/usr/bin/env python3
"""Cycle-909 INDEPENDENT CHECKER -- specified to REFUTE the revised
within-world constraint arithmetic.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
checker consumed the unlanded Cycle-863/878/902/905/906/907 census stack;
that closure is removed.  This checker now refutes the revised primary's
stipulated-table claims by independent routes:

R1  primality/factorization of 19003 and of the reduced degree-2
    denominator, by an independent primality test (6k+-1 trial order),
    never by re-running the primary's factorizer;
R2  the per-site table, by multiplication (sites * per_site == column)
    instead of the primary's division;
R3  the sum-of-two-squares representations, by a downward enumeration on p
    (the primary enumerates upward on q);
R4  the necessary denominator lemma, on a DIFFERENT random seed and with a
    multiplicative test (lcm * sum must be an integer);
R5  the CLAIMS_JSON line parsed from the primary's pinned cache must match
    the recomputed values field for field.

Fail-closed: any refutation FAILs its certificate and the checker exits 1.
No universal negative is checked because the revised primary makes none.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle909_within_world_pricing_2026_07_28.py",
    "logs/runner-cache/frontier_cycle909_within_world_pricing_2026_07_28.txt",
)

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS

# re-pinned by the review-loop fix pass whenever the primary or its cache
# changes; a mismatch is a hard refutation, never a soft warning.
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "260b2cd957f12a2c5f231fcb0a103525f1cec3e02bbf47fc66d81effdd5b7840",
    PRIMARY_CACHE:
        "b0ea7d76a1b9701026798a2fa4fa3d607aa6bcf2a2c7fb030df708370ccdb666",
}

STIPULATED_COLUMNS = {
    "degree0_column": [15600, 2910, 492, 1],
    "degree2_column": [1728, 264, 108, 0],
    "atom_sites": [12, 6, 6, 1],
}

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    k = 5
    while k * k <= n:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True


def reps_downward(n: int) -> list[tuple[int, int]]:
    out = []
    p = int(n ** 0.5) + 1
    while p >= 0:
        rest = n - p * p
        if rest >= 0:
            q = int(rest ** 0.5)
            for cand in (q - 1, q, q + 1):
                if 0 <= cand <= p and p * p + cand * cand == n:
                    out.append((p, cand))
        p -= 1
    return sorted(set(out))


def main() -> int:
    t0 = monotonic()
    payloads, pins_ok, pin_details = {}, True, []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        data = target.read_bytes() if target.is_file() else b""
        payloads[path] = data
        got = sha256(data).hexdigest()
        match = got == EXPECTED_SHA256[path]
        pins_ok &= bool(data) and match
        pin_details.append(f"{path}:{'MATCH' if match else 'MISMATCH'}")
    check("R0_PINNED_EVIDENCE", pins_ok, "; ".join(pin_details))

    claims = None
    for line in payloads[PRIMARY_CACHE].decode("utf-8",
                                               errors="replace").splitlines():
        if line.startswith("CLAIMS_JSON: "):
            claims = json.loads(line[len("CLAIMS_JSON: "):])
    check("R0b_CLAIMS_PARSED", claims is not None,
          f"claims_line_found={claims is not None}")
    if claims is None:
        claims = {}

    # R1 factorization by independent primality testing
    ok1 = (31 * 613 == 19003 and is_prime(31) and is_prime(613)
           and 175 == 5 * 5 * 7 and is_prime(5) and is_prime(7))
    got_f = claims.get("scale0_factors", {})
    ok1 &= {int(k): v for k, v in got_f.items()} == {31: 1, 613: 1}
    ok1 &= claims.get("degree2_reduced_denominator") == 175
    check("R1_FACTORIZATION", ok1,
          f"19003=31*613 primality independently confirmed; "
          f"primary_factors={got_f}")

    # R2 table by multiplication
    c0 = STIPULATED_COLUMNS["degree0_column"]
    c2 = STIPULATED_COLUMNS["degree2_column"]
    sites = STIPULATED_COLUMNS["atom_sites"]
    p0 = claims.get("per_site_degree0", [])
    p2 = claims.get("per_site_degree2", [])
    ok2 = (len(p0) == len(c0) == len(sites)
           and all(s * v == a for s, v, a in zip(sites, p0, c0))
           and all(s * v == a for s, v, a in zip(sites, p2, c2)))
    check("R2_TABLE_BY_MULTIPLICATION", ok2,
          f"sites*per_site==column for both degrees: {ok2}")

    # R3 two-squares by downward enumeration
    counts = [len(reps_downward(v)) for v in (1300, 485, 82, 1)]
    prod = 1
    for c in counts:
        prod *= c
    ok3 = (counts == claims.get("representation_counts")
           and prod == claims.get("admissible_degree2_columns")
           and (36, 2) in reps_downward(1300)
           and (22, 1) in reps_downward(485)
           and (9, 1) in reps_downward(82)
           and (1, 0) in reps_downward(1))
    check("R3_TWO_SQUARES_INDEPENDENT", ok3,
          f"counts={counts} product={prod} "
          f"primary={claims.get('representation_counts')}"
          f"/{claims.get('admissible_degree2_columns')}")

    # R4 denominator lemma on a different seed, multiplicative test
    rng = random.Random(0x909C4EC)
    bad = 0
    trials = 3000
    for _ in range(trials):
        k = rng.randint(1, 9)
        sums = [rng.randint(1, 1200) for _ in range(k)]
        nums = [rng.randint(0, 1200) for _ in range(k)]
        L = 1
        for s in sums:
            L = L * s // gcd(L, s)
        total = sum(Fraction(a, s) for a, s in zip(nums, sums))
        if (total * L).denominator != 1:
            bad += 1
    ok4 = bad == 0 and claims.get("lemma_violations") == 0
    check("R4_DENOMINATOR_LEMMA_INDEPENDENT", ok4,
          f"trials={trials} violations={bad} "
          f"primary_violations={claims.get('lemma_violations')}")

    elapsed = monotonic() - t0
    check("R5_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 909 -- INDEPENDENT CHECKER (REVISED), SPECIFIED TO REFUTE")
    w("=" * 78)
    w("")
    w("Scope: the revised primary's stipulated-table claims only.  The")
    w("unlanded census closure is removed; no universal negative exists to")
    w("check and none is certified.")
    w("")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<36} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if nfail == 0
               else "PRIMARY_REFUTED_ON_THIS_CHECK")
    w(f"VERDICT: {verdict}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 909,
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "verdict": verdict,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite; refutes the stipulated-table "
                    "cores by independent routes; fail-closed exit"),
        },
    }
    (ROOT / "outputs" /
     "within_world_independent_check_cycle909_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
