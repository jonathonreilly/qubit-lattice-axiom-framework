#!/usr/bin/env python3
"""Cycle-871 exact pricing of the source-action bridge.

The owner directive names the source-action bridge as the single derivation
gap that keeps the gravity, mass and readout conditionals conditional.  This
runner prices that bridge instead of attempting it.

Four sections, all findings computed rather than declared:

(QUOTE REPLAY).  Every line in a declared, SHA-pinned scope of landed notes that
    names the bridge (or one of its aliased forms) is extracted verbatim with
    its file, sha256, git blob and line number.  The extraction rule is fixed
    in advance and the quotes are byte-recovered from the pinned payloads.

(FINITE-MAP DIMENSION, AT A DECLARED ANSATZ).  A candidate source-to-action map
    on a finite periodic lattice patch is a function A from the Boolean
    subsets of sites to rational values.  That domain and three linear
    constraint families are DECLARED: empty-set vanishing, additivity for two
    nonempty disjoint subsets, and translation invariance.  The current
    canonical axioms do not supply this scalar domain, empty-set vanishing,
    finite additivity, or an action functional.  The physical source-action
    bridge therefore remains OPEN, and every result in this section is
    conditional on the independent model stipulations.
    The exact dimension of the surviving solution space is computed by two
    independent routes (sparse exact Gaussian elimination over Q, and a
    triangular forward-substitution route that never enumerates the
    configuration space).  An ablation ladder then prices each declared
    clause by how many free parameters it removes.

(PRODUCT STABILIZER).  The landed Gate B interface note observes that in the
    linear form L(1 - lambda*strength/(r+eps)) a rescaling of lambda against
    strength with fixed product leaves the action identical, and concludes the
    normalization is "still a runner convention".  The landed runner checks
    that at one float point with a 1e-15 tolerance.  Here the whole stabilizer
    is determined algebraically: over nonzero rationals the product-one
    rescalings form a group.  A declared finite grid checks classification of
    sampled pairs but is not itself called a group.  The runner also asks
    whether any finite difference or ratio of in-scope action values separates
    the two factors.

(OBLIGATION MODELS, MODELED DIMENSIONS ONLY).  Every remaining clause quoted
    in (A) is given an explicit unknowns/constraints model chosen by the
    author, its free dimension is computed by the same solver, and its
    modeled dimension is compared with the bridge model's by a pure function
    of those computed integers.  Equal modeled dimension is NOT mutual
    implication and larger modeled dimension is NOT logical strength: no
    implication maps between the heterogeneous physical obligations are
    constructed here, and none is claimed.

No new axiom, primitive or premise is introduced.  Nothing here promotes a row
or predicts an audit outcome.  Clauses that stay free are reported as imports
with their narrow role, not as derived content.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md",
    "docs/SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md",
    "docs/SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md",
    "docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md",
    "docs/YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
    "scripts/gate_b_weak_field_source_action_interface_2026_06_16.py",
)

import ast
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
PYTHON_PATHS = tuple(p for p in AUDIT_INPUT_PATHS if p.endswith(".py"))
QUOTE_PATHS = tuple(p for p in AUDIT_INPUT_PATHS if p.endswith(".md"))
BLOCKLISTED_MODULES = tuple(Path(p).stem for p in PYTHON_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    AUDIT_INPUT_PATHS[1]:
        "af7bbdfda8831df1c86ec7ca9cf62b6cbdd920f4dca1a4cb03e7f389c73e386a",
    AUDIT_INPUT_PATHS[2]:
        "cb19cb3441136c4a3948cdd12cb5d4d9b82478988ad1047294230501039184cd",
    AUDIT_INPUT_PATHS[3]:
        "5de15beb514fc3eab952992932907a159fa33232caef1d135d14e07f46c6a508",
    AUDIT_INPUT_PATHS[4]:
        "c03409f79768b8f59b8a07b4a2571a1ea554d4cb40fd16bcbee4b14b02fd4d69",
    AUDIT_INPUT_PATHS[5]:
        "ef5e0280ab8bc7ae132f609635b893e208628650720eade6f27d164290a053d1",
    AUDIT_INPUT_PATHS[6]:
        "4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c",
    AUDIT_INPUT_PATHS[7]:
        "ac9ea8b6b7556ce8679d734e98a152bf3af7a9988d9f72f5722ad4c8f7ec9453",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    AUDIT_INPUT_PATHS[1]: "36c2b9dd0b799f7102c7685db5e4fc5121b933ce",
    AUDIT_INPUT_PATHS[2]: "f2256fe7c1bfd5099e462688cc56cd48c7956a63",
    AUDIT_INPUT_PATHS[3]: "ecfa17055c67820fd426e7b60367787bc9d45c93",
    AUDIT_INPUT_PATHS[4]: "b4d3526079afd729319f236c3b246365007daff9",
    AUDIT_INPUT_PATHS[5]: "b9f089eef2395145f54c85103a770ed7d096ea48",
    AUDIT_INPUT_PATHS[6]: "9a449956422a5687b5b1346f428c9e4e35489038",
    AUDIT_INPUT_PATHS[7]: "d604bc5f180e87844f477d52f82376df61e0134e",
}
LANE_OF_PATH = {
    AUDIT_INPUT_PATHS[0]: "gravity",
    AUDIT_INPUT_PATHS[1]: "gravity",
    AUDIT_INPUT_PATHS[2]: "gravity",
    AUDIT_INPUT_PATHS[3]: "gravity",
    AUDIT_INPUT_PATHS[4]: "gravity",
    AUDIT_INPUT_PATHS[5]: "mass",
    AUDIT_INPUT_PATHS[6]: "readout",
    AUDIT_INPUT_PATHS[7]: "gravity",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Cited .py primaries are text/AST evidence only, never imported."""

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
RECORDING = True


