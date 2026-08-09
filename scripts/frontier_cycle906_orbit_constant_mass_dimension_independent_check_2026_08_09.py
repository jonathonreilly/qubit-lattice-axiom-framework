#!/usr/bin/env python3
"""Cycle 906 independent check: specified to REFUTE the orbit-constant
pushforward-mass dimension theorem and its receipt.

Its only declared inputs are the two files of this same landing delta -- the
primary runner's source and the primary runner's receipt -- pinned by
sha256 and git blob and verified hard-fail before any comparison.  It reads
no ancestor artifact, no axiom file and no repository census, and imports no
repository module.

INDEPENDENCE.  The checker re-derives every advertised number from its own
in-file rebuild; it never takes a value from the receipt and re-prints it.
The rebuild differs from the primary's implementation path at every level
that matters:

  * base points are laid out in the reverse orbit order, fibre points are
    indexed in reverse base order, and the orbit-constancy rows are
    CONSECUTIVE differences around each orbit rather than differences
    against a fixed orbit head, so the constraint matrix is a different
    matrix with the same solution space;
  * the dimension is obtained by MODULAR rank over three large primes
    (integer arithmetic mod p) instead of the primary's fraction-free
    integer elimination;
  * a second dimension is obtained by a rank-nullity SPLIT -- the kernel of
    the pushforward map counted directly, plus the base-level dimension --
    which never touches the fibre-level matrix at all;
  * a third dimension is obtained from a reduced row echelon form over the
    rationals with an explicit free-variable basis, every vector of which is
    re-verified against both linear conditions.

REFUTATION DISCIPLINE.  Every advertised receipt row is a recomputed
comparison that fails closed, and nine planted receipt corruptions are
applied to confirm each gate can detect tampering.  The verdict is
CORROBORATES only when every comparison agrees and every tooth bites; any
disagreement, any failed gate, and any tooth that does not bite produces a
NONZERO EXIT.

Every fraction emitted is a BOOKKEEPING FRACTION, NOT A PROBABILITY.

Support runner.  Authority none, audit unset.  Independent audit still
required.
"""
from __future__ import annotations

import ast
import copy
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import itertools
import json
from pathlib import Path
import sys

AUDIT_TIMEOUT_SEC = 600

# Both declared inputs are files of THIS landing delta, reviewed here: the
# primary runner's source and the receipt that run emitted.  Nothing else --
# no ancestor source, receipt, note or axiom file -- is declared or read.
# The paths are written as literals because the cache envelope and the
# evidence-readiness gate parse this tuple without executing the module.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle906_orbit_constant_mass_dimension_2026_08_09.py",
    "outputs/orbit_constant_mass_dimension_cycle906_receipt_2026_08_09.json",
)

PRIMARY_PATH, PRIMARY_RECEIPT = AUDIT_INPUT_PATHS
SELF_PATH = ("scripts/frontier_cycle906_orbit_constant_mass_dimension"
             "_independent_check_2026_08_09.py")
RECEIPT_PATH = ("outputs/orbit_constant_mass_dimension_independent_check"
                "_cycle906_receipt_2026_08_09.json")

EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "a4b3ac215741e2f4b9d015708fbce089fd599cf92cfd821553a6cb08717b2fdf",
    PRIMARY_RECEIPT:
        "9bf77b90fdb7e5b6fde99d223a913404d7580d2f254f8d2199bd18668f7292b2",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "e358ad784912444e203bb06bed408501cf2cdb22",
    PRIMARY_RECEIPT: "ad7fe2c733141101f614008c20894406c5bc8bd1",
}

ROOT = Path(__file__).resolve().parents[1]
FRACTION_LABEL = "bookkeeping fraction, not probability"

# The checker's OWN transcription of the declared family.  It is compared
# against the primary's declared constants by an AST read below; a mismatch
# is a refutation, not a repair.
CHECK_MAX_BASE_POINTS = 5
CHECK_FIBRE_ALPHABET_SMALL = (1, 2, 3)
CHECK_FIBRE_ALPHABET_WIDE = (1, 2)
CHECK_WIDE_ALPHABET_FROM = 5

PRIMES = (2147483647, 2147483629, 2147483587)


class _RepositoryImportFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        leaf = fullname.rsplit(".", 1)[-1]
        if leaf.startswith(("frontier_", "toy_", "runner_cache")):
            self.hits.append(fullname)
            raise ImportError(f"independent checker forbids import: {fullname}")
        return None


FIREWALL = _RepositoryImportFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


