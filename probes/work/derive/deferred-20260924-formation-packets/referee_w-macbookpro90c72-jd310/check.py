#!/usr/bin/env python3
"""Independent referee: deferred-20260924-formation-packets a1.

Recomputes the record-ring flip graph, the separating function, the cyclic
span of the uniform vector, the frozen nullity-one controls, and the
alternating-cycle counterexample. Does not import the attempt.
"""
from __future__ import annotations

import hashlib
import itertools
import subprocess
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


# ---------------------------------------------------------------- sources
HEAD = "ff1edc030d8a2aaec9aab16a2354e7cc113ef8cf"
MAIN = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"
SRC = ".claude/science/mobile-record-formation-20260920/campaign12h_third/"
HELPER = SRC + "local_gauge_record_cooling_check.py"
README = SRC + "LOCAL_FIELD_PUBLICATION_README.md"
LANDED = "scripts/local_gauge_record_cooling_check.py"
WANT = {
    HELPER: "9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552",
    README: "920f0bfd9b8e3d5a7ce15ecd55ec3a5a491075056601b2a0e869101eddbe1349",
    LANDED: "1dfd370af4b92bcff307a91314e610750e7b7961184a547f2f33d094027a8282",
}


def blob(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", ref + ":" + path])


main_sha = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
helper_b = blob(HEAD, HELPER)
readme_b = blob(HEAD, README)
landed_b = blob("origin/main", LANDED)
hash_ok = (
    main_sha == MAIN
    and hashlib.sha256(helper_b).hexdigest() == WANT[HELPER]
    and hashlib.sha256(readme_b).hexdigest() == WANT[README]
    and hashlib.sha256(landed_b).hexdigest() == WANT[LANDED]
)
manifest = open("probes/work/deferred-science-20260924/review-unit12-v1.json", encoding="utf-8").read()
pin = '"original_path": "' + HELPER + '"'
pin_at = manifest.find(pin)
window = manifest[pin_at:pin_at + 900] if pin_at >= 0 else ""
manifest_ok = (
    pin_at >= 0
    and WANT[HELPER] in window
    and WANT[LANDED] in window
    and "unused cooling calculations deferred" in window
)
landed_ok = (
    b"def geometry" in landed_b
    and b"def gauss" in landed_b
    and b"Lindblad" not in landed_b
    and b"matching_matrix" not in landed_b
)
readme_flat = b" ".join(readme_b.split())
readme_ok = b"unused cooling routines are not additional claims of this unit" in readme_flat
check(
    "V1 frozen sources",
    hash_ok and manifest_ok and landed_ok and readme_ok,
    "origin/main %s; helper, README, and landed extract match the manifest pins; "
    "the landed file keeps geometry and gauss only" % main_sha[:12],
)


# ---------------------------------------------------------------- local algebra
def local_algebra() -> bool:
    L = sp.Matrix([[1, -1, 0], [1, -1, 0], [0, 0, 0]]) / 2
    Pm, Pp, I3 = L.T * L, L * L.T, sp.eye(3)
    a, b = sp.symbols("a b")

    def chan(q):
        K0 = I3 + (q - 1) * Pm
        return sp.kronecker_product(K0, K0) + (1 - q**2) * sp.kronecker_product(L, L)

    D = sp.kronecker_product(L, L) - (
        sp.kronecker_product(I3, Pm) + sp.kronecker_product(Pm, I3)
    ) / 2
    compose = (chan(a) * chan(b) - chan(a * b)).applyfunc(sp.expand)
    deriv = (-sp.diff(chan(a), a).subs(a, 1) / 2 - D).applyfunc(sp.expand)
    partial = (
        L * L == sp.zeros(3)
        and Pm**2 == Pm
        and Pp**2 == Pp
        and Pm * Pp == sp.zeros(3)
        and L.T * L == Pm
        and L * L.T == Pp
    )
    # One flip pair, no spectator: m^T v = 2 κ P^- v for v = (1, t).
    m = sp.Matrix([[1, -1], [1, -1]])
    t = sp.symbols("t")
    v = sp.Matrix([1, t])
    kappa = (1 + t) / (1 - t)
    Pminus = sp.together(m.T * m / 4)
    handle = sp.simplify((m.T * v - 2 * kappa * Pminus * v) * (1 - t))
    return bool(partial and compose == sp.zeros(9) and deriv == sp.zeros(9) and handle == sp.zeros(2, 1))


check(
    "A1 local algebra",
    local_algebra(),
    "L = |+><-| is a partial isometry, L^2 = 0; Phi_a Phi_b = Phi_(ab); "
    "half the derivative at 1 is D[L]; m^T v = 2 κ P^- v on a pair",
)


# ---------------------------------------------------------------- separating-function lemma
def base3_injective(limit: int = 40) -> bool:
    # |sum_{i<j} 3^i (s_i-s'_i)| <= 3^j - 1 < 2 * 3^j = |3^j (s_j-s'_j)|.
    for j in range(1, limit):
        if not (3**j - 1 < 2 * 3**j):
            return False
    return True


def signed_pow3_nonzero(limit: int = 40) -> bool:
    # Any nonempty signed sum of distinct powers of 3 is nonzero:
    # the largest power strictly exceeds the sum of the smaller ones.
    for e in range(0, limit):
        if not ((3**e - 1) // 2 < 3**e):
            return False
    return True


check(
    "F0 base-3 lemma",
    base3_injective() and signed_pow3_nonzero(),
    "F2 = sum_j 3^j s_j, s_j = ±1, is injective on every cube of dimension < 40; "
    "a signed sum of distinct powers of 3 cannot vanish",
)


# ---------------------------------------------------------------- geometry
def geometry(shape, periodic):
    vertices = list(itertools.product(*[range(n) for n in shape]))
    vset = set(vertices)

    def shift(v, axis):
        q = list(v)
        q[axis] += 1
        if periodic:
            q[axis] %= shape[axis]
        q = tuple(q)
        return q if q in vset else None

    edges = []
    for v in vertices:
        for axis in range(len(shape)):
            w = shift(v, axis)
            if w is not None:
                edges.append((v, axis, w))
    ei = {(v, axis): j for j, (v, axis, w) in enumerate(edges)}
    faces = []
    skipped = 0
    for v in vertices:
        for a, b in itertools.combinations(range(len(shape)), 2):
            va, vb = shift(v, a), shift(v, b)
            if va is None or vb is None or (va, b) not in ei or (vb, a) not in ei:
                continue
            raised = (ei[(v, a)], ei[(va, b)])
            lowered = (ei[(vb, a)], ei[(v, b)])
            if len(set(raised + lowered)) < 4:
                skipped += 1
                continue
            faces.append(
                {
                    "raised": raised,
                    "lowered": lowered,
                    "r": sum(1 << e for e in raised),
                    "l": sum(1 << e for e in lowered),
                }
            )
    return vertices, edges, faces, skipped


def flip_preserves_divergence(vertices, edges, face) -> bool:
    """A raising flip has known signs: lowered links are occupied, raised links empty.

    Reversing a link of sign s changes the divergence by -2s at its tail and
    +2s at its head. The four-link change is therefore independent of every
    other link, and it has to cancel at every vertex.
    """
    delta = {v: 0 for v in vertices}

    def reverse(edge_index: int, old_sign: int) -> None:
        tail, _axis, head = edges[edge_index]
        change = -2 * old_sign
        delta[tail] += change
        delta[head] -= change

    for edge_index in face["lowered"]:
        reverse(edge_index, 1)
    for edge_index in face["raised"]:
        reverse(edge_index, -1)
    return all(value == 0 for value in delta.values())


class ModSpan:
    def __init__(self, dim: int, prime: int):
        self.d = dim
        self.p = prime
        self.piv: dict[int, list[int]] = {}

    def insert(self, vec) -> bool:
        p, d = self.p, self.d
        v = [int(x) % p for x in vec]
        for col, row in self.piv.items():
            factor = v[col]
            if factor:
                for i in range(d):
                    v[i] = (v[i] - factor * row[i]) % p
        pivot = next((c for c in range(d) if v[c]), -1)
        if pivot < 0:
            return False
        inv = pow(v[pivot], -1, p)
        for i in range(d):
            v[i] = (v[i] * inv) % p
        for col, row in list(self.piv.items()):
            factor = row[pivot]
            if factor:
                for i in range(d):
                    row[i] = (row[i] - factor * v[i]) % p
        self.piv[pivot] = v
        return True


def cyclic_rank(dim: int, rows, prime: int) -> int:
    span = ModSpan(dim, prime)
    ones = tuple(1 for _ in range(dim))
    if not span.insert(ones):
        return 0
    raw = [ones]
    head = 0
    while head < len(raw) and len(span.piv) < dim:
        cur = raw[head]
        head += 1
        for row in rows:
            image = [0] * dim
            for a, b in row:
                total = (cur[a] + cur[b]) % prime
                image[a] = (image[a] + total) % prime
                image[b] = (image[b] - total) % prime
            if span.insert(image):
                raw.append(tuple(image))
    return len(span.piv)


def pair_graph_connected(dim: int, rows) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        node = stack.pop()
        for row in rows:
            for a, b in row:
                other = b if a == node else a if b == node else None
                if other is not None and other not in seen:
                    seen.add(other)
                    stack.append(other)
    return len(seen) == dim


def pairs_of(states, faces):
    index = {c: i for i, c in enumerate(states)}
    rows = []
    for face in faces:
        row = []
        used = set()
        for c in states:
            if c & face["r"] == 0 and c & face["l"] == face["l"]:
                other = c ^ face["r"] ^ face["l"]
                a, b = index[c], index[other]
                if a == b or a in used or b in used:
                    return None
                used.add(a)
                used.add(b)
                row.append((a, b))
        rows.append(row)
    return rows


P1 = 1000003
P2 = 1000033
if not (sp.isprime(P1) and sp.isprime(P2)):
    raise SystemExit("referee primes are not prime")


def rank_mod(matrix, prime: int) -> int:
    mat = np.array(matrix, dtype=np.int64) % prime
    rows, cols = mat.shape
    rank = 0
    for col in range(cols):
        if rank == rows:
            break
        nz = np.flatnonzero(mat[rank:, col])
        if nz.size == 0:
            continue
        pivot = rank + int(nz[0])
        if pivot != rank:
            mat[[rank, pivot]] = mat[[pivot, rank]]
        inv = pow(int(mat[rank, col]), -1, prime)
        mat[rank] = (mat[rank] * inv) % prime
        factor = mat[:, col].copy()
        factor[rank] = 0
        if np.any(factor):
            mat = (mat - np.outer(factor, mat[rank])) % prime
        rank += 1
    return int(rank)


def sqrt_minus_one(prime: int) -> int:
    for a in range(2, prime):
        if (a * a) % prime == prime - 1:
            return a
    raise RuntimeError("no square root of -1")


I65537 = 256
assert (I65537 * I65537) % 65537 == 65536


def eight_G(dim, face_rows, gammas, hs, extra_H8=None):
    eye = np.eye(dim, dtype=np.int64)
    real = np.zeros((dim * dim, dim * dim), dtype=np.int64)
    H8 = np.zeros((dim, dim), dtype=np.int64)
    for row, gamma, hh in zip(face_rows, gammas, hs):
        em = np.zeros((dim, dim), dtype=np.int64)
        for a, b in row:
            em[a, a] += 1
            em[b, a] += 1
            em[a, b] -= 1
            em[b, b] -= 1
        pm4 = em.T @ em
        real += int(gamma) * (2 * np.kron(em, em) - np.kron(eye, pm4) - np.kron(pm4, eye))
        H8 += 2 * int(hh) * pm4
    if extra_H8 is not None:
        H8 = H8 + np.array(extra_H8, dtype=np.int64)
    imag = np.kron(H8.T, eye) - np.kron(eye, H8)
    return real, imag


def nullity_one(dim, face_rows, gammas, hs, extra_H8=None) -> bool:
    real, imag = eight_G(dim, face_rows, gammas, hs, extra_H8)
    target = np.ones(dim * dim, dtype=np.int64)
    if np.any(real @ target) or np.any(imag @ target):
        return False
    primes = (65537,) if np.any(imag) else (P1,)
    iunits = {65537: I65537}
    for prime in primes:
        if np.any(imag):
            encoded = (real + iunits[prime] * imag) % prime
        else:
            encoded = real % prime
        if rank_mod(encoded, prime) == dim * dim - 1:
            return True
    # A short rank can be an unlucky reduction. Retry the complex encoding
    # at a second prime before rejecting.
    prime = 7340033  # 1 mod 4
    assert sp.isprime(prime) and prime % 4 == 1
    iunit = sqrt_minus_one(prime)
    encoded = (real + iunit * imag) % prime
    return rank_mod(encoded, prime) == dim * dim - 1


# Self-test the span and the rank before any census.
_span = ModSpan(3, P1)
assert _span.insert([1, 0, 0]) and _span.insert([0, 1, 0]) and not _span.insert([2, 3, 0])
assert cyclic_rank(4, [[(0, 1), (2, 3)], [(1, 2), (3, 0)]], P1) == 2
assert cyclic_rank(2, [[(0, 1)]], P1) == 2
assert rank_mod(np.eye(4, dtype=np.int64), P1) == 4
assert rank_mod(np.ones((3, 3), dtype=np.int64), P1) == 1


# ---------------------------------------------------------------- census
GEOMS = [
    ((2, 2), False),
    ((3, 2), False),
    ((2, 2, 2), False),
    ((3, 3), False),
    ((4, 2), False),
    ((4, 3), False),
    ((2, 2), True),
    ((3, 2), True),
    ((3, 3), True),
]
ANCHOR = {((2, 2), False): 2, ((3, 2), False): 3, ((2, 2, 2), False): 9}

total = 0
sep_ok = 0
conn_ok = 0
cyc_ok = 0
gauss_faces = 0
gauss_faces_total = 0
max_d = 0
per_geom = []
frozen = {}


def scan(shape, periodic):
    global total, sep_ok, conn_ok, cyc_ok, gauss_faces, gauss_faces_total, max_d
    vertices, edges, faces, skipped = geometry(shape, periodic)
    for face in faces:
        gauss_faces_total += 1
        gauss_faces += flip_preserves_divergence(vertices, edges, face)
    ne = len(edges)
    pow3 = [3**j for j in range(ne)]
    masks = [(f["r"], f["l"]) for f in faces]
    seen = bytearray(1 << ne)
    nbig = 0
    local_max = 0
    local_frozen = None
    t_geom = time.time()
    for seed in range(1 << ne):
        if seen[seed]:
            continue
        stack = [seed]
        seen[seed] = 1
        states = [seed]
        while stack:
            cur = stack.pop()
            for raised, lowered in masks:
                if (cur & raised == 0 and cur & lowered == lowered) or (
                    cur & raised == raised and cur & lowered == 0
                ):
                    nxt = cur ^ raised ^ lowered
                    if not seen[nxt]:
                        seen[nxt] = 1
                        states.append(nxt)
                        stack.append(nxt)
        dim = len(states)
        if dim < 2:
            continue
        nbig += 1
        total += 1
        local_max = max(local_max, dim)
        max_d = max(max_d, dim)
        rows = pairs_of(states, faces)
        if rows is None:
            continue
        nonempty = [row for row in rows if row]
        # Separating F2 and constant plaquette displacement.
        values = []
        for bits in states:
            acc = 0
            for j in range(ne):
                acc += pow3[j] if (bits >> j) & 1 else -pow3[j]
            values.append(acc)
        index = {c: i for i, c in enumerate(states)}
        good_f = len(set(values)) == dim
        for face, row in zip(faces, rows):
            if not row:
                continue
            delta = 2 * (
                sum(pow3[e] for e in face["raised"]) - sum(pow3[e] for e in face["lowered"])
            )
            good_f = good_f and delta != 0 and all(
                values[b] - values[a] == delta for a, b in row
            )
        sep_ok += good_f
        # Exact connectivity of the pair graph: common kernel is the constants.
        good_c = pair_graph_connected(dim, nonempty) and len(nonempty) >= 1
        conn_ok += good_c
        # Cyclicity of the uniform vector under the transposed jumps.
        if dim == 2:
            good_y = good_c
        else:
            rank = cyclic_rank(dim, nonempty, P1)
            if rank != dim:
                rank = cyclic_rank(dim, nonempty, P2)
            good_y = rank == dim
        cyc_ok += good_y
        if local_frozen is None or dim > local_frozen[0]:
            local_frozen = (dim, rows)
    per_geom.append(
        (
            shape,
            periodic,
            nbig,
            local_max,
            len(edges),
            len(faces),
            skipped,
            time.time() - t_geom,
        )
    )
    label = "%s%s" % ("x".join(str(n) for n in shape), "p" if periodic else "o")
    print(
        "  census %s components=%d max_d=%d links=%d faces=%d skipped=%d %.1fs"
        % (label, nbig, local_max, len(edges), len(faces), skipped, time.time() - t_geom),
        flush=True,
    )
    if (shape, periodic) in ANCHOR and local_max != ANCHOR[(shape, periodic)]:
        check(
            "anchor " + label,
            False,
            "largest component is %d, attempt states %d" % (local_max, ANCHOR[(shape, periodic)]),
        )
        return
    if (shape, periodic) in ANCHOR:
        frozen[(shape, periodic)] = local_frozen


for shape, periodic in GEOMS:
    scan(shape, periodic)
    if any(tag.startswith("anchor") for tag in FAILS):
        break

census_msg = ", ".join(
    "%s%s:%d(max %d)"
    % ("x".join(str(n) for n in shape), "p" if periodic else "o", nbig, local_max)
    for shape, periodic, nbig, local_max, *_rest in per_geom
)
check(
    "F1 separating function",
    sep_ok == total and total > 0,
    "F2 injective with a nonzero constant displacement on all %d components; %s" % (total, census_msg),
)
check(
    "U1 cyclic uniform vector",
    cyc_ok == total and conn_ok == total and total > 0,
    "pair graph connected and the uniform vector cyclic (mod %d, retry %d) on every component, d up to %d"
    % (P1, P2, max_d),
)
check(
    "G1 divergence",
    gauss_faces == gauss_faces_total and gauss_faces_total > 0,
    "every retained plaquette flip changes the lattice divergence by zero, so each component is one Gauss sector (%d faces)"
    % gauss_faces_total,
)


# ---------------------------------------------------------------- frozen nullity and a second Hamiltonian
def frozen_point(dim, face_rows) -> bool:
    nfaces = len(face_rows)
    gammas = [q + 1 for q in range(nfaces)]
    hs = [(-1) ** q * (q + 2) for q in range(nfaces)]
    return nullity_one(dim, face_rows, gammas, hs)


def positive_point(dim, face_rows, extra) -> bool:
    nfaces = len(face_rows)
    return nullity_one(dim, face_rows, [1] * nfaces, [0] * nfaces, extra)


ok_frozen = True
dims = []
index_same = True
if len(frozen) == 3:
    for shape in ((2, 2), (3, 2), (2, 2, 2)):
        dim, face_rows = frozen[(shape, False)]
        dims.append(dim)
        ok_frozen = ok_frozen and frozen_point(dim, face_rows)
        nonempty = [row for row in face_rows if row]
        # The attempt numbers only nonempty plaquettes. Record whether that
        # is the same rate vector as the frozen face order.
        src_rates = [
            (q + 1, (-1) ** q * (q + 2)) for q, row in enumerate(face_rows) if row
        ]
        alt_rates = [(q + 1, (-1) ** q * (q + 2)) for q in range(len(nonempty))]
        index_same = index_same and src_rates == alt_rates
        v = np.zeros(dim, dtype=np.int64)
        v[0], v[1] = 1, -1
        ok_frozen = ok_frozen and positive_point(dim, face_rows, 8 * np.outer(v, v))
        ok_frozen = ok_frozen and positive_point(dim, face_rows, None)
check(
    "R1 frozen nullity",
    ok_frozen and dims == [2, 3, 9],
    "largest open 2x2, 3x2, 2x2x2 components d=%s; frozen rates and H=v v^T "
    "(v orthogonal to the uniform vector) each give nullity one; nonempty reindexing %s"
    % (dims, "matches the frozen face order" if index_same else "DIFFERS from the frozen face order"),
)


# ---------------------------------------------------------------- two-level symbolic kernel
def two_level_symbolic() -> bool:
    em = sp.Matrix([[1, -1], [1, -1]])
    pm4 = em.T * em
    eye = sp.eye(2)
    diss = (
        2 * sp.kronecker_product(em, em)
        - sp.kronecker_product(eye, pm4)
        - sp.kronecker_product(pm4, eye)
    )
    g, h = sp.symbols("g h")
    H8 = 2 * h * pm4
    imag = sp.kronecker_product(H8.T, eye) - sp.kronecker_product(eye, H8)
    matrix = g * diss + sp.I * imag
    if sp.simplify(matrix * sp.ones(4, 1)) != sp.zeros(4, 1):
        return False
    # The leading 3x3 minor is -64 g (g^2 + 4 h^2). For real g, h this is
    # nonzero exactly when g != 0, since g^2 + (2h)^2 > 0 then. The all-ones
    # vector is always a kernel vector, so the nullity is one for every real
    # rate g != 0 and every real coefficient h.
    witness = sp.factor(sp.expand(matrix[:3, :3].det()))
    dropped = matrix.subs({g: 0, h: 1}).rank() < 3
    return bool(witness == -64 * g * (g**2 + 4 * h**2) and dropped)


check(
    "K1 two-level kernel",
    two_level_symbolic(),
    "on one flip pair the leading minor is -64 g (g^2+4 h^2), so the nullity is one for every real g != 0 and every real h",
)


# ---------------------------------------------------------------- counterexample
def counterexample() -> bool:
    rows = [[(0, 1), (2, 3)], [(1, 2), (3, 0)]]
    if cyclic_rank(4, rows, P1) != 2:
        return False
    if not pair_graph_connected(4, rows):
        return False
    m1 = sp.zeros(4)
    m2 = sp.zeros(4)
    for (mat, row) in ((m1, rows[0]), (m2, rows[1])):
        for a, b in row:
            mat[a, a] += 1
            mat[b, a] += 1
            mat[a, b] -= 1
            mat[b, b] -= 1
    L1, L2 = m1 / 2, m2 / 2
    u = sp.ones(4, 1)
    v = sp.Matrix([1, 1, -1, -1]) / 2
    w = sp.Matrix([-1, 1, 1, -1]) / 2
    rho = (v * v.T + w * w.T) / 2

    def dissip(jump, state):
        return jump * state * jump.T - (jump.T * jump * state + state * jump.T * jump) / 2

    # Constant displacement on each matching forces F(0)=F(2) and F(1)=F(3).
    f = sp.symbols("f0:4")
    equations = [f[1] - f[0] - (f[3] - f[2]), f[2] - f[1] - (f[0] - f[3])]
    solution = sp.linsolve(equations, list(f))
    forced = solution == {(f[2], f[3], f[2], f[3])}
    dark = L1 * u == sp.zeros(4, 1) and L2 * u == sp.zeros(4, 1)
    stationary = dissip(L1, rho) + dissip(L2, rho) == sp.zeros(4)
    # The same density is stationary for H = P1^- + P2^- as well.
    H = L1.T * L1 + L2.T * L2
    comm = H * rho - rho * H == sp.zeros(4)
    return bool(forced and dark and stationary and comm and sp.trace(rho) == 1)


check(
    "C1 alternating cycle",
    counterexample(),
    "connected, unique common dark vector, cyclic span of dimension 2, and (v v^T + w w^T)/2 stationary; "
    "a separating F is forced to identify opposite states",
)

print("time %.0f s" % (time.time() - T0), flush=True)
if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. On all %d flip components (d up to %d) of the nine open and periodic boxes, "
    "F2 separates with a nonzero constant plaquette displacement, the pair graph is connected, and the "
    "uniform vector is cyclic for the transposed jumps. For every positive rate vector and every Hermitian "
    "H killing that vector, the normalized RK projector is then the unique stationary state and a simple "
    "eigenvalue of the Lindbladian. The frozen single-parameter nullity-one controls on the open 2x2, 3x2, "
    "and 2x2x2 boxes reproduce (d = 2, 3, 9), including a Hamiltonian outside the plaquette projectors. "
    "The four-state alternating cycle is stationary and not cyclic. The general implication from a separating "
    "F to cyclicity is still open, and the frozen numerical transients were not rebuilt."
    % (total, max_d),
    flush=True,
)
print(
    "HIT: confirmed - the RK projector is the unique stationary state of this local cooling, for every "
    "positive rate vector and every Hermitian H that kills the uniform vector, on all %d flip components "
    "of the nine boxes"
    % total,
    flush=True,
)