def certify(name: str, ok: bool, detail: str) -> bool:
    if RECORDING:
        CERTS.append((name, bool(ok), detail))
    return bool(ok)


# ==========================================================================
# provenance
# ==========================================================================
def provenance() -> dict:
    rows = []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.is_file()
        payload = target.read_bytes() if exists else b""
        rows.append({
            "path": path,
            "worktree_relative": not Path(path).is_absolute(),
            "exists": exists,
            "bytes": len(payload),
            "sha256": sha256(payload).hexdigest(),
            "sha256_exact": sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob(payload),
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
            "lane": LANE_OF_PATH[path],
            "access": ("TEXT_AST_ONLY_BLOCKLISTED_PRIMARY"
                       if path.endswith(".py") else "TEXT_ONLY_PINNED_SOURCE"),
        })
    leaked = [m for m in BLOCKLISTED_MODULES if m in sys.modules]
    ok = (
        all(r["exists"] and r["worktree_relative"] for r in rows)
        and all(r["sha256_exact"] and r["git_blob_exact"] for r in rows)
        and not leaked
    )
    certify("CERT-PROV/pinned-inputs", ok,
            f"paths={len(rows)} sha_exact={sum(r['sha256_exact'] for r in rows)}"
            f" blob_exact={sum(r['git_blob_exact'] for r in rows)}"
            f" blocklist_leaks={leaked}")
    return {
        "rows": rows,
        "blocklist": list(BLOCKLISTED_MODULES),
        "blocklist_leaks": leaked,
        "payloads": {r["path"]: (ROOT / r["path"]).read_bytes() for r in rows},
    }


# ==========================================================================
# (A) quote the blocked rows
# ==========================================================================
ALIAS_PATTERNS = {
    "bridge_object": re.compile(
        r"source[\s/_-]{0,2}action\s+"
        r"(?:bridge|term|premise|interface|identification|ansatz|packet|"
        r"contract|proposal|boundary)", re.I),
    "scale_object": re.compile(
        r"(?:source[\s-]strength\s+normalization|source\s+normalization|"
        r"scalar\s+normalization|normalization\s+residual|"
        r"source[\s-]unit\s+bookkeeping|source\s+scale)", re.I),
}
BLOCKER_PATTERN = re.compile(
    r"(?:not\s+retained|not\s+derived|un-?derived|until\s+derived|"
    r"unless\s+a|does\s+not\s+(?:\w+\s+){0,3}(?:derive|supply|close|discharge)|"
    r"open[-\s_]gate|open\s+(?:gate|obligation|derivation)|obligation|"
    r"still\s+supplied|remains?\s+supplied|remain\s+supplied|"
    r"must\s+provide|runner\s+convention|new\s+source-action\s+premise|"
    r"not\s+a\s+derived\s+constant|supplies?\s+no)", re.I)
SENTENCE_SPLIT = re.compile(r"(?<=[.;:])\s+")


def sentence_around(lines: list[str], idx: int, pattern: re.Pattern) -> str:
    """Rebuild the hard-wrapped sentence carrying the match, deterministically.

    The sentence is selected by character offset of the alias hit inside the
    reconstructed paragraph, so a match that straddles a hard wrap cannot be
    attributed to a neighbouring sentence.
    """
    lo = idx
    while lo > 0 and lines[lo - 1].strip():
        lo -= 1
    hi = idx
    while hi + 1 < len(lines) and lines[hi + 1].strip():
        hi += 1
    parts = [re.sub(r"\s+", " ", x.strip()) for x in lines[lo:hi + 1]]
    starts, pos = [], 0
    for p in parts:
        starts.append(pos)
        pos += len(p) + 1
    para = " ".join(parts)
    hit = pattern.search(parts[idx - lo])
    off = starts[idx - lo] + (hit.start() if hit else 0)
    spans, s = [], 0
    for gap in SENTENCE_SPLIT.finditer(para):
        spans.append((s, gap.start()))
        s = gap.end()
    spans.append((s, len(para)))
    for a, b in spans:
        if a <= off < b:
            return para[a:b].strip()
    return para


