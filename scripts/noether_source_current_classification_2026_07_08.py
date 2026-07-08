#!/usr/bin/env python3
"""Classify bounded-support conserved densities in the two-species matter chain.

This runner uses exact normal-ordered fermionic algebra for the infinite
two-site-cell translation-covariant problem.  The candidate density basis is
number-conserving per species, Hermitian, anchored at minimum site 0 or 1, and
restricted to fermionic degree <= 4 in support windows W_SITES=4 and 6.

The finite-ring JW string sanity check is retained as CHECK-00.  CHECK-00b
validates the symbolic CAR normal-ordering engine against sparse many-body
matrices on an open 8-site, two-species chain.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import argparse
import importlib.util
import itertools
import math
from pathlib import Path
import sys
import time
from typing import Iterable

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp


sys.dont_write_bytecode = True

RNG_SEED = 20260708
CHECK_TOL = 1.0e-12
ANGLE_TOL = 1.0e-10
GAUGE_ANGLE_FALLBACK = 1.0e-6
KERNEL_SINGULAR_TOL = 1.0e-6
GAP_FACTOR = 1.0e6
CLEAN_TOL = 1.0e-14
CELL_SITES = 2
CELL_QUBITS = 4

Mode = tuple[int, int]  # (site, species_index), species_index: a=0, b=1
FKey = tuple[tuple[Mode, ...], tuple[Mode, ...]]
Token = tuple[int, int, int]  # (1 for creation, 0 for annihilation, site, species)


@dataclass(frozen=True)
class Couplings:
    t_a: float
    t_b: float
    m_a: float
    m_b: float
    U: float
    V_a: float
    V_b: float
    W_ab: float


@dataclass(frozen=True, order=True)
class PauliKey:
    anchor: int
    letters: str


@dataclass
class FermionBasis:
    window: int
    monomials: list[FKey]
    ops: list[dict[FKey, complex]]
    labels: list[str]
    self_cols: dict[FKey, int]
    pair_reps: dict[FKey, tuple[FKey, complex, int, int]]
    pair_adjs: dict[FKey, tuple[FKey, complex, int, int]]


@dataclass
class KernelResult:
    dim: int
    singular_values: np.ndarray
    gap: float
    kernel_basis: np.ndarray
    matrix: sp.csr_matrix
    basis: FermionBasis
    row_count: int
    overflow_norm: float


PAULI_MUL: dict[tuple[str, str], tuple[int, str]] = {
    ("I", "I"): (0, "I"),
    ("I", "X"): (0, "X"),
    ("I", "Y"): (0, "Y"),
    ("I", "Z"): (0, "Z"),
    ("X", "I"): (0, "X"),
    ("Y", "I"): (0, "Y"),
    ("Z", "I"): (0, "Z"),
    ("X", "X"): (0, "I"),
    ("Y", "Y"): (0, "I"),
    ("Z", "Z"): (0, "I"),
    ("X", "Y"): (1, "Z"),
    ("Y", "Z"): (1, "X"),
    ("Z", "X"): (1, "Y"),
    ("Y", "X"): (3, "Z"),
    ("Z", "Y"): (3, "X"),
    ("X", "Z"): (3, "Y"),
}


def random_couplings(rng: np.random.Generator) -> Couplings:
    return Couplings(*map(float, rng.uniform(0.3, 1.7, size=8)))


def free_like(c: Couplings) -> Couplings:
    return Couplings(c.t_a, c.t_b, c.m_a, c.m_b, 0.0, 0.0, 0.0, 0.0)


def decoupled_like(c: Couplings) -> Couplings:
    return Couplings(c.t_a, c.t_b, c.m_a, c.m_b, 0.0, c.V_a, c.V_b, 0.0)


def species_index(species: str) -> int:
    if species == "a":
        return 0
    if species == "b":
        return 1
    raise ValueError(species)


def mode(site: int, species: str | int) -> Mode:
    return (site, species if isinstance(species, int) else species_index(species))


def site_qubit(site: int, species: str | int) -> int:
    return 2 * site + (species if isinstance(species, int) else species_index(species))


def mode_qubit(m: Mode) -> int:
    return 2 * m[0] + m[1]


def op_add(accum: dict[FKey, complex], key: FKey, coeff: complex) -> None:
    if abs(coeff) <= CLEAN_TOL:
        return
    accum[key] = accum.get(key, 0.0 + 0.0j) + coeff
    if abs(accum[key]) <= CLEAN_TOL:
        del accum[key]


def op_add_scaled(accum: dict[FKey, complex], op: dict[FKey, complex], scale: complex) -> None:
    if abs(scale) <= CLEAN_TOL:
        return
    for key, coeff in op.items():
        op_add(accum, key, scale * coeff)


def identity_key() -> FKey:
    return ((), ())


def key_degree(key: FKey) -> int:
    return len(key[0]) + len(key[1])


def key_sites(key: FKey) -> list[int]:
    return [m[0] for m in key[0]] + [m[0] for m in key[1]]


def key_bounds(key: FKey) -> tuple[int, int]:
    sites = key_sites(key)
    if not sites:
        raise ValueError("identity has no support")
    return min(sites), max(sites)


def key_width(key: FKey) -> int:
    lo, hi = key_bounds(key)
    return hi - lo + 1


def translate_key(key: FKey, delta_sites: int) -> FKey:
    if delta_sites == 0:
        return key
    return (
        tuple((site + delta_sites, spc) for site, spc in key[0]),
        tuple((site + delta_sites, spc) for site, spc in key[1]),
    )


def anchor_key(key: FKey) -> FKey:
    lo, _ = key_bounds(key)
    anchor = lo % CELL_SITES
    cell_shift = (lo - anchor) // CELL_SITES
    return translate_key(key, -CELL_SITES * cell_shift)


def sort_modes_with_sign(modes: tuple[Mode, ...]) -> tuple[int, tuple[Mode, ...]]:
    if len(set(modes)) != len(modes):
        return 0, ()
    inversions = 0
    for i, left in enumerate(modes):
        for right in modes[i + 1 :]:
            if left > right:
                inversions += 1
    return (-1 if inversions & 1 else 1), tuple(sorted(modes))


def cleaned_items(accum: dict[FKey, complex]) -> tuple[tuple[FKey, complex], ...]:
    return tuple(sorted((key, coeff) for key, coeff in accum.items() if abs(coeff) > CLEAN_TOL))


@lru_cache(maxsize=None)
def normal_order_word(word: tuple[Token, ...]) -> tuple[tuple[FKey, complex], ...]:
    """Normal order a fermion word using c_i c_j^dag = delta_ij - c_j^dag c_i."""
    for idx in range(len(word) - 1):
        left = word[idx]
        right = word[idx + 1]
        if left[0] == 0 and right[0] == 1:
            accum: dict[FKey, complex] = {}
            swapped = word[:idx] + (right, left) + word[idx + 2 :]
            for key, coeff in normal_order_word(swapped):
                op_add(accum, key, -coeff)
            if left[1:] == right[1:]:
                contracted = word[:idx] + word[idx + 2 :]
                for key, coeff in normal_order_word(contracted):
                    op_add(accum, key, coeff)
            return cleaned_items(accum)

    creations = tuple((site, spc) for dagger, site, spc in word if dagger == 1)
    annihilations = tuple((site, spc) for dagger, site, spc in word if dagger == 0)
    sign_c, sorted_c = sort_modes_with_sign(creations)
    sign_a, sorted_a = sort_modes_with_sign(annihilations)
    if sign_c == 0 or sign_a == 0:
        return ()
    return (((sorted_c, sorted_a), complex(sign_c * sign_a)),)


def multiply_monomials(left: FKey, right: FKey) -> dict[FKey, complex]:
    word: list[Token] = []
    word.extend((1, site, spc) for site, spc in left[0])
    word.extend((0, site, spc) for site, spc in left[1])
    word.extend((1, site, spc) for site, spc in right[0])
    word.extend((0, site, spc) for site, spc in right[1])
    return dict(normal_order_word(tuple(word)))


@lru_cache(maxsize=None)
def commutator_key_items(left: FKey, right: FKey) -> tuple[tuple[FKey, complex], ...]:
    accum: dict[FKey, complex] = {}
    for key, coeff in multiply_monomials(left, right).items():
        op_add(accum, key, coeff)
    for key, coeff in multiply_monomials(right, left).items():
        op_add(accum, key, -coeff)
    return cleaned_items(accum)


def multiply_ops(left: dict[FKey, complex], right: dict[FKey, complex]) -> dict[FKey, complex]:
    accum: dict[FKey, complex] = {}
    for l_key, l_coeff in left.items():
        for r_key, r_coeff in right.items():
            for out_key, out_coeff in multiply_monomials(l_key, r_key).items():
                op_add(accum, out_key, l_coeff * r_coeff * out_coeff)
    return accum


def adjoint_monomial(key: FKey) -> tuple[FKey, complex]:
    word: list[Token] = []
    word.extend((1, site, spc) for site, spc in reversed(key[1]))
    word.extend((0, site, spc) for site, spc in reversed(key[0]))
    items = normal_order_word(tuple(word))
    if len(items) != 1:
        raise RuntimeError("adjoint of a canonical monomial was not monomial")
    return items[0]


def number_op(m: Mode) -> dict[FKey, complex]:
    return {((m,), (m,)): 1.0 + 0.0j}


def add_number(accum: dict[FKey, complex], m: Mode, coeff: complex) -> None:
    op_add(accum, ((m,), (m,)), coeff)


def add_monomial(accum: dict[FKey, complex], creations: Iterable[Mode], annihilations: Iterable[Mode], coeff: complex) -> None:
    cre = tuple(sorted(creations))
    ann = tuple(sorted(annihilations))
    if len(set(cre)) != len(cre) or len(set(ann)) != len(ann):
        return
    op_add(accum, (cre, ann), coeff)


def add_hop(accum: dict[FKey, complex], left: Mode, right: Mode, coeff: float) -> None:
    add_monomial(accum, (left,), (right,), coeff)
    add_monomial(accum, (right,), (left,), coeff)


def add_current(accum: dict[FKey, complex], left: Mode, right: Mode, coeff: float) -> None:
    add_monomial(accum, (left,), (right,), -1.0j * coeff)
    add_monomial(accum, (right,), (left,), 1.0j * coeff)


def add_density_product(accum: dict[FKey, complex], left: Mode, right: Mode, coeff: float) -> None:
    product = multiply_ops(number_op(left), number_op(right))
    op_add_scaled(accum, product, coeff)


def build_h_density(c: Couplings, *, part: str = "total") -> dict[FKey, complex]:
    out: dict[FKey, complex] = {}
    include_a = part in {"total", "a"}
    include_b = part in {"total", "b"}
    include_inter = part == "total"

    for site in (0, 1):
        stagger = 1.0 if (site % 2 == 0) else -1.0
        if include_a:
            add_number(out, mode(site, "a"), c.m_a * stagger)
            add_hop(out, mode(site, "a"), mode(site + 1, "a"), -0.5 * c.t_a)
        if include_b:
            add_number(out, mode(site, "b"), c.m_b * stagger)
            add_hop(out, mode(site, "b"), mode(site + 1, "b"), -0.5 * c.t_b)

    for site in (0, 1):
        a0 = mode(site, "a")
        b0 = mode(site, "b")
        if include_inter:
            add_density_product(out, a0, b0, c.U)
            add_density_product(out, a0, mode(site + 1, "b"), c.W_ab)
            add_density_product(out, b0, mode(site + 1, "a"), c.W_ab)
        if include_a:
            add_density_product(out, a0, mode(site + 1, "a"), c.V_a)
        if include_b:
            add_density_product(out, b0, mode(site + 1, "b"), c.V_b)
    return out


def build_charge_operator(species: str) -> dict[FKey, complex]:
    out: dict[FKey, complex] = {}
    for site in (0, 1):
        add_number(out, mode(site, species), 1.0)
    return out


def build_staggered_charge_operator() -> dict[FKey, complex]:
    out: dict[FKey, complex] = {}
    for site in (0, 1):
        stagger = 1.0 if (site % 2 == 0) else -1.0
        add_number(out, mode(site, "a"), stagger)
        add_number(out, mode(site, "b"), stagger)
    return out


def build_current_operator(species: str, c: Couplings) -> dict[FKey, complex]:
    out: dict[FKey, complex] = {}
    t = c.t_a if species == "a" else c.t_b
    for site in (0, 1):
        add_current(out, mode(site, species), mode(site + 1, species), 0.5 * t)
    return out


def candidate_monomials(window: int) -> list[FKey]:
    keys: set[FKey] = set()

    def add_key(creations: Iterable[Mode], annihilations: Iterable[Mode], anchor: int) -> None:
        cre = tuple(sorted(creations))
        ann = tuple(sorted(annihilations))
        if len(set(cre)) != len(cre) or len(set(ann)) != len(ann):
            return
        key = (cre, ann)
        sites = key_sites(key)
        if min(sites) == anchor and max(sites) - min(sites) + 1 <= window:
            keys.add(key)

    for anchor in (0, 1):
        sites = tuple(range(anchor, anchor + window))
        for spc in (0, 1):
            for c_site in sites:
                for a_site in sites:
                    add_key((mode(c_site, spc),), (mode(a_site, spc),), anchor)

            pairs = tuple(itertools.combinations(sites, 2))
            for c_pair in pairs:
                for a_pair in pairs:
                    add_key(
                        (mode(c_pair[0], spc), mode(c_pair[1], spc)),
                        (mode(a_pair[0], spc), mode(a_pair[1], spc)),
                        anchor,
                    )

        for ca_site in sites:
            for cb_site in sites:
                cre = (mode(ca_site, "a"), mode(cb_site, "b"))
                for aa_site in sites:
                    for ab_site in sites:
                        ann = (mode(aa_site, "a"), mode(ab_site, "b"))
                        add_key(cre, ann, anchor)

    return sorted(keys)


def key_label(key: FKey) -> str:
    def fmt(block: tuple[Mode, ...]) -> str:
        return ",".join(f"{site}{'a' if spc == 0 else 'b'}" for site, spc in block)

    return f"C[{fmt(key[0])}]A[{fmt(key[1])}]"


@lru_cache(maxsize=None)
def build_fermion_basis(window: int) -> FermionBasis:
    monomials = candidate_monomials(window)
    monomial_set = set(monomials)
    ops: list[dict[FKey, complex]] = []
    labels: list[str] = []
    self_cols: dict[FKey, int] = {}
    pair_reps: dict[FKey, tuple[FKey, complex, int, int]] = {}
    pair_adjs: dict[FKey, tuple[FKey, complex, int, int]] = {}
    seen: set[FKey] = set()

    for key in monomials:
        if key in seen:
            continue
        adj_key, phase = adjoint_monomial(key)
        if adj_key not in monomial_set:
            raise RuntimeError("candidate enumeration is not adjoint-closed")
        if adj_key == key:
            if abs(phase - 1.0) > CLEAN_TOL:
                raise RuntimeError("self-adjoint monomial has nontrivial adjoint phase")
            col = len(ops)
            ops.append({key: 1.0 + 0.0j})
            labels.append(key_label(key))
            self_cols[key] = col
            seen.add(key)
            continue

        rep = min(key, adj_key)
        other, rep_phase = adjoint_monomial(rep)
        h_col = len(ops)
        ops.append({rep: 1.0 + 0.0j, other: rep_phase})
        labels.append(f"Re[{key_label(rep)}]")
        a_col = len(ops)
        ops.append({rep: 1.0j, other: -1.0j * rep_phase})
        labels.append(f"Im[{key_label(rep)}]")
        pair_reps[rep] = (other, rep_phase, h_col, a_col)
        pair_adjs[other] = (rep, rep_phase, h_col, a_col)
        seen.add(rep)
        seen.add(other)

    return FermionBasis(
        window=window,
        monomials=monomials,
        ops=ops,
        labels=labels,
        self_cols=self_cols,
        pair_reps=pair_reps,
        pair_adjs=pair_adjs,
    )


def operator_to_basis_vector(op: dict[FKey, complex], basis: FermionBasis) -> np.ndarray:
    vec = np.zeros(len(basis.ops), dtype=np.float64)
    for key, col in basis.self_cols.items():
        coeff = op.get(key, 0.0 + 0.0j)
        vec[col] = float(coeff.real)
    for rep, (other, phase, h_col, a_col) in basis.pair_reps.items():
        coeff = op.get(rep, 0.0 + 0.0j)
        if abs(coeff) <= CLEAN_TOL and other in op:
            coeff = np.conjugate(op[other] / phase)
        vec[h_col] = float(coeff.real)
        vec[a_col] = float(coeff.imag)
    return vec


def basis_vector_to_operator(vec: np.ndarray, basis: FermionBasis) -> dict[FKey, complex]:
    out: dict[FKey, complex] = {}
    for col, coeff in enumerate(vec):
        if abs(coeff) <= CLEAN_TOL:
            continue
        op_add_scaled(out, basis.ops[col], float(coeff))
    return out


def overlap_cell_shifts(h_key: FKey, o_key: FKey) -> range:
    h_min, h_max = key_bounds(h_key)
    o_min, o_max = key_bounds(o_key)
    first = math.ceil((o_min - h_max) / CELL_SITES)
    last = math.floor((o_max - h_min) / CELL_SITES)
    return range(first, last + 1)


def build_commutator_matrix(basis: FermionBasis, h_density: dict[FKey, complex]) -> tuple[sp.csr_matrix, int, float]:
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    row_index: dict[FKey, int] = {}
    overflow_sq = 0.0
    h_terms = [(key, coeff) for key, coeff in h_density.items() if key != identity_key() and abs(coeff) > CLEAN_TOL]

    for col, op in enumerate(basis.ops):
        column: dict[FKey, complex] = {}
        for o_key, o_coeff in op.items():
            if o_key == identity_key() or abs(o_coeff) <= CLEAN_TOL:
                continue
            for h_key0, h_coeff in h_terms:
                for shift in overlap_cell_shifts(h_key0, o_key):
                    h_key = translate_key(h_key0, CELL_SITES * shift)
                    scale = h_coeff * o_coeff
                    for out_key, coeff in commutator_key_items(h_key, o_key):
                        if out_key == identity_key():
                            continue
                        op_add(column, anchor_key(out_key), scale * coeff)

        for out_key, coeff in sorted(column.items()):
            if abs(coeff) <= CLEAN_TOL:
                continue
            if key_degree(out_key) > 6 or key_width(out_key) > basis.window + 2:
                overflow_sq += float(abs(coeff) ** 2)
                continue
            row_base = row_index.setdefault(out_key, len(row_index))
            if abs(coeff.real) > CLEAN_TOL:
                rows.append(2 * row_base)
                cols.append(col)
                data.append(float(coeff.real))
            if abs(coeff.imag) > CLEAN_TOL:
                rows.append(2 * row_base + 1)
                cols.append(col)
                data.append(float(coeff.imag))

    mat = sp.coo_matrix((data, (rows, cols)), shape=(2 * len(row_index), len(basis.ops)), dtype=np.float64)
    mat.sum_duplicates()
    mat = mat.tocsr()
    mat.eliminate_zeros()
    return mat, 2 * len(row_index), math.sqrt(overflow_sq)


def dense_kernel(matrix: sp.csr_matrix, basis: FermionBasis, overflow_norm: float) -> KernelResult:
    gram = (matrix.T @ matrix).toarray()
    gram = (gram + gram.T) * 0.5
    evals, evecs = sla.eigh(gram)
    evals = np.maximum(evals.real, 0.0)
    singular = np.sqrt(evals)
    dim = int(np.count_nonzero(singular <= KERNEL_SINGULAR_TOL))
    kernel_basis = evecs[:, :dim].real if dim else np.zeros((matrix.shape[1], 0), dtype=np.float64)
    below = float(np.max(singular[:dim])) if dim else 0.0
    above = float(singular[dim]) if dim < len(singular) else math.inf
    gap = above / max(below, np.finfo(float).tiny)
    return KernelResult(dim, singular, gap, kernel_basis, matrix, basis, matrix.shape[0], overflow_norm)


def classify_for_couplings(c: Couplings, window: int) -> KernelResult:
    basis = build_fermion_basis(window)
    matrix, row_count, overflow = build_commutator_matrix(basis, build_h_density(c))
    result = dense_kernel(matrix, basis, overflow)
    result.row_count = row_count
    return result


def orthonormal_basis(columns: np.ndarray, tol: float = 1.0e-12) -> np.ndarray:
    if columns.size == 0:
        return np.zeros((columns.shape[0], 0), dtype=columns.dtype)
    u, s, _ = sla.svd(columns, full_matrices=False)
    rank = int(np.count_nonzero(s > tol))
    return u[:, :rank]


def principal_angle_to_span(kernel_basis: np.ndarray, known_vectors: np.ndarray) -> float:
    q_kernel = orthonormal_basis(kernel_basis)
    q_known = orthonormal_basis(known_vectors)
    if q_kernel.shape[1] == 0 or q_known.shape[1] == 0:
        return math.pi / 2.0
    residual = q_known - q_kernel @ (q_kernel.conjugate().T @ q_known)
    sin_theta = float(sla.svdvals(residual)[0]) if residual.size else 0.0
    return float(math.asin(np.clip(sin_theta, 0.0, 1.0)))


def vector_angle_to_kernel(kernel_basis: np.ndarray, vector: np.ndarray) -> float:
    norm = float(np.linalg.norm(vector))
    if norm == 0.0 or kernel_basis.shape[1] == 0:
        return math.pi / 2.0
    q_kernel = orthonormal_basis(kernel_basis)
    residual = vector - q_kernel @ (q_kernel.conjugate().T @ vector)
    return float(math.asin(np.clip(np.linalg.norm(residual) / norm, 0.0, 1.0)))


def known_vectors(c: Couplings, basis: FermionBasis) -> np.ndarray:
    return np.column_stack(
        [
            operator_to_basis_vector(build_charge_operator("a"), basis),
            operator_to_basis_vector(build_charge_operator("b"), basis),
            operator_to_basis_vector(build_h_density(c), basis),
        ]
    )


def matrix_residual(result: KernelResult, op: dict[FKey, complex]) -> float:
    vec = operator_to_basis_vector(op, result.basis)
    return float(np.linalg.norm(result.matrix @ vec))


def stabilized_known_gap(result: KernelResult, known: np.ndarray) -> float:
    q_known = orthonormal_basis(known)
    if q_known.shape[1] != result.dim or result.dim == 0:
        return result.gap
    residual_block = result.matrix @ q_known
    below = float(sla.svdvals(residual_block)[0]) if residual_block.size else 0.0
    above = float(result.singular_values[result.dim]) if result.dim < len(result.singular_values) else math.inf
    return above / max(below, np.finfo(float).tiny)


def apply_single_fock(fock: int, qubit: int, create: bool) -> tuple[int, int] | None:
    occupied = (fock >> qubit) & 1
    if create and occupied:
        return None
    if (not create) and not occupied:
        return None
    sign = -1 if ((fock & ((1 << qubit) - 1)).bit_count() & 1) else 1
    return fock ^ (1 << qubit), sign


def apply_cdag_c(fock: int, create_site: int, annihilate_site: int) -> tuple[int, int] | None:
    first = apply_single_fock(fock, annihilate_site, False)
    if first is None:
        return None
    fock_after, sign1 = first
    second = apply_single_fock(fock_after, create_site, True)
    if second is None:
        return None
    fock_out, sign2 = second
    return fock_out, sign1 * sign2


def monomial_sparse(key: FKey, n_sites: int) -> sp.csr_matrix:
    n_modes = 2 * n_sites
    dim = 1 << n_modes
    tokens: list[tuple[bool, int]] = []
    tokens.extend((True, mode_qubit(m)) for m in key[0])
    tokens.extend((False, mode_qubit(m)) for m in key[1])
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    for state in range(dim):
        out = state
        sign = 1
        ok = True
        for create, qubit in reversed(tokens):
            applied = apply_single_fock(out, qubit, create)
            if applied is None:
                ok = False
                break
            out, step_sign = applied
            sign *= step_sign
        if ok:
            rows.append(out)
            cols.append(state)
            data.append(sign)
    mat = sp.coo_matrix((data, (rows, cols)), shape=(dim, dim), dtype=np.complex128)
    mat.sum_duplicates()
    return mat.tocsr()


def operator_sparse(op: dict[FKey, complex], n_sites: int, cache: dict[FKey, sp.csr_matrix] | None = None) -> sp.csr_matrix:
    dim = 1 << (2 * n_sites)
    out = sp.csr_matrix((dim, dim), dtype=np.complex128)
    for key, coeff in op.items():
        if key == identity_key():
            out = out + coeff * sp.identity(dim, format="csr", dtype=np.complex128)
            continue
        if cache is not None:
            mat = cache.get(key)
            if mat is None:
                mat = monomial_sparse(key, n_sites)
                cache[key] = mat
        else:
            mat = monomial_sparse(key, n_sites)
        out = out + coeff * mat
    out.eliminate_zeros()
    return out


def sparse_max_abs(matrix: sp.spmatrix) -> float:
    coo = matrix.tocoo()
    return float(np.max(np.abs(coo.data))) if coo.nnz else 0.0


def check_00b_algebra(rng: np.random.Generator) -> tuple[bool, float]:
    monomials = candidate_monomials(6)
    cache: dict[FKey, sp.csr_matrix] = {}
    worst = 0.0
    for _ in range(20):
        left = monomials[int(rng.integers(0, len(monomials)))]
        right = monomials[int(rng.integers(0, len(monomials)))]
        left_mat = operator_sparse({left: 1.0}, 8, cache)
        right_mat = operator_sparse({right: 1.0}, 8, cache)
        direct = left_mat @ right_mat - right_mat @ left_mat
        symbolic = operator_sparse(dict(commutator_key_items(left, right)), 8, cache)
        diff = direct - symbolic
        diff.eliminate_zeros()
        worst = max(worst, sparse_max_abs(diff))
    return worst <= CHECK_TOL, worst


def pauli_canonical_abs(abs_letters: dict[int, str]) -> PauliKey | None:
    nontrivial = {pos: letter for pos, letter in abs_letters.items() if letter != "I"}
    if not nontrivial:
        return None
    left = min(nontrivial)
    right = max(nontrivial)
    anchor = left % CELL_QUBITS
    cell_shift = (left - anchor) // CELL_QUBITS
    shifted_left = left - CELL_QUBITS * cell_shift
    shifted_right = right - CELL_QUBITS * cell_shift
    letters = [nontrivial.get(pos + CELL_QUBITS * cell_shift, "I") for pos in range(shifted_left, shifted_right + 1)]
    return PauliKey(anchor, "".join(letters))


def add_pauli(accum: dict[PauliKey, float], abs_letters: dict[int, str], coeff: float) -> None:
    key = pauli_canonical_abs(abs_letters)
    if key is None or abs(coeff) == 0.0:
        return
    accum[key] = accum.get(key, 0.0) + float(coeff)
    if abs(accum[key]) < 1.0e-15:
        del accum[key]


def pauli_sparse(n_qubits: int, abs_letters: dict[int, str], coeff: complex) -> sp.csr_matrix:
    dim = 1 << n_qubits
    rows = np.empty(dim, dtype=np.int64)
    cols = np.arange(dim, dtype=np.int64)
    data = np.empty(dim, dtype=np.complex128)
    for state in range(dim):
        out = state
        phase = 1.0 + 0.0j
        for q, letter in abs_letters.items():
            bit = (out >> q) & 1
            if letter == "Z":
                if bit:
                    phase = -phase
            elif letter == "X":
                out ^= 1 << q
            elif letter == "Y":
                phase *= -1.0j if bit else 1.0j
                out ^= 1 << q
        rows[state] = out
        data[state] = coeff * phase
    return sp.coo_matrix((data, (rows, cols)), shape=(dim, dim)).tocsr()


def finite_string_hamiltonian(c: Couplings, n_sites: int) -> sp.csr_matrix:
    n_qubits = 2 * n_sites
    dim = 1 << n_qubits
    out = sp.csr_matrix((dim, dim), dtype=np.complex128)

    def add(abs_letters: dict[int, str], coeff: float) -> None:
        nonlocal out
        out = out + pauli_sparse(n_qubits, abs_letters, coeff)

    def add_density(q1: int, q2: int, coeff: float) -> None:
        add({}, 0.25 * coeff)
        add({q1: "Z"}, -0.25 * coeff)
        add({q2: "Z"}, -0.25 * coeff)
        add({q1: "Z", q2: "Z"}, 0.25 * coeff)

    def add_hopping(p: int, q: int, coeff: float) -> None:
        lo, hi = sorted((p, q))
        middle = {r: "Z" for r in range(lo + 1, hi)}
        add({lo: "X", hi: "X", **middle}, 0.5 * coeff)
        add({lo: "Y", hi: "Y", **middle}, 0.5 * coeff)

    for site in range(n_sites):
        nxt = (site + 1) % n_sites
        stagger = 1.0 if site % 2 == 0 else -1.0
        qa = site_qubit(site, "a")
        qb = site_qubit(site, "b")
        add({}, 0.5 * c.m_a * stagger)
        add({}, 0.5 * c.m_b * stagger)
        add({qa: "Z"}, -0.5 * c.m_a * stagger)
        add({qb: "Z"}, -0.5 * c.m_b * stagger)
        add_hopping(qa, site_qubit(nxt, "a"), -0.5 * c.t_a)
        add_hopping(qb, site_qubit(nxt, "b"), -0.5 * c.t_b)
        add_density(qa, qb, c.U)
        add_density(qa, site_qubit(nxt, "a"), c.V_a)
        add_density(qb, site_qubit(nxt, "b"), c.V_b)
        add_density(qa, site_qubit(nxt, "b"), c.W_ab)
        add_density(qb, site_qubit(nxt, "a"), c.W_ab)
    return out


def finite_fermion_hamiltonian(c: Couplings, n_sites: int) -> sp.csr_matrix:
    n_qubits = 2 * n_sites
    dim = 1 << n_qubits
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    for fock in range(dim):
        diag = 0.0
        for site in range(n_sites):
            nxt = (site + 1) % n_sites
            stagger = 1.0 if site % 2 == 0 else -1.0
            na = (fock >> site_qubit(site, "a")) & 1
            nb = (fock >> site_qubit(site, "b")) & 1
            diag += c.m_a * stagger * na + c.m_b * stagger * nb
            diag += c.U * na * nb
            diag += c.V_a * na * ((fock >> site_qubit(nxt, "a")) & 1)
            diag += c.V_b * nb * ((fock >> site_qubit(nxt, "b")) & 1)
            diag += c.W_ab * na * ((fock >> site_qubit(nxt, "b")) & 1)
            diag += c.W_ab * nb * ((fock >> site_qubit(nxt, "a")) & 1)
        rows.append(fock)
        cols.append(fock)
        data.append(diag)

        for site in range(n_sites):
            nxt = (site + 1) % n_sites
            for spc, t in (("a", c.t_a), ("b", c.t_b)):
                p = site_qubit(site, spc)
                q = site_qubit(nxt, spc)
                for create, annihilate in ((p, q), (q, p)):
                    applied = apply_cdag_c(fock, create, annihilate)
                    if applied is None:
                        continue
                    new_fock, sign = applied
                    rows.append(new_fock)
                    cols.append(fock)
                    data.append(-0.5 * t * sign)
    mat = sp.coo_matrix((data, (rows, cols)), shape=(dim, dim), dtype=np.complex128)
    mat.sum_duplicates()
    return mat.tocsr()


def check_00_jw_sanity(rng: np.random.Generator) -> tuple[bool, float]:
    c = random_couplings(rng)
    string_h = finite_string_hamiltonian(c, 6)
    fermion_h = finite_fermion_hamiltonian(c, 6)
    diff = string_h - fermion_h
    diff.eliminate_zeros()
    err = sparse_max_abs(diff)
    return err <= CHECK_TOL, err


def import_engine():
    engine_path = Path(__file__).with_name("gauged_schwinger_staggered_ed_engine_2026_07_08.py")
    spec = importlib.util.spec_from_file_location("gauged_schwinger_staggered_ed_engine_2026_07_08", engine_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load gauged Schwinger engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def hs_inner(left: sp.spmatrix, right: sp.spmatrix) -> complex:
    return complex(left.conjugate().multiply(right).sum())


def sparse_key(matrix: sp.spmatrix, decimals: int = 12) -> tuple[bytes, bytes, bytes]:
    coo = matrix.tocoo()
    order = np.lexsort((coo.col, coo.row))
    rows = coo.row[order].astype(np.int32)
    cols = coo.col[order].astype(np.int32)
    data = np.round(coo.data[order], decimals=decimals)
    return rows.tobytes(), cols.tobytes(), data.tobytes()


def gauge_diag_operator(engine, basis, values) -> sp.csr_matrix:
    diag = np.empty(basis.dim, dtype=np.complex128)
    for idx in range(basis.dim):
        _local_f, fock, w_index = basis.unpack(idx)
        diag[idx] = values(int(fock), basis.w_value(w_index))
    return sp.diags(diag, format="csr")


def gauge_number_operator(engine, basis, site: int) -> sp.csr_matrix:
    return gauge_diag_operator(engine, basis, lambda fock, _w: (fock >> (site % basis.n_sites)) & 1)


def gauge_charge_operator(engine, basis) -> sp.csr_matrix:
    return gauge_diag_operator(engine, basis, lambda fock, _w: engine.fock_charge(basis.n_sites, fock))


def gauge_e_operator(engine, basis, link: int, power: int) -> sp.csr_matrix:
    link %= basis.n_sites

    def value(fock: int, w: int) -> complex:
        q = engine.charges(basis.n_sites, fock)
        e_val = w + int(np.sum(q[: link + 1]))
        return e_val**power

    return gauge_diag_operator(engine, basis, value)


def gauge_link_forward_operator(engine, basis, link: int) -> sp.csr_matrix:
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    n_sites = basis.n_sites
    link %= n_sites
    right = (link + 1) % n_sites
    is_boundary = link == n_sites - 1
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        applied = engine.apply_cdag_c(fock, link, right)
        if applied is None:
            continue
        new_fock, sign = applied
        new_local = basis.fock_to_local.get(new_fock)
        if new_local is None:
            continue
        for w_index in range(basis.n_w):
            new_w = basis.w_value(w_index) + (1 if is_boundary and basis.rotor else 0)
            new_w_index = basis.w_index_from_value(new_w)
            if new_w_index is None:
                continue
            rows.append(basis.index(new_local, new_w_index))
            cols.append(basis.index(local_f, w_index))
            data.append(sign)
    mat = sp.coo_matrix((data, (rows, cols)), shape=(basis.dim, basis.dim), dtype=np.complex128)
    mat.sum_duplicates()
    return mat.tocsr()


def traceless(op: sp.spmatrix) -> sp.csr_matrix:
    csr = op.tocsr()
    dim = csr.shape[0]
    trace = complex(csr.diagonal().sum())
    if abs(trace) > CLEAN_TOL:
        csr = csr - (trace / dim) * sp.identity(dim, format="csr", dtype=np.complex128)
    csr.eliminate_zeros()
    return csr


def check_05_gauged(rng: np.random.Generator) -> tuple[bool, str]:
    engine = import_engine()
    n_sites = 8
    w_max = 3
    mass = float(rng.uniform(0.5, 1.3))
    coupling = float(rng.uniform(0.5, 1.3))
    basis = engine.Basis(n_sites=n_sites, w_max=w_max, charge_sector=None, rotor=True)
    hamiltonian = engine.build_many_body_hamiltonian(
        basis,
        mass,
        coupling,
        boundary_holonomy_shifts_w=True,
    ).tocsr()

    primitive_cache: dict[tuple[str, int], sp.csr_matrix] = {}

    def primitive(kind: str, offset: int) -> sp.csr_matrix:
        site = offset % n_sites
        key = (kind, site)
        if key in primitive_cache:
            return primitive_cache[key]
        if kind == "n":
            op = gauge_number_operator(engine, basis, site)
        elif kind == "E":
            op = gauge_e_operator(engine, basis, site, 1)
        elif kind == "E2":
            op = gauge_e_operator(engine, basis, site, 2)
        elif kind == "F":
            op = gauge_link_forward_operator(engine, basis, site)
        else:
            raise ValueError(kind)
        primitive_cache[key] = op
        return op

    def translated_single_sum(kind: str, offset: int) -> sp.csr_matrix:
        total = sp.csr_matrix((basis.dim, basis.dim), dtype=np.complex128)
        for cell_shift in range(0, n_sites, CELL_SITES):
            total = total + primitive(kind, offset + cell_shift)
        return total

    def translated_product_sum(pattern: tuple[tuple[str, int], ...]) -> sp.csr_matrix:
        total = sp.csr_matrix((basis.dim, basis.dim), dtype=np.complex128)
        for cell_shift in range(0, n_sites, CELL_SITES):
            prod = sp.identity(basis.dim, format="csr", dtype=np.complex128)
            for kind, offset in pattern:
                prod = prod @ primitive(kind, offset + cell_shift)
            total = total + prod
        return total

    ops: list[sp.csr_matrix] = []
    seen: set[tuple[bytes, bytes, bytes]] = set()

    def add_op(op: sp.spmatrix) -> None:
        candidate = traceless(op)
        norm = math.sqrt(max(0.0, abs(hs_inner(candidate, candidate))))
        if norm <= 1.0e-10:
            return
        key = sparse_key(candidate)
        if key in seen:
            return
        seen.add(key)
        ops.append(candidate)

    for offset in (0, 1):
        add_op(translated_single_sum("n", offset))
        add_op(translated_single_sum("E", offset))
        add_op(translated_single_sum("E2", offset))
        f_sum = translated_single_sum("F", offset)
        add_op((f_sum + f_sum.getH()) * 0.5)
        add_op((f_sum - f_sum.getH()) * (-0.5j))

    for site_offset in (0, 1, 2):
        for link_offset in (0, 1):
            lo = min(site_offset, link_offset)
            hi = max(site_offset, link_offset + 1)
            if hi - lo + 1 <= 3:
                add_op(translated_product_sum((("n", site_offset), ("E", link_offset))))

    q_total = gauge_charge_operator(engine, basis)
    add_op(q_total)
    add_op(hamiltonian)

    n_ops = len(ops)
    gram = np.empty((n_ops, n_ops), dtype=np.complex128)
    comm_gram = np.empty((n_ops, n_ops), dtype=np.complex128)
    comms = [(hamiltonian @ op - op @ hamiltonian).tocsr() for op in ops]
    for i in range(n_ops):
        gram[i, i] = hs_inner(ops[i], ops[i])
        comm_gram[i, i] = hs_inner(comms[i], comms[i])
        for j in range(i + 1, n_ops):
            gij = hs_inner(ops[i], ops[j])
            cij = hs_inner(comms[i], comms[j])
            gram[i, j] = gij
            gram[j, i] = np.conjugate(gij)
            comm_gram[i, j] = cij
            comm_gram[j, i] = np.conjugate(cij)

    evals, evecs = sla.eigh((gram + gram.conjugate().T) * 0.5)
    keep = evals > max(1.0e-10, 1.0e-12 * float(np.max(evals.real)))
    transform = evecs[:, keep] / np.sqrt(evals[keep])[None, :]
    c_orth = transform.conjugate().T @ comm_gram @ transform
    c_orth = (c_orth + c_orth.conjugate().T) * 0.5
    liouville_evals, liouville_vecs = sla.eigh(c_orth)
    singular = np.sqrt(np.maximum(liouville_evals.real, 0.0))
    kernel_mask = singular <= GAUGE_ANGLE_FALLBACK
    kernel = liouville_vecs[:, kernel_mask]
    kernel_dim = int(np.count_nonzero(kernel_mask))

    known_coords = []
    for known in (traceless(q_total), traceless(hamiltonian)):
        overlaps = np.array([hs_inner(op, known) for op in ops], dtype=np.complex128)
        known_coords.append(transform.conjugate().T @ overlaps)
    known_matrix = np.column_stack(known_coords)
    angle = principal_angle_to_span(kernel, known_matrix)
    ok = kernel_dim == 2 and angle <= GAUGE_ANGLE_FALLBACK
    kernel_tail = float(np.max(singular[kernel_mask])) if kernel_dim else math.inf
    note = ",TRUNCATION-NOTE" if ok and (angle > 1.0e-8 or kernel_tail > 1.0e-8) else ""
    detail = f"traceless_dim={kernel_dim},ops={n_ops},angle={angle:.1e},m={mass:.3g},g={coupling:.3g}{note}"
    return ok, detail


def run_smoke() -> int:
    started = time.time()
    rng = np.random.default_rng(RNG_SEED)
    ok00, err00 = check_00_jw_sanity(rng)
    ok00b, err00b = check_00b_algebra(rng)
    c = random_couplings(rng)
    result = classify_for_couplings(c, 4)
    known = known_vectors(c, result.basis)
    residual = max(
        matrix_residual(result, build_charge_operator("a")),
        matrix_residual(result, build_charge_operator("b")),
        matrix_residual(result, build_h_density(c)),
    )
    angle = principal_angle_to_span(result.kernel_basis, known)
    gap = stabilized_known_gap(result, known)
    ok = (
        ok00
        and ok00b
        and result.dim == 3
        and gap >= GAP_FACTOR
        and angle <= ANGLE_TOL
        and residual <= CHECK_TOL
        and result.overflow_norm <= CHECK_TOL
    )
    elapsed = time.time() - started
    print(f"KERNELS smoke_W4_dim={result.dim},gap={gap:.1e},angle={angle:.1e}")
    print("CONTROLS smoke-not-run")
    print("GAUGED smoke-not-run")
    print(f"CHECKS CHECK-00={'ok' if ok00 else 'FAIL'}({err00:.1e}); CHECK-00b={'ok' if ok00b else 'FAIL'}({err00b:.1e}); CHECK-01-smoke=res={residual:.1e}")
    print(f"TOTAL {'KERNEL-EXACT-3' if ok else 'MACHINERY-FAIL'} elapsed={elapsed:.2f}s notes=smoke")
    return 0 if ok else 1


def run_official(args: argparse.Namespace) -> int:
    started = time.time()
    rng = np.random.default_rng(RNG_SEED)
    notes: list[str] = []
    verdict = "MACHINERY-FAIL"

    try:
        ok00, err00 = check_00_jw_sanity(rng)
        ok00b, err00b = check_00b_algebra(rng)
        generic_draws = [random_couplings(rng) for _ in range(5)]

        results: dict[tuple[int, int], KernelResult] = {}
        for window in (4, 6):
            for idx, c in enumerate(generic_draws):
                results[(window, idx)] = classify_for_couplings(c, window)

        membership_ok = True
        membership_worst = 0.0
        membership_angle = 0.0
        for window in (4, 6):
            for idx, c in enumerate(generic_draws[:3]):
                result = results[(window, idx)]
                residual = max(
                    matrix_residual(result, build_charge_operator("a")),
                    matrix_residual(result, build_charge_operator("b")),
                    matrix_residual(result, build_h_density(c)),
                )
                angle = principal_angle_to_span(result.kernel_basis, known_vectors(c, result.basis))
                membership_worst = max(membership_worst, residual)
                membership_angle = max(membership_angle, angle)
                membership_ok = membership_ok and residual <= CHECK_TOL and angle <= ANGLE_TOL

        generic_ok = True
        any_larger = False
        min_gap = math.inf
        max_angle = 0.0
        max_overflow = 0.0
        dim_tokens: list[str] = []
        for window in (4, 6):
            dims: list[int] = []
            for idx, c in enumerate(generic_draws):
                result = results[(window, idx)]
                known = known_vectors(c, result.basis)
                angle = principal_angle_to_span(result.kernel_basis, known)
                gap = stabilized_known_gap(result, known)
                dims.append(result.dim)
                min_gap = min(min_gap, gap)
                max_angle = max(max_angle, angle)
                max_overflow = max(max_overflow, result.overflow_norm)
                any_larger = any_larger or result.dim > 3
                generic_ok = (
                    generic_ok
                    and result.dim == 3
                    and gap >= GAP_FACTOR
                    and angle <= ANGLE_TOL
                    and result.overflow_norm <= CHECK_TOL
                )
            dim_tokens.append(f"W{window}={dims}")

        base = generic_draws[0]
        c_free = free_like(base)
        free_result = classify_for_couplings(c_free, 6)
        ha_vec = operator_to_basis_vector(build_h_density(c_free, part="a"), free_result.basis)
        hb_vec = operator_to_basis_vector(build_h_density(c_free, part="b"), free_result.basis)
        free_ha = vector_angle_to_kernel(free_result.kernel_basis, ha_vec)
        free_hb = vector_angle_to_kernel(free_result.kernel_basis, hb_vec)
        free_ok = free_result.dim > 3 and free_ha <= ANGLE_TOL and free_hb <= ANGLE_TOL
        if free_result.dim <= 4:
            notes.append(f"free-control-dim-not-strictly-above-4:{free_result.dim}")

        c_partial = decoupled_like(base)
        partial_result = classify_for_couplings(c_partial, 6)
        pha_vec = operator_to_basis_vector(build_h_density(c_partial, part="a"), partial_result.basis)
        phb_vec = operator_to_basis_vector(build_h_density(c_partial, part="b"), partial_result.basis)
        partial_ha = vector_angle_to_kernel(partial_result.kernel_basis, pha_vec)
        partial_hb = vector_angle_to_kernel(partial_result.kernel_basis, phb_vec)
        partial_ok = partial_result.dim >= 4 and partial_ha <= ANGLE_TOL and partial_hb <= ANGLE_TOL

        absentee_ok = True
        absentee_min = math.inf
        absentee_tokens: list[str] = []
        for window in (4, 6):
            local_min = math.inf
            for idx, c in enumerate(generic_draws):
                result = results[(window, idx)]
                for op in (
                    build_staggered_charge_operator(),
                    build_current_operator("a", c),
                    build_current_operator("b", c),
                ):
                    residual = matrix_residual(result, op)
                    local_min = min(local_min, residual)
                    absentee_min = min(absentee_min, residual)
            absentee_tokens.append(f"W{window}:{local_min:.1e}")
        absentee_ok = absentee_min >= 1.0e-3

        if args.skip_gauged:
            gauged_ok = True
            gauged_detail = "skipped"
        else:
            gauged_ok, gauged_detail = check_05_gauged(rng)

        machinery_ok = ok00 and ok00b and membership_ok and free_ok and partial_ok and absentee_ok and gauged_ok
        if machinery_ok and generic_ok:
            verdict = "KERNEL-EXACT-3"
        elif machinery_ok and any_larger:
            verdict = "KERNEL-LARGER"
        else:
            verdict = "MACHINERY-FAIL"

        kernel_line = (
            f"{' '.join(dim_tokens)},min_gap={min_gap:.1e},max_angle={max_angle:.1e},"
            f"rowsW4={results[(4, 0)].row_count},rowsW6={results[(6, 0)].row_count},overflow={max_overflow:.1e}"
        )
        control_line = (
            f"free_W6_dim={free_result.dim},HaHb=({free_ha:.1e},{free_hb:.1e}); "
            f"decoupled_W6_dim={partial_result.dim},HaHb=({partial_ha:.1e},{partial_hb:.1e}); "
            f"absentees_min={absentee_min:.1e}[{','.join(absentee_tokens)}]"
        )
        check_line = (
            f"CHECK-00={'ok' if ok00 else 'FAIL'}({err00:.1e}); "
            f"CHECK-00b={'ok' if ok00b else 'FAIL'}({err00b:.1e}); "
            f"CHECK-01={'ok' if membership_ok else 'FAIL'}(res={membership_worst:.1e},ang={membership_angle:.1e}); "
            f"CHECK-02={'ok' if generic_ok else 'FAIL'}; "
            f"CHECK-03={'ok' if free_ok else 'FAIL'}; "
            f"CHECK-04={'ok' if partial_ok else 'FAIL'}; "
            f"CHECK-05={'ok' if gauged_ok else 'FAIL'}; "
            f"CHECK-06={'ok' if absentee_ok else 'FAIL'}"
        )

    except Exception as exc:
        notes.append(f"execution-stopped:{type(exc).__name__}:{exc}")
        kernel_line = "generic=blocked"
        control_line = "free=blocked decoupled=blocked absentees=blocked"
        gauged_detail = "blocked"
        check_line = "CHECK-00/00b/01/02/03/04/05/06=blocked"

    elapsed = time.time() - started
    note_text = "none" if not notes else "|".join(notes)
    print(f"KERNELS {kernel_line}")
    print(f"CONTROLS {control_line}")
    print(f"GAUGED {gauged_detail}")
    print(f"CHECKS {check_line}")
    print(f"TOTAL {verdict} elapsed={elapsed:.2f}s notes={note_text}")
    return 0 if verdict == "KERNEL-EXACT-3" else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-gauged", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.smoke:
        return run_smoke()
    return run_official(args)


if __name__ == "__main__":
    raise SystemExit(main())
