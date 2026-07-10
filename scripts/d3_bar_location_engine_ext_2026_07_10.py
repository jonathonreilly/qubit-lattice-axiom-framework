#!/usr/bin/env python3
"""Frozen engine extensions for the d=3 bar-location measurement.

This module extends, but does not modify, the validated
``d3_cubic_orbit_engine_2026_07_09`` machinery.  It supplies the seven paths
commissioned by ``D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md``:

1. class-uniform product preparation;
2. one per-process raw-configuration-to-orbit lookup;
3. arbitrary ordered ``k <= 5`` pointer-conditional fragment marginals;
4. ordered ``(S,F_a,F_b)`` joint marginals and conditional mutual information;
5. frozen route-C descriptors and explicit 24-rotation verification;
6. the two lowest orthonormal invariant-sector Lanczos states; and
7. independent dense-slab validation of every new numerical path.

No routine constructs a ``2^27`` complex state.  Cube marginals are formed
by chunked raw-amplitude gathers and BLAS ``M M^dagger`` products.  The sole
``2^27`` object is the required transient-in-process ``int32`` lookup; it is
never persisted.

SPEC-NOTE (single-subset gather versus observer wording): the frozen memo
describes every declared operator through its complete proper-rotation
average, while the binding implementation note observes that an exactly
invariant-sector state gives the same density matrix from one declared
subset.  This implementation uses the latter gather identity and exposes
the memo's redundant closed-five/wedge-four reductions so the runner can
enforce the required class-agreement machinery gate; it never averages a
disagreement away.

SPEC-NOTE (validation RSS): the two-state ``k=2`` Lanczos call uses
``ncv=5`` rather than inheriting the single-state engine's ``ncv=12``.  The
solver tolerance, 800-iteration bound, Hamiltonian, and explicit residual,
norm, and overlap gates are unchanged; the smaller bounded subspace avoids
an ARPACK workspace peak above the memo's strict 4 GiB validation cap.

SPEC-NOTE (zero-weight conditioning): the exact ``+X`` preparation has
``p(X_S=-)=0`` at ``t=0``.  The dephased joint block is uniquely zero, while
its normalized conditional state is mathematically undefined.  For density
diagnostics only, this module reports the deterministic maximally mixed
placeholder ``I/d`` and marks the zero-probability outcome; its weight is
exactly zero in every Holevo and conditional-mutual-information scalar.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.

No formation rule.

Sets no audit status.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import itertools
import json
import math
import sys
import time
from types import MappingProxyType
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
import numpy.typing as npt
from scipy.sparse.linalg import eigsh


_OLD_DONT_WRITE_BYTECODE = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    import d3_cubic_orbit_engine_2026_07_09 as orbit_engine
finally:
    sys.dont_write_bytecode = _OLD_DONT_WRITE_BYTECODE


ComplexArray = npt.NDArray[np.complex128]
UIntArray = npt.NDArray[np.uint32]

DESCRIPTOR_SCHEMA = "d3-bar-location-fragment-descriptor-v1"
RAW_LOOKUP_SCHEMA = "d3-bar-location-raw-to-orbit-v1"
EXTENSION_VALIDATION_SCHEMA = "d3-bar-location-extension-validation-v1"
MARGINAL_TOL = 1.0e-9
ORTHOGONALITY_TOL = 1.0e-9
GROUND_RESIDUAL_TOL = 1.0e-8
DEFAULT_GATHER_AMPLITUDE_BYTES = 64 << 20
MAX_SELECTED_QUBITS = 11
MAX_FRAGMENT_QUBITS = 5
VALIDATION_WALL_SECONDS = 15.0 * 60.0
VALIDATION_RSS_GB = 4.0

FRAGMENT_LABEL_ORDER = ("+x", "-x", "+y", "-y", "+z", "-z")

_FRAGMENT_COORDINATES_MUTABLE: dict[
    str, tuple[tuple[int, int, int], ...]
] = {
    "+x": (
        (1, 0, 0),
        (1, 1, 0),
        (1, -1, 0),
        (1, 0, 1),
        (1, 0, -1),
    ),
    "-x": (
        (-1, 0, 0),
        (-1, 1, 0),
        (-1, -1, 0),
        (-1, 0, 1),
        (-1, 0, -1),
    ),
    "+y": (
        (0, 1, 0),
        (0, 1, 1),
        (1, 1, 1),
        (-1, 1, 1),
    ),
    "+z": (
        (0, 0, 1),
        (0, -1, 1),
        (1, -1, 1),
        (-1, -1, 1),
    ),
    "-y": (
        (0, -1, 0),
        (0, -1, -1),
        (1, -1, -1),
        (-1, -1, -1),
    ),
    "-z": (
        (0, 0, -1),
        (0, 1, -1),
        (1, 1, -1),
        (-1, 1, -1),
    ),
}
FRAGMENT_COORDINATES: Mapping[str, tuple[tuple[int, int, int], ...]] = (
    MappingProxyType(_FRAGMENT_COORDINATES_MUTABLE)
)

FRAGMENT_CLASS_MEMBERS: Mapping[str, tuple[str, ...]] = MappingProxyType(
    {
        "closed-five": ("+x", "-x"),
        "wedge-four": ("+y", "-y", "+z", "-z"),
    }
)

PAIR_CLASS_MEMBERS: Mapping[str, tuple[tuple[str, str], ...]] = MappingProxyType(
    {
        "opposite-55": (("+x", "-x"),),
        "opposite-44": (("+y", "-y"), ("+z", "-z")),
        "plus-x-orthogonal": (
            ("+x", "+y"),
            ("+x", "-y"),
            ("+x", "+z"),
            ("+x", "-z"),
        ),
        "minus-x-orthogonal": (
            ("-x", "+y"),
            ("-x", "-y"),
            ("-x", "+z"),
            ("-x", "-z"),
        ),
        "transverse-orthogonal": (
            ("+y", "+z"),
            ("+z", "-y"),
            ("-y", "-z"),
            ("-z", "+y"),
        ),
    }
)

PAIR_CLASS_ORDER = tuple(PAIR_CLASS_MEMBERS)
FRAGMENT_CLASS_ORDER = tuple(FRAGMENT_CLASS_MEMBERS)


@dataclass(frozen=True)
class FragmentDescriptorSet:
    """Verified immutable route-C descriptor payload."""

    schema: str
    fragment_labels: tuple[str, ...]
    fragments: tuple[tuple[str, tuple[tuple[int, int, int], ...]], ...]
    fragment_classes: tuple[tuple[str, tuple[str, ...]], ...]
    pair_classes: tuple[tuple[str, tuple[tuple[str, str], ...]], ...]
    rotation_count: int
    checksum: str

    def fragment_map(self) -> dict[str, tuple[tuple[int, int, int], ...]]:
        return dict(self.fragments)

    def fragment_class_map(self) -> dict[str, tuple[str, ...]]:
        return dict(self.fragment_classes)

    def pair_class_map(self) -> dict[str, tuple[tuple[str, str], ...]]:
        return dict(self.pair_classes)


@dataclass(frozen=True)
class RawOrbitLookup:
    """The checksum-bound, nonpersistent raw-index to orbit-index table."""

    raw_to_orbit: npt.NDArray[np.int32]
    basis_checksum: str
    geometry: str
    schema: str
    checksum: str
    build_seconds: float


@dataclass(frozen=True)
class DensitySummary:
    dimension: int
    trace_real: float
    trace_imag: float
    hermiticity_error: float
    minimum_eigenvalue: float
    entropy_bits: float
    checksum: str

    def as_dict(self) -> dict[str, object]:
        return {
            "dimension": self.dimension,
            "trace_real": self.trace_real,
            "trace_imag": self.trace_imag,
            "hermiticity_error": self.hermiticity_error,
            "minimum_eigenvalue": self.minimum_eigenvalue,
            "entropy_bits": self.entropy_bits,
            "checksum": self.checksum,
        }


@dataclass(frozen=True)
class ConditionalMarginal:
    """Pointer-dephased marginal in tensor order ``(S, subset...)``."""

    pointer_basis: str
    subset_sites: tuple[int, ...]
    probabilities: tuple[float, float]
    states: tuple[ComplexArray, ComplexArray]
    dephased_joint: ComplexArray
    state_summaries: tuple[DensitySummary, DensitySummary]
    joint_summary: DensitySummary
    removed_pointer_coherence: float
    zero_probability_outcomes: tuple[bool, bool]


@dataclass(frozen=True)
class PairConditionalMarginal:
    """Joint ``(S,F_a,F_b)`` result and CMI derived from that joint."""

    conditional: ConditionalMarginal
    fragment_a_sites: tuple[int, ...]
    fragment_b_sites: tuple[int, ...]
    fragment_a_states: tuple[ComplexArray, ComplexArray]
    fragment_b_states: tuple[ComplexArray, ComplexArray]
    fragment_a_summaries: tuple[DensitySummary, DensitySummary]
    fragment_b_summaries: tuple[DensitySummary, DensitySummary]
    conditional_mi_bits: float


@dataclass(frozen=True)
class TwoStateLanczosResult:
    energies: tuple[float, float]
    states: tuple[ComplexArray, ComplexArray]
    residuals: tuple[float, float]
    norm_errors: tuple[float, float]
    overlap: float


_RAW_LOOKUP: RawOrbitLookup | None = None
_VERIFIED_DESCRIPTORS: FragmentDescriptorSet | None = None


def _hash_array(name: str, array: npt.NDArray) -> str:
    contiguous = np.ascontiguousarray(array)
    digest = hashlib.sha256()
    digest.update(name.encode("utf-8"))
    digest.update(contiguous.dtype.str.encode("ascii"))
    digest.update(np.asarray(contiguous.shape, dtype=np.int64).tobytes())
    raw = memoryview(contiguous).cast("B")
    block = 64 << 20
    for offset in range(0, raw.nbytes, block):
        digest.update(raw[offset : offset + block])
    return digest.hexdigest()


def _matrix_checksum(matrix: npt.NDArray[np.complex128]) -> str:
    return _hash_array("density", np.asarray(matrix, dtype=np.complex128))


def _fragment_signature(
    coordinates: Iterable[tuple[int, int, int]],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted(tuple(map(int, coordinate)) for coordinate in coordinates))


def _pair_signature(
    first: Iterable[tuple[int, int, int]],
    second: Iterable[tuple[int, int, int]],
) -> tuple[tuple[tuple[int, int, int], ...], tuple[tuple[int, int, int], ...]]:
    pieces = (_fragment_signature(first), _fragment_signature(second))
    return tuple(sorted(pieces))  # type: ignore[return-value]


def verify_fragment_descriptors() -> FragmentDescriptorSet:
    """Verify the frozen partition and its two/five rotation classes.

    Every relationship is checked by explicit enumeration of the engine's
    independently verified 24 proper cube rotations.  Fragment membership
    is setwise for the symmetry proof; the stored coordinate tuples retain
    the memo's tensor-factor order exactly.
    """

    global _VERIFIED_DESCRIPTORS
    if _VERIFIED_DESCRIPTORS is not None:
        return _VERIFIED_DESCRIPTORS

    if tuple(FRAGMENT_COORDINATES) != ("+x", "-x", "+y", "+z", "-y", "-z"):
        raise AssertionError("fragment coordinate literals changed order")
    if set(FRAGMENT_COORDINATES) != set(FRAGMENT_LABEL_ORDER):
        raise AssertionError("fragment labels do not match the frozen graph order")
    sizes = tuple(len(FRAGMENT_COORDINATES[label]) for label in FRAGMENT_LABEL_ORDER)
    if sizes != (5, 5, 4, 4, 4, 4):
        raise AssertionError(f"fragment sizes {sizes}, expected (5,5,4,4,4,4)")

    flattened = [
        coordinate
        for label in FRAGMENT_LABEL_ORDER
        for coordinate in FRAGMENT_COORDINATES[label]
    ]
    expected_noncenter = {
        coordinate
        for coordinate in itertools.product((-1, 0, 1), repeat=3)
        if coordinate != (0, 0, 0)
    }
    if len(flattened) != 26 or len(set(flattened)) != 26:
        raise AssertionError("route-C fragments are not a disjoint 26-site partition")
    if set(flattened) != expected_noncenter:
        raise AssertionError("route-C fragments omit or add a non-center cube site")

    geometry = orbit_engine._cube_geometry()
    if geometry.permutations.shape[0] != 24:
        raise AssertionError("descriptor verification did not receive 24 rotations")
    coordinate_index = {
        tuple(map(int, coordinate)): index
        for index, coordinate in enumerate(geometry.coordinates)
    }

    def rotate_fragment(
        coordinates: Sequence[tuple[int, int, int]],
        permutation: npt.NDArray[np.int16],
    ) -> tuple[tuple[int, int, int], ...]:
        return tuple(
            tuple(map(int, geometry.coordinates[int(permutation[coordinate_index[c]])]))
            for c in coordinates
        )

    declared_fragment_signatures = {
        label: _fragment_signature(FRAGMENT_COORDINATES[label])
        for label in FRAGMENT_LABEL_ORDER
    }
    classified_fragments: set[str] = set()
    for class_name, members in FRAGMENT_CLASS_MEMBERS.items():
        representative = FRAGMENT_COORDINATES[members[0]]
        orbit = {
            _fragment_signature(rotate_fragment(representative, permutation))
            for permutation in geometry.permutations
        }
        for member in members:
            if declared_fragment_signatures[member] not in orbit:
                raise AssertionError(
                    f"fragment {member} is not in declared class {class_name}"
                )
            if member in classified_fragments:
                raise AssertionError(f"fragment {member} has duplicate class membership")
            classified_fragments.add(member)
    if classified_fragments != set(FRAGMENT_LABEL_ORDER):
        raise AssertionError("two fragment classes do not partition all six labels")

    all_declared_pairs = {
        tuple(pair)
        for pair in itertools.combinations(FRAGMENT_LABEL_ORDER, 2)
    }
    classified_pairs: set[tuple[str, str]] = set()
    for class_name, members in PAIR_CLASS_MEMBERS.items():
        rep_left, rep_right = members[0]
        orbit = {
            _pair_signature(
                rotate_fragment(FRAGMENT_COORDINATES[rep_left], permutation),
                rotate_fragment(FRAGMENT_COORDINATES[rep_right], permutation),
            )
            for permutation in geometry.permutations
        }
        for left, right in members:
            normalized = tuple(
                sorted((left, right), key=FRAGMENT_LABEL_ORDER.index)
            )
            if _pair_signature(
                FRAGMENT_COORDINATES[left], FRAGMENT_COORDINATES[right]
            ) not in orbit:
                raise AssertionError(
                    f"pair {(left, right)} is not in declared class {class_name}"
                )
            if normalized in classified_pairs:
                raise AssertionError(f"pair {normalized} has duplicate class membership")
            classified_pairs.add(normalized)
    if classified_pairs != all_declared_pairs:
        missing = sorted(all_declared_pairs - classified_pairs)
        extra = sorted(classified_pairs - all_declared_pairs)
        raise AssertionError(f"five pair classes do not partition K6: missing={missing}, extra={extra}")

    payload = {
        "schema": DESCRIPTOR_SCHEMA,
        "fragment_label_order": list(FRAGMENT_LABEL_ORDER),
        "fragments": {
            label: [list(coordinate) for coordinate in FRAGMENT_COORDINATES[label]]
            for label in FRAGMENT_LABEL_ORDER
        },
        "fragment_classes": {
            name: list(members) for name, members in FRAGMENT_CLASS_MEMBERS.items()
        },
        "pair_classes": {
            name: [list(pair) for pair in members]
            for name, members in PAIR_CLASS_MEMBERS.items()
        },
        "proper_rotation_count": 24,
    }
    checksum = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    _VERIFIED_DESCRIPTORS = FragmentDescriptorSet(
        schema=DESCRIPTOR_SCHEMA,
        fragment_labels=FRAGMENT_LABEL_ORDER,
        fragments=tuple(
            (label, FRAGMENT_COORDINATES[label]) for label in FRAGMENT_LABEL_ORDER
        ),
        fragment_classes=tuple(FRAGMENT_CLASS_MEMBERS.items()),
        pair_classes=tuple(PAIR_CLASS_MEMBERS.items()),
        rotation_count=24,
        checksum=checksum,
    )
    return _VERIFIED_DESCRIPTORS


def qubit_amplitudes_from_bloch(
    bloch: Sequence[float],
) -> tuple[complex, complex]:
    """Return the canonical pure-qubit amplitudes for an exact Bloch vector."""

    vector = np.asarray(bloch, dtype=np.float64)
    if vector.shape != (3,) or not np.all(np.isfinite(vector)):
        raise ValueError("Bloch vector must contain three finite real values")
    norm = float(np.linalg.norm(vector))
    if abs(norm - 1.0) > 1.0e-12:
        raise ValueError(f"Bloch vector norm {norm:.16g} is not one")
    x, y, z = map(float, vector)
    if z <= -1.0 + 1.0e-14:
        amplitudes = (0.0 + 0.0j, 1.0 + 0.0j)
    else:
        zero = math.sqrt(max(0.0, (1.0 + z) / 2.0))
        one = complex(x, y) / math.sqrt(2.0 * (1.0 + z))
        amplitudes = (complex(zero), complex(one))
    if abs(sum(abs(value) ** 2 for value in amplitudes) - 1.0) > 1.0e-12:
        raise AssertionError("Bloch-to-amplitude conversion lost normalization")
    return amplitudes


def _validated_qubit_vector(
    value: Sequence[complex], label: str
) -> tuple[complex, complex]:
    array = np.asarray(value, dtype=np.complex128)
    if array.shape != (2,) or not np.all(np.isfinite(array)):
        raise ValueError(f"{label} must be one finite two-amplitude qubit vector")
    norm = float(np.vdot(array, array).real)
    if abs(norm - 1.0) > 1.0e-12:
        raise ValueError(f"{label} qubit-vector norm {norm:.16g} is not one")
    return complex(array[0]), complex(array[1])


def _site_class_indices(basis: Any) -> dict[str, tuple[int, ...]]:
    classes: dict[str, list[int]] = {
        "center": [],
        "face": [],
        "edge": [],
        "corner": [],
    }
    if basis.geometry_name == "open-3x3x3":
        for index, coordinate in enumerate(basis.coordinates):
            nonzero = sum(int(component) != 0 for component in coordinate)
            classes[("center", "face", "edge", "corner")[nonzero]].append(index)
        expected = {"center": 1, "face": 6, "edge": 12, "corner": 8}
        if {name: len(values) for name, values in classes.items()} != expected:
            raise AssertionError("cube site classes are not 1/6/12/8")
    elif basis.geometry_name == "open-3x3x2":
        # Methods-only surrogate: D4 preserves the in-plane radial class and
        # may exchange layers.  The otherwise unused 'edge' vector has an
        # empty slab class; all three nonempty classes remain independently
        # distinguishable and class-uniform under every slab rotation.
        for index, coordinate in enumerate(basis.coordinates):
            radial_nonzero = sum(int(component) != 0 for component in coordinate[:2])
            name = ("center", "face", "corner")[radial_nonzero]
            classes[name].append(index)
        expected = {"center": 2, "face": 8, "edge": 0, "corner": 8}
        if {name: len(values) for name, values in classes.items()} != expected:
            raise AssertionError("slab class-product surrogate is not 2/8/0/8")
    else:
        raise ValueError(f"unsupported class-product geometry {basis.geometry_name!r}")
    return {name: tuple(values) for name, values in classes.items()}


def _mask_for_sites(sites: Sequence[int]) -> np.uint32:
    mask = 0
    for site in sites:  # at most 27 sites, never raw configurations
        mask |= 1 << int(site)
    return np.uint32(mask)


def class_product_state(
    basis: Any,
    *,
    center: Sequence[complex],
    face: Sequence[complex],
    edge: Sequence[complex],
    corner: Sequence[complex],
) -> ComplexArray:
    """Construct a class-uniform product state in the normalized orbit basis.

    The only accepted inputs are one vector per complete spatial site class;
    a per-site/nonuniform form is intentionally not accepted.  Representative
    amplitudes are evaluated from four vectorized class-popcount arrays and
    multiplied by ``sqrt(orbit_size)`` exactly as required.
    """

    vectors = {
        "center": _validated_qubit_vector(center, "center"),
        "face": _validated_qubit_vector(face, "face"),
        "edge": _validated_qubit_vector(edge, "edge"),
        "corner": _validated_qubit_vector(corner, "corner"),
    }
    classes = _site_class_indices(basis)
    masks = {name: _mask_for_sites(sites) for name, sites in classes.items()}
    state = np.empty(basis.n_orbits, dtype=np.complex128)
    for chunk_number, start in enumerate(
        range(0, basis.n_orbits, orbit_engine.TABLE_CHUNK)
    ):
        stop = min(start + orbit_engine.TABLE_CHUNK, basis.n_orbits)
        representatives = basis.representatives[start:stop]
        raw = np.ones(stop - start, dtype=np.complex128)
        for class_name in ("center", "face", "edge", "corner"):
            count = orbit_engine._popcount_uint32(
                representatives & masks[class_name]
            )
            class_size = len(classes[class_name])
            zero, one = vectors[class_name]
            raw *= np.power(zero, class_size - count.astype(np.int16))
            raw *= np.power(one, count.astype(np.int16))
        state[start:stop] = np.sqrt(
            basis.orbit_sizes[start:stop].astype(np.float64)
        ) * raw
        if chunk_number % orbit_engine.RSS_CHECK_EVERY_CHUNKS == 0:
            orbit_engine._guard_rss(f"bar class-product chunk {chunk_number}")
    norm = float(np.linalg.norm(state))
    if not np.isfinite(norm) or abs(norm - 1.0) > 1.0e-10:
        raise AssertionError(f"class-product reduced norm {norm:.16g} is invalid")
    state /= norm
    return state


def _lookup_checksum(raw_to_orbit: npt.NDArray[np.int32], basis_checksum: str) -> str:
    digest = hashlib.sha256()
    digest.update(RAW_LOOKUP_SCHEMA.encode("utf-8"))
    digest.update(basis_checksum.encode("ascii"))
    digest.update(_hash_array("raw_to_orbit", raw_to_orbit).encode("ascii"))
    return digest.hexdigest()


def get_raw_to_orbit_lookup(
    basis: Any, *, budget_gb: float = orbit_engine.BUDGET_GB
) -> RawOrbitLookup:
    """Build once and retain the required nonpersistent ``int32`` lookup."""

    global _RAW_LOOKUP
    if _RAW_LOOKUP is not None:
        if (
            _RAW_LOOKUP.basis_checksum != basis.checksum
            or _RAW_LOOKUP.geometry != basis.geometry_name
            or _RAW_LOOKUP.raw_to_orbit.shape != (1 << basis.n_sites,)
        ):
            raise RuntimeError(
                "one-process raw-to-orbit lookup is already bound to a different basis"
            )
        return _RAW_LOOKUP

    started = time.perf_counter()
    geometry = orbit_engine._geometry_for_basis(basis)
    luts = orbit_engine._permutation_luts(geometry)
    raw_to_orbit = np.full(1 << basis.n_sites, -1, dtype=np.int32)
    for group_index, rotation_lut in enumerate(luts):
        for start in range(0, basis.n_orbits, orbit_engine.TABLE_CHUNK):
            stop = min(start + orbit_engine.TABLE_CHUNK, basis.n_orbits)
            images = orbit_engine._permute_bits(
                basis.representatives[start:stop], rotation_lut
            )
            orbit_indices = np.arange(start, stop, dtype=np.int32)
            previous = raw_to_orbit[images]
            if np.any((previous >= 0) & (previous != orbit_indices)):
                raise AssertionError("canonicalization assigned one raw state to two orbits")
            raw_to_orbit[images] = orbit_indices
        if group_index % orbit_engine.RSS_CHECK_EVERY_CHUNKS == 0:
            orbit_engine._guard_rss(
                f"bar raw-to-orbit rotation {group_index}", budget_gb
            )
    if np.any(raw_to_orbit < 0):
        raise AssertionError("raw-to-orbit lookup has unassigned configurations")
    expected_representatives = np.arange(basis.n_orbits, dtype=np.int32)
    if not np.array_equal(raw_to_orbit[basis.representatives], expected_representatives):
        raise AssertionError("raw-to-orbit lookup does not fix representatives")
    checksum = _lookup_checksum(raw_to_orbit, basis.checksum)
    _RAW_LOOKUP = RawOrbitLookup(
        raw_to_orbit=raw_to_orbit,
        basis_checksum=basis.checksum,
        geometry=basis.geometry_name,
        schema=RAW_LOOKUP_SCHEMA,
        checksum=checksum,
        build_seconds=time.perf_counter() - started,
    )
    orbit_engine._guard_rss("bar raw-to-orbit complete", budget_gb)
    return _RAW_LOOKUP


def clear_raw_to_orbit_lookup() -> None:
    """Release the process lookup, primarily between slab and cube validation."""

    global _RAW_LOOKUP
    _RAW_LOOKUP = None


def center_bond_runtime_tables(basis: Any, tables: Any) -> Any:
    """Retain only double-flip rows used by the existing center-bond path.

    Loading the landed table cache has already validated its complete
    checksum.  Fragment and fragment-pair paths in this extension use raw
    gathers, while Hamiltonian matvec uses only the diagonal and single-flip
    arrays.  Keeping the six exact center--face masks therefore preserves
    every runtime consumer and releases fifteen unused pair-observer rows
    before Lanczos.  Nothing is rewritten to the persistent cache.
    """

    if tables.basis_checksum != basis.checksum:
        raise ValueError("Hamiltonian tables do not belong to this basis")
    spec = orbit_engine._observable_spec(basis)
    required_masks = sorted(
        {
            (1 << first) | (1 << second)
            for _, (first, second), _ in orbit_engine._operator_orbit(
                basis, spec.center_bond, ("X", "X")
            )
        }
    )
    indices: list[int] = []
    for mask in required_masks:
        index = int(np.searchsorted(tables.double_flip_masks, np.uint32(mask)))
        if (
            index >= tables.double_flip_masks.size
            or int(tables.double_flip_masks[index]) != mask
        ):
            raise RuntimeError(f"validated table cache lacks center-bond mask 0x{mask:x}")
        indices.append(index)
    masks = np.asarray(required_masks, dtype=np.uint32)
    targets = np.asarray(tables.double_flip_targets[indices], dtype=np.int32)
    runtime = orbit_engine.HamiltonianTables(
        diagonal_zz=tables.diagonal_zz,
        flip_targets=tables.flip_targets,
        flip_amplitudes=tables.flip_amplitudes,
        double_flip_masks=masks,
        double_flip_targets=targets,
        basis_checksum=tables.basis_checksum,
        checksum=f"center-bond-runtime-view:{tables.checksum}",
        cache_status=f"{tables.cache_status}-center-bond-runtime-view",
        cache_path=tables.cache_path,
    )
    orbit_engine._ACTIVE_BASIS = basis
    orbit_engine._ACTIVE_TABLES = runtime
    orbit_engine._ACTIVE_SPEC = spec
    return runtime


def verify_raw_lookup_checksum(lookup: RawOrbitLookup) -> str:
    """Recompute and enforce the lookup checksum at an explicit gate."""

    computed = _lookup_checksum(lookup.raw_to_orbit, lookup.basis_checksum)
    if computed != lookup.checksum:
        raise RuntimeError(
            f"raw-to-orbit checksum mismatch: stored {lookup.checksum}, computed {computed}"
        )
    return computed


def coordinate_sites(
    basis: Any, coordinates: Sequence[Sequence[int]]
) -> tuple[int, ...]:
    """Translate an ordered coordinate tuple to ordered engine bit sites."""

    index = {
        tuple(map(int, coordinate)): site
        for site, coordinate in enumerate(basis.coordinates)
    }
    result: list[int] = []
    for coordinate in coordinates:
        key = tuple(map(int, coordinate))
        if key not in index:
            raise ValueError(f"coordinate {key} is not in {basis.geometry_name}")
        result.append(int(index[key]))
    if len(result) != len(set(result)):
        raise ValueError("ordered coordinate subset contains a duplicate")
    return tuple(result)


def fragment_sites(basis: Any, label: str) -> tuple[int, ...]:
    """Return one frozen fragment's bit sites in memo tensor-factor order."""

    if label not in FRAGMENT_COORDINATES:
        raise ValueError(f"unknown fragment label {label!r}")
    return coordinate_sites(basis, FRAGMENT_COORDINATES[label])


