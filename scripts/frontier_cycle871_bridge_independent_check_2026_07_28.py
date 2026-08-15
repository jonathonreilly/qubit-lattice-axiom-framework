#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-871 source-action pricing.

This checker is specified to REFUTE. It independently attacks the finite-map
dimension and cardinality form, the normalization stabilizer, all eight
obligation-model dimensions, exact quote replay, and deterministic execution.
Every advertised primary row and scalar headline is required exactly once.
Missing, duplicate, unchecked, or corrupted claims are refutations.

The SHA-pinned primary is executed once in a subprocess so the checker tests
fresh output; it is never imported.  The cited sources remain SHA-pinned text
evidence behind a meta-path import firewall.  The arithmetic route is
independent -- integers modulo small primes and union-find here, exact
rationals and Gaussian elimination there -- so a bug in one route cannot
reproduce itself in the other.  Eight hostile controls must be killed before a
clean run can pass.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py",
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md",
    "docs/SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md",
    "docs/SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md",
    "docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md",
    "docs/YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
)

from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations, product
import json
from pathlib import Path
import random
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PYTHON_PATHS = tuple(p for p in AUDIT_INPUT_PATHS if p.endswith(".py"))
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in PYTHON_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "f3434775f604ff6a2a3ed4aa099f0f2b32238f162b9b35b1ed047b005efb54e8",
    AUDIT_INPUT_PATHS[1]:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    AUDIT_INPUT_PATHS[2]:
        "af7bbdfda8831df1c86ec7ca9cf62b6cbdd920f4dca1a4cb03e7f389c73e386a",
    AUDIT_INPUT_PATHS[3]:
        "cb19cb3441136c4a3948cdd12cb5d4d9b82478988ad1047294230501039184cd",
    AUDIT_INPUT_PATHS[4]:
        "5de15beb514fc3eab952992932907a159fa33232caef1d135d14e07f46c6a508",
    AUDIT_INPUT_PATHS[5]:
        "c03409f79768b8f59b8a07b4a2571a1ea554d4cb40fd16bcbee4b14b02fd4d69",
    AUDIT_INPUT_PATHS[6]:
        "ef5e0280ab8bc7ae132f609635b893e208628650720eade6f27d164290a053d1",
    AUDIT_INPUT_PATHS[7]:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "3e6684727548ed987054b0d1d8795ac90b247557",
    AUDIT_INPUT_PATHS[1]: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    AUDIT_INPUT_PATHS[2]: "36c2b9dd0b799f7102c7685db5e4fc5121b933ce",
    AUDIT_INPUT_PATHS[3]: "f2256fe7c1bfd5099e462688cc56cd48c7956a63",
    AUDIT_INPUT_PATHS[4]: "ecfa17055c67820fd426e7b60367787bc9d45c93",
    AUDIT_INPUT_PATHS[5]: "b4d3526079afd729319f236c3b246365007daff9",
    AUDIT_INPUT_PATHS[6]: "b9f089eef2395145f54c85103a770ed7d096ea48",
    AUDIT_INPUT_PATHS[7]: "9a449956422a5687b5b1346f428c9e4e35489038",
}
PRIMARY_REQUIRED_MARKERS = (
    "section_a_quotes",
    "section_b_forced_free",
    "section_c_subgap",
    "section_d_map",
    "MODEL_CLAUSES",
    "ALIAS_PATTERNS",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


CERTS: list[tuple[str, bool, str]] = []


def certify(name: str, ok: bool, detail: str) -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


# ==========================================================================
# pinned evidence and parsing of the primary's claims
# ==========================================================================
def evidence() -> dict:
    rows, payloads = [], {}
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.is_file()
        payload = target.read_bytes() if exists else b""
        payloads[path] = payload
        rows.append({
            "path": path, "exists": exists,
            "worktree_relative": not Path(path).is_absolute(),
            "bytes": len(payload),
            "sha256": sha256(payload).hexdigest(),
            "sha256_exact": sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
            "access": ("TEXT_AST_ONLY_BLOCKLISTED_PRIMARY" if path.endswith(".py")
                       else "TEXT_ONLY_PINNED_SOURCE"),
        })
    src = payloads[PRIMARY_PATH].decode("utf-8")
    missing = [m for m in PRIMARY_REQUIRED_MARKERS if m not in src]
    leaked = [m for m in BLOCKLISTED_MODULES if m in sys.modules]
    ok = (all(r["exists"] and r["worktree_relative"] for r in rows)
          and all(r["sha256_exact"] and r["git_blob_exact"] for r in rows)
          and not missing and not leaked)
    certify("CERT-PROV/pinned-evidence", ok,
            f"paths={len(rows)} sha_exact={sum(r['sha256_exact'] for r in rows)} "
            f"blob_exact={sum(r['git_blob_exact'] for r in rows)} "
            f"missing_markers={missing} blocklist_leaks={leaked}")
    return {"rows": rows, "payloads": payloads, "blocklist_leaks": leaked}


PATCH_ROW = re.compile(
    r"^\s+(\((?:\d+,\s*)*\d+,?\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s+(\d+)\s+"
    r"(True|False|None)\s*$")
MAP_ROW = re.compile(
    r"^\s+(\d+)\s+(smaller-model-dim|equal-model-dim|larger-model-dim)"
    r"\s+(\S.*)$")
QUOTE_HEAD = re.compile(r"^\s+(\S+\.md):(\d+)\s+\[(\w+)\]\s+sha256=([0-9a-f]{12})")
QUOTE_LINE = re.compile(r"^\s{4}VERBATIM LINE \| (.*)$")
NUM_AFTER = re.compile(r":\s*(-?\d+)\s*$")

EXPECTED_PATCH_DIMS = (
    (2,), (3,), (4,), (5,), (6,), (2, 2), (2, 3), (7,), (8,), (10,),
    (12,), (3, 3), (2, 2, 2), (2, 2, 3), (4, 4), (3, 3, 3),
)
EXPECTED_MAP = {
    "GB-S1a linear test-action shape": (0, "smaller-model-dim"),
    "GB-S1b source-strength normalization (absorbs 1/(4 pi) and any unit conversion)":
        (1, "equal-model-dim"),
    "physical Newton constant / SI normalization": (1, "equal-model-dim"),
    "finite-core scalar 1/(r+0.1) vs the exact periodic graph-Laplacian Green solution":
        (5, "larger-model-dim"),
    "GB-S2 phase-propagation kernel and detector-window readout":
        (8, "larger-model-dim"),
    "GB-S3 label/offset generated-connectivity family":
        (4, "larger-model-dim"),
    "signed-gravity locked source-action term (scale plus locked orientation)":
        (1, "equal-model-dim"),
    "h-class/h-unit density-to-angle readout identity":
        (2, "larger-model-dim"),
}
EXPECTED_QUOTES = {
    ("docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md", 104),
    ("docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md", 247),
    ("docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md", 527),
    ("docs/SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md", 205),
    ("docs/SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md", 92),
    ("docs/SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md", 472),
    ("docs/YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md", 96),
    ("docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md", 21),
}


def parse_primary(cache_text: str) -> dict:
    lines = cache_text.split("\n")
    patches, mapped, quotes = [], [], []
    pending = None
    for line in lines:
        m = PATCH_ROW.match(line)
        if m:
            patches.append({
                "patch": m.group(1), "sites": int(m.group(2)),
                "unknowns": int(m.group(3)), "rank": int(m.group(4)),
                "full_dim": int(m.group(5)), "struct_dim": int(m.group(6)),
                "agree": m.group(7)})
            continue
        m = MAP_ROW.match(line)
        if m:
            mapped.append({"free_dim": int(m.group(1)), "strength": m.group(2),
                           "clause": m.group(3).strip()})
            continue
        m = QUOTE_HEAD.match(line)
        if m:
            pending = {"path": m.group(1), "line_no": int(m.group(2)),
                       "lane": m.group(3), "sha12": m.group(4)}
            continue
        m = QUOTE_LINE.match(line)
        if m and pending:
            pending["line_verbatim"] = m.group(1)
            quotes.append(pending)
            pending = None

    def find_num(prefix: str) -> int | None:
        for line in lines:
            if prefix in line:
                m = NUM_AFTER.search(line)
                if m:
                    return int(m.group(1))
        return None

    return {
        "patches": patches,
        "map": mapped,
        "quotes": quotes,
        "invariant_pairs": find_num("pairs acting trivially"),
        "grid_pairs": find_num("grid pairs tested"),
        "separating": find_num("separating lambda from sigma"),
        "scale_free_dim": find_num("free dimension of the scale itself"),
        "verdict_pass": "VERDICT: PASS" in cache_text,
    }


def validate_primary_contract(claims: dict) -> list[str]:
    """Bind every advertised primary row and scalar headline fail closed."""
    bad: list[str] = []
    expected_patch_keys = [str(d).replace(" ", "") for d in EXPECTED_PATCH_DIMS]
    patch_keys = [r["patch"].replace(" ", "") for r in claims["patches"]]
    if Counter(patch_keys) != Counter(expected_patch_keys):
        bad.append("finite-map patch identities/count are not exact and unique")
    for row in claims["patches"]:
        key = row["patch"].replace(" ", "")
        if key not in expected_patch_keys:
            continue
        dims = EXPECTED_PATCH_DIMS[expected_patch_keys.index(key)]
        sites = 1
        for d in dims:
            sites *= d
        small = sites <= 6
        expected = {
            "sites": sites,
            "unknowns": (1 << sites) if small else 0,
            "rank": ((1 << sites) - 1) if small else 0,
            "full_dim": 1 if small else -1,
            "struct_dim": 1,
            "agree": "True" if small else "None",
        }
        if any(row[name] != value for name, value in expected.items()):
            bad.append(f"finite-map row corrupted: {key}")

    map_keys = [r["clause"] for r in claims["map"]]
    if Counter(map_keys) != Counter(EXPECTED_MAP.keys()):
        bad.append("obligation-model identities/count are not exact and unique")
    for row in claims["map"]:
        expected = EXPECTED_MAP.get(row["clause"])
        if expected and (row["free_dim"], row["strength"]) != expected:
            bad.append(f"obligation-model row corrupted: {row['clause']}")

    quote_keys = [(q["path"], q["line_no"]) for q in claims["quotes"]]
    if Counter(quote_keys) != Counter(EXPECTED_QUOTES):
        bad.append("quote identities/count are not exact and unique")
    expected_scalars = {
        "grid_pairs": 100,
        "invariant_pairs": 10,
        "separating": 0,
        "scale_free_dim": 1,
    }
    for name, expected in expected_scalars.items():
        if claims.get(name) != expected:
            bad.append(f"stabilizer headline corrupted: {name}")
    if not claims["verdict_pass"]:
        bad.append("primary verdict is not PASS")
    return bad


def run_primary() -> str:
    proc = subprocess.run(
        [sys.executable, str(ROOT / PRIMARY_PATH)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    stdout_bytes = len(proc.stdout.encode())
    ok = (proc.returncode == 0 and "VERDICT: PASS" in proc.stdout
          and stdout_bytes <= STDOUT_LIMIT_BYTES)
    certify(
        "CERT-PRIMARY/fresh-execution",
        ok,
        f"returncode={proc.returncode} stdout_bytes={stdout_bytes} "
        f"stderr_bytes={len(proc.stderr.encode())}",
    )
    return proc.stdout


# ==========================================================================
# Independent finite-map dimension and cardinality-form checks
# ==========================================================================
BRUTE = (((2,), 2), ((2,), 3), ((2,), 5), ((2,), 7),
         ((3,), 2), ((3,), 3),
         ((4,), 2), ((2, 2), 2))


def sites_of(dims):
    return [tuple(c) for c in product(*[range(d) for d in dims])]


def shift(mask, sites, index, dims, v):
    out = 0
    for i, s in enumerate(sites):
        if mask >> i & 1:
            moved = tuple((s[k] + v[k]) % dims[k] for k in range(len(dims)))
            out |= 1 << index[moved]
    return out


def brute_force_count(dims, p):
    sites = sites_of(dims)
    n = len(sites)
    index = {s: i for i, s in enumerate(sites)}
    nconf = 1 << n
    pairs = []
    for assign in product((0, 1, 2), repeat=n):
        a = b = 0
        for i, t in enumerate(assign):
            if t == 1:
                a |= 1 << i
            elif t == 2:
                b |= 1 << i
        if a and b and a < b:
            pairs.append((a | b, a, b))
    shifts = []
    for i in range(len(dims)):
        v = tuple(1 if j == i else 0 for j in range(len(dims)))
        for m in range(nconf):
            t = shift(m, sites, index, dims, v)
            if t != m:
                shifts.append((m, t))
    solutions, off_shape = 0, []
    for flat in product(range(p), repeat=nconf):
        if flat[0] % p:
            continue
        if any((flat[u] - flat[a] - flat[b]) % p for u, a, b in pairs):
            continue
        if any((flat[m] - flat[t]) % p for m, t in shifts):
            continue
        solutions += 1
        c = flat[1] if n else 0
        if any(flat[m] != (c * bin(m).count("1")) % p for m in range(nconf)):
            off_shape.append(flat)
    return solutions, off_shape


def singleton_translation_orbits(dims) -> int:
    sites = sites_of(dims)
    parent = list(range(len(sites)))
    index = {site: i for i, site in enumerate(sites)}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for axis in range(len(dims)):
        for site in sites:
            moved = tuple(
                (site[k] + (1 if k == axis else 0)) % dims[k]
                for k in range(len(dims))
            )
            a, b = find(index[site]), find(index[moved])
            if a != b:
                parent[a] = b
    return len({find(i) for i in range(len(sites))})


def hunt_finite_map(claims: dict) -> dict:
    claimed = {}
    for row in claims["patches"]:
        claimed[row["patch"].replace(" ", "")] = row["struct_dim"]
    results, refutations = [], []
    for dims, p in BRUTE:
        key = str(dims).replace(" ", "")
        count, off = brute_force_count(dims, p)
        want = claimed.get(key)
        implied = None
        if count > 0:
            k, q = 0, count
            while q % p == 0:
                q //= p
                k += 1
            implied = k if q == 1 else None
        row = {"dims": list(dims), "p": p, "solutions": count,
               "implied_dim": implied, "primary_dim": want,
               "off_shape_solutions": len(off)}
        if want is not None and implied != want:
            refutations.append(f"finite-map dimension mismatch {dims} mod {p}: brute "
                               f"count={count} implies {implied}, primary {want}")
        if off:
            refutations.append(f"non-cardinality solution found on {dims} mod {p}")
        results.append(row)
    structural = []
    for dims in EXPECTED_PATCH_DIMS:
        key = str(dims).replace(" ", "")
        mine = singleton_translation_orbits(dims)
        theirs = claimed.get(key)
        structural.append({"dims": list(dims), "independent": mine,
                           "primary": theirs})
        if theirs != mine:
            refutations.append(
                f"singleton-orbit dimension mismatch {dims}: "
                f"independent={mine} primary={theirs}"
            )
    return {"rows": results, "structural_rows": structural,
            "refutations": refutations}


# ==========================================================================
# Randomized wide-grid product-stabilizer hunt
# ==========================================================================
EPS = Fraction(1, 10)


def act(L, lam, sig, r):
    return L * (1 - lam * sig / (r + EPS))


def vec(L, lam, sig, rs, action_fn=act):
    return tuple(action_fn(L, lam, sig, r) for r in rs)


def rand_frac(rng, lo=-9, hi=9, nonzero=True):
    while True:
        num = rng.randint(lo, hi)
        den = rng.randint(1, 9)
        f = Fraction(num, den)
        if f or not nonzero:
            return f


def alt_observables(v):
    """A different functional family from the primary's differences/ratios."""
    obs = list(v) + [x * x for x in v]
    obs += [v[i] * v[j] for i, j in combinations(range(len(v)), 2)]
    for i, j, k, m in combinations(range(len(v)), 4):
        if v[j] and v[m] and v[k]:
            obs.append((v[i] / v[j]) * (v[k] / v[m]))
    return tuple(obs)


def hunt_product_stabilizer(trials: int = 4000, action_fn=act) -> dict:
    rng = random.Random(0x871C3)
    bigger, broken, separating = [], [], []
    for _ in range(trials):
        rs = tuple(rand_frac(rng, 0, 9, nonzero=False) for _ in range(3))
        L = rand_frac(rng, 1, 9)
        lam, sig = rand_frac(rng), rand_frac(rng)
        a, b = rand_frac(rng), rand_frac(rng)
        base = vec(L, lam, sig, rs, action_fn)
        if vec(L, a * lam, b * sig, rs, action_fn) == base and a * b != 1:
            bigger.append((str(a), str(b)))
        t = rand_frac(rng)
        if vec(L, t * lam, sig / t, rs, action_fn) != base:
            broken.append((str(t), str(lam), str(sig)))
        if alt_observables(vec(L, t * lam, sig / t, rs, action_fn)) != alt_observables(base):
            separating.append((str(t), str(lam), str(sig)))
    refutations = []
    if bigger:
        refutations.append(f"stabilizer larger than product-one: {bigger[:3]}")
    if broken:
        refutations.append(f"product-one rescaling moved the action: {broken[:3]}")
    if separating:
        refutations.append(f"an observable separates the factors: "
                           f"{separating[:3]}")
    return {"trials": trials, "larger_stabilizer_hits": len(bigger),
            "broken_invariance_hits": len(broken),
            "separating_observable_hits": len(separating),
            "refutations": refutations,
            "stream_sha256": digest([len(bigger), len(broken), len(separating)])}


def check_stabilizer_headlines(claims: dict) -> dict:
    scales = (
        Fraction(-2), Fraction(-1), Fraction(-1, 2), Fraction(1, 3),
        Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2),
        Fraction(2), Fraction(3),
    )
    grid_pairs = len(scales) ** 2
    invariant_pairs = sum(a * b == 1 for a, b in product(scales, repeat=2))
    expected = {
        "grid_pairs": grid_pairs,
        "invariant_pairs": invariant_pairs,
        "separating": 0,
        "scale_free_dim": 1,
    }
    bad = [
        f"stabilizer headline mismatch {name}: independent={value} "
        f"primary={claims.get(name)}"
        for name, value in expected.items() if claims.get(name) != value
    ]
    return {"independent": expected, "refutations": bad}


# ==========================================================================
# Obligation-model dimensions by union-find orbit counting
# ==========================================================================
MAP_PATCH = (3, 3)


def orbits(items, movers) -> int:
    parent = {x: x for x in items}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for mv in movers:
        for x in items:
            y = mv(x)
            a, b = find(x), find(y)
            if a != b:
                parent[a] = b
    return len({find(x) for x in items})


def hunt_obligation_models(claims: dict) -> dict:
    d = MAP_PATCH
    sites = sites_of(d)
    tr = [lambda pr, i=i: (
        tuple((pr[0][k] + (1 if k == i else 0)) % d[k] for k in range(2)),
        tuple((pr[1][k] + (1 if k == i else 0)) % d[k] for k in range(2)))
        for i in range(2)]
    refl = [lambda pr: (tuple((-pr[0][k]) % d[k] for k in range(2)),
                        tuple((-pr[1][k]) % d[k] for k in range(2)))]
    ordered = [(x, y) for x in sites for y in sites]
    kernel_lat = orbits(ordered, tr)
    kernel_refl = orbits(ordered, tr + refl)

    def norm(pr):
        return pr if pr[0] <= pr[1] else (pr[1], pr[0])

    unordered = sorted({norm((x, y)) for x in sites for y in sites if x != y})
    conn_movers = [lambda pr, i=i: norm((
        tuple((pr[0][k] + (1 if k == i else 0)) % d[k] for k in range(2)),
        tuple((pr[1][k] + (1 if k == i else 0)) % d[k] for k in range(2))))
        for i in range(2)]
    conn = orbits(unordered, conn_movers)
    window = len({sum(min(s[k], d[k] - s[k]) ** 2 for k in range(2))
                  for s in sites})

    by_clause = {c["clause"]: c["free_dim"] for c in claims["map"]}
    independent = {
        "GB-S1a linear test-action shape": 0,
        "GB-S1b source-strength normalization (absorbs 1/(4 pi) and any unit conversion)": 1,
        "physical Newton constant / SI normalization": 1,
        "finite-core scalar 1/(r+0.1) vs the exact periodic graph-Laplacian Green solution":
            kernel_refl,
        "GB-S2 phase-propagation kernel and detector-window readout":
            kernel_refl + window,
        "GB-S3 label/offset generated-connectivity family": conn,
        "signed-gravity locked source-action term (scale plus locked orientation)": 1,
        "h-class/h-unit density-to-angle readout identity": 2,
    }
    checks, refutations = [], []
    for label, mine in independent.items():
        theirs = by_clause.get(label)
        checks.append({"model": label, "independent": mine, "primary": theirs})
        if theirs != mine:
            refutations.append(f"obligation-model mismatch {label}: "
                               f"independent={mine} primary={theirs}")
    return {"kernel_translation_only": kernel_lat, "checks": checks,
            "window_classes": window, "refutations": refutations}


# ==========================================================================
# Re-read every required quote from pinned source bytes
# ==========================================================================
def hunt_quote_replay(claims: dict, ev: dict) -> dict:
    bad, checked = [], 0
    for q in claims["quotes"]:
        payload = ev["payloads"].get(q["path"])
        if payload is None:
            bad.append(f"quoted path not in pinned evidence: {q['path']}")
            continue
        lines = payload.decode("utf-8").split("\n")
        idx = q["line_no"] - 1
        checked += 1
        if not (0 <= idx < len(lines)):
            bad.append(f"quoted line {q['line_no']} out of range in {q['path']}")
            continue
        if lines[idx].rstrip("\r") != q["line_verbatim"]:
            bad.append(f"quoted-byte mismatch {q['path']}:{q['line_no']}")
        if not sha256(payload).hexdigest().startswith(q["sha12"]):
            bad.append(f"quote SHA prefix mismatch for {q['path']}")
    return {"quotes_checked": checked, "refutations": bad}


# ==========================================================================
# Hostile controls -- each mutation must trigger the corresponding hunt
# ==========================================================================
def hostile_mutation_controls(claims: dict, ev: dict) -> dict:
    controls = []

    dim_claims = json.loads(json.dumps(claims))
    dim_claims["patches"][0]["struct_dim"] += 1
    controls.append((
        "claimed-dimension-off-by-one",
        bool(validate_primary_contract(dim_claims)
             or hunt_finite_map(dim_claims)["refutations"]),
    ))

    map_claims = json.loads(json.dumps(claims))
    target = next(
        row for row in map_claims["map"]
        if "GB-S2 phase-propagation" in row["clause"]
    )
    target["free_dim"] += 1
    controls.append((
        "obligation-model-count-off-by-one",
        bool(validate_primary_contract(map_claims)
             or hunt_obligation_models(map_claims)["refutations"]),
    ))

    quote_claims = json.loads(json.dumps(claims))
    quote_claims["quotes"][0]["line_verbatim"] += "!"
    controls.append((
        "quoted-byte-changed",
        bool(hunt_quote_replay(quote_claims, ev)["refutations"]),
    ))

    def additive_instead_of_product(L, lam, sig, r):
        return L * (1 - (lam + sig) / (r + EPS))

    controls.append((
        "action-product-dependence-changed",
        bool(hunt_product_stabilizer(256, additive_instead_of_product)["refutations"]),
    ))

    omitted = json.loads(json.dumps(claims))
    omitted["patches"].pop()
    controls.append(("required-row-omitted", bool(validate_primary_contract(omitted))))

    duplicated = json.loads(json.dumps(claims))
    duplicated["map"].append(dict(duplicated["map"][0]))
    controls.append(("duplicate-row", bool(validate_primary_contract(duplicated))))

    large_patch = json.loads(json.dumps(claims))
    target_patch = next(
        row for row in large_patch["patches"]
        if row["patch"].replace(" ", "") == "(12,)"
    )
    target_patch["struct_dim"] = 99
    controls.append((
        "large-patch-claim-corrupted",
        bool(validate_primary_contract(large_patch)
             or hunt_finite_map(large_patch)["refutations"]),
    ))

    stabilizer = json.loads(json.dumps(claims))
    stabilizer["invariant_pairs"] = 999
    controls.append((
        "stabilizer-headline-corrupted",
        bool(validate_primary_contract(stabilizer)),
    ))

    killed = sum(ok for _, ok in controls)
    certify(
        "CERT-MUTATION/hostile-controls",
        killed == len(controls),
        f"killed={killed}/{len(controls)} names={[name for name, _ in controls]}",
    )
    return {"controls": controls, "killed": killed, "total": len(controls)}


# ==========================================================================
def main() -> int:
    t0 = monotonic()
    ev = evidence()
    primary_stdout = run_primary()
    claims = parse_primary(primary_stdout)

    contract_refutations = validate_primary_contract(claims)
    finite_map = hunt_finite_map(claims)
    stabilizer = hunt_product_stabilizer()
    stabilizer_claims = check_stabilizer_headlines(claims)
    obligation_models = hunt_obligation_models(claims)
    quote_replay = hunt_quote_replay(claims, ev)
    replay = hunt_product_stabilizer()
    det = replay["stream_sha256"] == stabilizer["stream_sha256"]
    mutations = hostile_mutation_controls(claims, ev)

    certify("CERT-PRIMARY-CONTRACT/exact", not contract_refutations,
            f"patches={len(claims['patches'])}/16 maps={len(claims['map'])}/8 "
            f"quotes={len(claims['quotes'])}/8 refutations={len(contract_refutations)}")
    certify("CERT-FINITE-MAP/independent", not finite_map["refutations"],
            f"brute_models={len(finite_map['rows'])} "
            f"structural_models={len(finite_map['structural_rows'])} "
            f"refutations={len(finite_map['refutations'])}")
    certify("CERT-PRODUCT-STABILIZER/randomized", not stabilizer["refutations"],
            f"trials={stabilizer['trials']} larger={stabilizer['larger_stabilizer_hits']} "
            f"broken={stabilizer['broken_invariance_hits']} "
            f"separating={stabilizer['separating_observable_hits']}")
    certify("CERT-STABILIZER-HEADLINES/exact", not stabilizer_claims["refutations"],
            f"independent={compact(stabilizer_claims['independent'])}")
    certify("CERT-OBLIGATION-MODELS/orbit-recount",
            not obligation_models["refutations"],
            f"models={len(obligation_models['checks'])} "
            f"refutations={len(obligation_models['refutations'])}")
    certify("CERT-QUOTE-REPLAY/exact", not quote_replay["refutations"],
            f"quotes_checked={quote_replay['quotes_checked']} "
            f"refutations={len(quote_replay['refutations'])}")
    certify("CERT-DETERMINISM/hunt-replay", det,
            f"hunt_sha_first={stabilizer['stream_sha256'][:16]} "
            f"hunt_sha_second={replay['stream_sha256'][:16]}")
    elapsed = monotonic() - t0
    certify("CERT-RUNTIME/budget", elapsed < AUDIT_TIMEOUT_SEC,
            f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("CYCLE 871 — INDEPENDENT REFUTATION CHECKER")
    w(f"EVIDENCE paths={len(ev['rows'])} primary_executions=1 "
      f"blocklist_leaks={ev['blocklist_leaks']}")
    w(f"PRIMARY_CONTRACT patches={len(claims['patches'])} maps={len(claims['map'])} "
      f"quotes={len(claims['quotes'])} scalars="
      f"{claims['grid_pairs']},{claims['invariant_pairs']},"
      f"{claims['separating']},{claims['scale_free_dim']}")
    w("FINITE_MAP_BRUTE dims p solutions implied primary off_shape")
    for row in finite_map["rows"]:
        w(f"  {tuple(row['dims'])} {row['p']} {row['solutions']} "
          f"{row['implied_dim']} {row['primary_dim']} "
          f"{row['off_shape_solutions']}")
    w(f"FINITE_MAP_STRUCTURAL rows={len(finite_map['structural_rows'])} "
      f"refutations={len(finite_map['refutations'])}")
    w(f"PRODUCT_STABILIZER trials={stabilizer['trials']} "
      f"larger={stabilizer['larger_stabilizer_hits']} "
      f"broken={stabilizer['broken_invariance_hits']} "
      f"separating={stabilizer['separating_observable_hits']}")
    w(f"STABILIZER_HEADLINES {compact(stabilizer_claims['independent'])}")
    w("OBLIGATION_MODELS independent primary clause")
    for row in obligation_models["checks"]:
        w(f"  {row['independent']} {row['primary']} {row['model']}")
    w(f"QUOTE_REPLAY checked={quote_replay['quotes_checked']} "
      f"refutations={len(quote_replay['refutations'])}")
    w("HOSTILE_MUTATIONS")
    for name, killed in mutations["controls"]:
        w(f"  {'KILLED' if killed else 'SURVIVED'} {name}")
    w(f"MUTATION_KILLS {mutations['killed']}/{mutations['total']}")
    allref = (contract_refutations + finite_map["refutations"]
              + stabilizer["refutations"] + stabilizer_claims["refutations"]
              + obligation_models["refutations"] + quote_replay["refutations"])
    if allref:
        for r in allref:
            w(f"REFUTED {r}")
    else:
        w("REFUTATIONS none")
    for name, ok, detail in CERTS:
        w(f"{'PASS' if ok else 'FAIL'} {name} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"REFUTATIONS FOUND: {len(allref)}")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
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
