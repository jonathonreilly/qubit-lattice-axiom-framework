#!/usr/bin/env python3
"""Deterministic SU(3) fundamental-fusion CG library for the B4 packet.

The construction is intentionally local to the repository task:

* seed (0,0), (1,0), and (0,1) generator matrices;
* realize higher irreps by projecting 3 x (p,q) with the quadratic Casimir;
* align every product eigenspace to the realized target basis by an
  intertwiner recovered from generator actions;
* expose normalized isometries V: H_target -> H_carrier x H_source.

No random sampling, external tables, runtime dates, or fitted values are used.
The one-step closure halo is built so products from B4 have full completeness
checks; the W44 contraction can still restrict its state labels to B4.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction

import numpy as np


Label = tuple[int, int]

FUND: Label = (1, 0)
ANTIFUND: Label = (0, 1)
ZERO: Label = (0, 0)


@dataclass(frozen=True)
class Irrep:
    label: Label
    generators: tuple[np.ndarray, ...]
    construction: str

    @property
    def dim(self) -> int:
        return int(self.generators[0].shape[0])


@dataclass(frozen=True)
class FusionIsometry:
    carrier: str
    source: Label
    target: Label
    matrix: np.ndarray
    intertwiner_residual: float
    orthonormal_error: float
    projector_error: float
    generic_gap: float


@dataclass(frozen=True)
class Library:
    irreps: dict[Label, Irrep]
    fundamental_isometries: dict[tuple[Label, Label], FusionIsometry]
    antifundamental_isometries: dict[tuple[Label, Label], FusionIsometry]
    c2_degenerate_products: tuple[tuple[str, Label, tuple[Label, ...]], ...]


def dim_su3(label: Label) -> int:
    p, q = label
    return ((p + 1) * (q + 1) * (p + q + 2)) // 2


def c2_fraction(label: Label) -> Fraction:
    p, q = label
    return Fraction(p * p + q * q + p * q, 3) + p + q


def c2_value(label: Label) -> float:
    return float(c2_fraction(label))


def conjugate_label(label: Label) -> Label:
    return (label[1], label[0])


def b4_labels() -> tuple[Label, ...]:
    return tuple((p, q) for p in range(5) for q in range(5))


def closure_labels() -> tuple[Label, ...]:
    """B4 plus the one-step product halo needed for full B4 completeness."""
    labels: set[Label] = set(b4_labels())
    for label in b4_labels():
        labels.update(fundamental_outcomes(label))
        labels.update(antifundamental_outcomes(label))
    return tuple(sorted(labels, key=lambda x: (x[0] + x[1], x[0], x[1])))


def fundamental_outcomes(label: Label) -> tuple[Label, ...]:
    p, q = label
    out: list[Label] = [(p + 1, q)]
    if p >= 1:
        out.append((p - 1, q + 1))
    if q >= 1:
        out.append((p, q - 1))
    return tuple(out)


def antifundamental_outcomes(label: Label) -> tuple[Label, ...]:
    p, q = label
    out: list[Label] = [(p, q + 1)]
    if q >= 1:
        out.append((p + 1, q - 1))
    if p >= 1:
        out.append((p - 1, q))
    return tuple(out)


def gell_mann() -> tuple[np.ndarray, ...]:
    z = np.zeros((3, 3), dtype=complex)
    out: list[np.ndarray] = []

    m = z.copy()
    m[0, 1] = 1.0
    m[1, 0] = 1.0
    out.append(m)

    m = z.copy()
    m[0, 1] = -1.0j
    m[1, 0] = 1.0j
    out.append(m)

    m = z.copy()
    m[0, 0] = 1.0
    m[1, 1] = -1.0
    out.append(m)

    m = z.copy()
    m[0, 2] = 1.0
    m[2, 0] = 1.0
    out.append(m)

    m = z.copy()
    m[0, 2] = -1.0j
    m[2, 0] = 1.0j
    out.append(m)

    m = z.copy()
    m[1, 2] = 1.0
    m[2, 1] = 1.0
    out.append(m)

    m = z.copy()
    m[1, 2] = -1.0j
    m[2, 1] = 1.0j
    out.append(m)

    m = z.copy()
    m[0, 0] = 1.0 / math.sqrt(3.0)
    m[1, 1] = 1.0 / math.sqrt(3.0)
    m[2, 2] = -2.0 / math.sqrt(3.0)
    out.append(m)
    return tuple(out)


def fundamental_generators() -> tuple[np.ndarray, ...]:
    return tuple(0.5 * lam for lam in gell_mann())


def antifundamental_generators() -> tuple[np.ndarray, ...]:
    return tuple(-gen.T for gen in fundamental_generators())


def structure_constants() -> np.ndarray:
    lam = gell_mann()
    f = np.zeros((8, 8, 8), dtype=float)
    for a in range(8):
        for b in range(8):
            comm = lam[a] @ lam[b] - lam[b] @ lam[a]
            for c in range(8):
                value = (1.0 / (4.0j)) * np.trace(lam[c] @ comm)
                f[a, b, c] = float(value.real)
    return f


def casimir(generators: tuple[np.ndarray, ...] | list[np.ndarray]) -> np.ndarray:
    dim = int(generators[0].shape[0])
    out = np.zeros((dim, dim), dtype=complex)
    for gen in generators:
        out = out + gen @ gen
    return out


def product_generators(
    carrier_generators: tuple[np.ndarray, ...],
    source_generators: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, ...]:
    carrier_dim = int(carrier_generators[0].shape[0])
    source_dim = int(source_generators[0].shape[0])
    eye_carrier = np.eye(carrier_dim, dtype=complex)
    eye_source = np.eye(source_dim, dtype=complex)
    return tuple(
        np.kron(carrier_generators[a], eye_source)
        + np.kron(eye_carrier, source_generators[a])
        for a in range(8)
    )


def c2_degeneracy_report(
    labels: tuple[Label, ...] | None = None,
) -> tuple[tuple[str, Label, tuple[Label, ...]], ...]:
    if labels is None:
        labels = b4_labels()
    rows: list[tuple[str, Label, tuple[Label, ...]]] = []
    for carrier, outcome_fn in (
        ("fund", fundamental_outcomes),
        ("antifund", antifundamental_outcomes),
    ):
        for label in labels:
            groups: dict[Fraction, list[Label]] = {}
            for target in outcome_fn(label):
                groups.setdefault(c2_fraction(target), []).append(target)
            for group in groups.values():
                if len(group) > 1:
                    rows.append((carrier, label, tuple(group)))
    return tuple(rows)


def _select_casimir_block(
    generators: tuple[np.ndarray, ...],
    target: Label,
    tolerance: float = 1.0e-8,
) -> tuple[np.ndarray, np.ndarray, float]:
    c2 = casimir(generators)
    evals, evecs = np.linalg.eigh((c2 + c2.conj().T) / 2.0)
    target_value = c2_value(target)
    target_dim = dim_su3(target)
    order = np.argsort(np.abs(evals - target_value), kind="stable")
    chosen = np.sort(order[:target_dim])
    chosen_evals = evals[chosen]
    max_target_error = float(np.max(np.abs(chosen_evals - target_value)))
    if max_target_error > tolerance:
        raise RuntimeError(
            f"Casimir projector failed for {target}: "
            f"max eigenvalue error {max_target_error:.3e}"
        )
    if len(evals) > target_dim:
        outside = order[target_dim:]
        nearest_outside = float(np.min(np.abs(evals[outside] - target_value)))
        if nearest_outside < 1.0e-6:
            raise RuntimeError(
                f"Casimir block for {target} is not separated: "
                f"nearest outside gap {nearest_outside:.3e}"
            )
    block = evecs[:, chosen]
    projector = block @ block.conj().T
    return block, projector, max_target_error


def _realize_irrep_from_product(
    source: Irrep,
    target: Label,
    carrier_generators: tuple[np.ndarray, ...],
    construction: str,
) -> Irrep:
    product = product_generators(carrier_generators, source.generators)
    block, _projector, _err = _select_casimir_block(product, target)
    generators = tuple(block.conj().T @ gen @ block for gen in product)
    return Irrep(label=target, generators=generators, construction=construction)


def build_irreps(
    target_labels: tuple[Label, ...] | None = None,
) -> dict[Label, Irrep]:
    if target_labels is None:
        target_labels = closure_labels()
    target_set = set(target_labels)
    fund = fundamental_generators()
    anti = antifundamental_generators()
    irreps: dict[Label, Irrep] = {
        ZERO: Irrep(
            ZERO,
            tuple(np.zeros((1, 1), dtype=complex) for _ in range(8)),
            "seed trivial",
        ),
        FUND: Irrep(FUND, fund, "seed fundamental"),
        ANTIFUND: Irrep(ANTIFUND, anti, "seed antifundamental"),
    }
    target_set.update({ZERO, FUND, ANTIFUND})

    while not target_set.issubset(irreps):
        progressed = False
        for source_label in sorted(irreps, key=lambda x: (x[0] + x[1], x[0], x[1])):
            source = irreps[source_label]
            for target in fundamental_outcomes(source_label):
                if target not in target_set or target in irreps:
                    continue
                irreps[target] = _realize_irrep_from_product(
                    source,
                    target,
                    fund,
                    f"Casimir block in 3 x {source_label}",
                )
                progressed = True
        if not progressed:
            missing = sorted(target_set.difference(irreps))
            raise RuntimeError(f"could not realize labels: {missing}")
    return {label: irreps[label] for label in sorted(target_set)}


def _generic_coefficients(dim: int) -> tuple[float, ...]:
    banks = (
        (0.17, -0.31, 0.43, -0.59, 0.67, -0.73, 0.79, -0.83),
        (0.23, 0.41, -0.37, 0.61, -0.71, 0.19, -0.53, 0.89),
        (-0.29, 0.47, 0.13, -0.77, 0.31, -0.43, 0.97, 0.11),
    )
    return banks[dim % len(banks)]


def _generic_probe(
    generators: tuple[np.ndarray, ...],
    coeffs: tuple[float, ...],
) -> np.ndarray:
    """Hermitian polynomial probe used only to align equivalent bases.

    A linear Lie-algebra element can have forced degeneracies in nontrivial
    SU(3) irreps.  Adding fixed anticommutator terms keeps the probe
    deterministic and representation-covariant while separating those
    accidental alignment degeneracies.
    """
    probe = sum(coeffs[a] * generators[a] for a in range(8))
    pairs = (
        (0, 1, 0.071),
        (0, 3, -0.053),
        (1, 4, 0.047),
        (2, 5, -0.061),
        (3, 6, 0.037),
        (4, 7, -0.029),
        (0, 7, 0.019),
        (2, 4, -0.017),
    )
    for a, b, coeff in pairs:
        probe = probe + coeff * (generators[a] @ generators[b] + generators[b] @ generators[a])
    return (probe + probe.conj().T) / 2.0


def _phase_aligned_intertwiner(
    source_generators: tuple[np.ndarray, ...],
    target_generators: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, float, float]:
    dim = int(target_generators[0].shape[0])
    if dim == 1:
        return np.ones((1, 1), dtype=complex), 0.0, float("inf")

    best: tuple[np.ndarray, float, float] | None = None
    coefficient_sets = [
        _generic_coefficients(dim),
        (0.23, 0.41, -0.37, 0.61, -0.71, 0.19, -0.53, 0.89),
        (-0.29, 0.47, 0.13, -0.77, 0.31, -0.43, 0.97, 0.11),
        (0.11, -0.67, 0.31, 0.73, -0.17, 0.83, -0.47, 0.59),
    ]
    for coeffs in coefficient_sets:
        h_source = _generic_probe(source_generators, coeffs)
        h_target = _generic_probe(target_generators, coeffs)
        eval_s, evec_s = np.linalg.eigh(h_source)
        eval_t, evec_t = np.linalg.eigh(h_target)
        order_s = np.argsort(eval_s, kind="stable")
        order_t = np.argsort(eval_t, kind="stable")
        eval_s = eval_s[order_s]
        eval_t = eval_t[order_t]
        evec_s = evec_s[:, order_s]
        evec_t = evec_t[:, order_t]
        spectrum_error = float(np.max(np.abs(eval_s - eval_t)))
        gap = float(np.min(np.diff(eval_t))) if dim > 1 else float("inf")
        if spectrum_error > 1.0e-7 or gap < 1.0e-8:
            continue

        source_in_h = [evec_s.conj().T @ gen @ evec_s for gen in source_generators]
        target_in_h = [evec_t.conj().T @ gen @ evec_t for gen in target_generators]
        phases: list[complex | None] = [None] * dim
        phases[0] = 1.0 + 0.0j
        queue = [0]
        edge_tol = 1.0e-10
        while queue:
            j = queue.pop(0)
            assert phases[j] is not None
            phase_j = phases[j]
            for gen_s, gen_t in zip(source_in_h, target_in_h, strict=True):
                for i in range(dim):
                    if phases[i] is not None:
                        continue
                    den = gen_t[i, j]
                    num = gen_s[i, j]
                    if abs(den) <= edge_tol or abs(num) <= edge_tol:
                        continue
                    ratio = num * phase_j / den
                    if abs(ratio) <= edge_tol:
                        continue
                    phases[i] = ratio / abs(ratio)
                    queue.append(i)
        if any(phase is None for phase in phases):
            continue

        phase_vec = np.array([complex(phase) for phase in phases], dtype=complex)
        unitary = evec_s @ np.diag(phase_vec) @ evec_t.conj().T
        residual = max(
            float(np.max(np.abs(source_generators[a] @ unitary - unitary @ target_generators[a])))
            for a in range(8)
        )
        if best is None or residual < best[1]:
            best = (unitary, residual, gap)
        if residual < 1.0e-9:
            return unitary, residual, gap

    if best is None:
        raise RuntimeError(f"failed to align {dim}-dimensional intertwiner")
    return best


def build_isometry(
    irreps: dict[Label, Irrep],
    source_label: Label,
    target_label: Label,
    carrier: str,
) -> FusionIsometry:
    if carrier == "fund":
        carrier_generators = fundamental_generators()
    elif carrier == "antifund":
        carrier_generators = antifundamental_generators()
    else:
        raise ValueError(f"unknown carrier: {carrier}")

    source = irreps[source_label]
    target = irreps[target_label]
    product = product_generators(carrier_generators, source.generators)
    block, projector, _casimir_error = _select_casimir_block(product, target_label)
    restricted = tuple(block.conj().T @ gen @ block for gen in product)
    unitary, residual, gap = _phase_aligned_intertwiner(restricted, target.generators)
    matrix = block @ unitary
    ident = np.eye(target.dim, dtype=complex)
    orth = float(np.max(np.abs(matrix.conj().T @ matrix - ident)))
    proj = float(np.max(np.abs(matrix @ matrix.conj().T - projector)))
    residual = max(
        residual,
        max(
            float(
                np.max(
                    np.abs(product[a] @ matrix - matrix @ target.generators[a])
                )
            )
            for a in range(8)
        ),
    )
    return FusionIsometry(
        carrier=carrier,
        source=source_label,
        target=target_label,
        matrix=matrix,
        intertwiner_residual=float(residual),
        orthonormal_error=orth,
        projector_error=proj,
        generic_gap=gap,
    )


def build_library(
    include_closure_halo: bool = True,
) -> Library:
    labels = closure_labels() if include_closure_halo else b4_labels()
    irreps = build_irreps(labels)
    fundamental: dict[tuple[Label, Label], FusionIsometry] = {}
    antifundamental: dict[tuple[Label, Label], FusionIsometry] = {}
    for source in b4_labels():
        for target in fundamental_outcomes(source):
            if target in irreps:
                fundamental[(source, target)] = build_isometry(
                    irreps, source, target, "fund"
                )
        for target in antifundamental_outcomes(source):
            if target in irreps:
                antifundamental[(source, target)] = build_isometry(
                    irreps, source, target, "antifund"
                )
    return Library(
        irreps=irreps,
        fundamental_isometries=fundamental,
        antifundamental_isometries=antifundamental,
        c2_degenerate_products=c2_degeneracy_report(b4_labels()),
    )


def commutator_residual(irrep: Irrep, f: np.ndarray | None = None) -> float:
    if f is None:
        f = structure_constants()
    worst = 0.0
    for a in range(8):
        for b in range(8):
            lhs = irrep.generators[a] @ irrep.generators[b] - irrep.generators[b] @ irrep.generators[a]
            rhs = 1.0j * sum(f[a, b, c] * irrep.generators[c] for c in range(8))
            worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    return worst


def casimir_residual(irrep: Irrep) -> float:
    c2 = casimir(irrep.generators)
    ident = np.eye(irrep.dim, dtype=complex)
    return float(np.max(np.abs(c2 - c2_value(irrep.label) * ident)))


def completeness_residual(
    library: Library,
    source: Label,
    carrier: str,
) -> tuple[float, int, int]:
    if carrier == "fund":
        isometries = [
            library.fundamental_isometries[(source, target)].matrix
            for target in fundamental_outcomes(source)
            if (source, target) in library.fundamental_isometries
        ]
    elif carrier == "antifund":
        isometries = [
            library.antifundamental_isometries[(source, target)].matrix
            for target in antifundamental_outcomes(source)
            if (source, target) in library.antifundamental_isometries
        ]
    else:
        raise ValueError(f"unknown carrier: {carrier}")
    product_dim = 3 * library.irreps[source].dim
    accum = np.zeros((product_dim, product_dim), dtype=complex)
    target_dim_sum = 0
    for matrix in isometries:
        accum = accum + matrix @ matrix.conj().T
        target_dim_sum += int(matrix.shape[1])
    err = float(np.max(np.abs(accum - np.eye(product_dim, dtype=complex))))
    return err, product_dim, target_dim_sum


def partial_fundamental_trace(isometry: FusionIsometry, source_dim: int) -> np.ndarray:
    target_dim = int(isometry.matrix.shape[1])
    tensor = isometry.matrix.reshape(3, source_dim, target_dim)
    return np.einsum("iat,jat->ij", tensor, tensor.conj(), optimize=True)


def singlet_projector_factor(
    fund_iso: FusionIsometry,
    anti_iso: FusionIsometry,
    fund_source_dim: int,
    anti_source_dim: int,
) -> float:
    """Phase-insensitive factor from two three-character link projectors.

    This evaluates

        Tr[(P_fund x P_antifund)(P_singlet x I_source)] / (d_target_f d_target_a)

    where P = V V^dag and P_singlet is normalized on 3 x 3bar.  It is the
    dimension-stripped fundamental-window bond factor used by the W53 runner.
    """
    rf = partial_fundamental_trace(fund_iso, fund_source_dim)
    ra = partial_fundamental_trace(anti_iso, anti_source_dim)
    target_f = int(fund_iso.matrix.shape[1])
    target_a = int(anti_iso.matrix.shape[1])
    numerator = (1.0 / 3.0) * np.sum(rf * ra).real
    return float(numerator / (target_f * target_a))


def w50_singlet_overlap(library: Library) -> float:
    iso = library.fundamental_isometries[(ANTIFUND, ZERO)].matrix
    expected = (np.eye(3, dtype=complex) / math.sqrt(3.0)).reshape(9, 1)
    return float(abs((expected.conj().T @ iso)[0, 0]))
