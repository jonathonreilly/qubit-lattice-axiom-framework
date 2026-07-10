#!/usr/bin/env python3
"""Orbit-reduced exact-evolution engine for the d=3 registration pilot.

This machinery module implements the open ``3 x 3 x 3`` qubit cube with
sites ``(x, y, z) in {-1, 0, 1}^3``.  Its 27 qubits have ``2^27`` raw
configurations.  Quotienting those configurations by the 24 proper cubic
rotations gives exactly 5,605,504 spatial orbits; both the group order and
the orbit count are independently checked below.  The reduced state is one
``complex128`` coefficient per *normalised* orbit sum and is therefore about
90 MB.  No reduced-mode routine constructs a ``2^27`` complex vector.

Invariant-sector argument
-------------------------
The preparation used by the pilot is a spatially uniform product state and
the open-cube Hamiltonian is invariant under every proper cubic rotation.
Consequently exact evolution remains in the invariant subspace.  If
``|psi>`` is invariant and ``O_g = U_g O U_g^dagger``, then
``<psi|O_g|psi> = <psi|O|psi>``.  A local site, fragment, or pair expectation
may therefore be evaluated as the average of its complete group orbit.  That
average is an invariant operator and acts entirely inside the orbit basis.
The observable routines below always form this group average (the centre is
a fixed point), including the projector ``P_(Z_S=s)`` and all off-diagonal
Pauli terms.  Thus the returned one- and two-qubit states equal the states at
each symmetry-related physical site/pair while remaining computable without
expanding the raw Hilbert-space vector.

Orbit normalisation and the flip factor
---------------------------------------
For a configuration orbit ``A`` of size ``n_A``, the stored basis vector is

``|A> = n_A^(-1/2) sum_(x in A) |x>``.

Let output row ``A`` gather from input orbit ``B`` after a representative
bit flip.  In raw amplitudes an invariant state has amplitude
``psi_B/sqrt(n_B)`` at every member of ``B``; converting the output raw
amplitude back to the normalised coordinate multiplies it by ``sqrt(n_A)``.
Every row-gather contribution consequently carries
``sqrt(n_A/n_B)``.  In the tables and docstrings, **target** means the output
orbit of ``H psi`` and **source** means the gathered input orbit, so this is
exactly ``sqrt(orbit_size_target/orbit_size_source)``.  Multiplicities arise
because several physical site flips can reach the same orbit.  Reversing
target/source to mean “representative before/after the flip” would give the
reciprocal and is not Hermitian when orbit sizes differ.

SPEC-NOTE (flip-table wording): ``flip_targets[site, row]`` is retained as
the familiar name for the orbit reached by flipping the row representative,
but in the matrix row-gather that integer is the *input source* ``B`` and the
row is the output target ``A``.  Accordingly ``flip_amplitudes[site, row]``
stores ``sqrt(n_A/n_B)``.  This convention is not a silent correction: the
alternative literal before/after interpretation conflicts with the required
Hermiticity check.  The implementation verifies the summed operator both as
a sparse slab matrix and with complex random vectors to relative ``1e-12``.

The module makes numerical-machinery claims only.  It makes no physical,
formation, gravity, or audit-status claim.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import resource
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence

import numpy as np
import numpy.typing as npt
from scipy import sparse
from scipy.sparse.linalg import LinearOperator, eigsh, expm_multiply


# Fixed resource and numerical policy.  Chunks bound temporary staging even
# when the persistent cube transition tables are resident.
BUDGET_GB = 10.0
VALIDATION_BUDGET_GB = 4.0
CACHE_DISK_BUDGET_BYTES = 2_500_000_000
CANONICAL_CHUNK = 1 << 19
TABLE_CHUNK = 1 << 19
MATVEC_CHUNK = 1 << 17
OBSERVABLE_CHUNK = 1 << 18
RSS_CHECK_EVERY_CHUNKS = 8
EVOLVE_NORM_TOL = 1.0e-9
DENSITY_TOL = 1.0e-9
HERMITICITY_TOL = 1.0e-12
GROUND_TOL = 1.0e-10
GROUND_MAXITER = 800
GROUND_NCV = 12
CHECKPOINT_EVERY = 5

EXPECTED_CUBE_ORBITS = 5_605_504
EXPECTED_CUBE_BONDS = 54
EXPECTED_CUBE_GROUP_ORDER = 24
EXPECTED_SLAB_GROUP_ORDER = 8
EXPECTED_SLAB_BONDS = 33
TABLE_SCHEMA = "d3-orbit-engine-v1"

REPO_ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = REPO_ROOT / "logs" / "runner-cache" / "d3_engine_tables"
CHECKPOINT_PATH = CACHE_DIR / "d3_evolution_checkpoint.npz"

UIntArray = npt.NDArray[np.uint32]
FloatArray = npt.NDArray[np.float64]
ComplexArray = npt.NDArray[np.complex128]


@dataclass(frozen=True)
class OrbitBasis:
    """Normalised spatial-orbit basis and its verified geometry.

    ``representatives`` is a strictly increasing ``uint32`` array of the
    minimum integer in each rotation orbit.  ``orbit_sizes`` is ``uint8``
    here (all sizes divide 24).  ``site_permutations[g, i]`` is the
    source-to-destination site map for group element ``g``.  The remaining
    fields make the indexing and cache association explicit; callers should
    treat all arrays as read-only.
    """

    representatives: UIntArray
    orbit_sizes: npt.NDArray[np.uint8]
    site_permutations: npt.NDArray[np.int16]
    coordinates: npt.NDArray[np.int8]
    bonds: npt.NDArray[np.int16]
    group_name: str
    geometry_name: str
    checksum: str
    cache_status: str = "memory"
    cache_path: str = ""

    @property
    def n_orbits(self) -> int:
        return int(self.representatives.size)

    @property
    def n_sites(self) -> int:
        return int(self.coordinates.shape[0])


@dataclass(frozen=True)
class HamiltonianTables:
    """Cached matrix-free tables in site-major layout.

    ``diagonal_zz`` is ``float64`` and contains
    ``-sum_<ij> Z_i Z_j``.  ``flip_targets`` and ``flip_amplitudes`` have
    shape ``(n_sites, n_orbits)``.  For output row ``A`` and site ``i``, the
    former identifies input orbit ``B`` of the flipped representative and
    the latter is the normalised row-gather factor ``sqrt(n_A/n_B)`` derived
    in the module docstring.  ``double_flip_targets`` stores only the masks
    required by the exposed two-qubit observables; their factors are derived
    from the two orbit-size arrays in a chunk.
    """

    diagonal_zz: FloatArray
    flip_targets: npt.NDArray[np.int32]
    flip_amplitudes: FloatArray
    double_flip_masks: UIntArray
    double_flip_targets: npt.NDArray[np.int32]
    basis_checksum: str
    checksum: str
    cache_status: str = "memory"
    cache_path: str = ""


@dataclass(frozen=True)
class _Geometry:
    name: str
    coordinates: npt.NDArray[np.int8]
    bonds: npt.NDArray[np.int16]
    permutations: npt.NDArray[np.int16]
    group_name: str
    expected_group_order: int
    expected_bonds: int
    expected_orbits: int | None

    @property
    def n_sites(self) -> int:
        return int(self.coordinates.shape[0])


@dataclass(frozen=True)
class _ObservableSpec:
    pointer: int
    fragments: Mapping[str, int]
    pairs: Mapping[str, tuple[int, int]]
    center_bond: tuple[int, int]


@dataclass
class _DensityDiagnostics:
    hermiticity: float = 0.0
    trace: float = 0.0
    negativity: float = 0.0


_ACTIVE_BASIS: OrbitBasis | None = None
_ACTIVE_TABLES: HamiltonianTables | None = None
_ACTIVE_SPEC: _ObservableSpec | None = None
_DENSITY_WORST = _DensityDiagnostics()
_LAST_CACHE_STATS: dict[str, object] = {}


def rss_gb() -> float:
    """Return process peak resident-set size in GiB using only ``resource``.

    ``ru_maxrss`` is bytes on macOS and KiB on Linux.  It is a peak rather
    than an instantaneous sample, which makes every later guard conservative.
    """

    raw = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return raw / (1024.0**3 if sys.platform == "darwin" else 1024.0**2)


def _guard_rss(point: str, budget_gb: float = BUDGET_GB) -> None:
    used = rss_gb()
    if used > budget_gb:
        raise RuntimeError(
            f"RSS guard at {point}: {used:.3f} GiB exceeds {budget_gb:.3f} GiB"
        )


def _det3(matrix: npt.NDArray[np.int64]) -> int:
    a = matrix
    return int(
        a[0, 0] * (a[1, 1] * a[2, 2] - a[1, 2] * a[2, 1])
        - a[0, 1] * (a[1, 0] * a[2, 2] - a[1, 2] * a[2, 0])
        + a[0, 2] * (a[1, 0] * a[2, 1] - a[1, 1] * a[2, 0])
    )


def _nearest_neighbor_bonds(
    coordinates: npt.NDArray[np.int8], spacing: int
) -> npt.NDArray[np.int16]:
    delta = np.abs(
        coordinates[:, None, :].astype(np.int16)
        - coordinates[None, :, :].astype(np.int16)
    )
    adjacent = (np.count_nonzero(delta, axis=2) == 1) & (
        np.sum(delta, axis=2) == spacing
    )
    i, j = np.nonzero(np.triu(adjacent, k=1))
    return np.column_stack((i, j)).astype(np.int16, copy=False)


def _proper_rotation_permutations(
    coordinates: npt.NDArray[np.int8],
) -> npt.NDArray[np.int16]:
    index = {tuple(map(int, xyz)): i for i, xyz in enumerate(coordinates)}
    rotations: list[tuple[tuple[int, ...], npt.NDArray[np.int16]]] = []
    for axes in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=np.int64)
            for row in range(3):
                matrix[row, axes[row]] = signs[row]
            if _det3(matrix) != 1:
                continue
            transformed = coordinates.astype(np.int64) @ matrix.T
            try:
                perm = np.asarray(
                    [index[tuple(map(int, xyz))] for xyz in transformed],
                    dtype=np.int16,
                )
            except KeyError:
                continue
            rotations.append((tuple(int(v) for v in matrix.ravel()), perm))
    rotations.sort(key=lambda item: item[0])
    return np.stack([perm for _, perm in rotations], axis=0)


def _assert_group_and_graph(geometry: _Geometry) -> None:
    perms = geometry.permutations
    order, n_sites = perms.shape
    if order != geometry.expected_group_order:
        raise AssertionError(
            f"{geometry.name} group order {order}, expected "
            f"{geometry.expected_group_order}"
        )
    expected_sites = np.arange(n_sites, dtype=np.int16)
    keys = {tuple(map(int, p)) for p in perms}
    if len(keys) != order or tuple(map(int, expected_sites)) not in keys:
        raise AssertionError(f"{geometry.name} rotations are not a distinct group")
    for left in perms:
        for right in perms:
            # source --left--> left[source] --right--> right[left[source]]
            if tuple(map(int, right[left])) not in keys:
                raise AssertionError(f"{geometry.name} rotation closure failed")
    if geometry.bonds.shape != (geometry.expected_bonds, 2):
        raise AssertionError(
            f"{geometry.name} has {geometry.bonds.shape[0]} bonds, expected "
            f"{geometry.expected_bonds}"
        )
    bond_set = {tuple(sorted(map(int, bond))) for bond in geometry.bonds}
    for perm in perms:
        mapped = {
            tuple(sorted((int(perm[i]), int(perm[j]))))
            for i, j in geometry.bonds
        }
        if mapped != bond_set:
            raise AssertionError(
                f"{geometry.name} rotation does not preserve neighbor graph"
            )


def _cube_geometry() -> _Geometry:
    coords = np.asarray(
        list(itertools.product((-1, 0, 1), repeat=3)), dtype=np.int8
    )
    geometry = _Geometry(
        name="open-3x3x3",
        coordinates=coords,
        bonds=_nearest_neighbor_bonds(coords, spacing=1),
        permutations=_proper_rotation_permutations(coords),
        group_name="proper cubic rotation group O (order 24)",
        expected_group_order=EXPECTED_CUBE_GROUP_ORDER,
        expected_bonds=EXPECTED_CUBE_BONDS,
        expected_orbits=EXPECTED_CUBE_ORBITS,
    )
    _assert_group_and_graph(geometry)
    _guard_rss("cube geometry/group verification")
    return geometry


def _slab_geometry() -> _Geometry:
    # Doubled centred coordinates keep both slab layers integral.  The full
    # orientation-preserving symmetry group of the square prism is D4: four
    # rotations around the thin axis and four pi rotations about in-plane
    # axes/diagonals.  It has order 8 and may exchange the two layers.
    coords = np.asarray(
        list(itertools.product((-2, 0, 2), (-2, 0, 2), (-1, 1))),
        dtype=np.int8,
    )
    geometry = _Geometry(
        name="open-3x3x2",
        coordinates=coords,
        bonds=_nearest_neighbor_bonds(coords, spacing=2),
        permutations=_proper_rotation_permutations(coords),
        group_name="proper square-prism rotation group D4 (order 8)",
        expected_group_order=EXPECTED_SLAB_GROUP_ORDER,
        expected_bonds=EXPECTED_SLAB_BONDS,
        expected_orbits=None,
    )
    _assert_group_and_graph(geometry)
    _guard_rss("slab geometry/group verification")
    return geometry


def _cycle_count(permutation: npt.NDArray[np.int16]) -> int:
    seen = np.zeros(permutation.size, dtype=bool)
    cycles = 0
    for start in range(permutation.size):  # at most 27, never configurations
        if seen[start]:
            continue
        cycles += 1
        cursor = start
        while not seen[cursor]:
            seen[cursor] = True
            cursor = int(permutation[cursor])
    return cycles


def _burnside_orbit_count(geometry: _Geometry) -> int:
    total = sum(1 << _cycle_count(perm) for perm in geometry.permutations)
    quotient, remainder = divmod(total, geometry.permutations.shape[0])
    if remainder:
        raise AssertionError("Burnside sum is not divisible by group order")
    return quotient


def _geometry_stamp(geometry: _Geometry, kind: str) -> str:
    payload = {
        "schema": TABLE_SCHEMA,
        "kind": kind,
        "name": geometry.name,
        "coordinates": geometry.coordinates.astype(int).tolist(),
        "bonds": geometry.bonds.astype(int).tolist(),
        "permutations": geometry.permutations.astype(int).tolist(),
        "normalisation": "normalised-orbit-row-gather-target-over-source",
        "dtype": "float64",
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()[:16]


def _hash_arrays(arrays: Iterable[tuple[str, npt.NDArray]]) -> str:
    digest = hashlib.sha256()
    block = 64 << 20
    for name, array in arrays:
        contiguous = np.ascontiguousarray(array)
        digest.update(name.encode())
        digest.update(contiguous.dtype.str.encode())
        digest.update(np.asarray(contiguous.shape, dtype=np.int64).tobytes())
        raw = memoryview(contiguous).cast("B")
        for offset in range(0, raw.nbytes, block):
            digest.update(raw[offset : offset + block])
    return digest.hexdigest()


def _cache_size_bytes() -> int:
    if not CACHE_DIR.exists():
        return 0
    # The 2.5 GB requirement is for one-time *tables*.  The separately
    # declared evolution checkpoint is deliberately not counted as a table.
    return sum(
        path.stat().st_size
        for path in CACHE_DIR.glob("*.npz")
        if path.resolve() != CHECKPOINT_PATH.resolve()
    )


def _enforce_cache_budget() -> None:
    size = _cache_size_bytes()
    if size >= CACHE_DISK_BUDGET_BYTES:
        raise RuntimeError(
            f"engine cache is {size / 1e9:.3f} GB; limit is "
            f"{CACHE_DISK_BUDGET_BYTES / 1e9:.3f} GB"
        )


def _atomic_savez(path: Path, *, compressed: bool, **arrays: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.stem}.{os.getpid()}.tmp.npz")
    try:
        if compressed:
            np.savez_compressed(temporary, **arrays)
        else:
            np.savez(temporary, **arrays)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    try:
        _enforce_cache_budget()
    except Exception:
        # Never leave a newly written table behind in violation of the hard
        # on-disk budget.  Checkpoints are excluded from that table budget.
        if path.resolve() != CHECKPOINT_PATH.resolve():
            path.unlink(missing_ok=True)
        raise


def _basis_cache_path(geometry: _Geometry) -> Path:
    return CACHE_DIR / f"{geometry.name}-basis-{_geometry_stamp(geometry, 'basis')}.npz"


def _table_cache_path(
    geometry: _Geometry, basis: OrbitBasis, double_masks: UIntArray
) -> Path:
    suffix = hashlib.sha256(
        (basis.checksum + ":" + double_masks.tobytes().hex()).encode()
    ).hexdigest()[:16]
    return CACHE_DIR / (
        f"{geometry.name}-hamiltonian-{_geometry_stamp(geometry, 'tables')}-{suffix}.npz"
    )


def _permutation_luts(geometry: _Geometry) -> npt.NDArray[np.uint32]:
    """Build 9-bit block LUTs for vectorised 27-bit permutations."""

    values = np.arange(1 << 9, dtype=np.uint32)
    luts = np.zeros(
        (geometry.permutations.shape[0], 3, 1 << 9), dtype=np.uint32
    )
    for group_index, permutation in enumerate(geometry.permutations):
        for block_index in range(3):
            mapped = np.zeros(values.size, dtype=np.uint32)
            for local_bit in range(9):  # site loop only; configurations vectorised
                source = 9 * block_index + local_bit
                if source >= geometry.n_sites:
                    break
                destination = int(permutation[source])
                mapped |= ((values >> np.uint32(local_bit)) & np.uint32(1)) << np.uint32(
                    destination
                )
            luts[group_index, block_index] = mapped
    return luts


def _permute_bits(
    values: UIntArray, rotation_lut: npt.NDArray[np.uint32]
) -> UIntArray:
    """Apply one source-to-destination site map with shifts/masks on a chunk."""

    mask = np.uint32((1 << 9) - 1)
    return (
        rotation_lut[0, values & mask]
        | rotation_lut[1, (values >> np.uint32(9)) & mask]
        | rotation_lut[2, (values >> np.uint32(18)) & mask]
    )


def _canonicalise_chunk(
    values: UIntArray, luts: npt.NDArray[np.uint32]
) -> UIntArray:
    canonical = values.copy()
    for rotation_lut in luts:
        np.minimum(canonical, _permute_bits(values, rotation_lut), out=canonical)
    return canonical


def _basis_checksum(
    representatives: UIntArray,
    orbit_sizes: npt.NDArray[np.uint8],
    geometry: _Geometry,
) -> str:
    return _hash_arrays(
        (
            ("representatives", representatives),
            ("orbit_sizes", orbit_sizes),
            ("site_permutations", geometry.permutations),
            ("coordinates", geometry.coordinates),
            ("bonds", geometry.bonds),
        )
    )


def _validate_basis_arrays(
    geometry: _Geometry,
    representatives: npt.NDArray,
    orbit_sizes: npt.NDArray,
    permutations: npt.NDArray,
    stored_checksum: str,
) -> str:
    expected_orbits = _burnside_orbit_count(geometry)
    if geometry.expected_orbits is not None and expected_orbits != geometry.expected_orbits:
        raise AssertionError(
            f"computed {geometry.name} orbit count {expected_orbits}; expected "
            f"{geometry.expected_orbits}"
        )
    if representatives.shape != (expected_orbits,) or representatives.dtype != np.uint32:
        raise RuntimeError(
            f"invalid cached representative shape/dtype: {representatives.shape}, "
            f"{representatives.dtype}"
        )
    if orbit_sizes.shape != (expected_orbits,) or orbit_sizes.dtype != np.uint8:
        raise RuntimeError(
            f"invalid cached orbit-size shape/dtype: {orbit_sizes.shape}, "
            f"{orbit_sizes.dtype}"
        )
    if permutations.shape != geometry.permutations.shape or permutations.dtype != np.int16:
        raise RuntimeError("invalid cached site-permutation table")
    if not np.array_equal(permutations, geometry.permutations):
        raise RuntimeError("cached site permutations do not match geometry stamp")
    if representatives.size and (
        int(representatives[0]) != 0
        or np.any(representatives[1:] <= representatives[:-1])
    ):
        raise RuntimeError("cached representatives are not strictly increasing from zero")
    group_order = geometry.permutations.shape[0]
    if np.any(orbit_sizes == 0) or np.any(group_order % orbit_sizes != 0):
        raise RuntimeError("cached orbit sizes do not divide the group order")
    computed = _basis_checksum(representatives, orbit_sizes, geometry)
    if computed != stored_checksum:
        raise RuntimeError(
            f"basis cache checksum mismatch: stored {stored_checksum}, computed {computed}"
        )
    return computed


def _load_basis(geometry: _Geometry, path: Path) -> OrbitBasis | None:
    if not path.exists():
        return None
    try:
        with np.load(path, allow_pickle=False) as archive:
            representatives = np.asarray(archive["representatives"])
            orbit_sizes = np.asarray(archive["orbit_sizes"])
            permutations = np.asarray(archive["site_permutations"])
            stored_checksum = str(np.asarray(archive["checksum"]).item())
            stored_schema = str(np.asarray(archive["schema"]).item())
        if stored_schema != TABLE_SCHEMA:
            raise RuntimeError(
                f"basis cache schema {stored_schema!r}, expected {TABLE_SCHEMA!r}"
            )
        checksum = _validate_basis_arrays(
            geometry,
            representatives,
            orbit_sizes,
            permutations,
            stored_checksum,
        )
    except Exception as exc:
        raise RuntimeError(f"invalid basis cache {path}: {exc}") from exc
    _guard_rss(f"load basis {geometry.name}")
    return OrbitBasis(
        representatives=representatives,
        orbit_sizes=orbit_sizes,
        site_permutations=permutations,
        coordinates=geometry.coordinates.copy(),
        bonds=geometry.bonds.copy(),
        group_name=geometry.group_name,
        geometry_name=geometry.name,
        checksum=checksum,
        cache_status="loaded",
        cache_path=str(path),
    )


def _construct_basis(geometry: _Geometry, path: Path) -> OrbitBasis:
    started = time.perf_counter()
    luts = _permutation_luts(geometry)
    raw_dimension = 1 << geometry.n_sites
    pieces: list[UIntArray] = []
    for chunk_number, start in enumerate(range(0, raw_dimension, CANONICAL_CHUNK)):
        stop = min(start + CANONICAL_CHUNK, raw_dimension)
        values = np.arange(start, stop, dtype=np.uint32)
        canonical = _canonicalise_chunk(values, luts)
        pieces.append(values[values == canonical])
        if chunk_number % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} canonical basis chunk {chunk_number}")
    representatives = np.concatenate(pieces).astype(np.uint32, copy=False)
    del pieces

    burnside_count = _burnside_orbit_count(geometry)
    if representatives.size != burnside_count:
        raise AssertionError(
            f"enumerated {geometry.name} orbit count {representatives.size}; "
            f"Burnside gives {burnside_count}"
        )
    if geometry.expected_orbits is not None and burnside_count != geometry.expected_orbits:
        raise AssertionError(
            f"computed {geometry.name} orbit count {burnside_count}; expected "
            f"{geometry.expected_orbits}"
        )

    stabiliser_sizes = np.zeros(representatives.size, dtype=np.uint8)
    for group_index, rotation_lut in enumerate(luts):
        for start in range(0, representatives.size, TABLE_CHUNK):
            stop = min(start + TABLE_CHUNK, representatives.size)
            values = representatives[start:stop]
            stabiliser_sizes[start:stop] += (
                _permute_bits(values, rotation_lut) == values
            ).astype(np.uint8)
        if group_index % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} orbit-size group element {group_index}")
    group_order = geometry.permutations.shape[0]
    if np.any(stabiliser_sizes == 0) or np.any(group_order % stabiliser_sizes != 0):
        raise AssertionError("invalid stabiliser size during basis construction")
    orbit_sizes = (group_order // stabiliser_sizes).astype(np.uint8)
    if int(np.sum(orbit_sizes, dtype=np.uint64)) != raw_dimension:
        raise AssertionError("orbit sizes do not sum to the raw Hilbert dimension")
    checksum = _basis_checksum(representatives, orbit_sizes, geometry)
    _atomic_savez(
        path,
        compressed=True,
        representatives=representatives,
        orbit_sizes=orbit_sizes,
        site_permutations=geometry.permutations,
        checksum=np.asarray(checksum),
        schema=np.asarray(TABLE_SCHEMA),
    )
    _LAST_CACHE_STATS[f"{geometry.name}-basis-seconds"] = time.perf_counter() - started
    _guard_rss(f"complete {geometry.name} basis construction")
    return OrbitBasis(
        representatives=representatives,
        orbit_sizes=orbit_sizes,
        site_permutations=geometry.permutations.copy(),
        coordinates=geometry.coordinates.copy(),
        bonds=geometry.bonds.copy(),
        group_name=geometry.group_name,
        geometry_name=geometry.name,
        checksum=checksum,
        cache_status="built",
        cache_path=str(path),
    )


def _build_basis_for_geometry(geometry: _Geometry) -> OrbitBasis:
    _enforce_cache_budget()
    path = _basis_cache_path(geometry)
    started = time.perf_counter()
    basis = _load_basis(geometry, path)
    if basis is None:
        basis = _construct_basis(geometry, path)
    _LAST_CACHE_STATS[f"{geometry.name}-basis-status"] = basis.cache_status
    _LAST_CACHE_STATS[f"{geometry.name}-basis-wall-seconds"] = (
        time.perf_counter() - started
    )
    return basis


def build_orbit_basis() -> OrbitBasis:
    """Build or load the verified 5,605,504-orbit cube basis.

    Canonical representatives are found as the minimum of all 24 bit-
    permuted images.  The raw integer range is visited only in ``uint32``
    chunks of :data:`CANONICAL_CHUNK`; no raw complex state is allocated.
    Each rotation uses three precomputed 9-bit LUTs, themselves derived from
    the verified source-to-destination site map, and applies them with
    vectorised shifts and masks.  The Burnside count and enumerated count
    must both equal 5,605,504; a mismatch raises rather than changing the
    declared value.  The checksummed, SHA-stamped result is cached below
    ``logs/runner-cache/d3_engine_tables``.
    """

    return _build_basis_for_geometry(_cube_geometry())


def _coordinate_index(basis: OrbitBasis) -> dict[tuple[int, int, int], int]:
    return {
        tuple(map(int, coordinate)): i
        for i, coordinate in enumerate(basis.coordinates)
    }


def _observable_spec(basis: OrbitBasis) -> _ObservableSpec:
    index = _coordinate_index(basis)
    if basis.geometry_name == "open-3x3x3":
        pointer = index[(0, 0, 0)]
        plus_x = index[(1, 0, 0)]
        return _ObservableSpec(
            pointer=pointer,
            fragments={
                "axial": plus_x,
                "edge": index[(1, 1, 0)],
                "corner": index[(1, 1, 1)],
            },
            pairs={
                "opposite-axis": (plus_x, index[(-1, 0, 0)]),
                "orthogonal-axis": (plus_x, index[(0, 1, 0)]),
            },
            center_bond=(pointer, plus_x),
        )
    if basis.geometry_name == "open-3x3x2":
        pointer = index[(0, 0, -1)]
        plus_x = index[(2, 0, -1)]
        return _ObservableSpec(
            pointer=pointer,
            fragments={
                "axial": plus_x,
                "edge": index[(2, 2, -1)],
                "corner": index[(2, 2, 1)],
            },
            pairs={
                "opposite-axis": (plus_x, index[(-2, 0, -1)]),
                "orthogonal-axis": (plus_x, index[(0, 2, -1)]),
            },
            center_bond=(pointer, plus_x),
        )
    raise ValueError(f"unsupported observable geometry {basis.geometry_name}")


def _operator_orbit(
    basis: OrbitBasis,
    sites: Sequence[int],
    labels: Sequence[str],
    pointer: int | None = None,
) -> list[tuple[int | None, tuple[int, ...], tuple[str, ...]]]:
    if len(sites) != len(labels):
        raise ValueError("Pauli sites and labels have different lengths")
    terms: set[tuple[int | None, tuple[int, ...], tuple[str, ...]]] = set()
    label_tuple = tuple(labels)
    for permutation in basis.site_permutations:
        transformed_sites = tuple(int(permutation[site]) for site in sites)
        transformed_pointer = None if pointer is None else int(permutation[pointer])
        terms.add((transformed_pointer, transformed_sites, label_tuple))
    return sorted(terms, key=repr)


def _required_double_masks(basis: OrbitBasis, spec: _ObservableSpec) -> UIntArray:
    masks: set[int] = set()
    for pair in (*spec.pairs.values(), spec.center_bond):
        for _, transformed, _ in _operator_orbit(basis, pair, ("X", "X")):
            first, second = transformed
            masks.add((1 << first) | (1 << second))
    return np.asarray(sorted(masks), dtype=np.uint32)


def _table_checksum(
    diagonal: FloatArray,
    flip_targets: npt.NDArray[np.int32],
    flip_amplitudes: FloatArray,
    double_masks: UIntArray,
    double_targets: npt.NDArray[np.int32],
    basis_checksum: str,
) -> str:
    digest = hashlib.sha256(basis_checksum.encode())
    digest.update(
        _hash_arrays(
            (
                ("diagonal_zz", diagonal),
                ("flip_targets", flip_targets),
                ("flip_amplitudes", flip_amplitudes),
                ("double_flip_masks", double_masks),
                ("double_flip_targets", double_targets),
            )
        ).encode()
    )
    return digest.hexdigest()


def _validate_table_arrays(
    basis: OrbitBasis,
    diagonal: npt.NDArray,
    flip_targets: npt.NDArray,
    flip_amplitudes: npt.NDArray,
    double_masks: npt.NDArray,
    double_targets: npt.NDArray,
    stored_basis_checksum: str,
    stored_checksum: str,
) -> str:
    n_sites, n_orbits = basis.n_sites, basis.n_orbits
    if stored_basis_checksum != basis.checksum:
        raise RuntimeError("Hamiltonian table belongs to a different orbit basis")
    expected = {
        "diagonal": (diagonal, (n_orbits,), np.dtype(np.float64)),
        "flip_targets": (
            flip_targets,
            (n_sites, n_orbits),
            np.dtype(np.int32),
        ),
        "flip_amplitudes": (
            flip_amplitudes,
            (n_sites, n_orbits),
            np.dtype(np.float64),
        ),
        "double_masks": (double_masks, (double_masks.size,), np.dtype(np.uint32)),
        "double_targets": (
            double_targets,
            (double_masks.size, n_orbits),
            np.dtype(np.int32),
        ),
    }
    for name, (array, shape, dtype) in expected.items():
        if array.shape != shape or array.dtype != dtype:
            raise RuntimeError(
                f"invalid {name} shape/dtype {array.shape}/{array.dtype}; "
                f"expected {shape}/{dtype}"
            )
    if double_masks.size and np.any(double_masks[1:] <= double_masks[:-1]):
        raise RuntimeError("double-flip masks are not strictly increasing")
    if np.any(flip_targets < 0) or np.any(flip_targets >= n_orbits):
        raise RuntimeError("single-flip target index outside orbit basis")
    if np.any(double_targets < 0) or np.any(double_targets >= n_orbits):
        raise RuntimeError("double-flip target index outside orbit basis")
    if not np.all(np.isfinite(flip_amplitudes)) or np.any(flip_amplitudes <= 0):
        raise RuntimeError("invalid single-flip amplitude")
    computed = _table_checksum(
        diagonal,
        flip_targets,
        flip_amplitudes,
        double_masks,
        double_targets,
        basis.checksum,
    )
    if computed != stored_checksum:
        raise RuntimeError(
            f"Hamiltonian cache checksum mismatch: stored {stored_checksum}, "
            f"computed {computed}"
        )
    return computed


def _load_tables(
    basis: OrbitBasis, path: Path, required_masks: UIntArray
) -> HamiltonianTables | None:
    if not path.exists():
        return None
    try:
        with np.load(path, allow_pickle=False) as archive:
            diagonal = np.asarray(archive["diagonal_zz"])
            flip_targets = np.asarray(archive["flip_targets"])
            flip_amplitudes = np.asarray(archive["flip_amplitudes"])
            double_masks = np.asarray(archive["double_flip_masks"])
            double_targets = np.asarray(archive["double_flip_targets"])
            stored_basis_checksum = str(
                np.asarray(archive["basis_checksum"]).item()
            )
            stored_checksum = str(np.asarray(archive["checksum"]).item())
            stored_schema = str(np.asarray(archive["schema"]).item())
        if stored_schema != TABLE_SCHEMA:
            raise RuntimeError(
                f"table cache schema {stored_schema!r}, expected {TABLE_SCHEMA!r}"
            )
        if not np.array_equal(double_masks, required_masks):
            raise RuntimeError("cached double-flip masks do not match observable set")
        checksum = _validate_table_arrays(
            basis,
            diagonal,
            flip_targets,
            flip_amplitudes,
            double_masks,
            double_targets,
            stored_basis_checksum,
            stored_checksum,
        )
    except Exception as exc:
        raise RuntimeError(f"invalid Hamiltonian cache {path}: {exc}") from exc
    _guard_rss(f"load Hamiltonian tables {basis.geometry_name}")
    return HamiltonianTables(
        diagonal_zz=diagonal,
        flip_targets=flip_targets,
        flip_amplitudes=flip_amplitudes,
        double_flip_masks=double_masks,
        double_flip_targets=double_targets,
        basis_checksum=basis.checksum,
        checksum=checksum,
        cache_status="loaded",
        cache_path=str(path),
    )


def _construct_tables(
    basis: OrbitBasis,
    geometry: _Geometry,
    path: Path,
    required_masks: UIntArray,
) -> HamiltonianTables:
    started = time.perf_counter()
    n_orbits, n_sites = basis.n_orbits, basis.n_sites
    representatives = basis.representatives
    sizes = basis.orbit_sizes
    luts = _permutation_luts(geometry)

    # A temporary 512 MiB int32 raw-to-orbit map for the cube replaces 27x24
    # repeated canonicalisation passes.  It is never complex and is deleted
    # before checksumming/saving the persistent tables.
    raw_dimension = 1 << n_sites
    orbit_index = np.full(raw_dimension, -1, dtype=np.int32)
    for group_index, rotation_lut in enumerate(luts):
        for start in range(0, n_orbits, TABLE_CHUNK):
            stop = min(start + TABLE_CHUNK, n_orbits)
            images = _permute_bits(representatives[start:stop], rotation_lut)
            orbit_index[images] = np.arange(start, stop, dtype=np.int32)
        if group_index % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} raw-to-orbit group element {group_index}")
    if np.any(orbit_index < 0):
        raise AssertionError("raw-to-orbit map has unassigned configurations")
    if not np.array_equal(orbit_index[representatives], np.arange(n_orbits, dtype=np.int32)):
        raise AssertionError("raw-to-orbit map does not fix canonical representatives")

    diagonal = np.empty(n_orbits, dtype=np.float64)
    left = geometry.bonds[:, 0].astype(np.uint32)
    right = geometry.bonds[:, 1].astype(np.uint32)
    for chunk_number, start in enumerate(range(0, n_orbits, TABLE_CHUNK)):
        stop = min(start + TABLE_CHUNK, n_orbits)
        values = representatives[start:stop]
        disagreements = (
            ((values[None, :] >> left[:, None]) ^ (values[None, :] >> right[:, None]))
            & np.uint32(1)
        )
        diagonal[start:stop] = -float(geometry.expected_bonds) + 2.0 * np.sum(
            disagreements, axis=0, dtype=np.int16
        )
        if chunk_number % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} ZZ diagonal chunk {chunk_number}")

    flip_targets = np.empty((n_sites, n_orbits), dtype=np.int32)
    flip_amplitudes = np.empty((n_sites, n_orbits), dtype=np.float64)
    row_sizes = sizes.astype(np.float64)
    for site in range(n_sites):
        targets = orbit_index[representatives ^ np.uint32(1 << site)]
        flip_targets[site] = targets
        np.sqrt(row_sizes / sizes[targets].astype(np.float64), out=flip_amplitudes[site])
        if site % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} single-flip site {site}")

    double_targets = np.empty((required_masks.size, n_orbits), dtype=np.int32)
    for mask_index, mask in enumerate(required_masks):
        double_targets[mask_index] = orbit_index[representatives ^ mask]
        if mask_index % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"{geometry.name} double-flip mask {mask_index}")
    del orbit_index

    checksum = _table_checksum(
        diagonal,
        flip_targets,
        flip_amplitudes,
        required_masks,
        double_targets,
        basis.checksum,
    )
    _atomic_savez(
        path,
        compressed=True,
        diagonal_zz=diagonal,
        flip_targets=flip_targets,
        flip_amplitudes=flip_amplitudes,
        double_flip_masks=required_masks,
        double_flip_targets=double_targets,
        basis_checksum=np.asarray(basis.checksum),
        checksum=np.asarray(checksum),
        schema=np.asarray(TABLE_SCHEMA),
    )
    _LAST_CACHE_STATS[f"{geometry.name}-tables-seconds"] = time.perf_counter() - started
    _guard_rss(f"complete {geometry.name} table construction")
    return HamiltonianTables(
        diagonal_zz=diagonal,
        flip_targets=flip_targets,
        flip_amplitudes=flip_amplitudes,
        double_flip_masks=required_masks,
        double_flip_targets=double_targets,
        basis_checksum=basis.checksum,
        checksum=checksum,
        cache_status="built",
        cache_path=str(path),
    )


def _geometry_for_basis(basis: OrbitBasis) -> _Geometry:
    geometry = _cube_geometry() if basis.geometry_name == "open-3x3x3" else _slab_geometry()
    if not np.array_equal(geometry.coordinates, basis.coordinates):
        raise ValueError("basis coordinates do not match the named geometry")
    return geometry


def build_hamiltonian_tables(basis: OrbitBasis) -> HamiltonianTables:
    """Build or load all cached tables required by the reduced engine.

    The persistent arrays use about 1.9 GB uncompressed for the cube: a
    ``float64`` ZZ diagonal, site-major ``int32`` single-flip indices,
    ``float64`` normalisation factors, and only the double-flip indices used
    by the named observables.  The compressed SHA-stamped ``.npz`` cache is
    checksum-validated on every load and the whole cache directory is held
    below 2.5 GB.  Construction uses a temporary ``int32`` raw-to-orbit map,
    not a raw complex state.  This call also installs the basis/table pair as
    the active context used by the intentionally compact observable API.
    """

    global _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC
    geometry = _geometry_for_basis(basis)
    spec = _observable_spec(basis)
    required_masks = _required_double_masks(basis, spec)
    path = _table_cache_path(geometry, basis, required_masks)
    started = time.perf_counter()
    tables = _load_tables(basis, path, required_masks)
    if tables is None:
        tables = _construct_tables(basis, geometry, path, required_masks)
    _LAST_CACHE_STATS[f"{geometry.name}-tables-status"] = tables.cache_status
    _LAST_CACHE_STATS[f"{geometry.name}-tables-wall-seconds"] = (
        time.perf_counter() - started
    )
    _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC = basis, tables, spec
    return tables


def hamiltonian_apply(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    lam: float,
    psi: npt.NDArray,
) -> npt.NDArray:
    """Return ``H psi`` for ``H=-sum_<ij> Zi Zj-lam sum_i Xi`` (``J=1``).

    The open cube contains exactly 54 nearest-neighbour bonds, asserted when
    its geometry is constructed.  ``diagonal_zz`` is precomputed in
    ``float64``.  The transverse part is a chunked, site-vectorised gather;
    it never stages more than ``n_sites * MATVEC_CHUNK`` coefficients.

    Flip-amplitude derivation: write the invariant raw amplitude on orbit
    ``B`` as ``c_B=psi_B/sqrt(n_B)``.  In output representative row ``A``, a
    site flip gathers ``c_B``.  The normalised output coefficient is the raw
    output multiplied by ``sqrt(n_A)``, hence the contribution is
    ``sqrt(n_A/n_B) psi_B``.  Here ``A`` is the output *target* and ``B`` the
    input *source*, exactly the stored target/source factor.  Summing all 27
    site rows supplies the transition multiplicities.  For example, in a
    two-site swap quotient the two flips from the size-one ``00`` orbit to
    the size-two one-excitation orbit sum to ``sqrt(2)``, as direct Pauli
    algebra requires.  A reciprocal before/after interpretation would fail
    Hermiticity; :func:`dense_slab_crosscheck` tests the assembled matrix and
    random complex inner products to relative ``1e-12``.
    """

    global _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC
    if tables.basis_checksum != basis.checksum:
        raise ValueError("Hamiltonian tables do not belong to this basis")
    if not np.isfinite(lam):
        raise ValueError("lam must be finite")
    vector = np.asarray(psi)
    if vector.ndim != 1 or vector.shape[0] != basis.n_orbits:
        raise ValueError(
            f"psi shape {vector.shape}; expected ({basis.n_orbits},) reduced vector"
        )
    if not np.issubdtype(vector.dtype, np.number):
        raise TypeError("psi must be a numeric array")
    _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC = (
        basis,
        tables,
        _observable_spec(basis),
    )
    _guard_rss("Hamiltonian matvec entry")
    output = tables.diagonal_zz * vector
    for chunk_number, start in enumerate(range(0, basis.n_orbits, MATVEC_CHUNK)):
        stop = min(start + MATVEC_CHUNK, basis.n_orbits)
        targets = tables.flip_targets[:, start:stop]
        gathered = vector[targets]
        transverse = np.sum(
            tables.flip_amplitudes[:, start:stop] * gathered,
            axis=0,
            dtype=np.result_type(vector.dtype, np.float64),
        )
        output[start:stop] -= float(lam) * transverse
        if chunk_number % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"Hamiltonian matvec chunk {chunk_number}")
    _guard_rss("Hamiltonian matvec exit")
    return output


def _reduced_operator(
    basis: OrbitBasis, tables: HamiltonianTables, lam: float, dtype: npt.DTypeLike
) -> LinearOperator:
    def matvec(vector: npt.NDArray) -> npt.NDArray:
        return hamiltonian_apply(basis, tables, lam, np.asarray(vector).reshape(-1))

    return LinearOperator(
        shape=(basis.n_orbits, basis.n_orbits),
        matvec=matvec,
        rmatvec=matvec,
        dtype=np.dtype(dtype),
    )


def _random_hermiticity_residual(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    lam: float,
    seed: int = 20260709,
) -> float:
    rng = np.random.default_rng(seed)
    u = rng.standard_normal(basis.n_orbits) + 1j * rng.standard_normal(
        basis.n_orbits
    )
    v = rng.standard_normal(basis.n_orbits) + 1j * rng.standard_normal(
        basis.n_orbits
    )
    u = np.asarray(u / np.linalg.norm(u), dtype=np.complex128)
    v = np.asarray(v / np.linalg.norm(v), dtype=np.complex128)
    hu = hamiltonian_apply(basis, tables, lam, u)
    hv = hamiltonian_apply(basis, tables, lam, v)
    left = np.vdot(u, hv)
    right = np.vdot(hu, v)
    residual = float(abs(left - right) / max(1.0, abs(left), abs(right)))
    if residual > HERMITICITY_TOL:
        raise AssertionError(
            f"reduced random-vector Hermiticity residual {residual:.3e} > "
            f"{HERMITICITY_TOL:.1e}"
        )
    return residual


def _sparse_hermiticity_residual(
    basis: OrbitBasis, tables: HamiltonianTables, lam: float
) -> float:
    rows = np.broadcast_to(
        np.arange(basis.n_orbits, dtype=np.int32),
        (basis.n_sites, basis.n_orbits),
    ).ravel()
    columns = tables.flip_targets.ravel()
    data = (-float(lam) * tables.flip_amplitudes).ravel()
    transverse = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(basis.n_orbits, basis.n_orbits),
        dtype=np.float64,
    ).tocsr()
    difference = transverse - transverse.T
    residual = 0.0 if difference.nnz == 0 else float(np.max(np.abs(difference.data)))
    if residual > HERMITICITY_TOL:
        raise AssertionError(
            f"assembled sparse Hermiticity residual {residual:.3e} > "
            f"{HERMITICITY_TOL:.1e}"
        )
    return residual


def _ground_state_impl(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    lam: float,
    *,
    report: bool,
) -> tuple[float, ComplexArray, float]:
    operator = _reduced_operator(basis, tables, lam, np.float64)
    rng = np.random.default_rng(271828)
    initial = rng.standard_normal(basis.n_orbits)
    initial /= np.linalg.norm(initial)
    ncv = min(max(4, GROUND_NCV), basis.n_orbits)
    eigenvalues, eigenvectors = eigsh(
        operator,
        k=1,
        which="SA",
        v0=initial,
        tol=GROUND_TOL,
        maxiter=GROUND_MAXITER,
        ncv=ncv,
        return_eigenvectors=True,
    )
    energy = float(eigenvalues[0])
    real_state = np.asarray(eigenvectors[:, 0], dtype=np.float64)
    real_state /= np.linalg.norm(real_state)
    residual = float(
        np.linalg.norm(hamiltonian_apply(basis, tables, lam, real_state) - energy * real_state)
    )
    if residual > 1.0e-8:
        raise RuntimeError(f"ground-state residual {residual:.3e} exceeds 1e-8")
    state = np.asarray(real_state, dtype=np.complex128)
    if report:
        print(f"ground residual: {residual:.3e}")
    return energy, state, residual


def ground_state(
    basis: OrbitBasis, tables: HamiltonianTables, lam: float
) -> tuple[float, ComplexArray]:
    """Compute the lowest eigenpair with matrix-free Lanczos (``eigsh``).

    The real symmetric operator uses ``tol=1e-10``, at most 800 Lanczos
    iterations, and a 12-vector Krylov subspace to bound cube memory.  The
    returned vector is ``complex128`` for direct use by :func:`evolve`; its
    absolute residual is printed and must not exceed ``1e-8``.
    """

    energy, state, _ = _ground_state_impl(basis, tables, lam, report=True)
    return energy, state


def _state_checksum(state: npt.NDArray) -> str:
    return _hash_arrays((("psi", np.asarray(state)),))


def save_checkpoint(
    step: int,
    psi: npt.NDArray,
    *,
    path: Path = CHECKPOINT_PATH,
    basis_checksum: str = "",
    lam: float = math.nan,
    dt: float = math.nan,
    n_steps: int = -1,
    initial_checksum: str = "",
    reference_norm: float = math.nan,
) -> None:
    """Atomically save an evolution checkpoint at the declared cache path."""

    state = np.asarray(psi, dtype=np.complex128)
    checksum = _state_checksum(state)
    _atomic_savez(
        path,
        compressed=False,
        step=np.asarray(step, dtype=np.int64),
        psi=state,
        psi_checksum=np.asarray(checksum),
        basis_checksum=np.asarray(basis_checksum),
        lam=np.asarray(lam, dtype=np.float64),
        dt=np.asarray(dt, dtype=np.float64),
        n_steps=np.asarray(n_steps, dtype=np.int64),
        initial_checksum=np.asarray(initial_checksum),
        reference_norm=np.asarray(reference_norm, dtype=np.float64),
    )


def load_checkpoint(
    path: Path = CHECKPOINT_PATH,
) -> tuple[int, ComplexArray, dict[str, object]]:
    """Load and checksum-validate ``(step, psi)`` plus resume metadata."""

    with np.load(path, allow_pickle=False) as archive:
        step = int(np.asarray(archive["step"]).item())
        state = np.asarray(archive["psi"], dtype=np.complex128)
        stored_checksum = str(np.asarray(archive["psi_checksum"]).item())
        metadata: dict[str, object] = {
            "basis_checksum": str(np.asarray(archive["basis_checksum"]).item()),
            "lam": float(np.asarray(archive["lam"]).item()),
            "dt": float(np.asarray(archive["dt"]).item()),
            "n_steps": int(np.asarray(archive["n_steps"]).item()),
            "initial_checksum": str(
                np.asarray(archive["initial_checksum"]).item()
            ),
            "reference_norm": float(np.asarray(archive["reference_norm"]).item()),
        }
    computed = _state_checksum(state)
    if computed != stored_checksum:
        raise RuntimeError(
            f"checkpoint checksum mismatch: stored {stored_checksum}, computed {computed}"
        )
    if state.ndim != 1 or step < 0:
        raise RuntimeError("checkpoint has invalid step/state shape")
    return step, state, metadata


def _scaled_exponential_operator(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    lam: float,
    scale: complex,
) -> LinearOperator:
    def matvec(vector: npt.NDArray) -> npt.NDArray:
        return scale * hamiltonian_apply(
            basis, tables, lam, np.asarray(vector).reshape(-1)
        )

    def rmatvec(vector: npt.NDArray) -> npt.NDArray:
        return np.conjugate(scale) * hamiltonian_apply(
            basis, tables, lam, np.asarray(vector).reshape(-1)
        )

    return LinearOperator(
        shape=(basis.n_orbits, basis.n_orbits),
        matvec=matvec,
        rmatvec=rmatvec,
        dtype=np.dtype(np.complex128),
    )


def _reduced_hamiltonian_trace(
    basis: OrbitBasis, tables: HamiltonianTables, lam: float
) -> float:
    """Exact trace in the normalised orbit sector (not the raw-space trace)."""

    trace = float(np.sum(tables.diagonal_zz, dtype=np.float64))
    transverse_trace = 0.0
    for start in range(0, basis.n_orbits, MATVEC_CHUNK):
        stop = min(start + MATVEC_CHUNK, basis.n_orbits)
        rows = np.arange(start, stop, dtype=np.int32)
        fixed = tables.flip_targets[:, start:stop] == rows[None, :]
        transverse_trace += float(
            np.sum(
                np.where(fixed, tables.flip_amplitudes[:, start:stop], 0.0),
                dtype=np.float64,
            )
        )
    return trace - float(lam) * transverse_trace


def evolve(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    lam: float,
    psi: npt.NDArray,
    dt: float,
    n_steps: int,
    callback: Callable[[int, ComplexArray], None] | None,
) -> ComplexArray:
    """Evolve by adaptive ``scipy.sparse.linalg.expm_multiply`` steps.

    SciPy's Al-Mohy--Higham adaptive truncated-Taylor exponential action is
    used for each ``exp(-i H dt)`` (the API explicitly permits
    ``expm_multiply``).  Its internal truncation target is double-precision
    roundoff; this engine additionally treats relative norm drift ``1e-9`` as
    a hard claimed-error budget and raises instead of renormalising.  The
    callback receives the initial/resumed step and every completed step, so
    observables can be streamed without retaining a time-by-state array.

    A checksummed checkpoint is written atomically every five steps and at
    completion to :data:`CHECKPOINT_PATH`.  Set environment variable
    ``D3_ENGINE_RESUME=1`` to load it.  Resume validates basis, ``lam``,
    ``dt``, requested step count, and the checksum of the originally supplied
    initial state before accepting ``(step, psi)``.
    """

    if not np.isfinite(dt) or dt == 0.0:
        raise ValueError("dt must be finite and nonzero")
    if int(n_steps) != n_steps or n_steps < 0:
        raise ValueError("n_steps must be a nonnegative integer")
    state = np.asarray(psi, dtype=np.complex128)
    if state.ndim != 1 or state.shape[0] != basis.n_orbits:
        raise ValueError(f"psi must have reduced shape ({basis.n_orbits},)")
    state = state.copy()
    initial_checksum = _state_checksum(state)
    reference_norm = float(np.linalg.norm(state))
    if not np.isfinite(reference_norm) or reference_norm == 0.0:
        raise ValueError("initial state has invalid norm")
    start_step = 0

    if os.environ.get("D3_ENGINE_RESUME", "0") == "1" and CHECKPOINT_PATH.exists():
        saved_step, saved_state, metadata = load_checkpoint(CHECKPOINT_PATH)
        exact_metadata = (
            metadata["basis_checksum"] == basis.checksum
            and float(metadata["lam"]) == float(lam)
            and float(metadata["dt"]) == float(dt)
            and int(metadata["n_steps"]) == int(n_steps)
            and metadata["initial_checksum"] == initial_checksum
            and saved_state.shape == state.shape
        )
        if not exact_metadata:
            raise RuntimeError("checkpoint metadata does not match requested evolution")
        start_step, state = saved_step, saved_state
        reference_norm = float(metadata["reference_norm"])
        if start_step > n_steps:
            raise RuntimeError("checkpoint step exceeds requested n_steps")

    if callback is not None:
        callback(start_step, state)
    exponential = _scaled_exponential_operator(
        basis, tables, lam, complex(0.0, -float(dt))
    )
    exponential_trace = complex(0.0, -float(dt)) * _reduced_hamiltonian_trace(
        basis, tables, lam
    )
    for step in range(start_step + 1, n_steps + 1):
        state = np.asarray(
            expm_multiply(exponential, state, traceA=exponential_trace),
            dtype=np.complex128,
        )
        drift = abs(float(np.linalg.norm(state)) - reference_norm) / reference_norm
        if drift > EVOLVE_NORM_TOL:
            raise RuntimeError(
                f"evolution norm drift {drift:.3e} at step {step} exceeds "
                f"{EVOLVE_NORM_TOL:.1e}"
            )
        if callback is not None:
            callback(step, state)
        if step % CHECKPOINT_EVERY == 0 or step == n_steps:
            save_checkpoint(
                step,
                state,
                basis_checksum=basis.checksum,
                lam=lam,
                dt=dt,
                n_steps=n_steps,
                initial_checksum=initial_checksum,
                reference_norm=reference_norm,
            )
        _guard_rss(f"evolution step {step}")
    return state


_PAULI: dict[str, npt.NDArray[np.complex128]] = {
    "I": np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.complex128),
    "X": np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128),
    "Y": np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128),
    "Z": np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128),
}


def _active_context(
    psi: npt.NDArray,
) -> tuple[OrbitBasis, HamiltonianTables, _ObservableSpec, ComplexArray]:
    if _ACTIVE_BASIS is None or _ACTIVE_TABLES is None or _ACTIVE_SPEC is None:
        raise RuntimeError(
            "no active reduced context; call build_hamiltonian_tables(basis) first"
        )
    state = np.asarray(psi, dtype=np.complex128)
    if state.ndim != 1 or state.shape[0] != _ACTIVE_BASIS.n_orbits:
        raise ValueError(
            f"psi shape {state.shape} does not match active reduced dimension "
            f"{_ACTIVE_BASIS.n_orbits}"
        )
    return _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC, state


def _term_flip_mask(sites: Sequence[int], labels: Sequence[str]) -> int:
    mask = 0
    for site, label in zip(sites, labels, strict=True):
        if label in ("X", "Y"):
            mask ^= 1 << site
        elif label not in ("I", "Z"):
            raise ValueError(f"unknown Pauli label {label!r}")
    return mask


def _output_phase(
    representatives: UIntArray,
    sites: Sequence[int],
    labels: Sequence[str],
) -> ComplexArray:
    """Return ``<output|P|source>`` phases for a Pauli monomial."""

    phase = np.ones(representatives.size, dtype=np.complex128)
    for site, label in zip(sites, labels, strict=True):
        if label in ("Y", "Z"):
            z_value = 1.0 - 2.0 * (
                (representatives >> np.uint32(site)) & np.uint32(1)
            ).astype(np.float64)
            if label == "Y":
                phase *= -1j * z_value
            else:
                phase *= z_value
    return phase


def _double_mask_index(tables: HamiltonianTables, mask: int) -> int:
    index = int(np.searchsorted(tables.double_flip_masks, np.uint32(mask)))
    if index >= tables.double_flip_masks.size or int(tables.double_flip_masks[index]) != mask:
        raise KeyError(
            f"double flip mask 0x{mask:x} was not precomputed for observable toolkit"
        )
    return index


def _expect_reduced(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    psi: ComplexArray,
    sites: Sequence[int],
    labels: Sequence[str],
    *,
    pointer: int | None = None,
    projector_sign: int | None = None,
) -> complex:
    """Expectation of a jointly group-averaged projected Pauli monomial."""

    if (pointer is None) != (projector_sign is None):
        raise ValueError("pointer and projector_sign must be supplied together")
    if projector_sign not in (None, -1, 1):
        raise ValueError("projector_sign must be +1 or -1")
    terms = _operator_orbit(basis, sites, labels, pointer=pointer)
    total = 0.0j
    sizes = basis.orbit_sizes
    for chunk_number, start in enumerate(range(0, basis.n_orbits, OBSERVABLE_CHUNK)):
        stop = min(start + OBSERVABLE_CHUNK, basis.n_orbits)
        reps = basis.representatives[start:stop]
        action = np.zeros(stop - start, dtype=np.complex128)
        for transformed_pointer, transformed_sites, transformed_labels in terms:
            flip_mask = _term_flip_mask(transformed_sites, transformed_labels)
            phase = _output_phase(reps, transformed_sites, transformed_labels)
            if transformed_pointer is not None:
                pointer_z = 1.0 - 2.0 * (
                    (reps >> np.uint32(transformed_pointer)) & np.uint32(1)
                ).astype(np.float64)
                phase *= 0.5 * (1.0 + float(projector_sign) * pointer_z)

            bit_count = flip_mask.bit_count()
            if bit_count == 0:
                contribution = phase * psi[start:stop]
            elif bit_count == 1:
                site = flip_mask.bit_length() - 1
                targets = tables.flip_targets[site, start:stop]
                contribution = (
                    phase
                    * tables.flip_amplitudes[site, start:stop]
                    * psi[targets]
                )
            elif bit_count == 2:
                mask_index = _double_mask_index(tables, flip_mask)
                targets = tables.double_flip_targets[mask_index, start:stop]
                amplitudes = np.sqrt(
                    sizes[start:stop].astype(np.float64)
                    / sizes[targets].astype(np.float64)
                )
                contribution = phase * amplitudes * psi[targets]
            else:
                raise NotImplementedError("observable toolkit supports at most two flips")
            action += contribution
        action /= float(len(terms))
        total += np.vdot(psi[start:stop], action)
        if chunk_number % RSS_CHECK_EVERY_CHUNKS == 0:
            _guard_rss(f"observable contraction chunk {chunk_number}")
    return complex(total)


def _validate_density_matrix(
    matrix: npt.NDArray[np.complex128], label: str
) -> npt.NDArray[np.complex128]:
    global _DENSITY_WORST
    raw = np.asarray(matrix, dtype=np.complex128)
    hermiticity = float(np.max(np.abs(raw - raw.conj().T)))
    trace_error = float(abs(np.trace(raw) - 1.0))
    # Explicit roundoff cleanup only after recording/asserting the raw errors.
    cleaned = 0.5 * (raw + raw.conj().T)
    minimum_eigenvalue = float(np.min(np.linalg.eigvalsh(cleaned)))
    negativity = max(0.0, -minimum_eigenvalue)
    _DENSITY_WORST.hermiticity = max(_DENSITY_WORST.hermiticity, hermiticity)
    _DENSITY_WORST.trace = max(_DENSITY_WORST.trace, trace_error)
    _DENSITY_WORST.negativity = max(_DENSITY_WORST.negativity, negativity)
    worst = max(hermiticity, trace_error, negativity)
    if worst > DENSITY_TOL:
        raise AssertionError(
            f"{label} density matrix invalid: herm={hermiticity:.3e}, "
            f"trace={trace_error:.3e}, negative={negativity:.3e}"
        )
    return cleaned


def density_matrix_diagnostics() -> dict[str, float]:
    """Report worst raw Hermiticity, trace, and PSD violations seen so far."""

    return {
        "hermiticity": _DENSITY_WORST.hermiticity,
        "trace": _DENSITY_WORST.trace,
        "negativity": _DENSITY_WORST.negativity,
    }


def pointer_populations(psi: npt.NDArray) -> tuple[float, float]:
    """Return ``p(Z_S=+1), p(Z_S=-1)`` for the centre pointer.

    The cube centre is fixed by all 24 rotations.  More generally this uses
    the complete joint group average of its projector, which is equal to any
    symmetry-related local value in an invariant state (see the module
    invariant-sector argument).
    """

    basis, tables, spec, state = _active_context(psi)
    plus = _expect_reduced(
        basis,
        tables,
        state,
        (),
        (),
        pointer=spec.pointer,
        projector_sign=1,
    )
    minus = _expect_reduced(
        basis,
        tables,
        state,
        (),
        (),
        pointer=spec.pointer,
        projector_sign=-1,
    )
    if abs(plus.imag) > DENSITY_TOL or abs(minus.imag) > DENSITY_TOL:
        raise AssertionError("pointer probabilities have an imaginary component")
    p_plus, p_minus = float(plus.real), float(minus.real)
    if (
        p_plus < -DENSITY_TOL
        or p_minus < -DENSITY_TOL
        or abs(p_plus + p_minus - 1.0) > DENSITY_TOL
    ):
        raise AssertionError(
            f"invalid pointer populations ({p_plus:.16g}, {p_minus:.16g})"
        )
    return p_plus, p_minus


def _conditional_fragment_state_impl(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    spec: _ObservableSpec,
    state: ComplexArray,
    site_class: str,
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    if site_class not in spec.fragments:
        raise ValueError(
            f"site_class must be one of {tuple(spec.fragments)}, got {site_class!r}"
        )
    fragment = spec.fragments[site_class]
    probabilities = []
    for sign in (1, -1):
        value = _expect_reduced(
            basis,
            tables,
            state,
            (),
            (),
            pointer=spec.pointer,
            projector_sign=sign,
        )
        probabilities.append(float(value.real))
    matrices: list[npt.NDArray[np.complex128]] = []
    for sign, probability in zip((1, -1), probabilities, strict=True):
        if probability <= 1.0e-15:
            raise ValueError(f"Z_S={sign:+d} conditioning probability is zero")
        expectations: dict[str, complex] = {"I": 1.0 + 0.0j}
        for label in ("X", "Y", "Z"):
            numerator = _expect_reduced(
                basis,
                tables,
                state,
                (fragment,),
                (label,),
                pointer=spec.pointer,
                projector_sign=sign,
            )
            expectations[label] = numerator / probability
        matrix = sum(
            expectations[label] * _PAULI[label] for label in ("I", "X", "Y", "Z")
        ) / 2.0
        matrices.append(
            _validate_density_matrix(matrix, f"conditional {site_class} ZS={sign:+d}")
        )
    return matrices[0], matrices[1]


def conditional_fragment_state(
    psi: npt.NDArray, site_class: str
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    """Return fragment ``2x2`` states conditioned on ``Z_S=+1/-1``.

    ``site_class`` is ``'axial'``, ``'edge'``, or ``'corner'``.  The centre
    projector and fragment Pauli are transformed together and averaged over
    the complete rotation orbit.  In the invariant sector that average is
    exactly the value for every member of the named class.  ``I`` and ``Z``
    use diagonal masked sums; ``X`` and ``Y`` use the precomputed single-bit
    gathers with the same ``Z_S`` output mask.  Results are returned in
    ``(+,-)`` order and asserted Hermitian, PSD, and trace one to ``1e-9``.
    """

    basis, tables, spec, state = _active_context(psi)
    return _conditional_fragment_state_impl(
        basis, tables, spec, state, site_class
    )


def _conditional_pair_state_impl(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    spec: _ObservableSpec,
    state: ComplexArray,
    pair_class: str,
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    if pair_class not in spec.pairs:
        raise ValueError(
            f"pair_class must be one of {tuple(spec.pairs)}, got {pair_class!r}"
        )
    pair = spec.pairs[pair_class]
    matrices: list[npt.NDArray[np.complex128]] = []
    for sign in (1, -1):
        probability = float(
            _expect_reduced(
                basis,
                tables,
                state,
                (),
                (),
                pointer=spec.pointer,
                projector_sign=sign,
            ).real
        )
        if probability <= 1.0e-15:
            raise ValueError(f"Z_S={sign:+d} conditioning probability is zero")
        matrix = np.zeros((4, 4), dtype=np.complex128)
        for first_label in ("I", "X", "Y", "Z"):
            for second_label in ("I", "X", "Y", "Z"):
                if first_label == second_label == "I":
                    expectation = 1.0 + 0.0j
                else:
                    expectation = _expect_reduced(
                        basis,
                        tables,
                        state,
                        pair,
                        (first_label, second_label),
                        pointer=spec.pointer,
                        projector_sign=sign,
                    ) / probability
                matrix += expectation * np.kron(
                    _PAULI[first_label], _PAULI[second_label]
                )
        matrices.append(
            _validate_density_matrix(
                matrix / 4.0, f"conditional {pair_class} ZS={sign:+d}"
            )
        )
    return matrices[0], matrices[1]


def conditional_pair_state(
    psi: npt.NDArray, pair_class: str
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    """Return conditional ``4x4`` states for the two axial pair classes.

    Accepted classes are ``'opposite-axis'`` and ``'orthogonal-axis'``.  All
    16 two-site Pauli coefficients are contracted under ``P_(Z_S=s)``;
    terms with two off-diagonal Paulis use the precomputed double-flip
    gathers.  Pointer and ordered pair are averaged jointly over proper
    rotations, which equals each physical pair value in the invariant
    sector.  The ``(+,-)`` matrices are PSD/Hermitian/trace-one asserted to
    ``1e-9`` and use computational order ``|00>,|01>,|10>,|11>``.
    """

    basis, tables, spec, state = _active_context(psi)
    return _conditional_pair_state_impl(basis, tables, spec, state, pair_class)


def _center_bond_state_impl(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    spec: _ObservableSpec,
    state: ComplexArray,
) -> npt.NDArray[np.complex128]:
    matrix = np.zeros((4, 4), dtype=np.complex128)
    for first_label in ("I", "X", "Y", "Z"):
        for second_label in ("I", "X", "Y", "Z"):
            if first_label == second_label == "I":
                expectation = 1.0 + 0.0j
            else:
                expectation = _expect_reduced(
                    basis,
                    tables,
                    state,
                    spec.center_bond,
                    (first_label, second_label),
                )
            matrix += expectation * np.kron(
                _PAULI[first_label], _PAULI[second_label]
            )
    return _validate_density_matrix(matrix / 4.0, "centre-axial bond")


def center_bond_state(psi: npt.NDArray) -> npt.NDArray[np.complex128]:
    """Return the rotation-averaged ``4x4`` state of ``(S, axial neighbor)``.

    The ordered centre bond is averaged over all six axial directions.  By
    the invariant-sector argument this equals every individual centre bond,
    while directly supplying the memo's unrescaled two-site purity input.
    The site order is ``(S,F)`` and the result is density-validated to
    ``1e-9``.
    """

    basis, tables, spec, state = _active_context(psi)
    return _center_bond_state_impl(basis, tables, spec, state)


def site_class_table() -> dict[str, tuple[tuple[int, int, int], ...]]:
    """Return the four proper-cubic site classes in memo coordinates.

    The result has centre (1), face/axial (6), edge (12), and corner (8)
    entries.  Coordinates follow the module's lexicographic little-endian
    bit-site order, with the last coordinate varying fastest.
    """

    classes: dict[str, list[tuple[int, int, int]]] = {
        "center": [],
        "axial": [],
        "edge": [],
        "corner": [],
    }
    for coordinate in itertools.product((-1, 0, 1), repeat=3):
        nonzero = sum(value != 0 for value in coordinate)
        name = ("center", "axial", "edge", "corner")[nonzero]
        classes[name].append(coordinate)
    result = {name: tuple(values) for name, values in classes.items()}
    expected = {"center": 1, "axial": 6, "edge": 12, "corner": 8}
    if {name: len(values) for name, values in result.items()} != expected:
        raise AssertionError("site-class cardinalities are not 1/6/12/8")
    return result


def _popcount_uint32(values: UIntArray) -> npt.NDArray[np.uint8]:
    byte_counts = np.asarray([int(value).bit_count() for value in range(256)], dtype=np.uint8)
    return (
        byte_counts[values & np.uint32(255)]
        + byte_counts[(values >> np.uint32(8)) & np.uint32(255)]
        + byte_counts[(values >> np.uint32(16)) & np.uint32(255)]
        + byte_counts[(values >> np.uint32(24)) & np.uint32(255)]
    ).astype(np.uint8, copy=False)


def _off_axis_qubit() -> tuple[complex, complex]:
    """Qubit amplitudes with Bloch vector ``(1,1,1)/sqrt(3)``."""

    component = 1.0 / math.sqrt(3.0)
    zero = math.sqrt((1.0 + component) / 2.0)
    one = complex(component, component) / math.sqrt(2.0 * (1.0 + component))
    if abs(abs(zero) ** 2 + abs(one) ** 2 - 1.0) > 1.0e-15:
        raise AssertionError("off-axis one-qubit state is not normalised")
    return complex(zero), one


def _reduced_product_state(basis: OrbitBasis) -> ComplexArray:
    zero, one = _off_axis_qubit()
    populations = _popcount_uint32(basis.representatives).astype(np.int16)
    raw = np.power(zero, basis.n_sites - populations) * np.power(one, populations)
    state = np.sqrt(basis.orbit_sizes.astype(np.float64)) * raw
    state = np.asarray(state, dtype=np.complex128)
    norm = float(np.linalg.norm(state))
    if abs(norm - 1.0) > 1.0e-10:
        raise AssertionError("reduced product state is not normalised")
    # A 5.6-million-term BLAS reduction accumulates ~1e-12 roundoff.  Apply
    # one declared scalar normalisation, never an orbit-dependent correction.
    state /= norm
    return state


def _dense_product_state(n_sites: int) -> ComplexArray:
    if n_sites > 18:
        raise RuntimeError(
            "raw complex product states are restricted to the 18-qubit validation slab"
        )
    zero, one = _off_axis_qubit()
    state = np.ones(1, dtype=np.complex128)
    for _ in range(n_sites):  # only 18 tensor factors; amplitudes vectorised
        state = np.concatenate((zero * state, one * state))
    norm = float(np.linalg.norm(state))
    if state.shape != (1 << n_sites,) or abs(norm - 1.0) > 1.0e-10:
        raise AssertionError("dense product-state construction failed")
    state /= norm
    return state


@dataclass(frozen=True)
class _DenseSlabTables:
    diagonal_zz: FloatArray
    flip_targets: npt.NDArray[np.int32]
    indices: UIntArray


def _build_dense_slab_tables(geometry: _Geometry) -> _DenseSlabTables:
    if geometry.n_sites != 18:
        raise RuntimeError("dense machinery is restricted to the 18-qubit slab")
    dimension = 1 << geometry.n_sites
    indices = np.arange(dimension, dtype=np.uint32)
    left = geometry.bonds[:, 0].astype(np.uint32)
    right = geometry.bonds[:, 1].astype(np.uint32)
    disagreements = (
        ((indices[None, :] >> left[:, None]) ^ (indices[None, :] >> right[:, None]))
        & np.uint32(1)
    )
    diagonal = -float(geometry.expected_bonds) + 2.0 * np.sum(
        disagreements, axis=0, dtype=np.int16
    )
    diagonal = np.asarray(diagonal, dtype=np.float64)
    site_bits = (np.uint32(1) << np.arange(geometry.n_sites, dtype=np.uint32))[
        :, None
    ]
    flip_targets = np.asarray(indices[None, :] ^ site_bits, dtype=np.int32)
    _guard_rss("dense slab table construction", VALIDATION_BUDGET_GB)
    return _DenseSlabTables(diagonal, flip_targets, indices)


def _dense_hamiltonian_apply(
    tables: _DenseSlabTables, lam: float, vector: npt.NDArray
) -> npt.NDArray:
    state = np.asarray(vector).reshape(-1)
    if state.shape != tables.diagonal_zz.shape:
        raise ValueError("dense slab vector has wrong shape")
    output = tables.diagonal_zz * state
    for start in range(0, state.size, MATVEC_CHUNK):
        stop = min(start + MATVEC_CHUNK, state.size)
        output[start:stop] -= float(lam) * np.sum(
            state[tables.flip_targets[:, start:stop]],
            axis=0,
            dtype=np.result_type(state.dtype, np.float64),
        )
    return output


def _dense_operator(
    tables: _DenseSlabTables, lam: float, dtype: npt.DTypeLike
) -> LinearOperator:
    dimension = tables.diagonal_zz.size

    def matvec(vector: npt.NDArray) -> npt.NDArray:
        return _dense_hamiltonian_apply(tables, lam, vector)

    return LinearOperator(
        (dimension, dimension), matvec=matvec, rmatvec=matvec, dtype=np.dtype(dtype)
    )


def _dense_random_hermiticity_residual(
    tables: _DenseSlabTables, lam: float, seed: int = 20260709
) -> float:
    rng = np.random.default_rng(seed)
    dimension = tables.diagonal_zz.size
    u = rng.standard_normal(dimension) + 1j * rng.standard_normal(dimension)
    v = rng.standard_normal(dimension) + 1j * rng.standard_normal(dimension)
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    hu = _dense_hamiltonian_apply(tables, lam, u)
    hv = _dense_hamiltonian_apply(tables, lam, v)
    left, right = np.vdot(u, hv), np.vdot(hu, v)
    residual = float(abs(left - right) / max(1.0, abs(left), abs(right)))
    if residual > HERMITICITY_TOL:
        raise AssertionError(
            f"dense random Hermiticity residual {residual:.3e} > {HERMITICITY_TOL:.1e}"
        )
    return residual


def _dense_ground_state(
    tables: _DenseSlabTables, lam: float
) -> tuple[float, ComplexArray, float]:
    operator = _dense_operator(tables, lam, np.float64)
    rng = np.random.default_rng(271828)
    initial = rng.standard_normal(tables.diagonal_zz.size)
    initial /= np.linalg.norm(initial)
    eigenvalues, eigenvectors = eigsh(
        operator,
        k=1,
        which="SA",
        v0=initial,
        tol=GROUND_TOL,
        maxiter=GROUND_MAXITER,
        ncv=GROUND_NCV,
    )
    energy = float(eigenvalues[0])
    state = np.asarray(eigenvectors[:, 0], dtype=np.float64)
    state /= np.linalg.norm(state)
    residual = float(
        np.linalg.norm(_dense_hamiltonian_apply(tables, lam, state) - energy * state)
    )
    if residual > 1.0e-8:
        raise RuntimeError(f"dense ground residual {residual:.3e} exceeds 1e-8")
    return energy, np.asarray(state, dtype=np.complex128), residual


def _dense_exponential_operator(
    tables: _DenseSlabTables, lam: float, scale: complex
) -> LinearOperator:
    dimension = tables.diagonal_zz.size

    def matvec(vector: npt.NDArray) -> npt.NDArray:
        return scale * _dense_hamiltonian_apply(tables, lam, vector)

    def rmatvec(vector: npt.NDArray) -> npt.NDArray:
        return np.conjugate(scale) * _dense_hamiltonian_apply(tables, lam, vector)

    return LinearOperator(
        (dimension, dimension),
        matvec=matvec,
        rmatvec=rmatvec,
        dtype=np.dtype(np.complex128),
    )


def _expect_dense(
    basis: OrbitBasis,
    tables: _DenseSlabTables,
    psi: ComplexArray,
    sites: Sequence[int],
    labels: Sequence[str],
    *,
    pointer: int | None = None,
    projector_sign: int | None = None,
) -> complex:
    """Direct raw-basis Pauli algebra, explicitly averaged over slab D4."""

    if (pointer is None) != (projector_sign is None):
        raise ValueError("pointer and projector sign must be supplied together")
    terms = _operator_orbit(basis, sites, labels, pointer=pointer)
    total = 0.0j
    indices = tables.indices
    for transformed_pointer, transformed_sites, transformed_labels in terms:
        flip_mask = _term_flip_mask(transformed_sites, transformed_labels)
        source = indices ^ np.uint32(flip_mask)
        # Independent direct Pauli algebra: use literal matrix elements
        # <output_bit|sigma|source_bit>, not the reduced path's phase helper.
        phase = np.ones(indices.size, dtype=np.complex128)
        for site, label in zip(
            transformed_sites, transformed_labels, strict=True
        ):
            output_bit = ((indices >> np.uint32(site)) & np.uint32(1)).astype(
                np.int8
            )
            source_bit = ((source >> np.uint32(site)) & np.uint32(1)).astype(
                np.int8
            )
            phase *= _PAULI[label][output_bit, source_bit]
        if transformed_pointer is not None:
            pointer_z = 1.0 - 2.0 * (
                (indices >> np.uint32(transformed_pointer)) & np.uint32(1)
            ).astype(np.float64)
            phase *= 0.5 * (1.0 + float(projector_sign) * pointer_z)
        total += np.vdot(psi, phase * psi[source])
    return complex(total / float(len(terms)))


def _dense_partial_trace(
    psi: ComplexArray,
    n_sites: int,
    selected_sites: Sequence[int],
    *,
    conditioned_site: int | None = None,
    conditioned_bit: int | None = None,
) -> tuple[float, npt.NDArray[np.complex128]]:
    """Independent raw tensor partial trace in the requested site order."""

    if psi.shape != (1 << n_sites,):
        raise ValueError("raw state shape does not match n_sites")
    if (conditioned_site is None) != (conditioned_bit is None):
        raise ValueError("conditioned site and bit must be supplied together")
    if conditioned_bit not in (None, 0, 1):
        raise ValueError("conditioned bit must be zero or one")
    if conditioned_site is not None and conditioned_site in selected_sites:
        raise ValueError("conditioned site cannot also be a selected output site")

    # C-order tensor axis n-1-i corresponds to little-endian bit/site i.
    selected_axes = [n_sites - 1 - site for site in selected_sites]
    condition_axes = (
        [] if conditioned_site is None else [n_sites - 1 - conditioned_site]
    )
    leading = condition_axes + selected_axes
    remainder = [axis for axis in range(n_sites) if axis not in leading]
    tensor = np.transpose(psi.reshape((2,) * n_sites), leading + remainder)
    if conditioned_site is not None:
        tensor = tensor[int(conditioned_bit)]
    subsystem_dimension = 1 << len(selected_sites)
    amplitudes = tensor.reshape(subsystem_dimension, -1)
    matrix = amplitudes @ amplitudes.conj().T
    probability = float(np.trace(matrix).real)
    if probability <= 1.0e-15:
        raise ValueError("direct conditioning probability vanished")
    return probability, np.asarray(matrix / probability, dtype=np.complex128)


def _dense_snapshot_direct(
    basis: OrbitBasis,
    spec: _ObservableSpec,
    psi: ComplexArray,
) -> dict[str, object]:
    """Raw-state observable snapshot by independent tensor partial traces."""

    pointer_probabilities = []
    for bit in (0, 1):
        probability, scalar_state = _dense_partial_trace(
            psi,
            basis.n_sites,
            (),
            conditioned_site=spec.pointer,
            conditioned_bit=bit,
        )
        if abs(scalar_state[0, 0] - 1.0) > DENSITY_TOL:
            raise AssertionError("conditioned scalar state is not one")
        pointer_probabilities.append(probability)

    fragments: dict[str, npt.NDArray[np.complex128]] = {}
    for class_name, site in spec.fragments.items():
        states = []
        for bit, sign in ((0, 1), (1, -1)):
            _, matrix = _dense_partial_trace(
                psi,
                basis.n_sites,
                (site,),
                conditioned_site=spec.pointer,
                conditioned_bit=bit,
            )
            states.append(
                _validate_density_matrix(
                    matrix, f"direct fragment {class_name} {sign:+d}"
                )
            )
        fragments[class_name] = np.stack(states)

    pairs: dict[str, npt.NDArray[np.complex128]] = {}
    for class_name, pair in spec.pairs.items():
        states = []
        for bit, sign in ((0, 1), (1, -1)):
            _, matrix = _dense_partial_trace(
                psi,
                basis.n_sites,
                pair,
                conditioned_site=spec.pointer,
                conditioned_bit=bit,
            )
            states.append(
                _validate_density_matrix(matrix, f"direct pair {class_name} {sign:+d}")
            )
        pairs[class_name] = np.stack(states)

    _, bond = _dense_partial_trace(
        psi, basis.n_sites, spec.center_bond
    )
    return {
        "pointer": np.asarray(pointer_probabilities, dtype=np.float64),
        "fragment": fragments,
        "pair": pairs,
        "center_bond": _validate_density_matrix(bond, "direct centre bond"),
    }


def _snapshot_from_expectation(
    spec: _ObservableSpec,
    expect: Callable[..., complex],
) -> dict[str, object]:
    probabilities = np.asarray(
        [
            expect((), (), pointer=spec.pointer, projector_sign=sign).real
            for sign in (1, -1)
        ],
        dtype=np.float64,
    )
    if np.any(probabilities <= 1.0e-15):
        raise AssertionError("validation conditioning probability vanished")

    fragments: dict[str, npt.NDArray[np.complex128]] = {}
    for class_name, site in spec.fragments.items():
        conditioned = []
        for sign, probability in zip((1, -1), probabilities, strict=True):
            matrix = _PAULI["I"].copy()
            for label in ("X", "Y", "Z"):
                coefficient = expect(
                    (site,),
                    (label,),
                    pointer=spec.pointer,
                    projector_sign=sign,
                ) / float(probability)
                matrix += coefficient * _PAULI[label]
            conditioned.append(
                _validate_density_matrix(
                    matrix / 2.0, f"validation fragment {class_name} {sign:+d}"
                )
            )
        fragments[class_name] = np.stack(conditioned)

    pairs: dict[str, npt.NDArray[np.complex128]] = {}
    for class_name, pair in spec.pairs.items():
        conditioned = []
        for sign, probability in zip((1, -1), probabilities, strict=True):
            matrix = np.zeros((4, 4), dtype=np.complex128)
            for first_label in ("I", "X", "Y", "Z"):
                for second_label in ("I", "X", "Y", "Z"):
                    coefficient = (
                        1.0 + 0.0j
                        if first_label == second_label == "I"
                        else expect(
                            pair,
                            (first_label, second_label),
                            pointer=spec.pointer,
                            projector_sign=sign,
                        )
                        / float(probability)
                    )
                    matrix += coefficient * np.kron(
                        _PAULI[first_label], _PAULI[second_label]
                    )
            conditioned.append(
                _validate_density_matrix(
                    matrix / 4.0, f"validation pair {class_name} {sign:+d}"
                )
            )
        pairs[class_name] = np.stack(conditioned)

    bond = np.zeros((4, 4), dtype=np.complex128)
    for first_label in ("I", "X", "Y", "Z"):
        for second_label in ("I", "X", "Y", "Z"):
            coefficient = (
                1.0 + 0.0j
                if first_label == second_label == "I"
                else expect(spec.center_bond, (first_label, second_label))
            )
            bond += coefficient * np.kron(
                _PAULI[first_label], _PAULI[second_label]
            )
    return {
        "pointer": probabilities,
        "fragment": fragments,
        "pair": pairs,
        "center_bond": _validate_density_matrix(
            bond / 4.0, "validation centre bond"
        ),
    }


def _reduced_snapshot(
    basis: OrbitBasis,
    tables: HamiltonianTables,
    spec: _ObservableSpec,
    psi: ComplexArray,
) -> dict[str, object]:
    # Exercise the exact public observable entry points in validation, not a
    # parallel reconstruction that could agree while the exposed API drifts.
    global _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC
    _ACTIVE_BASIS, _ACTIVE_TABLES, _ACTIVE_SPEC = basis, tables, spec
    fragments = {
        class_name: np.stack(conditional_fragment_state(psi, class_name))
        for class_name in spec.fragments
    }
    pairs = {
        class_name: np.stack(conditional_pair_state(psi, class_name))
        for class_name in spec.pairs
    }
    return {
        "pointer": np.asarray(pointer_populations(psi), dtype=np.float64),
        "fragment": fragments,
        "pair": pairs,
        "center_bond": center_bond_state(psi),
    }


def _dense_snapshot(
    basis: OrbitBasis,
    tables: _DenseSlabTables,
    spec: _ObservableSpec,
    psi: ComplexArray,
) -> dict[str, object]:
    return _snapshot_from_expectation(
        spec,
        lambda sites, labels, **kwargs: _expect_dense(
            basis, tables, psi, sites, labels, **kwargs
        ),
    )


def _snapshot_deviations(
    dense: Mapping[str, object], reduced: Mapping[str, object]
) -> dict[str, float]:
    deviations = {
        "pointer": float(
            np.max(
                np.abs(
                    np.asarray(dense["pointer"], dtype=np.float64)
                    - np.asarray(reduced["pointer"], dtype=np.float64)
                )
            )
        ),
        "fragment": 0.0,
        "pair": 0.0,
        "center_bond": float(
            np.max(
                np.abs(
                    np.asarray(dense["center_bond"])
                    - np.asarray(reduced["center_bond"])
                )
            )
        ),
    }
    for family in ("fragment", "pair"):
        dense_family = dense[family]
        reduced_family = reduced[family]
        if not isinstance(dense_family, Mapping) or not isinstance(
            reduced_family, Mapping
        ):
            raise TypeError("snapshot family is not a mapping")
        deviations[family] = max(
            float(np.max(np.abs(np.asarray(dense_family[key]) - reduced_family[key])))
            for key in dense_family
        )
    return deviations


def _entropy_bits(matrix: npt.NDArray[np.complex128]) -> float:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    eigenvalues = eigenvalues[eigenvalues > 1.0e-15]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def _partial_traces_two_qubit(
    matrix: npt.NDArray[np.complex128],
) -> tuple[npt.NDArray[np.complex128], npt.NDArray[np.complex128]]:
    tensor = np.asarray(matrix).reshape(2, 2, 2, 2)
    first = np.trace(tensor, axis1=1, axis2=3)
    second = np.trace(tensor, axis1=0, axis2=2)
    return first, second


def _zero_intersite_information(snapshot: Mapping[str, object]) -> float:
    probabilities = np.asarray(snapshot["pointer"], dtype=np.float64)
    worst = 0.0
    fragments = snapshot["fragment"]
    pairs = snapshot["pair"]
    if not isinstance(fragments, Mapping) or not isinstance(pairs, Mapping):
        raise TypeError("snapshot families are malformed")
    for conditioned in fragments.values():
        states = np.asarray(conditioned)
        average = probabilities[0] * states[0] + probabilities[1] * states[1]
        holevo = _entropy_bits(average) - sum(
            probabilities[index] * _entropy_bits(states[index]) for index in range(2)
        )
        worst = max(worst, abs(float(holevo)))
    for conditioned in pairs.values():
        states = np.asarray(conditioned)
        conditional_mutual_information = 0.0
        for index in range(2):
            first, second = _partial_traces_two_qubit(states[index])
            mutual_information = (
                _entropy_bits(first)
                + _entropy_bits(second)
                - _entropy_bits(states[index])
            )
            conditional_mutual_information += probabilities[index] * mutual_information
        worst = max(worst, abs(float(conditional_mutual_information)))
    return worst


def _evolution_sequence(
    operator: LinearOperator, state: ComplexArray, trace_a: complex
) -> npt.NDArray[np.complex128]:
    # Exactly the validation grid t=0:0.1:2.  Supplying the exact trace avoids
    # SciPy's stochastic LinearOperator trace estimate.  The reduced-sector
    # trace is generally nonzero even though each raw-space Pauli is traceless.
    return np.asarray(
        expm_multiply(
            operator,
            state,
            start=0.0,
            stop=2.0,
            num=21,
            endpoint=True,
            traceA=trace_a,
        ),
        dtype=np.complex128,
    )


def dense_slab_crosscheck() -> dict[str, object]:
    """Validate every exposed observable on the open ``3 x 3 x 2`` slab.

    The slab's proper spatial symmetry group is the orientation-preserving
    square-prism group ``D4`` of order 8: four rotations around the thin axis
    and four pi rotations about in-plane axes/diagonals (the latter exchange
    layers).  The same Hamiltonian is built twice: direct Pauli algebra on all
    ``2^18`` configurations and the independently enumerated 33,168-orbit
    basis of this group.  The dense Hamiltonian uses literal ``Z`` phases and
    ``X`` bit gathers; dense local states come from raw tensor partial traces.
    At ``t=0`` a second reconstruction from literal Pauli-matrix elements is
    required to agree with those partial traces to ``1e-12``, keeping the
    dense reference independent of the reduced phase and reconstruction path.

    Both representations evolve the uniform Bloch ``(1,1,1)/sqrt(3)``
    product state at ``lambda=0.1`` on ``t=0:0.1:2``.  At every one of the 21
    samples this compares pointer populations, all three conditional
    one-qubit class states, both conditional axial-pair states, and the centre
    bond state to ``1e-9``.  It also checks dense/reduced ground energies,
    assembled and random-vector Hermiticity, norm conservation, density-
    matrix validity, and zero initial pointer Holevo/conditional pair mutual
    information.  The routine stays below 4 GiB and returns diagnostics
    without printing; the module main formats at most eight lines.
    """

    global _DENSITY_WORST
    _DENSITY_WORST = _DensityDiagnostics()
    started = time.perf_counter()
    lam = 0.1
    classes = site_class_table()
    if tuple(map(len, classes.values())) != (1, 6, 12, 8):
        raise AssertionError("public cube site-class table failed validation")
    geometry = _slab_geometry()
    burnside_count = _burnside_orbit_count(geometry)
    if burnside_count != 33_168:
        raise AssertionError(f"slab Burnside orbit count {burnside_count}, expected 33168")
    basis = _build_basis_for_geometry(geometry)
    tables = build_hamiltonian_tables(basis)
    dense_tables = _build_dense_slab_tables(geometry)
    spec = _observable_spec(basis)

    sparse_hermiticity = _sparse_hermiticity_residual(basis, tables, lam)
    reduced_random_hermiticity = _random_hermiticity_residual(
        basis, tables, lam
    )
    dense_random_hermiticity = _dense_random_hermiticity_residual(
        dense_tables, lam
    )

    reduced_energy, _, reduced_ground_residual = _ground_state_impl(
        basis, tables, lam, report=False
    )
    dense_energy, _, dense_ground_residual = _dense_ground_state(dense_tables, lam)
    ground_energy_deviation = abs(reduced_energy - dense_energy)
    if ground_energy_deviation > 1.0e-9:
        raise AssertionError(
            f"slab ground energies differ by {ground_energy_deviation:.3e}"
        )

    reduced_initial = _reduced_product_state(basis)
    dense_initial = _dense_product_state(geometry.n_sites)
    reduced_generator = _scaled_exponential_operator(
        basis, tables, lam, complex(0.0, -1.0)
    )
    dense_generator = _dense_exponential_operator(
        dense_tables, lam, complex(0.0, -1.0)
    )
    reduced_trace = _evolution_sequence(
        reduced_generator,
        reduced_initial,
        complex(0.0, -1.0) * _reduced_hamiltonian_trace(basis, tables, lam),
    )
    dense_trace = _evolution_sequence(dense_generator, dense_initial, 0.0j)
    if reduced_trace.shape != (21, basis.n_orbits) or dense_trace.shape != (
        21,
        1 << geometry.n_sites,
    ):
        raise AssertionError("evolution sequence returned an unexpected shape")

    reduced_norm_drift = float(
        np.max(np.abs(np.linalg.norm(reduced_trace, axis=1) - 1.0))
    )
    dense_norm_drift = float(
        np.max(np.abs(np.linalg.norm(dense_trace, axis=1) - 1.0))
    )
    if max(reduced_norm_drift, dense_norm_drift) > EVOLVE_NORM_TOL:
        raise AssertionError(
            f"slab norm drift dense={dense_norm_drift:.3e}, "
            f"reduced={reduced_norm_drift:.3e}"
        )

    maximum_deviations = {
        "pointer": 0.0,
        "fragment": 0.0,
        "pair": 0.0,
        "center_bond": 0.0,
    }
    t0_information = 0.0
    direct_pauli_deviation = 0.0
    for sample in range(21):
        dense_snapshot = _dense_snapshot_direct(basis, spec, dense_trace[sample])
        reduced_snapshot = _reduced_snapshot(
            basis, tables, spec, reduced_trace[sample]
        )
        deviations = _snapshot_deviations(dense_snapshot, reduced_snapshot)
        for family, deviation in deviations.items():
            maximum_deviations[family] = max(
                maximum_deviations[family], deviation
            )
        if sample == 0:
            direct_pauli_snapshot = _dense_snapshot(
                basis, dense_tables, spec, dense_trace[sample]
            )
            direct_pauli_deviation = max(
                _snapshot_deviations(
                    dense_snapshot, direct_pauli_snapshot
                ).values()
            )
            t0_information = max(
                _zero_intersite_information(dense_snapshot),
                _zero_intersite_information(reduced_snapshot),
            )
        _guard_rss(f"slab observable sample {sample}", VALIDATION_BUDGET_GB)

    worst_observable = max(maximum_deviations.values())
    if worst_observable > 1.0e-9:
        raise AssertionError(
            f"slab exposed-observable deviation {worst_observable:.3e} exceeds 1e-9"
        )
    if t0_information > 1.0e-9:
        raise AssertionError(
            f"slab t=0 intersite information {t0_information:.3e} exceeds 1e-9"
        )
    if direct_pauli_deviation > 1.0e-12:
        raise AssertionError(
            f"direct Pauli and tensor partial traces differ by "
            f"{direct_pauli_deviation:.3e}"
        )
    density = density_matrix_diagnostics()
    if max(density.values()) > DENSITY_TOL:
        raise AssertionError(f"density diagnostics exceeded tolerance: {density}")
    _guard_rss("complete slab validation", VALIDATION_BUDGET_GB)
    return {
        "slab_orbits": burnside_count,
        "basis_status": basis.cache_status,
        "tables_status": tables.cache_status,
        "elapsed_seconds": time.perf_counter() - started,
        "cache_bytes": _cache_size_bytes(),
        "sparse_hermiticity": sparse_hermiticity,
        "reduced_random_hermiticity": reduced_random_hermiticity,
        "dense_random_hermiticity": dense_random_hermiticity,
        "ground_energy_deviation": ground_energy_deviation,
        "reduced_ground_residual": reduced_ground_residual,
        "dense_ground_residual": dense_ground_residual,
        "maximum_deviations": maximum_deviations,
        "reduced_norm_drift": reduced_norm_drift,
        "dense_norm_drift": dense_norm_drift,
        "t0_information": t0_information,
        "direct_pauli_deviation": direct_pauli_deviation,
        "density_worst": max(density.values()),
        "rss_peak_gb": rss_gb(),
    }


def _main() -> int:
    cube_count = -1
    try:
        cube = _cube_geometry()
        cube_count = _burnside_orbit_count(cube)
        count_ok = cube_count == EXPECTED_CUBE_ORBITS
        print(
            f"orbit-count: cube={cube_count} expected={EXPECTED_CUBE_ORBITS} "
            f"group={cube.permutations.shape[0]} {'OK' if count_ok else 'MISMATCH'}"
        )
        if not count_ok:
            raise AssertionError(
                f"computed cube count {cube_count}; refusing to adjust declared count"
            )
        result = dense_slab_crosscheck()
        deviations = result["maximum_deviations"]
        if not isinstance(deviations, Mapping):
            raise TypeError("validation deviations are malformed")
        print(
            "tables: "
            f"slab-basis={result['basis_status']} slab-H={result['tables_status']} "
            f"group=D4/{EXPECTED_SLAB_GROUP_ORDER} orbits={result['slab_orbits']} "
            f"cache={result['cache_bytes']/2**20:.1f}MiB "
            f"wall={result['elapsed_seconds']:.1f}s"
        )
        print(
            "Hermiticity: "
            f"sparse={result['sparse_hermiticity']:.2e} "
            f"random-red={result['reduced_random_hermiticity']:.2e} "
            f"random-dense={result['dense_random_hermiticity']:.2e} "
            f"GS-dE={result['ground_energy_deviation']:.2e} "
            f"GS-res={max(result['reduced_ground_residual'], result['dense_ground_residual']):.2e}"
        )
        print(
            "slab-maxdev: "
            f"pointer={deviations['pointer']:.2e} "
            f"fragment={deviations['fragment']:.2e} "
            f"pair={deviations['pair']:.2e} "
            f"center-bond={deviations['center_bond']:.2e} "
            f"direct-P={result['direct_pauli_deviation']:.2e}"
        )
        print(
            "norm/info: "
            f"dense={result['dense_norm_drift']:.2e} "
            f"reduced={result['reduced_norm_drift']:.2e} "
            f"t0-chi={result['t0_information']:.2e} "
            f"rho-worst={result['density_worst']:.2e}"
        )
        print(
            f"RSS peak: {result['rss_peak_gb']:.3f} GiB "
            f"(guard={BUDGET_GB:.1f}, validation-cap={VALIDATION_BUDGET_GB:.1f})"
        )
        print("TOTAL: ENGINE-VALID")
        return 0
    except Exception as exc:
        message = " ".join(str(exc).splitlines())
        if cube_count < 0:
            print(
                f"orbit-count: cube={cube_count} expected={EXPECTED_CUBE_ORBITS} "
                "group=unknown MISMATCH"
            )
        print(f"failure: {type(exc).__name__}: {message}")
        print("TOTAL: MACHINERY-FAIL")
        return 2


if __name__ == "__main__":
    raise SystemExit(_main())