def pointer_site(basis: Any) -> int:
    """Return the declared cube center (or engine slab surrogate) pointer."""

    return int(orbit_engine._observable_spec(basis).pointer)


def _scatter_ordered_patterns(
    patterns: UIntArray, sites: Sequence[int]
) -> UIntArray:
    """Scatter big-endian subsystem bits into little-endian raw site bits."""

    output = np.zeros(patterns.shape, dtype=np.uint32)
    width = len(sites)
    for factor, site in enumerate(sites):  # at most 27 tensor factors
        source_shift = np.uint32(width - 1 - factor)
        output |= (
            ((patterns >> source_shift) & np.uint32(1))
            << np.uint32(int(site))
        )
    return output


def _validate_selected_sites(
    basis: Any, selected_sites: Sequence[int]
) -> tuple[int, ...]:
    selected = tuple(int(site) for site in selected_sites)
    if not selected:
        raise ValueError("a gathered marginal must select at least one site")
    if len(selected) > MAX_SELECTED_QUBITS:
        raise ValueError(
            f"selected subset has {len(selected)} qubits; hard limit is {MAX_SELECTED_QUBITS}"
        )
    if len(selected) != len(set(selected)):
        raise ValueError("selected subset contains duplicate sites")
    if min(selected) < 0 or max(selected) >= basis.n_sites:
        raise ValueError("selected subset contains a site outside the basis")
    return selected