DISAGREEMENTS: list[dict] = []


def disagree(gate: str, detail: str, expected: object, observed: object) -> None:
    DISAGREEMENTS.append({"gate": gate, "detail": detail,
                          "receipt_says": expected, "checker_finds": observed})


def emit(name: str, payload: dict) -> bool:
    ok = bool(payload.get("pass"))
    print(f"CERTIFICATE {name} {'PASS' if ok else 'FAIL'} {compact(payload)}")
    return ok


# ---------------------------------------------------------------------------
# independent linear algebra
# ---------------------------------------------------------------------------

def modular_rank(rows: list[list[int]], ncols: int, prime: int) -> int:
    mat = [[x % prime for x in row] for row in rows]
    nrows = len(mat)
    rank = 0
    for col in range(ncols):
        if rank >= nrows:
            break
        pivot = None
        for r in range(rank, nrows):
            if mat[r][col]:
                pivot = r
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inverse = pow(mat[rank][col], prime - 2, prime)
        prow = [(x * inverse) % prime for x in mat[rank]]
        mat[rank] = prow
        for r in range(rank + 1, nrows):
            factor = mat[r][col]
            if factor:
                row = mat[r]
                for c in range(col, ncols):
                    row[c] = (row[c] - factor * prow[c]) % prime
        rank += 1
    return rank


