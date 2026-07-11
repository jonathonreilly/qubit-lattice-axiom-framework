#!/usr/bin/env python3
"""Actual L_s=3 spatial Wilson-environment character coefficients.

This runner attacks the physical residual named by
GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.
It does not insert a rho sequence.  Instead it uses the exact marked-factor
deletion identity

  rho_lam^env = <conj(chi_lam(U_m))/w_beta(U_m)>_full
                / (d_lam <1/w_beta(U_m)>_full),

where the expectation is in the full periodic three-dimensional Wilson
ensemble and w_beta(U)=exp[(beta/3) Re Tr U].  Translation/orientation
symmetry permits averaging the estimator over every plaquette of each sampled
configuration without changing its expectation.

The numerical certificate is finite-volume and statistical.  It is not an
all-weight exact-arithmetic evaluation and it never uses the canonical
plaquette comparator as input or as a pass condition.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass

import numpy as np
from scipy.special import iv


BETA = 6.0
L = 3
AUDIT_TIMEOUT_SEC = 180
DEFAULT_SEEDS = (61003, 61019, 61031, 61043)
IRREPS = ((0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2))


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_character_from_trace(trace_u: complex, p: int, q: int) -> complex:
    """SU(3) Schur character s_(p+q,q,0) from Tr(U).

    For det(U)=1 the elementary symmetric polynomials are
    e1=Tr(U), e2=conj(Tr(U)), e3=1.  Newton's recurrence constructs the
    complete homogeneous functions, and the two-row Jacobi--Trudi determinant
    gives chi_(p,q)=h_(p+q) h_q-h_(p+q+1) h_(q-1).
    """
    nmax = p + q + 1
    h = np.zeros(nmax + 1, dtype=complex)
    h[0] = 1.0
    for n in range(1, nmax + 1):
        h[n] = trace_u * h[n - 1]
        if n >= 2:
            h[n] -= np.conjugate(trace_u) * h[n - 2]
        if n >= 3:
            h[n] += h[n - 3]
    h_q_minus_1 = 0.0 if q == 0 else h[q - 1]
    return h[p + q] * h[q] - h[p + q + 1] * h_q_minus_1


def random_haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    q = q @ np.diag(np.conjugate(phases))
    det_q = np.linalg.det(q)
    q[:, 0] *= np.conjugate(det_q)
    return q


def random_su2_subgroup_step(rng: np.random.Generator, epsilon: float) -> np.ndarray:
    """Symmetric near-identity SU(3) proposal in a random SU(2) subgroup."""
    pair = ((0, 1), (0, 2), (1, 2))[int(rng.integers(0, 3))]
    v = rng.normal(scale=epsilon, size=3)
    theta = float(np.linalg.norm(v))
    if theta == 0.0:
        return np.eye(3, dtype=complex)
    n1, n2, n3 = v / theta
    c = math.cos(theta)
    s = math.sin(theta)
    block = np.array(
        [
            [c + 1j * n3 * s, (1j * n1 + n2) * s],
            [(1j * n1 - n2) * s, c - 1j * n3 * s],
        ],
        dtype=complex,
    )
    out = np.eye(3, dtype=complex)
    a, b = pair
    out[np.ix_((a, b), (a, b))] = block
    return out


def site_index(x: int, y: int, z: int) -> int:
    return (x % L) + L * (y % L) + L * L * (z % L)


def link_index(x: int, y: int, z: int, direction: int) -> int:
    return 3 * site_index(x, y, z) + direction


def build_plaquettes() -> tuple[list[tuple[tuple[int, int], ...]], list[list[int]]]:
    faces: list[tuple[tuple[int, int], ...]] = []
    for z in range(L):
        for y in range(L):
            for x in range(L):
                coord = [x, y, z]
                for mu in range(3):
                    for nu in range(mu + 1, 3):
                        plus_mu = coord.copy()
                        plus_mu[mu] += 1
                        plus_nu = coord.copy()
                        plus_nu[nu] += 1
                        faces.append(
                            (
                                (link_index(*coord, mu), +1),
                                (link_index(*plus_mu, nu), +1),
                                (link_index(*plus_nu, mu), -1),
                                (link_index(*coord, nu), -1),
                            )
                        )
    link_to_faces: list[list[int]] = [[] for _ in range(3 * L**3)]
    for face_id, face in enumerate(faces):
        for link_id, _ in face:
            link_to_faces[link_id].append(face_id)
    return faces, link_to_faces


FACES, LINK_TO_FACES = build_plaquettes()


def face_matrix(links: np.ndarray, face: tuple[tuple[int, int], ...]) -> np.ndarray:
    out = np.eye(3, dtype=complex)
    for link_id, orientation in face:
        u = links[link_id]
        out = out @ (u if orientation == 1 else u.conj().T)
    return out


def face_real_trace(links: np.ndarray, face_id: int) -> float:
    return float(np.trace(face_matrix(links, FACES[face_id])).real)


def all_face_traces(links: np.ndarray) -> np.ndarray:
    return np.array([np.trace(face_matrix(links, face)) for face in FACES])


def full_log_weight(links: np.ndarray, beta: float) -> float:
    return float((beta / 3.0) * np.sum(all_face_traces(links).real))


def metropolis_sweep(
    links: np.ndarray,
    rng: np.random.Generator,
    epsilon: float,
    beta: float,
    excluded_face: int | None = None,
) -> float:
    accepted = 0
    for link_id in rng.permutation(len(links)):
        old_link = links[link_id].copy()
        active_faces = [f for f in LINK_TO_FACES[link_id] if f != excluded_face]
        old_sum = sum(face_real_trace(links, f) for f in active_faces)
        proposal = random_su2_subgroup_step(rng, epsilon) @ old_link
        links[link_id] = proposal
        new_sum = sum(face_real_trace(links, f) for f in active_faces)
        delta_log_weight = (beta / 3.0) * (new_sum - old_sum)
        if delta_log_weight >= 0.0 or rng.random() < math.exp(delta_log_weight):
            accepted += 1
        else:
            links[link_id] = old_link
    return accepted / len(links)


def environment_observable(links: np.ndarray, beta: float) -> np.ndarray:
    """Per-configuration all-plaquette averages for numerator channels."""
    traces = all_face_traces(links)
    inverse_local_weight = np.exp(-(beta / 3.0) * traces.real)
    channels = np.empty(len(IRREPS), dtype=complex)
    for i, (p, q) in enumerate(IRREPS):
        chars = np.array([su3_character_from_trace(t, p, q) for t in traces])
        channels[i] = np.mean(inverse_local_weight * np.conjugate(chars)) / dim_su3(p, q)
    return channels


@dataclass
class ChainResult:
    seed: int
    initial: str
    measure_kind: str
    excluded_face: int | None
    epsilon: float
    acceptance: float
    samples: np.ndarray
    plaquette_samples: np.ndarray


def average_plaquette_from_traces(traces: np.ndarray) -> float:
    return float(np.mean(traces.real) / 3.0)


def run_chain(
    seed: int,
    initial: str,
    therm_sweeps: int,
    measure_sweeps: int,
    sample_every: int,
    beta: float,
    verbose: bool,
    measure_kind: str = "full_reweight",
    excluded_face: int | None = None,
) -> ChainResult:
    rng = np.random.default_rng(seed)
    if initial == "cold":
        links = np.tile(np.eye(3, dtype=complex), (3 * L**3, 1, 1))
    else:
        links = np.array([random_haar_su3(rng) for _ in range(3 * L**3)])

    epsilon = 0.32
    for sweep in range(therm_sweeps):
        acc = metropolis_sweep(links, rng, epsilon, beta, excluded_face=excluded_face)
        if (sweep + 1) % 25 == 0:
            if acc > 0.62:
                epsilon *= 1.05
            elif acc < 0.42:
                epsilon *= 0.95
            epsilon = float(np.clip(epsilon, 0.06, 1.2))

    values: list[np.ndarray] = []
    plaquettes: list[float] = []
    acceptances: list[float] = []
    for sweep in range(measure_sweeps):
        acceptances.append(metropolis_sweep(links, rng, epsilon, beta, excluded_face=excluded_face))
        if (sweep + 1) % sample_every == 0:
            traces = all_face_traces(links)
            plaquettes.append(average_plaquette_from_traces(traces))
            sample = np.empty(len(IRREPS), dtype=complex)
            if measure_kind == "full_reweight":
                inverse_local_weight = np.exp(-(beta / 3.0) * traces.real)
                for i, (p, q) in enumerate(IRREPS):
                    chars = np.array([su3_character_from_trace(t, p, q) for t in traces])
                    sample[i] = np.mean(inverse_local_weight * np.conjugate(chars)) / dim_su3(p, q)
            elif measure_kind == "environment_direct":
                if excluded_face is None:
                    raise ValueError("environment_direct requires excluded_face")
                marked_trace = traces[excluded_face]
                for i, (p, q) in enumerate(IRREPS):
                    sample[i] = np.conjugate(su3_character_from_trace(marked_trace, p, q)) / dim_su3(p, q)
            else:
                raise ValueError(f"unknown measure_kind={measure_kind}")
            values.append(sample)

    result = ChainResult(
        seed=seed,
        initial=initial,
        measure_kind=measure_kind,
        excluded_face=excluded_face,
        epsilon=epsilon,
        acceptance=float(np.mean(acceptances)),
        samples=np.array(values),
        plaquette_samples=np.array(plaquettes),
    )
    if verbose:
        rho = np.mean(result.samples, axis=0) / np.mean(result.samples[:, 0])
        print(
            f"  seed={seed} init={initial:4s} kind={measure_kind:18s} "
            f"excluded={str(excluded_face):>4s} eps={epsilon:.4f} "
            f"acc={result.acceptance:.3f} n={len(values)} "
            f"P={np.mean(result.plaquette_samples):.6f} "
            f"rho10={rho[1].real:.6f} rho11={rho[3].real:.6f}"
        )
    return result


def blocked_means(chains: list[ChainResult], blocks_per_chain: int) -> np.ndarray:
    blocks: list[np.ndarray] = []
    for chain in chains:
        n = len(chain.samples)
        block_size = n // blocks_per_chain
        if block_size < 2:
            raise ValueError("too few samples for requested blocking")
        for b in range(blocks_per_chain):
            lo = b * block_size
            hi = n if b == blocks_per_chain - 1 else (b + 1) * block_size
            blocks.append(np.mean(chain.samples[lo:hi], axis=0))
    return np.array(blocks)


def ratio_from_mean(mean_channels: np.ndarray) -> np.ndarray:
    return mean_channels / mean_channels[0]


def jackknife_ratios(blocks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = len(blocks)
    total = np.sum(blocks, axis=0)
    leave_one = np.array([ratio_from_mean((total - blocks[i]) / (n - 1)) for i in range(n)])
    center = ratio_from_mean(np.mean(blocks, axis=0))
    errors = np.sqrt((n - 1) / n * np.sum(np.abs(leave_one - np.mean(leave_one, axis=0)) ** 2, axis=0))
    return center, errors.real


def integrated_autocorrelation_time(values: np.ndarray, max_lag: int = 100) -> float:
    x = np.asarray(values, dtype=float)
    x = x - np.mean(x)
    var = float(np.dot(x, x) / len(x))
    if var <= 0.0:
        return 0.5
    tau = 0.5
    upper = min(max_lag, len(x) // 4)
    for lag in range(1, upper + 1):
        corr = float(np.dot(x[:-lag], x[lag:]) / (len(x) - lag) / var)
        if corr <= 0.0:
            break
        tau += corr
    return tau


def wilson_character_coefficient(p: int, q: int, beta: float, mode_max: int = 80) -> float:
    lam = [p + q, q, 0]
    arg = beta / 3.0
    total = 0.0
    for mode in range(-mode_max, mode_max + 1):
        matrix = np.array(
            [[iv(mode + lam[j] + i - j, arg) for j in range(3)] for i in range(3)],
            dtype=float,
        )
        total += float(np.linalg.det(matrix))
    return total


def single_link_rho(beta: float) -> np.ndarray:
    c00 = wilson_character_coefficient(0, 0, beta)
    return np.array(
        [wilson_character_coefficient(p, q, beta) / (dim_su3(p, q) * c00) for p, q in IRREPS]
    )


def weyl_haar_character_moments(grid: int = 32) -> np.ndarray:
    """Deterministic Cartan-torus Weyl quadrature, normalized by its mass."""
    accum = np.zeros(len(IRREPS), dtype=complex)
    mass = 0.0
    for ia in range(grid):
        a = 2.0 * math.pi * ia / grid
        for ib in range(grid):
            b = 2.0 * math.pi * ib / grid
            eig = np.array([np.exp(1j * a), np.exp(1j * b), np.exp(-1j * (a + b))])
            vandermonde_sq = float(
                abs(eig[0] - eig[1]) ** 2
                * abs(eig[0] - eig[2]) ** 2
                * abs(eig[1] - eig[2]) ** 2
            )
            trace_u = np.sum(eig)
            mass += vandermonde_sq
            for i, (p, q) in enumerate(IRREPS):
                accum[i] += vandermonde_sq * su3_character_from_trace(trace_u, p, q)
    return accum / mass


def exact_sanity_checks() -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    identity_trace = 3.0 + 0.0j
    max_dim_error = max(
        abs(su3_character_from_trace(identity_trace, p, q) - dim_su3(p, q)) for p, q in IRREPS
    )
    checks.append(("Jacobi--Trudi character values equal irrep dimensions at identity", max_dim_error < 1e-12, f"max error={max_dim_error:.3e}"))
    checks.append(("periodic L_s=3 census has 81 links and 81 plaquettes", 3 * L**3 == 81 and len(FACES) == 81, f"links={3*L**3}, faces={len(FACES)}"))
    incidence_counts = [len(v) for v in LINK_TO_FACES]
    checks.append(("every spatial link has four incident plaquettes", min(incidence_counts) == 4 and max(incidence_counts) == 4, f"range={min(incidence_counts)}..{max(incidence_counts)}"))

    rng = np.random.default_rng(9173)
    links = np.array([random_haar_su3(rng) for _ in range(3 * L**3)])
    link_id = 17
    old_total = full_log_weight(links, BETA)
    old_link = links[link_id].copy()
    old_local = sum(face_real_trace(links, f) for f in LINK_TO_FACES[link_id])
    step = random_su2_subgroup_step(rng, 0.27)
    links[link_id] = step @ old_link
    new_total = full_log_weight(links, BETA)
    new_local = sum(face_real_trace(links, f) for f in LINK_TO_FACES[link_id])
    local_delta = (BETA / 3.0) * (new_local - old_local)
    checks.append(("local Metropolis action delta equals full Wilson-weight delta", abs((new_total - old_total) - local_delta) < 1e-11, f"residual={abs((new_total-old_total)-local_delta):.3e}"))
    unitary_error = float(np.max(np.abs(step.conj().T @ step - np.eye(3))))
    determinant_error = abs(np.linalg.det(step) - 1.0)
    checks.append(("SU(2)-subgroup proposal remains in SU(3)", unitary_error < 1e-12 and determinant_error < 1e-12, f"unitary={unitary_error:.3e}, determinant={determinant_error:.3e}"))
    haar_moments = weyl_haar_character_moments()
    haar_residual = float(np.max(np.abs(haar_moments[1:])))
    checks.append(("beta=0/marked-only Haar control kills every nontrivial tracked character", haar_residual < 1e-12, f"max moment={haar_residual:.3e}"))
    return checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--therm", type=int, default=900)
    parser.add_argument("--measure", type=int, default=2400)
    parser.add_argument("--sample-every", type=int, default=4)
    parser.add_argument("--blocks-per-chain", type=int, default=12)
    parser.add_argument("--chains", type=int, default=4, choices=(2, 4))
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=" * 79)
    print("ACTUAL L_s=3 SPATIAL WILSON ENVIRONMENT CHARACTER MEASURE")
    print("=" * 79)
    print(
        f"beta={BETA}, L={L}, links={3*L**3}, plaquettes={len(FACES)}, "
        f"chains={args.chains}, therm={args.therm}, measure={args.measure}, "
        f"sample_every={args.sample_every}"
    )
    print("No canonical plaquette comparator or fitted rho enters this runner.")

    passed = 0
    failed = 0
    print("\nExact implementation checks")
    for name, ok, detail in exact_sanity_checks():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed += int(ok)
        failed += int(not ok)

    print("\nIndependent full-Wilson chains (marked-factor deletion estimator)")
    start = time.time()
    chains: list[ChainResult] = []
    for i, seed in enumerate(DEFAULT_SEEDS[: args.chains]):
        chains.append(
            run_chain(
                seed=seed,
                initial="cold" if i % 2 == 0 else "hot",
                therm_sweeps=args.therm,
                measure_sweeps=args.measure,
                sample_every=args.sample_every,
                beta=BETA,
                verbose=not args.quiet,
                measure_kind="full_reweight",
            )
        )
    print(f"  elapsed={time.time()-start:.1f}s")

    blocks = blocked_means(chains, args.blocks_per_chain)
    rho, rho_err = jackknife_ratios(blocks)
    single = single_link_rho(BETA)
    print("\nMarked-factor deletion estimator")
    print("  irrep      d       rho_env +/- block-JK error       single-link rho")
    for i, (p, q) in enumerate(IRREPS):
        print(
            f"  ({p},{q}) {dim_su3(p,q):6d}   "
            f"{rho[i].real:+.9f} {rho[i].imag:+.2e}i +/- {rho_err[i]:.3e}   "
            f"{single[i]:+.9f}"
        )

    print("\nIndependent 80-plaquette environment chains (direct estimator)")
    direct_chains: list[ChainResult] = []
    excluded_faces = (0, 1, 27, 54)
    for i, seed in enumerate(DEFAULT_SEEDS[: args.chains]):
        direct_chains.append(
            run_chain(
                seed=seed + 1000,
                initial="hot" if i % 2 == 0 else "cold",
                therm_sweeps=args.therm,
                measure_sweeps=args.measure,
                sample_every=args.sample_every,
                beta=BETA,
                verbose=not args.quiet,
                measure_kind="environment_direct",
                excluded_face=excluded_faces[i],
            )
        )
    direct_blocks = blocked_means(direct_chains, args.blocks_per_chain)
    direct_rho, direct_err = jackknife_ratios(direct_blocks)
    print("  irrep          direct rho_env +/- block-JK error       deletion difference")
    for i, (p, q) in enumerate(IRREPS):
        print(
            f"  ({p},{q})   {direct_rho[i].real:+.9f} {direct_rho[i].imag:+.2e}i "
            f"+/- {direct_err[i]:.3e}   delta={direct_rho[i].real-rho[i].real:+.3e}"
        )

    chain_rhos = np.array([ratio_from_mean(np.mean(c.samples, axis=0)) for c in chains])
    pooled_se = np.maximum(rho_err, 1e-14)
    chain_spread_z = np.max(np.abs(chain_rhos.real - rho.real) / pooled_se, axis=0)
    tau10 = max(
        integrated_autocorrelation_time((c.samples[:, 1] - rho[1] * c.samples[:, 0]).real)
        for c in chains
    )
    tau11 = max(
        integrated_autocorrelation_time((c.samples[:, 3] - rho[3] * c.samples[:, 0]).real)
        for c in chains
    )
    direct_chain_rhos = np.array(
        [ratio_from_mean(np.mean(c.samples, axis=0)) for c in direct_chains]
    )
    direct_chain_spread_z = np.max(
        np.abs(direct_chain_rhos.real - direct_rho.real) / np.maximum(direct_err, 1e-14),
        axis=0,
    )
    direct_tau10 = max(
        integrated_autocorrelation_time(c.samples[:, 1].real) for c in direct_chains
    )
    direct_tau11 = max(
        integrated_autocorrelation_time(c.samples[:, 3].real) for c in direct_chains
    )
    block_size = min(len(c.samples) for c in chains) // args.blocks_per_chain
    direct_block_size = min(len(c.samples) for c in direct_chains) // args.blocks_per_chain
    certifying_protocol = (
        args.chains == 4
        and args.therm >= 900
        and args.measure >= 2400
        and args.sample_every <= 4
        and args.blocks_per_chain >= 12
    )
    conjugation_residual = max(abs(rho[1] - rho[2]), abs(rho[4] - rho[5]))
    imaginary_residual = float(np.max(np.abs(rho.imag)))
    normalization_residual = abs(rho[0] - 1.0)
    separation_10 = abs(rho[1].real - single[1]) / max(rho_err[1], 1e-14)
    separation_11 = abs(rho[3].real - single[3]) / max(rho_err[3], 1e-14)
    estimator_agreement_z = np.abs(direct_rho.real - rho.real) / np.sqrt(
        np.maximum(direct_err**2 + rho_err**2, 1e-28)
    )
    direct_conjugation_residual = max(
        abs(direct_rho[1] - direct_rho[2]), abs(direct_rho[4] - direct_rho[5])
    )
    direct_imaginary_residual = float(np.max(np.abs(direct_rho.imag)))

    statistical_checks = [
        ("audit certificate uses the fixed minimum production protocol", certifying_protocol, f"chains={args.chains}, therm={args.therm}, measure={args.measure}, sample_every={args.sample_every}, blocks={args.blocks_per_chain}"),
        ("rho_(0,0)^env is normalized by construction", normalization_residual < 1e-12, f"residual={normalization_residual:.3e}"),
        ("environment coefficients are real within four jackknife errors", imaginary_residual < 4.0 * max(rho_err[1:]), f"imag max={imaginary_residual:.3e}"),
        ("conjugate irreps agree within four jackknife errors", conjugation_residual < 4.0 * max(rho_err[1], rho_err[2], rho_err[4], rho_err[5]), f"residual={conjugation_residual:.3e}"),
        ("independent hot/cold chain means are mutually consistent", float(np.max(chain_spread_z[1:])) < 5.0, f"max chain deviation={float(np.max(chain_spread_z[1:])):.2f} pooled SE"),
        ("proposal acceptance remains nondegenerate", all(0.25 < c.acceptance < 0.80 for c in chains), "range=" + f"{min(c.acceptance for c in chains):.3f}..{max(c.acceptance for c in chains):.3f}"),
        ("full-chain block length exceeds ten estimated autocorrelation times", block_size > 10.0 * max(tau10, tau11), f"block={block_size}, tau10={tau10:.2f}, tau11={tau11:.2f}"),
        ("direct-environment marked-face chain means are mutually consistent", float(np.max(direct_chain_spread_z[1:])) < 5.0, f"max chain deviation={float(np.max(direct_chain_spread_z[1:])):.2f} pooled SE"),
        ("direct-environment proposal acceptance remains nondegenerate", all(0.25 < c.acceptance < 0.80 for c in direct_chains), f"range={min(c.acceptance for c in direct_chains):.3f}..{max(c.acceptance for c in direct_chains):.3f}"),
        ("direct-environment spectrum is real within four jackknife errors", direct_imaginary_residual < 4.0 * max(direct_err[1:]), f"imag max={direct_imaginary_residual:.3e}"),
        ("direct-environment conjugate irreps agree within four jackknife errors", direct_conjugation_residual < 4.0 * max(direct_err[1], direct_err[2], direct_err[4], direct_err[5]), f"residual={direct_conjugation_residual:.3e}"),
        ("direct-environment block length exceeds ten estimated autocorrelation times", direct_block_size > 10.0 * max(direct_tau10, direct_tau11), f"block={direct_block_size}, tau10={direct_tau10:.2f}, tau11={direct_tau11:.2f}"),
        ("actual rho_(1,0)^env is statistically distinct from the single-link packet", separation_10 > 5.0, f"separation={separation_10:.1f} sigma"),
        ("actual rho_(1,1)^env is statistically distinct from the single-link packet", separation_11 > 5.0, f"separation={separation_11:.1f} sigma"),
        ("direct 80-plaquette and marked-factor-deletion spectra agree", float(np.max(estimator_agreement_z[1:])) < 4.0, f"max difference={float(np.max(estimator_agreement_z[1:])):.2f} combined SE"),
    ]
    print("\nStatistical and discriminating checks")
    for name, ok, detail in statistical_checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed += int(ok)
        failed += int(not ok)

    print("\nCertificate boundary")
    print("  The exact deletion identity derives the estimator from the actual")
    print("  80-active-plaquette environment integral.  The reported beta=6")
    print("  coefficients are finite-volume computed lattice inputs with block-")
    print("  jackknife uncertainty, not exact all-weight arithmetic data.")
    print(f"\nSUMMARY: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