def _validate_state_mixture(
    basis: Any,
    states: Sequence[npt.NDArray[np.complex128]],
    weights: Sequence[float] | None,
) -> tuple[tuple[ComplexArray, ...], tuple[float, ...]]:
    if not states:
        raise ValueError("at least one invariant-sector state is required")
    normalized_states: list[ComplexArray] = []
    for index, state in enumerate(states):
        array = np.asarray(state, dtype=np.complex128)
        if array.shape != (basis.n_orbits,) or not np.all(np.isfinite(array)):
            raise ValueError(f"state {index} does not match the orbit basis")
        norm_error = abs(float(np.vdot(array, array).real) - 1.0)
        if norm_error > MARGINAL_TOL:
            raise ValueError(f"state {index} norm-squared error {norm_error:.3e}")
        normalized_states.append(array)
    if weights is None:
        normalized_weights = tuple(1.0 / len(states) for _ in states)
    else:
        normalized_weights = tuple(float(weight) for weight in weights)
    if len(normalized_weights) != len(states):
        raise ValueError("mixture weights and states have different lengths")
    if (
        any(not np.isfinite(weight) or weight < 0.0 for weight in normalized_weights)
        or abs(sum(normalized_weights) - 1.0) > MARGINAL_TOL
    ):
        raise ValueError("mixture weights must be finite, nonnegative, and sum to one")
    return tuple(normalized_states), normalized_weights


