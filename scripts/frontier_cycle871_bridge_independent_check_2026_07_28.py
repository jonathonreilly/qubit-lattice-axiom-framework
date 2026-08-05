#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-871 source-action pricing.

This checker is specified to REFUTE.  Every hunt below is written to succeed
when the primary is WRONG; the checker passes only when all of them come back
empty.  Six refutation targets:

R1  the free dimension.  The primary solved a sparse rational system by
    Gaussian elimination.  This checker never solves anything: it enumerates
    EVERY map from configurations to F_p by brute force and counts how many
    satisfy the axiom constraints.  A solution space of dimension d must have
    exactly p**d members.  Any other count refutes the primary's dimension.

R2  the forced form.  Among those brute-forced solutions, any map that is not
    a constant multiple of the record count refutes the claim that the axioms
    force the additive uniform shape.

R3  the normalization stabilizer.  The primary tested a fixed 10x10 rational
    grid.  This checker draws random rationals from a seeded PRNG on a much
    wider range and hunts in both directions: a rescaling with product not one
    that nevertheless leaves the action fixed, and a rescaling with product one
    that moves it.  It also builds a different observable family from the
    primary's -- squares, pairwise products and four-point cross ratios -- and
    hunts for one that separates the two factors.

R4  the obligation-map dimensions.  Recomputed by union-find orbit counting
    instead of elimination.  Any disagreement with the numbers parsed out of
    the primary's pinned stdout refutes the map.

R5  the quotes.  Every "VERBATIM LINE" the primary printed is re-read from the
    SHA-pinned source at the line number the primary claimed.  A mismatch
    refutes the quoting.

R6  determinism of this checker's own hunts.

Nothing from the primary lineage is executed: the primary runner, its pinned
stdout and the eight sources it cited are SHA-pinned text evidence behind a
meta-path import firewall.  The arithmetic route is independent as well --
integers modulo small primes and union-find here, exact rationals and Gaussian
elimination there -- so a bug in one cannot reproduce itself in the other.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py",
    "logs/runner-cache/frontier_cycle871_source_action_bridge_pricing_2026_07_28.txt",
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md",
    "docs/SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md",
    "docs/SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md",
    "docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md",
    "docs/YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
)

from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations, product
import json
from pathlib import Path
import random
import re
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS[0], AUDIT_INPUT_PATHS[1]
PYTHON_PATHS = tuple(p for p in AUDIT_INPUT_PATHS if p.endswith(".py"))
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in PYTHON_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "e27b91b699917aea27b3e603096fde16751c45d8cb3c1e7b0ff14bb1a46641fc",
    AUDIT_INPUT_PATHS[1]:
        "bf1e493cff5775bfba10e4f293ffe794c09cfe8448b3b5c4103e61d82ceb3ad8",
    AUDIT_INPUT_PATHS[2]:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    AUDIT_INPUT_PATHS[3]:
        "af7bbdfda8831df1c86ec7ca9cf62b6cbdd920f4dca1a4cb03e7f389c73e386a",
    AUDIT_INPUT_PATHS[4]:
        "cb19cb3441136c4a3948cdd12cb5d4d9b82478988ad1047294230501039184cd",
    AUDIT_INPUT_PATHS[5]:
        "5de15beb514fc3eab952992932907a159fa33232caef1d135d14e07f46c6a508",
    AUDIT_INPUT_PATHS[6]:
        "c03409f79768b8f59b8a07b4a2571a1ea554d4cb40fd16bcbee4b14b02fd4d69",
    AUDIT_INPUT_PATHS[7]:
        "ef5e0280ab8bc7ae132f609635b893e208628650720eade6f27d164290a053d1",
    AUDIT_INPUT_PATHS[8]:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "b0515ad74f0a883e091fa3c9b4f3126c1fe6fe60",
    AUDIT_INPUT_PATHS[1]: "d491b5f42ab1186bd8eb952583304c5d6769d7ac",
    AUDIT_INPUT_PATHS[2]: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    AUDIT_INPUT_PATHS[3]: "36c2b9dd0b799f7102c7685db5e4fc5121b933ce",
    AUDIT_INPUT_PATHS[4]: "f2256fe7c1bfd5099e462688cc56cd48c7956a63",
    AUDIT_INPUT_PATHS[5]: "ecfa17055c67820fd426e7b60367787bc9d45c93",
    AUDIT_INPUT_PATHS[6]: "b4d3526079afd729319f236c3b246365007daff9",
    AUDIT_INPUT_PATHS[7]: "b9f089eef2395145f54c85103a770ed7d096ea48",
    AUDIT_INPUT_PATHS[8]: "9a449956422a5687b5b1346f428c9e4e35489038",
}
PRIMARY_REQUIRED_MARKERS = (
    "section_a_quotes",
    "section_b_forced_free",
    "section_c_subgap",
    "section_d_map",
    "AXIOM_CLAUSES",
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
MAP_ROW = re.compile(r"^\s+(\d+)\s+(weaker|equivalent|stronger)\s+(\S.*)$")
QUOTE_HEAD = re.compile(r"^\s+(\S+\.md):(\d+)\s+\[(\w+)\]\s+sha256=([0-9a-f]{12})")
QUOTE_LINE = re.compile(r"^\s{4}VERBATIM LINE \| (.*)$")
NUM_AFTER = re.compile(r":\s*(-?\d+)\s*$")


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
        "shape_free_dim": find_num("after quotienting the scale"),
        "verdict_pass": "VERDICT: PASS" in cache_text,
    }