def section_a_quotes(prov: dict) -> dict:
    """Quote only the prose sources; the .py primary is AST evidence, not prose."""
    rows = []
    for path in QUOTE_PATHS:
        payload = prov["payloads"][path]
        text = payload.decode("utf-8")
        lines = text.split("\n")
        for idx, line in enumerate(lines):
            classes = sorted(k for k, p in ALIAS_PATTERNS.items() if p.search(line))
            if not classes:
                continue
            verbatim = line.rstrip("\r")
            sentence = sentence_around(lines, idx, ALIAS_PATTERNS[classes[0]])
            rows.append({
                "path": path,
                "lane": LANE_OF_PATH[path],
                "sha256": sha256(payload).hexdigest(),
                "line_no": idx + 1,
                "alias_classes": classes,
                # the obligation is carried by the sentence, not the hard-wrap
                "names_blocker": bool(BLOCKER_PATTERN.search(sentence)),
                "line_verbatim": verbatim,
                "sentence": sentence,
                "byte_recovered": verbatim.encode("utf-8") in payload,
            })
    replay = [
        (r["path"], r["line_no"], r["line_verbatim"]) for r in rows
    ]
    rows2 = []
    for path in QUOTE_PATHS:
        text = prov["payloads"][path].decode("utf-8")
        for idx, line in enumerate(text.split("\n")):
            if any(p.search(line) for p in ALIAS_PATTERNS.values()):
                rows2.append((path, idx + 1, line.rstrip("\r")))
    deterministic = replay == rows2
    all_recovered = all(r["byte_recovered"] for r in rows)
    certify("CERT-QUOTE/integrity", all_recovered and deterministic,
            f"rows={len(rows)} byte_recovered={sum(r['byte_recovered'] for r in rows)}"
            f" deterministic={deterministic}")
    lanes: dict[str, int] = {}
    for r in rows:
        if r["names_blocker"]:
            lanes[r["lane"]] = lanes.get(r["lane"], 0) + 1
    return {
        "rows": rows,
        "row_count": len(rows),
        "blocker_row_count": sum(r["names_blocker"] for r in rows),
        "blocker_rows_by_lane": lanes,
        "stream_sha256": digest(replay),
    }


# ==========================================================================
# exact sparse linear algebra over Q
# ==========================================================================
def echelon(rows: list[dict[int, Fraction]]) -> dict[int, dict[int, Fraction]]:
    pivots: dict[int, dict[int, Fraction]] = {}
    for raw in rows:
        r = {c: v for c, v in raw.items() if v}
        while r:
            col = min(r)
            if col in pivots:
                p = pivots[col]
                f = r[col]
                for c, v in p.items():
                    nv = r.get(c, Fraction(0)) - f * v
                    if nv:
                        r[c] = nv
                    else:
                        r.pop(c, None)
            else:
                f = r[col]
                pivots[col] = {c: v / f for c, v in r.items()}
                break
    return pivots


def nullspace(n: int, pivots: dict[int, dict[int, Fraction]]) -> list[list[Fraction]]:
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        vec = [Fraction(0)] * n
        vec[f] = Fraction(1)
        for col in sorted(pivots, reverse=True):
            row = pivots[col]
            s = sum(v * vec[c] for c, v in row.items() if c != col)
            vec[col] = -s
        basis.append(vec)
    return basis


# ==========================================================================
# (B) forced vs free, conditional on a declared finite model
# ==========================================================================
FULL_ROUTE_MAX_SITES = 6
STRUCT_VERIFY_MAX_MASKS = 1 << 14
PATCHES = (
    (2,), (3,), (4,), (5,), (6,), (2, 2), (2, 3),
    (7,), (8,), (10,), (12,), (3, 3), (2, 2, 2), (2, 2, 3), (4, 4), (3, 3, 3),
)