def gather_subset_density(
    basis: Any,
    lookup: RawOrbitLookup,
    states: Sequence[npt.NDArray[np.complex128]],
    selected_sites: Sequence[int],
    *,
    weights: Sequence[float] | None = None,
    amplitude_bytes: int = DEFAULT_GATHER_AMPLITUDE_BYTES,
    budget_gb: float = orbit_engine.BUDGET_GB,
) -> ComplexArray:
    """Gather an ordered exact marginal without a raw complex state.

    For each complement chunk this forms
    ``M[a,c] = psi_orbit[raw_to_orbit[index(a,c)]] / sqrt(orbit_size)``
    and linearly accumulates ``weight * M M^dagger``.  All raw indices,
    canonical gathers, and amplitude recovery are vectorized NumPy arrays;
    Python loops range only over bounded tensor factors, chunks, and mixture
    members.
    """

    selected = _validate_selected_sites(basis, selected_sites)
    if lookup.basis_checksum != basis.checksum:
        raise ValueError("raw-to-orbit lookup belongs to a different basis")
    if lookup.raw_to_orbit.shape != (1 << basis.n_sites,):
        raise ValueError("raw-to-orbit lookup has the wrong raw dimension")
    mixture_states, mixture_weights = _validate_state_mixture(
        basis, states, weights
    )
    if int(amplitude_bytes) != amplitude_bytes or amplitude_bytes < 1:
        raise ValueError("amplitude_bytes must be a positive integer")

    selected_dimension = 1 << len(selected)
    complement = tuple(site for site in range(basis.n_sites) if site not in selected)
    complement_dimension = 1 << len(complement)
    selected_patterns = np.arange(selected_dimension, dtype=np.uint32)
    selected_masks = _scatter_ordered_patterns(selected_patterns, selected)
    chunk_columns = max(
        1,
        min(
            complement_dimension,
            1 << 18,
            int(amplitude_bytes) // (np.dtype(np.complex128).itemsize * selected_dimension),
        ),
    )
    density = np.zeros(
        (selected_dimension, selected_dimension), dtype=np.complex128
    )
    for chunk_number, start in enumerate(
        range(0, complement_dimension, chunk_columns)
    ):
        stop = min(start + chunk_columns, complement_dimension)
        complement_patterns = np.arange(start, stop, dtype=np.uint32)
        complement_masks = _scatter_ordered_patterns(
            complement_patterns, complement
        )
        raw_indices = selected_masks[:, None] | complement_masks[None, :]
        orbit_indices = lookup.raw_to_orbit[raw_indices]
        if np.any(orbit_indices < 0):
            raise AssertionError("gather encountered an unassigned raw configuration")
        denominators = np.sqrt(
            basis.orbit_sizes[orbit_indices].astype(np.float64)
        )
        for state, weight in zip(
            mixture_states, mixture_weights, strict=True
        ):
            amplitudes = np.asarray(
                state[orbit_indices] / denominators, dtype=np.complex128
            )
            product = amplitudes @ amplitudes.conj().T
            density += float(weight) * product
            del amplitudes, product
        del complement_patterns, complement_masks, raw_indices, orbit_indices, denominators
        if chunk_number % orbit_engine.RSS_CHECK_EVERY_CHUNKS == 0:
            orbit_engine._guard_rss(
                f"bar marginal q={len(selected)} chunk {chunk_number}", budget_gb
            )

    hermiticity = float(np.max(np.abs(density - density.conj().T)))
    trace_error = float(abs(np.trace(density) - 1.0))
    if max(hermiticity, trace_error) > MARGINAL_TOL:
        raise AssertionError(
            f"gathered q={len(selected)} density invalid: "
            f"hermiticity={hermiticity:.3e}, trace={trace_error:.3e}"
        )
    cleaned = np.asarray(0.5 * (density + density.conj().T), dtype=np.complex128)
    orbit_engine._guard_rss(f"bar marginal q={len(selected)} complete", budget_gb)
    return cleaned