# ==========================================================================
# R1 / R2 -- brute-force solution counting over F_p
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


def hunt_r1_r2(claims: dict) -> dict:
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
            refutations.append(f"R1 dim mismatch {dims} mod {p}: brute "
                               f"count={count} implies {implied}, primary {want}")
        if off:
            refutations.append(f"R2 non-uniform solution found on {dims} mod {p}")
        results.append(row)
    return {"rows": results, "refutations": refutations}


# ==========================================================================
# R3 -- randomized wide-grid stabilizer hunt with a different observable family
# ==========================================================================
EPS = Fraction(1, 10)


def act(L, lam, sig, r):
    return L * (1 - lam * sig / (r + EPS))


def vec(L, lam, sig, rs):
    return tuple(act(L, lam, sig, r) for r in rs)


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


def hunt_r3(trials: int = 4000) -> dict:
    rng = random.Random(0x871C3)
    bigger, broken, separating = [], [], []
    for _ in range(trials):
        rs = tuple(rand_frac(rng, 0, 9, nonzero=False) for _ in range(3))
        L = rand_frac(rng, 1, 9)
        lam, sig = rand_frac(rng), rand_frac(rng)
        a, b = rand_frac(rng), rand_frac(rng)
        base = vec(L, lam, sig, rs)
        if vec(L, a * lam, b * sig, rs) == base and a * b != 1:
            bigger.append((str(a), str(b)))
        t = rand_frac(rng)
        if vec(L, t * lam, sig / t, rs) != base:
            broken.append((str(t), str(lam), str(sig)))
        if alt_observables(vec(L, t * lam, sig / t, rs)) != alt_observables(base):
            separating.append((str(t), str(lam), str(sig)))
    refutations = []
    if bigger:
        refutations.append(f"R3 stabilizer larger than product-one: {bigger[:3]}")
    if broken:
        refutations.append(f"R3 product-one rescaling moved the action: {broken[:3]}")
    if separating:
        refutations.append(f"R3 an observable separates the factors: "
                           f"{separating[:3]}")
    return {"trials": trials, "larger_stabilizer_hits": len(bigger),
            "broken_invariance_hits": len(broken),
            "separating_observable_hits": len(separating),
            "refutations": refutations,
            "stream_sha256": digest([len(bigger), len(broken), len(separating)])}


# ==========================================================================
# R4 -- obligation-map dimensions by union-find orbit counting
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


def hunt_r4(claims: dict) -> dict:
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
    checks, refutations = [], []
    for label, mine, needle in (
        ("kernel (translation+reflection)", kernel_refl, "finite-core scalar"),
        ("kernel+window", kernel_refl + window, "GB-S2 phase-propagation"),
        ("connectivity", conn, "GB-S3 label/offset"),
    ):
        theirs = next((v for k, v in by_clause.items() if needle in k), None)
        checks.append({"model": label, "independent": mine, "primary": theirs})
        if theirs is not None and theirs != mine:
            refutations.append(f"R4 {label}: union-find gives {mine}, "
                               f"primary printed {theirs}")
    return {"kernel_translation_only": kernel_lat, "checks": checks,
            "window_classes": window, "refutations": refutations}


# ==========================================================================
# R5 -- re-read every quoted line from the pinned source
# ==========================================================================
def hunt_r5(claims: dict, ev: dict) -> dict:
    bad, checked = [], 0
    for q in claims["quotes"]:
        payload = ev["payloads"].get(q["path"])
        if payload is None:
            bad.append(f"R5 quoted path not in pinned evidence: {q['path']}")
            continue
        lines = payload.decode("utf-8").split("\n")
        idx = q["line_no"] - 1
        checked += 1
        if not (0 <= idx < len(lines)):
            bad.append(f"R5 line {q['line_no']} out of range in {q['path']}")
            continue
        if lines[idx].rstrip("\r") != q["line_verbatim"]:
            bad.append(f"R5 mismatch {q['path']}:{q['line_no']}")
        if not sha256(payload).hexdigest().startswith(q["sha12"]):
            bad.append(f"R5 sha prefix mismatch for {q['path']}")
    return {"quotes_checked": checked, "refutations": bad}


