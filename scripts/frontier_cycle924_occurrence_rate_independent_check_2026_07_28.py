#!/usr/bin/env python3
"""Cycle-924 INDEPENDENT CHECKER -- specified to REFUTE the revised
occurrence-rate-route arithmetic.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
checker's hidden-import check passed a literal True regardless of the
smuggled list it computed; corrected -- every certificate below binds
`pass` to its predicate and a refutation exits 1.  The unlanded/generated
input closure is removed.

Independent routes:

EXACT RATIOS by cross-multiplication over the integers (no
    Fraction reduction): 84*41 == 21*164; (2*123 - 3*57)... expanded
    integer identities for the 19/123 miss; 16*3 == 2*24;
CYCLIC-PATCH NULLITY by the structural route (additivity forces
    determination by singletons; cyclic invariance identifies all
    singletons; hence dimension 1), cross-checked by explicit singleton
    orbit counting -- never by the primary's echelon elimination;
GROUP EQUALITY by direct set construction;
MENU LINE and imported-normalization collapse by direct
    substitution with integer arithmetic;
FRESH CLAIM PARSING from one primary subprocess execution must match field for
    field;
OVERCLAIM SCAN on the primary's emitted output: withdrawn wording
    ("priced shut", "blocked BY THEOREM", "sole remaining", "TERMINAL")
    must not be asserted.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle924_occurrence_rate_route_2026_07_28.py",
)

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]

# Re-pinned whenever the primary changes; a mismatch is a hard refutation.
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "98a8ba289b699f44524ad4ce49875afca1c0ea744d1df0abdf3f0f0b4e0d16bf",
}

WITHDRAWN_WORDING = ("priced shut", "blocked BY THEOREM", "sole remaining",
                     "TERMINAL")

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def main() -> int:
    t0 = monotonic()
    payloads, pins_ok, details = {}, True, []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        data = target.read_bytes() if target.is_file() else b""
        payloads[path] = data
        match = sha256(data).hexdigest() == EXPECTED_SHA256[path]
        pins_ok &= bool(data) and match
        details.append(f"{path}:{'MATCH' if match else 'MISMATCH'}")
    check("PINNED_EVIDENCE", pins_ok, "; ".join(details))

    proc = subprocess.run(
        [sys.executable, str(ROOT / PRIMARY_PATH)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    primary_text = proc.stdout
    fresh_ok = (proc.returncode == 0 and "VERDICT: PASS" in primary_text
                and len(primary_text.encode()) < STDOUT_LIMIT_BYTES)
    check("FRESH_PRIMARY_EXECUTION", fresh_ok,
          f"returncode={proc.returncode} stdout_bytes={len(primary_text.encode())} "
          f"stderr_bytes={len(proc.stderr.encode())}")

    claims = None
    for line in primary_text.splitlines():
        if line.startswith("CLAIMS_JSON: "):
            claims = json.loads(line[len("CLAIMS_JSON: "):])
    check("CLAIMS_PARSED", claims is not None,
          f"claims_line_found={claims is not None}")
    if claims is None:
        claims = {}

    # Exact-ratio integer cross-multiplication
    #   84/164 == 21/41  <=>  84*41 == 21*164
    #   2/3 - 21/41 == 19/123  <=>  (2*41 - 3*21) == 19 and 3*41 == 123
    #   16/24 == 2/3  <=>  16*3 == 2*24
    ok1 = (84 * 41 == 21 * 164
           and 2 * 41 - 3 * 21 == 19 and 3 * 41 == 123
           and 16 * 3 == 2 * 24
           and claims.get("share") == "21/41"
           and claims.get("miss") == "19/123"
           and claims.get("period_ratio") == "2/3")
    check("RATIOS_CROSS_MULTIPLIED", ok1,
          f"84*41={84*41}==21*164={21*164}; 2*41-3*21={2*41-3*21}; "
          f"16*3={16*3}==2*24={2*24}")

    # Structural nullity: additivity determines A by singleton values
    # (every configuration is the disjoint union of its singletons);
    # cyclic invariance identifies all singletons into one orbit.
    ok2 = True
    dims = []
    for m in range(2, 7):
        # singleton orbit count under the cyclic shift
        parent = list(range(m))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(m):
            a, b = find(i), find((i + 1) % m)
            if a != b:
                parent[a] = b
        orbits = len({find(i) for i in range(m)})
        dims.append((f"Z/{m}", orbits))
        ok2 &= orbits == 1
    primary_dims = [tuple(x) for x in claims.get("patch_dims", [])]
    ok2 &= primary_dims == dims
    check("NULLITY_STRUCTURAL", ok2,
          f"singleton_orbits={dims} primary={primary_dims}")

    # Group equality by direct construction
    rotations = {tuple((i + k) % 3 for i in range(3)) for k in range(3)}
    translations = {tuple((i + t) % 3 for i in range(3)) for t in range(3)}
    ok3 = rotations == translations and claims.get("group_equality") is True
    check("GROUP_EQUALITY_DIRECT", ok3,
          f"equal={rotations == translations}")

    # Menu line plus normalization by integer substitution
    # alpha * count(full) = 2/9 with count(full)=3  =>  alpha = 2/27
    # integer check: alpha = 2/27 satisfies 27 * alpha * 3 == 2 * 3 / ... :
    # 3 * (2/27) == 2/9  <=>  3 * 2 * 9 == 2 * 27
    menu_27ths = {"alpha_zero": 0, "alpha_ninth": 3, "alpha_third": 9,
                  "alpha_one": 27, "alpha_2_27": 2}
    survivors = [n for n, v in menu_27ths.items() if 3 * v * 9 == 2 * 27]
    ok4 = (3 * 2 * 9 == 2 * 27
           and survivors == ["alpha_2_27"]
           and claims.get("forced_alpha") == "2/27"
           and claims.get("survivors") == ["alpha_2_27"])
    check("NORMALIZATION_COLLAPSE", ok4,
          f"3*(2/27)==2/9 by integers: {3 * 2 * 9}=={2 * 27}; "
          f"survivors={survivors}")

    # Overclaim scan on the fresh primary output
    hits = []
    for term in WITHDRAWN_WORDING:
        for i, ln in enumerate(primary_text.splitlines(), 1):
            if term in ln and "withdrawn" not in ln.lower() \
                    and "Withdrawn:" not in ln:
                hits.append(f"fresh-output:{i}:{term}")
    ok6 = not hits
    check("OVERCLAIM_SCAN", ok6, f"hits={hits if hits else 'none'}")

    elapsed = monotonic() - t0
    check("RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 924 -- INDEPENDENT CHECKER (REVISED), SPECIFIED TO REFUTE")
    w("=" * 78)
    w("")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<32} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if nfail == 0
               else "PRIMARY_REFUTED_ON_THIS_CHECK")
    w(f"VERDICT: {verdict}")
    text = "\n".join(out) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stderr.write(
            f"stdout budget exceeded: {len(text.encode())}>="
            f"{STDOUT_LIMIT_BYTES}\n"
        )
        return 1
    sys.stdout.write(text)
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