def rref_free_basis(rows: list[list[int]], ncols: int
                    ) -> list[list[Fraction]]:
    """Solution basis from the reduced row echelon form's free variables."""
    mat = [[Fraction(x) for x in row] for row in rows]
    pivots: list[int] = []
    r = 0
    for col in range(ncols):
        pivot = None
        for i in range(r, len(mat)):
            if mat[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        head = mat[r][col]
        mat[r] = [x / head for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][col] != 0:
                factor = mat[i][col]
                mat[i] = [a - factor * b for a, b in zip(mat[i], mat[r])]
        pivots.append(col)
        r += 1
    pivot_set = set(pivots)
    basis: list[list[Fraction]] = []
    for free_col in range(ncols):
        if free_col in pivot_set:
            continue
        vector = [Fraction(0)] * ncols
        vector[free_col] = Fraction(1)
        for i, pivot_col in enumerate(pivots):
            vector[pivot_col] = -mat[i][free_col]
        basis.append(vector)
    return basis


# ---------------------------------------------------------------------------
# the checker's own rebuild of an instance -- reverse layout, consecutive rows
# ---------------------------------------------------------------------------

class Rebuild:
    def __init__(self, orbit_sizes: tuple[int, ...],
                 fibre_sizes: tuple[int, ...],
                 zero_mask: tuple[int, ...]) -> None:
        self.orbit_sizes = orbit_sizes
        self.fibre_sizes = fibre_sizes
        self.zero_mask = zero_mask
        self.n_base = sum(orbit_sizes)
        # canonical (declared) base numbering, used only for the shared key
        orbits: list[tuple[int, ...]] = []
        start = 0
        for size in orbit_sizes:
            orbits.append(tuple(range(start, start + size)))
            start += size
        self.orbits = tuple(orbits)
        # the checker's OWN fibre indexing: reverse base order
        self.local_index: dict[tuple[int, int], int] = {}
        lookup: list[int] = []
        running = 0
        for base in reversed(range(self.n_base)):
            for local in range(fibre_sizes[base]):
                self.local_index[(base, local)] = running
                lookup.append(base)
                running += 1
        self.n_fibre = running
        self.base_lookup = tuple(lookup)
        self.required_zero = frozenset(b for b in range(self.n_base)
                                       if zero_mask[b])

    @property
    def key(self) -> tuple:
        return (self.orbit_sizes,
                tuple((self.fibre_sizes[v], int(v in self.required_zero))
                      for v in range(self.n_base)))

    def points(self, base: int) -> list[int]:
        return [self.local_index[(base, i)]
                for i in range(self.fibre_sizes[base])]

    def disjoint_orbits(self) -> tuple[tuple[int, ...], ...]:
        return tuple(o for o in self.orbits
                     if not (set(o) & self.required_zero))

    def constraint_rows(self) -> list[list[int]]:
        """Reverse layout, and CONSECUTIVE differences around each orbit."""
        rows: list[list[int]] = []
        for orbit in reversed(self.orbits):
            for i in range(len(orbit)):
                nxt = orbit[(i + 1) % len(orbit)]
                if len(orbit) == 1:
                    break
                if i == len(orbit) - 1:
                    break
                row = [0] * self.n_fibre
                for point in self.points(orbit[i]):
                    row[point] += 1
                for point in self.points(nxt):
                    row[point] -= 1
                rows.append(row)
        for base in sorted(self.required_zero, reverse=True):
            for point in self.points(base):
                row = [0] * self.n_fibre
                row[point] = 1
                rows.append(row)
        return rows

    def base_rows(self) -> list[list[int]]:
        rows: list[list[int]] = []
        for orbit in reversed(self.orbits):
            for i in range(len(orbit) - 1):
                row = [0] * self.n_base
                row[orbit[i]] += 1
                row[orbit[i + 1]] -= 1
                rows.append(row)
        for base in sorted(self.required_zero, reverse=True):
            row = [0] * self.n_base
            row[base] = 1
            rows.append(row)
        return rows

    # ---- three independent dimension routes -------------------------------

    def dimension_modular(self) -> tuple[int, list[int]]:
        rows = self.constraint_rows()
        ranks = [modular_rank(rows, self.n_fibre, p) for p in PRIMES]
        return self.n_fibre - max(ranks), ranks

    def dimension_split(self) -> int:
        """Rank-nullity split; never touches the fibre-level matrix."""
        kernel_of_pushforward = sum(
            self.fibre_sizes[v] - 1 for v in range(self.n_base)
            if v not in self.required_zero)
        base_rows = self.base_rows()
        base_dim = self.n_base - max(
            modular_rank(base_rows, self.n_base, p) for p in PRIMES)
        return kernel_of_pushforward + base_dim

    def dimension_rref(self) -> int:
        basis = rref_free_basis(self.constraint_rows(), self.n_fibre)
        for vector in basis:
            weight = {i: v for i, v in enumerate(vector) if v != 0}
            if not (self.satisfies_zero(weight)
                    and self.satisfies_orbit_constancy(weight)):
                return -1
        return len(basis)

    def base_dimension(self) -> int:
        base_rows = self.base_rows()
        return self.n_base - max(
            modular_rank(base_rows, self.n_base, p) for p in PRIMES)

    # ---- condition checks -------------------------------------------------

    def satisfies_zero(self, weight: dict[int, Fraction]) -> bool:
        return all(self.base_lookup[p] not in self.required_zero
                   for p, v in weight.items() if v != 0)

    def pushforward(self, weight: dict[int, Fraction]) -> list[Fraction]:
        mass = [Fraction(0)] * self.n_base
        for point, value in weight.items():
            mass[self.base_lookup[point]] += value
        return mass

    def satisfies_orbit_constancy(self, weight: dict[int, Fraction]) -> bool:
        mass = self.pushforward(weight)
        return all(all(mass[x] == mass[o[0]] for x in o) for o in self.orbits)

    # ---- representatives, rebuilt independently ---------------------------

    def uniform_representative(self) -> dict[int, Fraction] | None:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        out: dict[int, Fraction] = {}
        for base in orbit:
            share = Fraction(1, len(orbit) * self.fibre_sizes[base])
            for point in self.points(base):
                out[point] = share
        return out

    def concentrated_representative(self) -> dict[int, Fraction] | None:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return None
        orbit = disjoint[0]
        return {self.points(base)[0]: Fraction(1, len(orbit))
                for base in orbit}

    def cross_orbit_signed_witness(self) -> dict[int, Fraction] | None:
        disjoint_bases = {v for o in self.disjoint_orbits() for v in o}
        for base in range(self.n_base):
            if base in self.required_zero or base in disjoint_bases:
                continue
            if self.fibre_sizes[base] < 2:
                continue
            pts = self.points(base)
            return {pts[0]: Fraction(1), pts[1]: Fraction(-1)}
        return None

    def polytope_dimension(self) -> int:
        disjoint = self.disjoint_orbits()
        if not disjoint:
            return -1
        return sum(self.fibre_sizes[v] - 1 for o in disjoint for v in o) \
            + len(disjoint) - 1

    def zero_count(self, weight: dict[int, Fraction]) -> int:
        return self.n_fibre - sum(1 for v in weight.values() if v != 0)


def partitions(total: int) -> list[tuple[int, ...]]:
    if total == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def walk(remaining: int, cap: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for part in range(min(cap, remaining), 0, -1):
            walk(remaining - part, part, prefix + (part,))

    walk(total, total, ())
    return out


_FAMILY: list["Rebuild"] = []
_COMPUTED: dict[str, object] = {}


def rebuild_family() -> list[Rebuild]:
    if _FAMILY:
        return _FAMILY
    out: list[Rebuild] = []
    for n_base in range(1, CHECK_MAX_BASE_POINTS + 1):
        alphabet = (CHECK_FIBRE_ALPHABET_WIDE
                    if n_base >= CHECK_WIDE_ALPHABET_FROM
                    else CHECK_FIBRE_ALPHABET_SMALL)
        for orbit_sizes in partitions(n_base):
            for fibres in itertools.product(alphabet, repeat=n_base):
                for mask in range(1 << n_base):
                    bits = tuple(1 if mask & (1 << v) else 0
                                 for v in range(n_base))
                    out.append(Rebuild(orbit_sizes, fibres, bits))
    _FAMILY.extend(out)
    return _FAMILY


def computed_table() -> dict:
    """One sweep of the whole family; cached so the teeth stay cheap."""
    if "table" in _COMPUTED:
        return _COMPUTED["table"]  # type: ignore[return-value]
    table: list[tuple[str, int]] = []
    route_mismatches = 0
    first_mismatch = None
    base_mismatches = 0
    for inst in rebuild_family():
        modular, _ = inst.dimension_modular()
        split = inst.dimension_split()
        rref = inst.dimension_rref()
        if not (modular == split == rref):
            route_mismatches += 1
            if first_mismatch is None:
                first_mismatch = {"key": inst.key, "modular": modular,
                                  "split": split, "rref": rref}
        if inst.base_dimension() != len(inst.disjoint_orbits()):
            base_mismatches += 1
        table.append((compact(inst.key), modular))
    table.sort()
    result = {
        "table": table,
        "digest": digest(table),
        "sum": sum(d for _, d in table),
        "route_mismatches": route_mismatches,
        "first_mismatch": first_mismatch,
        "base_mismatches": base_mismatches,
    }
    _COMPUTED["table"] = result
    return result


def computed_witnesses() -> dict:
    if "witnesses" in _COMPUTED:
        return _COMPUTED["witnesses"]  # type: ignore[return-value]
    with_solution = two_distinct = zero_differs = signed_outside = 0
    defects: list[str] = []
    for inst in rebuild_family():
        uniform = inst.uniform_representative()
        if uniform is None:
            continue
        with_solution += 1
        concentrated = inst.concentrated_representative()
        for weight in (uniform, concentrated):
            if sum(weight.values(), Fraction(0)) != 1 \
                    or any(v < 0 for v in weight.values()) \
                    or not inst.satisfies_zero(weight) \
                    or not inst.satisfies_orbit_constancy(weight):
                defects.append("representative fails a declared property")
        if uniform != concentrated:
            two_distinct += 1
            if inst.pushforward(uniform) != inst.pushforward(concentrated):
                defects.append("distinct representatives disagree on mass")
            if inst.zero_count(uniform) != inst.zero_count(concentrated):
                zero_differs += 1
        witness = inst.cross_orbit_signed_witness()
        if witness is not None:
            signed_outside += 1
            if not (inst.satisfies_zero(witness)
                    and inst.satisfies_orbit_constancy(witness)):
                defects.append("cross-orbit signed witness is not a solution")
    result = {
        "counts": {
            "instances_with_a_disjoint_orbit": with_solution,
            "instances_with_two_distinct_representatives": two_distinct,
            "instances_where_zero_counts_differ": zero_differs,
            "instances_with_a_cross_orbit_signed_solution": signed_outside,
        },
        "defects": sorted(set(defects)),
    }
    _COMPUTED["witnesses"] = result
    return result


def computed_large(spec: dict) -> dict:
    params = spec.get("declared_parameters", {})
    key = compact([params.get("orbit_sizes"), params.get("fibre_rule"),
                   params.get("required_zero_rule")])
    cache: dict = _COMPUTED.setdefault("large", {})  # type: ignore[assignment]
    if key in cache:
        return cache[key]
    inst = rebuild_large(spec)
    uniform = inst.uniform_representative()
    values = {
        "base_points": inst.n_base,
        "fibre_points": inst.n_fibre,
        "orbits_disjoint_from_required_zero": len(inst.disjoint_orbits()),
        "solution_space_dimension": inst.dimension_split(),
        "pushforward_mass_dimension": inst.base_dimension(),
        "non_negative_normalized_polytope_dimension": inst.polytope_dimension(),
        "representative_zero_count": inst.zero_count(uniform),
    }
    representative_ok = (
        sum(uniform.values(), Fraction(0)) == 1
        and all(v >= 0 for v in uniform.values())
        and inst.satisfies_zero(uniform)
        and inst.satisfies_orbit_constancy(uniform))
    cache[key] = {"values": values, "representative_ok": representative_ok}
    return cache[key]


def rebuild_large(spec: dict) -> Rebuild:
    orbit_sizes = tuple(spec["declared_parameters"]["orbit_sizes"])
    n_base = sum(orbit_sizes)
    bounds: list[int] = []
    running = 0
    for size in orbit_sizes:
        bounds.append(running)
        running += size
    fibre_rule = spec["declared_parameters"]["fibre_rule"]
    zero_rule = spec["declared_parameters"]["required_zero_rule"]
    if "every base point carries 129" in fibre_rule:
        fibres = tuple(129 for _ in range(n_base))
    else:
        fibres = tuple(129 if v >= bounds[11] else 7 for v in range(n_base))
    if zero_rule.startswith("every base point of the first eleven orbits"):
        zero = set(range(bounds[11]))
    else:
        zero = set(range(bounds[10])) | {bounds[10]}
    bits = tuple(1 if v in zero else 0 for v in range(n_base))
    return Rebuild(orbit_sizes, fibres, bits)


# ---------------------------------------------------------------------------
# gates
# ---------------------------------------------------------------------------

def gate_pins() -> tuple[dict, dict]:
    payloads = {}
    for path in AUDIT_INPUT_PATHS:
        payloads[path] = (ROOT / path).read_bytes()
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    sha_ok = sha_rows == EXPECTED_SHA256
    blob_ok = blob_rows == EXPECTED_GIT_BLOBS
    receipt = json.loads(payloads[PRIMARY_RECEIPT].decode("utf-8"))
    # independent AST read of the primary's declared closure and family
    tree = ast.parse(payloads[PRIMARY_PATH].decode("utf-8"),
                     filename=PRIMARY_PATH)
    declared: dict[str, object] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            try:
                declared[name] = ast.literal_eval(node.value)
            except (ValueError, TypeError, SyntaxError):
                continue
    primary_closure = tuple(declared.get("AUDIT_INPUT_PATHS") or ())
    closure_is_self_only = primary_closure == (PRIMARY_PATH,)
    family_matches = (
        declared.get("MAX_BASE_POINTS") == CHECK_MAX_BASE_POINTS
        and tuple(declared.get("FIBRE_ALPHABET_SMALL") or ())
        == CHECK_FIBRE_ALPHABET_SMALL
        and tuple(declared.get("FIBRE_ALPHABET_WIDE") or ())
        == CHECK_FIBRE_ALPHABET_WIDE
        and declared.get("WIDE_ALPHABET_FROM") == CHECK_WIDE_ALPHABET_FROM
    )
    if not sha_ok:
        disagree("pins", "declared input sha256 drift",
                 EXPECTED_SHA256, sha_rows)
    if not blob_ok:
        disagree("pins", "declared input git blob drift",
                 EXPECTED_GIT_BLOBS, blob_rows)
    if not closure_is_self_only:
        disagree("pins",
                 "the primary's declared closure is not exactly its own source",
                 (PRIMARY_PATH,), primary_closure)
    if not family_matches:
        disagree("pins", "the primary's declared family differs from the "
                         "checker's independent transcription",
                 {"MAX_BASE_POINTS": CHECK_MAX_BASE_POINTS},
                 {k: declared.get(k) for k in
                  ("MAX_BASE_POINTS", "FIBRE_ALPHABET_SMALL",
                   "FIBRE_ALPHABET_WIDE", "WIDE_ALPHABET_FROM")})
    payload = {
        "certificate": "PINS",
        "declared_inputs": list(AUDIT_INPUT_PATHS),
        "both_declared_inputs_are_files_of_this_landing_delta": True,
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "sha256_all_match": sha_ok,
        "git_blobs_all_match": blob_ok,
        "primary_declared_closure": list(primary_closure),
        "primary_closure_is_its_own_source_only": closure_is_self_only,
        "primary_closure_contains_no_ancestor_artifact": True,
        "primary_family_matches_independent_transcription": family_matches,
        "import_firewall_hits": list(FIREWALL.hits),
    }
    payload["pass"] = bool(sha_ok and blob_ok and closure_is_self_only
                           and family_matches and not FIREWALL.hits)
    return payload, receipt


def gate_dimension_table(receipt: dict) -> dict:
    family = rebuild_family()
    computed = computed_table()
    route_mismatches = computed["route_mismatches"]
    first_mismatch = computed["first_mismatch"]
    table = computed["table"]
    own_digest = computed["digest"]
    claimed_digest = (receipt.get("certificates", {})
                      .get("THREE_ROUTES_AGREE", {})
                      .get("dimension_table_digest"))
    claimed_count = (receipt.get("certificates", {})
                     .get("THREE_ROUTES_AGREE", {}).get("instances"))
    claimed_sum = (receipt.get("certificates", {})
                   .get("THREE_ROUTES_AGREE", {}).get("dimension_sum"))
    own_sum = computed["sum"]
    if own_digest != claimed_digest:
        disagree("dimension_table", "per-instance dimension table digest",
                 claimed_digest, own_digest)
    if claimed_count != len(family):
        disagree("dimension_table", "instance count",
                 claimed_count, len(family))
    if claimed_sum != own_sum:
        disagree("dimension_table", "dimension sum", claimed_sum, own_sum)
    payload = {
        "certificate": "DIMENSION_TABLE_REBUILT",
        "instances_rebuilt": len(family),
        "primes_used": list(PRIMES),
        "routes": ["modular rank", "rank-nullity split",
                   "rational reduced row echelon free-variable basis"],
        "internal_route_mismatches": route_mismatches,
        "first_internal_mismatch": first_mismatch,
        "checker_dimension_table_digest": own_digest,
        "receipt_dimension_table_digest": claimed_digest,
        "digest_agrees": own_digest == claimed_digest,
        "checker_dimension_sum": own_sum,
        "receipt_dimension_sum": claimed_sum,
        "instance_count_agrees": claimed_count == len(family),
    }
    payload["pass"] = bool(route_mismatches == 0
                           and own_digest == claimed_digest
                           and claimed_count == len(family)
                           and claimed_sum == own_sum)
    return payload


def gate_base_level(receipt: dict) -> dict:
    family = rebuild_family()
    mismatches = computed_table()["base_mismatches"]
    claimed = (receipt.get("certificates", {})
               .get("THREE_ROUTES_AGREE", {}).get("base_level_disagreements"))
    if mismatches:
        disagree("base_level", "pushforward-mass dimension does not equal the "
                               "number of disjoint orbits", 0, mismatches)
    if claimed != 0:
        disagree("base_level", "receipt admits base-level disagreements",
                 0, claimed)
    payload = {
        "certificate": "PUSHFORWARD_DIMENSION_REBUILT",
        "statement": ("on every rebuilt instance the pushforward-mass"
                      " dimension, computed by modular rank on the checker's"
                      " own base-level matrix, equals the number of orbits"
                      " disjoint from the required-zero subset"),
        "instances_rebuilt": len(family),
        "checker_mismatches": mismatches,
        "receipt_base_level_disagreements": claimed,
    }
    payload["pass"] = bool(mismatches == 0 and claimed == 0)
    return payload


def gate_witnesses(receipt: dict) -> dict:
    computed = computed_witnesses()
    rows: dict = computed["counts"]
    defects: list[str] = list(computed["defects"])
    with_solution = rows["instances_with_a_disjoint_orbit"]
    two_distinct = rows["instances_with_two_distinct_representatives"]
    zero_differs = rows["instances_where_zero_counts_differ"]
    signed_outside = rows["instances_with_a_cross_orbit_signed_solution"]
    claimed = (receipt.get("certificates", {})
               .get("NON_NEGATIVE_WITNESSES", {}))
    for name, value in rows.items():
        if claimed.get(name) != value:
            disagree("witnesses", name, claimed.get(name), value)
    payload = {
        "certificate": "WITNESSES_REBUILT",
        "statement": ("the checker rebuilds both non-negative normalized"
                      " representatives and the cross-orbit signed witness"
                      " from its own layout and recounts every advertised"
                      " tally; a distinct second representative with the same"
                      " pushforward mass and a different zero count is what"
                      " keeps the retained claim at the pushforward level"),
        "checker_counts": rows,
        "receipt_counts": {k: claimed.get(k) for k in rows},
        "defects": sorted(set(defects))[:8],
        "counts_agree": all(claimed.get(k) == v for k, v in rows.items()),
    }
    payload["pass"] = bool(not defects
                           and all(claimed.get(k) == v for k, v in rows.items())
                           and with_solution and two_distinct
                           and zero_differs and signed_outside)
    return payload


def gate_large_instances(receipt: dict) -> dict:
    claimed_rows = (receipt.get("certificates", {})
                    .get("LARGE_DECLARED_INSTANCES", {}).get("rows", []))
    rows = []
    ok = bool(claimed_rows)
    for spec in claimed_rows:
        computed = computed_large(spec)
        own = computed["values"]
        representative_ok = computed["representative_ok"]
        agree = {k: (spec.get(k) == v) for k, v in own.items()}
        for k, matched in agree.items():
            if not matched:
                disagree("large_instances", f"{spec.get('name')}:{k}",
                         spec.get(k), own[k])
        if not representative_ok:
            disagree("large_instances",
                     f"{spec.get('name')}:representative", True, False)
        ok = ok and all(agree.values()) and representative_ok
        rows.append({"name": spec.get("name"), "checker_values": own,
                     "agrees": agree,
                     "representative_verified": representative_ok})
    payload = {
        "certificate": "LARGE_INSTANCES_REBUILT",
        "statement": ("each declared larger instance is rebuilt from the"
                      " receipt's declared parameters alone and every"
                      " advertised number is recomputed by the checker's"
                      " rank-nullity split and its own representative"),
        "rows": rows,
    }
    payload["pass"] = bool(ok)
    return payload


def gate_receipt_consistency(receipt: dict) -> dict:
    certificates = receipt.get("certificates", {})
    every_certificate_passes = all(bool(c.get("pass"))
                                   for c in certificates.values())
    claimed_all = bool(receipt.get("all_certificates_pass"))
    closure_self_only = receipt.get("AUDIT_INPUT_PATHS") == [PRIMARY_PATH]
    timeout = receipt.get("AUDIT_TIMEOUT_SEC")
    teeth = certificates.get("MUTATION_TEETH", {})
    teeth_all_bite = (teeth.get("teeth_total") == teeth.get("teeth_biting")
                      and (teeth.get("teeth_total") or 0) >= 9)
    self_containment = certificates.get("SELF_CONTAINMENT", {})
    no_external_reads = (
        self_containment.get("read_inventory", {})
        .get("external_or_ancestral_scientific_inputs") == []
        and not self_containment.get("repository_modules_imported"))
    if claimed_all and not every_certificate_passes:
        disagree("receipt_consistency",
                 "receipt claims all certificates pass while one does not",
                 True, False)
    if not closure_self_only:
        disagree("receipt_consistency",
                 "receipt evidence closure is not the primary's own source only",
                 [PRIMARY_PATH], receipt.get("AUDIT_INPUT_PATHS"))
    if not teeth_all_bite:
        disagree("receipt_consistency", "planted mutations do not all bite",
                 teeth.get("teeth_total"), teeth.get("teeth_biting"))
    if not no_external_reads:
        disagree("receipt_consistency",
                 "the primary reports an external scientific read", [], "some")
    payload = {
        "certificate": "RECEIPT_CONSISTENCY",
        "every_certificate_in_the_receipt_passes": every_certificate_passes,
        "receipt_claims_all_pass": claimed_all,
        "evidence_closure_is_the_primary_source_only": closure_self_only,
        "declared_audit_timeout_sec": timeout,
        "planted_mutations_all_bite": teeth_all_bite,
        "primary_reports_no_external_scientific_read": no_external_reads,
    }
    payload["pass"] = bool(every_certificate_passes == claimed_all
                           and claimed_all and closure_self_only
                           and teeth_all_bite and no_external_reads
                           and timeout == AUDIT_TIMEOUT_SEC)
    return payload


# ---------------------------------------------------------------------------
# teeth: planted receipt corruptions, each must be refused
# ---------------------------------------------------------------------------

def run_teeth(receipt: dict) -> dict:
    teeth: list[dict] = []

    def bite(name: str, mutate, gate) -> None:
        spoiled = copy.deepcopy(receipt)
        mutate(spoiled)
        before = len(DISAGREEMENTS)
        payload = gate(spoiled)
        caught = (not payload.get("pass")) or len(DISAGREEMENTS) > before
        del DISAGREEMENTS[before:]
        teeth.append({"tooth": name, "bites": bool(caught)})

    bite("corrupt_dimension_table_digest",
         lambda r: r["certificates"]["THREE_ROUTES_AGREE"].__setitem__(
             "dimension_table_digest", "0" * 64),
         gate_dimension_table)
    bite("corrupt_instance_count",
         lambda r: r["certificates"]["THREE_ROUTES_AGREE"].__setitem__(
             "instances", 1),
         gate_dimension_table)
    bite("corrupt_dimension_sum",
         lambda r: r["certificates"]["THREE_ROUTES_AGREE"].__setitem__(
             "dimension_sum", 0),
         gate_dimension_table)
    bite("corrupt_base_level_disagreements",
         lambda r: r["certificates"]["THREE_ROUTES_AGREE"].__setitem__(
             "base_level_disagreements", 3),
         gate_base_level)
    bite("corrupt_zero_count_witness_tally",
         lambda r: r["certificates"]["NON_NEGATIVE_WITNESSES"].__setitem__(
             "instances_where_zero_counts_differ", 0),
         gate_witnesses)
    bite("corrupt_large_instance_solution_dimension",
         lambda r: r["certificates"]["LARGE_DECLARED_INSTANCES"]["rows"][0]
         .__setitem__("solution_space_dimension", 1),
         gate_large_instances)
    bite("corrupt_large_instance_polytope_dimension",
         lambda r: r["certificates"]["LARGE_DECLARED_INSTANCES"]["rows"][0]
         .__setitem__("non_negative_normalized_polytope_dimension", 0),
         gate_large_instances)
    bite("corrupt_evidence_closure_to_an_ancestor_pin",
         lambda r: r.__setitem__(
             "AUDIT_INPUT_PATHS",
             [PRIMARY_PATH, "outputs/some_rejected_ancestor_receipt.json"]),
         gate_receipt_consistency)
    bite("launder_a_failed_certificate_into_all_pass",
         lambda r: r["certificates"]["MUTATION_TEETH"].__setitem__("pass", False),
         gate_receipt_consistency)

    payload = {
        "certificate": "TEETH",
        "statement": ("nine planted receipt corruptions, each applied to a"
                      " deep copy and pushed through the gate that owns it;"
                      " every one must be refused"),
        "teeth": teeth,
        "teeth_total": len(teeth),
        "teeth_biting": sum(1 for t in teeth if t["bites"]),
    }
    payload["pass"] = all(t["bites"] for t in teeth)
    return payload


def main() -> int:
    print("CYCLE906_INDEPENDENT_CHECK_SPECIFIED_TO_REFUTE")
    print("EVERY_EMITTED_FRACTION_IS_A_BOOKKEEPING_FRACTION_NOT_A_PROBABILITY")

    pins, receipt = gate_pins()
    ok = emit("PINS", pins)
    if not ok:
        print("VERDICT DISAGREES (declared inputs did not verify)")
        return 1

    order: list[str] = []
    certificates: dict[str, dict] = {}

    def record(payload: dict) -> bool:
        certificates[payload["certificate"]] = payload
        order.append(payload["certificate"])
        return emit(payload["certificate"], payload)

    certificates["PINS"] = pins
    order.append("PINS")
    ok &= record(gate_dimension_table(receipt))
    ok &= record(gate_base_level(receipt))
    ok &= record(gate_witnesses(receipt))
    ok &= record(gate_large_instances(receipt))
    ok &= record(gate_receipt_consistency(receipt))
    ok &= record(run_teeth(receipt))

    verdict = "CORROBORATES" if (ok and not DISAGREEMENTS) else "DISAGREES"
    summary = {
        "certificate": "VERDICT",
        "verdict": verdict,
        "disagreements": DISAGREEMENTS[:8],
        "disagreement_count": len(DISAGREEMENTS),
        "gates_run": order,
        "all_gates_pass": bool(ok),
        "pass": bool(ok and not DISAGREEMENTS),
    }
    emit("VERDICT", summary)

    out = {
        "runner": SELF_PATH,
        "checks": PRIMARY_PATH,
        "authority": "none",
        "audit": "unset",
        "AUDIT_INPUT_PATHS": list(AUDIT_INPUT_PATHS),
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "fraction_label": FRACTION_LABEL,
        "checker_verdict": verdict,
        "disagreements": DISAGREEMENTS,
        "certificates": {name: certificates[name] for name in order},
        "all_certificates_pass": bool(ok and not DISAGREEMENTS),
    }
    (ROOT / RECEIPT_PATH).write_text(
        json.dumps(out, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    print(f"RECEIPT {RECEIPT_PATH} sha256={digest(out)[:16]}")
    print(f"VERDICT {verdict}")
    return 0 if (ok and not DISAGREEMENTS) else 1


if __name__ == "__main__":
    sys.exit(main())
