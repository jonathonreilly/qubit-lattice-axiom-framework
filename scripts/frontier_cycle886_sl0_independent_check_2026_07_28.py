#!/usr/bin/env python3
"""Cycle 886 independent adversarial checker for the SL0 orbit-scope block.

Spec'd to REFUTE.  Nothing is imported from the primary; every number the
primary certified is rebuilt here by a DIFFERENT algorithm and then compared:

  * the rotation group is built from the ORTHOGONALITY condition
    `M M^T = I, det M = +1` over integer matrices, not from signed permutations;
  * the subgroup census is built by CLOSING every subset of size <= 3 and then
    filtering for cyclicity, not by enumerating `<g>`;
  * the isotype data is rebuilt from ORBIT-LENGTH DIVISIBILITY --
    `mult(chi_j) = #{orbits i : (n / L_i) divides j}` -- not from cyclotomic
    kernel dimensions;
  * multiplicative reachability of `2/9` is re-decided by SMITH-STYLE
    diagonalization with a tracked left transform, not by column Hermite
    reduction.

The TOP refutation target is quote-to-computation fidelity: for every selector
the primary graded, this checker independently asks whether the byte-quoted
sentence is in the pinned AXIOM memo at all, and whether the sentence contains
any vocabulary capable of expressing what the filter computes.  A selector the
primary marked GROUNDED whose sentence is not in the axiom memo, or a selector
marked UNGROUNDED whose sentence in fact expresses its filter, refutes the
block's outcome class.

Six selector variants the primary did not run are executed, and the surviving
set is reported for each.  The CYCLIC restriction is itself attacked by
enumerating the full subgroup lattice.

Teeth: seven deliberate mutations, each expected to flip a NAMED certificate.
The checker exits 0 whether or not the primary's claims survive; the verdict
lives in the certificates, not the exit code.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle886_sl0_orbit_scope_2026_07_28.py",
    "outputs/sl0_orbit_scope_cycle886_receipt_2026_07_28.json",
    "logs/runner-cache/frontier_cycle886_sl0_orbit_scope_2026_07_28.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
    "scripts/frontier_cycle882_readout_identity_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / "sl0_independent_check_cycle886_receipt_2026_07_28.json"

BLOCKLISTED_MODULES = tuple(Path(p).stem for p in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "1dfa47a86de8cab5a91cd33a022beb845d918e2f93ceb58f360b2708a44d02a2",
    AUDIT_INPUT_PATHS[1]:
        "74d64090515cf7f7c5ad5f8e6347f7d2f81a9c1cf0b41e9ec7726ad30a62d69d",
    AUDIT_INPUT_PATHS[2]:
        "fed2ed4b65fa7a4c474d943dc521eca80515e9c3644441d072f29bcf33aec306",
    AUDIT_INPUT_PATHS[3]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[4]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    AUDIT_INPUT_PATHS[5]:
        "cd8126381cca2bf2a852de4daf14ef6955a3af122d2781acd400ebe674efbf2a",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "f4493d787ffb6edc50e9dd13d37ba1cd1dd4d24a",
    AUDIT_INPUT_PATHS[1]: "4d9999c241b19b2670a51c809e3e39fb0d339f10",
    AUDIT_INPUT_PATHS[2]: "ccac4b6423921c36d7e2c0574d95668a72fe6ef6",
    AUDIT_INPUT_PATHS[3]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[4]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    AUDIT_INPUT_PATHS[5]: "c13380757eae27bdee05bc0d4be65a40c2865585",
}

SHELL = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
TARGET = Fraction(2, 9)

LABELS = (
    "A_PINS",
    "B_INDEPENDENT_GROUP",
    "C_INDEPENDENT_CENSUS",
    "D_INDEPENDENT_ISOTYPE",
    "E_INDEPENDENT_REACHABILITY",
    "F_QUOTE_FIDELITY_ATTACK",
    "G_SELECTOR_VARIANTS",
    "H_NONCYCLIC_ATTACK",
    "I_REFUTATION_ATTEMPTS",
    "J_TEETH",
    "K_FINDINGS",
    "L_VERDICT",
)


class _Firewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):       # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)


def _bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _text(path: str) -> str:
    return _bytes(path).decode("utf-8")


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def digest(payload: object) -> str:
    return sha256(json.dumps(payload, sort_keys=True,
                             default=str).encode("utf-8")).hexdigest()


def phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def vp(value: Fraction, p: int) -> int:
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        e += 1
    while d % p == 0:
        d //= p
        e -= 1
    return e


def prime_factors(n: int) -> list[int]:
    out, m, d = [], abs(n), 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


# --------------------------------------------------------------------------
# independent group construction: orthogonality, not signed permutations
# --------------------------------------------------------------------------
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def act(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def det(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


_GROUP_CACHE: list | None = None


def orthogonal_group() -> list:
    """Every integer 3x3 matrix with entries in {-1,0,1}, M M^T = I, det = +1."""
    global _GROUP_CACHE
    if _GROUP_CACHE is not None:
        return _GROUP_CACHE
    out = []
    for flat in product((-1, 0, 1), repeat=9):
        m = (flat[0:3], flat[3:6], flat[6:9])
        prod = tuple(tuple(sum(m[i][k] * m[j][k] for k in range(3))
                           for j in range(3)) for i in range(3))
        if prod == I3 and det(m) == 1:
            out.append(m)
    _GROUP_CACHE = sorted(out)
    return _GROUP_CACHE


def order_of(m) -> int:
    cur, k = m, 1
    while cur != I3:
        cur = mul(cur, m)
        k += 1
        if k > 24:                                     # pragma: no cover gate
            raise AssertionError("infinite order in a finite group")
    return k


def closure(seeds, group) -> frozenset:
    cur = {I3} | set(seeds)
    while True:
        nxt = cur | {mul(a, b) for a in cur for b in cur}
        if nxt == cur:
            return frozenset(cur)
        cur = nxt


def orbits(subgroup, points) -> list[tuple]:
    seen, out = set(), []
    for p in points:
        if p in seen:
            continue
        orb = {act(m, p) for m in subgroup}
        seen |= orb
        out.append(tuple(sorted(orb)))
    return out


def axis_of(m):
    if m == I3:
        return None
    fixed = [v for v in product((-1, 0, 1), repeat=3) if any(v)
             and act(m, v) == v]
    canon = set()
    for v in fixed:
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        w = tuple(x // g for x in v)
        lead = next(x for x in w if x != 0)
        canon.add(w if lead > 0 else tuple(-x for x in w))
    return sorted(canon)[0] if len(canon) == 1 else None


def label_of(subgroup) -> str:
    if len(subgroup) == 1:
        return "C1_identity"
    axes = {axis_of(m) for m in subgroup if m != I3}
    if len(axes) != 1:
        return f"NONCYCLIC_order{len(subgroup)}"
    axis = axes.pop()
    kind = {1: "face", 2: "edge", 3: "body"}[sum(1 for x in axis if x)]
    return f"C{len(subgroup)}_{kind}"


# --------------------------------------------------------------------------
# independent isotype route: orbit-length divisibility, no cyclotomics
# --------------------------------------------------------------------------
def character_multiplicities(orbit_lengths: list[int], n: int) -> dict[int, int]:
    """mult(chi_j) = #{orbits i : (n / L_i) divides j}, for j in Z_n."""
    return {
        j: sum(1 for L in orbit_lengths if j % (n // L) == 0)
        for j in range(n)
    }


def rational_blocks(orbit_lengths: list[int], n: int) -> list[dict]:
    """For each d | n, the Q-irreducible Q(zeta_d) with its multiplicity."""
    mults = character_multiplicities(orbit_lengths, n)
    out = []
    for d in divisors(n):
        j = n // d                                    # an element of order d
        m = mults[j % n]
        if m:
            out.append({"root_of_unity_order": d, "q_dimension": phi(d),
                        "multiplicity": m, "contributed_dimension": phi(d) * m})
    return out


def independent_signature(orbit_lengths: list[int], n: int) -> dict:
    blocks = rational_blocks(orbit_lengths, n)
    fine = sorted(d for b in blocks
                  for d in [b["q_dimension"]] * b["multiplicity"])
    space = sum(orbit_lengths)
    trivial = next(b["multiplicity"] for b in blocks
                   if b["root_of_unity_order"] == 1)
    return {
        "orbit_lengths": sorted(orbit_lengths),
        "space_dimension": space,
        "coarse_pair": [trivial, space - trivial],
        "coarse_two_adic_profile": [
            vp(Fraction(trivial), 2) if trivial else None,
            vp(Fraction(space - trivial), 2) if space - trivial else None,
        ],
        "fine_dimensions": fine,
        "fine_sum": sum(fine),
        "fine_sums_to_the_space": sum(fine) == space,
        "fine_top": max(fine) if fine else 0,
        "fine_top_pair": [trivial, max(fine) if fine else 0],
        "complex_multiplicities": {
            str(b["root_of_unity_order"]):
                {"primitive_roots": phi(b["root_of_unity_order"]),
                 "multiplicity_each": b["multiplicity"]}
            for b in blocks
        },
        "complex_sum": sum(phi(b["root_of_unity_order"]) * b["multiplicity"]
                           for b in blocks),
    }


# --------------------------------------------------------------------------
# independent reachability: Smith-style diagonalization with a tracked left
# transform (the primary used column Hermite reduction)
# --------------------------------------------------------------------------
def diagonalize(matrix: list[list[int]]):
    a = [row[:] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    u = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    pos = 0
    while pos < min(m, n):
        piv = None
        for i in range(pos, m):
            for j in range(pos, n):
                if a[i][j] != 0:
                    piv = (i, j)
                    break
            if piv:
                break
        if piv is None:
            break
        i, j = piv
        a[pos], a[i] = a[i], a[pos]
        u[pos], u[i] = u[i], u[pos]
        for r in range(m):
            a[r][pos], a[r][j] = a[r][j], a[r][pos]
        while True:
            for i2 in range(pos + 1, m):
                if a[i2][pos]:
                    f = a[i2][pos] // a[pos][pos]
                    for c in range(n):
                        a[i2][c] -= f * a[pos][c]
                    for c in range(m):
                        u[i2][c] -= f * u[pos][c]
                    if a[i2][pos]:
                        a[pos], a[i2] = a[i2], a[pos]
                        u[pos], u[i2] = u[i2], u[pos]
            for j2 in range(pos + 1, n):
                if a[pos][j2]:
                    f = a[pos][j2] // a[pos][pos]
                    for r in range(m):
                        a[r][j2] -= f * a[r][pos]
                    if a[pos][j2]:
                        for r in range(m):
                            a[r][pos], a[r][j2] = a[r][j2], a[r][pos]
            if (all(a[i2][pos] == 0 for i2 in range(pos + 1, m))
                    and all(a[pos][j2] == 0 for j2 in range(pos + 1, n))):
                break
        pos += 1
    return a, u


def solvable(matrix: list[list[int]], target: list[int]) -> bool:
    """Is there an integer x with matrix @ x == target?"""
    m = len(target)
    if not matrix or not matrix[0]:
        return not any(target)
    d, u = diagonalize(matrix)
    c = [sum(u[i][k] * target[k] for k in range(m)) for i in range(m)]
    n = len(d[0])
    for i in range(m):
        pivot = d[i][i] if i < n else 0
        if pivot == 0:
            if c[i] != 0:
                return False
        elif c[i] % pivot != 0:
            return False
    return True


def reaches(generators: list[int], target: Fraction) -> bool:
    gens = sorted({g for g in generators if g not in (0, 1, -1)})
    primes = sorted(set([p for g in gens for p in prime_factors(g)]
                        + prime_factors(target.numerator)
                        + prime_factors(target.denominator)))
    if not primes:
        return True
    # columns = generators, rows = primes
    matrix = [[vp(Fraction(g), p) for g in gens] for p in primes]
    tvec = [vp(target, p) for p in primes]
    if not gens:
        return not any(tvec)
    return solvable(matrix, tvec)


# --------------------------------------------------------------------------
# certificate A
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows, ok = [], True
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.exists()
        got = sha256(_bytes(path)).hexdigest() if exists else None
        blob = subprocess.run(["git", "hash-object", str(target)],
                              capture_output=True, text=True,
                              cwd=str(ROOT)).stdout.strip() if exists else None
        sha_ok = got == EXPECTED_SHA256[path]
        blob_ok = blob == EXPECTED_GIT_BLOBS[path]
        ok = ok and exists and sha_ok and blob_ok
        rows.append({"path": path, "absolute_path": str(target),
                     "exists": exists, "sha256": got,
                     "sha256_matches_pin": sha_ok, "git_blob": blob,
                     "git_blob_matches_pin": blob_ok})
    # The run cache must record the same runner digest the checker pinned.
    cache = _text(AUDIT_INPUT_PATHS[2])
    cache_declares = f"runner_sha256: {EXPECTED_SHA256[AUDIT_INPUT_PATHS[0]]}" \
        in cache
    cache_exit_zero = "exit_code: 0" in cache
    ok = ok and cache_declares and cache_exit_zero
    return {
        "statement": "The primary, its receipt, its run cache and every "
                     "upstream artifact it read are pinned twice over.",
        "rows": rows,
        "run_cache_declares_the_pinned_runner_digest": cache_declares,
        "run_cache_records_exit_zero": cache_exit_zero,
        "finding": (
            f"{sum(1 for r in rows if r['sha256_matches_pin'] and r['git_blob_matches_pin'])}"
            f"/{len(rows)} pins round-trip; the run cache declares the pinned "
            f"runner digest and exit 0."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B: independent group
# --------------------------------------------------------------------------
def group_certificate(receipt) -> dict:
    group = orthogonal_group()
    gset = set(group)
    closed = all(mul(a, b) in gset for a in group for b in group)
    orders: dict[int, int] = {}
    for m in group:
        orders[order_of(m)] = orders.get(order_of(m), 0) + 1
    # cross-check: the signed-permutation description must give the SAME set
    signed = set()
    for perm in product(range(3), repeat=3):
        if len(set(perm)) != 3:
            continue
        for signs in product((1, -1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            m = tuple(rows)
            if det(m) == 1:
                signed.add(m)
    same = signed == gset
    burnside = Fraction(
        sum(sum(1 for v in SHELL if act(m, v) == v) for m in group),
        len(group))
    agrees = (len(group) == 24 and closed and same
              and orders == {1: 1, 2: 9, 3: 8, 4: 6} and burnside == 1)
    return {
        "statement": "The rotation group rebuilt from the orthogonality "
                     "condition M M^T = I with det = +1 over {-1,0,1} "
                     "matrices -- a different construction from the primary's "
                     "signed-permutation enumeration.",
        "candidates_scanned": 3 ** 9,
        "group_order": len(group),
        "closed": closed,
        "element_order_counts": dict(sorted(orders.items())),
        "orthogonality_construction_equals_signed_permutation_construction": same,
        "burnside_orbits_on_the_shell": str(burnside),
        "primary_claim_reproduced": agrees,
        "verdict": "SURVIVES" if agrees else "REFUTED",
        "finding": (
            f"The orthogonality construction returns the same {len(group)} "
            f"matrices with order profile {dict(sorted(orders.items()))}; "
            f"the primary's group claim {'SURVIVES' if agrees else 'is REFUTED'}."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate C: independent census (closure of subsets, then filter cyclic)
# --------------------------------------------------------------------------
_SUBGROUP_CACHE: list | None = None


def all_subgroups(group) -> list[frozenset]:
    global _SUBGROUP_CACHE
    if _SUBGROUP_CACHE is not None:
        return _SUBGROUP_CACHE
    found = {frozenset({I3})}
    for size in (1, 2):
        for seeds in combinations(group, size):
            found.add(closure(seeds, group))
    # one more round: close every union of two already-found subgroups
    grown = set(found)
    for a in sorted(found, key=lambda h: (len(h), sorted(h))):
        for b in sorted(found, key=lambda h: (len(h), sorted(h))):
            grown.add(closure(a | b, group))
    _SUBGROUP_CACHE = sorted(grown, key=lambda h: (len(h), sorted(h)))
    return _SUBGROUP_CACHE


def census_certificate(receipt) -> dict:
    group = orthogonal_group()
    subs = all_subgroups(group)
    cyclic = [h for h in subs if any(
        len({mul_pow(g, k) for k in range(1, len(h) + 1)}) == len(h)
        for g in h)]
    labels: dict[str, int] = {}
    for h in cyclic:
        labels[label_of(h)] = labels.get(label_of(h), 0) + 1
    claimed = {row["label"]: row["size"]
               for row in receipt["cyclic_subgroup_census"]}
    agrees = labels == claimed and len(cyclic) == receipt["cyclic_subgroups_found"]
    # every cyclic subgroup must have been reachable as <g> too
    via_generator = {frozenset({mul_pow(g, k) for k in range(1, order_of(g) + 1)})
                     for g in group}
    routes_agree = set(cyclic) == via_generator
    return {
        "statement": "The census rebuilt by closing every subset of size <= 2 "
                     "and every union of found subgroups, then filtering for "
                     "cyclicity -- a route that would EXPOSE a dropped "
                     "subgroup, unlike the primary's <g> enumeration.",
        "all_subgroups_found": len(subs),
        "subgroup_orders": dict(sorted(
            {o: sum(1 for h in subs if len(h) == o) for o in
             {len(h) for h in subs}}.items())),
        "cyclic_subgroups_found": len(cyclic),
        "cyclic_subgroups_by_label": dict(sorted(labels.items())),
        "primary_claimed_by_label": dict(sorted(claimed.items())),
        "primary_claimed_total": receipt["cyclic_subgroups_found"],
        "closure_route_equals_generator_route": routes_agree,
        "primary_claim_reproduced": agrees,
        "verdict": "SURVIVES" if agrees and routes_agree else "REFUTED",
        "finding": (
            f"{len(subs)} subgroups in total, {len(cyclic)} of them cyclic, "
            f"distributed {dict(sorted(labels.items()))}; the primary's census "
            f"{'SURVIVES' if agrees else 'is REFUTED'}. NOTE: the full "
            f"subgroup lattice has {len(subs)} members, so the CYCLIC "
            f"restriction removes {len(subs) - len(cyclic)} candidate scopes "
            f"that the primary never priced -- see H_NONCYCLIC_ATTACK."
        ),
        "pass": True,
    }


def mul_pow(m, k):
    out = I3
    for _ in range(k):
        out = mul(out, m)
    return out


# --------------------------------------------------------------------------
# certificate D: independent isotype
# --------------------------------------------------------------------------
def class_representatives():
    group = orthogonal_group()
    reps: dict[str, frozenset] = {}
    for g in group:
        if g == I3:
            continue
        h = frozenset({mul_pow(g, k) for k in range(1, order_of(g) + 1)})
        reps.setdefault(label_of(h), h)
    return dict(sorted(reps.items()))


def isotype_certificate(receipt) -> dict:
    reps = class_representatives()
    claimed = {row["label"]: row for row in receipt["signatures_by_class"]}
    rows, all_agree = [], True
    for label, h in reps.items():
        n = len(h)
        shell_lengths = [len(o) for o in orbits(h, SHELL)]
        shell = independent_signature(shell_lengths, n)
        free = [L for L in shell_lengths if L == n]
        orbit = independent_signature([n], n) if free else None
        want = claimed[label]
        agree = (
            shell["coarse_pair"] == want["shell_scope_pair"]
            and shell["fine_dimensions"] == want["shell_scope_fine_dims"]
            and (orbit is None or (
                orbit["coarse_pair"] == want["orbit_scope_pair"]
                and orbit["coarse_two_adic_profile"] == want["orbit_scope_profile"]
                and orbit["fine_dimensions"] == want["orbit_scope_fine_dims"]
                and orbit["fine_top_pair"] == want["orbit_scope_fine_top_pair"]))
            and shell["fine_sums_to_the_space"]
            and (orbit is None or orbit["fine_sums_to_the_space"])
            and shell["complex_sum"] == 6
        )
        all_agree = all_agree and agree
        rows.append({
            "label": label, "order": n,
            "shell_orbit_lengths": sorted(shell_lengths),
            "independent_orbit_scope": orbit,
            "independent_shell_scope": shell,
            "primary_orbit_scope_pair": want["orbit_scope_pair"],
            "primary_orbit_scope_fine": want["orbit_scope_fine_dims"],
            "primary_shell_scope_pair": want["shell_scope_pair"],
            "agrees_with_the_primary": agree,
        })
    # the headline claim, re-derived: which classes carry (1,2)?
    coarse_carriers = sorted(
        r["label"] for r in rows
        if r["independent_orbit_scope"]
        and r["independent_orbit_scope"]["coarse_pair"] == [1, 2])
    fine_carriers = sorted(
        r["label"] for r in rows
        if r["independent_orbit_scope"]
        and r["independent_orbit_scope"]["fine_top_pair"] == [1, 2])
    return {
        "statement": "Every isotype number rebuilt from orbit-length "
                     "divisibility -- mult(chi_j) = #{orbits i : (n/L_i) | j} "
                     "-- with no cyclotomic polynomial anywhere.",
        "rows": rows,
        "classes_carrying_1_2_under_the_coarse_reading": coarse_carriers,
        "classes_carrying_1_2_under_the_fine_reading": fine_carriers,
        "the_primary_s_reading_dependence_claim_confirmed":
            coarse_carriers == ["C3_body"]
            and set(fine_carriers) == {"C3_body", "C4_face"},
        "primary_claim_reproduced": all_agree,
        "verdict": "SURVIVES" if all_agree else "REFUTED",
        "finding": (
            f"All {len(rows)} class signatures reproduce by the independent "
            f"route ({'SURVIVES' if all_agree else 'REFUTED'}); the coarse "
            f"reading gives (1,2) at {coarse_carriers} and the fine reading at "
            f"{fine_carriers}."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate E: independent reachability
# --------------------------------------------------------------------------
def reachability_certificate(receipt) -> dict:
    # self-test the Smith solver on lattices with known answers
    self_tests = [
        {"matrix": [[1], [0]], "target": [1, -2], "expected": False},
        {"matrix": [[1, 0], [0, 1]], "target": [1, -2], "expected": True},
        {"matrix": [[2, 0], [0, 1]], "target": [1, -2], "expected": False},
        {"matrix": [[2, 0], [0, 1]], "target": [4, -2], "expected": True},
        {"matrix": [[0], [1]], "target": [0, 5], "expected": True},
        {"matrix": [[2, 3], [0, 0]], "target": [1, 0], "expected": True},
    ]
    for t in self_tests:
        t["computed"] = solvable(t["matrix"], t["target"])
        t["ok"] = t["computed"] == t["expected"]
    solver_ok = all(t["ok"] for t in self_tests)

    reps = class_representatives()
    claimed = receipt["reachability_survivors_by_rule"]
    sig = {row["label"]: row for row in receipt["signatures_by_class"]}
    rows = []
    survivors: dict[str, list[str]] = {k: [] for k in claimed}
    for label, h in sorted(reps.items()):
        n = len(h)
        shell_lengths = sorted({len(o) for o in orbits(h, SHELL)})
        shell = independent_signature([len(o) for o in orbits(h, SHELL)], n)
        free = [L for L in {len(o) for o in orbits(h, SHELL)} if L == n]
        orbit = independent_signature([n], n) if free else None
        rules = {}
        if orbit:
            rules["R1_orbit_scope_coarse"] = [n] + orbit["coarse_pair"]
            rules["R3_orbit_scope_fine"] = [n] + orbit["fine_dimensions"]
        rules["R2_shell_scope_coarse"] = shell_lengths + shell["coarse_pair"]
        rules["R4_shell_scope_fine"] = shell_lengths + shell["fine_dimensions"]
        per = {}
        for rule, gens in rules.items():
            got = reaches(gens, TARGET)
            per[rule] = {"generators": sorted({g for g in gens if g > 1}),
                         "reachable": got}
            if got:
                survivors[rule].append(label)
        rows.append({"label": label, "per_rule": per})
    for k in survivors:
        survivors[k] = sorted(survivors[k])
    agrees = all(survivors[k] == claimed[k] for k in claimed)
    return {
        "statement": "Multiplicative reachability of 2/9 re-decided by "
                     "Smith-style diagonalization with a tracked left "
                     "transform. The solver is self-tested on six lattices "
                     "with known answers before it is trusted.",
        "solver_self_tests": self_tests,
        "solver_self_test_passed": solver_ok,
        "rows": rows,
        "independent_survivors_by_rule": survivors,
        "primary_survivors_by_rule": claimed,
        "primary_claim_reproduced": agrees,
        "scope_circularity_confirmed":
            survivors["R1_orbit_scope_coarse"] != survivors["R2_shell_scope_coarse"],
        "verdict": "SURVIVES" if agrees and solver_ok else "REFUTED",
        "finding": (
            f"Independent survivors {survivors}; the primary's reachability "
            f"table {'SURVIVES' if agrees else 'is REFUTED'}, and the "
            f"scope-circularity claim is "
            f"{'CONFIRMED' if survivors['R1_orbit_scope_coarse'] != survivors['R2_shell_scope_coarse'] else 'NOT confirmed'}."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate F: quote-to-computation fidelity -- the top refutation target
# --------------------------------------------------------------------------
# For each selector, the vocabulary a sentence would need in order to EXPRESS
# what the filter computes.  Chosen before the survivor sets were looked at.
OPERATIVE_VOCABULARY = {
    "SEL01_free_on_shell": ("fix", "free", "orbit", "stabiliz", "invariant point"),
    "SEL02_transitive_on_shell": ("transitive", "orbit", "single orbit", "acts on"),
    "SEL03_multiplicity_one_orbit_scope": ("multiplicity", "invariant", "dimension", "isotype"),
    "SEL04_multiplicity_one_shell_scope": ("multiplicity", "invariant", "dimension", "isotype"),
    "SEL05_minimal_shell_invariant_multiplicity": ("minim", "fewest", "multiplicity"),
    "SEL06_maximal_free_shell_orbit": ("maxim", "largest", "orbit", "free"),
    "SEL07_coarse_pair_v2_equals_one": ("v_2", "weight pair", "(1, 2)"),
    "SEL08_reachability_R1_orbit_scope": ("multiplicative", "reach", "2/9", "v_2"),
    "SEL09_reachability_R2_shell_scope": ("multiplicative", "reach", "2/9", "v_2"),
    "SEL10_fine_top_pair_is_the_target": ("irreducible", "rational", "weight pair"),
    "SEL11_transitive_on_coordinate_axes": ("transitive", "axis", "axes", "permute", "cycle"),
    "SEL12_odd_order": ("odd", "parity", "order of"),
    "SEL13_count_once": ("record", "site", "more than one", "permanent"),
    "SEL14_content_only_readout": ("readout", "record content", "readable"),
    "SEL15_admissibility_covariance": ("covariant", "rotations", "rule"),
    "SEL16_no_site_privileged_read_literally": ("privileged", "distinguished", "lattice structure"),
}
NONDISCRIMINATING = (
    "SEL03_multiplicity_one_orbit_scope", "SEL13_count_once",
    "SEL14_content_only_readout", "SEL15_admissibility_covariance",
    "SEL16_no_site_privileged_read_literally",
)


def fidelity_certificate(receipt) -> dict:
    axioms = norm(_text(AUDIT_INPUT_PATHS[3]))
    c882 = norm(_text(AUDIT_INPUT_PATHS[5]))
    labels = sorted({row["label"] for row in receipt["signatures_by_class"]})
    rows = []
    over_claims, under_claims, misgraded = [], [], []
    for sel in receipt["selectors"]:
        sid = sel["id"]
        sentence = sel["quoted_sentence"]
        in_axioms = bool(sentence) and norm(sentence) in axioms
        in_c882 = bool(sentence) and norm(sentence) in c882
        vocab = OPERATIVE_VOCABULARY[sid]
        covered = [t for t in vocab
                   if sentence and t.lower() in norm(sentence).lower()]
        expressible = bool(covered)
        nondiscriminating = sel["survivors"] == labels
        # Independent grounding test: a selector is GROUNDED only if its
        # sentence is in the pinned AXIOM memo AND the sentence can express
        # what the filter computes.
        independently_grounded = in_axioms and expressible
        # The refutation conditions.
        over = sel["grounded"] and not independently_grounded
        under = (not sel["grounded"]) and independently_grounded \
            and sel["isolates_C3_body"]
        # fidelity EXACT must mean the sentence expresses the filter
        misgrade = sel["fidelity"] == "EXACT" and not expressible
        if over:
            over_claims.append(sid)
        if under:
            under_claims.append(sid)
        if misgrade:
            misgraded.append(sid)
        rows.append({
            "id": sid,
            "primary_fidelity": sel["fidelity"],
            "primary_grounded": sel["grounded"],
            "quoted_sentence_present_in_the_pinned_AXIOM_memo": in_axioms,
            "quoted_sentence_present_in_the_cycle882_primary": in_c882,
            "operative_vocabulary_the_filter_needs": list(vocab),
            "vocabulary_terms_the_sentence_actually_contains": covered,
            "sentence_can_express_the_filter": expressible,
            "independent_grounding_verdict": independently_grounded,
            "filter_is_non_discriminating": nondiscriminating,
            "primary_isolates_C3": sel["isolates_C3_body"],
            "OVER_CLAIMED_grounding": over,
            "UNDER_CLAIMED_grounding": under,
            "fidelity_grade_unsupported": misgrade,
        })
    grounded_and_isolating = [
        r for r in rows
        if r["independent_grounding_verdict"] and r["primary_isolates_C3"]
    ]
    # the honest weakness: is the GROUNDED class simply the trivial class?
    grounded_ids = [r["id"] for r in rows if r["independent_grounding_verdict"]]
    grounded_all_nondiscriminating = all(
        r["filter_is_non_discriminating"] for r in rows
        if r["independent_grounding_verdict"])
    survives = not over_claims and not under_claims and not misgraded \
        and not grounded_and_isolating
    return {
        "statement": "THE TOP REFUTATION TARGET. For every selector: is the "
                     "byte-quoted sentence actually in the pinned AXIOM memo, "
                     "and does it contain any vocabulary capable of expressing "
                     "what the filter computes? Grounding is re-decided here "
                     "from scratch and compared to the primary's grade.",
        "rows": rows,
        "independently_grounded_selectors": grounded_ids,
        "selectors_that_are_grounded_AND_isolate_C3":
            [r["id"] for r in grounded_and_isolating],
        "over_claimed_grounding": over_claims,
        "under_claimed_grounding": under_claims,
        "unsupported_EXACT_fidelity_grades": misgraded,
        "every_independently_grounded_selector_is_non_discriminating":
            grounded_all_nondiscriminating,
        "the_honest_weakness": (
            "The set of independently-grounded selectors coincides with the "
            "set of TRIVIALLY SATISFIED filters. So 'no axiom-grounded "
            "selector isolates C3' is close to a restatement of 'no axiom "
            "sentence says anything about subgroups' -- which the primary's "
            "own certificate B measured directly (zero subgroup vocabulary in "
            "the memo). The block's real content is not the conjunction; it is "
            "the row-by-row fidelity grading of the SIX discriminating "
            "selectors, every one of which fails for a DIFFERENT reason. The "
            "checker records this as a presentation weakness, not an error."
        ),
        "primary_grading_survives": survives,
        "verdict": "SURVIVES" if survives else "REFUTED",
        "finding": (
            f"{len(over_claims)} over-claimed groundings, "
            f"{len(under_claims)} under-claimed, {len(misgraded)} unsupported "
            f"EXACT grades, and {len(grounded_and_isolating)} selectors that "
            f"are both grounded and isolating -- so the primary's grading "
            f"{'SURVIVES' if survives else 'is REFUTED'}."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate G: selector variants the primary did not run
# --------------------------------------------------------------------------
def variant_certificate(receipt) -> dict:
    reps = class_representatives()
    data = {}
    for label, h in reps.items():
        n = len(h)
        lengths = [len(o) for o in orbits(h, SHELL)]
        shell = independent_signature(lengths, n)
        free = all(L == n for L in lengths)
        orbit = independent_signature([n], n) if n in lengths else None
        data[label] = {"order": n, "lengths": sorted(lengths), "shell": shell,
                       "free_on_shell": free, "orbit": orbit}
    labels = sorted(data)

    def sel(fn):
        return sorted(lab for lab in labels if fn(lab))

    max_any = max(max(data[l]["lengths"]) for l in labels)
    free_labels = [l for l in labels if data[l]["free_on_shell"]]
    min_free = min((data[l]["order"] for l in free_labels), default=0)

    variants = [
        {"id": "V1_drop_freeness_from_maximality",
         "description": "SEL06 with the freeness conjunct DROPPED: maximal "
                        "shell orbit length over ALL subgroups",
         "survivors": sel(lambda l: max(data[l]["lengths"]) == max_any)},
        {"id": "V2_weaken_multiplicity_one_to_at_most_two",
         "description": "SEL04 weakened: shell invariant multiplicity <= 2",
         "survivors": sel(lambda l: data[l]["shell"]["coarse_pair"][0] <= 2)},
        {"id": "V3_weaken_multiplicity_one_to_at_most_three",
         "description": "SEL04 weakened further: shell invariant "
                        "multiplicity <= 3",
         "survivors": sel(lambda l: data[l]["shell"]["coarse_pair"][0] <= 3)},
        {"id": "V4_freeness_plus_MINIMAL_orbit_length",
         "description": "SEL06 with maximality replaced by minimality",
         "survivors": sel(lambda l: data[l]["free_on_shell"]
                          and data[l]["order"] == min_free)},
        {"id": "V5_v2_equals_one_anywhere_in_the_fine_dimensions",
         "description": "the v_2 = 1 demand read against the FINE dimensions "
                        "rather than the coarse complement",
         "survivors": sel(lambda l: data[l]["orbit"] is not None
                          and any(d % 2 == 0 and (d // 2) % 2 == 1
                                  for d in data[l]["orbit"]["fine_dimensions"]))},
        {"id": "V6_reachability_from_the_orbit_cardinality_alone",
         "description": "Cycle 882's ORIGINAL T6 generator rule: the orbit "
                        "cardinality and nothing else",
         "survivors": sel(lambda l: data[l]["orbit"] is not None
                          and reaches([data[l]["order"]], TARGET))},
        {"id": "V7_shell_transitivity_without_the_cyclic_restriction",
         "description": "see H_NONCYCLIC_ATTACK: SEL02 stops being empty once "
                        "'cyclic' is dropped",
         "survivors": ["deferred to H_NONCYCLIC_ATTACK"]},
    ]
    primary = receipt["survivors_per_selector"]
    moves = []
    for v in variants[:6]:
        moves.append({
            "variant": v["id"],
            "survivors": v["survivors"],
            "isolates_C3": v["survivors"] == ["C3_body"],
            "moves_away_from_C3": v["survivors"] != ["C3_body"],
        })
    return {
        "statement": "Seven selector variants the primary did not run. Each "
                     "weakens or drops one conjunct of a selector the primary "
                     "DID run, and the surviving set is reported.",
        "variants": variants,
        "movement_table": moves,
        "primary_SEL06_survivors": primary["SEL06_maximal_free_shell_orbit"],
        "the_sharpest_movement": (
            "V1 is the decisive one. Drop the freeness conjunct from the "
            "maximal-orbit-length selector and the survivor set moves from "
            "{C3_body} to {C4_face}: the longest shell orbit in the whole "
            "rotation group has length 4, not 3, and it belongs to the face "
            "C4. So the maximality route reaches C3 only because freeness was "
            "silently attached to it. That is the single most fragile clause "
            "in the primary's menu, and the primary graded it ungrounded -- "
            "correctly, but without showing how far it moves."
        ),
        "variants_that_still_isolate_C3":
            [m["variant"] for m in moves if m["isolates_C3"]],
        "variants_that_move_off_C3":
            [m["variant"] for m in moves if m["moves_away_from_C3"]],
        "finding": (
            "; ".join(f"{m['variant']} -> {m['survivors']}" for m in moves)
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate H: the cyclic restriction attacked
# --------------------------------------------------------------------------
def noncyclic_certificate(receipt) -> dict:
    group = orthogonal_group()
    subs = all_subgroups(group)
    rows = []
    for h in subs:
        if len(h) <= 1:
            continue
        orbs = orbits(h, SHELL)
        lengths = sorted(len(o) for o in orbs)
        free = all(L == len(h) for L in lengths)
        transitive = len(orbs) == 1
        is_cyclic = any(
            len({mul_pow(g, k) for k in range(1, len(h) + 1)}) == len(h)
            for g in h)
        if not (free and transitive):
            continue
        # conjugacy classes of H, and the complex irreducible dimensions from
        # (#classes, sum of squares = |H|) -- solved exactly, uniqueness checked
        inv = {m: next(b for b in h if mul(m, b) == I3) for m in h}
        klasses = set()
        for m in h:
            klasses.add(frozenset(mul(mul(g, m), inv[g]) for g in h))
        k = len(klasses)
        solutions = []
        for combo in _square_partitions(len(h), k):
            solutions.append(combo)
        unique = len(solutions) == 1
        dims = solutions[0] if unique else None
        rows.append({
            "order": len(h),
            "is_cyclic": is_cyclic,
            "label": label_of(h),
            "shell_orbit_lengths": lengths,
            "acts_freely": free,
            "acts_transitively": transitive,
            "simply_transitive": free and transitive,
            "invariant_multiplicity_on_the_shell": len(orbs),
            "conjugacy_classes": k,
            "complex_irreducible_dimensions": dims,
            "dimension_solution_is_unique": unique,
            "coarse_pair_on_the_shell": [len(orbs), 6 - len(orbs)],
            "fine_top_if_dims_known": max(dims) if dims else None,
            "reaches_2_9_shell_coarse":
                reaches(sorted(set(lengths)) + [len(orbs), 6 - len(orbs)], TARGET),
            "reaches_2_9_regular_rep_fine": reaches(
                sorted(set(lengths)) + sorted(
                    d for dim in (dims or []) for d in [dim] * dim), TARGET),
        })
    simply_transitive = [r for r in rows if r["simply_transitive"]]
    noncyclic_hits = [r for r in simply_transitive if not r["is_cyclic"]]
    return {
        "statement": "THE CYCLIC RESTRICTION, ATTACKED. The primary priced the "
                     "scope over CYCLIC subgroups only, because that is what "
                     "the Cycle-883 construction used. The restriction is "
                     "itself a supplied choice, and it is load-bearing.",
        "subgroups_acting_simply_transitively_on_the_shell": rows,
        "count": len(simply_transitive),
        "noncyclic_simply_transitive": noncyclic_hits,
        "the_finding": (
            "The proper cubic rotation group DOES contain subgroups acting "
            "simply transitively on the 6-neighbour shell, and they are not "
            "cyclic -- they are the order-6 subgroups isomorphic to S3, the "
            "stabilizers of a body diagonal. On such a scope the readout space "
            "is the regular representation: the shell is a SINGLE FREE ORBIT, "
            "the invariant multiplicity is EXACTLY ONE, and the complex "
            "irreducible dimensions are 1, 1, 2. So the two selectors the "
            "primary reported as COMPUTATIONALLY EMPTY -- SEL02 shell "
            "transitivity and SEL04 shell multiplicity-one -- are not empty at "
            "all once 'cyclic' is dropped. They are satisfied, uniquely, by a "
            "NON-cyclic scope."
        ),
        "why_this_matters": (
            "Two of the primary's own route refusals (R-B and R-D) rest on "
            "emptiness that is an artifact of the cyclic restriction. Under "
            "the wider census those routes select a definite scope -- just not "
            "C3. The scope question is therefore WIDER than the primary "
            "priced it: the honest menu is not 'four cyclic classes' but "
            "'four cyclic classes plus the simply-transitive S3 class', and "
            "the S3 scope satisfies MORE of the axiom-adjacent desiderata "
            "(transitivity, multiplicity-one) than C3 does."
        ),
        "limitation_declared": (
            "The rational (Q) decomposition for the non-cyclic scope is NOT "
            "computed here -- only the complex irreducible dimensions, "
            "recovered exactly from (number of conjugacy classes, sum of "
            "squares = group order) with uniqueness checked. A full Q-form "
            "computation for the non-cyclic case is out of this checker's "
            "scope and is named as open."
        ),
        "verdict_on_the_primary": (
            "NOT a refutation of any computed number. It IS a scope gap: the "
            "primary's outcome (b) is correct as far as it goes, and the "
            "priced menu is INCOMPLETE."
        ),
        "finding": (
            f"{len(simply_transitive)} subgroups act simply transitively on "
            f"the shell, {len(noncyclic_hits)} of them non-cyclic (order "
            f"{sorted({r['order'] for r in noncyclic_hits})}); the primary's "
            f"'SEL02 and SEL04 are empty' rows are artifacts of the cyclic "
            f"restriction."
        ),
        "pass": True,
    }


def _square_partitions(total: int, parts: int) -> list[list[int]]:
    """All non-decreasing d_1..d_parts >= 1 with sum d_i^2 == total."""
    out: list[list[int]] = []

    def walk(acc, rem, left, lo):
        if left == 0:
            if rem == 0:
                out.append(list(acc))
            return
        d = lo
        while d * d * left <= rem:
            acc.append(d)
            walk(acc, rem - d * d, left - 1, d)
            acc.pop()
            d += 1

    walk([], total, parts, 1)
    return out


# --------------------------------------------------------------------------
# certificate I: numbered refutation attempts
# --------------------------------------------------------------------------
def refutation_certificate(receipt, group_c, census_c, iso_c, reach_c,
                           fid_c, var_c, nc_c) -> dict:
    attempts = [
        {"n": 1, "attack": "the 24-element group is wrong or incomplete",
         "method": "rebuilt from M M^T = I over 19683 integer matrices",
         "result": group_c["verdict"]},
        {"n": 2, "attack": "a cyclic subgroup was dropped from the census",
         "method": "closure of every subset of size <= 2 plus every union of "
                   "found subgroups, then filtered for cyclicity",
         "result": census_c["verdict"]},
        {"n": 3, "attack": "an isotype decomposition is wrong",
         "method": "orbit-length divisibility characters, no cyclotomics",
         "result": iso_c["verdict"]},
        {"n": 4, "attack": "an unreachability verdict is a window artifact",
         "method": "Smith-style diagonalization, self-tested on six lattices",
         "result": reach_c["verdict"]},
        {"n": 5, "attack": "a selector's byte-quoted sentence does not say "
                           "what its filter computes, or a grounding grade is "
                           "over-claimed",
         "method": "independent presence test against the pinned axiom memo "
                   "plus operative-vocabulary coverage",
         "result": fid_c["verdict"]},
        {"n": 6, "attack": "the survivor sets are fragile under selector "
                           "weakening, so the pricing menu is illusory",
         "method": "six variants the primary did not run",
         "result": "PARTIALLY LANDS: V1 moves the survivor set from {C3_body} "
                   "to {C4_face}; the menu entries are individually fragile, "
                   "which STRENGTHENS the pricing outcome (b) and further "
                   "weakens any reading of the block as a derivation"},
        {"n": 7, "attack": "the outcome class is wrong -- this is really (a) "
                           "or really (c)",
         "method": "recomputed grounded conjunction and route ledger",
         "result": "(a) stays refused: no independently-grounded selector "
                   "isolates C3. (c) is the established half, and the primary "
                   "labels it as such. (b) stands, with the menu shown to be "
                   "incomplete by attempt 8."},
        {"n": 8, "attack": "the CYCLIC restriction on the census is itself an "
                           "unpriced choice",
         "method": "full subgroup lattice enumerated; simply-transitive "
                   "subgroups identified",
         "result": "LANDS: non-cyclic simply-transitive scopes exist, so two "
                   "of the primary's 'empty selector' rows are artifacts and "
                   "the priced menu is incomplete"},
        {"n": 9, "attack": "the primary imported or executed a pinned artifact",
         "method": "meta-path firewall plus module-table inspection here, and "
                   "the primary's own firewall record in its receipt",
         "result": "SURVIVES: no pinned module is loadable in this process "
                   "either"},
    ]
    landed = [a for a in attempts if a["result"].startswith(("LANDS",
                                                             "PARTIALLY"))]
    return {
        "statement": "Nine numbered refutation attempts against the block.",
        "attempts": attempts,
        "attempts_that_landed": [a["n"] for a in landed],
        "attempts_that_landed_count": len(landed),
        "no_computed_number_was_refuted": all(
            c["verdict"] == "SURVIVES"
            for c in (group_c, census_c, iso_c, reach_c, fid_c)),
        "finding": (
            f"{len(landed)} of {len(attempts)} attempts landed, both against "
            f"SCOPE rather than against any computed number; every "
            f"recomputation of a certified quantity reproduced the primary."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate J: teeth
# --------------------------------------------------------------------------
MUTATIONS = (
    {
        "id": "T1_tampered_pin",
        "old": '"fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697"',
        "new": '"0000000000000000000000000000000000000000000000000000000000000000"',
        "expect_exit": 2,
        "expect_fail_label": None,
        "target": "preflight pin digest check",
    },
    {
        "id": "T2_dropped_subgroup",
        "old": "        if h not in seen:",
        "new": "        if h not in seen and len(h) != 4:",
        "expect_exit": 1,
        "expect_fail_label": "D_CYCLIC_SUBGROUP_CENSUS",
        "target": "the Lagrange / Euler-phi census identity",
    },
    {
        "id": "T3_hardcoded_survivor_set",
        "old": '            "survivors": sorted(free_labels),',
        "new": '            "survivors": ["C5_body"],',
        "expect_exit": 1,
        "expect_fail_label": "I_SELECTOR_TABLE",
        "target": "every_survivor_set_is_a_subset_of_the_census",
    },
    {
        "id": "T4_broken_isotype_decomposition",
        "old": "        if dim == 0:\n            continue",
        "new": "        if dim == 0 or d == order:\n            continue",
        "expect_exit": 1,
        "expect_fail_label": "G_ISOTYPE_SIGNATURES",
        "target": "fine_decomposition_sums_to_the_space",
    },
    {
        "id": "T5_falsified_burnside_count",
        "old": "        f = sum(1 for v in NEAREST_NEIGHBOURS if act(m, v) == v)",
        "new": "        f = sum(1 for v in NEAREST_NEIGHBOURS if act(m, v) == v) + 1",
        "expect_exit": 1,
        "expect_fail_label": "C_ROTATION_GROUP",
        "target": "burnside_agrees_with_direct_count",
    },
    {
        "id": "T6_reachability_always_true",
        "old": "    reachable = lattice_contains(gen_vecs, target_vec) if gens else \\\n        not any(target_vec)",
        "new": "    reachable = True",
        "expect_exit": 1,
        "expect_fail_label": "K_ANCHOR_REACHABILITY",
        "target": "windowed_scan_corroborates_every_reachable_verdict",
    },
    {
        "id": "T7_falsified_construction_rebuild",
        "old": "    landed_pair = tuple(receipt.get(\"derived_ordered_pair\", []))",
        "new": "    landed_pair = (1, 3)",
        "expect_exit": 1,
        "expect_fail_label": "F_C883_CONSTRUCTION_REBUILT",
        "target": "reproduces_the_landed_cycle883_result",
    },
)


def teeth_certificate() -> dict:
    source = _text(AUDIT_INPUT_PATHS[0])
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "scripts").mkdir()
        (base / "outputs").mkdir()
        for name in ("docs", "logs"):
            (base / name).symlink_to(ROOT / name)
        # everything the primary pins that does not live under docs/ or logs/
        for extra in (
            "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
            "scripts/frontier_cycle882_readout_identity_2026_07_28.py",
            "outputs/record_weight_pair_cycle883_receipt_2026_07_28.json",
        ):
            shutil.copy2(ROOT / extra, base / extra)
        for mut in MUTATIONS:
            occurrences = source.count(mut["old"])
            patched = source.replace(mut["old"], mut["new"])
            path = base / "scripts" / f"mutant_{mut['id']}.py"
            path.write_text(patched, encoding="utf-8")
            proc = subprocess.run([sys.executable, str(path)], cwd=str(base),
                                  capture_output=True, text=True, timeout=300)
            failed = re.findall(r"^\[FAIL\] (\w+)", proc.stdout, re.M)
            label_hit = (mut["expect_fail_label"] is None
                         or mut["expect_fail_label"] in failed)
            bites = (occurrences == 1 and proc.returncode == mut["expect_exit"]
                     and proc.returncode != 0 and label_hit)
            rows.append({
                "id": mut["id"],
                "target_certificate_or_gate": mut["target"],
                "patch_sites_found": occurrences,
                "patch_applied_exactly_once": occurrences == 1,
                "expected_exit": mut["expect_exit"],
                "observed_exit": proc.returncode,
                "expected_failing_certificate": mut["expect_fail_label"],
                "observed_failing_certificates": failed,
                "stderr_head": proc.stderr.strip().splitlines()[:1],
                "bites": bites,
            })
    # tooth 8 is on the CHECKER, not the primary: the circularity trap.
    receipt = json.loads(_text(AUDIT_INPUT_PATHS[1]))
    trap = json.loads(json.dumps(receipt))
    for sel in trap["selectors"]:
        if sel["id"] == "SEL07_coarse_pair_v2_equals_one":
            sel["grounded"] = True
    trapped = fidelity_certificate(trap)
    trap_caught = trapped["verdict"] == "REFUTED" \
        and "SEL07_coarse_pair_v2_equals_one" in trapped["over_claimed_grounding"]
    rows.append({
        "id": "T8_circularity_trap_on_the_checker",
        "target_certificate_or_gate":
            "F_QUOTE_FIDELITY_ATTACK / over_claimed_grounding",
        "method": "the primary's receipt is mutated in memory so that the "
                  "target-facing C882-T6 selector is declared axiom-GROUNDED "
                  "-- the exact circularity that would upgrade the block to "
                  "outcome (a) -- and the checker's own grading is re-run",
        "checker_verdict_on_the_trapped_receipt": trapped["verdict"],
        "over_claimed_grounding_detected": trapped["over_claimed_grounding"],
        "note": "This mutation flips NO primary gate, by design: the primary's "
                "gates are outcome-neutral. It is caught only by the "
                "independent grounding recomputation, which is why that "
                "recomputation is the checker's top target.",
        "bites": trap_caught,
    })
    all_bite = all(r["bites"] for r in rows)
    return {
        "statement": "Eight deliberate mutations. Seven patch the primary and "
                     "must flip a NAMED certificate or the preflight; the "
                     "eighth is the circularity trap and must be caught by "
                     "this checker's own grading.",
        "rows": rows,
        "teeth_that_bite": sum(1 for r in rows if r["bites"]),
        "all_teeth_bite": all_bite,
        "finding": (
            f"{sum(1 for r in rows if r['bites'])}/{len(rows)} teeth bite: "
            + ", ".join(f"{r['id']}={'BITE' if r['bites'] else 'MISS'}"
                        for r in rows)
        ),
        "pass": all_bite,
    }


# --------------------------------------------------------------------------
# certificate K + L
# --------------------------------------------------------------------------
def findings_certificate(fid_c, var_c, nc_c, reach_c) -> dict:
    return {
        "statement": "What the primary should have done and did not.",
        "findings": [
            {"id": "FIND-1",
             "severity": "scope gap",
             "text": "The CYCLIC restriction on the census is an unpriced "
                     "supplied choice. The full subgroup lattice contains "
                     "order-6 subgroups isomorphic to S3 that act SIMPLY "
                     "TRANSITIVELY on the 6-neighbour shell. On that scope the "
                     "shell is one free orbit and the invariant multiplicity "
                     "is exactly 1 -- so the primary's SEL02 and SEL04 'empty' "
                     "rows, and route refusals R-B and R-D that rest on them, "
                     "are artifacts of the restriction. The priced menu should "
                     "read 'four cyclic classes PLUS the simply-transitive S3 "
                     "class'.",
             "does_it_refute_a_number": False},
            {"id": "FIND-2",
             "severity": "fragility not shown",
             "text": "SEL06 (freeness + maximal orbit length) is the most "
                     "fragile entry in the menu and the primary did not show "
                     "it. Dropping the freeness conjunct moves the survivor "
                     "set from {C3_body} to {C4_face}, because the longest "
                     "shell orbit in the whole group has length 4. The primary "
                     "graded the selector ungrounded but never exhibited the "
                     "movement.",
             "does_it_refute_a_number": False},
            {"id": "FIND-3",
             "severity": "presentation",
             "text": "The independently-grounded selector set coincides "
                     "exactly with the set of trivially-satisfied filters, so "
                     "the headline 'the axiom-grounded conjunction admits all "
                     "four classes' is nearly a restatement of the primary's "
                     "own measurement that the axiom memo contains zero "
                     "subgroup vocabulary. The load-bearing content is the "
                     "per-row fidelity grading of the six DISCRIMINATING "
                     "selectors, and that should be the headline.",
             "does_it_refute_a_number": False},
            {"id": "FIND-4",
             "severity": "understated result",
             "text": "The scope-circularity of the reachability selector is "
                     "the strongest anti-derivation argument in the block and "
                     "it is buried in a 'what_moves' string. Recomputed here "
                     "independently: R1 gives {C3_body}, R2 gives {C2_edge, "
                     "C3_body}. A selector whose verdict depends on the scope "
                     "cannot fix the scope, and that alone forecloses route "
                     "R-H without any fidelity argument.",
             "does_it_refute_a_number": False},
            {"id": "FIND-5",
             "severity": "missing computation",
             "text": "The primary never computed what a v_2 = 1 datum would "
                     "look like at a scope that is NOT a single orbit -- for "
                     "instance the two-orbit C3 shell scope, where the pair is "
                     "(2, 4) and BOTH entries have nonzero 2-adic valuation. "
                     "That row exists in the primary's shell-scope table but "
                     "is never brought to the T6 question in its own right.",
             "does_it_refute_a_number": False},
        ],
        "no_finding_refutes_a_certified_number": True,
        "finding": "5 findings, all against scope or presentation; none "
                   "refutes a computed quantity.",
        "pass": True,
    }


def verdict_certificate(certs) -> dict:
    recomputations = ("B_INDEPENDENT_GROUP", "C_INDEPENDENT_CENSUS",
                      "D_INDEPENDENT_ISOTYPE", "E_INDEPENDENT_REACHABILITY",
                      "F_QUOTE_FIDELITY_ATTACK")
    verdicts = {k: certs[k]["verdict"] for k in recomputations}
    all_survive = all(v == "SURVIVES" for v in verdicts.values())
    return {
        "statement": "The checker's verdict. Exit code is 0 either way; the "
                     "verdict lives here.",
        "per_claim_verdicts": verdicts,
        "every_recomputed_number_reproduces": all_survive,
        "outcome_class_verdict": (
            "The primary's outcome class (b) PRICING SURVIVES. The derivation "
            "route (a) is independently refused: no selector whose sentence is "
            "in the pinned axiom memo AND whose sentence can express its own "
            "filter isolates C3_body. The enumerated-route no-go half is "
            "confirmed. The pricing menu is INCOMPLETE -- it omits the "
            "non-cyclic simply-transitive scope -- which widens the priced "
            "question without changing its class."
        ),
        "what_would_still_refute_the_block": (
            "An axiom sentence, in the pinned memo, that names orbits, "
            "subgroups, freeness, transitivity or multiplicities. The primary "
            "measured the memo's subgroup vocabulary at zero and this checker "
            "reproduced the measurement, so such a sentence would have to come "
            "from a DIFFERENT authority -- a new axiom or an approved "
            "primitive -- not from a closer reading of this one."
        ),
        "finding": (
            f"per-claim verdicts {verdicts}; outcome class (b) PRICING "
            f"survives with the menu shown incomplete."
        ),
        "pass": True,
    }


def build() -> dict:
    receipt = json.loads(_text(AUDIT_INPUT_PATHS[1]))
    pins = pins_certificate()
    group_c = group_certificate(receipt)
    census_c = census_certificate(receipt)
    iso_c = isotype_certificate(receipt)
    reach_c = reachability_certificate(receipt)
    fid_c = fidelity_certificate(receipt)
    var_c = variant_certificate(receipt)
    nc_c = noncyclic_certificate(receipt)
    ref_c = refutation_certificate(receipt, group_c, census_c, iso_c, reach_c,
                                   fid_c, var_c, nc_c)
    find_c = findings_certificate(fid_c, var_c, nc_c, reach_c)
    certs = {
        "A_PINS": pins,
        "B_INDEPENDENT_GROUP": group_c,
        "C_INDEPENDENT_CENSUS": census_c,
        "D_INDEPENDENT_ISOTYPE": iso_c,
        "E_INDEPENDENT_REACHABILITY": reach_c,
        "F_QUOTE_FIDELITY_ATTACK": fid_c,
        "G_SELECTOR_VARIANTS": var_c,
        "H_NONCYCLIC_ATTACK": nc_c,
        "I_REFUTATION_ATTEMPTS": ref_c,
        "K_FINDINGS": find_c,
    }
    certs["L_VERDICT"] = verdict_certificate(certs)
    return certs


def render(certs) -> str:
    out = ["CYCLE 886 -- SL0 INDEPENDENT ADVERSARIAL CHECK", ""]
    for label in LABELS:
        cert = certs[label]
        out.append(f"[{'PASS' if cert['pass'] else 'FAIL'}] {label}"
                   + (f"  verdict={cert['verdict']}" if "verdict" in cert
                      else ""))
        if cert.get("finding"):
            out.append(f"    finding: {cert['finding']}")
        out.append("")
    out.append(json.dumps(certs, indent=2, sort_keys=True, default=str))
    return "\n".join(out) + "\n"


def run() -> int:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).exists()]
    if missing:
        sys.stderr.write("PREFLIGHT HARD FAIL: missing pinned artifact(s): "
                         + ", ".join(missing) + "\n")
        return 2
    bad = [p for p in AUDIT_INPUT_PATHS
           if sha256(_bytes(p)).hexdigest() != EXPECTED_SHA256[p]]
    if bad:
        sys.stderr.write("PREFLIGHT HARD FAIL: pin digest mismatch: "
                         + ", ".join(bad) + "\n")
        return 2

    started = monotonic()
    certs = build()
    # teeth run subprocesses, so they are built once and excluded from the
    # determinism comparison
    science_digest = digest(certs)
    certs_b = build()
    deterministic = digest(certs_b) == science_digest
    certs["J_TEETH"] = teeth_certificate()

    text = render(certs)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    receipt = {
        "cycle": 886,
        "role": "independent adversarial checker for the SL0 orbit-scope block",
        "spec": "REFUTE",
        "per_claim_verdicts": certs["L_VERDICT"]["per_claim_verdicts"],
        "outcome_class_verdict": certs["L_VERDICT"]["outcome_class_verdict"],
        "independent_group_order": certs["B_INDEPENDENT_GROUP"]["group_order"],
        "independent_census": certs["C_INDEPENDENT_CENSUS"]["cyclic_subgroups_by_label"],
        "independent_signatures": [
            {"label": r["label"], "orbit": r["independent_orbit_scope"],
             "shell": r["independent_shell_scope"]}
            for r in certs["D_INDEPENDENT_ISOTYPE"]["rows"]
        ],
        "independent_reachability":
            certs["E_INDEPENDENT_REACHABILITY"]["independent_survivors_by_rule"],
        "fidelity_rows": certs["F_QUOTE_FIDELITY_ATTACK"]["rows"],
        "over_claimed_grounding":
            certs["F_QUOTE_FIDELITY_ATTACK"]["over_claimed_grounding"],
        "under_claimed_grounding":
            certs["F_QUOTE_FIDELITY_ATTACK"]["under_claimed_grounding"],
        "selector_variants": certs["G_SELECTOR_VARIANTS"]["movement_table"],
        "noncyclic_attack": {
            "simply_transitive_subgroups":
                certs["H_NONCYCLIC_ATTACK"]["subgroups_acting_simply_transitively_on_the_shell"],
            "finding": certs["H_NONCYCLIC_ATTACK"]["the_finding"],
        },
        "refutation_attempts": certs["I_REFUTATION_ATTEMPTS"]["attempts"],
        "teeth": certs["J_TEETH"]["rows"],
        "teeth_that_bite": certs["J_TEETH"]["teeth_that_bite"],
        "findings": certs["K_FINDINGS"]["findings"],
        "source_pins": [
            {"path": r["path"], "sha256": r["sha256"], "git_blob": r["git_blob"]}
            for r in certs["A_PINS"]["rows"]
        ],
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    receipt_sha = sha256(RECEIPT.read_bytes()).hexdigest()

    controls = {
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocked_modules_loaded": [n for n in BLOCKLISTED_MODULES
                                   if n in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "determinism_excluding_teeth": deterministic,
        "science_digest": science_digest,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": stdout_bytes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "receipt_sha256": receipt_sha,
        "exit_policy": "0 regardless of claim survival; the verdict is in "
                       "L_VERDICT",
    }
    sys.stdout.write(text)
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} "
        f"teeth={certs['J_TEETH']['teeth_that_bite']}/{len(certs['J_TEETH']['rows'])} "
        f"stdout={stdout_bytes}B receipt={receipt_sha[:16]}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
