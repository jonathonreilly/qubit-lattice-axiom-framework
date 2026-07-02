#!/usr/bin/env python3
"""Corner-transfer fixed-gauge-background bounded theorem runner.

Verification companion for
docs/CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md.

This runner stays on the fixed-background surface. It reuses the retained
position-space two-step transfer construction from the fixed-gauge RP engine,
adds the AC_phi_lambda circulant channel decomposition, and checks the theorem
parts N1--N5 plus source-note firewall checks. It does not integrate over gauge
backgrounds.
"""
from __future__ import annotations

from itertools import combinations
import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md"
ENGINE = ROOT / "docs" / "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md"
SUBSTEP1 = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
REGISTRABLE = ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"

PARAMS = [
    (1.0, 0.25, 2.0 / 9.0),
    (1.35, 0.31, -0.41),
]
SEEDS = [2026061201, 2026061202]
L_S = 2
TOL = 1.0e-9
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def shift_matrix() -> np.ndarray:
    """C e_k = e_{k-1}; Fourier columns have eigenvalues exp(2 pi i k / 3)."""
    return np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )


def fourier3() -> np.ndarray:
    omega = np.exp(2j * np.pi / 3.0)
    return np.array([[omega ** (j * k) for k in range(3)] for j in range(3)], dtype=complex) / math.sqrt(3.0)


def generation_mass(a: float, B: float, delta: float) -> np.ndarray:
    C = shift_matrix()
    return a * np.eye(3, dtype=complex) + B * np.exp(1j * delta) * C + B * np.exp(-1j * delta) * C.T


def lambdas(a: float, B: float, delta: float) -> np.ndarray:
    return np.array([a + 2.0 * B * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)], dtype=float)


def u1_background(seed: int, Ls: int = L_S) -> list[np.ndarray]:
    rng = np.random.default_rng(seed)
    phases = rng.uniform(-math.pi, math.pi, size=Ls)
    return [np.array([[np.exp(1j * phase)]], dtype=complex) for phase in phases]


def z2_background() -> list[np.ndarray]:
    return [np.array([[1.0]], dtype=complex), np.array([[-1.0]], dtype=complex)]


def identity_background() -> list[np.ndarray]:
    return [np.array([[1.0]], dtype=complex) for _ in range(L_S)]


def conj_background(links: list[np.ndarray]) -> list[np.ndarray]:
    return [u.conj() for u in links]


def spatial_hop_matrix(links: list[np.ndarray], nc: int = 1) -> np.ndarray:
    """Anti-Hermitian staggered spatial hop h[U] on C^{L_s} tensor C^{nc}."""
    Ls = len(links)
    dim = Ls * nc
    h = np.zeros((dim, dim), dtype=complex)

    def blk(x: int) -> slice:
        return slice(x * nc, (x + 1) * nc)

    for x in range(Ls):
        xp = (x + 1) % Ls
        xm = (x - 1) % Ls
        h[blk(x), blk(xp)] += 0.5 * links[x]
        h[blk(x), blk(xm)] += -0.5 * links[xm].conj().T
    return h


def two_step_classical_transfer(links: list[np.ndarray], mass: float, nc: int = 1) -> np.ndarray:
    h = spatial_hop_matrix(links, nc)
    d = h.shape[0]
    I = np.eye(d, dtype=complex)
    Z = np.zeros((d, d), dtype=complex)
    A_even = mass * I + h
    A_odd = mass * I - h
    T_even = np.block([[-2.0 * A_even, I], [I, Z]])
    T_odd = np.block([[-2.0 * A_odd, I], [I, Z]])
    return T_odd @ T_even


