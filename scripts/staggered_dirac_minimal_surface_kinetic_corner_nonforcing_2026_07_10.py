#!/usr/bin/env python3
"""Finite certificates for the minimal-surface kinetic/corner no-go.

The theorem note gives an infinite-Z^3 quasi-local countermodel.  This runner
checks its finite local restrictions and the sharper finite-lattice
discriminators without importing the staggered kinetic law as a premise:

* one explicit current-A_min Admissibility/Record reduct, including the
  degenerate all-possibilities branch and a nonempty permanent record history;
* a basis-independent qubit-exchange Hamiltonian whose one-excitation
  restriction is the cubic graph Laplacian;
* translation/proper-cubic invariance and the graph-Laplacian Fourier symbol,
  whose zero set contains one point rather than the eight staggered corners;
* the plus/minus plaquette-flux split and PBC versus (-,-,-) holonomy for the
  Kawamoto-Smit comparator.

The finite checks are a certificate for formulas used in the analytic proof;
they are not substituted for the proof on infinite Z^3.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AXIOM_NOTE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
L = 4
NS = L**3
TOL = 1.0e-9

_passed = 0
_failed = 0


def check(section: str, number: int, description: str, condition: bool, detail: str = "") -> bool:
    global _passed, _failed
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    if ok:
        _passed += 1
    else:
        _failed += 1
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] ({section}{number:02d}) {description}{suffix}")
    return ok


def kron_at(op: np.ndarray, site: int, nsites: int) -> np.ndarray:
    factors = [np.eye(2, dtype=complex) for _ in range(nsites)]
    factors[site] = op
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def idx(x: tuple[int, int, int]) -> int:
    return (x[0] % L) + L * ((x[1] % L) + L * (x[2] % L))


def sites():
    for x3 in range(L):
        for x2 in range(L):
            for x1 in range(L):
                yield (x1, x2, x3)


E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((x[i] + y[i]) % L for i in range(3))


def shift(mu: int) -> np.ndarray:
    matrix = np.zeros((NS, NS), dtype=float)
    for x in sites():
        matrix[idx(add(x, E[mu])), idx(x)] = 1.0
    return matrix


def permutation_operator(mapping) -> np.ndarray:
    matrix = np.zeros((NS, NS), dtype=float)
    for x in sites():
        matrix[idx(mapping(x)), idx(x)] = 1.0
    return matrix


def eta_plus(_x: tuple[int, int, int], _mu: int) -> int:
    return 1


def eta_ks(x: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0] % 2)
    return (-1) ** ((x[0] + x[1]) % 2)


def plaquette_fluxes(eta) -> set[int]:
    values: set[int] = set()
    for x in sites():
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xmu = add(x, E[mu])
                xnu = add(x, E[nu])
                values.add(
                    int(eta(x, mu) * eta(xmu, nu) * eta(xnu, mu) * eta(x, nu))
                )
    return values


def build_staggered(eta, holonomy: tuple[int, int, int]) -> np.ndarray:
    matrix = np.zeros((NS, NS), dtype=float)
    for x in sites():
        for mu, e in enumerate(E):
            xp = add(x, e)
            xm = tuple((x[i] - e[i]) % L for i in range(3))
            forward_wrap = holonomy[mu] if x[mu] == L - 1 else 1
            backward_wrap = holonomy[mu] if x[mu] == 0 else 1
            matrix[idx(x), idx(xp)] += 0.5 * eta(x, mu) * forward_wrap
            matrix[idx(x), idx(xm)] -= 0.5 * eta(x, mu) * backward_wrap
    return matrix


def corner_vector(bits: tuple[int, int, int]) -> np.ndarray:
    vector = np.array(
        [(-1.0) ** sum(bits[mu] * x[mu] for mu in range(3)) for x in sites()],
        dtype=float,
    )
    return vector / np.linalg.norm(vector)


print("=" * 78)
print("Minimal-surface staggered kinetic/corner non-forcing certificate")
print("=" * 78)


# ---------------------------------------------------------------------------
print("\n--- [S] current-A_min source guards")
axiom_text = AXIOM_NOTE.read_text(encoding="utf-8")
axiom_flat = " ".join(axiom_text.split())
source_checks = [
    check("S", 1, "Qubit supplies one-site M_2(C)", "M_2(C)" in axiom_text),
    check("S", 2, "Lattice supplies the cubic lattice Z^3", "Z^3" in axiom_text),
    check(
        "S",
        3,
        "Admissibility does not choose a Hamiltonian or transfer operator",
        "does not choose a Hamiltonian or transfer operator" in axiom_flat,
    ),
    check(
        "S",
        4,
        "the staggered-Dirac/finite-Grassmann realization is outside axiom content",
        "the staggered-Dirac/finite-Grassmann realization" in axiom_text,
    ),
    check(
        "S",
        5,
        "A_min includes one fixed nearest-neighbor Admissibility rule",
        "There is one fixed nearest-neighbor admissibility rule" in axiom_flat,
    ),
    check("S", 6, "A_min explicitly says records form", "Records form." in axiom_text),
]


# ---------------------------------------------------------------------------
print("\n--- [R] explicit shared Admissibility/Record reduct")
p0 = np.array([[1, 0], [0, 0]], dtype=complex)
p1 = np.array([[0, 0], [0, 1]], dtype=complex)
zero2 = np.zeros((2, 2), dtype=complex)
hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2.0)


def top_eigenspace_support(neighbor_projectors: list[np.ndarray]) -> np.ndarray:
    """Projector onto the full largest-eigenvalue eigenspace.

    If the neighbor sum is scalar, this returns I, representing that every
    rank-one projector is available.  No arbitrary eigenvector is selected.
    """
    neighbor_sum = sum(neighbor_projectors, zero2.copy())
    values, vectors = np.linalg.eigh(neighbor_sum)
    mask = np.abs(values - np.max(values)) < TOL
    top_vectors = vectors[:, mask]
    return top_vectors @ top_vectors.conj().T


mixed_neighbors = [p0, p1, p0, p0, p1, p0]
mixed_support = top_eigenspace_support(mixed_neighbors)
admissibility_varies = np.allclose(top_eigenspace_support([p0] * 6), p0) and np.allclose(
    top_eigenspace_support([p1] * 6), p1
)
neighbor_order_blind = all(
    np.allclose(top_eigenspace_support(order), mixed_support)
    for order in (
        mixed_neighbors,
        list(reversed(mixed_neighbors)),
        mixed_neighbors[2:] + mixed_neighbors[:2],
    )
)
r1 = check(
    "R",
    1,
    "fixed rule varies with neighbor conditions and is neighbor-order blind",
    admissibility_varies and neighbor_order_blind,
)

balanced_neighbors = [p0, p1, p0, p1, p0, p1]
frame_covariant = True
for neighbors in (mixed_neighbors, balanced_neighbors):
    support = top_eigenspace_support(neighbors)
    rotated_neighbors = [hadamard @ p @ hadamard.conj().T for p in neighbors]
    frame_covariant &= np.allclose(
        top_eigenspace_support(rotated_neighbors), hadamard @ support @ hadamard.conj().T
    )
r2 = check(
    "R",
    2,
    "availability support is frame covariant in nondegenerate and scalar-tie cases",
    frame_covariant,
)

tie_support = top_eigenspace_support(balanced_neighbors)
r3 = check(
    "R",
    3,
    "scalar neighbor sum returns the full possibility space, not a preferred projector",
    np.allclose(tie_support, np.eye(2)) and int(round(np.trace(tie_support).real)) == 2,
)


def infinite_neighbors(site: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    result = []
    for e in E:
        result.append(tuple(site[k] + e[k] for k in range(3)))
        result.append(tuple(site[k] - e[k] for k in range(3)))
    return result


def available_support(records: dict[tuple[int, int, int], np.ndarray], site) -> np.ndarray:
    return top_eigenspace_support([records.get(y, zero2) for y in infinite_neighbors(site)])


def can_lock(records: dict[tuple[int, int, int], np.ndarray], site, projector) -> bool:
    support = available_support(records, site)
    return site not in records and np.allclose(support @ projector, projector)


origin = (0, 0, 0)
far = (2, 0, 0)
middle = (1, 0, 0)
p_plus = hadamard @ p0 @ hadamard.conj().T
history: list[dict[tuple[int, int, int], np.ndarray]] = [{}]
formation_ok = can_lock(history[-1], origin, p0)
history.append({origin: p0})
formation_ok &= can_lock(history[-1], far, p1)
history.append({origin: p0, far: p1})
formation_ok &= can_lock(history[-1], middle, p_plus)
history.append({origin: p0, far: p1, middle: p_plus})

permanent = all(
    set(history[t]).issubset(history[t + 1])
    and all(np.allclose(history[t][x], history[t + 1][x]) for x in history[t])
    for t in range(len(history) - 1)
)
one_per_site = all(len(state) == len(set(state)) for state in history)
projector_content = all(
    np.allclose(p @ p, p) and abs(np.trace(p).real - 1.0) < TOL
    for state in history
    for p in state.values()
)
r4 = check(
    "R",
    4,
    "nonempty history realizes admissible formation, one record per site, and permanence",
    formation_ok and len(history[1]) > 0 and permanent and one_per_site and projector_content,
    f"record counts = {[len(state) for state in history]}",
)


def record_readout(records: dict[tuple[int, int, int], np.ndarray]) -> float:
    return float(sum(np.trace(projector).real for projector in records.values()))


left = {origin: p0, far: p1}
right = {middle: p_plus}
r5 = check(
    "R",
    5,
    "record readout is content-determined, empty-normalized, and additive on disjoint sites",
    set(left).isdisjoint(right)
    and record_readout({**left, **right}) == record_readout(left) + record_readout(right)
    and record_readout({}) == 0.0,
)


# ---------------------------------------------------------------------------
print("\n--- [M] non-staggered local qubit-exchange completion")
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
creator = (sx - 1j * sy) / 2.0

cube_sites = list(itertools.product((0, 1), repeat=3))
cube_index = {x: i for i, x in enumerate(cube_sites)}
cube_edges = {
    tuple(sorted((cube_index[x], cube_index[tuple(x[k] ^ (k == mu) for k in range(3))])))
    for x in cube_sites
    for mu in range(3)
}


def push_edges(mapping) -> set[tuple[int, int]]:
    return {
        tuple(sorted((cube_index[mapping(cube_sites[i])], cube_index[mapping(cube_sites[j])])))
        for i, j in cube_edges
    }


cube_symmetry_ok = all(
    push_edges(mapping) == cube_edges
    for mapping in (
        lambda x: (x[0] ^ 1, x[1], x[2]),
        lambda x: (x[0], x[1] ^ 1, x[2]),
        lambda x: (x[0], x[1], x[2] ^ 1),
        lambda x: (x[2], x[0], x[1]),
        lambda x: (x[1], x[0], x[2]),
    )
)
m1 = check(
    "M",
    1,
    "2^3 cube edge set is translation- and cubic-permutation invariant",
    len(cube_edges) == 12 and cube_symmetry_ok,
    f"vertices = {len(cube_sites)}; edges = {len(cube_edges)}",
)

cube_creators = [kron_at(creator, j, len(cube_sites)) for j in range(len(cube_sites))]
cube_annihilators = [op.conj().T for op in cube_creators]
local_paulis = {
    label: [kron_at(pauli, j, len(cube_sites)) for j in range(len(cube_sites))]
    for label, pauli in (("x", sx), ("y", sy), ("z", sz))
}
many_identity = np.eye(2 ** len(cube_sites), dtype=complex)
h_exchange = np.zeros_like(cube_creators[0])
q_axis = np.zeros_like(cube_creators[0])
for c, a in zip(cube_creators, cube_annihilators):
    q_axis += c @ a
for i, j in cube_edges:
    swap_ij = 0.5 * (
        many_identity
        + local_paulis["x"][i] @ local_paulis["x"][j]
        + local_paulis["y"][i] @ local_paulis["y"][j]
        + local_paulis["z"][i] @ local_paulis["z"][j]
    )
    h_exchange += many_identity - swap_ij
exchange_dynamics_ok = (
    np.allclose(h_exchange, h_exchange.conj().T)
    and np.linalg.norm(h_exchange) > TOL
    and np.allclose(h_exchange @ q_axis, q_axis @ h_exchange)
)
m2 = check(
    "M",
    2,
    "sum of edge (I-SWAP) interactions is nonzero, Hermitian, local, and number conserving",
    exchange_dynamics_ok,
    f"matrix = {h_exchange.shape[0]}x{h_exchange.shape[1]}",
)

global_hadamard = hadamard
for _ in range(len(cube_sites) - 1):
    global_hadamard = np.kron(global_hadamard, hadamard)
frame_invariant = np.allclose(
    global_hadamard @ h_exchange @ global_hadamard.conj().T, h_exchange
)
m3 = check(
    "M",
    3,
    "exchange law is invariant under a common one-site frame change",
    frame_invariant,
)

vacuum = np.zeros(2 ** len(cube_sites), dtype=complex)
vacuum[0] = 1.0
one_particle = np.column_stack([c @ vacuum for c in cube_creators])
restricted_h = one_particle.conj().T @ h_exchange @ one_particle
cube_adjacency = np.zeros((len(cube_sites), len(cube_sites)), dtype=float)
for i, j in cube_edges:
    cube_adjacency[i, j] = cube_adjacency[j, i] = 1.0
cube_laplacian = 3.0 * np.eye(len(cube_sites)) - cube_adjacency
m4 = check(
    "M",
    4,
    "one-excitation restriction is exactly the cubic graph Laplacian",
    np.allclose(restricted_h, cube_laplacian),
)


# ---------------------------------------------------------------------------
print("\n--- [K] kinetic/corner discriminators")
translations = [shift(mu) for mu in range(3)]
laplacian = 6.0 * np.eye(NS) - sum(t + t.T for t in translations)
offdiag_support_ok = True
for x in sites():
    for y in sites():
        if x == y or abs(laplacian[idx(x), idx(y)]) < TOL:
            continue
        delta = [min((x[k] - y[k]) % L, (y[k] - x[k]) % L) for k in range(3)]
        offdiag_support_ok &= sorted(delta) == [0, 0, 1]
k1 = check(
    "K",
    1,
    "periodic graph Laplacian is Hermitian, nonzero, and nearest-neighbor local",
    np.allclose(laplacian, laplacian.T) and offdiag_support_ok and np.linalg.norm(laplacian) > TOL,
)

translation_ok = all(np.allclose(laplacian @ t, t @ laplacian) for t in translations)
k2 = check("K", 2, "graph Laplacian is exactly translation invariant", translation_ok)

cyclic = permutation_operator(lambda x: (x[2], x[0], x[1]))
c4z = permutation_operator(lambda x: ((-x[1]) % L, x[0], x[2]))
rotation_ok = all(np.allclose(laplacian @ r, r @ laplacian) for r in (cyclic, c4z))
k3 = check(
    "K",
    3,
    "graph Laplacian is invariant under C3[111] and C4z proper-cubic generators",
    rotation_ok,
)

lap_eigs = np.linalg.eigvalsh(laplacian)
lap_kernel = int(np.sum(np.abs(lap_eigs) < TOL))
corner_eigenvalues = []
corner_eigenvector_ok = True
for bits in itertools.product((0, 1), repeat=3):
    vector = corner_vector(bits)
    expected = 4.0 * sum(bits)
    value = float(np.vdot(vector, laplacian @ vector).real)
    corner_eigenvalues.append(round(value, 10))
    corner_eigenvector_ok &= np.linalg.norm(laplacian @ vector - expected * vector) < TOL
k4 = check(
    "K",
    4,
    "same-lattice completion has one zero, not eight BZ-corner zeros",
    lap_kernel == 1 and corner_eigenvector_ok and corner_eigenvalues.count(0.0) == 1,
    f"kernel = {lap_kernel}; corners = {corner_eigenvalues}",
)


def delta_symbol(momentum: tuple[float, float, float]) -> float:
    return 2.0 * sum(1.0 - np.cos(component) for component in momentum)


momentum_grid = [2.0 * np.pi * n / 17.0 for n in range(17)]
grid_zeros = [
    momentum
    for momentum in itertools.product(momentum_grid, repeat=3)
    if abs(delta_symbol(momentum)) < TOL
]
symbol_corners = [
    round(delta_symbol(tuple(np.pi * bit for bit in bits)), 10)
    for bits in itertools.product((0, 1), repeat=3)
]
infinite_symbol_ok = grid_zeros == [(0.0, 0.0, 0.0)] and symbol_corners == corner_eigenvalues
k5 = check(
    "K",
    5,
    "infinite-Z^3 symbol 2 sum(1-cos k_mu) has only the origin zero on a coprime grid and gives 4h at corners",
    infinite_symbol_ok,
)

plus_flux = plaquette_fluxes(eta_plus)
minus_flux = plaquette_fluxes(eta_ks)
k6 = check(
    "K",
    6,
    "uniform plus and Kawamoto-Smit systems have flux +1 and -1",
    plus_flux == {1} and minus_flux == {-1},
)
k7 = check(
    "K",
    7,
    "different plaquette flux proves the two link systems are not site-gauge equivalent",
    plus_flux.isdisjoint(minus_flux),
)

d_pbc = build_staggered(eta_ks, holonomy=(1, 1, 1))
d_mmm = build_staggered(eta_ks, holonomy=(-1, -1, -1))
k8 = check("K", 8, "periodic Kawamoto-Smit D is real antisymmetric", np.allclose(d_pbc, -d_pbc.T))
sv_pbc = np.linalg.svd(d_pbc, compute_uv=False)
sv_mmm = np.linalg.svd(d_mmm, compute_uv=False)
pbc_kernel = int(np.sum(sv_pbc < TOL))
mmm_kernel = int(np.sum(sv_mmm < TOL))
corner_null_ok = all(
    np.linalg.norm(d_pbc @ corner_vector(bits)) < TOL
    for bits in itertools.product((0, 1), repeat=3)
)
k9 = check(
    "K",
    9,
    "PBC Kawamoto-Smit comparator has exactly eight corner null vectors",
    pbc_kernel == 8 and corner_null_ok,
    f"kernel = {pbc_kernel}",
)
k10 = check(
    "K",
    10,
    "the same local law with (-,-,-) wrap holonomy has no exact finite-volume zero",
    mmm_kernel == 0 and float(np.min(sv_mmm)) > TOL,
    f"kernel = {mmm_kernel}; min singular value = {np.min(sv_mmm):.10f}",
)


# ---------------------------------------------------------------------------
print("\n--- [C] no-go assembly")
shared_current_amin = all(source_checks) and all((r1, r2, r3, r4, r5))
nonstaggered_completion = all((m1, m2, m3, m4, k1, k2, k3, k4, k5))
c1 = check(
    "C",
    1,
    "explicit current-A_min reduct admits a nonzero local cubic kinetic completion with one, not eight, zero",
    shared_current_amin and nonstaggered_completion,
    "basis-independent exchange interaction; graph-Laplacian one-particle generator",
)
c2 = check(
    "C",
    2,
    "flux and wrap-holonomy checks sharpen the independent choices after a kinetic surface is supplied",
    all((k6, k7, k8, k9, k10)),
)

print("\n" + "=" * 78)
print(f"TOTAL: PASS={_passed} FAIL={_failed}")
if _failed == 0 and c1 and c2:
    print("VERDICT: exact kinetic/corner non-forcing countermodel VERIFIED.")
    print("         Current A_min admits a nonzero, local, translation/proper-")
    print("         cubic-invariant qubit-exchange interaction whose infinite-Z^3")
    print("         one-particle Bloch symbol is the graph-Laplacian symbol,")
    print("         not staggered Dirac, and its zero set is {k=0}.")
    print("         Flux class and finite wrap holonomy remain additional choices.")
else:
    print("VERDICT: certificate FAILED; no no-go conclusion is licensed.")

sys.exit(0 if _failed == 0 and c1 and c2 else 1)
