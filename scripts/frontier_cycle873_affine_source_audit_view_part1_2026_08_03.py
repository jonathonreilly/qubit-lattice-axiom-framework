#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 affine source, part 1/3."""

TARGET_SOURCE = "scripts/frontier_cycle873_uniform_affine_gauss_intertwiner_core_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 3
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 557
TOTAL_SOURCE_LINES = 1118
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "a1bc2159c5e2d5f59087860e3fe40bb1919cd4e476f6565a99c326d5af1c5ca9"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000001|#!/usr/bin/env python3
# C873SRC 000002|"""Cycle873 uniform Z17 affine-Gauss intertwiner core.
# C873SRC 000003|
# C873SRC 000004|This core works directly over finite-field incidence matrices and sparse state
# C873SRC 000005|dictionaries.  It proves that the trivial-character uniform affine fiber
# C873SRC 000006|intertwines every augmented FSWAP, checks a contractible loop and repeated L2
# C873SRC 000007|factors, and then tests the actual Cycle219 beta=-0.3 dense coin and decoded
# C873SRC 000008|free one-particle dispersion.  State preparation/enforcement and periodic
# C873SRC 000009|Wilson-sector selection are not supplied by this calculation.
# C873SRC 000010|"""
# C873SRC 000011|from __future__ import annotations
# C873SRC 000012|
# C873SRC 000013|from dataclasses import dataclass
# C873SRC 000014|from hashlib import sha256
# C873SRC 000015|from itertools import product
# C873SRC 000016|import argparse
# C873SRC 000017|import json
# C873SRC 000018|import math
# C873SRC 000019|from pathlib import Path
# C873SRC 000020|import subprocess
# C873SRC 000021|import sys
# C873SRC 000022|
# C873SRC 000023|import numpy as np
# C873SRC 000024|
# C873SRC 000025|
# C873SRC 000026|ROOT = Path(__file__).resolve().parents[1]
# C873SRC 000027|sys.path.insert(0, str(ROOT / "scripts"))
# C873SRC 000028|
# C873SRC 000029|import common_matter_field_coin_family_cycle219_2026_07_16 as C219
# C873SRC 000030|import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
# C873SRC 000031|
# C873SRC 000032|
# C873SRC 000033|P = 17
# C873SRC 000034|TOL = 3.0e-10
# C873SRC 000035|EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
# C873SRC 000036|OUT = ROOT / "outputs/cycle873_uniform_affine_gauss_intertwiner_core_receipt_2026_08_03.json"
# C873SRC 000037|SOURCE_PINS = {
# C873SRC 000038|    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
# C873SRC 000039|        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
# C873SRC 000040|    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
# C873SRC 000041|        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
# C873SRC 000042|    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
# C873SRC 000043|        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
# C873SRC 000044|    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py":
# C873SRC 000045|        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
# C873SRC 000046|}
# C873SRC 000047|
# C873SRC 000048|
# C873SRC 000049|def file_sha256(path: Path) -> str:
# C873SRC 000050|    return sha256(path.read_bytes()).hexdigest()
# C873SRC 000051|
# C873SRC 000052|
# C873SRC 000053|def rref_mod(matrix: np.ndarray, p: int = P):
# C873SRC 000054|    a = np.asarray(matrix, dtype=np.int64).copy() % p
# C873SRC 000055|    row = 0
# C873SRC 000056|    pivots: list[int] = []
# C873SRC 000057|    for col in range(a.shape[1]):
# C873SRC 000058|        pivot = next((r for r in range(row, a.shape[0]) if int(a[r, col]) % p), None)
# C873SRC 000059|        if pivot is None:
# C873SRC 000060|            continue
# C873SRC 000061|        a[[row, pivot]] = a[[pivot, row]]
# C873SRC 000062|        a[row] = (a[row] * pow(int(a[row, col]), -1, p)) % p
# C873SRC 000063|        for r in range(a.shape[0]):
# C873SRC 000064|            if r != row and a[r, col]:
# C873SRC 000065|                a[r] = (a[r] - int(a[r, col]) * a[row]) % p
# C873SRC 000066|        pivots.append(col)
# C873SRC 000067|        row += 1
# C873SRC 000068|        if row == a.shape[0]:
# C873SRC 000069|            break
# C873SRC 000070|    return a, pivots
# C873SRC 000071|
# C873SRC 000072|
# C873SRC 000073|def rank_mod(matrix: np.ndarray, p: int = P) -> int:
# C873SRC 000074|    return len(rref_mod(matrix, p)[1])
# C873SRC 000075|
# C873SRC 000076|
# C873SRC 000077|def nullspace_mod(matrix: np.ndarray, p: int = P) -> np.ndarray:
# C873SRC 000078|    a, pivots = rref_mod(matrix, p)
# C873SRC 000079|    free = [c for c in range(a.shape[1]) if c not in pivots]
# C873SRC 000080|    basis = []
# C873SRC 000081|    for f in free:
# C873SRC 000082|        x = np.zeros(a.shape[1], dtype=np.int64)
# C873SRC 000083|        x[f] = 1
# C873SRC 000084|        for r, pivot in enumerate(pivots):
# C873SRC 000085|            x[pivot] = (-a[r, f]) % p
# C873SRC 000086|        basis.append(x)
# C873SRC 000087|    return np.asarray(basis, dtype=np.int64).T if basis else np.zeros((a.shape[1], 0), dtype=np.int64)
# C873SRC 000088|
# C873SRC 000089|
# C873SRC 000090|def solve_mod(matrix: np.ndarray, rhs: np.ndarray, p: int = P) -> np.ndarray:
# C873SRC 000091|    a = np.asarray(matrix, dtype=np.int64) % p
# C873SRC 000092|    b = np.asarray(rhs, dtype=np.int64).reshape(-1, 1) % p
# C873SRC 000093|    aug, pivots = rref_mod(np.hstack((a, b)), p)
# C873SRC 000094|    n = a.shape[1]
# C873SRC 000095|    for row in aug:
# C873SRC 000096|        if not np.any(row[:n]) and row[n]:
# C873SRC 000097|            raise ValueError("inconsistent affine Gauss sector")
# C873SRC 000098|    x = np.zeros(n, dtype=np.int64)
# C873SRC 000099|    for r, pivot in enumerate(p for p in pivots if p < n):
# C873SRC 000100|        x[pivot] = aug[r, n]
# C873SRC 000101|    assert np.array_equal((a @ x) % p, b[:, 0])
# C873SRC 000102|    return x
# C873SRC 000103|
# C873SRC 000104|
# C873SRC 000105|def independent_columns(matrix: np.ndarray, p: int = P) -> list[int]:
# C873SRC 000106|    chosen: list[int] = []
# C873SRC 000107|    old_rank = 0
# C873SRC 000108|    for col in range(matrix.shape[1]):
# C873SRC 000109|        trial = chosen + [col]
# C873SRC 000110|        new_rank = rank_mod(matrix[:, trial], p)
# C873SRC 000111|        if new_rank > old_rank:
# C873SRC 000112|            chosen.append(col)
# C873SRC 000113|            old_rank = new_rank
# C873SRC 000114|    return chosen
# C873SRC 000115|
# C873SRC 000116|
# C873SRC 000117|@dataclass(frozen=True)
# C873SRC 000118|class CubicComplex:
# C873SRC 000119|    name: str
# C873SRC 000120|    dims: tuple[int, int, int]
# C873SRC 000121|    vertices: tuple[tuple[int, int, int], ...]
# C873SRC 000122|    edges: tuple[tuple[int, int, int], ...]  # tail index, head index, axis
# C873SRC 000123|    face_labels: tuple[tuple[tuple[int, int, int], int, int], ...]
# C873SRC 000124|    incidence: np.ndarray
# C873SRC 000125|    faces: np.ndarray  # edge x face oriented-boundary matrix
# C873SRC 000126|
# C873SRC 000127|
# C873SRC 000128|@dataclass(frozen=True)
# C873SRC 000129|class FixedStarBackground:
# C873SRC 000130|    """A supplied affine-star background for one fixed-number matter sector.
# C873SRC 000131|
# C873SRC 000132|    The admitted fiber obeys incidence*ell = alpha*n + field (mod 17).
# C873SRC 000133|    Solvability therefore requires sum(field) = -alpha*particle_number.
# C873SRC 000134|    The field is input structure; this core neither selects nor prepares it.
# C873SRC 000135|    """
# C873SRC 000136|
# C873SRC 000137|    label: str
# C873SRC 000138|    alpha: int
# C873SRC 000139|    particle_number: int
# C873SRC 000140|    field: tuple[int, ...]
# C873SRC 000141|
# C873SRC 000142|
# C873SRC 000143|def open_box(name: str, dims: tuple[int, int, int]) -> CubicComplex:
# C873SRC 000144|    vertices = tuple(product(*(range(length) for length in dims)))
# C873SRC 000145|    vid = {vertex: index for index, vertex in enumerate(vertices)}
# C873SRC 000146|    edges = []
# C873SRC 000147|    edge_index = {}
# C873SRC 000148|    for vertex in vertices:
# C873SRC 000149|        for axis in range(3):
# C873SRC 000150|            if vertex[axis] + 1 >= dims[axis]:
# C873SRC 000151|                continue
# C873SRC 000152|            target = list(vertex)
# C873SRC 000153|            target[axis] += 1
# C873SRC 000154|            target_t = tuple(target)
# C873SRC 000155|            edge_index[(vertex, target_t)] = len(edges)
# C873SRC 000156|            edges.append((vid[vertex], vid[target_t], axis))
# C873SRC 000157|    incidence = np.zeros((len(vertices), len(edges)), dtype=np.int64)
# C873SRC 000158|    for edge, (tail, head, _axis) in enumerate(edges):
# C873SRC 000159|        incidence[tail, edge] = -1
# C873SRC 000160|        incidence[head, edge] = +1
# C873SRC 000161|
# C873SRC 000162|    face_vectors = []
# C873SRC 000163|    face_labels = []
# C873SRC 000164|    for a in range(3):
# C873SRC 000165|        for b in range(a + 1, 3):
# C873SRC 000166|            for base in vertices:
# C873SRC 000167|                if base[a] + 1 >= dims[a] or base[b] + 1 >= dims[b]:
# C873SRC 000168|                    continue
# C873SRC 000169|                ea = [0, 0, 0]
# C873SRC 000170|                eb = [0, 0, 0]
# C873SRC 000171|                ea[a] = 1
# C873SRC 000172|                eb[b] = 1
# C873SRC 000173|                va = tuple(base[i] + ea[i] for i in range(3))
# C873SRC 000174|                vb = tuple(base[i] + eb[i] for i in range(3))
# C873SRC 000175|                vab = tuple(base[i] + ea[i] + eb[i] for i in range(3))
# C873SRC 000176|                vector = np.zeros(len(edges), dtype=np.int64)
# C873SRC 000177|                vector[edge_index[(base, va)]] += 1
# C873SRC 000178|                vector[edge_index[(va, vab)]] += 1
# C873SRC 000179|                vector[edge_index[(vb, vab)]] -= 1
# C873SRC 000180|                vector[edge_index[(base, vb)]] -= 1
# C873SRC 000181|                face_vectors.append(vector % P)
# C873SRC 000182|                face_labels.append((base, a, b))
# C873SRC 000183|    faces = (
# C873SRC 000184|        np.asarray(face_vectors, dtype=np.int64).T % P
# C873SRC 000185|        if face_vectors
# C873SRC 000186|        else np.zeros((len(edges), 0), dtype=np.int64)
# C873SRC 000187|    )
# C873SRC 000188|    return CubicComplex(
# C873SRC 000189|        name, dims, vertices, tuple(edges), tuple(face_labels), incidence % P, faces
# C873SRC 000190|    )
# C873SRC 000191|
# C873SRC 000192|
# C873SRC 000193|def bits_array(bits: int, count: int) -> np.ndarray:
# C873SRC 000194|    return np.asarray([(bits >> index) & 1 for index in range(count)], dtype=np.int64)
# C873SRC 000195|
# C873SRC 000196|
# C873SRC 000197|def supplied_star_background(
# C873SRC 000198|    graph: CubicComplex,
# C873SRC 000199|    particle_number: int,
# C873SRC 000200|    *,
# C873SRC 000201|    alpha: int = 1,
# C873SRC 000202|    convention: str = "ordered_prefix",
# C873SRC 000203|) -> FixedStarBackground:
# C873SRC 000204|    """Construct one explicit diagnostic input field, never a selected vacuum."""
# C873SRC 000205|
# C873SRC 000206|    if not 0 <= particle_number <= len(graph.vertices):
# C873SRC 000207|        raise ValueError("particle number outside graph")
# C873SRC 000208|    field = np.zeros(len(graph.vertices), dtype=np.int64)
# C873SRC 000209|    if convention == "ordered_prefix":
# C873SRC 000210|        field[:particle_number] = -alpha
# C873SRC 000211|    elif convention == "first_anchor":
# C873SRC 000212|        field[0] = -alpha * particle_number
# C873SRC 000213|    elif convention == "last_anchor":
# C873SRC 000214|        field[-1] = -alpha * particle_number
# C873SRC 000215|    else:
# C873SRC 000216|        raise ValueError(f"unknown background convention: {convention}")
# C873SRC 000217|    field %= P
# C873SRC 000218|    assert int(field.sum()) % P == (-alpha * particle_number) % P
# C873SRC 000219|    return FixedStarBackground(
# C873SRC 000220|        convention,
# C873SRC 000221|        alpha % P,
# C873SRC 000222|        particle_number,
# C873SRC 000223|        tuple(int(value) for value in field),
# C873SRC 000224|    )
# C873SRC 000225|
# C873SRC 000226|
# C873SRC 000227|def background_variants(
# C873SRC 000228|    graph: CubicComplex, particle_number: int, *, alpha: int = 1
# C873SRC 000229|) -> tuple[FixedStarBackground, ...]:
# C873SRC 000230|    return tuple(
# C873SRC 000231|        supplied_star_background(
# C873SRC 000232|            graph, particle_number, alpha=alpha, convention=convention
# C873SRC 000233|        )
# C873SRC 000234|        for convention in ("ordered_prefix", "first_anchor", "last_anchor")
# C873SRC 000235|    )
# C873SRC 000236|
# C873SRC 000237|
# C873SRC 000238|def matter_charge(
# C873SRC 000239|    graph: CubicComplex, bits: int, background: FixedStarBackground
# C873SRC 000240|) -> np.ndarray:
# C873SRC 000241|    """Return q_g(n)=alpha*n+g for an explicitly supplied fixed background."""
# C873SRC 000242|
# C873SRC 000243|    n = bits_array(bits, len(graph.vertices))
# C873SRC 000244|    if int(n.sum()) != background.particle_number:
# C873SRC 000245|        raise ValueError("matter word leaves the supplied fixed-number sector")
# C873SRC 000246|    if len(background.field) != len(graph.vertices):
# C873SRC 000247|        raise ValueError("background support does not match graph")
# C873SRC 000248|    q = (background.alpha * n + np.asarray(background.field, dtype=np.int64)) % P
# C873SRC 000249|    assert int(q.sum()) % P == 0
# C873SRC 000250|    return q
# C873SRC 000251|
# C873SRC 000252|
# C873SRC 000253|def swap_bits(bits: int, u: int, v: int):
# C873SRC 000254|    nu, nv = (bits >> u) & 1, (bits >> v) & 1
# C873SRC 000255|    out = bits
# C873SRC 000256|    if nu != nv:
# C873SRC 000257|        out ^= (1 << u) | (1 << v)
# C873SRC 000258|    phase = -1 if nu == nv == 1 else 1
# C873SRC 000259|    return out, phase, nu, nv
# C873SRC 000260|
# C873SRC 000261|
# C873SRC 000262|def state_residual(left: dict, right: dict) -> float:
# C873SRC 000263|    return math.sqrt(
# C873SRC 000264|        sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in set(left) | set(right))
# C873SRC 000265|    )
# C873SRC 000266|
# C873SRC 000267|
# C873SRC 000268|def state_overlap(left: dict, right: dict) -> complex:
# C873SRC 000269|    return sum(np.conj(value) * right.get(key, 0.0j) for key, value in left.items())
# C873SRC 000270|
# C873SRC 000271|
# C873SRC 000272|def affine_state(
# C873SRC 000273|    graph: CubicComplex,
# C873SRC 000274|    bits: int,
# C873SRC 000275|    generators: np.ndarray,
# C873SRC 000276|    background: FixedStarBackground,
# C873SRC 000277|    character: tuple[int, ...] | None = None,
# C873SRC 000278|) -> dict:
# C873SRC 000279|    q = matter_charge(graph, bits, background)
# C873SRC 000280|    base = solve_mod(graph.incidence, q)
# C873SRC 000281|    beta = generators.shape[1]
# C873SRC 000282|    character = (0,) * beta if character is None else character
# C873SRC 000283|    assert len(character) == beta
# C873SRC 000284|    size = P ** beta
# C873SRC 000285|    amplitude = 1.0 / math.sqrt(size)
# C873SRC 000286|    omega = np.exp(2j * math.pi / P)
# C873SRC 000287|    output = {}
# C873SRC 000288|    for coeff in product(range(P), repeat=beta):
# C873SRC 000289|        link = (base + generators @ np.asarray(coeff, dtype=np.int64)) % P
# C873SRC 000290|        phase_power = sum(a * b for a, b in zip(character, coeff)) % P
# C873SRC 000291|        output[(bits, tuple(int(v) for v in link))] = amplitude * omega ** phase_power
# C873SRC 000292|    assert abs(sum(abs(v) ** 2 for v in output.values()) - 1.0) < 1e-12
# C873SRC 000293|    return output
# C873SRC 000294|
# C873SRC 000295|
# C873SRC 000296|def augmented_fswap_state(
# C873SRC 000297|    graph: CubicComplex,
# C873SRC 000298|    state: dict,
# C873SRC 000299|    edge_index: int,
# C873SRC 000300|    current_alpha: int = 1,
# C873SRC 000301|) -> dict:
# C873SRC 000302|    u, v, _axis = graph.edges[edge_index]
# C873SRC 000303|    output = {}
# C873SRC 000304|    for (bits, link_tuple), amplitude in state.items():
# C873SRC 000305|        new_bits, phase, nu, nv = swap_bits(bits, u, v)
# C873SRC 000306|        link = np.asarray(link_tuple, dtype=np.int64)
# C873SRC 000307|        link[edge_index] = (link[edge_index] + current_alpha * (nu - nv)) % P
# C873SRC 000308|        key = (new_bits, tuple(int(x) for x in link))
# C873SRC 000309|        output[key] = output.get(key, 0.0j) + phase * amplitude
# C873SRC 000310|    return output
# C873SRC 000311|
# C873SRC 000312|
# C873SRC 000313|def expected_fswap_state(
# C873SRC 000314|    graph, bits, generators, background, edge_index, character=None
# C873SRC 000315|):
# C873SRC 000316|    u, v, _axis = graph.edges[edge_index]
# C873SRC 000317|    new_bits, phase, _nu, _nv = swap_bits(bits, u, v)
# C873SRC 000318|    return {
# C873SRC 000319|        key: phase * value
# C873SRC 000320|        for key, value in affine_state(
# C873SRC 000321|            graph, new_bits, generators, background, character
# C873SRC 000322|        ).items()
# C873SRC 000323|    }
# C873SRC 000324|
# C873SRC 000325|
# C873SRC 000326|def apply_sequence(graph, state, sequence, current_alpha=1):
# C873SRC 000327|    for edge in sequence:
# C873SRC 000328|        state = augmented_fswap_state(graph, state, edge, current_alpha)
# C873SRC 000329|    return state
# C873SRC 000330|
# C873SRC 000331|
# C873SRC 000332|def expected_sequence(
# C873SRC 000333|    graph, bits, generators, background, sequence, character=None
# C873SRC 000334|):
# C873SRC 000335|    phase = 1
# C873SRC 000336|    current = bits
# C873SRC 000337|    for edge in sequence:
# C873SRC 000338|        u, v, _axis = graph.edges[edge]
# C873SRC 000339|        current, step_phase, _nu, _nv = swap_bits(current, u, v)
# C873SRC 000340|        phase *= step_phase
# C873SRC 000341|    return {
# C873SRC 000342|        key: phase * value
# C873SRC 000343|        for key, value in affine_state(
# C873SRC 000344|            graph, current, generators, background, character
# C873SRC 000345|        ).items()
# C873SRC 000346|    }, current, phase
# C873SRC 000347|
# C873SRC 000348|
# C873SRC 000349|def enumerate_affine_sector(graph: CubicComplex, generators: np.ndarray, chunk=100_000) -> int:
# C873SRC 000350|    """Exhaust every coefficient word, checking the Gauss equation in batches."""
# C873SRC 000351|    beta = generators.shape[1]
# C873SRC 000352|    total = P ** beta
# C873SRC 000353|    q = np.zeros(len(graph.vertices), dtype=np.int64)
# C873SRC 000354|    base = solve_mod(graph.incidence, q)
# C873SRC 000355|    checked = 0
# C873SRC 000356|    powers = np.asarray([P ** i for i in range(beta)], dtype=np.int64)
# C873SRC 000357|    for start in range(0, total, chunk):
# C873SRC 000358|        stop = min(total, start + chunk)
# C873SRC 000359|        words = np.arange(start, stop, dtype=np.int64)
# C873SRC 000360|        coeff = ((words[None, :] // powers[:, None]) % P).astype(np.int64)
# C873SRC 000361|        links = (base[:, None] + generators @ coeff) % P
# C873SRC 000362|        assert np.count_nonzero((graph.incidence @ links) % P) == 0
# C873SRC 000363|        checked += stop - start
# C873SRC 000364|    assert checked == total and rank_mod(generators) == beta
# C873SRC 000365|    return checked
# C873SRC 000366|
# C873SRC 000367|
# C873SRC 000368|def graph_certificate(graph: CubicComplex) -> dict:
# C873SRC 000369|    b_rank = rank_mod(graph.incidence)
# C873SRC 000370|    kernel = nullspace_mod(graph.incidence)
# C873SRC 000371|    beta = kernel.shape[1]
# C873SRC 000372|    f_rank = rank_mod(graph.faces)
# C873SRC 000373|    face_basis_indices = independent_columns(graph.faces)
# C873SRC 000374|    face_basis = graph.faces[:, face_basis_indices]
# C873SRC 000375|    assert b_rank == len(graph.vertices) - 1
# C873SRC 000376|    assert np.count_nonzero((graph.incidence @ graph.faces) % P) == 0
# C873SRC 000377|    assert f_rank == beta
# C873SRC 000378|    assert rank_mod(face_basis) == beta
# C873SRC 000379|    sector_size = P ** beta
# C873SRC 000380|    enumerated = enumerate_affine_sector(graph, face_basis)
# C873SRC 000381|    face_relations = nullspace_mod(graph.faces)
# C873SRC 000382|
# C873SRC 000383|    return {
# C873SRC 000384|        "vertices": len(graph.vertices),
# C873SRC 000385|        "edges": len(graph.edges),
# C873SRC 000386|        "faces": graph.faces.shape[1],
# C873SRC 000387|        "incidence_rank": b_rank,
# C873SRC 000388|        "kernel_dimension": beta,
# C873SRC 000389|        "affine_sector_size": sector_size,
# C873SRC 000390|        "enumerated_affine_points": enumerated,
# C873SRC 000391|        "plaquette_boundary_rank": f_rank,
# C873SRC 000392|        "uniform_invariant_subspace_dimension": P ** (beta - f_rank),
# C873SRC 000393|        "edge_order": [
# C873SRC 000394|            {"tail": list(graph.vertices[u]), "head": list(graph.vertices[v]), "axis": axis}
# C873SRC 000395|            for u, v, axis in graph.edges
# C873SRC 000396|        ],
# C873SRC 000397|        "face_labels": [
# C873SRC 000398|            {"base": list(base), "axes": [a, b]} for base, a, b in graph.face_labels
# C873SRC 000399|        ],
# C873SRC 000400|        "face_vectors_mod17": graph.faces.T.tolist(),
# C873SRC 000401|        "independent_face_indices": face_basis_indices,
# C873SRC 000402|        "independent_face_vectors_mod17": face_basis.T.tolist(),
# C873SRC 000403|        "face_relation_basis_mod17": face_relations.T.tolist(),
# C873SRC 000404|    }
# C873SRC 000405|
# C873SRC 000406|
# C873SRC 000407|plaquette = open_box("filled_plaquette", (2, 2, 1))
# C873SRC 000408|cube_l2 = open_box("open_cube_L2", (2, 2, 2))
# C873SRC 000409|plaquette_cert = graph_certificate(plaquette)
# C873SRC 000410|cube_cert = graph_certificate(cube_l2)
# C873SRC 000411|
# C873SRC 000412|plaquette_basis = plaquette.faces[:, plaquette_cert["independent_face_indices"]]
# C873SRC 000413|cube_basis = cube_l2.faces[:, cube_cert["independent_face_indices"]]
# C873SRC 000414|
# C873SRC 000415|# Direct sparse matrix-column checks on the filled plaquette: all matter basis
# C873SRC 000416|# words and all seams.  This includes the |11> FSWAP minus sign.
# C873SRC 000417|direct_residuals = []
# C873SRC 000418|background_variant_residuals = []
# C873SRC 000419|background_variant_cases = 0
# C873SRC 000420|wrong_sign_residuals = []
# C873SRC 000421|wrong_alpha_active_residuals = {alpha: [] for alpha in range(P) if alpha != 1}
# C873SRC 000422|for bits in range(1 << len(plaquette.vertices)):
# C873SRC 000423|    particle_number = int(bits.bit_count())
# C873SRC 000424|    backgrounds = background_variants(plaquette, particle_number)
# C873SRC 000425|    for edge in range(len(plaquette.edges)):
# C873SRC 000426|        background = backgrounds[0]
# C873SRC 000427|        encoded = affine_state(plaquette, bits, plaquette_basis, background)
# C873SRC 000428|        observed = augmented_fswap_state(plaquette, encoded, edge, +1)
# C873SRC 000429|        expected = expected_fswap_state(
# C873SRC 000430|            plaquette, bits, plaquette_basis, background, edge
# C873SRC 000431|        )
# C873SRC 000432|        direct_residuals.append(state_residual(observed, expected))
# C873SRC 000433|        for supplied_background in backgrounds:
# C873SRC 000434|            variant_encoded = affine_state(
# C873SRC 000435|                plaquette, bits, plaquette_basis, supplied_background
# C873SRC 000436|            )
# C873SRC 000437|            variant_observed = augmented_fswap_state(
# C873SRC 000438|                plaquette, variant_encoded, edge, +1
# C873SRC 000439|            )
# C873SRC 000440|            variant_expected = expected_fswap_state(
# C873SRC 000441|                plaquette, bits, plaquette_basis, supplied_background, edge
# C873SRC 000442|            )
# C873SRC 000443|            background_variant_residuals.append(
# C873SRC 000444|                state_residual(variant_observed, variant_expected)
# C873SRC 000445|            )
# C873SRC 000446|            background_variant_cases += 1
# C873SRC 000447|        wrong = augmented_fswap_state(plaquette, encoded, edge, -1)
# C873SRC 000448|        wrong_sign_residuals.append(state_residual(wrong, expected))
# C873SRC 000449|        u, v, _axis = plaquette.edges[edge]
# C873SRC 000450|        _new_bits, _phase, nu, nv = swap_bits(bits, u, v)
# C873SRC 000451|        if nu != nv:
# C873SRC 000452|            for wrong_alpha in wrong_alpha_active_residuals:
# C873SRC 000453|                wrong = augmented_fswap_state(
# C873SRC 000454|                    plaquette, encoded, edge, wrong_alpha
# C873SRC 000455|                )
# C873SRC 000456|                wrong_alpha_active_residuals[wrong_alpha].append(
# C873SRC 000457|                    state_residual(wrong, expected)
# C873SRC 000458|                )
# C873SRC 000459|assert max(direct_residuals) == 0.0
# C873SRC 000460|assert max(background_variant_residuals) == 0.0
# C873SRC 000461|assert all(
# C873SRC 000462|    all(abs(value - math.sqrt(2)) < 1e-12 for value in residuals)
# C873SRC 000463|    for residuals in wrong_alpha_active_residuals.values()
# C873SRC 000464|)
# C873SRC 000465|
# C873SRC 000466|# The oriented loop is bottom, right, reverse-top, reverse-left in the fixed
# C873SRC 000467|# positive-axis edge orientation.  A single particle returns to its matter
# C873SRC 000468|# basis word while the accumulated link current is the plaquette boundary.
# C873SRC 000469|edge_lookup_plaq = {
# C873SRC 000470|    (plaquette.vertices[u], plaquette.vertices[v]): edge
# C873SRC 000471|    for edge, (u, v, _axis) in enumerate(plaquette.edges)
# C873SRC 000472|}
# C873SRC 000473|v00, v10, v01, v11 = (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)
# C873SRC 000474|loop_sequence = (
# C873SRC 000475|    edge_lookup_plaq[(v00, v10)],
# C873SRC 000476|    edge_lookup_plaq[(v10, v11)],
# C873SRC 000477|    edge_lookup_plaq[(v01, v11)],
# C873SRC 000478|    edge_lookup_plaq[(v00, v01)],
# C873SRC 000479|)
# C873SRC 000480|sequence_residuals = []
# C873SRC 000481|for bits in range(1 << len(plaquette.vertices)):
# C873SRC 000482|    background = supplied_star_background(plaquette, bits.bit_count())
# C873SRC 000483|    observed = apply_sequence(
# C873SRC 000484|        plaquette,
# C873SRC 000485|        affine_state(plaquette, bits, plaquette_basis, background),
# C873SRC 000486|        loop_sequence,
# C873SRC 000487|    )
# C873SRC 000488|    expected, _final_bits, _phase = expected_sequence(
# C873SRC 000489|        plaquette, bits, plaquette_basis, background, loop_sequence
# C873SRC 000490|    )
# C873SRC 000491|    sequence_residuals.append(state_residual(observed, expected))
# C873SRC 000492|assert max(sequence_residuals) == 0.0
# C873SRC 000493|
# C873SRC 000494|single_particle = 1 << plaquette.vertices.index(v00)
# C873SRC 000495|single_background = supplied_star_background(plaquette, 1)
# C873SRC 000496|expected_uniform, final_single_particle, _ = expected_sequence(
# C873SRC 000497|    plaquette, single_particle, plaquette_basis, single_background, loop_sequence
# C873SRC 000498|)
# C873SRC 000499|assert final_single_particle == single_particle
# C873SRC 000500|uniform_loop = apply_sequence(
# C873SRC 000501|    plaquette,
# C873SRC 000502|    affine_state(plaquette, single_particle, plaquette_basis, single_background),
# C873SRC 000503|    loop_sequence,
# C873SRC 000504|)
# C873SRC 000505|uniform_loop_overlap = state_overlap(expected_uniform, uniform_loop)
# C873SRC 000506|
# C873SRC 000507|basis_generators = np.zeros((len(plaquette.edges), 0), dtype=np.int64)
# C873SRC 000508|basis_loop = apply_sequence(
# C873SRC 000509|    plaquette,
# C873SRC 000510|    affine_state(plaquette, single_particle, basis_generators, single_background),
# C873SRC 000511|    loop_sequence,
# C873SRC 000512|)
# C873SRC 000513|basis_expected, _, _ = expected_sequence(
# C873SRC 000514|    plaquette, single_particle, basis_generators, single_background, loop_sequence
# C873SRC 000515|)
# C873SRC 000516|basis_overlap = state_overlap(basis_expected, basis_loop)
# C873SRC 000517|basis_residual = state_residual(basis_loop, basis_expected)
# C873SRC 000518|
# C873SRC 000519|character = (1,)
# C873SRC 000520|character_loop = apply_sequence(
# C873SRC 000521|    plaquette,
# C873SRC 000522|    affine_state(
# C873SRC 000523|        plaquette, single_particle, plaquette_basis, single_background, character
# C873SRC 000524|    ),
# C873SRC 000525|    loop_sequence,
# C873SRC 000526|)
# C873SRC 000527|character_expected, _, _ = expected_sequence(
# C873SRC 000528|    plaquette,
# C873SRC 000529|    single_particle,
# C873SRC 000530|    plaquette_basis,
# C873SRC 000531|    single_background,
# C873SRC 000532|    loop_sequence,
# C873SRC 000533|    character,
# C873SRC 000534|)
# C873SRC 000535|character_overlap = state_overlap(character_expected, character_loop)
# C873SRC 000536|character_residual = state_residual(character_loop, character_expected)
# C873SRC 000537|assert abs(abs(character_overlap) - 1.0) < 1e-12
# C873SRC 000538|assert character_residual > 0.3
# C873SRC 000539|
# C873SRC 000540|# Exhaust the incidence-current condition on every L2 occupation word and
# C873SRC 000541|# seam.  Then repeat the complete seam list three times to test induction.
# C873SRC 000542|direct_l2_cases = 0
# C873SRC 000543|direct_l2_incidence_failures = 0
# C873SRC 000544|wrong_sign_nontrivial = 0
# C873SRC 000545|wrong_alpha_l2_cases = 0
# C873SRC 000546|for bits in range(1 << len(cube_l2.vertices)):
# C873SRC 000547|    background = supplied_star_background(cube_l2, bits.bit_count())
# C873SRC 000548|    q0 = matter_charge(cube_l2, bits, background)
# C873SRC 000549|    for edge, (u, v, _axis) in enumerate(cube_l2.edges):
# C873SRC 000550|        new_bits, _phase, nu, nv = swap_bits(bits, u, v)
# C873SRC 000551|        q1 = matter_charge(cube_l2, new_bits, background)
# C873SRC 000552|        current = np.zeros(len(cube_l2.edges), dtype=np.int64)
# C873SRC 000553|        current[edge] = nu - nv
# C873SRC 000554|        direct_l2_incidence_failures += not np.array_equal(
# C873SRC 000555|            (cube_l2.incidence @ current) % P, (q1 - q0) % P
# C873SRC 000556|        )
# C873SRC 000557|        direct_l2_cases += 1