def partial_trace_density(
    matrix: npt.NDArray[np.complex128],
    n_qubits: int,
    keep_factors: Sequence[int],
) -> ComplexArray:
    """Vectorized ordered partial trace of a qubit density matrix."""

    if int(n_qubits) != n_qubits or n_qubits < 1:
        raise ValueError("n_qubits must be a positive integer")
    keep = tuple(int(factor) for factor in keep_factors)
    if len(keep) != len(set(keep)) or any(
        factor < 0 or factor >= n_qubits for factor in keep
    ):
        raise ValueError("keep_factors are not a unique ordered subset")
    rho = np.asarray(matrix, dtype=np.complex128)
    dimension = 1 << n_qubits
    if rho.shape != (dimension, dimension):
        raise ValueError(
            f"density shape {rho.shape} does not match {n_qubits} qubits"
        )
    traced = tuple(factor for factor in range(n_qubits) if factor not in keep)
    permutation = keep + traced + tuple(n_qubits + factor for factor in keep) + tuple(
        n_qubits + factor for factor in traced
    )
    kept_dimension = 1 << len(keep)
    traced_dimension = 1 << len(traced)
    tensor = np.transpose(rho.reshape((2,) * (2 * n_qubits)), permutation)
    tensor = tensor.reshape(
        kept_dimension, traced_dimension, kept_dimension, traced_dimension
    )
    reduced = np.einsum("aibi->ab", tensor, optimize=True)
    return np.asarray(reduced, dtype=np.complex128)


def density_summary(
    matrix: npt.NDArray[np.complex128],
    *,
    label: str = "density",
    tolerance: float = MARGINAL_TOL,
) -> DensitySummary:
    """Validate and summarize a normalized density matrix."""

    raw = np.asarray(matrix, dtype=np.complex128)
    if raw.ndim != 2 or raw.shape[0] != raw.shape[1] or not np.all(np.isfinite(raw)):
        raise ValueError(f"{label} is not a finite square matrix")
    hermiticity = float(np.max(np.abs(raw - raw.conj().T)))
    trace = complex(np.trace(raw))
    trace_error = abs(trace - 1.0)
    hermitian = 0.5 * (raw + raw.conj().T)
    eigenvalues = np.linalg.eigvalsh(hermitian)
    minimum = float(np.min(eigenvalues))
    if max(hermiticity, trace_error, max(0.0, -minimum)) > tolerance:
        raise AssertionError(
            f"{label} invalid: herm={hermiticity:.3e}, trace={trace_error:.3e}, "
            f"minimum={minimum:.3e}"
        )
    positive = eigenvalues[eigenvalues > 0.0]
    entropy = float(-np.sum(positive * np.log2(positive)))
    return DensitySummary(
        dimension=int(raw.shape[0]),
        trace_real=float(trace.real),
        trace_imag=float(trace.imag),
        hermiticity_error=hermiticity,
        minimum_eigenvalue=minimum,
        entropy_bits=entropy,
        checksum=_matrix_checksum(raw),
    )


def _binary_entropy(probabilities: Sequence[float]) -> float:
    return float(
        -sum(float(value) * math.log2(float(value)) for value in probabilities if value > 0.0)
    )


def _pointer_basis_transform(
    joint: npt.NDArray[np.complex128], pointer_basis: str
) -> ComplexArray:
    basis_name = pointer_basis.upper()
    if basis_name not in ("Z", "X"):
        raise ValueError("pointer_basis must be 'Z' or 'X'")
    matrix = np.asarray(joint, dtype=np.complex128)
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] % 2:
        raise ValueError("joint density does not have a leading pointer qubit")
    if basis_name == "Z":
        return matrix.copy()
    rest = matrix.shape[0] // 2
    tensor = matrix.reshape(2, rest, 2, rest)
    hadamard = np.asarray(
        [[1.0, 1.0], [1.0, -1.0]], dtype=np.complex128
    ) / math.sqrt(2.0)
    transformed = np.einsum(
        "sa,sitj,tb->aibj",
        hadamard.conj(),
        tensor,
        hadamard,
        optimize=True,
    )
    return np.asarray(transformed.reshape(matrix.shape), dtype=np.complex128)


def _joint_summary_from_blocks(
    joint: ComplexArray,
    probabilities: tuple[float, float],
    state_summaries: tuple[DensitySummary, DensitySummary],
) -> DensitySummary:
    trace = complex(np.trace(joint))
    hermiticity = float(np.max(np.abs(joint - joint.conj().T)))
    minimum = min(
        probabilities[index] * state_summaries[index].minimum_eigenvalue
        for index in range(2)
    )
    entropy = _binary_entropy(probabilities) + sum(
        probabilities[index] * state_summaries[index].entropy_bits
        for index in range(2)
    )
    if max(hermiticity, abs(trace - 1.0), max(0.0, -minimum)) > MARGINAL_TOL:
        raise AssertionError("pointer-dephased joint density failed validation")
    return DensitySummary(
        dimension=int(joint.shape[0]),
        trace_real=float(trace.real),
        trace_imag=float(trace.imag),
        hermiticity_error=hermiticity,
        minimum_eigenvalue=float(minimum),
        entropy_bits=float(entropy),
        checksum=_matrix_checksum(joint),
    )