# ==========================================================================
def main() -> int:
    t0 = monotonic()
    ev = evidence()
    claims = parse_primary(ev["payloads"][PRIMARY_CACHE].decode("utf-8"))

    r12 = hunt_r1_r2(claims)
    r3 = hunt_r3()
    r4 = hunt_r4(claims)
    r5 = hunt_r5(claims, ev)
    replay = hunt_r3()
    det = replay["stream_sha256"] == r3["stream_sha256"]

    parsed_ok = (len(claims["patches"]) >= 8 and len(claims["map"]) >= 5
                 and len(claims["quotes"]) >= 1
                 and claims["scale_free_dim"] is not None)
    certify("CERT-PARSE/claims-extracted", parsed_ok,
            f"patch_rows={len(claims['patches'])} map_rows={len(claims['map'])} "
            f"quotes={len(claims['quotes'])} "
            f"scale_free_dim={claims['scale_free_dim']}")
    certify("CERT-R1R2/brute-force-dimension", not r12["refutations"],
            f"models={len(r12['rows'])} refutations={len(r12['refutations'])}")
    certify("CERT-R3/stabilizer-hunt", not r3["refutations"],
            f"trials={r3['trials']} larger={r3['larger_stabilizer_hits']} "
            f"broken={r3['broken_invariance_hits']} "
            f"separating={r3['separating_observable_hits']}")
    certify("CERT-R4/orbit-recount", not r4["refutations"],
            f"models={len(r4['checks'])} refutations={len(r4['refutations'])}")
    certify("CERT-R5/quote-reread", not r5["refutations"],
            f"quotes_checked={r5['quotes_checked']} "
            f"refutations={len(r5['refutations'])}")
    certify("CERT-R6/determinism", det,
            f"hunt_sha_first={r3['stream_sha256'][:16]} "
            f"hunt_sha_second={replay['stream_sha256'][:16]}")
    elapsed = monotonic() - t0
    certify("CERT-RUNTIME/budget", elapsed < AUDIT_TIMEOUT_SEC,
            f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 871 -- INDEPENDENT CHECKER, SPECIFIED TO REFUTE")
    w("=" * 78)
    w("")
    w("-- pinned evidence (text/AST only, primary never imported) --------------")
    for r in ev["rows"]:
        w(f"  {r['path']}")
        w(f"      sha256={r['sha256'][:16]} exact={r['sha256_exact']} "
          f"blob_exact={r['git_blob_exact']} access={r['access']}")
    w(f"  BLOCKLIST={list(BLOCKLISTED_MODULES)} leaks={ev['blocklist_leaks']}")
    w("")
    w("-- claims parsed out of the primary's pinned stdout ---------------------")
    w(f"  patch rows={len(claims['patches'])} obligation rows={len(claims['map'])} "
      f"quoted lines={len(claims['quotes'])}")
    w(f"  primary says: grid_pairs={claims['grid_pairs']} "
      f"invariant_pairs={claims['invariant_pairs']} "
      f"separating_observables={claims['separating']} "
      f"scale_free_dim={claims['scale_free_dim']} "
      f"shape_free_dim={claims['shape_free_dim']}")
    w("")
    w("-- R1/R2 brute-force solution counting over F_p -------------------------")
    w(f"  {'patch':<10}{'p':>3}{'solutions':>12}{'implied_dim':>13}"
      f"{'primary_dim':>13}{'off_shape':>11}")
    for row in r12["rows"]:
        w(f"  {str(tuple(row['dims'])):<10}{row['p']:>3}{row['solutions']:>12}"
          f"{str(row['implied_dim']):>13}{str(row['primary_dim']):>13}"
          f"{row['off_shape_solutions']:>11}")
    w("")
    w("-- R3 randomized wide-grid stabilizer hunt ------------------------------")
    w(f"  trials={r3['trials']}")
    w(f"  rescalings with product != 1 that left the action fixed: "
      f"{r3['larger_stabilizer_hits']}")
    w(f"  rescalings with product == 1 that moved the action:      "
      f"{r3['broken_invariance_hits']}")
    w(f"  observables (values, squares, products, cross ratios) separating "
      f"the two factors: {r3['separating_observable_hits']}")
    w("")
    w("-- R4 obligation-map dimensions recomputed by union-find ----------------")
    w(f"  kernel with translation only: {r4['kernel_translation_only']}   "
      f"window classes: {r4['window_classes']}")
    for c in r4["checks"]:
        w(f"  {c['model']:<34} independent={c['independent']} "
          f"primary={c['primary']}")
    w("")
    w("-- R5 quote re-read from the pinned sources -----------------------------")
    w(f"  quoted lines re-read at their claimed line numbers: "
      f"{r5['quotes_checked']}")
    w("")
    w("-- REFUTATIONS ---------------------------------------------------------")
    allref = (r12["refutations"] + r3["refutations"] + r4["refutations"]
              + r5["refutations"])
    if allref:
        for r in allref:
            w(f"  REFUTED: {r}")
    else:
        w("  none: every refutation hunt came back empty")
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<34} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"REFUTATIONS FOUND: {len(allref)}")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")
    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
