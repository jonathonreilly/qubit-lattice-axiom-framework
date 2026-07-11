#!/usr/bin/env python3
"""Class-A certificate for the coupled SU(3)+staggered multi-slice half-space OS Gram.

Paired with docs/RP_COUPLED_MULTISLICE_HALFSPACE_GAUGE_STAGGERED_OS_GRAM_NARROW_THEOREM_NOTE_2026-07-11.md

Self-contained. Implements the ordered-field fermionic Wick recursion once and uses it in
every gate. Every gate is externally anchored (exact hand-derived anchor, independent
spectral product, or a wrong-convention rejector) so a wrong implementation fails.

Claim under test (open reflected lattice, reflection plane between t=0 and t=1,
theta(t)=1-t):
  - Fermion reflection:  theta(chi(x,t)) = -bar(x,1-t),  theta(bar(x,t)) = -chi(x,1-t).
  - Gauge reflection (antilinear on matrix elements):
        theta(U_k(x,t)_{c c'}) = conj( U_k(x,1-t)_{c c'} ).
  - The coupled Berezin OS Gram  G_ij = <theta(F_i) F_j>  on the full multi-slice
    positive-half algebra A_+^half (all monomials supported on slices t>=1) is Hermitian
    and positive semidefinite, with partition function Z = det(D) = prod(m^2+lambda^2) > 0.

Gate map (all deterministic):
  G0    engine anchor (exact 4x4) + engine unphased discriminator
  L4a   open-even determinant positivity (chiral pairing => prod(m^2+lambda^2) > 0)
  L4b   open-odd determinant positivity
  L4c   periodic-odd control genuinely breaks {epsilon, M_KS} = 0
  L2    multi-slice side covariance  I_-[theta(A)] = conj(I_+[A])  under the conj rule
  L3a   exact per-config Hermiticity of the reflected-background multi-slice Gram
  L3b   exact per-config PSD of that Gram
  L3c   crossing-sign-flip convention drives lambda_min strongly negative (discriminates)
  L3d   unphased-reflection convention drives lambda_min strongly negative (discriminates)
  H1a   H=1 reduction union Gram is PSD
  H1b   H=1 one-site/one-color collapse reproduces the exact G0 anchor
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from scipy.stats import unitary_group

TOL = 1.0e-10

Coord = tuple[int, int, int]  # (t, x, color)
Field = tuple[str, Coord]     # ("chi" | "bar", coordinate)


# --------------------------------------------------------------------------- engine
@dataclass(frozen=True)
class Geometry:
    slices: tuple[int, ...]
    ls: int
    nc: int

    def __post_init__(self) -> None:
        if tuple(sorted(self.slices)) != self.slices:
            raise ValueError("slices must be in increasing chronological order")

    @property
    def n(self) -> int:
        return len(self.slices) * self.ls * self.nc

    def index(self, q: Coord) -> int:
        t, x, c = q
        return (self.slices.index(t) * self.ls + x) * self.nc + c


def f(kind: str, t: int, x: int = 0, c: int = 0) -> Field:
    return (kind, (t, x, c))


def su3_batch(rng: np.random.Generator, count: int) -> np.ndarray:
    """Haar U(3) projected to SU(3) by the prescribed cube-root division."""
    u = unitary_group.rvs(3, size=count, random_state=rng)
    dets = np.linalg.det(u)
    roots = np.exp(1j * np.angle(dets) / 3.0)
    return u / roots[:, None, None]


def random_links(
    rng: np.random.Generator, slices: Iterable[int], ls: int
) -> dict[tuple[int, int], np.ndarray]:
    keys = [(t, x) for t in slices for x in range(ls)]
    mats = su3_batch(rng, len(keys))
    return {key: mats[k] for k, key in enumerate(keys)}


def assemble_mks(
    geom: Geometry,
    links: dict[tuple[int, int], np.ndarray] | None,
    *,
    periodic_time: bool = False,
    flip_crossing: bool = False,
) -> np.ndarray:
    """Massless staggered Kogut-Susskind operator M_KS for the given geometry."""
    mks = np.zeros((geom.n, geom.n), dtype=np.complex128)

    if geom.ls > 1:
        if links is None:
            raise ValueError("spatial links are required when L_s > 1")
        for t in geom.slices:
            eta = -1.0 if (t % 2) else 1.0
            for x in range(geom.ls):
                xp = (x + 1) % geom.ls
                u = links[(t, x)]
                udag = u.conj().T
                for c in range(geom.nc):
                    for cp in range(geom.nc):
                        mks[geom.index((t, x, c)), geom.index((t, xp, cp))] += (
                            0.5 * eta * u[c, cp]
                        )
                        mks[geom.index((t, xp, c)), geom.index((t, x, cp))] += (
                            -0.5 * eta * udag[c, cp]
                        )

    temporal_bonds = list(zip(geom.slices[:-1], geom.slices[1:]))
    if periodic_time:
        temporal_bonds.append((geom.slices[-1], geom.slices[0]))
    for ta, tb in temporal_bonds:
        sign = -1.0 if (flip_crossing and {ta, tb} == {0, 1}) else 1.0
        for x in range(geom.ls):
            for c in range(geom.nc):
                ia = geom.index((ta, x, c))
                ib = geom.index((tb, x, c))
                mks[ia, ib] += 0.5 * sign
                mks[ib, ia] += -0.5 * sign
    return mks


def epsilon_matrix(geom: Geometry) -> np.ndarray:
    vals: list[float] = []
    for t in geom.slices:
        for x in range(geom.ls):
            vals.extend([(-1.0) ** (t + x)] * geom.nc)
    return np.diag(np.asarray(vals, dtype=np.complex128))


def theta_fields(
    fields: tuple[Field, ...], phased: bool = True
) -> tuple[complex, tuple[Field, ...]]:
    """Antilinear antiautomorphism on the Grassmann part of a monomial (t -> 1-t)."""
    sign = (-1.0) ** len(fields) if phased else 1.0
    out: list[Field] = []
    for kind, (t, x, c) in reversed(fields):
        mapped_kind = "bar" if kind == "chi" else "chi"
        out.append((mapped_kind, (1 - t, x, c)))
    return complex(sign), tuple(out)


def two_point(a: tuple[str, int], b: tuple[str, int], cov: np.ndarray) -> complex:
    ka, ia = a
    kb, ib = b
    if ka == "chi" and kb == "bar":
        return complex(cov[ia, ib])
    if ka == "bar" and kb == "chi":
        return complex(-cov[ib, ia])
    return 0.0j


def wick_pairing_sum(fields: tuple[tuple[str, int], ...], cov: np.ndarray) -> complex:
    """General ordered-field Wick recursion, including pairing permutation signs."""
    n = len(fields)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2:
        return 0.0j
    first = fields[0]
    ans = 0.0j
    for j in range(1, n):
        contraction = two_point(first, fields[j], cov)
        if contraction == 0.0j:
            continue
        pairing_sign = 1.0 if (j % 2) else -1.0
        remaining = fields[1:j] + fields[j + 1 :]
        ans += pairing_sign * contraction * wick_pairing_sum(remaining, cov)
    return ans


def localized(fields: tuple[Field, ...], geom: Geometry) -> tuple[tuple[str, int], ...]:
    return tuple((kind, geom.index(q)) for kind, q in fields)


def side_integral(
    geom: Geometry, dmat: np.ndarray, fields: tuple[Field, ...], coeff: complex
) -> complex:
    return coeff * np.linalg.det(dmat) * wick_pairing_sum(localized(fields, geom), np.linalg.inv(dmat))


def gram_for_basis(
    geom: Geometry,
    dmat: np.ndarray,
    basis: list[tuple[Field, ...]],
    *,
    phased: bool,
    coefficients: list[complex] | None = None,
    theta_coefficients: list[complex] | None = None,
) -> np.ndarray:
    k = len(basis)
    coefficients = coefficients if coefficients is not None else [1.0 + 0.0j] * k
    theta_coefficients = (
        theta_coefficients if theta_coefficients is not None else [1.0 + 0.0j] * k
    )
    det_d = np.linalg.det(dmat)
    cov = np.linalg.inv(dmat)
    result = np.empty((k, k), dtype=np.complex128)
    reflected = [theta_fields(fields, phased=phased) for fields in basis]
    for i in range(k):
        grassmann_sign, theta_i = reflected[i]
        for j in range(k):
            coeff = grassmann_sign * theta_coefficients[i] * coefficients[j]
            result[i, j] = coeff * det_d * wick_pairing_sum(
                localized(theta_i + basis[j], geom), cov
            )
    return result


def hermitize(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.conj().T)


def open_pair_product(mks: np.ndarray, mass: float) -> tuple[float, float]:
    lambdas = np.linalg.eigvalsh(hermitize(-1j * mks))
    positive = lambdas[lambdas > 1.0e-9]
    if len(positive) * 2 != len(lambdas):
        raise AssertionError("unexpected zero mode or unpaired eigenvalue in open test")
    product = float(np.prod(mass * mass + positive * positive))
    pairing_error = float(np.max(np.abs(lambdas + lambdas[::-1])))
    return product, pairing_error


# --------------------------------------------------------------------------- observables
@dataclass(frozen=True)
class Observable:
    name: str
    fields: tuple[Field, ...]
    coefficient: Callable[[dict[tuple[int, int], np.ndarray]], complex]
    theta_coefficient: Callable[[dict[tuple[int, int], np.ndarray]], complex]


def halfspace_observables() -> list[Observable]:
    """A_+^half generators supported on slices t in {1,2}: identity, odd generators on
    BOTH positive slices (so the unphased convention is genuinely sign-discriminating),
    two genuinely multi-slice monomials, and a gauge-dressed spatial hop whose reflected
    coefficient carries the antilinear conjugation."""
    one: Callable[[dict[tuple[int, int], np.ndarray]], complex] = lambda links: 1.0 + 0.0j
    return [
        Observable("1", tuple(), one, one),
        Observable("bar(1,0,0)", (f("bar", 1, 0, 0),), one, one),
        Observable("chi(1,0,0)", (f("chi", 1, 0, 0),), one, one),
        Observable("bar(1,0,0)chi(1,0,0)", (f("bar", 1, 0, 0), f("chi", 1, 0, 0)), one, one),
        Observable("bar(1,0,0)chi(2,0,0) [multi]", (f("bar", 1, 0, 0), f("chi", 2, 0, 0)), one, one),
        Observable("chi(1,0,0)chi(2,1,1) [multi]", (f("chi", 1, 0, 0), f("chi", 2, 1, 1)), one, one),
        Observable(
            "U-hop(1) [gauge-dressed]",
            (f("bar", 1, 0, 0), f("chi", 1, 1, 1)),
            lambda links: complex(links[(1, 0)][0, 1]),
            lambda links: complex(np.conj(links[(0, 0)][0, 1])),
        ),
        Observable("bar(2,1,1)", (f("bar", 2, 1, 1),), one, one),
        Observable("chi(2,1,1)", (f("chi", 2, 1, 1),), one, one),
    ]


def reflected_background(
    rng: np.random.Generator, half_slices: tuple[int, ...]
) -> dict[tuple[int, int], np.ndarray]:
    """SU(3) background on the full lattice made reflection-symmetric about t=0/t=1:
    U_k(x, 1-t) = U_k(x, t) as matrices."""
    positive = random_links(rng, half_slices, 2)
    links = dict(positive)
    for (t, x), mat in positive.items():
        links[(1 - t, x)] = mat.copy()
    return links


def gram_from_observables(
    geom: Geometry,
    dmat: np.ndarray,
    links: dict[tuple[int, int], np.ndarray],
    observables: list[Observable],
    *,
    phased: bool,
) -> np.ndarray:
    basis = [o.fields for o in observables]
    coeffs = [o.coefficient(links) for o in observables]
    theta_coeffs = [o.theta_coefficient(links) for o in observables]
    return gram_for_basis(
        geom, dmat, basis, phased=phased, coefficients=coeffs, theta_coefficients=theta_coeffs
    )


# --------------------------------------------------------------------------- gates
def check(results: list[tuple[str, bool, str]], name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def gate_G0(results: list[tuple[str, bool, str]]) -> None:
    geom = Geometry((0, 1), 1, 1)
    dmat = np.eye(2, dtype=np.complex128) + assemble_mks(geom, None)
    basis = [tuple(), (f("bar", 1),), (f("chi", 1),), (f("bar", 1), f("chi", 1))]
    phased = gram_for_basis(geom, dmat, basis, phased=True)
    unphased = gram_for_basis(geom, dmat, basis, phased=False)
    expected = np.array(
        [[1.25, 0, 0, -1.0], [0, 0.5, 0, 0], [0, 0, 0.5, 0], [-1.0, 0, 0, 1.0]],
        dtype=np.complex128,
    )
    mismatch = float(np.max(np.abs(phased - expected)))
    un_min = float(np.linalg.eigvalsh(hermitize(unphased))[0])
    check(results, "G0_engine_anchor_exact", mismatch < 1.0e-12,
          f"max entrywise mismatch from exact 4x4 anchor = {mismatch:.3e}")
    check(results, "G0_engine_unphased_discriminates",
          abs(unphased[1, 1].real + 0.5) < 1e-12 and abs(unphased[2, 2].real + 0.5) < 1e-12 and un_min < 0.0,
          f"unphased odd diagonals = {unphased[1,1].real:.3f},{unphased[2,2].real:.3f}; min-eig = {un_min:.3f}")


def gate_L4(results: list[tuple[str, bool, str]]) -> None:
    rng = np.random.default_rng(2026071101)
    masses = (0.1, 0.5, 1.0)
    configs = [random_links(rng, (-1, 0, 1, 2), 2) for _ in range(3)]

    def run_open(label: str, geom: Geometry) -> tuple[bool, str]:
        ok = True
        worst_rel = 0.0
        worst_pair = 0.0
        worst_anti = 0.0
        min_det = float("inf")
        for links_all in configs:
            links = {(t, x): links_all[(t, x)] for t in geom.slices for x in range(geom.ls)}
            mks = assemble_mks(geom, links)
            anti = float(np.linalg.norm(epsilon_matrix(geom) @ mks + mks @ epsilon_matrix(geom), ord="fro"))
            worst_anti = max(worst_anti, anti)
            for mass in masses:
                dmat = mass * np.eye(geom.n, dtype=np.complex128) + mks
                det_d = np.linalg.det(dmat)
                product, pairing_error = open_pair_product(mks, mass)
                rel = abs(det_d.real - product) / max(1.0, abs(det_d.real), abs(product))
                worst_rel = max(worst_rel, rel)
                worst_pair = max(worst_pair, pairing_error)
                min_det = min(min_det, det_d.real)
                ok = ok and abs(det_d.imag) < 1e-10 and det_d.real > 0.0 and rel < 1e-8 and pairing_error < 1e-9 and anti < TOL
        return ok, (f"{label}: min Re(det)={min_det:.4e}>0, max |det-prod(m^2+lam^2)|_rel={worst_rel:.2e}, "
                    f"max pairing err={worst_pair:.2e}, max ||{{eps,M}}||_F={worst_anti:.2e}")

    even_ok, even_detail = run_open("open-even {-1,0,1,2}", Geometry((-1, 0, 1, 2), 2, 3))
    odd_ok, odd_detail = run_open("open-odd {0,1,2}", Geometry((0, 1, 2), 2, 3))
    check(results, "L4a_open_even_det_positive", even_ok, even_detail)
    check(results, "L4b_open_odd_det_positive", odd_ok, odd_detail)

    # periodic-odd control: bipartite anticommutator MUST break, det leaves R_{>0}
    geom = Geometry((0, 1, 2), 2, 3)
    control_broke = True
    worst_anti = 0.0
    saw_complex_or_nonpos = False
    for links_all in configs:
        links = {(t, x): links_all[(t, x)] for t in geom.slices for x in range(geom.ls)}
        mks = assemble_mks(geom, links, periodic_time=True)
        anti = float(np.linalg.norm(epsilon_matrix(geom) @ mks + mks @ epsilon_matrix(geom), ord="fro"))
        worst_anti = min(worst_anti, anti) if worst_anti else anti
        ah = float(np.linalg.norm(mks.conj().T + mks, ord="fro"))
        control_broke = control_broke and anti > 1e-6 and ah < TOL
        for mass in masses:
            det_d = np.linalg.det(mass * np.eye(geom.n, dtype=np.complex128) + mks)
            if abs(det_d.imag) > 1e-10 or det_d.real <= 0.0:
                saw_complex_or_nonpos = True
    check(results, "L4c_periodic_control_breaks", control_broke and saw_complex_or_nonpos,
          f"periodic-odd: ||{{eps,M}}||_F={worst_anti:.3e}>1e-6 (breaks), det leaves R_>0 = {saw_complex_or_nonpos}")


def gate_L2(results: list[tuple[str, bool, str]]) -> None:
    rng = np.random.default_rng(2026071102)
    links = reflected_background(rng, (1, 2))
    gp = Geometry((1, 2), 2, 3)
    gm = Geometry((-1, 0), 2, 3)
    mass = 0.7
    dp = mass * np.eye(gp.n, dtype=np.complex128) + assemble_mks(gp, links)
    dm = mass * np.eye(gm.n, dtype=np.complex128) + assemble_mks(gm, links)
    x, y, c, cp, dcol = 0, 1, 0, 1, 2
    observables = [
        ("A1 multi bilinear", (f("bar", 1, x, c), f("chi", 2, x, c)), 1.0 + 0j, 1.0 + 0j),
        ("A2 multi bilinear", (f("chi", 1, x, c), f("chi", 2, y, cp)), 1.0 + 0j, 1.0 + 0j),
        ("A3 multi quartic",
         (f("bar", 1, x, c), f("chi", 2, x, c), f("bar", 1, y, cp), f("chi", 2, y, cp)), 1.0 + 0j, 1.0 + 0j),
        ("A4 gauge-dressed multi",
         (f("bar", 1, x, c), f("chi", 1, (x + 1) % 2, cp), f("bar", 2, y, dcol), f("chi", 2, y, dcol)),
         complex(links[(1, x)][c, cp]), complex(np.conj(links[(0, x)][c, cp]))),
    ]
    worst = 0.0
    signal = 0.0
    for _, fields, coeff_p, coeff_theta in observables:
        ip = side_integral(gp, dp, fields, coeff_p)
        grassmann_sign, reflected = theta_fields(fields, phased=True)
        im = side_integral(gm, dm, reflected, grassmann_sign * coeff_theta)
        worst = max(worst, float(abs(im - np.conj(ip))))
        signal = max(signal, float(abs(ip)))
    check(results, "L2a_multislice_side_covariance", worst < 1e-9,
          f"max |I_-[theta(A)] - conj(I_+[A])| over 4 multi-slice/gauge-dressed A (conj rule) = {worst:.3e}")
    # Discriminating falsifier: the matrix-element gauge conjugation is load-bearing.
    # Reflecting the gauge-dressed hop A4 WITHOUT conjugating the link element must break
    # covariance by an amount of order the signal itself (not a small numerical residual).
    _, a4_fields, a4_coeff_p, _ = observables[3]
    a4_ip = side_integral(gp, dp, a4_fields, a4_coeff_p)
    a4_sign, a4_reflected = theta_fields(a4_fields, phased=True)
    a4_coeff_theta_noconj = complex(links[(0, x)][c, cp])  # link element, NOT conjugated
    a4_im_noconj = side_integral(gm, dm, a4_reflected, a4_sign * a4_coeff_theta_noconj)
    noconj_residual = float(abs(a4_im_noconj - np.conj(a4_ip)))
    check(results, "L2b_noconj_gauge_discriminates", noconj_residual > 0.1 * signal,
          f"no-conj gauge reflection residual = {noconj_residual:.3e} vs signal scale {signal:.3e} "
          f"(conj-rule residual {worst:.1e})")


def gate_L3(results: list[tuple[str, bool, str]]) -> None:
    geom = Geometry((-1, 0, 1, 2), 2, 3)
    mass = 1.0
    observables = halfspace_observables()
    seeds = (20260711, 20260712, 20260713)
    max_antiherm = 0.0
    min_psd = float("inf")
    max_flip = -float("inf")
    max_unph = -float("inf")
    for seed in seeds:
        rng = np.random.default_rng(seed)
        links = reflected_background(rng, (1, 2))
        dmat = mass * np.eye(geom.n, dtype=np.complex128) + assemble_mks(geom, links)
        dmat_flip = mass * np.eye(geom.n, dtype=np.complex128) + assemble_mks(geom, links, flip_crossing=True)
        g = gram_from_observables(geom, dmat, links, observables, phased=True)
        g_flip = gram_from_observables(geom, dmat_flip, links, observables, phased=True)
        g_unph = gram_from_observables(geom, dmat, links, observables, phased=False)
        max_antiherm = max(max_antiherm, float(np.linalg.norm(g - g.conj().T, ord="fro")))
        min_psd = min(min_psd, float(np.linalg.eigvalsh(hermitize(g))[0]))
        max_flip = max(max_flip, float(np.linalg.eigvalsh(hermitize(g_flip))[0]))
        max_unph = max(max_unph, float(np.linalg.eigvalsh(hermitize(g_unph))[0]))
    check(results, "L3a_exact_per_config_hermitian", max_antiherm < 1e-10,
          f"max ||G-G^dagger||_F over 3 reflected backgrounds = {max_antiherm:.3e} (no Hermitization applied)")
    check(results, "L3b_exact_per_config_psd", min_psd > -1e-9,
          f"min lambda_min(G) over 3 backgrounds = {min_psd:.6e}")
    check(results, "L3c_crossing_flip_discriminates", max_flip < -1e-6,
          f"worst (largest) crossing-flip lambda_min = {max_flip:.4e} << 0")
    check(results, "L3d_unphased_discriminates", max_unph < -1e-6,
          f"worst (largest) unphased lambda_min = {max_unph:.4e} << 0")


def gate_H1(results: list[tuple[str, bool, str]]) -> None:
    rng = np.random.default_rng(2026071104)
    positive = random_links(rng, (1,), 2)
    links = dict(positive)
    for x in range(2):
        links[(0, x)] = positive[(1, x)].copy()
    geom = Geometry((0, 1), 2, 3)
    dmat = np.eye(geom.n, dtype=np.complex128) + assemble_mks(geom, links)
    basis: list[tuple[Field, ...]] = [tuple()]
    for x in range(2):
        for c in range(3):
            basis.extend([(f("bar", 1, x, c),), (f("chi", 1, x, c),),
                          (f("bar", 1, x, c), f("chi", 1, x, c))])
    union = gram_for_basis(geom, dmat, basis, phased=True)
    union_min = float(np.linalg.eigvalsh(hermitize(union))[0])
    union_antiherm = float(np.linalg.norm(union - union.conj().T, ord="fro"))
    check(results, "H1a_union_gram_psd", union_min > -1e-10 and union_antiherm < 1e-10,
          f"19-dim union min-eig = {union_min:.6e}; ||G-G^dagger||_F = {union_antiherm:.3e}")

    # one-site/one-color collapse reproduces the exact G0 anchor
    geom1 = Geometry((0, 1), 1, 1)
    dmat1 = np.eye(2, dtype=np.complex128) + assemble_mks(geom1, None)
    local = [tuple(), (f("bar", 1),), (f("chi", 1),), (f("bar", 1), f("chi", 1))]
    collapse = gram_for_basis(geom1, dmat1, local, phased=True)
    anchor = np.array([[1.25, 0, 0, -1.0], [0, 0.5, 0, 0], [0, 0, 0.5, 0], [-1.0, 0, 0, 1.0]], dtype=np.complex128)
    collapse_mismatch = float(np.max(np.abs(collapse - anchor)))
    check(results, "H1b_collapse_matches_anchor", collapse_mismatch < 1e-12,
          f"one-site/one-color H=1 Gram vs exact anchor: max mismatch = {collapse_mismatch:.3e}")


def main() -> None:
    print("RP coupled SU(3)+staggered multi-slice half-space OS Gram — class-A certificate")
    print("geometry {-1,0,1,2}, L_s=2, N_c=3; reflection theta(t)=1-t, theta(U_{cc'})=conj(U_{cc'}) at 1-t\n")
    results: list[tuple[str, bool, str]] = []
    gate_G0(results)
    gate_L4(results)
    gate_L2(results)
    gate_L3(results)
    gate_H1(results)
    npass = sum(1 for _, ok, _ in results if ok)
    nfail = sum(1 for _, ok, _ in results if not ok)
    print(f"\nTOTAL: PASS={npass} FAIL={nfail}")


if __name__ == "__main__":
    main()
