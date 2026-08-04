#!/usr/bin/env python3
"""Cycle 886: SL0 -- is the C3 orbit scope FORCED, or PRICED?

Cycle 883 derived SL1: over one lattice-realized C3 orbit the record's readout
space carries the ordered weight pair `(1, 2)` -- the C3 isotype split `1 + 2`,
no free parameter.  Cycle 883 also named its own residual, SL0, in its own
words (byte-quoted and pinned below):

    "C2, C3 and C4 subgroups are ALL supplied by the same Lattice clause, so
    the axioms alone do not choose n."

This cycle attacks SL0 and only SL0.  The question, exactly: for which cyclic
subgroups `C` of the proper cubic rotation group does the Cycle-883
construction produce a readout carrying a weight pair, and what selects `C3`?

(A) THE CENSUS, EXACT.  The 24 proper cubic rotations are rebuilt from scratch
    as the determinant-`+1` signed permutation matrices, the group axioms are
    checked exhaustively (all 576 products, all 13824 associativity triples,
    inverses, orders), and EVERY cyclic subgroup is enumerated -- 17 of them --
    together with their conjugacy classes under the full group.  The census is
    gated against the Lagrange / Euler-phi identity
    `#cyclic subgroups of order d = #elements of order d / phi(d)` and against
    Burnside's orbit count on the 6-neighbour shell.  Subgroup CLASS LABELS
    (face-C2, edge-C2, body-C3, face-C4) are DERIVED from each generator's
    integer rotation axis, never hardcoded.

(B) THE SIGNATURES, EXACT.  For every nontrivial cyclic subgroup, at two
    scopes -- one maximal free orbit (Cycle 883's own scope) and the whole
    6-neighbour shell -- the runner computes the orbit structure, the invariant
    (trivial-isotype) multiplicity BY TWO INDEPENDENT ROUTES (exact nullspace of
    `P - I`, and Burnside averaging over the subgroup), the coarse ordered
    weight pair `(invariant, complement)`, the FINE decomposition into rational
    irreducibles via exact cyclotomic kernel dimensions `dim ker Phi_d(P)`, the
    complex weight multiset, and the 2-adic profile of the pair.  Every
    decomposition is gated to sum back to the space dimension.

(C) THE SELECTION QUESTION, AS DATA.  Sixteen candidate selectors are run as
    filters over the census.  Each carries a byte-quoted sentence (or an
    explicit `NONE`), what that sentence SAYS, what the filter COMPUTES, and a
    quote-to-computation FIDELITY grade.  The surviving set of each selector is
    reported as data, and the conjunction is taken twice: over the
    axiom-GROUNDED selectors only, and over every non-empty selector.

(D) THE BRIDGE, RECOMPUTED.  Cycle 882's `C882-T6` anchor-reachability question
    is recomputed here from scratch -- never cited -- for every subgroup, under
    four explicitly stated generator rules, using exact integer-lattice
    membership (Hermite-style column reduction over the prime valuation
    lattice), so unreachability is PROVED rather than window-bounded.

(E) THE PRICE.  If no axiom-grounded selector isolates `C3`, the honest output
    is the exact menu of supplied clauses that DO isolate it, each with its
    named consequences, plus the signature of every rival scope.

All cited primaries are SHA-256 and git-blob pinned, read as text/AST only, and
blocked from import by a meta-path firewall.  Every certified quantity is exact
(`int` / `Fraction`); no floating point enters any certificate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 400_000

# Literal, greppable, and pinned below.
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
    "scripts/frontier_cycle882_readout_identity_2026_07_28.py",
    "logs/runner-cache/record_weight_pair_cycle883_receipt_2026_07_28.json",
    "docs/RECORD_WEIGHT_PAIR_DERIVED_CYCLE883_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "outputs/record_weight_pair_cycle883_receipt_2026_07_28.json",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import product
import json
from math import gcd
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "outputs" / "sl0_orbit_scope_cycle886_receipt_2026_07_28.json"

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    AUDIT_INPUT_PATHS[2]:
        "cd8126381cca2bf2a852de4daf14ef6955a3af122d2781acd400ebe674efbf2a",
    AUDIT_INPUT_PATHS[3]:
        "b12e382a4a408bd3fe518bb47aca83083a27e0180355128b3a76b5282accd511",
    AUDIT_INPUT_PATHS[4]:
        "d2f6544cbe9c4022a41b149e874b2507d0e59d3c5bf793b6c14941455b9c9b0f",
    AUDIT_INPUT_PATHS[5]:
        "973d18d9aa2e05a2decac79ddd8a6f245d923e9a94d772baf80869228ca27d60",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[1]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
    AUDIT_INPUT_PATHS[2]: "c13380757eae27bdee05bc0d4be65a40c2865585",
    AUDIT_INPUT_PATHS[3]: "86e923ae910a02cad84eb756e5a255b97d820f0e",
    AUDIT_INPUT_PATHS[4]: "fd5c708967c03fced5ff349b9636164861cd1c04",
    AUDIT_INPUT_PATHS[5]: "d4290cbe8cfedf965fad828dc673e8fee2e75cd5",
}

# --------------------------------------------------------------------------
# Verbatim needles.  Each is quoted from a pinned artifact; if the artifact
# stops containing it character for character (after whitespace normalization)
# the pins certificate fails.
# --------------------------------------------------------------------------
AXIOM_SENTENCES = {
    "lattice_rotations":
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site.",
    "no_site_privileged":
        "No site is privileged. Sites are distinguished by the supplied "
        "lattice structure alone.",
    "admissibility_covariance":
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations.",
    "count_once":
        "A site never carries more than one record; records are permanent.",
    "content_only_readout":
        "Only records are readable. A readout value is determined by record "
        "content alone.",
    "finite_additive_readout":
        "For any finite collection of pairwise-disjoint records, scalar "
        "readout `I` is additive, with `I(empty)=0`.",
    "law_privileges_no_states":
        "A law privileges no states.",
    "only_named_primitive_content":
        "These axioms state only their named primitive content.",
    "unfixed_choice_stays_conditional":
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency.",
    "axioms_and_primitives_complete":
        "Axioms and approved primitives are the complete supplied foundation.",
}

# Cycle 883's own statement of SL0, byte-quoted from its source (AST string
# constants).  This is the residual this cycle attacks.
C883_SL0_NEEDLES = {
    "sl0_residual":
        "C2, C3 and C4 subgroups are ALL supplied by the same Lattice clause, "
        "so the axioms alone do not choose n. What chooses n = 3 here is the "
        "obligation's own scope: Cycle 882 pins the object as 'one registered "
        "full C3 orbit' with ORBIT_LENGTH = 3. The derivation is therefore "
        "exact AT the pinned scope and carries a named upstream dependency "
        "(the C3 scope) rather than a hidden one.",
    "sl0_same_clause":
        "A C3 subgroup is axiom-supplied, not imported. Note the honest "
        "consequence carried forward: C2 and C4 subgroups are supplied by the "
        "SAME clause, which is why certificate I must compute what pairs they "
        "give.",
}

# Cycle 882's escape condition, byte-quoted from its source.  This is the
# ORIGIN of the v_2 = 1 selector -- and it is an obligation sentence, not an
# axiom sentence.  That distinction is the whole point of certificate I.
C882_T6_NEEDLE = (
    "A Record-facing datum with v_2 = 1 must enter. Concretely: derive that "
    "the charged-lepton record carries the fixed-locus weight pair (1, 2) as "
    "Record content. That is a sharper successor target than 'derive h-class'."
)

# Recomputed here, never imported.
TARGET_ANCHOR = Fraction(2, 9)
TARGET_PAIR = (1, 2)

NEAREST_NEIGHBOURS = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1),
)
COORDINATE_AXES = ("x", "y", "z")

FIDELITY_GRADES = ("EXACT", "PARTIAL", "NONE")
OUTCOME_CLASSES = ("a_DERIVATION", "b_PRICING", "c_NO_GO")

LABELS = (
    "A_PINS",
    "B_AXIOM_SENTENCES",
    "C_ROTATION_GROUP",
    "D_CYCLIC_SUBGROUP_CENSUS",
    "E_SHELL_ORBIT_STRUCTURE",
    "F_C883_CONSTRUCTION_REBUILT",
    "G_ISOTYPE_SIGNATURES",
    "H_CLASS_INVARIANCE",
    "I_SELECTOR_TABLE",
    "J_CONJUNCTIONS",
    "K_ANCHOR_REACHABILITY",
    "L_ROUTE_LEDGER",
    "M_PRICE",
    "N_IMPOSTOR_STRESS",
    "O_OUTCOME",
)


# --------------------------------------------------------------------------
# import firewall: cited primaries are evidence, never libraries
# --------------------------------------------------------------------------
class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):       # pragma: no cover legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers -- exact arithmetic only
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def digest(payload: object) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def vp(value: Fraction, p: int) -> int | None:
    """p-adic valuation of a nonzero rational; None at zero."""
    if value == 0:
        return None
    n, d, e = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        e += 1
    while d % p == 0:
        d //= p
        e -= 1
    return e


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def euler_phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


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


# ---- exact integer/rational linear algebra ----
def identity_matrix(m: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]


def mat_mul_int(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def mat_add_scaled(a, b, c: int):
    return [[a[i][j] + c * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def mat_pow_int(a, e: int):
    out = identity_matrix(len(a))
    for _ in range(e):
        out = mat_mul_int(out, a)
    return out


def rank_exact(rows: list[list[Fraction]]) -> int:
    matrix = [[Fraction(x) for x in row] for row in rows]
    if not matrix or not matrix[0]:
        return 0
    width = len(matrix[0])
    rank = 0
    for col in range(width):
        pivot = None
        for r in range(rank, len(matrix)):
            if matrix[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        head = matrix[rank][col]
        matrix[rank] = [x / head for x in matrix[rank]]
        for r in range(len(matrix)):
            if r != rank and matrix[r][col] != 0:
                factor = matrix[r][col]
                matrix[r] = [a - factor * b
                             for a, b in zip(matrix[r], matrix[rank])]
        rank += 1
    return rank


def kernel_dimension(matrix) -> int:
    """dim ker over Q of a square integer matrix."""
    m = len(matrix)
    return m - rank_exact([[Fraction(x) for x in row] for row in matrix])


# ---- exact integer polynomials, cyclotomics ----
def poly_divide(num: list[int], den: list[int]) -> list[int]:
    """Exact integer polynomial division (low->high coefficients)."""
    num = list(num)
    out = [0] * (len(num) - len(den) + 1)
    for i in range(len(out) - 1, -1, -1):
        coeff, lead = num[i + len(den) - 1], den[-1]
        if coeff % lead != 0:                          # pragma: no cover gate
            raise AssertionError("inexact polynomial division")
        c = coeff // lead
        out[i] = c
        for j, dv in enumerate(den):
            num[i + j] -= c * dv
    if any(num):                                       # pragma: no cover gate
        raise AssertionError("nonzero polynomial remainder")
    return out


_CYCLO_CACHE: dict[int, list[int]] = {}


def cyclotomic(n: int) -> list[int]:
    """Phi_n(x) coefficients, low->high, by exact division of x^n - 1."""
    if n in _CYCLO_CACHE:
        return _CYCLO_CACHE[n]
    poly = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n):
        if d == n:
            continue
        poly = poly_divide(poly, cyclotomic(d))
    _CYCLO_CACHE[n] = poly
    return poly


def poly_of_matrix(coeffs: list[int], p_matrix) -> list[list[int]]:
    m = len(p_matrix)
    acc = [[0] * m for _ in range(m)]
    for k, c in enumerate(coeffs):
        if c == 0:
            continue
        acc = mat_add_scaled(acc, mat_pow_int(p_matrix, k), c)
    return acc


# ---- exact integer-lattice membership (proves UNreachability) ----
def lattice_contains(gen_valuations: list[list[int]], target: list[int]) -> bool:
    """Is `target` an integer combination of the generator valuation vectors?

    `gen_valuations[i]` is generator i's valuation vector indexed by prime, so
    each entry is already a COLUMN of the lattice matrix.  Column-style Hermite
    reduction with Euclidean pivoting, then exact back-substitution.  This is a
    PROOF of membership or non-membership, not a windowed search.
    """
    cols = [list(vec) for vec in gen_valuations]
    rows = len(target)
    pool = [c for c in cols if any(c)]
    pivots: list[tuple[int, list[int]]] = []
    for i in range(rows):
        while True:
            nz = [c for c in pool if c[i] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda c: abs(c[i]))
            base = nz[0]
            for other in nz[1:]:
                factor = other[i] // base[i]
                for r in range(rows):
                    other[r] -= factor * base[r]
        nz = [c for c in pool if c[i] != 0]
        if nz:
            piv = nz[0]
            pool = [c for c in pool if c is not piv and any(c)]
            pivots.append((i, piv))
    residual = list(target)
    for i, piv in pivots:
        if residual[i] % piv[i] != 0:
            return False
        factor = residual[i] // piv[i]
        for r in range(rows):
            residual[r] -= factor * piv[r]
    return not any(residual)


def multiplicative_group_reaches(generators: list[int],
                                 target: Fraction) -> dict:
    """Exact test: is `target` in the multiplicative group <generators>?"""
    gens = sorted({g for g in generators if g not in (0, 1, -1)})
    primes = sorted(set(
        [p for g in gens for p in prime_factors(g)]
        + prime_factors(target.numerator)
        + prime_factors(target.denominator)
    ))
    gen_vecs = [[vp(Fraction(g), p) for p in primes] for g in gens]
    target_vec = [vp(target, p) for p in primes]
    reachable = lattice_contains(gen_vecs, target_vec) if gens else \
        not any(target_vec)
    return {
        "generators": gens,
        "primes": primes,
        "generator_valuation_vectors": gen_vecs,
        "target_valuation_vector": target_vec,
        "reachable": reachable,
    }


# --------------------------------------------------------------------------
# certificate A: pins
# --------------------------------------------------------------------------
def pins_certificate() -> dict:
    rows, ok = [], True
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        exists = target.exists()
        got_sha = sha256(_read_bytes(path)).hexdigest() if exists else None
        try:
            blob = subprocess.run(
                ["git", "hash-object", str(target)],
                capture_output=True, text=True, cwd=str(ROOT), check=True,
            ).stdout.strip() if exists else None
        except Exception:                              # pragma: no cover gate
            blob = None
        sha_ok = got_sha == EXPECTED_SHA256[path]
        blob_ok = blob == EXPECTED_GIT_BLOBS[path]
        ok = ok and exists and sha_ok and blob_ok
        rows.append({
            "path": path,
            "absolute_path": str(target),
            "exists": exists,
            "sha256": got_sha,
            "sha256_matches_pin": sha_ok,
            "git_blob": blob,
            "git_blob_matches_pin": blob_ok,
        })
    return {
        "statement": (
            "Every cited artifact is pinned by absolute path, SHA-256 and git "
            "blob, and is read as text/AST/JSON only. A missing or moved pin "
            "is a hard preflight failure (exit 2)."
        ),
        "rows": rows,
        "read_mode": "text/AST/JSON only; import blocked by meta-path firewall",
        "finding": (
            f"{sum(1 for r in rows if r['sha256_matches_pin'] and r['git_blob_matches_pin'])}"
            f"/{len(rows)} pinned artifacts round-trip on both SHA-256 and git "
            f"blob."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B: the axiom sentences, byte-quoted
# --------------------------------------------------------------------------
def axiom_sentences_certificate() -> dict:
    axioms = norm(_read_text(AUDIT_INPUT_PATHS[0]))
    rows, ok = [], True
    for key, sentence in sorted(AXIOM_SENTENCES.items()):
        present = norm(sentence) in axioms
        ok = ok and present
        rows.append({
            "id": key,
            "byte_quoted_sentence": sentence,
            "present_in_pinned_axiom_memo": present,
        })

    def _constants(path: str) -> list[str]:
        tree = ast.parse(_read_text(path))
        return [n.value for n in ast.walk(tree)
                if isinstance(n, ast.Constant) and isinstance(n.value, str)]

    c883_constants = {norm(s) for s in _constants(AUDIT_INPUT_PATHS[1])}
    c882_constants = {norm(s) for s in _constants(AUDIT_INPUT_PATHS[2])}
    sl0_rows = []
    for key, sentence in sorted(C883_SL0_NEEDLES.items()):
        present = norm(sentence) in c883_constants
        ok = ok and present
        sl0_rows.append({
            "id": key,
            "byte_quoted_from": AUDIT_INPUT_PATHS[1],
            "sentence": sentence,
            "recovered_by_ast": present,
        })
    t6_present = norm(C882_T6_NEEDLE) in c882_constants
    ok = ok and t6_present

    # The decisive textual fact for this cycle, computed rather than asserted:
    # the axiom memo contains no subgroup / orbit / isotype vocabulary at all.
    scope_vocabulary = (
        "subgroup", "cyclic", "orbit", "isotype", "irreducible",
        "multiplicity", "C2", "C3", "C4", "body diagonal", "stabilizer",
        "representation", "weight pair", "free action",
    )
    vocab_rows = [{"term": term,
                   "occurrences_in_axiom_memo": axioms.lower().count(term.lower())}
                  for term in scope_vocabulary]
    vocabulary_absent = all(r["occurrences_in_axiom_memo"] == 0
                            for r in vocab_rows)
    rotation_mentions = axioms.count("proper cubic rotations")
    return {
        "statement": (
            "The sentences this cycle is allowed to quote, recovered verbatim "
            "from the pinned artifacts. Also computed: whether the axiom memo "
            "contains ANY vocabulary capable of naming a subgroup scope."
        ),
        "axiom_sentences": rows,
        "cycle883_sl0_statements": sl0_rows,
        "cycle882_t6_escape_condition": {
            "sentence": C882_T6_NEEDLE,
            "byte_quoted_from": AUDIT_INPUT_PATHS[2],
            "recovered_by_ast": t6_present,
            "class": "OBLIGATION sentence, not an axiom sentence",
        },
        "scope_vocabulary_scan": vocab_rows,
        "axiom_memo_has_no_subgroup_vocabulary": vocabulary_absent,
        "occurrences_of_proper_cubic_rotations": rotation_mentions,
        "what_this_establishes": (
            "The axiom memo names the proper cubic rotations as a WHOLE "
            f"{rotation_mentions} times (Lattice and Admissibility) and never "
            "names a subgroup, an orbit, an isotype or a multiplicity. Any "
            "selector that discriminates among cyclic subgroups therefore has "
            "to be built on TOP of the axiom text, and certificate I grades "
            "exactly how far each one is from its quoted sentence."
        ),
        "finding": (
            f"{sum(1 for r in rows if r['present_in_pinned_axiom_memo'])}"
            f"/{len(rows)} axiom sentences round-trip byte for byte; Cycle "
            f"883's two SL0 statements and Cycle 882's T6 escape condition are "
            f"recovered by AST; the axiom memo's subgroup vocabulary count is "
            f"{sum(r['occurrences_in_axiom_memo'] for r in vocab_rows)}."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate C: the proper cubic rotation group, rebuilt and checked
# --------------------------------------------------------------------------
def signed_permutation_matrices() -> list[tuple[tuple[int, ...], ...]]:
    out = []
    for perm in product(range(3), repeat=3):
        if len(set(perm)) != 3:
            continue
        for signs in product((1, -1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            out.append(tuple(rows))
    return out


def det3(m) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def mul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def act(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


IDENTITY3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def element_order(m) -> int:
    cur, k = m, 1
    while cur != IDENTITY3:
        cur = mul(cur, m)
        k += 1
        if k > 24:                                     # pragma: no cover gate
            raise AssertionError("not a finite rotation")
    return k


def proper_rotations() -> list:
    return sorted(m for m in signed_permutation_matrices() if det3(m) == 1)


def rotation_axis(m) -> tuple[int, ...] | None:
    """The primitive integer axis of a nonidentity rotation, canonically signed."""
    if m == IDENTITY3:
        return None
    candidates = [v for v in product((-1, 0, 1), repeat=3)
                  if any(v) and act(m, v) == v]
    prim = []
    for v in candidates:
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        prim.append(tuple(x // g for x in v))
    canon = set()
    for v in prim:
        lead = next(x for x in v if x != 0)
        canon.add(v if lead > 0 else tuple(-x for x in v))
    if len(canon) != 1:                                # pragma: no cover gate
        raise AssertionError(f"axis not unique: {sorted(canon)}")
    return canon.pop()


def rotation_group_certificate() -> dict:
    group = proper_rotations()
    gset = set(group)
    closed = all(mul(a, b) in gset for a in group for b in group)
    products_checked = len(group) ** 2
    associative = all(
        mul(mul(a, b), c) == mul(a, mul(b, c))
        for a in group for b in group for c in group
    )
    triples_checked = len(group) ** 3
    inverses = all(
        any(mul(a, b) == IDENTITY3 for b in group) for a in group
    )
    all_det_one = all(det3(m) == 1 for m in group)
    orders: dict[int, int] = {}
    for m in group:
        orders[element_order(m)] = orders.get(element_order(m), 0) + 1
    order_counts = dict(sorted(orders.items()))
    lagrange = all(len(group) % d == 0 for d in order_counts)

    # Burnside on the 6-neighbour shell for the FULL group.
    fixed_counts = {}
    total_fixed = 0
    for m in group:
        f = sum(1 for v in NEAREST_NEIGHBOURS if act(m, v) == v)
        total_fixed += f
        fixed_counts.setdefault(f, 0)
        fixed_counts[f] += 1
    burnside_orbits = Fraction(total_fixed, len(group))
    shell_orbits_direct = len(orbits_of_group(group, NEAREST_NEIGHBOURS))
    burnside_ok = burnside_orbits == shell_orbits_direct == 1

    ok = (
        len(group) == 24 and closed and associative and inverses
        and all_det_one and lagrange and burnside_ok
        and order_counts == {1: 1, 2: 9, 3: 8, 4: 6}
    )
    return {
        "statement": (
            "GATE C886-G1. The Lattice axiom's 'proper cubic rotations about "
            "each site' rebuild as the 24 determinant-one signed permutation "
            "matrices on Z^3. Group axioms are checked exhaustively and "
            "Burnside's count is verified on the 6-neighbour shell."
        ),
        "axiom_sentence_used": AXIOM_SENTENCES["lattice_rotations"],
        "signed_permutation_matrices": len(signed_permutation_matrices()),
        "proper_rotations": len(group),
        "closure_products_checked": products_checked,
        "closed_under_composition": closed,
        "associativity_triples_checked": triples_checked,
        "associative": associative,
        "every_element_has_an_inverse_in_the_group": inverses,
        "every_element_has_determinant_plus_one": all_det_one,
        "element_order_counts": order_counts,
        "every_element_order_divides_the_group_order": lagrange,
        "shell_fixed_point_histogram": dict(sorted(fixed_counts.items())),
        "sum_of_fixed_points_over_the_group": total_fixed,
        "burnside_orbit_count_on_the_shell": q(burnside_orbits),
        "orbit_count_computed_directly": shell_orbits_direct,
        "burnside_agrees_with_direct_count": burnside_ok,
        "finding": (
            f"{len(group)} proper rotations, order profile {order_counts}, "
            f"{products_checked} products and {triples_checked} associativity "
            f"triples verified; Burnside gives {q(burnside_orbits)} orbit on "
            f"the shell, matching the direct count {shell_orbits_direct}."
        ),
        "pass": ok,
    }


def orbits_of_group(elements, points) -> list[tuple]:
    seen, out = set(), []
    for p in points:
        if p in seen:
            continue
        orbit = set()
        frontier = [p]
        while frontier:
            cur = frontier.pop()
            if cur in orbit:
                continue
            orbit.add(cur)
            for m in elements:
                nxt = act(m, cur)
                if nxt not in orbit:
                    frontier.append(nxt)
        seen |= orbit
        out.append(tuple(sorted(orbit)))
    return out


# --------------------------------------------------------------------------
# certificate D: the cyclic subgroup census
# --------------------------------------------------------------------------
def cyclic_subgroup(generator) -> frozenset:
    out, cur = set(), generator
    while True:
        out.add(cur)
        if cur == IDENTITY3:
            break
        cur = mul(cur, generator)
    return frozenset(out)


def class_label(subgroup: frozenset) -> str:
    """DERIVED label: order plus the integer type of the rotation axis."""
    order = len(subgroup)
    if order == 1:
        return "C1_identity"
    axes = {rotation_axis(m) for m in subgroup if m != IDENTITY3}
    if len(axes) != 1:                                 # pragma: no cover gate
        raise AssertionError("cyclic subgroup with more than one axis")
    axis = axes.pop()
    weight = sum(1 for x in axis if x != 0)
    kind = {1: "face", 2: "edge", 3: "body"}[weight]
    return f"C{order}_{kind}"


def build_census() -> list[dict]:
    group = proper_rotations()
    seen: dict[frozenset, dict] = {}
    for m in group:
        h = cyclic_subgroup(m)
        if h not in seen:
            gens = sorted(x for x in h if cyclic_subgroup(x) == h)
            seen[h] = {
                "elements": h,
                "order": len(h),
                "generators": gens,
                "axis": rotation_axis(gens[0]) if len(h) > 1 else None,
                "label": class_label(h),
            }
    return sorted(seen.values(), key=lambda r: (r["order"], r["label"],
                                                sorted(r["elements"])))


def conjugacy_classes(census: list[dict]) -> dict[frozenset, int]:
    group = proper_rotations()
    inverse = {m: next(b for b in group if mul(m, b) == IDENTITY3)
               for m in group}
    keys = [r["elements"] for r in census]
    remaining = set(keys)
    classes: dict[frozenset, int] = {}
    idx = 0
    for key in keys:
        if key not in remaining:
            continue
        orbit = set()
        for g in group:
            conj = frozenset(mul(mul(g, h), inverse[g]) for h in key)
            orbit.add(conj)
        for member in orbit:
            classes[member] = idx
            remaining.discard(member)
        idx += 1
    return classes


def census_certificate(census, classes) -> dict:
    group = proper_rotations()
    order_counts: dict[int, int] = {}
    for m in group:
        order_counts[element_order(m)] = \
            order_counts.get(element_order(m), 0) + 1
    predicted = {d: order_counts[d] // euler_phi(d) for d in sorted(order_counts)}
    observed: dict[int, int] = {}
    for row in census:
        observed[row["order"]] = observed.get(row["order"], 0) + 1
    phi_identity = predicted == observed
    exact_division = all(order_counts[d] % euler_phi(d) == 0
                         for d in order_counts)

    every_closed = all(
        all(mul(a, b) in row["elements"] for a in row["elements"]
            for b in row["elements"])
        for row in census
    )
    every_has_identity = all(IDENTITY3 in row["elements"] for row in census)
    every_cyclic = all(
        any(cyclic_subgroup(g) == row["elements"] for g in row["elements"])
        for row in census
    )
    lagrange = all(24 % row["order"] == 0 for row in census)

    class_rows: dict[int, dict] = {}
    for row in census:
        idx = classes[row["elements"]]
        entry = class_rows.setdefault(idx, {
            "class_index": idx, "label": row["label"], "order": row["order"],
            "size": 0, "axes": [],
        })
        entry["size"] += 1
        if row["axis"] is not None:
            entry["axes"].append(list(row["axis"]))
    class_table = [class_rows[i] for i in sorted(class_rows)]
    for entry in class_table:
        entry["axes"] = sorted(entry["axes"])
    labels_constant_on_classes = all(
        len({row["label"] for row in census
             if classes[row["elements"]] == entry["class_index"]}) == 1
        for entry in class_table
    )
    class_sizes_sum = sum(e["size"] for e in class_table)

    ok = (
        len(census) == 17 and phi_identity and exact_division and every_closed
        and every_has_identity and every_cyclic and lagrange
        and labels_constant_on_classes and class_sizes_sum == len(census)
        and len(class_table) == 5
    )
    return {
        "statement": (
            "GATE C886-G2. Every cyclic subgroup of the proper cubic rotation "
            "group is enumerated and grouped into conjugacy classes. "
            "Completeness is gated by the Lagrange / Euler-phi identity "
            "#{cyclic subgroups of order d} = #{elements of order d} / phi(d)."
        ),
        "cyclic_subgroups_found": len(census),
        "element_order_counts": dict(sorted(order_counts.items())),
        "euler_phi_by_order": {d: euler_phi(d) for d in sorted(order_counts)},
        "predicted_cyclic_subgroups_by_order": predicted,
        "observed_cyclic_subgroups_by_order": dict(sorted(observed.items())),
        "phi_identity_holds": phi_identity,
        "element_counts_divide_exactly_by_phi": exact_division,
        "every_subgroup_closed_under_composition": every_closed,
        "every_subgroup_contains_the_identity": every_has_identity,
        "every_subgroup_has_a_generator_of_its_own_order": every_cyclic,
        "every_subgroup_order_divides_24": lagrange,
        "conjugacy_class_table": class_table,
        "conjugacy_classes": len(class_table),
        "class_sizes_sum_to_the_census": class_sizes_sum == len(census),
        "derived_labels_constant_on_conjugacy_classes":
            labels_constant_on_classes,
        "census": [
            {"label": row["label"], "order": row["order"],
             "axis": list(row["axis"]) if row["axis"] else None,
             "generators": len(row["generators"]),
             "class_index": classes[row["elements"]],
             "elements": [[list(r) for r in m] for m in sorted(row["elements"])]}
            for row in census
        ],
        "finding": (
            f"{len(census)} cyclic subgroups in {len(class_table)} conjugacy "
            f"classes: "
            + ", ".join(f"{e['label']} x{e['size']}" for e in class_table)
            + f"; the phi identity {predicted} matches the observed census "
              f"{dict(sorted(observed.items()))}."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate E: shell orbit structure per subgroup
# --------------------------------------------------------------------------
def subgroup_shell_orbits(subgroup: frozenset) -> list[tuple]:
    return orbits_of_group(sorted(subgroup), NEAREST_NEIGHBOURS)


def shell_orbit_certificate(census, classes) -> dict:
    rows = []
    for row in census:
        orbs = subgroup_shell_orbits(row["elements"])
        lengths = sorted(len(o) for o in orbs)
        free = all(len(o) == row["order"] for o in orbs)
        fixed = [list(v) for v in NEAREST_NEIGHBOURS
                 if all(act(m, v) == v for m in row["elements"])]
        transitive = len(orbs) == 1
        # orbit-stabilizer: every orbit length divides the subgroup order
        stabilizer_ok = all(row["order"] % L == 0 for L in lengths)
        sums_ok = sum(lengths) == len(NEAREST_NEIGHBOURS)
        # coordinate-axis action
        axis_orbits = coordinate_axis_orbits(row["elements"])
        rows.append({
            "label": row["label"],
            "class_index": classes[row["elements"]],
            "order": row["order"],
            "axis": list(row["axis"]) if row["axis"] else None,
            "shell_orbit_lengths": lengths,
            "shell_orbit_count": len(orbs),
            "acts_freely_on_the_shell": free,
            "fixed_shell_sites": fixed,
            "fixed_shell_site_count": len(fixed),
            "transitive_on_the_shell": transitive,
            "maximal_orbit_length": max(lengths),
            "maximal_FREE_orbit_length":
                max([L for L in lengths if L == row["order"]], default=0),
            "orbit_lengths_divide_the_subgroup_order": stabilizer_ok,
            "orbit_lengths_sum_to_six": sums_ok,
            "coordinate_axis_orbit_sizes": sorted(len(o) for o in axis_orbits),
            "transitive_on_the_three_coordinate_axes": len(axis_orbits) == 1,
        })
    all_stab = all(r["orbit_lengths_divide_the_subgroup_order"] for r in rows)
    all_sum = all(r["orbit_lengths_sum_to_six"] for r in rows)
    return {
        "statement": (
            "GATE C886-G3. Orbit structure of every cyclic subgroup on the "
            "6-neighbour shell and on the three coordinate axes. Gated by "
            "orbit-stabilizer (every orbit length divides the subgroup order) "
            "and by the partition identity (lengths sum to 6)."
        ),
        "rows": rows,
        "every_orbit_length_divides_its_subgroup_order": all_stab,
        "every_partition_sums_to_six": all_sum,
        "finding": (
            "shell orbit-length profiles by class: "
            + "; ".join(
                f"{lab} -> {prof}" for lab, prof in sorted({
                    (r["label"], tuple(r["shell_orbit_lengths"])) for r in rows
                })
            )
        ),
        "pass": all_stab and all_sum,
    }


def coordinate_axis_orbits(subgroup: frozenset) -> list[tuple]:
    """Orbits of the subgroup on the three UNSIGNED coordinate axes."""
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def canon(v):
        lead = next(x for x in v if x != 0)
        return v if lead > 0 else tuple(-x for x in v)

    seen, out = set(), []
    for a in axes:
        if a in seen:
            continue
        orbit = {canon(act(m, a)) for m in subgroup}
        seen |= orbit
        out.append(tuple(sorted(orbit)))
    return out


# --------------------------------------------------------------------------
# certificate F: Cycle 883's construction, rebuilt from the pinned source
# --------------------------------------------------------------------------
def c883_construction_certificate() -> dict:
    source = _read_text(AUDIT_INPUT_PATHS[1])
    tree = ast.parse(source)

    fn = next((n for n in ast.walk(tree)
               if isinstance(n, ast.FunctionDef)
               and n.name == "isotype_pair_over_Q"), None)
    fn_source = ast.get_source_segment(source, fn) if fn else None
    calls = {n.func.id for n in ast.walk(fn)
             if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)} \
        if fn else set()
    uses_nullspace = "nullspace_dimension" in calls
    # the construction's shape: rows a_i - a_{i+1 mod n}
    has_modular_shift = bool(fn_source and "% n" in fn_source)
    has_plus_minus = bool(fn_source and "+= 1" in fn_source
                          and "-= 1" in fn_source)
    returns_pair = bool(
        fn and any(isinstance(n, ast.Return) and isinstance(n.value, ast.Tuple)
                   and len(n.value.elts) == 2 for n in ast.walk(fn))
    )

    assigns = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            try:
                assigns[node.targets[0].id] = ast.literal_eval(node.value)
            except ValueError:
                assigns[node.targets[0].id] = ast.dump(node.value)
    orbit_length = assigns.get("ORBIT_LENGTH")
    target_pair = assigns.get("TARGET_PAIR")
    neighbours = assigns.get("NEAREST_NEIGHBOURS")

    receipt = json.loads(_read_text(AUDIT_INPUT_PATHS[3]))
    landed_pair = tuple(receipt.get("derived_ordered_pair", []))
    landed_profile = tuple(receipt.get("two_adic_profile", []))
    landed_successors = receipt.get("open_successors")

    # The block ship receipt is pinned separately and must corroborate the
    # runner receipt AND name SL0 as the open residual this cycle attacks.
    ship = json.loads(_read_text(AUDIT_INPUT_PATHS[5]))
    headline = ship.get("headline", "")
    ship_names_the_pair = "(1,2)" in headline and "(0,1)" in headline
    ship_names_sl0 = "SL0" in headline
    ship_corroborates = ship_names_the_pair and ship_names_sl0

    # Independent reimplementation, then agreement against the pinned source's
    # OWN semantics for n = 2..8.
    def rebuilt_pair(n: int) -> tuple[int, int]:
        rows = []
        for i in range(n):
            row = [Fraction(0)] * n
            row[i] += 1
            row[(i + 1) % n] -= 1
            rows.append(row)
        invariant = n - rank_exact(rows)
        return invariant, n - invariant

    # Same thing computed group-theoretically: dim ker(P - I) on the free orbit.
    def group_theoretic_pair(n: int) -> tuple[int, int]:
        p = [[1 if i == (j + 1) % n else 0 for j in range(n)] for i in range(n)]
        inv = kernel_dimension(mat_add_scaled(p, identity_matrix(n), -1))
        return inv, n - inv

    agreement = [
        {"n": n, "rebuilt": list(rebuilt_pair(n)),
         "group_theoretic": list(group_theoretic_pair(n)),
         "agree": rebuilt_pair(n) == group_theoretic_pair(n),
         "formula_1_n_minus_1": rebuilt_pair(n) == (1, n - 1)}
        for n in range(2, 9)
    ]
    routes_agree = all(r["agree"] and r["formula_1_n_minus_1"]
                       for r in agreement)
    reproduces_883 = (
        orbit_length == 3
        and rebuilt_pair(orbit_length) == tuple(target_pair)
        and tuple(target_pair) == landed_pair == TARGET_PAIR
        and landed_profile == (0, 1)
    )
    ok = (
        fn is not None and uses_nullspace and has_modular_shift
        and has_plus_minus and returns_pair
        and neighbours is not None and len(neighbours) == 6
        and set(neighbours) == set(NEAREST_NEIGHBOURS)
        and routes_agree and reproduces_883 and ship_corroborates
    )
    return {
        "statement": (
            "The Cycle-883 readout construction is recovered from the pinned "
            "source by AST -- never imported -- and reimplemented here twice: "
            "once as Cycle 883 wrote it (nullspace of a_i - a_{i+1}) and once "
            "group-theoretically (dim ker(P - I) for the orbit permutation "
            "matrix). The two routes must agree at every orbit length before "
            "this cycle is allowed to generalize the construction."
        ),
        "extracted_function": "isotype_pair_over_Q",
        "extracted_source": fn_source,
        "calls_nullspace_dimension": uses_nullspace,
        "builds_modular_shift_rows": has_modular_shift,
        "builds_plus_one_minus_one_rows": has_plus_minus,
        "returns_an_ordered_pair": returns_pair,
        "ast_recovered_ORBIT_LENGTH": orbit_length,
        "ast_recovered_TARGET_PAIR": list(target_pair) if target_pair else None,
        "ast_recovered_NEAREST_NEIGHBOURS":
            [list(v) for v in neighbours] if neighbours else None,
        "neighbour_shell_matches_this_cycle":
            neighbours is not None and set(neighbours) == set(NEAREST_NEIGHBOURS),
        "cycle883_landed_receipt_pair": list(landed_pair),
        "cycle883_landed_receipt_profile": list(landed_profile),
        "cycle883_landed_open_successors": landed_successors,
        "cycle883_ship_receipt_headline": headline,
        "ship_receipt_names_the_pair_and_profile": ship_names_the_pair,
        "ship_receipt_names_SL0_as_open": ship_names_sl0,
        "ship_receipt_corroborates_the_runner_receipt": ship_corroborates,
        "two_route_agreement_table": agreement,
        "both_routes_agree_everywhere": routes_agree,
        "reproduces_the_landed_cycle883_result": reproduces_883,
        "what_this_licenses": (
            "The construction generalizes verbatim to any cyclic subgroup "
            "acting freely on a set of records: it is 'the linear additive "
            "readout on the free orbit, decomposed under the acting group'. "
            "Nothing in the construction mentions the number 3."
        ),
        "finding": (
            f"The pinned construction round-trips by AST and reproduces the "
            f"landed pair {list(landed_pair)} at ORBIT_LENGTH = {orbit_length}; "
            f"the rebuilt and group-theoretic routes agree on all "
            f"{len(agreement)} orbit lengths tested and both follow (1, n-1)."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate G: isotype signatures for every subgroup, both scopes
# --------------------------------------------------------------------------
def permutation_matrix(elem, points) -> list[list[int]]:
    index = {p: i for i, p in enumerate(points)}
    m = [[0] * len(points) for _ in range(len(points))]
    for j, p in enumerate(points):
        m[index[act(elem, p)]][j] = 1
    return m


def fine_decomposition(elem, points, order: int) -> dict:
    """dim ker Phi_d(P) for every d | order, with multiplicities."""
    p_matrix = permutation_matrix(elem, points)
    blocks = []
    total = 0
    for d in divisors(order):
        coeffs = cyclotomic(d)
        dim = kernel_dimension(poly_of_matrix(coeffs, p_matrix))
        if dim == 0:
            continue
        phi = euler_phi(d)
        blocks.append({
            "root_of_unity_order": d,
            "rational_irreducible_dimension": phi,
            "isotypic_dimension": dim,
            "multiplicity": Fraction(dim, phi),
            "multiplicity_is_an_integer": dim % phi == 0,
            "cyclotomic_polynomial_coefficients": coeffs,
        })
        total += dim
    return {"blocks": blocks, "total_dimension": total,
            "space_dimension": len(points)}


def signature_for(subgroup, points, order) -> dict:
    gens = sorted(g for g in subgroup if cyclic_subgroup(g) == subgroup) \
        if order > 1 else [IDENTITY3]
    gen = gens[0]
    p_matrix = permutation_matrix(gen, points)

    # route 1: exact nullspace of P - I
    inv_nullspace = kernel_dimension(
        mat_add_scaled(p_matrix, identity_matrix(len(points)), -1))
    # route 2: Burnside average over the whole subgroup
    total_fixed = sum(
        sum(1 for p in points if act(h, p) == p) for h in subgroup)
    inv_burnside = Fraction(total_fixed, order)
    # route 3: number of orbits
    orbit_count = len(orbits_of_group(sorted(subgroup), points))
    routes_agree = (
        inv_nullspace == inv_burnside == orbit_count
    )

    fine = fine_decomposition(gen, points, order)
    # generator independence: every generator must give the same fine data
    gen_independent = True
    for other in gens[1:]:
        alt = fine_decomposition(other, points, order)
        if [b["isotypic_dimension"] for b in alt["blocks"]] != \
                [b["isotypic_dimension"] for b in fine["blocks"]]:
            gen_independent = False
    # transpose (inverse) independence
    transposed = [[p_matrix[j][i] for j in range(len(points))]
                  for i in range(len(points))]
    inv_transposed = kernel_dimension(
        mat_add_scaled(transposed, identity_matrix(len(points)), -1))

    dim = len(points)
    coarse = (inv_nullspace, dim - inv_nullspace)
    fine_dims = sorted(
        d for b in fine["blocks"]
        for d in [b["rational_irreducible_dimension"]] * int(b["multiplicity"])
    )
    top_fine = max(fine_dims) if fine_dims else 0
    complex_weights = [
        {"root_of_unity_order": b["root_of_unity_order"],
         "primitive_roots": euler_phi(b["root_of_unity_order"]),
         "multiplicity_each": int(b["multiplicity"])}
        for b in fine["blocks"]
    ]
    complex_total = sum(w["primitive_roots"] * w["multiplicity_each"]
                        for w in complex_weights)
    return {
        "space_dimension": dim,
        "invariant_dim_by_nullspace": inv_nullspace,
        "invariant_dim_by_burnside": q(inv_burnside),
        "invariant_dim_by_orbit_count": orbit_count,
        "three_routes_agree": routes_agree,
        "invariant_dim_on_the_transposed_action": inv_transposed,
        "transpose_gives_the_same_invariant_dim": inv_transposed == inv_nullspace,
        "generator_independent": gen_independent,
        "coarse_ordered_pair": list(coarse),
        "coarse_two_adic_profile": [
            vp(Fraction(coarse[0]), 2) if coarse[0] else None,
            vp(Fraction(coarse[1]), 2) if coarse[1] else None,
        ],
        "fine_rational_irreducible_dimensions": fine_dims,
        "fine_blocks": [
            {k: (q(v) if isinstance(v, Fraction) else v)
             for k, v in b.items()} for b in fine["blocks"]
        ],
        "fine_dimensions_sum": sum(fine_dims),
        "fine_decomposition_sums_to_the_space": sum(fine_dims) == dim,
        "top_rational_irreducible_dimension": top_fine,
        "fine_top_pair": [inv_nullspace, top_fine],
        "fine_top_two_adic_profile": [
            vp(Fraction(inv_nullspace), 2) if inv_nullspace else None,
            vp(Fraction(top_fine), 2) if top_fine else None,
        ],
        "complex_weight_multiset": complex_weights,
        "complex_weights_sum_to_the_space": complex_total == dim,
        "every_multiplicity_is_an_integer":
            all(b["multiplicity_is_an_integer"] for b in fine["blocks"]),
    }


def isotype_signature_certificate(census, classes) -> dict:
    rows = []
    for row in census:
        if row["order"] == 1:
            continue
        subgroup, order = row["elements"], row["order"]
        orbs = subgroup_shell_orbits(subgroup)
        free_orbits = [o for o in orbs if len(o) == order]
        orbit_scope = (
            signature_for(subgroup, sorted(max(free_orbits, key=len)), order)
            if free_orbits else None
        )
        shell_scope = signature_for(subgroup, list(NEAREST_NEIGHBOURS), order)
        rows.append({
            "label": row["label"],
            "class_index": classes[subgroup],
            "order": order,
            "axis": list(row["axis"]),
            "has_a_free_orbit_on_the_shell": bool(free_orbits),
            "free_orbit_count": len(free_orbits),
            "ORBIT_SCOPE_cycle883_construction": orbit_scope,
            "SHELL_SCOPE_whole_neighbourhood": shell_scope,
        })
    dim_gates = all(
        r["SHELL_SCOPE_whole_neighbourhood"]["fine_decomposition_sums_to_the_space"]
        and r["SHELL_SCOPE_whole_neighbourhood"]["complex_weights_sum_to_the_space"]
        and r["SHELL_SCOPE_whole_neighbourhood"]["three_routes_agree"]
        and r["SHELL_SCOPE_whole_neighbourhood"]["generator_independent"]
        and (r["ORBIT_SCOPE_cycle883_construction"] is None or (
            r["ORBIT_SCOPE_cycle883_construction"]["fine_decomposition_sums_to_the_space"]
            and r["ORBIT_SCOPE_cycle883_construction"]["complex_weights_sum_to_the_space"]
            and r["ORBIT_SCOPE_cycle883_construction"]["three_routes_agree"]
            and r["ORBIT_SCOPE_cycle883_construction"]["generator_independent"]))
        for r in rows
    )
    int_gates = all(
        r["SHELL_SCOPE_whole_neighbourhood"]["every_multiplicity_is_an_integer"]
        for r in rows
    )
    summary = []
    for label in sorted({r["label"] for r in rows}):
        sample = next(r for r in rows if r["label"] == label)
        osc = sample["ORBIT_SCOPE_cycle883_construction"]
        summary.append({
            "label": label,
            "orbit_scope_pair": osc["coarse_ordered_pair"] if osc else None,
            "orbit_scope_profile": osc["coarse_two_adic_profile"] if osc else None,
            "orbit_scope_fine_dims":
                osc["fine_rational_irreducible_dimensions"] if osc else None,
            "orbit_scope_fine_top_pair": osc["fine_top_pair"] if osc else None,
            "shell_scope_pair":
                sample["SHELL_SCOPE_whole_neighbourhood"]["coarse_ordered_pair"],
            "shell_scope_profile":
                sample["SHELL_SCOPE_whole_neighbourhood"]["coarse_two_adic_profile"],
            "shell_scope_fine_dims":
                sample["SHELL_SCOPE_whole_neighbourhood"]["fine_rational_irreducible_dimensions"],
            "carries_the_target_pair_coarse_orbit_scope":
                bool(osc) and tuple(osc["coarse_ordered_pair"]) == TARGET_PAIR,
            "carries_the_target_pair_fine_top_orbit_scope":
                bool(osc) and tuple(osc["fine_top_pair"]) == TARGET_PAIR,
        })
    return {
        "statement": (
            "GATE C886-G4 + THE SIGNATURE TABLE. For every nontrivial cyclic "
            "subgroup, at both scopes: invariant multiplicity by three "
            "independent routes, the coarse ordered weight pair with its "
            "2-adic profile, the fine decomposition into rational irreducibles "
            "by exact cyclotomic kernel dimensions, and the complex weight "
            "multiset. Every decomposition is gated to sum back to the space "
            "dimension. NO gate here tests for a preferred subgroup."
        ),
        "rows": rows,
        "by_class": summary,
        "every_decomposition_sums_and_every_route_agrees": dim_gates,
        "every_isotypic_multiplicity_is_an_integer": int_gates,
        "the_reading_matters": (
            "Two readings of 'weight pair' are computed and they DISAGREE on "
            "which subgroups reach the target. COARSE (invariant, complement) "
            "-- Cycle 883's reading -- gives (1, 2) only at C3. FINE "
            "(invariant, top rational irreducible) gives (1, 2) at C3 AND at "
            "C4_face, because the regular representation of C4 over Q contains "
            "the 2-dimensional block Q(i). The choice of reading is itself a "
            "supplied convention, and it moves the survivor set."
        ),
        "finding": (
            "; ".join(
                f"{s['label']}: orbit-scope pair {s['orbit_scope_pair']} "
                f"profile {s['orbit_scope_profile']} fine "
                f"{s['orbit_scope_fine_dims']}"
                for s in summary
            )
        ),
        "pass": dim_gates and int_gates,
    }


# --------------------------------------------------------------------------
# certificate H: signatures are conjugation-invariant (class functions)
# --------------------------------------------------------------------------
def class_invariance_certificate(signature_rows) -> dict:
    groups: dict[int, list[dict]] = {}
    for row in signature_rows:
        groups.setdefault(row["class_index"], []).append(row)
    rows = []
    all_constant = True
    for idx in sorted(groups):
        members = groups[idx]
        keys = {digest({
            "orbit": m["ORBIT_SCOPE_cycle883_construction"],
            "shell": m["SHELL_SCOPE_whole_neighbourhood"],
            "free": m["has_a_free_orbit_on_the_shell"],
        }) for m in members}
        constant = len(keys) == 1
        all_constant = all_constant and constant
        rows.append({
            "class_index": idx,
            "label": members[0]["label"],
            "members": len(members),
            "distinct_signature_digests": len(keys),
            "signature_is_constant_on_the_class": constant,
        })
    return {
        "statement": (
            "GATE C886-G5. Every computed signature is constant on each "
            "conjugacy class of subgroups. This is the structural reason any "
            "selector compatible with 'no site is privileged' must be a "
            "function of the CLASS, so the selection problem has exactly as "
            "many candidate answers as there are nontrivial classes."
        ),
        "rows": rows,
        "every_signature_is_a_class_function": all_constant,
        "candidate_scope_answers": len(rows),
        "finding": (
            f"All {sum(r['members'] for r in rows)} nontrivial cyclic "
            f"subgroups collapse to {len(rows)} distinct signatures, one per "
            f"conjugacy class, so the scope question has exactly {len(rows)} "
            f"candidate answers."
        ),
        "pass": all_constant,
    }


# --------------------------------------------------------------------------
# certificate K: anchor reachability, recomputed (never cited)
# --------------------------------------------------------------------------
GENERATOR_RULES = {
    "R1_orbit_scope_coarse": (
        "generators = {free orbit length} U {coarse pair entries}, values > 1 "
        "-- exactly the data Cycle 883 fed to its own T6 recomputation"
    ),
    "R2_shell_scope_coarse": (
        "generators = {distinct shell orbit lengths} U {shell coarse pair "
        "entries}, values > 1"
    ),
    "R3_orbit_scope_fine": (
        "generators = {free orbit length} U {fine rational irreducible "
        "dimensions}, values > 1"
    ),
    "R4_shell_scope_fine": (
        "generators = {distinct shell orbit lengths} U {fine rational "
        "irreducible dimensions on the shell}, values > 1"
    ),
}


def reachability_certificate(signature_rows) -> dict:
    rows = []
    for row in signature_rows:
        osc = row["ORBIT_SCOPE_cycle883_construction"]
        ssc = row["SHELL_SCOPE_whole_neighbourhood"]
        shell_lengths = sorted({len(o) for o in
                                subgroup_shell_orbits_by_label(row)})
        rules = {}
        if osc:
            rules["R1_orbit_scope_coarse"] = \
                [row["order"]] + list(osc["coarse_ordered_pair"])
            rules["R3_orbit_scope_fine"] = \
                [row["order"]] + list(osc["fine_rational_irreducible_dimensions"])
        rules["R2_shell_scope_coarse"] = \
            shell_lengths + list(ssc["coarse_ordered_pair"])
        rules["R4_shell_scope_fine"] = \
            shell_lengths + list(ssc["fine_rational_irreducible_dimensions"])
        per_rule = {}
        for rule, gens in rules.items():
            res = multiplicative_group_reaches(gens, TARGET_ANCHOR)
            # windowed corroboration in Cycle 883's own style
            window = range(-6, 7)
            gs = res["generators"]
            windowed = False
            if gs:
                for exps in product(window, repeat=len(gs)):
                    value = Fraction(1)
                    for g, e in zip(gs, exps):
                        value *= Fraction(g) ** e
                    if value == TARGET_ANCHOR:
                        windowed = True
                        break
            res["windowed_scan_confirms"] = windowed
            res["window_corroborates_the_lattice_proof"] = (
                windowed if res["reachable"] else True
            )
            res["window_scanned"] = [min(window), max(window)]
            per_rule[rule] = res
        rows.append({
            "label": row["label"],
            "class_index": row["class_index"],
            "per_rule": per_rule,
        })
    survivors = {
        rule: sorted({r["label"] for r in rows
                      if rule in r["per_rule"]
                      and r["per_rule"][rule]["reachable"]})
        for rule in GENERATOR_RULES
    }
    # Every windowed scan must corroborate the lattice proof wherever the
    # lattice proof says REACHABLE (a reachable point must be findable).
    corroborated = all(
        (not res["reachable"]) or res["windowed_scan_confirms"]
        for r in rows for res in r["per_rule"].values()
    )
    target_v2 = vp(TARGET_ANCHOR, 2)
    target_v3 = vp(TARGET_ANCHOR, 3)
    return {
        "statement": (
            "Cycle 882's C882-T6 reachability question, RECOMPUTED here for "
            "every subgroup and never cited. Membership in the multiplicative "
            "group generated by a subgroup's own numerical data is decided "
            "EXACTLY by integer-lattice membership over the prime valuation "
            "vectors, so 'unreachable' is a proof rather than a window result. "
            "Four generator rules are run because the rule itself is a choice."
        ),
        "target_anchor": q(TARGET_ANCHOR),
        "target_2_adic_valuation": target_v2,
        "target_3_adic_valuation": target_v3,
        "generator_rules": GENERATOR_RULES,
        "rows": rows,
        "survivors_by_rule": survivors,
        "survivor_set_is_rule_invariant":
            len({tuple(v) for v in survivors.values()}) == 1,
        "windowed_scan_corroborates_every_reachable_verdict": corroborated,
        "what_moves": (
            "Under R1 (Cycle 883's own rule) and under R3 and R4 the survivor "
            "set is exactly {C3_body}. Under R2 the edge-C2 class joins, "
            "because three free length-2 orbits supply the numbers 2 and 3 "
            "just as one free length-3 orbit supplies 3 and 2. The "
            "reachability selector therefore depends on the SCOPE CONVENTION "
            "-- and the scope convention is precisely what SL0 asks us to "
            "derive. Using reachability to pin the scope is circular; the "
            "circle is exhibited here rather than hidden."
        ),
        "finding": (
            "survivors by rule: "
            + "; ".join(f"{k} -> {v}" for k, v in sorted(survivors.items()))
        ),
        "pass": corroborated,
    }


_SHELL_ORBIT_CACHE: dict[str, list[tuple]] = {}


def subgroup_shell_orbits_by_label(signature_row) -> list[tuple]:
    label = signature_row["label"]
    if label not in _SHELL_ORBIT_CACHE:
        census = build_census()
        row = next(r for r in census if r["label"] == label)
        _SHELL_ORBIT_CACHE[label] = subgroup_shell_orbits(row["elements"])
    return _SHELL_ORBIT_CACHE[label]


# --------------------------------------------------------------------------
# certificate I: the selector table
# --------------------------------------------------------------------------
def selector_table_certificate(orbit_rows, signature_rows, reach) -> dict:
    by_label = {r["label"]: r for r in orbit_rows}
    sig = {r["label"]: r for r in signature_rows}
    labels = sorted(sig)

    shell_inv = {lab: sig[lab]["SHELL_SCOPE_whole_neighbourhood"]
                 ["invariant_dim_by_nullspace"] for lab in labels}
    min_shell_inv = min(shell_inv.values())
    free_labels = [lab for lab in labels
                   if by_label[lab]["acts_freely_on_the_shell"]]
    max_free_len = max((by_label[lab]["maximal_FREE_orbit_length"]
                        for lab in free_labels), default=0)

    def orbit_pair(lab):
        osc = sig[lab]["ORBIT_SCOPE_cycle883_construction"]
        return tuple(osc["coarse_ordered_pair"]) if osc else None

    def fine_top(lab):
        osc = sig[lab]["ORBIT_SCOPE_cycle883_construction"]
        return tuple(osc["fine_top_pair"]) if osc else None

    def orbit_v2(lab):
        osc = sig[lab]["ORBIT_SCOPE_cycle883_construction"]
        return osc["coarse_two_adic_profile"][1] if osc else None

    reach_by_rule = reach["survivors_by_rule"]

    selectors = [
        {
            "id": "SEL01_free_on_shell",
            "demand": "the subgroup acts with NO fixed site on the 6-neighbour shell",
            "quoted_sentence": AXIOM_SENTENCES["no_site_privileged"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": (
                "no site is privileged, AND sites are distinguished by the "
                "supplied lattice structure alone"
            ),
            "what_the_filter_computes": (
                "whether the subgroup's action fixes any of the six neighbour "
                "sites"
            ),
            "fidelity": "NONE",
            "fidelity_reason": (
                "The sentence's second clause explicitly LICENSES distinguishing "
                "sites by supplied lattice structure. A rotation axis IS supplied "
                "lattice structure, so the two sites a face-C2 fixes are "
                "distinguished exactly the way the sentence permits. The "
                "sentence forbids privileging by fiat; it does not forbid a "
                "subgroup from having fixed points."
            ),
            "grounded": False,
            "survivors": sorted(free_labels),
        },
        {
            "id": "SEL02_transitive_on_shell",
            "demand": "the subgroup acts transitively on the 6-neighbour shell",
            "quoted_sentence": AXIOM_SENTENCES["no_site_privileged"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": "no site is privileged",
            "what_the_filter_computes":
                "whether the shell is a single orbit of the subgroup",
            "fidelity": "NONE",
            "fidelity_reason": (
                "Same defect as SEL01, and strictly worse: no cyclic subgroup "
                "of a 24-element group with maximal element order 4 can act "
                "transitively on six points, so this reading of the sentence "
                "eliminates C3 along with everything else."
            ),
            "grounded": False,
            "survivors": sorted(lab for lab in labels
                                if by_label[lab]["transitive_on_the_shell"]),
        },
        {
            "id": "SEL03_multiplicity_one_orbit_scope",
            "demand": "trivial isotype multiplicity is exactly 1 on the readout space",
            "quoted_sentence": AXIOM_SENTENCES["finite_additive_readout"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says":
                "scalar readout is additive over disjoint records, I(empty)=0",
            "what_the_filter_computes":
                "the dimension of the invariant subspace of the orbit readout space",
            "fidelity": "NONE",
            "fidelity_reason": (
                "Additivity fixes that the readout is LINEAR. It says nothing "
                "about how many invariant directions that linear space has. "
                "The multiplicity-one demand is a modelling convention."
            ),
            "grounded": False,
            "survivors": sorted(
                lab for lab in labels
                if sig[lab]["ORBIT_SCOPE_cycle883_construction"]
                and sig[lab]["ORBIT_SCOPE_cycle883_construction"]
                ["invariant_dim_by_nullspace"] == 1
            ),
        },
        {
            "id": "SEL04_multiplicity_one_shell_scope",
            "demand": "trivial isotype multiplicity is exactly 1 on the whole shell",
            "quoted_sentence": AXIOM_SENTENCES["finite_additive_readout"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": "as SEL03",
            "what_the_filter_computes":
                "the invariant dimension of the 6-dimensional shell readout space",
            "fidelity": "NONE",
            "fidelity_reason": "as SEL03",
            "grounded": False,
            "survivors": sorted(lab for lab in labels if shell_inv[lab] == 1),
        },
        {
            "id": "SEL05_minimal_shell_invariant_multiplicity",
            "demand": "the subgroup MINIMIZES the trivial multiplicity on the shell",
            "quoted_sentence": None,
            "quote_source": None,
            "what_the_sentence_says": None,
            "what_the_filter_computes":
                "argmin over subgroups of the shell invariant dimension",
            "fidelity": "NONE",
            "fidelity_reason": (
                "No axiom sentence contains a minimization. This is an "
                "economy criterion supplied from outside the axiom set."
            ),
            "grounded": False,
            "survivors": sorted(lab for lab in labels
                                if shell_inv[lab] == min_shell_inv),
        },
        {
            "id": "SEL06_maximal_free_shell_orbit",
            "demand": "among subgroups acting freely on the shell, orbit length is maximal",
            "quoted_sentence": None,
            "quote_source": None,
            "what_the_sentence_says": None,
            "what_the_filter_computes":
                "argmax of free orbit length over the freely-acting subgroups",
            "fidelity": "NONE",
            "fidelity_reason": (
                "Two supplied clauses in a trenchcoat: freeness (SEL01, "
                "ungrounded) and maximality (no sentence contains it)."
            ),
            "grounded": False,
            "survivors": sorted(
                lab for lab in free_labels
                if by_label[lab]["maximal_FREE_orbit_length"] == max_free_len
            ),
        },
        {
            "id": "SEL07_coarse_pair_v2_equals_one",
            "demand": "the coarse weight pair has 2-adic profile (0, 1)",
            "quoted_sentence": C882_T6_NEEDLE,
            "quote_source": AUDIT_INPUT_PATHS[2],
            "what_the_sentence_says": (
                "a Record-facing datum with v_2 = 1 must enter, concretely the "
                "weight pair (1, 2)"
            ),
            "what_the_filter_computes":
                "v_2 of the complement dimension of the orbit readout space",
            "fidelity": "EXACT",
            "fidelity_reason": (
                "The filter computes precisely what the sentence demands. But "
                "the sentence is an OBLIGATION sentence recovered from the "
                "Cycle-882 primary, NOT an axiom sentence -- it states the "
                "target, so using it to select the scope selects the scope by "
                "reading the answer."
            ),
            "grounded": False,
            "grounding_defect": "target-facing, not axiom-grounded",
            "survivors": sorted(lab for lab in labels if orbit_v2(lab) == 1),
        },
        {
            "id": "SEL08_reachability_R1_orbit_scope",
            "demand": "the subgroup's own numbers multiplicatively reach 2/9",
            "quoted_sentence": C882_T6_NEEDLE,
            "quote_source": AUDIT_INPUT_PATHS[2],
            "what_the_sentence_says": "as SEL07",
            "what_the_filter_computes": GENERATOR_RULES["R1_orbit_scope_coarse"],
            "fidelity": "PARTIAL",
            "fidelity_reason": (
                "The sentence asks for a v_2 = 1 datum, not for multiplicative "
                "reachability of 2/9; the filter is strictly stronger than the "
                "quote. And it is target-facing either way."
            ),
            "grounded": False,
            "grounding_defect": "target-facing, not axiom-grounded",
            "survivors": reach_by_rule["R1_orbit_scope_coarse"],
        },
        {
            "id": "SEL09_reachability_R2_shell_scope",
            "demand": "the subgroup's shell numbers multiplicatively reach 2/9",
            "quoted_sentence": C882_T6_NEEDLE,
            "quote_source": AUDIT_INPUT_PATHS[2],
            "what_the_sentence_says": "as SEL07",
            "what_the_filter_computes": GENERATOR_RULES["R2_shell_scope_coarse"],
            "fidelity": "PARTIAL",
            "fidelity_reason": (
                "Same filter as SEL08 at a different scope, and the survivor "
                "set MOVES -- which shows the selector is scope-dependent and "
                "so cannot itself fix the scope."
            ),
            "grounded": False,
            "grounding_defect": "target-facing and scope-circular",
            "survivors": reach_by_rule["R2_shell_scope_coarse"],
        },
        {
            "id": "SEL10_fine_top_pair_is_the_target",
            "demand": "(invariant dim, top rational irreducible dim) == (1, 2)",
            "quoted_sentence": None,
            "quote_source": None,
            "what_the_sentence_says": None,
            "what_the_filter_computes":
                "the fine reading of the weight pair on the orbit readout space",
            "fidelity": "NONE",
            "fidelity_reason": (
                "No sentence fixes which reading of 'weight pair' is meant. "
                "This alternative reading is legitimate and it admits C4_face "
                "as well, because Q[C4] contains the 2-dimensional block Q(i)."
            ),
            "grounded": False,
            "survivors": sorted(lab for lab in labels
                                if fine_top(lab) == TARGET_PAIR),
        },
        {
            "id": "SEL11_transitive_on_coordinate_axes",
            "demand": "the subgroup permutes the three coordinate axes transitively",
            "quoted_sentence": AXIOM_SENTENCES["lattice_rotations"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": (
                "sites are the points of the CUBIC lattice Z^3 with proper "
                "cubic rotations about each site"
            ),
            "what_the_filter_computes":
                "whether the subgroup alone acts transitively on {x, y, z}",
            "fidelity": "PARTIAL",
            "fidelity_reason": (
                "The word 'cubic' does carry the equivalence of the three axis "
                "directions -- but the FULL 24-element group already realizes "
                "that equivalence. The filter demands that a single CYCLIC "
                "SUBGROUP realize it internally, which is strictly stronger "
                "than anything the sentence says. This is the closest any "
                "route gets to a derivation, and it still falls short."
            ),
            "grounded": False,
            "grounding_defect": (
                "the sentence grounds axis-equivalence for the whole group, "
                "not internal axis-transitivity for the scope subgroup"
            ),
            "survivors": sorted(
                lab for lab in labels
                if by_label[lab]["transitive_on_the_three_coordinate_axes"]
            ),
        },
        {
            "id": "SEL12_odd_order",
            "demand": "the subgroup has odd order greater than 1",
            "quoted_sentence": None,
            "quote_source": None,
            "what_the_sentence_says": None,
            "what_the_filter_computes": "parity of the subgroup order",
            "fidelity": "NONE",
            "fidelity_reason": (
                "No axiom sentence mentions parity. Listed because it is the "
                "CHEAPEST single supplied clause that pins the answer: order "
                "3 is the only odd nontrivial element order in a group of "
                "order 24 whose element orders are 1, 2, 3, 4."
            ),
            "grounded": False,
            "survivors": sorted(lab for lab in labels
                                if sig[lab]["order"] % 2 == 1),
        },
        {
            "id": "SEL13_count_once",
            "demand": "one record per site, permanently",
            "quoted_sentence": AXIOM_SENTENCES["count_once"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says":
                "a site never carries more than one record; records are permanent",
            "what_the_filter_computes": (
                "whether the subgroup's shell orbits are a PARTITION, i.e. "
                "whether any site would be counted twice"
            ),
            "fidelity": "EXACT",
            "fidelity_reason": (
                "The filter computes exactly the sentence's content -- and the "
                "sentence's content is satisfied by every group action, since "
                "orbits of a group action always partition the set. The clause "
                "is true of all 16 nontrivial cyclic subgroups."
            ),
            "grounded": True,
            "survivors": sorted(
                lab for lab in labels
                if sum(len(o) for o in subgroup_shell_orbits_by_label(sig[lab]))
                == len(NEAREST_NEIGHBOURS)
            ),
        },
        {
            "id": "SEL14_content_only_readout",
            "demand": "the readout value depends on record content alone",
            "quoted_sentence": AXIOM_SENTENCES["content_only_readout"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says":
                "only records are readable; readout is determined by record content",
            "what_the_filter_computes": (
                "whether the subgroup's readout space is spanned by the record "
                "coordinates, i.e. carries no data beyond record content"
            ),
            "fidelity": "EXACT",
            "fidelity_reason": (
                "The filter computes exactly what the sentence says, and the "
                "sentence is satisfied by every subgroup: the permutation "
                "representation on record coordinates is content-only by "
                "construction for any acting group."
            ),
            "grounded": True,
            "survivors": sorted(
                lab for lab in labels
                if sig[lab]["SHELL_SCOPE_whole_neighbourhood"]["space_dimension"]
                == len(NEAREST_NEIGHBOURS)
            ),
        },
        {
            "id": "SEL15_admissibility_covariance",
            "demand": "the scope must lie inside the covariance group of the admissibility rule",
            "quoted_sentence": AXIOM_SENTENCES["admissibility_covariance"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": (
                "one fixed nearest-neighbour rule, covariant under lattice "
                "translations and proper cubic rotations"
            ),
            "what_the_filter_computes":
                "whether the subgroup is a subgroup of the 24 proper rotations",
            "fidelity": "EXACT",
            "fidelity_reason": (
                "The filter computes exactly the sentence's content. The "
                "sentence names the covariance group as a WHOLE; every cyclic "
                "subgroup sits inside it, so the clause is an ANTI-selector: "
                "it is the textual reason all sixteen nontrivial cyclic "
                "subgroups are equally supplied."
            ),
            "grounded": True,
            "survivors": sorted(labels),
        },
        {
            "id": "SEL16_no_site_privileged_read_literally",
            "demand": (
                "no site is privileged except by supplied lattice structure "
                "-- read with BOTH of its clauses"
            ),
            "quoted_sentence": AXIOM_SENTENCES["no_site_privileged"],
            "quote_source": AUDIT_INPUT_PATHS[0],
            "what_the_sentence_says": (
                "no site is privileged; sites are distinguished by the supplied "
                "lattice structure alone"
            ),
            "what_the_filter_computes": (
                "whether the subgroup's shell orbit partition is determined by "
                "supplied lattice structure (the rotation axis) rather than by "
                "an external stipulation"
            ),
            "fidelity": "EXACT",
            "fidelity_reason": (
                "This is the sentence read with both clauses instead of only "
                "the first. Every cyclic subgroup's orbit partition is "
                "determined by its axis, which is supplied lattice structure, "
                "so the sentence is satisfied by all of them. SEL01 and SEL02 "
                "are strengthenings of this filter, and the strengthenings are "
                "where their grounding is lost."
            ),
            "grounded": True,
            "survivors": sorted(labels),
        },
    ]
    for sel in selectors:
        sel["survivor_count"] = len(sel["survivors"])
        sel["isolates_C3_body"] = sel["survivors"] == ["C3_body"]
        sel.setdefault("grounding_defect", None)

    valid_grades = all(s["fidelity"] in FIDELITY_GRADES for s in selectors)
    every_survivor_is_a_class = all(
        set(s["survivors"]) <= set(labels) for s in selectors)
    grounded = [s for s in selectors if s["grounded"]]
    grounded_isolating = [s for s in grounded if s["isolates_C3_body"]]
    return {
        "statement": (
            "Sixteen candidate selectors, each run as a filter over the "
            "subgroup census. Each row carries its byte-quoted sentence (or an "
            "explicit absence), what the sentence says, what the filter "
            "computes, and the quote-to-computation fidelity grade. The "
            "surviving set is DATA."
        ),
        "candidate_classes": sorted(labels),
        "selectors": selectors,
        "grounded_selector_ids": [s["id"] for s in grounded],
        "grounded_selectors_that_isolate_C3":
            [s["id"] for s in grounded_isolating],
        "ungrounded_selectors_that_isolate_C3":
            [s["id"] for s in selectors
             if s["isolates_C3_body"] and not s["grounded"]],
        "fidelity_grades_valid": valid_grades,
        "every_survivor_set_is_a_subset_of_the_census": every_survivor_is_a_class,
        "the_pattern": (
            "Every selector with EXACT fidelity to an AXIOM sentence is "
            "non-selective (it admits all four classes). Every selector that "
            "isolates C3 either quotes no sentence at all, quotes an "
            "obligation sentence rather than an axiom sentence, or "
            "strengthens its axiom sentence beyond what the sentence says. "
            "That is the whole SL0 finding, computed row by row."
        ),
        "finding": (
            f"{len(grounded)} of {len(selectors)} selectors are axiom-grounded; "
            f"{len(grounded_isolating)} of those isolate C3_body; "
            f"{len([s for s in selectors if s['isolates_C3_body']])} selectors "
            f"isolate C3_body in total, all of them ungrounded."
        ),
        "pass": valid_grades and every_survivor_is_a_class,
    }


# --------------------------------------------------------------------------
# certificate J: the conjunctions
# --------------------------------------------------------------------------
def conjunction_certificate(selector_cert) -> dict:
    selectors = selector_cert["selectors"]
    labels = set(selector_cert["candidate_classes"])

    def intersect(subset):
        acc = set(labels)
        for s in subset:
            acc &= set(s["survivors"])
        return sorted(acc)

    grounded = [s for s in selectors if s["grounded"]]
    nonempty = [s for s in selectors if s["survivors"]]
    grounded_survivors = intersect(grounded)
    all_survivors = intersect(selectors)
    nonempty_survivors = intersect(nonempty)
    ungrounded_nonempty = [s for s in nonempty if not s["grounded"]]
    return {
        "statement": (
            "The conjunctions. If the AXIOM-GROUNDED conjunction were exactly "
            "{C3_body} the outcome would be (a) DERIVATION. It is not."
        ),
        "grounded_conjunction": {
            "selector_ids": [s["id"] for s in grounded],
            "survivors": grounded_survivors,
            "isolates_C3_body": grounded_survivors == ["C3_body"],
        },
        "all_selector_conjunction": {
            "survivors": all_survivors,
            "is_empty": not all_survivors,
            "why_empty": (
                "SEL02 (shell transitivity) and SEL04 (shell multiplicity one) "
                "have empty survivor sets, so the unrestricted conjunction is "
                "inconsistent. Selector CONFLICT is itself SL0 data."
            ),
        },
        "nonempty_selector_conjunction": {
            "selector_ids": [s["id"] for s in nonempty],
            "survivors": nonempty_survivors,
            "isolates_C3_body": nonempty_survivors == ["C3_body"],
        },
        "ungrounded_nonempty_conjunction": {
            "selector_ids": [s["id"] for s in ungrounded_nonempty],
            "survivors": intersect(ungrounded_nonempty),
        },
        "reading": (
            "The ungrounded selectors CONVERGE on C3_body -- freeness plus "
            "maximality, axis transitivity, odd order, minimal shell "
            "multiplicity and orbit-scope reachability all point the same way. "
            "The convergence is real and worth recording. It is also entirely "
            "supplied: not one of the converging selectors survives the "
            "quote-to-computation test against an axiom sentence."
        ),
        "finding": (
            f"axiom-grounded conjunction survivors {grounded_survivors}; "
            f"non-empty-selector conjunction survivors {nonempty_survivors}; "
            f"unrestricted conjunction survivors {all_survivors}."
        ),
        "pass": True,
    }


# --------------------------------------------------------------------------
# certificate L: the route ledger
# --------------------------------------------------------------------------
def route_ledger_certificate(selector_cert, conjunctions) -> dict:
    by_id = {s["id"]: s for s in selector_cert["selectors"]}
    routes = [
        {"route": "R-A no-site-privileged => freeness",
         "selector": "SEL01_free_on_shell",
         "verdict": "FAILS",
         "why": "quote-to-computation fidelity NONE; survivors "
                f"{by_id['SEL01_free_on_shell']['survivors']} (two classes)"},
        {"route": "R-B no-site-privileged => shell transitivity",
         "selector": "SEL02_transitive_on_shell",
         "verdict": "FAILS",
         "why": "fidelity NONE and computationally empty: no cyclic subgroup "
                "of a 24-element group with maximal element order 4 is "
                "transitive on six points, so this route deletes C3 too"},
        {"route": "R-C Record additivity => invariant multiplicity one",
         "selector": "SEL03_multiplicity_one_orbit_scope",
         "verdict": "FAILS",
         "why": "fidelity NONE; and at the orbit scope the filter is satisfied "
                "by every class, so it discriminates nothing"},
        {"route": "R-D Record additivity => shell multiplicity one",
         "selector": "SEL04_multiplicity_one_shell_scope",
         "verdict": "FAILS",
         "why": "fidelity NONE and computationally empty at the shell scope "
                "(the minimum shell multiplicity is 2, at C3_body)"},
        {"route": "R-E economy => minimal shell invariant multiplicity",
         "selector": "SEL05_minimal_shell_invariant_multiplicity",
         "verdict": "ISOLATES C3 BUT UNGROUNDED",
         "why": "no axiom sentence contains a minimization"},
        {"route": "R-F freeness + maximal orbit length",
         "selector": "SEL06_maximal_free_shell_orbit",
         "verdict": "ISOLATES C3 BUT UNGROUNDED",
         "why": "conjunction of two supplied clauses, neither quotable"},
        {"route": "R-G C882-T6 v_2 = 1 demand",
         "selector": "SEL07_coarse_pair_v2_equals_one",
         "verdict": "ISOLATES C3 BUT TARGET-FACING",
         "why": "fidelity EXACT to an OBLIGATION sentence, not to an axiom "
                "sentence; selecting the scope by the answer it must produce"},
        {"route": "R-H C882-T6 reachability of 2/9, orbit scope",
         "selector": "SEL08_reachability_R1_orbit_scope",
         "verdict": "ISOLATES C3 BUT TARGET-FACING",
         "why": "same defect as R-G, plus the filter is strictly stronger than "
                "its quote"},
        {"route": "R-I C882-T6 reachability of 2/9, shell scope",
         "selector": "SEL09_reachability_R2_shell_scope",
         "verdict": "FAILS",
         "why": "the SAME reachability demand at the OTHER scope admits "
                f"{by_id['SEL09_reachability_R2_shell_scope']['survivors']}; a "
                "selector whose answer depends on the scope cannot fix the scope"},
        {"route": "R-J fine reading of the weight pair",
         "selector": "SEL10_fine_top_pair_is_the_target",
         "verdict": "FAILS",
         "why": "under the rational-irreducible reading C4_face also carries "
                "(1, 2), via the Q(i) block of Q[C4]; survivors "
                f"{by_id['SEL10_fine_top_pair_is_the_target']['survivors']}"},
        {"route": "R-K 'cubic' => internal axis transitivity",
         "selector": "SEL11_transitive_on_coordinate_axes",
         "verdict": "ISOLATES C3 BUT UNGROUNDED (closest route)",
         "why": "the sentence grounds axis-equivalence for the FULL group; "
                "demanding a cyclic subgroup realize it internally is a "
                "strictly stronger supplied clause"},
        {"route": "R-L odd order",
         "selector": "SEL12_odd_order",
         "verdict": "ISOLATES C3 BUT UNGROUNDED",
         "why": "no axiom sentence mentions parity; cheapest single supplied "
                "clause on the board"},
        {"route": "R-M count-once / permanence",
         "selector": "SEL13_count_once",
         "verdict": "GROUNDED BUT NON-SELECTIVE",
         "why": "orbits of any group action already partition the shell, so "
                "the clause is true of every class"},
        {"route": "R-N content-only readout",
         "selector": "SEL14_content_only_readout",
         "verdict": "GROUNDED BUT NON-SELECTIVE",
         "why": "the permutation representation on record coordinates is "
                "content-only for any acting group"},
        {"route": "R-O Admissibility covariance",
         "selector": "SEL15_admissibility_covariance",
         "verdict": "GROUNDED ANTI-SELECTOR",
         "why": "the sentence names the covariance group as a whole; it is the "
                "textual reason every cyclic subgroup is equally supplied"},
        {"route": "R-P no-site-privileged read with both clauses",
         "selector": "SEL16_no_site_privileged_read_literally",
         "verdict": "GROUNDED ANTI-SELECTOR",
         "why": "every subgroup's orbit partition is determined by its axis, "
                "which is supplied lattice structure"},
    ]
    grounded_and_isolating = [
        r for r in routes
        if by_id[r["selector"]]["grounded"]
        and by_id[r["selector"]]["isolates_C3_body"]
    ]
    every_route_marked = all(r["verdict"] for r in routes)
    every_selector_covered = (
        {r["selector"] for r in routes}
        == {s["id"] for s in selector_cert["selectors"]}
    )
    return {
        "statement": (
            "The enumerated routes from the axiom set to the scope, each "
            "marked. A route counts as a DERIVATION only if its selector is "
            "axiom-grounded (fidelity EXACT to a byte-quoted AXIOM sentence) "
            "AND its survivor set is exactly {C3_body}."
        ),
        "routes": routes,
        "route_count": len(routes),
        "every_route_marked": every_route_marked,
        "every_selector_has_a_route": every_selector_covered,
        "routes_that_are_grounded_AND_isolating": grounded_and_isolating,
        "no_go_over_the_enumerated_routes": not grounded_and_isolating,
        "no_go_scope": (
            "This is a bounded no-go over the SIXTEEN enumerated routes, not a "
            "universal one. A new axiom-grounded route -- in particular one "
            "resting on a sentence outside the pinned memo, or on an approved "
            "primitive -- is not excluded by anything computed here."
        ),
        "finding": (
            f"{len(routes)} routes enumerated and marked; "
            f"{len(grounded_and_isolating)} of them are both axiom-grounded "
            f"and isolating, so the derivation route (a) is refused over the "
            f"enumerated set."
        ),
        "pass": every_route_marked and every_selector_covered,
    }


# --------------------------------------------------------------------------
# certificate M: the price
# --------------------------------------------------------------------------
def price_certificate(selector_cert, signature_cert, reach) -> dict:
    selectors = selector_cert["selectors"]
    isolating = [s for s in selectors if s["isolates_C3_body"]]
    labels = selector_cert["candidate_classes"]
    by_class = {s["label"]: s for s in signature_cert["by_class"]}

    consequence_rows = []
    for label in labels:
        s = by_class[label]
        reaches = {
            rule: label in reach["survivors_by_rule"][rule]
            for rule in sorted(GENERATOR_RULES)
        }
        consequence_rows.append({
            "scope_class": label,
            "orbit_scope_weight_pair": s["orbit_scope_pair"],
            "orbit_scope_2_adic_profile": s["orbit_scope_profile"],
            "orbit_scope_fine_dims": s["orbit_scope_fine_dims"],
            "fine_top_pair": s["orbit_scope_fine_top_pair"],
            "shell_scope_weight_pair": s["shell_scope_pair"],
            "carries_the_target_pair_coarse":
                s["carries_the_target_pair_coarse_orbit_scope"],
            "carries_the_target_pair_fine":
                s["carries_the_target_pair_fine_top_orbit_scope"],
            "supplies_a_v2_equals_1_datum_coarse":
                s["orbit_scope_profile"] is not None
                and s["orbit_scope_profile"][1] == 1,
            "reaches_2_9_by_rule": reaches,
            "defeats_C882_T6": reaches["R1_orbit_scope_coarse"],
        })
    defeaters = [r["scope_class"] for r in consequence_rows
                 if r["defeats_C882_T6"]]
    return {
        "statement": (
            "THE PRICE. C3_body is one of four admissible scope classes. "
            "Selecting it costs exactly ONE supplied clause; the menu of "
            "single clauses that each suffice is listed, and every rival "
            "scope's signature and consequences are tabulated beside it."
        ),
        "axiom_sentence_that_licenses_this_outcome":
            AXIOM_SENTENCES["unfixed_choice_stays_conditional"],
        "admissible_scope_classes": labels,
        "admissible_scope_class_count": len(labels),
        "minimum_supplied_clauses_to_pin_C3": 1 if isolating else None,
        "single_clause_menu": [
            {"selector": s["id"], "demand": s["demand"],
             "quoted_sentence": s["quoted_sentence"],
             "fidelity": s["fidelity"],
             "grounding_defect": s["grounding_defect"]}
            for s in isolating
        ],
        "single_clause_menu_size": len(isolating),
        "consequences_by_scope": consequence_rows,
        "scopes_that_defeat_C882_T6_under_cycle883s_own_rule": defeaters,
        "named_consequences_of_choosing_C3_body": (
            "the coarse weight pair (1, 2) with 2-adic profile (0, 1); the "
            "fine decomposition 1 + 2 over Q; three complex weights "
            "{1, omega, omega^2}; multiplicative reach of 2/9 under all four "
            "generator rules; hence C882-T6 defeated, exactly as Cycle 883 "
            "reported -- but as a CONSEQUENCE OF THE CHOICE, not of the axioms."
        ),
        "named_consequences_of_the_rivals": (
            "C2_face and C2_edge give the pair (1, 1), profile (0, 0), no "
            "v_2 = 1 datum, and no reach of 2/9 at the orbit scope -- though "
            "C2_edge DOES reach 2/9 at the shell scope, where its three free "
            "length-2 orbits supply the numbers 2 and 3. C4_face gives the "
            "coarse pair (1, 3), profile (0, 0), and never reaches 2/9 because "
            "<4, 3> has even 2-adic valuation throughout -- yet under the fine "
            "reading it DOES carry (1, 2) via the Q(i) block, so it fails the "
            "reachability test for a different reason than it fails the pair "
            "test."
        ),
        "what_this_does_to_cycle_883": (
            "SL1 is untouched: at the C3 scope the pair is still (1, 2) with "
            "no free parameter. What this cycle changes is the STATUS of the "
            "scope. Cycle 883 called it 'inherited'; it is now priced at one "
            "supplied clause, with the rival signatures on the table and the "
            "reachability selector shown to be scope-circular."
        ),
        "finding": (
            f"{len(labels)} admissible scope classes; "
            f"{len(isolating)} distinct single supplied clauses each pin "
            f"C3_body; under Cycle 883's own generator rule the scopes that "
            f"defeat C882-T6 are {defeaters}."
        ),
        "pass": len(labels) == 4 and bool(isolating),
    }


# --------------------------------------------------------------------------
# certificate N: impostor stress
# --------------------------------------------------------------------------
def impostor_stress_certificate(census) -> dict:
    group = set(proper_rotations())
    census_keys = {row["elements"] for row in census}

    def is_cyclic(subset: frozenset) -> bool:
        return any(cyclic_subgroup(g) == subset for g in subset)

    def is_closed(subset: frozenset) -> bool:
        return all(mul(a, b) in subset for a in subset for b in subset)

    rows = []

    klein = frozenset({
        IDENTITY3,
        ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
        ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
        ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    })
    rows.append({
        "impostor": "Klein four-group V (a genuine SUBGROUP, but not cyclic)",
        "is_a_subset_of_the_rotation_group": klein <= group,
        "is_closed": is_closed(klein),
        "is_cyclic": is_cyclic(klein),
        "appears_in_the_census": klein in census_keys,
        "refused_by_gate": "D_CYCLIC_SUBGROUP_CENSUS / every_subgroup_has_a_"
                           "generator_of_its_own_order",
        "refused": not is_cyclic(klein) and klein not in census_keys,
    })

    r3 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    partial = frozenset({IDENTITY3, r3})
    rows.append({
        "impostor": "a non-closed set {e, r3} passed off as a subgroup",
        "is_a_subset_of_the_rotation_group": partial <= group,
        "is_closed": is_closed(partial),
        "is_cyclic": is_cyclic(partial),
        "appears_in_the_census": partial in census_keys,
        "refused_by_gate": "D_CYCLIC_SUBGROUP_CENSUS / "
                           "every_subgroup_closed_under_composition",
        "refused": (not is_closed(partial)) and partial not in census_keys,
    })

    minus_i = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    improper = frozenset({IDENTITY3, minus_i})
    rows.append({
        "impostor": "the inversion -I smuggled in as a C2 (an IMPROPER rotation)",
        "determinant": det3(minus_i),
        "is_a_subset_of_the_rotation_group": improper <= group,
        "is_cyclic": is_cyclic(improper),
        "appears_in_the_census": improper in census_keys,
        "refused_by_gate": "C_ROTATION_GROUP / "
                           "every_element_has_determinant_plus_one",
        "refused": det3(minus_i) == -1 and improper not in census_keys,
    })

    order_counts: dict[int, int] = {}
    for m in group:
        order_counts[element_order(m)] = order_counts.get(element_order(m), 0) + 1
    rows.append({
        "impostor": "a claimed C6 subgroup",
        "elements_of_order_6_in_the_group": order_counts.get(6, 0),
        "subgroups_of_order_6_in_the_census":
            sum(1 for row in census if row["order"] == 6),
        "refused_by_gate": "D_CYCLIC_SUBGROUP_CENSUS / phi_identity_holds",
        "refused": order_counts.get(6, 0) == 0
                   and not any(row["order"] == 6 for row in census),
    })

    broken_lengths = [3, 4]
    rows.append({
        "impostor": "a broken shell orbit decomposition with lengths [3, 4]",
        "claimed_lengths": broken_lengths,
        "sum": sum(broken_lengths),
        "shell_size": len(NEAREST_NEIGHBOURS),
        "refused_by_gate": "E_SHELL_ORBIT_STRUCTURE / every_partition_sums_to_six",
        "refused": sum(broken_lengths) != len(NEAREST_NEIGHBOURS),
    })

    # broken isotype: claim Q[C4] decomposes as 1 + 2
    claimed = [1, 2]
    real = fine_decomposition(
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
        [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)], 4)
    real_dims = sorted(
        d for b in real["blocks"]
        for d in [euler_phi(b["root_of_unity_order"])] * int(b["multiplicity"])
    )
    rows.append({
        "impostor": "a broken isotype decomposition 1 + 2 claimed for a free C4 orbit",
        "claimed_dimensions": claimed,
        "claimed_sum": sum(claimed),
        "computed_dimensions": real_dims,
        "computed_sum": sum(real_dims),
        "refused_by_gate":
            "G_ISOTYPE_SIGNATURES / fine_decomposition_sums_to_the_space",
        "refused": sum(claimed) != 4 and sum(real_dims) == 4,
    })

    # a hardcoded survivor set must not be able to enter: survivors are always
    # computed from the census labels
    rows.append({
        "impostor": "a survivor set naming a class that is not in the census",
        "fabricated_label": "C5_body",
        "present_in_the_census":
            any(row["label"] == "C5_body" for row in census),
        "refused_by_gate":
            "I_SELECTOR_TABLE / every_survivor_set_is_a_subset_of_the_census",
        "refused": not any(row["label"] == "C5_body" for row in census),
    })

    all_refused = all(r["refused"] for r in rows)
    return {
        "statement": (
            "Seven impostors are offered to the gates. Each must be refused by "
            "a NAMED gate, and the refusal must be computed here rather than "
            "asserted."
        ),
        "rows": rows,
        "every_impostor_refused": all_refused,
        "finding": (
            f"{sum(1 for r in rows if r['refused'])}/{len(rows)} impostors "
            f"refused by named gates."
        ),
        "pass": all_refused,
    }


# --------------------------------------------------------------------------
# certificate O: the outcome
# --------------------------------------------------------------------------
def outcome_certificate(selector_cert, conjunctions, routes, price) -> dict:
    grounded_isolates = conjunctions["grounded_conjunction"]["isolates_C3_body"]
    no_go = routes["no_go_over_the_enumerated_routes"]
    priced = price["minimum_supplied_clauses_to_pin_C3"] is not None
    if grounded_isolates:
        outcome = "a_DERIVATION"
    elif priced and no_go:
        outcome = "b_PRICING"
    else:
        outcome = "c_NO_GO"
    return {
        "question": (
            "SL0. For which cyclic subgroups of the proper cubic rotation "
            "group does the Cycle-883 construction produce a readout carrying "
            "a weight pair, and what selects C3?"
        ),
        "answer": (
            "ALL of them. Every one of the four nontrivial conjugacy classes "
            "of cyclic subgroups produces a readout with a computable weight "
            "pair: C2_face and C2_edge give (1, 1), C3_body gives (1, 2), "
            "C4_face gives (1, 3) coarsely and 1 + 1 + 2 finely. Nothing in "
            "the four axioms selects among them. C3 is selected by exactly one "
            "supplied clause, and six different single clauses will do it."
        ),
        "outcome_class": outcome,
        "outcome_classes_available": list(OUTCOME_CLASSES),
        "a_DERIVATION_refused": not grounded_isolates,
        "a_refusal_reason": (
            "The conjunction of every axiom-grounded selector admits "
            f"{conjunctions['grounded_conjunction']['survivors']}, not "
            "{C3_body}. Every selector with EXACT fidelity to an axiom "
            "sentence is non-selective."
        ),
        "c_NO_GO_half_established": no_go,
        "c_no_go_statement": (
            "Bounded no-go: over the sixteen enumerated routes, none is both "
            "axiom-grounded and isolating. The no-go is over the enumerated "
            "set, not universal."
        ),
        "b_PRICING_headline": (
            "SL0 resolves as PRICING. The C3 orbit scope is one of four "
            "admissible scope classes; the selection costs exactly one "
            "supplied clause; the cheapest quotable candidate is the demand "
            "that the scope subgroup act transitively on the three coordinate "
            "axes, which C3_body alone satisfies and which the word 'cubic' "
            "motivates without licensing."
        ),
        "which_signatures_reach_the_v2_equals_1_datum": {
            "coarse_reading": sorted(
                r["scope_class"] for r in price["consequences_by_scope"]
                if r["supplies_a_v2_equals_1_datum_coarse"]
            ),
            "fine_reading": sorted(
                r["scope_class"] for r in price["consequences_by_scope"]
                if r["carries_the_target_pair_fine"]
            ),
            "reach_2_9_under_cycle883s_own_rule":
                price["scopes_that_defeat_C882_T6_under_cycle883s_own_rule"],
        },
        "effect_on_SL1": (
            "None. SL1's theorem is unchanged AT the C3 scope. Its status is "
            "changed: 'the C3 orbit scope is inherited, not derived' becomes "
            "'the C3 orbit scope is one supplied clause, priced, with the "
            "rival signatures computed and the reachability selector shown to "
            "be scope-circular'."
        ),
        "the_sharpest_new_fact": (
            "Cycle 883's uniqueness of (1, 2) is READING-DEPENDENT. Under the "
            "coarse (invariant, complement) reading it is unique to C3. Under "
            "the rational-irreducible reading, C4_face also carries (1, 2) -- "
            "trivial plus the Q(i) block -- so a v_2 = 1 datum exists at C4 as "
            "well. C4 still fails to reach 2/9, but for an unrelated reason "
            "(<4, 3> has even 2-adic valuation), and that is a different "
            "argument from the one Cycle 883 made."
        ),
        "the_second_sharpest_new_fact": (
            "The reachability selector is scope-circular. At the one-orbit "
            "scope it isolates C3; at the whole-shell scope C2_edge joins it, "
            "because three free length-2 orbits supply 2 and 3 exactly as one "
            "free length-3 orbit does. A selector whose verdict depends on the "
            "scope cannot be used to fix the scope."
        ),
        "next_attackable_question": (
            "Either (i) find an axiom-grounded sentence that demands internal "
            "axis transitivity of the scope subgroup -- the R-K route is the "
            "only one that came close and it needs a sentence the pinned memo "
            "does not contain; or (ii) register the scope choice as an "
            "approved primitive with the single-clause menu attached; or "
            "(iii) show that the DOWNSTREAM obligation is insensitive to the "
            "scope, which the C2_edge shell-scope reachability row suggests is "
            "worth testing."
        ),
        "finding": (
            f"outcome {outcome}: the axiom-grounded conjunction admits "
            f"{conjunctions['grounded_conjunction']['survivors']}, the "
            f"enumerated-route no-go holds, and the scope is priced at "
            f"{price['minimum_supplied_clauses_to_pin_C3']} supplied clause "
            f"chosen from a menu of {price['single_clause_menu_size']}."
        ),
        "pass": outcome in OUTCOME_CLASSES,
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def build_science() -> dict:
    _SHELL_ORBIT_CACHE.clear()
    pins = pins_certificate()
    sentences = axiom_sentences_certificate()
    rotations = rotation_group_certificate()
    census = build_census()
    classes = conjugacy_classes(census)
    census_cert = census_certificate(census, classes)
    orbit_cert = shell_orbit_certificate(census, classes)
    construction = c883_construction_certificate()
    signatures = isotype_signature_certificate(census, classes)
    invariance = class_invariance_certificate(signatures["rows"])
    reach = reachability_certificate(signatures["rows"])
    # collapse the per-subgroup signature rows to one row per class for the
    # selector table (certificate H has already gated class-constancy)
    class_rows = []
    for label in sorted({r["label"] for r in signatures["rows"]}):
        class_rows.append(next(r for r in signatures["rows"]
                               if r["label"] == label))
    orbit_class_rows = []
    for label in sorted({r["label"] for r in orbit_cert["rows"]
                         if r["order"] > 1}):
        orbit_class_rows.append(next(r for r in orbit_cert["rows"]
                                     if r["label"] == label))
    selectors = selector_table_certificate(orbit_class_rows, class_rows, reach)
    conjunctions = conjunction_certificate(selectors)
    routes = route_ledger_certificate(selectors, conjunctions)
    price = price_certificate(selectors, signatures, reach)
    impostors = impostor_stress_certificate(census)
    outcome = outcome_certificate(selectors, conjunctions, routes, price)
    return {
        "A_PINS": pins,
        "B_AXIOM_SENTENCES": sentences,
        "C_ROTATION_GROUP": rotations,
        "D_CYCLIC_SUBGROUP_CENSUS": census_cert,
        "E_SHELL_ORBIT_STRUCTURE": orbit_cert,
        "F_C883_CONSTRUCTION_REBUILT": construction,
        "G_ISOTYPE_SIGNATURES": signatures,
        "H_CLASS_INVARIANCE": invariance,
        "I_SELECTOR_TABLE": selectors,
        "J_CONJUNCTIONS": conjunctions,
        "K_ANCHOR_REACHABILITY": reach,
        "L_ROUTE_LEDGER": routes,
        "M_PRICE": price,
        "N_IMPOSTOR_STRESS": impostors,
        "O_OUTCOME": outcome,
    }


def preflight() -> int:
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).exists()]
    if missing:
        sys.stderr.write(
            "PREFLIGHT HARD FAIL: missing pinned artifact(s): "
            + ", ".join(missing) + "\n"
        )
        return 2
    bad = []
    for path in AUDIT_INPUT_PATHS:
        got = sha256(_read_bytes(path)).hexdigest()
        if got != EXPECTED_SHA256[path]:
            bad.append(f"{path} sha256 {got} != {EXPECTED_SHA256[path]}")
    if bad:
        sys.stderr.write("PREFLIGHT HARD FAIL: pin digest mismatch: "
                         + "; ".join(bad) + "\n")
        return 2
    return 0


def render(certs: dict) -> str:
    out = ["CYCLE 886 -- SL0: IS THE C3 ORBIT SCOPE FORCED, OR PRICED?", ""]
    for label in LABELS:
        cert = certs[label]
        out.append(f"[{'PASS' if cert['pass'] else 'FAIL'}] {label}")
        finding = cert.get("finding")
        if finding:
            out.append(f"    finding: {finding}")
        out.append("")
    out.append(json.dumps(certs, indent=2, sort_keys=True, default=str))
    return "\n".join(out) + "\n"


def run() -> int:
    code = preflight()
    if code:
        return code
    started = monotonic()
    science_a = build_science()
    science_b = build_science()
    deterministic = digest(science_a) == digest(science_b)

    certificates = {label: science_a[label] for label in LABELS}
    outcome = science_a["O_OUTCOME"]
    price = science_a["M_PRICE"]
    selectors = science_a["I_SELECTOR_TABLE"]

    receipt = {
        "cycle": 886,
        "question": (
            "SL0: for which cyclic subgroups of the proper cubic rotation "
            "group does the Cycle-883 construction produce a weight pair, and "
            "what selects C3 -- derivation, pricing, or no-go?"
        ),
        "outcome_class": outcome["outcome_class"],
        "answer": outcome["answer"],
        "a_DERIVATION_refused": outcome["a_DERIVATION_refused"],
        "c_NO_GO_half_established": outcome["c_NO_GO_half_established"],
        "cyclic_subgroup_census":
            science_a["D_CYCLIC_SUBGROUP_CENSUS"]["conjugacy_class_table"],
        "cyclic_subgroups_found":
            science_a["D_CYCLIC_SUBGROUP_CENSUS"]["cyclic_subgroups_found"],
        "signatures_by_class": science_a["G_ISOTYPE_SIGNATURES"]["by_class"],
        "shell_orbit_rows": [
            {k: v for k, v in row.items() if k != "elements"}
            for row in science_a["E_SHELL_ORBIT_STRUCTURE"]["rows"]
        ],
        "selectors": [
            {"id": s["id"], "demand": s["demand"],
             "quoted_sentence": s["quoted_sentence"],
             "quote_source": s["quote_source"],
             "fidelity": s["fidelity"], "grounded": s["grounded"],
             "grounding_defect": s["grounding_defect"],
             "survivors": s["survivors"],
             "isolates_C3_body": s["isolates_C3_body"]}
            for s in selectors["selectors"]
        ],
        "survivors_per_selector": {
            s["id"]: s["survivors"] for s in selectors["selectors"]
        },
        "grounded_conjunction_survivors":
            science_a["J_CONJUNCTIONS"]["grounded_conjunction"]["survivors"],
        "nonempty_conjunction_survivors":
            science_a["J_CONJUNCTIONS"]["nonempty_selector_conjunction"]["survivors"],
        "route_ledger": science_a["L_ROUTE_LEDGER"]["routes"],
        "reachability_survivors_by_rule":
            science_a["K_ANCHOR_REACHABILITY"]["survivors_by_rule"],
        "reachability_generator_rules": GENERATOR_RULES,
        "minimum_supplied_clauses_to_pin_C3":
            price["minimum_supplied_clauses_to_pin_C3"],
        "single_clause_menu": price["single_clause_menu"],
        "consequences_by_scope": price["consequences_by_scope"],
        "impostor_stress": science_a["N_IMPOSTOR_STRESS"]["rows"],
        "sharpest_new_facts": [
            outcome["the_sharpest_new_fact"],
            outcome["the_second_sharpest_new_fact"],
        ],
        "effect_on_SL1": outcome["effect_on_SL1"],
        "next_attackable_question": outcome["next_attackable_question"],
        "source_pins": [
            {"path": r["path"], "sha256": r["sha256"], "git_blob": r["git_blob"]}
            for r in science_a["A_PINS"]["rows"]
        ],
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    receipt_digest = sha256(RECEIPT.read_bytes()).hexdigest()

    text = render(certificates)
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    controls = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocked_modules_loaded": [
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ],
        "firewall_hits": list(FIREWALL.hits),
        "determinism": {
            "scope": "every certificate rebuilt from scratch and compared "
                     "digest for digest",
            "exact": deterministic,
            "science_digest": digest(science_a),
        },
        "receipt_path": str(RECEIPT.relative_to(ROOT)),
        "receipt_sha256": receipt_digest,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": stdout_bytes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "floating_point_in_certified_quantities": False,
        "gate_neutrality": (
            "No gate tests for a preferred subgroup or a preferred outcome. "
            "C gates on group axioms and Burnside; D on the Lagrange/phi "
            "census identity; E on orbit-stabilizer and the partition sum; F "
            "on two-route agreement for the rebuilt construction; G on "
            "decomposition sums and three-route agreement for every subgroup "
            "alike; H on class-constancy; I on grade validity and survivor-set "
            "wellformedness; K on window/lattice corroboration; N on impostor "
            "refusal. Every one of them passes identically whether the outcome "
            "is (a), (b) or (c)."
        ),
        "finding": (
            "All cited artifacts stayed text/AST/JSON-only behind the import "
            "firewall, the science payload rebuilt digest for digest, and the "
            "runtime and stdout caps were respected."
        ),
    }
    controls["pass"] = (
        deterministic
        and controls["runtime_under_limit"]
        and controls["stdout_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    certificates["P_CONTROLS"] = controls

    sys.stdout.write(text)
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} "
        f"runtime_under_limit={controls['runtime_under_limit']} "
        f"stdout={stdout_bytes}B receipt={receipt_digest[:16]}\n"
    )
    return 0 if all(cert["pass"] for cert in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