def _condition_pointer_joint(
    joint: npt.NDArray[np.complex128],
    *,
    pointer_basis: str,
    subset_sites: Sequence[int],
) -> ConditionalMarginal:
    transformed = _pointer_basis_transform(joint, pointer_basis)
    rest = transformed.shape[0] // 2
    tensor = transformed.reshape(2, rest, 2, rest)
    removed_coherence = float(
        max(np.max(np.abs(tensor[0, :, 1, :])), np.max(np.abs(tensor[1, :, 0, :])))
    )
    tensor[0, :, 1, :] = 0.0
    tensor[1, :, 0, :] = 0.0
    probabilities_list: list[float] = []
    states_list: list[ComplexArray] = []
    summaries_list: list[DensitySummary] = []
    zero_probability: list[bool] = []
    for outcome in range(2):
        block = np.asarray(tensor[outcome, :, outcome, :], dtype=np.complex128)
        probability_complex = complex(np.trace(block))
        if abs(probability_complex.imag) > MARGINAL_TOL:
            raise AssertionError("conditioning probability has an imaginary component")
        probability = float(probability_complex.real)
        if probability < -MARGINAL_TOL:
            raise ValueError(
                f"{pointer_basis} pointer outcome {outcome} has negative probability"
            )
        is_zero = probability <= 1.0e-15
        if is_zero:
            probability = 0.0
            state = np.eye(rest, dtype=np.complex128) / float(rest)
        else:
            state = np.asarray(block / probability, dtype=np.complex128)
        summary = density_summary(
            state, label=f"conditional {pointer_basis} outcome {outcome}"
        )
        probabilities_list.append(probability)
        states_list.append(state)
        summaries_list.append(summary)
        zero_probability.append(is_zero)
    probabilities = (probabilities_list[0], probabilities_list[1])
    if abs(sum(probabilities) - 1.0) > MARGINAL_TOL:
        raise AssertionError("pointer outcome probabilities do not sum to one")
    states = (states_list[0], states_list[1])
    summaries = (summaries_list[0], summaries_list[1])
    dephased = np.asarray(tensor.reshape(transformed.shape), dtype=np.complex128)
    joint_summary = _joint_summary_from_blocks(dephased, probabilities, summaries)
    return ConditionalMarginal(
        pointer_basis=pointer_basis.upper(),
        subset_sites=tuple(int(site) for site in subset_sites),
        probabilities=probabilities,
        states=states,
        dephased_joint=dephased,
        state_summaries=summaries,
        joint_summary=joint_summary,
        removed_pointer_coherence=removed_coherence,
        zero_probability_outcomes=(zero_probability[0], zero_probability[1]),
    )


def conditional_fragment_marginal(
    basis: Any,
    lookup: RawOrbitLookup,
    states: Sequence[npt.NDArray[np.complex128]],
    ordered_fragment_sites: Sequence[int],
    *,
    pointer_basis: str = "Z",
    pointer: int | None = None,
    weights: Sequence[float] | None = None,
    amplitude_bytes: int = DEFAULT_GATHER_AMPLITUDE_BYTES,
    budget_gb: float = orbit_engine.BUDGET_GB,
) -> ConditionalMarginal:
    """Return exact ``k <= 5`` pointer-conditioned fragment states."""

    fragment = tuple(int(site) for site in ordered_fragment_sites)
    if not 1 <= len(fragment) <= MAX_FRAGMENT_QUBITS:
        raise ValueError("fragment size must be in [1,5]")
    pointer_index = pointer_site(basis) if pointer is None else int(pointer)
    if pointer_index in fragment:
        raise ValueError("pointer cannot be a fragment tensor factor")
    selected = (pointer_index,) + fragment
    joint = gather_subset_density(
        basis,
        lookup,
        states,
        selected,
        weights=weights,
        amplitude_bytes=amplitude_bytes,
        budget_gb=budget_gb,
    )
    return _condition_pointer_joint(
        joint, pointer_basis=pointer_basis, subset_sites=fragment
    )


def fragment_pair_marginal(
    basis: Any,
    lookup: RawOrbitLookup,
    states: Sequence[npt.NDArray[np.complex128]],
    ordered_fragment_a_sites: Sequence[int],
    ordered_fragment_b_sites: Sequence[int],
    *,
    pointer_basis: str = "Z",
    pointer: int | None = None,
    weights: Sequence[float] | None = None,
    amplitude_bytes: int = DEFAULT_GATHER_AMPLITUDE_BYTES,
    budget_gb: float = orbit_engine.BUDGET_GB,
) -> PairConditionalMarginal:
    """Return the dephased ``(S,F_a,F_b)`` joint and its exact CMI."""

    fragment_a = tuple(int(site) for site in ordered_fragment_a_sites)
    fragment_b = tuple(int(site) for site in ordered_fragment_b_sites)
    if not 1 <= len(fragment_a) <= MAX_FRAGMENT_QUBITS:
        raise ValueError("fragment A size must be in [1,5]")
    if not 1 <= len(fragment_b) <= MAX_FRAGMENT_QUBITS:
        raise ValueError("fragment B size must be in [1,5]")
    if set(fragment_a) & set(fragment_b):
        raise ValueError("fragment-pair API forbids shared coordinates")
    pointer_index = pointer_site(basis) if pointer is None else int(pointer)
    if pointer_index in fragment_a or pointer_index in fragment_b:
        raise ValueError("pointer cannot occur in either fragment")
    selected = (pointer_index,) + fragment_a + fragment_b
    joint = gather_subset_density(
        basis,
        lookup,
        states,
        selected,
        weights=weights,
        amplitude_bytes=amplitude_bytes,
        budget_gb=budget_gb,
    )
    conditioned = _condition_pointer_joint(
        joint,
        pointer_basis=pointer_basis,
        subset_sites=fragment_a + fragment_b,
    )
    keep_a = tuple(range(len(fragment_a)))
    keep_b = tuple(range(len(fragment_a), len(fragment_a) + len(fragment_b)))
    a_states: list[ComplexArray] = []
    b_states: list[ComplexArray] = []
    a_summaries: list[DensitySummary] = []
    b_summaries: list[DensitySummary] = []
    conditional_mi = 0.0
    for outcome, pair_state in enumerate(conditioned.states):
        a_state = partial_trace_density(
            pair_state, len(fragment_a) + len(fragment_b), keep_a
        )
        b_state = partial_trace_density(
            pair_state, len(fragment_a) + len(fragment_b), keep_b
        )
        a_summary = density_summary(a_state, label=f"pair F_a outcome {outcome}")
        b_summary = density_summary(b_state, label=f"pair F_b outcome {outcome}")
        conditional_mi += conditioned.probabilities[outcome] * (
            a_summary.entropy_bits
            + b_summary.entropy_bits
            - conditioned.state_summaries[outcome].entropy_bits
        )
        a_states.append(a_state)
        b_states.append(b_state)
        a_summaries.append(a_summary)
        b_summaries.append(b_summary)
    if conditional_mi < -MARGINAL_TOL or not np.isfinite(conditional_mi):
        raise AssertionError(f"conditional mutual information {conditional_mi!r} is invalid")
    return PairConditionalMarginal(
        conditional=conditioned,
        fragment_a_sites=fragment_a,
        fragment_b_sites=fragment_b,
        fragment_a_states=(a_states[0], a_states[1]),
        fragment_b_states=(b_states[0], b_states[1]),
        fragment_a_summaries=(a_summaries[0], a_summaries[1]),
        fragment_b_summaries=(b_summaries[0], b_summaries[1]),
        conditional_mi_bits=float(conditional_mi),
    )


def holevo_bits(conditional: ConditionalMarginal) -> float:
    """Evaluate Holevo information from an already mixed conditional marginal."""

    probabilities = conditional.probabilities
    average = (
        probabilities[0] * conditional.states[0]
        + probabilities[1] * conditional.states[1]
    )
    average_summary = density_summary(average, label="conditional ensemble average")
    value = average_summary.entropy_bits - sum(
        probabilities[index] * conditional.state_summaries[index].entropy_bits
        for index in range(2)
    )
    pointer_entropy = _binary_entropy(probabilities)
    if value < -MARGINAL_TOL or value > pointer_entropy + MARGINAL_TOL:
        raise AssertionError(
            f"Holevo value {value:.16g} outside [0,H={pointer_entropy:.16g}]"
        )
    return float(value)