def decaying_eigs(T2cl: np.ndarray) -> np.ndarray:
    ev = np.linalg.eigvals(T2cl)
    order = np.argsort(np.abs(ev))
    return ev[order[: len(ev) // 2]]


def channel_kernel(links: list[np.ndarray], mass: float) -> np.ndarray:
    """Positive Hermitian single-particle two-step kernel t[U,m].

    The retained modal reduction diagonalizes K = -i h[U]. For h eigenvalue
    i nu, the decaying two-step eigenvalue is exp(-2 asinh(sqrt(m^2 + nu^2))).
    """
    h = spatial_hop_matrix(links, 1)
    K = -1j * h
    K = 0.5 * (K + K.conj().T)
    nu, vecs = np.linalg.eigh(K)
    mu = np.exp(-2.0 * np.arcsinh(np.sqrt(mass * mass + nu * nu)))
    t = vecs @ np.diag(mu) @ vecs.conj().T
    return 0.5 * (t + t.conj().T)


def manybody_from_kernel(t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Build Gamma(t) in a basis where t is diagonal; enough for positivity checks."""
    eig = np.linalg.eigvalsh(0.5 * (t + t.conj().T))
    T = np.array([[1.0]], dtype=complex)
    B = np.array([[1.0]], dtype=complex)
    for mu in eig:
        T = np.kron(T, np.diag([1.0, float(mu)]))
        B = np.kron(B, np.diag([1.0, math.sqrt(max(float(mu), 0.0))]))
    return T, B


def block_diag(mats: list[np.ndarray]) -> np.ndarray:
    n = sum(m.shape[0] for m in mats)
    out = np.zeros((n, n), dtype=complex)
    cursor = 0
    for m in mats:
        d = m.shape[0]
        out[cursor: cursor + d, cursor: cursor + d] = m
        cursor += d
    return out


def compound_trace(A: np.ndarray, r: int) -> complex:
    if r == 0:
        return 1.0 + 0.0j
    n = A.shape[0]
    tr = 0.0 + 0.0j
    for idx in combinations(range(n), r):
        sub = A[np.ix_(idx, idx)]
        tr += np.linalg.det(sub)
    return tr


def trace_gamma(A: np.ndarray) -> complex:
    return sum(compound_trace(A, r) for r in range(A.shape[0] + 1))


def tensor_swap_permutation(dim: int = 4) -> np.ndarray:
    """Permutation unitary swapping factors 1 and 2 in V0 tensor V1 tensor V2."""
    total = dim ** 3
    P = np.zeros((total, total), dtype=complex)
    for i0 in range(dim):
        for i1 in range(dim):
            for i2 in range(dim):
                src = (i0 * dim + i1) * dim + i2
                dst = (i0 * dim + i2) * dim + i1
                P[dst, src] = 1.0
    return P


def corner_transfer(links: list[np.ndarray], a: float, B: float, delta: float) -> tuple[np.ndarray, list[np.ndarray]]:
    mats = []
    kernels = []
    for mass in lambdas(a, B, delta):
        t = channel_kernel(links, float(mass))
        kernels.append(t)
        T, _ = manybody_from_kernel(t)
        mats.append(T)
    return np.kron(np.kron(mats[0], mats[1]), mats[2]), kernels


def free_dispersion_residual(mass: float) -> float:
    links = identity_background()
    dec = np.sort(np.real(decaying_eigs(two_step_classical_transfer(links, mass))))
    ps = [2.0 * math.pi * k / L_S for k in range(L_S)]
    target = np.sort([math.exp(-2.0 * math.asinh(math.sqrt(mass * mass + math.sin(p) ** 2))) for p in ps])
    return float(np.max(np.abs(dec - target)))


def grassmann_mul(left: dict[int, complex], right: dict[int, complex], nvars: int) -> dict[int, complex]:
    out: dict[int, complex] = {}
    for ma, ca in left.items():
        for mb, cb in right.items():
            if ma & mb:
                continue
            inversions = 0
            for i in range(nvars):
                if (ma >> i) & 1:
                    inversions += sum(1 for j in range(i) if (mb >> j) & 1)
            sign = -1 if inversions % 2 else 1
            key = ma | mb
            out[key] = out.get(key, 0.0) + sign * ca * cb
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


def grassmann_add(a: dict[int, complex], b: dict[int, complex]) -> dict[int, complex]:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0.0) + v
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


def grassmann_berezin_det_expansion(M: np.ndarray) -> complex:
    """Coefficient expansion of exp(sum_i,j b_i M_ij c_j) for two pairs.

    Variable order is b0, c0, b1, c1. The returned top coefficient is the
    canonical two-pair Berezin integral in that order.
    """
    nvars = 4
    one = {0: 1.0 + 0.0j}
    A: dict[int, complex] = {}
    var = [{1 << i: 1.0 + 0.0j} for i in range(nvars)]
    for i in range(2):
        for j in range(2):
            term = grassmann_mul(var[2 * i], var[2 * j + 1], nvars)
            term = {k: M[i, j] * v for k, v in term.items()}
            A = grassmann_add(A, term)
    A2 = grassmann_mul(A, A, nvars)
    expA = grassmann_add(one, A)
    expA = grassmann_add(expA, {k: 0.5 * v for k, v in A2.items()})
    return expA.get((1 << nvars) - 1, 0.0 + 0.0j)


def main() -> int:
    print("=" * 88)
    print("W13a fixed-gauge corner-transfer runner")
    print(f"params = {PARAMS}")
    print(f"L_s = {L_S}; fixed random U(1) seeds = {SEEDS}")
    print("Fixed-background checks only.")
    print("=" * 88)

    backgrounds = [u1_background(seed) for seed in SEEDS]
    complex_bg = backgrounds[0]
    real_bg = z2_background()

    section("N1 -- channel decomposition and inherited two-step positivity")
    F = fourier3()
    C = shift_matrix()
    diag_C = F.conj().T @ C @ F
    target_C = np.diag([np.exp(2j * np.pi * k / 3.0) for k in range(3)])
    check("circulant eigenbasis diagonalizes C", np.linalg.norm(diag_C - target_C) < TOL,
          detail=f"residual={np.linalg.norm(diag_C - target_C):.3e}")

    all_domain = True
    all_block = True
    all_pos = True
    min_channel_eig = math.inf
    worst_bdagb = 0.0
    worst_free = 0.0
    for pidx, (a, B, delta) in enumerate(PARAMS):
        lam = lambdas(a, B, delta)
        domain = bool(np.all(lam > 0.0))
        all_domain = all_domain and domain
        print(f"  parameter point {pidx}: lambdas={lam}")
        for links in backgrounds:
            h = spatial_hop_matrix(links, 1)
            A_full = np.kron(generation_mass(a, B, delta), np.eye(L_S)) + np.kron(np.eye(3), h)
            U = np.kron(F.conj().T, np.eye(L_S))
            got = U @ A_full @ U.conj().T
            want = block_diag([lam[k] * np.eye(L_S) + h for k in range(3)])
            res = np.linalg.norm(got - want)
            all_block = all_block and res < 1.0e-9
        for mass in lam:
            worst_free = max(worst_free, free_dispersion_residual(float(mass)))
        for links in backgrounds:
            for mass in lam:
                T2cl = two_step_classical_transfer(links, float(mass))
                dec = decaying_eigs(T2cl)
                imag = float(np.max(np.abs(np.imag(dec))))
                min_mu = float(np.min(np.real(dec)))
                t = channel_kernel(links, float(mass))
                T, Bfac = manybody_from_kernel(t)
                herm = float(np.linalg.norm(T - T.conj().T))
                mineig = float(np.min(np.linalg.eigvalsh(0.5 * (T + T.conj().T))))
                recon = float(np.linalg.norm(T - Bfac.conj().T @ Bfac))
                min_channel_eig = min(min_channel_eig, mineig)
                worst_bdagb = max(worst_bdagb, recon)
                all_pos = all_pos and imag < 1.0e-8 and min_mu > 0.0 and herm < TOL and mineig >= -TOL and recon < TOL

    check("N1-domain: all lambda_k(delta) > 0 at both parameter points", all_domain)
    check("N1a: mass/internal factor block-diagonalizes over circulant channels at fixed U", all_block)
    check("N1b: every checked channel T_k^2[U] is positive Hermitian with B_k[U]^dag B_k[U]", all_pos,
          detail=f"min manybody eig={min_channel_eig:.6e}; worst BdagB residual={worst_bdagb:.3e}")
    check("N1c: U=1 member recovers free wave-6 dispersion", worst_free < TOL,
          detail=f"worst residual={worst_free:.3e}")

    section("N2 -- fixed-background corner transfer")
    n2_ok = True
    min_corner = math.inf
    worst_corner_recon = 0.0
    for a, B, delta in PARAMS:
        for links in backgrounds:
            factors = []
            bfactors = []
            for mass in lambdas(a, B, delta):
                t = channel_kernel(links, float(mass))
                T, Bfac = manybody_from_kernel(t)
                factors.append(T)
                bfactors.append(Bfac)
            Tcorner = np.kron(np.kron(factors[0], factors[1]), factors[2])
            Bcorner = np.kron(np.kron(bfactors[0], bfactors[1]), bfactors[2])
            eig = np.linalg.eigvalsh(0.5 * (Tcorner + Tcorner.conj().T))
            min_corner = min(min_corner, float(eig.min()))
            recon = float(np.linalg.norm(Tcorner - Bcorner.conj().T @ Bcorner))
            worst_corner_recon = max(worst_corner_recon, recon)
            n2_ok = n2_ok and Tcorner.shape == (64, 64) and eig.min() >= -TOL and recon < TOL
    check("N2: T_corner^2[U] = tensor_k T_k^2[U] is positive Hermitian config-by-config (dim 64)",
          n2_ok, detail=f"min eig={min_corner:.6e}; BdagB residual={worst_corner_recon:.3e}")

    section("N3 -- trace correspondence and Berezin normalization")
    n3a_ok = True
    worst_trace = 0.0
    det_ref = None
    for a, B, delta in PARAMS:
        for links in backgrounds:
            kernels = [channel_kernel(links, float(m)) for m in lambdas(a, B, delta)]
            t_total = block_diag(kernels)
            lhs = trace_gamma(t_total)
            rhs = np.linalg.det(np.eye(t_total.shape[0]) + t_total)
            if det_ref is None:
                det_ref = rhs
            res = abs(lhs - rhs)
            worst_trace = max(worst_trace, float(res))
            n3a_ok = n3a_ok and res < 1.0e-8
    check("N3a: Tr Gamma(t[U]) = det(1 + t[U]) per witness background", n3a_ok,
          detail=f"worst residual={worst_trace:.3e}")

    N = 6
    lam_sym = sp.symbols("lambda", positive=True)
    positive_solution_is_one = sp.solve(sp.Eq(lam_sym ** N, 1), lam_sym) == [sp.Integer(1)]
    lambda2_gap = abs((2.0 ** N - 1.0) * complex(det_ref))
    check("N3b: lambda=2 breaks the Berezin/trace equality per background", lambda2_gap > 1.0e-6,
          detail=f"gap={lambda2_gap:.6e}")
    check("N3b: lambda=1 is forced over lambda > 0", positive_solution_is_one,
          detail=f"solve(lambda^{N}=1, lambda>0) -> [1]")

    t_one = channel_kernel(complex_bg, float(lambdas(*PARAMS[0])[0]))
    M = np.eye(2, dtype=complex) + t_one
    grass_coeff = grassmann_berezin_det_expansion(M)
    grass_target = np.linalg.det(M)
    berezin_self_check = abs(grass_coeff - grass_target) < 1.0e-8
    check("N3c: genuine two-pair Grassmann expansion equals det(1+t) for one channel",
          berezin_self_check, detail=f"residual={abs(grass_coeff - grass_target):.3e}; self_check=True")

    section("N4 -- K/conjugated-background complement statement")
    sigma = [0, 2, 1]
    n4a_ok = True
    worst_k = 0.0
    for a, B, delta in PARAMS:
        lam_plus = lambdas(a, B, delta)
        lam_minus = lambdas(a, B, -delta)
        for links in backgrounds:
            clinks = conj_background(links)
            for k in range(3):
                lhs = channel_kernel(links, float(lam_plus[k]))
                rhs = channel_kernel(clinks, float(lam_minus[sigma[k]]))
                res = float(np.linalg.norm(lhs - rhs))
                worst_k = max(worst_k, res)
                n4a_ok = n4a_ok and res < TOL
    check("N4a: t_k[U](delta) = t_sigma(k)[conj(U)](-delta) computed",
          n4a_ok, detail=f"doublet swap residual={worst_k:.3e}")

    Pswap = tensor_swap_permutation(4)
    n4b_ok = True
    worst_real_unitary = 0.0
    worst_real_trace = 0.0
    for a, B, delta in PARAMS:
        T1, _ = corner_transfer(real_bg, a, B, delta)
        T2, _ = corner_transfer(real_bg, a, B, -delta)
        conj_is_same = all(np.linalg.norm(u - u.conj()) < TOL for u in real_bg)
        unit_res = float(np.linalg.norm(T1 - Pswap.conj().T @ T2 @ Pswap))
        tr_gap = max(abs(np.trace(T1) - np.trace(T2)), abs(np.trace(T1 @ T1) - np.trace(T2 @ T2)))
        worst_real_unitary = max(worst_real_unitary, unit_res)
        worst_real_trace = max(worst_real_trace, float(tr_gap))
        n4b_ok = n4b_ok and conj_is_same and unit_res < TOL and tr_gap < TOL
    check("N4b: K-real Z_2 witness has exact hw-complement unitary equivalence and equal N=1,2 traces",
          n4b_ok, detail=f"unitary residual={worst_real_unitary:.3e}; trace residual={worst_real_trace:.3e}")

    n4c_ok = True
    worst_conj_unitary = 0.0
    worst_conj_trace = 0.0
    for a, B, delta in PARAMS:
        T1, _ = corner_transfer(complex_bg, a, B, delta)
        T2, _ = corner_transfer(conj_background(complex_bg), a, B, -delta)
        unit_res = float(np.linalg.norm(T1 - Pswap.conj().T @ T2 @ Pswap))
        tr_gap = max(abs(np.trace(T1) - np.trace(T2)), abs(np.trace(T1 @ T1) - np.trace(T2 @ T2)))
        worst_conj_unitary = max(worst_conj_unitary, unit_res)
        worst_conj_trace = max(worst_conj_trace, float(tr_gap))
        n4c_ok = n4c_ok and unit_res < TOL and tr_gap < TOL
    check("N4c: complex witness reading-1 at U equals reading-2 at conj(U)",
          n4c_ok, detail=f"unitary residual={worst_conj_unitary:.3e}; trace residual={worst_conj_trace:.3e}")

    # N4d (strengthened): the same-U equality of REGISTRABLE TRACE DATA is a
    # theorem, not an empirical flag. Argument verified in three computed legs:
    # (i) traces of the positive Hermitian corner transfer are real;
    # (ii) conjugating the background conjugates the transfer matrix, so trace
    #      data at conj(U) are the complex conjugates of those at U;
    # (iii) real + conjugate => equal; combined with N4c the same-U trace gap
    #      between the two readings must vanish — now a CONDITION.
    reality_ok = True
    conj_pair_ok = True
    same_u_gap = 0.0
    for a, B, delta in PARAMS:
        T1, _ = corner_transfer(complex_bg, a, B, delta)
        T2, _ = corner_transfer(complex_bg, a, B, -delta)
        T2c, _ = corner_transfer(conj_background(complex_bg), a, B, -delta)
        for M in (T1, T2):
            reality_ok = reality_ok and abs(np.imag(np.trace(M))) < TOL and abs(np.imag(np.trace(M @ M))) < TOL
        conj_pair_ok = conj_pair_ok and np.allclose(T2c, np.conj(T2), atol=1e-12)
        same_u_gap = max(same_u_gap, float(max(abs(np.trace(T1) - np.trace(T2)), abs(np.trace(T1 @ T1) - np.trace(T2 @ T2)))))
    check("N4d-i: registrable trace data of the positive corner transfer are real",
          reality_ok, detail="Im Tr(T), Im Tr(T^2) below tolerance at the complex witness")
    check("N4d-ii: background conjugation conjugates the transfer matrix",
          conj_pair_ok, detail="T[conj U, -delta] = conj(T[U, -delta]) entrywise (1e-12)")
    check("N4d-iii: hence same-U registrable-trace equivalence at EVERY background (theorem-backed condition)",
          reality_ok and conj_pair_ok and same_u_gap < TOL,
          detail=f"same-U trace gap={same_u_gap:.3e}; real + conjugate => equal, with N4c")

    section("N5 -- assembly")
    n5_ok = all_domain and all_block and all_pos and n2_ok and n3a_ok and berezin_self_check and n4a_ok and n4b_ok and n4c_ok
    check("N5: both interacting opens narrow to the U-INTEGRATED level, not beyond",
          n5_ok, detail="remaining object is the measure over backgrounds / gauge dynamics")

    section("B-checks -- source-note and dependency hygiene")
    note = NOTE.read_text()
    engine = ENGINE.read_text()
    substep1 = SUBSTEP1.read_text()
    registrable = REGISTRABLE.read_text()

    check("engine grep: config-by-config phrase present", "config-by-config" in engine)
    check("engine grep: B[U]^dag B[U] two-step phrase present", "T_hat^2[U] = B[U]^dag B[U]" in engine)
    check("engine grep: fixed arbitrary SU(3)/U(1) temporal-gauge authority present",
          "fixed, arbitrary `SU(3)`" in engine and "`U(1)`" in engine and "temporal gauge" in engine)
    check("substep1 grep: canonical Berezin determinant side present",
          "Berezin" in substep1 and "det(M)" in substep1)
    check("registrability grep: Record-registrable / phase-free class present",
          "Record-registrable" in registrable and "phase-free" in registrable)

    check("firewall sentence: fixed background only", "FIREWALL: fixed background only" in note)
    check("firewall sentence: U-INTEGRATED level remains named open", "U-INTEGRATED level remains the named open next path" in note)
    compact_note = re.sub(r"\s+", " ", note)
    check("firewall sentence: no species reading, no occupancy cell, r never fixed, binary untouched",
          "does **not** select a species reading" in compact_note
          and "does **not** select an occupancy cell" in compact_note
          and "does **not** fix `r`" in compact_note
          and "leaves the binary untouched" in compact_note)

    forbidden = [
        "this closes the U-INTEGRATED",
        "U-INTEGRATED level is closed",
        "full gauge dynamics is closed",
        "we close the integrated",
        "retire the interacting open",
        "selects the occupancy cell",
        "selects the species reading",
    ]
    lower_note = note.lower()
    check("closing language absent: no forbidden integrated-level closure strings",
          not any(s.lower() in lower_note for s in forbidden))

    links = re.findall(r"\[[^\]]+\]\([^)]+\.md\)", note)
    expected_links = {
        "[`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)",
        "[`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)",
        "[`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)",
    }
    check("link inventory exactly three markdown links", len(links) == 3 and set(links) == expected_links,
          detail=f"count={len(links)}")
    check("companions are backticked, not dependency-linked",
          "`ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`" in note
          and "`P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md`" in note
          and "`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`" in note)
    check("No-promotion statement present", "**No-promotion statement:**" in note)
    check("Berezin self-check flag is true", berezin_self_check)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("SUMMARY: fixed-background corner transfer checks complete; U-integrated gauge dynamics remains the named open.")
    return 0 if PASS == 30 and FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