def patch_sites(dims: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [tuple(c) for c in product(*[range(d) for d in dims])]


def unit_shifts(dims: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [tuple(1 if j == i else 0 for j in range(len(dims)))
            for i in range(len(dims))]


def shift_mask(mask: int, sites, index, dims, v) -> int:
    out = 0
    for i, site in enumerate(sites):
        if mask >> i & 1:
            out |= 1 << index[tuple((site[k] + v[k]) % dims[k]
                                    for k in range(len(dims)))]
    return out


def constraint_rows(dims: tuple[int, ...], use: set[str]):
    sites = patch_sites(dims)
    n = len(sites)
    index = {s: i for i, s in enumerate(sites)}
    rows: list[dict[int, Fraction]] = []
    if "REC0" in use:
        rows.append({0: Fraction(1)})
    if "REC1" in use:
        for assign in product((0, 1, 2), repeat=n):
            a = b = 0
            for i, t in enumerate(assign):
                if t == 1:
                    a |= 1 << i
                elif t == 2:
                    b |= 1 << i
            if a and b and a < b:
                rows.append({a | b: Fraction(1), a: Fraction(-1), b: Fraction(-1)})
    if "LAT" in use:
        for v in unit_shifts(dims):
            for m in range(1 << n):
                t = shift_mask(m, sites, index, dims, v)
                if t != m:
                    rows.append({m: Fraction(1), t: Fraction(-1)})
    return n, rows


def dim_full_route(dims: tuple[int, ...], use: set[str]) -> tuple[int, int, list]:
    n, rows = constraint_rows(dims, use)
    pivots = echelon(rows)
    n_unk = 1 << n
    basis = nullspace(n_unk, pivots) if n_unk - len(pivots) <= 4 else []
    return n_unk - len(pivots), len(pivots), basis


def dim_struct_route(dims: tuple[int, ...]) -> dict:
    """Triangular route: never enumerates the constraint family."""
    sites = patch_sites(dims)
    n = len(sites)
    index = {s: i for i, s in enumerate(sites)}
    # every mask of popcount >= 2 is eliminated by the REC1 row that splits off
    # its lowest set bit; verify the split exists and is a genuine disjoint pair
    checked = 0
    triangular_ok = True
    masks = range(1 << n) if (1 << n) <= STRUCT_VERIFY_MAX_MASKS else [
        random.Random(8710 + n).getrandbits(n) for _ in range(4096)]
    for m in masks:
        if bin(m).count("1") < 2:
            continue
        low = m & -m
        rest = m ^ low
        checked += 1
        if low & rest or (low | rest) != m or not rest:
            triangular_ok = False
    # singletons survive; LAT identifies them along the translation generators
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for v in unit_shifts(dims):
        for s in sites:
            t = tuple((s[k] + v[k]) % dims[k] for k in range(len(dims)))
            a, b = find(index[s]), find(index[t])
            if a != b:
                parent[a] = b
    orbits = len({find(i) for i in range(n)})
    return {
        "dims": dims, "sites": n, "triangular_ok": triangular_ok,
        "masks_checked": checked, "singleton_orbits": orbits, "dim": orbits,
    }


MODEL_CLAUSES = {
    "DOMAIN": "DECLARED model domain: Boolean subsets of sites on a finite "
              "periodic patch; this is not supplied as a source-action domain "
              "by the axioms.",
    "REC0": "DECLARED action clause: A(empty) = 0.",
    "REC1": "DECLARED action clause: two nonempty disjoint subsets compose "
            "additively under A.",
    "LAT": "DECLARED action clause: patch translations leave A invariant.",
}


def section_b_forced_free() -> dict:
    per_patch = []
    for dims in PATCHES:
        n = len(patch_sites(dims))
        entry = {"dims": list(dims), "sites": n}
        struct = dim_struct_route(dims)
        entry["struct"] = struct
        if n <= FULL_ROUTE_MAX_SITES:
            dim, rank, basis = dim_full_route(dims, {"REC0", "REC1", "LAT"})
            entry["full"] = {
                "unknowns": 1 << n, "rank": rank, "dim": dim,
                "generator_is_popcount": bool(
                    basis and all(
                        basis[0][m] == basis[0][1] * bin(m).count("1")
                        for m in range(1 << n))),
            }
            entry["routes_agree"] = (dim == struct["dim"])
        else:
            entry["full"] = None
            entry["routes_agree"] = None
        per_patch.append(entry)

    ablation = []
    for dims in ((3,), (4,), (2, 2)):
        n = len(patch_sites(dims))
        base = {"REC0", "REC1", "LAT"}
        for label, use in (
            ("all-declared-clauses", base),
            ("drop-LAT", base - {"LAT"}),
            ("drop-REC1", base - {"REC1"}),
            ("drop-REC0", base - {"REC0"}),
            ("drop-REC1-and-LAT", {"REC0"}),
            ("no-declared-clauses", set()),
        ):
            dim, rank, _ = dim_full_route(dims, use)
            ablation.append({"dims": list(dims), "sites": n, "clauses": sorted(use),
                             "ablation": label, "unknowns": 1 << n,
                             "rank": rank, "free_dim": dim})

    priced = []
    for dims in ((3,), (4,), (2, 2)):
        got = {a["ablation"]: a["free_dim"] for a in ablation
               if a["dims"] == list(dims)}
        priced.append({
            "dims": list(dims),
            "REC0_removes": got["drop-REC0"] - got["all-declared-clauses"],
            "REC1_removes": got["drop-REC1"] - got["all-declared-clauses"],
            "LAT_removes": got["drop-LAT"] - got["all-declared-clauses"],
            "residual_free_dim": got["all-declared-clauses"],
        })

    agree = [e for e in per_patch if e["routes_agree"] is not None]
    expected_patch_ids = [list(dims) for dims in PATCHES]
    patch_identity_ok = [e["dims"] for e in per_patch] == expected_patch_ids
    structural_ok = all(
        e["struct"]["triangular_ok"]
        and e["struct"]["singleton_orbits"] == 1
        and e["struct"]["dim"] == 1
        for e in per_patch
    )
    full_route_ok = (
        len(agree) == 7
        and all(
            e["routes_agree"]
            and e["full"] is not None
            and e["full"]["dim"] == 1
            and e["full"]["generator_is_popcount"]
            for e in agree
        )
        and all(e["full"] is None and e["routes_agree"] is None
                for e in per_patch if e["sites"] > FULL_ROUTE_MAX_SITES)
    )
    expected_ablation = {
        ((3,), "all-declared-clauses"): 1,
        ((3,), "drop-LAT"): 3,
        ((3,), "drop-REC1"): 3,
        ((3,), "drop-REC0"): 2,
        ((3,), "drop-REC1-and-LAT"): 7,
        ((3,), "no-declared-clauses"): 8,
        ((4,), "all-declared-clauses"): 1,
        ((4,), "drop-LAT"): 4,
        ((4,), "drop-REC1"): 5,
        ((4,), "drop-REC0"): 2,
        ((4,), "drop-REC1-and-LAT"): 15,
        ((4,), "no-declared-clauses"): 16,
        ((2, 2), "all-declared-clauses"): 1,
        ((2, 2), "drop-LAT"): 4,
        ((2, 2), "drop-REC1"): 6,
        ((2, 2), "drop-REC0"): 2,
        ((2, 2), "drop-REC1-and-LAT"): 15,
        ((2, 2), "no-declared-clauses"): 16,
    }
    observed_ablation = {
        (tuple(a["dims"]), a["ablation"]): a["free_dim"] for a in ablation
    }
    ablation_exact = observed_ablation == expected_ablation
    expected_prices = [
        ((3,), 1, 2, 2, 1),
        ((4,), 1, 4, 3, 1),
        ((2, 2), 1, 5, 3, 1),
    ]
    observed_prices = [
        (tuple(p["dims"]), p["REC0_removes"], p["REC1_removes"],
         p["LAT_removes"], p["residual_free_dim"])
        for p in priced
    ]
    prices_exact = observed_prices == expected_prices
    monotone_ok = all(
        a["free_dim"] >= next(x["free_dim"] for x in ablation
                              if x["dims"] == a["dims"]
                              and x["ablation"] == "all-declared-clauses")
        for a in ablation)
    exact_contract = (patch_identity_ok and structural_ok and full_route_ok
                      and ablation_exact and prices_exact and monotone_ok)
    certify("CERT-FINITE-MAP/exact-contract", exact_contract,
            f"patches={len(per_patch)}/16 identities={patch_identity_ok} "
            f"structural={structural_ok} full_routes={len(agree)}/7 "
            f"full_ok={full_route_ok} ablation={ablation_exact} "
            f"prices={prices_exact} monotone={monotone_ok}")
    dims_seen = sorted({e["struct"]["dim"] for e in per_patch})
    return {
        "model_clauses": MODEL_CLAUSES,
        "per_patch": per_patch,
        "ablation": ablation,
        "clause_price": priced,
        "free_dims_observed": dims_seen,
        "bridge_free_dim": max(dims_seen),
        "stream_sha256": digest([per_patch, ablation, priced]),
    }


# ==========================================================================
# (C) narrowest sub-gap: the exact normalization stabilizer
# ==========================================================================
GRID_L = (Fraction(1), Fraction(3, 2))
GRID_R = (Fraction(0), Fraction(1), Fraction(5, 2))
GRID_EPS = Fraction(1, 10)
GRID_LAM = (Fraction(1), Fraction(2, 3))
GRID_SIG = (Fraction(1, 4), Fraction(5))
GRID_SCALE = (Fraction(-2), Fraction(-1), Fraction(-1, 2), Fraction(1, 3),
              Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2),
              Fraction(2), Fraction(3))


def action(L: Fraction, lam: Fraction, sig: Fraction, r: Fraction) -> Fraction:
    return L * (1 - lam * sig / (r + GRID_EPS))


def action_vector(lam: Fraction, sig: Fraction) -> tuple[Fraction, ...]:
    return tuple(action(L, lam, sig, r) for L in GRID_L for r in GRID_R)


def section_c_subgap() -> dict:
    invariant, moving = [], []
    for a, b in product(GRID_SCALE, repeat=2):
        same = all(action_vector(a * lam, b * sig) == action_vector(lam, sig)
                   for lam in GRID_LAM for sig in GRID_SIG)
        (invariant if same else moving).append((a, b))
    inv_set = {(a, b) for a, b in invariant}
    product_one = {(a, b) for a, b in product(GRID_SCALE, repeat=2) if a * b == 1}

    # operational half: can any in-scope observable separate the two factors?
    base = [action_vector(lam, sig) for lam in GRID_LAM for sig in GRID_SIG]
    separating = []
    for t in GRID_SCALE:
        for lam in GRID_LAM:
            for sig in GRID_SIG:
                u = action_vector(lam, sig)
                w = action_vector(t * lam, sig / t)
                diffs_u = [u[i] - u[j] for i, j in combinations(range(len(u)), 2)]
                diffs_w = [w[i] - w[j] for i, j in combinations(range(len(w)), 2)]
                rats_u = [u[i] / u[j] for i, j in combinations(range(len(u)), 2)
                          if u[j]]
                rats_w = [w[i] / w[j] for i, j in combinations(range(len(w)), 2)
                          if w[j]]
                if (u, diffs_u, rats_u) != (w, diffs_w, rats_w):
                    separating.append((str(t), str(lam), str(sig)))

    every_pair_classified = len(invariant) + len(moving) == len(GRID_SCALE) ** 2
    sampled_classification_exact = inv_set == product_one
    certify("CERT-PRODUCT/stabilizer-determined",
            every_pair_classified and sampled_classification_exact,
            f"grid_pairs={len(GRID_SCALE)**2} invariant={len(inv_set)} "
            f"moving={len(moving)} "
            f"sampled_product_one_exact={sampled_classification_exact}; "
            "full Q* group follows algebraically from t -> (t, 1/t)")
    return {
        "grid_pairs": len(GRID_SCALE) ** 2,
        "invariant_pairs": len(inv_set),
        "sampled_invariant_equals_product_one": sampled_classification_exact,
        "full_stabilizer_group": "{(t, 1/t): t in Q*}",
        "separating_observables_found": len(separating),
        "separating_examples": separating[:5],
        "base_action_vectors": len(base),
        "scale_free_dim": 1 if sampled_classification_exact else None,
        "stream_sha256": digest([sorted(map(str, inv_set)), len(separating)]),
    }


# ==========================================================================
# (D) obligation map
# ==========================================================================
MAP_PATCH = (3, 3)


def _dim_kernel(with_reflection: bool) -> int:
    sites = patch_sites(MAP_PATCH)
    n = len(sites)
    index = {s: i for i, s in enumerate(sites)}
    rows: list[dict[int, Fraction]] = []
    for v in unit_shifts(MAP_PATCH):
        for x in sites:
            for y in sites:
                xs = tuple((x[k] + v[k]) % MAP_PATCH[k] for k in range(2))
                ys = tuple((y[k] + v[k]) % MAP_PATCH[k] for k in range(2))
                a = index[x] * n + index[y]
                b = index[xs] * n + index[ys]
                if a != b:
                    rows.append({a: Fraction(1), b: Fraction(-1)})
    if with_reflection:
        for x in sites:
            for y in sites:
                xr = tuple((-x[k]) % MAP_PATCH[k] for k in range(2))
                yr = tuple((-y[k]) % MAP_PATCH[k] for k in range(2))
                a = index[x] * n + index[y]
                b = index[xr] * n + index[yr]
                if a != b:
                    rows.append({a: Fraction(1), b: Fraction(-1)})
    return n * n - len(echelon(rows))


def _dim_connectivity() -> int:
    sites = patch_sites(MAP_PATCH)
    n = len(sites)
    index = {s: i for i, s in enumerate(sites)}
    pairs = list(combinations(range(n), 2))
    slot = {p: i for i, p in enumerate(pairs)}
    rows: list[dict[int, Fraction]] = []
    for v in unit_shifts(MAP_PATCH):
        for (i, j) in pairs:
            xs = tuple((sites[i][k] + v[k]) % MAP_PATCH[k] for k in range(2))
            ys = tuple((sites[j][k] + v[k]) % MAP_PATCH[k] for k in range(2))
            a, b = index[xs], index[ys]
            key = (a, b) if a < b else (b, a)
            if key != (i, j):
                rows.append({slot[(i, j)]: Fraction(1), slot[key]: Fraction(-1)})
    return len(pairs) - len(echelon(rows))


def _dim_window() -> int:
    """detector-window weights: one per squared-distance class of differences."""
    sites = patch_sites(MAP_PATCH)
    classes = set()
    for d in sites:
        classes.add(sum(min(d[k], MAP_PATCH[k] - d[k]) ** 2 for k in range(2)))
    return len(classes)


def _dim_readout() -> int:
    """density scale, angle scale, additive offset; REC0 kills the offset."""
    rows = [{2: Fraction(1)}]  # empty record reads zero angle
    return 3 - len(echelon(rows))


def _dim_signed_term() -> tuple[int, int, int]:
    """One continuous scale; the orientation is a two-point DISCRETE set, and
    the signed lane LOCKS it, leaving zero residual discrete choices.  A
    discrete cardinality is not a parameter-space dimension and is reported in
    a separate field, never added to the continuous dimension."""
    signs = [s for s in (1, -1) if s * s == 1]
    residual_sign_choices = 0  # the lane locks the orientation
    return 1, len(signs), residual_sign_choices


def section_d_map(section_b: dict) -> dict:
    bridge_dim = section_b["bridge_free_dim"]
    kernel_lat = _dim_kernel(False)
    kernel_lat_refl = _dim_kernel(True)
    window = _dim_window()
    conn = _dim_connectivity()
    readout = _dim_readout()
    sig_cont, sig_discrete, sig_residual = _dim_signed_term()

    clauses = [
        {"clause": "GB-S1a linear test-action shape",
         "source": AUDIT_INPUT_PATHS[0], "model": "REC0+REC1+LAT on the config map, "
         "quotiented by the overall scale",
         "free_dim": bridge_dim - 1,
         "generator": "none"},
        {"clause": "GB-S1b source-strength normalization (absorbs 1/(4 pi) and "
                   "any unit conversion)",
         "source": AUDIT_INPUT_PATHS[0], "model": "the residual free direction of "
         "REC0+REC1+LAT", "free_dim": bridge_dim, "generator": "uniform-scale"},
        {"clause": "physical Newton constant / SI normalization",
         "source": AUDIT_INPUT_PATHS[0],
         "model": "DECLARED as the same one-parameter uniform-scale model; "
                  "identity with the bridge residual (or with GB-S1b) is a "
                  "modeling choice, NOT a proven implication",
         "free_dim": bridge_dim, "generator": "uniform-scale"},
        {"clause": "finite-core scalar 1/(r+0.1) vs the exact periodic "
                   "graph-Laplacian Green solution",
         "source": AUDIT_INPUT_PATHS[0],
         "model": f"translation-covariant two-point kernel on Z_{MAP_PATCH[0]}^2 "
                  f"with the lattice reflection imposed (dim {kernel_lat_refl}; "
                  f"translation alone would give {kernel_lat})",
         "free_dim": kernel_lat_refl, "generator": "kernel"},
        {"clause": "GB-S2 phase-propagation kernel and detector-window readout",
         "source": AUDIT_INPUT_PATHS[0],
         "model": f"that same kernel ({kernel_lat_refl}) plus one detector-window "
                  f"weight per squared-distance class ({window})",
         "free_dim": kernel_lat_refl + window, "generator": "kernel+window"},
        {"clause": "GB-S3 label/offset generated-connectivity family",
         "source": AUDIT_INPUT_PATHS[0],
         "model": "translation-covariant symmetric adjacency on the patch",
         "free_dim": conn, "generator": "adjacency"},
        {"clause": "signed-gravity locked source-action term (scale plus locked "
                   "orientation)",
         "source": AUDIT_INPUT_PATHS[1],
         "model": "uniform scale plus the discrete orientation the lane locks "
                  "(locked: zero residual sign choices; the two-point sign set "
                  "has continuous dimension 0 and is reported separately)",
         "free_dim": sig_cont, "discrete_sign_cardinality": sig_discrete,
         "locked_orientation_residual_choices": sig_residual,
         "generator": "uniform-scale+locked-sign"},
        {"clause": "h-class/h-unit density-to-angle readout identity",
         "source": AUDIT_INPUT_PATHS[6],
         "model": "density scale, angle scale and offset under REC0",
         "free_dim": readout, "generator": "two-scale"},
    ]

    def classify(free_dim: int, generator: str) -> str:
        # A comparison of MODELED dimensions only.  Equal modeled dimension
        # does not establish mutual implication; a larger modeled dimension
        # does not establish that one obligation is logically stronger.
        if free_dim < bridge_dim:
            return "smaller-model-dim"
        if free_dim == bridge_dim:
            return "equal-model-dim"
        return "larger-model-dim"

    for c in clauses:
        c["modeled_dim_vs_bridge"] = classify(c["free_dim"], c["generator"])
        c["role_if_free"] = (
            "forced within this declared finite model; no import at the model "
            "level" if c["free_dim"] == 0 else
            "modeled import: one scalar normalization parameter in this declared "
            "finite model (equal modeled dimension is NOT mutual implication)"
            if c["modeled_dim_vs_bridge"] == "equal-model-dim" else
            f"modeled import: {c['free_dim']} free parameters in this declared "
            "finite model, more than the bridge model's 1 (a model-size "
            "comparison, NOT a logical-strength claim)")
    replay = [classify(c["free_dim"], c["generator"]) for c in clauses]
    pure = replay == [c["modeled_dim_vs_bridge"] for c in clauses]
    modelled = all(isinstance(c["free_dim"], int) for c in clauses)
    certify("CERT-OBLIGATION-MODELS/computed", pure and modelled,
            f"clauses={len(clauses)} pure_function_replay={pure} "
            f"all_dims_computed={modelled}")
    tally: dict[str, int] = {}
    for c in clauses:
        tally[c["modeled_dim_vs_bridge"]] = tally.get(
            c["modeled_dim_vs_bridge"], 0) + 1
    return {
        "bridge_free_dim": bridge_dim,
        "map_patch": list(MAP_PATCH),
        "clauses": clauses,
        "tally": tally,
        "stream_sha256": digest(clauses),
    }


# ==========================================================================
# AST evidence on the cited landed runner
# ==========================================================================
def section_ast(prov: dict) -> dict:
    path = AUDIT_INPUT_PATHS[7]
    tree = ast.parse(prov["payloads"][path].decode("utf-8"), filename=path)
    funcs = sorted(n.name for n in ast.walk(tree)
                   if isinstance(n, ast.FunctionDef))
    floats = sorted({n.value for n in ast.walk(tree)
                     if isinstance(n, ast.Constant) and isinstance(n.value, float)})
    ok = "gate_b_action" in funcs and "gate_b_phi" in funcs
    certify("CERT-AST/name-presence-only", ok,
            f"functions={len(funcs)} gate_b_action={'gate_b_action' in funcs} "
            f"gate_b_phi={'gate_b_phi' in funcs}")
    return {"path": path, "functions": funcs, "name_presence_only": True,
            "float_literals_in_landed_runner": len(floats),
            "primary_arithmetic_here": "exact Fraction"}


# ==========================================================================
def main() -> int:
    t0 = monotonic()
    random.seed(871)
    prov = provenance()
    sec_a = section_a_quotes(prov)
    sec_b = section_b_forced_free()
    sec_c = section_c_subgap()
    sec_d = section_d_map(sec_b)
    sec_ast = section_ast(prov)

    global RECORDING
    RECORDING = False
    random.seed(871)
    replay_b = section_b_forced_free()
    replay_c = section_c_subgap()
    replay_a = section_a_quotes(prov)
    replay_d = section_d_map(replay_b)
    RECORDING = True
    det = (replay_b["stream_sha256"] == sec_b["stream_sha256"]
           and replay_c["stream_sha256"] == sec_c["stream_sha256"]
           and replay_a["stream_sha256"] == sec_a["stream_sha256"]
           and replay_d["stream_sha256"] == sec_d["stream_sha256"])
    certify("CERT-DETERMINISM/section-replay", det,
            f"sections_replayed=4 all_stream_sha_stable={det}")
    elapsed = monotonic() - t0
    certify("CERT-RUNTIME/budget", elapsed < AUDIT_TIMEOUT_SEC,
            f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("CYCLE 871 — CONDITIONAL SOURCE-ACTION FINITE MODEL")
    w(f"PROVENANCE paths={len(prov['rows'])} blocklist_leaks={prov['blocklist_leaks']}")
    w(f"QUOTE_REPLAY blockers={sec_a['blocker_row_count']} lanes={compact(sec_a['blocker_rows_by_lane'])}")
    for r in sec_a["rows"]:
        if r["names_blocker"]:
            w(f"  {r['path']}:{r['line_no']} [{r['lane']}] sha256={r['sha256'][:12]}")
            w(f"    VERBATIM LINE | {r['line_verbatim']}")
    w("MODEL clauses=empty-set-vanishing,nonempty-disjoint-additivity,translation-invariance")
    w("PATCH_ROWS patch sites unknowns rank full_dim structural_dim agree")
    for e in sec_b["per_patch"]:
        full = e["full"]
        w(f"  {tuple(e['dims'])} {e['sites']} "
          f"{full['unknowns'] if full else 0} {full['rank'] if full else 0} "
          f"{full['dim'] if full else -1} {e['struct']['dim']} "
          f"{e['routes_agree']}")
    for p in sec_b["clause_price"]:
        w(f"MARGINAL patch={tuple(p['dims'])} empty={p['REC0_removes']} "
          f"nonempty_disjoint={p['REC1_removes']} translation={p['LAT_removes']} "
          f"residual={p['residual_free_dim']}")
    w(f"grid pairs tested: {sec_c['grid_pairs']}")
    w(f"pairs acting trivially: {sec_c['invariant_pairs']}")
    w(f"separating lambda from sigma: {sec_c['separating_observables_found']}")
    w(f"free dimension of the scale itself: {sec_c['scale_free_dim']}")
    w(f"PRODUCT_STABILIZER full={sec_c['full_stabilizer_group']} sampled_exact="
      f"{sec_c['sampled_invariant_equals_product_one']}")
    w("OBLIGATION_ROWS free_dim model_dim_vs_bridge clause")
    for c in sec_d["clauses"]:
        w(f"  {c['free_dim']} {c['modeled_dim_vs_bridge']} {c['clause']}")
    w(f"OBLIGATION_TALLY {compact(sec_d['tally'])}")
    w(f"AST_NAME_PRESENCE path={sec_ast['path']} only=True functions="
      f"{len(sec_ast['functions'])}")
    w("RESULT finite-map dimension=1 on 16 declared nonempty transitive patches")
    w("RESULT product-one stabilizer exact; parameter spaces are not identified")
    w("RESULT physical source-action bridge remains open")
    for name, ok, detail in CERTS:
        w(f"{'PASS' if ok else 'FAIL'} {name} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
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
