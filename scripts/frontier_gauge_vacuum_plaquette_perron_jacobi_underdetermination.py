#!/usr/bin/env python3
"""
On the 36-state NMAX=5 box, the supplied finite class does not determine
Perron/Jacobi data.

This is a finite-box existence witness in the supplied-diagonal factorization
class. A stipulated fourth-power diagonal packet and two supplied positive
swap-symmetric residual packets give different Perron moments and Jacobi data
for the same recurrence matrix. The fourth-power packet is not identified here
as a physical local Wilson factor.

The NMAX=5 box is NOT invariant under the character recurrence (Part 2), so the
box statement does not by itself give the untruncated statement. Part 3 reports
a cutoff-sensitivity diagnostic and Part 4 evaluates a finite-box perturbative
response while naming the two separate gates left untruncated. Neither
establishes the untruncated result, which stays open together with the physical
Wilson compression.
"""

from __future__ import annotations

import numpy as np
from scipy.special import iv


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX = 5
TAU = 6.0
ARG = 2.0
MODE_MAX = 80


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def build_recurrence_matrix(nmax: int) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    jmat = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in recurrence_neighbors(p, q):
            if (a, b) in index:
                jmat[index[(a, b)], i] += 1.0 / 6.0
    return jmat, weights, index


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def wilson_character_coefficient(p: int, q: int) -> float:
    lam = highest_weight_triple(p, q)
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        mat = np.array(
            [[iv(mode + lam[j] + i - j, ARG) for j in range(3)] for i in range(3)],
            dtype=float,
        )
        total += float(np.linalg.det(mat))
    return total


def conjugation_swap_matrix(weights: list[tuple[int, int]], index: dict[tuple[int, int], int]) -> np.ndarray:
    s = np.zeros((len(weights), len(weights)), dtype=float)
    for w in weights:
        s[index[(w[1], w[0])], index[w]] = 1.0
    return s