def two_lowest_states(
    basis: Any,
    tables: Any,
    lam: float,
    *,
    budget_gb: float = orbit_engine.BUDGET_GB,
) -> TwoStateLanczosResult:
    """Return the two lowest orthonormal invariant-sector Lanczos states."""

    if tables.basis_checksum != basis.checksum:
        raise ValueError("Hamiltonian tables do not belong to the basis")
    if not np.isfinite(lam):
        raise ValueError("lambda must be finite")
    operator = orbit_engine._reduced_operator(basis, tables, float(lam), np.float64)
    rng = np.random.default_rng(20260710)
    initial = rng.standard_normal(basis.n_orbits)
    initial /= np.linalg.norm(initial)
    ncv = min(5, basis.n_orbits)
    eigenvalues, eigenvectors = eigsh(
        operator,
        k=2,
        which="SA",
        v0=initial,
        tol=orbit_engine.GROUND_TOL,
        maxiter=orbit_engine.GROUND_MAXITER,
        ncv=ncv,
        return_eigenvectors=True,
    )
    del initial
    # ``eigsh`` normally returns these two SA values in ascending order.  Do
    # the exceptional swap with one column-sized temporary instead of fancy
    # indexing the entire (n_orbits,2) array.  On the cube that avoids an
    # otherwise unnecessary ~85.5 MiB copy at the strict validation RSS gate.
    if float(eigenvalues[0]) > float(eigenvalues[1]):
        temporary = eigenvectors[:, 0].copy()
        eigenvectors[:, 0] = eigenvectors[:, 1]
        eigenvectors[:, 1] = temporary
        eigenvalues = eigenvalues[::-1].copy()
        del temporary
    first = eigenvectors[:, 0]
    first /= np.linalg.norm(first)
    second = eigenvectors[:, 1]
    # Orthogonalize in place: a separate real vector would cost another
    # ~42.8 MiB on the cube and has no numerical benefit here.
    second -= float(np.dot(first, second)) * first
    second_norm = float(np.linalg.norm(second))
    if second_norm <= 1.0e-15:
        raise RuntimeError("two-state Lanczos returned linearly dependent vectors")
    second /= second_norm
    real_states = (first, second)
    energies_list: list[float] = []
    residuals_list: list[float] = []
    complex_states: list[ComplexArray] = []
    norm_errors: list[float] = []
    for index, real_state in enumerate(real_states):
        action = orbit_engine.hamiltonian_apply(
            basis, tables, float(lam), real_state
        )
        energy = float(np.vdot(real_state, action).real)
        for start in range(0, basis.n_orbits, orbit_engine.MATVEC_CHUNK):
            stop = min(start + orbit_engine.MATVEC_CHUNK, basis.n_orbits)
            action[start:stop] -= energy * real_state[start:stop]
        residual = float(np.linalg.norm(action))
        del action
        state = np.asarray(real_state, dtype=np.complex128)
        norm_error = abs(float(np.vdot(state, state).real) - 1.0)
        if residual > GROUND_RESIDUAL_TOL:
            raise RuntimeError(
                f"two-state eigenpair {index} residual {residual:.3e} exceeds 1e-8"
            )
        if norm_error > ORTHOGONALITY_TOL:
            raise RuntimeError(
                f"two-state eigenpair {index} norm error {norm_error:.3e} exceeds 1e-9"
            )
        energies_list.append(energy)
        residuals_list.append(residual)
        complex_states.append(state)
        norm_errors.append(norm_error)
        orbit_engine._guard_rss(
            f"bar two-state Lanczos eigenpair {index}", budget_gb
        )
    overlap = float(abs(np.vdot(complex_states[0], complex_states[1])))
    if overlap > ORTHOGONALITY_TOL:
        raise RuntimeError(f"two-state overlap {overlap:.3e} exceeds 1e-9")
    if energies_list[1] < energies_list[0] - 1.0e-12:
        raise AssertionError("two-state energies are not ordered")
    return TwoStateLanczosResult(
        energies=(energies_list[0], energies_list[1]),
        states=(complex_states[0], complex_states[1]),
        residuals=(residuals_list[0], residuals_list[1]),
        norm_errors=(norm_errors[0], norm_errors[1]),
        overlap=overlap,
    )


def _expand_invariant_slab_state(
    basis: Any, state: npt.NDArray[np.complex128]
) -> ComplexArray:
    """Independent methods-only expansion by rotation images, never lookup."""

    if basis.geometry_name != "open-3x3x2" or basis.n_sites != 18:
        raise RuntimeError("raw complex expansion is restricted to the methods slab")
    geometry = orbit_engine._geometry_for_basis(basis)
    luts = orbit_engine._permutation_luts(geometry)
    raw = np.zeros(1 << basis.n_sites, dtype=np.complex128)
    assigned = np.zeros(raw.size, dtype=bool)
    amplitudes = np.asarray(state, dtype=np.complex128) / np.sqrt(
        basis.orbit_sizes.astype(np.float64)
    )
    for rotation_lut in luts:
        images = orbit_engine._permute_bits(basis.representatives, rotation_lut)
        raw[images] = amplitudes
        assigned[images] = True
    if not np.all(assigned):
        raise AssertionError("independent slab expansion left configurations unassigned")
    return raw


def _direct_class_product_slab(
    basis: Any, vectors: Mapping[str, tuple[complex, complex]]
) -> ComplexArray:
    indices = np.arange(1 << basis.n_sites, dtype=np.uint32)
    classes = _site_class_indices(basis)
    raw = np.ones(indices.size, dtype=np.complex128)
    for class_name in ("center", "face", "edge", "corner"):
        mask = _mask_for_sites(classes[class_name])
        count = orbit_engine._popcount_uint32(indices & mask)
        zero, one = vectors[class_name]
        raw *= np.power(zero, len(classes[class_name]) - count.astype(np.int16))
        raw *= np.power(one, count.astype(np.int16))
    raw /= np.linalg.norm(raw)
    return raw


def _direct_condition_joint(
    joint: npt.NDArray[np.complex128], pointer_basis: str
) -> tuple[tuple[float, float], tuple[ComplexArray, ComplexArray], ComplexArray]:
    matrix = np.asarray(joint, dtype=np.complex128)
    rest = matrix.shape[0] // 2
    tensor = matrix.reshape(2, rest, 2, rest)
    if pointer_basis.upper() == "Z":
        vectors = (
            np.asarray([1.0, 0.0], dtype=np.complex128),
            np.asarray([0.0, 1.0], dtype=np.complex128),
        )
    elif pointer_basis.upper() == "X":
        vectors = (
            np.asarray([1.0, 1.0], dtype=np.complex128) / math.sqrt(2.0),
            np.asarray([1.0, -1.0], dtype=np.complex128) / math.sqrt(2.0),
        )
    else:
        raise ValueError("direct pointer basis must be Z or X")
    probabilities: list[float] = []
    states: list[ComplexArray] = []
    dephased = np.zeros_like(matrix)
    dephased_tensor = dephased.reshape(2, rest, 2, rest)
    for outcome, vector in enumerate(vectors):
        sigma = np.einsum(
            "s,sitj,t->ij", vector.conj(), tensor, vector, optimize=True
        )
        probability = float(np.trace(sigma).real)
        state = np.asarray(sigma / probability, dtype=np.complex128)
        probabilities.append(probability)
        states.append(state)
        dephased_tensor[outcome, :, outcome, :] = sigma
    return (
        (probabilities[0], probabilities[1]),
        (states[0], states[1]),
        dephased,
    )


def _conditional_deviation(
    measured: ConditionalMarginal,
    direct: tuple[tuple[float, float], tuple[ComplexArray, ComplexArray], ComplexArray],
) -> float:
    probabilities, states, dephased = direct
    return max(
        max(abs(measured.probabilities[index] - probabilities[index]) for index in range(2)),
        max(
            float(np.max(np.abs(measured.states[index] - states[index])))
            for index in range(2)
        ),
        float(np.max(np.abs(measured.dephased_joint - dephased))),
    )