def matrix_exponential_symmetric(m: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(m)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def dominant_eigenpair(m: np.ndarray) -> tuple[float, np.ndarray]:
    vals, vecs = np.linalg.eigh(m)
    idx = int(np.argmax(vals))
    vec = vecs[:, idx]
    if np.sum(vec) < 0.0:
        vec = -vec
    return float(vals[idx]), vec


def lanczos_jacobi(obs: np.ndarray, start: np.ndarray, kmax: int) -> tuple[list[float], list[float]]:
    q_prev = np.zeros_like(start)
    q = start / np.linalg.norm(start)
    alpha: list[float] = []
    beta: list[float] = []
    b_prev = 0.0
    for _ in range(kmax):
        z = obs @ q
        a = float(np.dot(q, z))
        z = z - a * q - b_prev * q_prev
        b = float(np.linalg.norm(z))
        alpha.append(a)
        if b < 1.0e-12:
            break
        beta.append(b)
        q_prev = q
        q = z / b
        b_prev = b
    return alpha, beta


def moments(obs: np.ndarray, state: np.ndarray, nmax: int) -> list[float]:
    return [float(state @ (np.linalg.matrix_power(obs, n) @ state)) for n in range(nmax + 1)]


def box_leakage(nmax: int) -> tuple[int, int, int]:
    """Count weights whose recurrence image leaves the truncation box.

    Returns (weights_with_leak, worst_case_leaked_moves, box_size). A nonzero
    first entry means the box is not invariant under the character recurrence,
    so the box operator is a non-invariant compression of the source operator.
    """
    weights = weights_box(nmax)
    inside = set(weights)
    leaking = 0
    worst = 0
    for p, q in weights:
        out = sum(1 for ab in recurrence_neighbors(p, q) if ab not in inside)
        if out:
            leaking += 1
        worst = max(worst, out)
    return leaking, worst, len(weights)


def build_box(nmax: int) -> dict[str, np.ndarray]:
    """Assemble every NMAX-box object the witnesses need, at one cutoff."""
    jmat, weights, index = build_recurrence_matrix(nmax)
    multiplier = matrix_exponential_symmetric(jmat, TAU / 2.0)
    c00 = wilson_character_coefficient(0, 0)
    local = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    return {
        "jmat": jmat,
        "swap": conjugation_swap_matrix(weights, index),
        "multiplier": multiplier,
        "d_packet": np.diag(local**4),
        "packet_coeffs": local,
        "r_a": np.diag([np.exp(-0.34 * (p + q) - 0.04 * ((p - q) ** 2)) for p, q in weights]),
        "r_b": np.diag([np.exp(-0.25 * (p + q) - 0.11 * ((p - q) ** 2)) for p, q in weights]),
        "size": len(weights),
    }


def moment_gaps(box: dict[str, np.ndarray]) -> tuple[float, float]:
    """First two Perron-moment gaps between the R_A and R_B witnesses on one box."""
    mult, d_packet = box["multiplier"], box["d_packet"]
    _, psi_a = dominant_eigenpair(mult @ d_packet @ box["r_a"] @ mult)
    _, psi_b = dominant_eigenpair(mult @ d_packet @ box["r_b"] @ mult)
    m_a = moments(box["jmat"], psi_a, 2)
    m_b = moments(box["jmat"], psi_b, 2)
    return abs(m_a[1] - m_b[1]), abs(m_a[2] - m_b[2])


def perron_moment_derivative(box: dict[str, np.ndarray]) -> tuple[float, float, float, float]:
    """Closed-form d/d(eps) of the first Perron moment along R(eps) = R_A + eps R_B.

    For a simple isolated top eigenvalue lam0 of T_0 = M D R_A M with reduced
    resolvent R_red on psi_0-perp, first-order perturbation theory gives
    psi'(0) = R_red V psi_0 with V = M D R_B M, hence m1'(0) = 2 <psi'(0), J psi_0>.
    Returns (lam0, absolute gap, relative gap, m1'(0)).
    """
    mult, d_packet, jmat = box["multiplier"], box["d_packet"], box["jmat"]
    t_0 = mult @ d_packet @ box["r_a"] @ mult
    v_dir = mult @ d_packet @ box["r_b"] @ mult
    vals, vecs = np.linalg.eigh(t_0)
    i0 = int(np.argmax(vals))
    lam0 = float(vals[i0])
    psi0 = vecs[:, i0]
    if psi0.sum() < 0.0:
        psi0 = -psi0
    gap = lam0 - float(np.max(np.delete(vals, i0)))
    reduced = np.zeros_like(t_0)
    for k in range(len(vals)):
        if k != i0:
            reduced += np.outer(vecs[:, k], vecs[:, k]) / (lam0 - vals[k])
    dpsi = reduced @ (v_dir @ psi0)
    return lam0, gap, gap / lam0, 2.0 * float(dpsi @ (jmat @ psi0))


def perron_moment_at(box: dict[str, np.ndarray], eps: float) -> float:
    """First Perron moment of the ray member R(eps) = R_A + eps R_B."""
    mult, d_packet = box["multiplier"], box["d_packet"]
    _, psi = dominant_eigenpair(mult @ d_packet @ (box["r_a"] + eps * box["r_b"]) @ mult)
    return float(psi @ (box["jmat"] @ psi))


def main() -> int:
    jmat, weights, index = build_recurrence_matrix(NMAX)
    swap = conjugation_swap_matrix(weights, index)

    multiplier = matrix_exponential_symmetric(jmat, TAU / 2.0)
    c00 = wilson_character_coefficient(0, 0)
    local = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    d_packet = np.diag(local**4)
    r_a = np.diag([np.exp(-0.34 * (p + q) - 0.04 * ((p - q) ** 2)) for p, q in weights])
    r_b = np.diag([np.exp(-0.25 * (p + q) - 0.11 * ((p - q) ** 2)) for p, q in weights])
    d_a = d_packet @ r_a
    d_b = d_packet @ r_b
    t_a = multiplier @ d_a @ multiplier
    t_b = multiplier @ d_b @ multiplier

    lam_a, psi_a = dominant_eigenpair(t_a)
    lam_b, psi_b = dominant_eigenpair(t_b)

    moments_a = moments(jmat, psi_a, 5)
    moments_b = moments(jmat, psi_b, 5)
    al_a, be_a = lanczos_jacobi(jmat, psi_a, 6)
    al_b, be_b = lanczos_jacobi(jmat, psi_b, 6)

    diff_m1 = abs(moments_a[1] - moments_b[1])
    diff_m2 = abs(moments_a[2] - moments_b[2])
    diff_alpha0 = abs(al_a[0] - al_b[0])
    diff_beta1 = abs(be_a[0] - be_b[0]) if be_a and be_b else 0.0

    sym_a = float(np.max(np.abs(swap @ r_a - r_a @ swap)))
    sym_b = float(np.max(np.abs(swap @ r_b - r_b @ swap)))
    packet_sym = float(np.max(np.abs(swap @ d_packet - d_packet @ swap)))
    inv_a = float(np.linalg.norm(swap @ psi_a - psi_a))
    inv_b = float(np.linalg.norm(swap @ psi_b - psi_b))
    inv_a_rendered = 0.0 if inv_a < 1.0e-12 else inv_a
    inv_b_rendered = 0.0 if inv_b < 1.0e-12 else inv_b
    min_entry_a = float(np.min(t_a))
    min_entry_b = float(np.min(t_b))
    floor_a = float(np.min(psi_a))
    floor_b = float(np.min(psi_b))

    print("GAUGE-VACUUM PLAQUETTE PERRON/JACOBI UNDERDETERMINATION")
    print(f"SCOPE: every theorem below is stated on the {len(weights)}-state NMAX={NMAX} dominant-weight")
    print("box only. The untruncated source sector and the physical Wilson compression")
    print("stay open; Parts 3 and 4 are diagnostics toward that lift, not the lift.")
    print()
    print("Part 1: two supplied residual packets on the NMAX=5 box")
    print(f"  box size            = {(NMAX + 1)} x {(NMAX + 1)} = {len(weights)} states")
    print(f"  tau                 = {TAU:.1f}")
    print(f"  packet symmetry err = {packet_sym:.3e}")
    print(f"  R_A / R_B sym err   = {sym_a:.3e} / {sym_b:.3e}")
    print(f"  T_A min / floor     = {min_entry_a:.6e} / {floor_a:.6e}")
    print(f"  T_B min / floor     = {min_entry_b:.6e} / {floor_b:.6e}")
    print(f"  m1^A, m1^B          = {moments_a[1]:.12f}, {moments_b[1]:.12f}")
    print(f"  m2^A, m2^B          = {moments_a[2]:.12f}, {moments_b[2]:.12f}")
    print(f"  |m1^A-m1^B|         = {diff_m1:.6e}")
    print(f"  |m2^A-m2^B|         = {diff_m2:.6e}")
    print(f"  alpha0^A, alpha0^B  = {al_a[0]:.12f}, {al_b[0]:.12f}")
    print(f"  beta1^A,  beta1^B   = {be_a[0]:.12f}, {be_b[0]:.12f}")
    print(f"  |alpha0^A-alpha0^B| = {diff_alpha0:.6e}")
    print(f"  |beta1^A-beta1^B|   = {diff_beta1:.6e}")

    check(
        "the stipulated finite fourth-power packet is positive and conjugation-symmetric",
        packet_sym < 1.0e-12 and float(np.min(local)) > 0.0,
        detail=f"min packet coefficient={float(np.min(local)):.3e}",
    )
    check(
        "the supplied class contains multiple positive conjugation-symmetric residual packets",
        sym_a < 1.0e-12 and sym_b < 1.0e-12 and min_entry_a > 0.0 and min_entry_b > 0.0,
        detail=f"min entries=({min_entry_a:.3e}, {min_entry_b:.3e})",
    )
    check(
        "each supplied-class generator has its own unique strictly positive Perron state",
        floor_a > 1.0e-8 and floor_b > 1.0e-8 and lam_a > 0.0 and lam_b > 0.0,
        detail=f"Perron floors=({floor_a:.3e}, {floor_b:.3e})",
    )
    check(
        "the two supplied residual packets induce different Perron moments for the same J_box",
        diff_m1 > 1.0e-4 and diff_m2 > 1.0e-4,
        detail=f"moment gaps=(m1:{diff_m1:.3e}, m2:{diff_m2:.3e})",
    )
    check(
        "the typed supplied-diagonal inputs therefore do not force unique Jacobi coefficients",
        diff_alpha0 > 1.0e-4 and diff_beta1 > 1.0e-4,
        detail=f"Jacobi gaps=(alpha0:{diff_alpha0:.3e}, beta1:{diff_beta1:.3e})",
    )

    check(
        "both Perron states remain fixed by the conjugation symmetry",
        inv_a < 1.0e-10 and inv_b < 1.0e-10,
        detail=f"invariance errors=({inv_a_rendered:.3e}, {inv_b_rendered:.3e})",
        bucket="SUPPORT",
    )
    check(
        "the same explicit recurrence matrix J_box is used in both witnesses",
        float(np.max(np.abs(jmat - jmat.T))) < 1.0e-15 and float(np.max(np.abs(swap @ jmat - jmat @ swap))) < 1.0e-12,
        detail="same self-adjoint conjugation-symmetric J_box in both cases",
        bucket="SUPPORT",
    )
    check(
        "the finite-box witness separation is not at floating-point noise scale",
        diff_m1 > 1.0e-4 and diff_alpha0 > 1.0e-4,
        detail=f"representative gaps=(m1:{diff_m1:.3e}, alpha0:{diff_alpha0:.3e})",
        bucket="SUPPORT",
    )

    print()
    print("Part 2: the NMAX=5 box is NOT recurrence-invariant (why no automatic lift)")
    leaking, worst, box_size = box_leakage(NMAX)
    print(f"  weights whose J-image leaves the box = {leaking}/{box_size}")
    print(f"  worst-case leaked recurrence moves   = {worst}/6 = {worst / 6.0:.6f}")
    check(
        "the box operator is a non-invariant compression, so box results do not transfer to the untruncated sector by restriction",
        leaking > 0 and worst > 0,
        detail=f"{leaking} of {box_size} weights leak; the compression is not a restriction of an invariant subspace",
    )

    print()
    print("Part 3: cutoff-sensitivity DIAGNOSTIC (bounds nothing untruncated)")
    witness_box = {
        "jmat": jmat,
        "multiplier": multiplier,
        "d_packet": d_packet,
        "r_a": r_a,
        "r_b": r_b,
        "size": len(weights),
    }
    sampled = sorted(
        [(NMAX, witness_box)] + [(n, build_box(n)) for n in (3, 4, 6, 7)],
        key=lambda row: row[0],
    )
    sampled_gaps = []
    for nmax, box in sampled:
        g1, g2 = moment_gaps(box)
        sampled_gaps.append(g1)
        print(f"  NMAX={nmax} states={box['size']:3d} |m1 gap|={g1:.6e} |m2 gap|={g2:.6e}")
    check(
        "the moment gap stays bounded away from zero across every sampled cutoff (the witnesses are not a single-box artifact)",
        min(sampled_gaps) > 1.0e-4,
        detail=f"min sampled gap={min(sampled_gaps):.6e}; this bounds only the sampled boxes, never the untruncated sector",
        bucket="SUPPORT",
    )

    print()
    print("Part 4: finite-box perturbative response; two gates remain untruncated")
    lam0, gap_abs, gap_rel, dm1 = perron_moment_derivative(witness_box)
    print(f"  lam0 / spectral gap = {lam0:.9e} / {gap_abs:.6e} (relative {gap_rel:.6e})")
    print(f"  closed-form dm1/deps at eps=0        = {dm1:.12f}")
    ray_floor = float(np.min(np.diag(r_a) - 1.0e-2 * np.diag(r_b)))
    check(
        "on the NMAX=5 box the top eigenvalue is simple and isolated and the ray R(eps)=R_A+eps R_B stays strictly positive over the sampled window",
        gap_rel > 1.0e-3 and ray_floor > 0.0,
        detail=f"relative gap={gap_rel:.6e}, min ray diagonal at eps=-0.01 is {ray_floor:.6e}",
        bucket="SUPPORT",
    )
    print("  central-difference check of the closed form (error must fall ~4x per halving):")
    fd_errs = []
    for eps in (1.0e-2, 5.0e-3, 2.5e-3):
        fd = (perron_moment_at(witness_box, eps) - perron_moment_at(witness_box, -eps)) / (2.0 * eps)
        fd_errs.append(abs(fd - dm1))
        ratio = fd_errs[-2] / fd_errs[-1] if len(fd_errs) > 1 else float("nan")
        print(f"    eps={eps:.5f} fd={fd:.12f} err={fd_errs[-1]:.3e} ratio={ratio:.3f}")
    ratios = [fd_errs[i - 1] / fd_errs[i] for i in range(1, len(fd_errs))]
    check(
        "the first Perron moment varies at first order along the admissible ray, with the closed-form derivative confirmed to second order",
        abs(dm1) > 1.0e-6 and all(3.6 < r < 4.4 for r in ratios),
        detail=f"dm1/deps={dm1:.9e}, convergence ratios={[round(r, 3) for r in ratios]} (a wrong derivative plateaus instead)",
    )
    print("  => the untruncated route still needs BOTH (1) bounded self-adjoint")
    print("     operators with a simple isolated top eigenvalue and (2) a proof that")
    print("     the full-sector moment response is nonzero. The finite-box derivative")
    print("     proves neither gate after cutoff removal, so the untruncated statement")
    print("     remains open.")

    print()
    print("Part 5: five-resolution decomposition of the A/B difference (NMAX=5)")
    delta_psi = psi_a - psi_b
    _, jvecs = np.linalg.eigh(jmat)
    mode_coeffs = jvecs.T @ delta_psi
    sym_part = 0.5 * (delta_psi + swap @ delta_psi)
    asym_part = 0.5 * (delta_psi - swap @ delta_psi)
    res_per_element = float(np.max(np.abs(t_a - t_b)))
    res_per_site = int(np.sum(np.abs(delta_psi) > 1.0e-6))
    res_per_mode = int(np.sum(np.abs(mode_coeffs) > 1.0e-6))
    res_sym = float(np.linalg.norm(sym_part))
    res_asym = float(np.linalg.norm(asym_part))
    print(f"  per_element  max|T_A-T_B|            = {res_per_element:.6e}")
    print(f"  per_site     weights with |dpsi|>1e-6= {res_per_site}/{len(weights)}")
    print(f"  per_mode     J-modes with |coef|>1e-6= {res_per_mode}/{len(weights)}")
    res_asym_rendered = 0.0 if res_asym < 1.0e-12 else res_asym
    print(f"  per_block    ||sym|| / ||antisym||   = {res_sym:.6e} / {res_asym_rendered:.3e}")
    print(f"  lattice_wide |m1 gap| / |m2 gap|     = {diff_m1:.6e} / {diff_m2:.6e}")
    check(
        "the finite-box A/B difference is visible in every reported diagnostic and lies in the conjugation-symmetric block",
        res_per_element > 1.0e-6 and res_per_site > 1 and res_per_mode > 1 and res_asym < 1.0e-12 < res_sym,
        detail=f"antisymmetric part {res_asym_rendered:.3e} is machine zero against symmetric part {res_sym:.6e}",
        bucket="SUPPORT",
    )

    print()
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