def dense_slab_extension_crosscheck() -> dict[str, object]:
    """Validate all seven extension paths against raw slab partial traces."""

    started = time.perf_counter()
    clear_raw_to_orbit_lookup()
    geometry = orbit_engine._slab_geometry()
    basis = orbit_engine._build_basis_for_geometry(geometry)
    tables = orbit_engine.build_hamiltonian_tables(basis)
    lookup = get_raw_to_orbit_lookup(basis, budget_gb=VALIDATION_RSS_GB)
    lookup_checksum = verify_raw_lookup_checksum(lookup)

    vectors = {
        "center": qubit_amplitudes_from_bloch((1.0, 0.0, 0.0)),
        "face": qubit_amplitudes_from_bloch((0.0, 1.0, 0.0)),
        "edge": qubit_amplitudes_from_bloch((0.0, 0.0, 1.0)),
        "corner": qubit_amplitudes_from_bloch((0.0, 0.0, -1.0)),
    }
    reduced_product = class_product_state(basis, **vectors)
    direct_product = _direct_class_product_slab(basis, vectors)
    projected_product = np.sqrt(basis.orbit_sizes.astype(np.float64)) * direct_product[
        basis.representatives
    ]
    class_product_deviation = float(
        np.max(np.abs(reduced_product - projected_product))
    )

    rng = np.random.default_rng(20260710)
    random_state = rng.standard_normal(basis.n_orbits) + 1j * rng.standard_normal(
        basis.n_orbits
    )
    random_state = np.asarray(random_state / np.linalg.norm(random_state), dtype=np.complex128)
    raw_random = _expand_invariant_slab_state(basis, random_state)
    pointer = pointer_site(basis)
    exterior = tuple(site for site in range(basis.n_sites) if site != pointer)
    fragment_a5 = exterior[:5]
    fragment_b5 = exterior[5:10]
    fragment_a4 = fragment_a5[:4]
    fragment_b4 = fragment_b5[:4]

    deviations: dict[str, float] = {
        "class_product": class_product_deviation,
        "k4_z": 0.0,
        "k4_x": 0.0,
        "k5_z": 0.0,
        "k5_x": 0.0,
        "q9_joint": 0.0,
        "q10_joint": 0.0,
        "q11_joint": 0.0,
        "partial_trace": 0.0,
        "doublet_fragment_mix": 0.0,
        "doublet_pair_mix": 0.0,
    }

    for label, fragment in (("k4", fragment_a4), ("k5", fragment_a5)):
        _, direct_joint = orbit_engine._dense_partial_trace(
            raw_random, basis.n_sites, (pointer,) + fragment
        )
        for pointer_basis_name in ("Z", "X"):
            measured = conditional_fragment_marginal(
                basis,
                lookup,
                (random_state,),
                fragment,
                pointer_basis=pointer_basis_name,
                pointer=pointer,
                budget_gb=VALIDATION_RSS_GB,
            )
            direct = _direct_condition_joint(direct_joint, pointer_basis_name)
            deviations[f"{label}_{pointer_basis_name.lower()}"] = _conditional_deviation(
                measured, direct
            )
            one_site = partial_trace_density(measured.states[0], len(fragment), (0,))
            direct_one = partial_trace_density(direct[1][0], len(fragment), (0,))
            deviations["partial_trace"] = max(
                deviations["partial_trace"],
                float(np.max(np.abs(one_site - direct_one))),
            )

    pair_cases = (
        ("q9_joint", fragment_a4, fragment_b4),
        ("q10_joint", fragment_a4, fragment_b5),
        ("q11_joint", fragment_a5, fragment_b5),
    )
    for label, first, second in pair_cases:
        measured_pair = fragment_pair_marginal(
            basis,
            lookup,
            (random_state,),
            first,
            second,
            pointer_basis="Z",
            pointer=pointer,
            budget_gb=VALIDATION_RSS_GB,
        )
        _, direct_joint = orbit_engine._dense_partial_trace(
            raw_random, basis.n_sites, (pointer,) + first + second
        )
        direct = _direct_condition_joint(direct_joint, "Z")
        deviations[label] = _conditional_deviation(measured_pair.conditional, direct)
        direct_a = partial_trace_density(
            direct[1][0], len(first) + len(second), tuple(range(len(first)))
        )
        direct_b = partial_trace_density(
            direct[1][0],
            len(first) + len(second),
            tuple(range(len(first), len(first) + len(second))),
        )
        deviations["partial_trace"] = max(
            deviations["partial_trace"],
            float(np.max(np.abs(measured_pair.fragment_a_states[0] - direct_a))),
            float(np.max(np.abs(measured_pair.fragment_b_states[0] - direct_b))),
        )
        del measured_pair, direct_joint, direct
        orbit_engine._guard_rss(f"extension validation {label}", VALIDATION_RSS_GB)

    doublet = two_lowest_states(
        basis, tables, 0.1, budget_gb=VALIDATION_RSS_GB
    )
    raw_doublet = (
        _expand_invariant_slab_state(basis, doublet.states[0]),
        _expand_invariant_slab_state(basis, doublet.states[1]),
    )
    measured_mix = conditional_fragment_marginal(
        basis,
        lookup,
        doublet.states,
        fragment_a4,
        pointer_basis="Z",
        pointer=pointer,
        weights=(0.5, 0.5),
        budget_gb=VALIDATION_RSS_GB,
    )
    direct_mixed_joint = np.zeros((1 << 5, 1 << 5), dtype=np.complex128)
    for raw_state in raw_doublet:
        _, pure_joint = orbit_engine._dense_partial_trace(
            raw_state, basis.n_sites, (pointer,) + fragment_a4
        )
        direct_mixed_joint += 0.5 * pure_joint
    direct_mix = _direct_condition_joint(direct_mixed_joint, "Z")
    deviations["doublet_fragment_mix"] = _conditional_deviation(
        measured_mix, direct_mix
    )

    measured_pair_mix = fragment_pair_marginal(
        basis,
        lookup,
        doublet.states,
        fragment_a4,
        fragment_b4,
        pointer_basis="X",
        pointer=pointer,
        weights=(0.5, 0.5),
        budget_gb=VALIDATION_RSS_GB,
    )
    direct_mixed_pair_joint = np.zeros((1 << 9, 1 << 9), dtype=np.complex128)
    for raw_state in raw_doublet:
        _, pure_joint = orbit_engine._dense_partial_trace(
            raw_state, basis.n_sites, (pointer,) + fragment_a4 + fragment_b4
        )
        direct_mixed_pair_joint += 0.5 * pure_joint
    direct_pair_mix = _direct_condition_joint(direct_mixed_pair_joint, "X")
    deviations["doublet_pair_mix"] = _conditional_deviation(
        measured_pair_mix.conditional, direct_pair_mix
    )

    maximum_deviation = max(deviations.values())
    elapsed = time.perf_counter() - started
    rss_peak = float(orbit_engine.rss_gb())
    if maximum_deviation > MARGINAL_TOL:
        raise AssertionError(
            f"extension slab maximum deviation {maximum_deviation:.3e} exceeds 1e-9"
        )
    if rss_peak >= VALIDATION_RSS_GB:
        raise RuntimeError(
            f"extension slab RSS {rss_peak:.3f} GiB is not below 4 GiB"
        )
    if elapsed >= VALIDATION_WALL_SECONDS:
        raise RuntimeError(
            f"extension slab wall {elapsed:.1f}s is not below 900s"
        )
    result = {
        "schema": EXTENSION_VALIDATION_SCHEMA,
        "geometry": basis.geometry_name,
        "slab_orbits": int(basis.n_orbits),
        "deviations": deviations,
        "maximum_deviation": maximum_deviation,
        "lookup_checksum": lookup_checksum,
        "lookup_build_seconds": lookup.build_seconds,
        "doublet_energies": list(doublet.energies),
        "doublet_residuals": list(doublet.residuals),
        "doublet_overlap": doublet.overlap,
        "rss_peak_gb": rss_peak,
        "elapsed_seconds": elapsed,
    }
    clear_raw_to_orbit_lookup()
    return result


__all__ = [
    "ConditionalMarginal",
    "DensitySummary",
    "FragmentDescriptorSet",
    "PairConditionalMarginal",
    "RawOrbitLookup",
    "TwoStateLanczosResult",
    "FRAGMENT_CLASS_MEMBERS",
    "FRAGMENT_CLASS_ORDER",
    "FRAGMENT_COORDINATES",
    "FRAGMENT_LABEL_ORDER",
    "PAIR_CLASS_MEMBERS",
    "PAIR_CLASS_ORDER",
    "class_product_state",
    "center_bond_runtime_tables",
    "clear_raw_to_orbit_lookup",
    "conditional_fragment_marginal",
    "coordinate_sites",
    "dense_slab_extension_crosscheck",
    "density_summary",
    "fragment_pair_marginal",
    "fragment_sites",
    "gather_subset_density",
    "get_raw_to_orbit_lookup",
    "holevo_bits",
    "partial_trace_density",
    "pointer_site",
    "qubit_amplitudes_from_bloch",
    "two_lowest_states",
    "verify_fragment_descriptors",
    "verify_raw_lookup_checksum",
]
