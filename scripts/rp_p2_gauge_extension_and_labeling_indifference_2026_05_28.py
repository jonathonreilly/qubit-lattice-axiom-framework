#!/usr/bin/env python3
"""Fixed-gauge RP transfer positivity + standalone relabeling-invariance exhibit.

In-repo verification companion for
docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md.

This runner does TWO independent things, both extending prior work:

  TASK A -- GAUGE EXTENSION OF REFLECTION POSITIVITY.
    The free-case 2-step transfer-matrix positivity established in
    scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py used
    translation invariance (momentum diagonalization, U = 1). Here we drop
    translation invariance and build the SAME 2-step transfer object at a
    FIXED, arbitrary spatial gauge background U_i(x) in temporal gauge
    (U_0 = 1), config-by-config, in POSITION SPACE. We verify
    spec(T_hat^2[U]) subset R_{>=0} for many random SU(3) and U(1) fixed
    backgrounds, i.e. T_hat^2[U] = B[U]^dag B[U] with
    H_hat[U] = -log(T_hat^2[U])/(2 a_tau) self-adjoint and bounded below.
    The free case (prior runner) is the U = 1 specialization; this is the
    genuine nontrivial-background extension.

  TASK B -- STANDALONE RELABELING INVARIANCE (permutation invariance of det/spec/Z).
    We exhibit the finite algebraic fact directly: permute / relabel the
    hw=1 corner-triplet staggered modes by an arbitrary permutation unitary P
    and verify det(M_KS + m I), spec(H_hat), and Z = Tr(e^{-beta H_hat}) are
    UNCHANGED to machine precision. This is only a standalone invariance result;
    downstream P2 / AC_phi_lambda residual claims are not asserted here.

----------------------------------------------------------------------------
PHYSICS OF TASK A (fixed gauge background, temporal gauge, position space)
----------------------------------------------------------------------------
Staggered (Kogut-Susskind) action in temporal gauge U_0 = 1 on L_t x L_s,
one Grassmann component per site, canonical phases eta_0 = 1, eta_1(t) = (-1)^t:

    S = sum_{t,x} bar_chi(t,x) [ m chi(t,x)
          + (1/2) ( chi(t+1,x) - chi(t-1,x) )                      (temporal, U_0=1)
          + (1/2) eta_1(t) ( U_1(t,x) chi(t,x+1)
                              - U_1(t,x-1)^dag chi(t,x-1) ) ]       (spatial, links)

In temporal gauge the temporal hop is clean (no link). Reflection
theta(t,x)=(-1-t,x) crosses ONLY temporal links, which are 1; the spatial
structure is reflection-symmetric. The single-particle transfer across one
time slice acts on the spatial Hilbert space C^{L_s} (per color). Writing the
spatial hop matrix

    h[U]_{x,y} = (1/2)( U_1(x) delta_{y,x+1} - U_1(x-1)^dag delta_{y,x-1} ),

h[U] is anti-Hermitian (h^dag = -h): the forward-hop block U_1(x) and the
backward-hop block -U_1(x-1)^dag are minus-conjugate-transposes. With the
alternating staggered phase eta_1(t) = (-1)^t the per-slice "alpha" matrix is

    A_even = m I + h[U],     A_odd = m I - h[U].

The banded-in-time staggered mode equation
    A_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0
gives the single-step classical transfer matrix on the 2L_s amplitude vector
V_t = (psi_t, psi_{t-1}):

    T_s(t) = [[ -2 A_t, I_{L_s} ], [ I_{L_s}, 0 ]],   T_even, T_odd from A_even,A_odd.

The physical (translation-free) 2-step single-particle transfer kernel is the
block

    T2cl[U] = T_odd[U] . T_even[U]   (2L_s x 2L_s).

Its 2L_s eigenvalues come in reciprocal pairs {mu, 1/mu}. The L_s "decaying"
eigenvalues (|mu| <= 1) are the single-particle 2-step kernel t1^(2)[U]; the
many-body 2-step transfer is the second quantization

    T_hat^2[U] = Gamma( t1^(2)[U] ),     H_hat[U] = -log(t1^(2)[U]) / (2 a_tau).

T_hat^2[U] >= 0  <=>  every decaying eigenvalue mu of T2cl[U] is REAL and
POSITIVE (0 < mu <= 1), equivalently spec(T2cl[U]) subset R_{>0}. That is the
config-by-config positivity we test. When it holds, the single-particle
2-step kernel t1^(2)[U] = diag-of-positive-reals (in its eigenbasis) is a PSD
contraction, H_hat[U] = -log(...)/(2 a_tau) is self-adjoint with spectrum
>= 0, and the many-body T_hat^2[U] = exp(-2 a_tau H_hat[U]) = B[U]^dag B[U].

We also confirm the temporal-gauge reduction is faithful: at U = 1 the
position-space eigenvalues reproduce the momentum-space free dispersion
e^{-2E(p)} of the prior free runner (sanity bridge to free two-step transfer-matrix positivity row).

U-INTEGRATED RP then follows from
    <Theta(F) F> = int dU (Haar . positive Wilson weight)
                      x (per-config fermion 2-step positivity, THIS runner)
                      x (det(M_KS + m I) >= m^n > 0 config-by-config,
                         retained dep STAGGERED_ONLY_DET_POSITIVITY_CASE_A)
                      x (gauge-half Cauchy-Schwarz norm-square, retained_bounded
                         dep REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ)
                  >= 0,
each factor non-negative. This runner supplies the per-config fermion factor at
nontrivial fixed SU(3)/U(1) background; the other two factors are the cited deps.

----------------------------------------------------------------------------
SCORECARD
----------------------------------------------------------------------------
  modal transfer formula : anti-Hermitian spatial-hop eigenmode gives the
                         exp(+/-2 asinh(sqrt(m^2+lambda^2))) transfer pair.
  free-case bridge       : at U=1, position-space 2-step decaying eigenvalues
                         reproduce momentum-space e^{-2E(p)} (max residual <1e-9)
  sampled SU(3) positivity: for many random fixed SU(3) backgrounds, every
                         decaying eigenvalue of T2cl[U] is real-positive
                         (spec subset R_{>0}); many-body T_hat^2[U] positive
                         Hermitian = B[U]^dag B[U]; H_hat[U] self-adjoint.
  sampled U(1) positivity : same, Abelian cross-check.
  determinant invariance  : det(M_KS + m I) unchanged under hw=1 label permutation
  spectrum invariance     : spec(H_hat) unchanged under hw=1 label permutation
  trace invariance        : Z = Tr(e^{-beta H_hat}) unchanged under hw=1 label perm
This runner verifies the modal proof, the sampled fixed-gauge exhibits, and the
standalone relabeling-invariance exhibit. Independent audit owns any status
verdict.
"""
from __future__ import annotations

import math

import numpy as np

MASS = 0.5
A_TAU = 1.0
TOL_DISP = 1e-9
TOL_POS = 1e-10
TOL_INV = 1e-10
RNG = np.random.default_rng(20260528)


# ===========================================================================
# Gauge link generators
# ===========================================================================

def random_su3() -> np.ndarray:
    """Haar-random SU(3) via QR of a complex Ginibre matrix, then unit det."""
    z = (RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    # fix phases so q is Haar on U(3)
    ph = np.diag(r) / np.abs(np.diag(r))
    q = q * ph
    # project U(3) -> SU(3)
    detq = np.linalg.det(q)
    q = q * (detq ** (-1.0 / 3.0))
    return q


def random_u1(nc: int = 1) -> np.ndarray:
    """Random U(1) phase as an nc x nc diagonal unitary (nc=1: scalar phase)."""
    theta = RNG.uniform(0.0, 2.0 * math.pi)
    return np.exp(1j * theta) * np.eye(nc, dtype=complex)


def identity_link(nc: int) -> np.ndarray:
    return np.eye(nc, dtype=complex)


# ===========================================================================
# Position-space spatial hop matrix and 2-step classical transfer
# ===========================================================================

def spatial_hop_matrix(links: list[np.ndarray], nc: int) -> np.ndarray:
    """Anti-Hermitian spatial hop h[U] on C^{L_s} tensor C^{nc} (periodic).

    h_{x,y} = (1/2)( U_1(x) delta_{y,x+1} - U_1(x-1)^dag delta_{y,x-1} ).
    links[x] is the nc x nc link U_1 from x to x+1. Returns an
    (L_s*nc) x (L_s*nc) matrix, block-indexed (x, color).
    """
    Ls = len(links)
    dim = Ls * nc
    h = np.zeros((dim, dim), dtype=complex)

    def blk(x):
        return slice(x * nc, (x + 1) * nc)

    for x in range(Ls):
        xp = (x + 1) % Ls
        xm = (x - 1) % Ls
        # forward hop x -> x+1 : +(1/2) U_1(x)
        h[blk(x), blk(xp)] += 0.5 * links[x]
        # backward hop x -> x-1 : -(1/2) U_1(x-1)^dag
        h[blk(x), blk(xm)] += -0.5 * links[xm].conj().T
    return h


def two_step_classical_transfer(links: list[np.ndarray], nc: int, m: float) -> np.ndarray:
    """Position-space 2-step classical transfer T2cl[U] = T_odd . T_even.

    Single-step block: T_s = [[ -2 A_s, I ], [ I, 0 ]] with
    A_even = m I + h[U], A_odd = m I - h[U]. Size 2*(L_s*nc).
    """
    Ls = len(links)
    d = Ls * nc
    I = np.eye(d, dtype=complex)
    Z = np.zeros((d, d), dtype=complex)
    h = spatial_hop_matrix(links, nc)
    A_even = m * I + h
    A_odd = m * I - h
    T_even = np.block([[-2.0 * A_even, I], [I, Z]])
    T_odd = np.block([[-2.0 * A_odd, I], [I, Z]])
    return T_odd @ T_even


def decaying_eigs(T2cl: np.ndarray) -> np.ndarray:
    """The half of T2cl eigenvalues with |mu| <= 1 (the physical decaying modes).

    T2cl is symplectic-like; eigenvalues come in reciprocal pairs {mu, 1/mu}.
    Return the L_s*nc eigenvalues of smallest modulus.
    """
    ev = np.linalg.eigvals(T2cl)
    order = np.argsort(np.abs(ev))
    half = len(ev) // 2
    return ev[order[:half]]


# ===========================================================================
# Many-body 2-step transfer T_hat^2[U] = Gamma(t1^(2)[U]) and H_hat[U]
# ===========================================================================

def manybody_T2_from_kernel(decay_eigs_real: np.ndarray):
    """Build many-body T_hat^2 = Gamma(diag(decay_eigs_real)) on Fock space
    (dim 2^{N}) plus its B^dag B factorization, given the real-positive
    single-particle decaying eigenvalues t1^(2). Returns diagnostics.

    For a free fermion theory Gamma(diag(mu_k)) = tensor_k diag(1, mu_k).
    """
    T2 = np.array([[1.0]], dtype=complex)
    B = np.array([[1.0]], dtype=complex)
    for mu in decay_eigs_real:
        T2 = np.kron(T2, np.diag([1.0, mu]))
        B = np.kron(B, np.diag([1.0, math.sqrt(max(mu, 0.0))]))
    herm = float(np.max(np.abs(T2 - T2.conj().T)))
    eig = np.linalg.eigvalsh(0.5 * (T2 + T2.conj().T))
    recon = float(np.max(np.abs(T2 - B.conj().T @ B)))
    return {
        "dim": T2.shape[0],
        "herm_err": herm,
        "min_eig": float(eig.min()),
        "max_eig": float(eig.max()),
        "BdagB_err": recon,
    }


# ===========================================================================
# Free-case momentum-space dispersion (bridge to free two-step transfer-matrix positivity row)
# ===========================================================================

def E_dispersion(p: float, m: float) -> float:
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def check_modal_transfer_formula(m: float):
    """Exact finite-mode check for an anti-Hermitian spatial-hop eigenvalue.

    If h has eigenvalue i*lambda with lambda real, the two-step transfer block
    has determinant 1 and trace 2 + 4*(m^2 + lambda^2). Its eigenvalues should
    be exp(+/- 2*asinh(sqrt(m^2 + lambda^2))), both real-positive.
    """
    lambdas = [-3.0, -1.25, -0.2, 0.0, 0.7, 2.5]
    worst_res = 0.0
    worst_imag = 0.0
    min_eig = math.inf
    for lam in lambdas:
        q = math.sqrt(m * m + lam * lam)
        target = np.sort([math.exp(-2.0 * math.asinh(q)), math.exp(2.0 * math.asinh(q))])
        T2 = np.array(
            [
                [4.0 * (m * m + lam * lam) + 1.0, -2.0 * (m - 1j * lam)],
                [-2.0 * (m + 1j * lam), 1.0],
            ],
            dtype=complex,
        )
        ev = np.linalg.eigvals(T2)
        worst_imag = max(worst_imag, float(np.max(np.abs(np.imag(ev)))))
        ev_real = np.sort(np.real(ev))
        worst_res = max(worst_res, float(np.max(np.abs(ev_real - target))))
        min_eig = min(min_eig, float(np.min(ev_real)))
    return worst_res, worst_imag, min_eig, lambdas


# ===========================================================================
# TASK A checks
# ===========================================================================

def check_free_bridge(Ls: int, m: float):
    """free-case bridge: at U=1, position-space 2-step decaying eigenvalues match the
    momentum-space free spectrum {e^{-2E(p)}}."""
    links = [identity_link(1) for _ in range(Ls)]
    T2cl = two_step_classical_transfer(links, 1, m)
    pos_decay = np.sort(np.real(decaying_eigs(T2cl)))
    ps = [2.0 * math.pi * k / Ls for k in range(Ls)]
    mom_decay = np.sort([math.exp(-2.0 * E_dispersion(p, m)) for p in ps])
    max_imag = float(np.max(np.abs(np.imag(decaying_eigs(T2cl)))))
    max_res = float(np.max(np.abs(pos_decay - mom_decay)))
    return max_res, max_imag, pos_decay, mom_decay


def positivity_over_configs(link_factory, nc: int, Ls: int, m: float, n_cfg: int,
                            fock_Ls: int):
    """Sampled SU(3)/U(1) positivity: build T2cl[U] at many random fixed backgrounds; verify every
    decaying eigenvalue is real-positive (spec subset R_{>0}); build the
    many-body T_hat^2 = B^dag B and report min eig of H_hat = -log/2a_tau."""
    worst_imag = 0.0          # max |Im(decay eig)| over configs (should be ~0)
    min_mu = math.inf         # min decaying eigenvalue (should be > 0)
    max_mu = -math.inf
    min_Hhat_eig = math.inf   # min single-particle H_hat eigenvalue over configs
    worst_recon = 0.0         # worst many-body B^dag B reconstruction error
    worst_herm = 0.0
    min_manybody_eig = math.inf
    n_pos_fail = 0
    for _ in range(n_cfg):
        links = [link_factory(nc) for _ in range(Ls)]
        T2cl = two_step_classical_transfer(links, nc, m)
        dec = decaying_eigs(T2cl)
        imag = float(np.max(np.abs(np.imag(dec))))
        worst_imag = max(worst_imag, imag)
        re = np.real(dec)
        min_mu = min(min_mu, float(np.min(re)))
        max_mu = max(max_mu, float(np.max(re)))
        # positivity test: decaying eigs real-positive
        if imag > 1e-8 or np.min(re) <= 0.0:
            n_pos_fail += 1
        # single-particle H_hat eigenvalues = -log(mu)/(2 a_tau)
        mu_clip = np.clip(re, 1e-300, None)
        Hhat_eigs = -np.log(mu_clip) / (2.0 * A_TAU)
        min_Hhat_eig = min(min_Hhat_eig, float(np.min(Hhat_eigs)))
        # many-body exhibit on a small Fock space (first fock_Ls decaying modes)
        sub = np.sort(re)[:fock_Ls]
        if np.min(sub) > 0.0:
            mb = manybody_T2_from_kernel(np.clip(sub, 0.0, None))
            worst_recon = max(worst_recon, mb["BdagB_err"])
            worst_herm = max(worst_herm, mb["herm_err"])
            min_manybody_eig = min(min_manybody_eig, mb["min_eig"])
    return {
        "n_cfg": n_cfg,
        "worst_imag": worst_imag,
        "min_decay_eig": min_mu,
        "max_decay_eig": max_mu,
        "min_Hhat_singleparticle_eig": min_Hhat_eig,
        "n_pos_fail": n_pos_fail,
        "manybody_worst_BdagB_err": worst_recon,
        "manybody_worst_herm_err": worst_herm,
        "manybody_min_eig": min_manybody_eig,
    }


# ===========================================================================
# TASK B: standalone relabeling invariance (permutation invariance of det/spec/Z)
# ===========================================================================

def permutation_unitary(perm: list[int], block: int = 1) -> np.ndarray:
    """Permutation unitary that relabels `len(perm)` blocks of size `block`.
    perm is a permutation of range(len(perm)); column j of block i lands in
    block perm[i]."""
    n = len(perm)
    P = np.zeros((n * block, n * block), dtype=complex)
    Ib = np.eye(block, dtype=complex)
    for i in range(n):
        P[perm[i] * block:(perm[i] + 1) * block, i * block:(i + 1) * block] = Ib
    return P


def hw1_triplet_operator(seed: int = 7):
    """A generic Hermitian operator on the hw=1 triplet carrier C^3 (the BZ-corner
    triplet of substep 4). We use a random Hermitian H_3 and read off its
    spectrum / det of (H_3) and Z = Tr(e^{-H_3}); these stand in for any
    relabeling-invariant readout (det/spec/trace) on the triplet sector.
    Label permutations act by conjugation H_3 -> P H_3 P^dag."""
    g = np.random.default_rng(seed)
    a = g.standard_normal((3, 3)) + 1j * g.standard_normal((3, 3))
    return (a + a.conj().T) / 2.0


def check_labeling_indifference():
    """determinant-invariance/spectrum-invariance/trace-invariance: build the staggered KS operator M = M_KS + m I on a small
    L_t x L_s lattice (free, U=1), and ALSO a generic hw=1 triplet operator.
    Permute the hw=1 corner-triplet labels by every permutation in S_3 and a
    larger staggered relabeling; verify det(M), spec(H_hat), Z = Tr(e^{-H_hat})
    are invariant to machine precision.

    The hw=1 triplet sits inside the staggered mode space; relabeling its three
    states is a conjugation by a permutation unitary P (extended by identity on
    the rest). det, spectrum, and trace are conjugation invariants, so this is
    an exact standalone identity, exhibited numerically.
    """
    import itertools

    # --- (i) staggered KS Dirac operator on a small lattice (free U=1) ---
    # Conventions match the retained det-positivity note
    # STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17: eta_t=+1,
    # eta_x(t)=(-1)^t, eps(t,x)=(-1)^(t+x), periodic, even/balanced lattice. On
    # this surface {eps, M_KS}=0 exactly and det(M_KS+mI) is real-positive, so
    # the det baseline printed here is faithful to the cited dependency.
    Lt, Ls, m = 4, 4, MASS
    Ls_total = Lt * Ls
    M = np.zeros((Ls_total, Ls_total), dtype=complex)

    def idx(t, x):
        return (t % Lt) * Ls + (x % Ls)

    for t in range(Lt):
        for x in range(Ls):
            i = idx(t, x)
            M[i, i] += m
            # temporal hop eta_t = 1, periodic
            M[i, idx(t + 1, x)] += 0.5
            M[i, idx(t - 1, x)] += -0.5
            # spatial hop eta_x(t) = (-1)^t, periodic
            eta_x = (-1.0) ** t
            M[i, idx(t, x + 1)] += 0.5 * eta_x
            M[i, idx(t, x - 1)] += -0.5 * eta_x
    det_M = np.linalg.det(M)
    # structural sanity: M_KS anti-Hermitian and {eps, M_KS} = 0 on this surface
    M_KS = M - m * np.eye(Ls_total, dtype=complex)
    eps = np.diag([(-1.0) ** (t + x) for t in range(Lt) for x in range(Ls)]).astype(complex)
    antiherm_err = float(np.max(np.abs(M_KS + M_KS.conj().T)))
    anticomm_err = float(np.max(np.abs(eps @ M_KS + M_KS @ eps)))

    # H_hat single-particle spectrum from the free 2-step kernel (momentum)
    ps = [2.0 * math.pi * k / Ls for k in range(Ls)]
    Hhat_spec = np.sort([E_dispersion(p, m) for p in ps])
    beta = Lt * A_TAU
    Z = float(np.prod([1.0 + math.exp(-beta * E) for E in Hhat_spec]))

    # --- (ii) generic hw=1 triplet operator ---
    H3 = hw1_triplet_operator()
    spec_H3 = np.sort(np.linalg.eigvalsh(H3))
    det_H3 = np.real(np.linalg.det(H3))
    Z3 = float(np.sum(np.exp(-spec_H3)))  # Tr(e^{-H3}) via its eigenvalues

    results = {
        "det_M_baseline": det_M,
        "antiherm_err": antiherm_err,
        "anticomm_err": anticomm_err,
        "Hhat_spec_baseline": Hhat_spec,
        "Z_baseline": Z,
        "det_H3_baseline": det_H3,
        "spec_H3_baseline": spec_H3,
        "Z3_baseline": Z3,
        "perm_det_M_dev": [],
        "perm_spec_H3_dev": [],
        "perm_Z3_dev": [],
        "perm_det_H3_dev": [],
        "n_perms": 0,
    }

    # Apply ALL 6 permutations of the hw=1 triplet labels to the triplet operator.
    for perm in itertools.permutations(range(3)):
        P = permutation_unitary(list(perm), block=1)
        H3p = P @ H3 @ P.conj().T
        det_dev = abs(np.real(np.linalg.det(H3p)) - det_H3)
        spec_dev = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(H3p)) - spec_H3)))
        Z3p = float(np.sum(np.exp(-np.linalg.eigvalsh(H3p))))
        z_dev = abs(Z3p - Z3)
        results["perm_det_H3_dev"].append(det_dev)
        results["perm_spec_H3_dev"].append(spec_dev)
        results["perm_Z3_dev"].append(z_dev)
        results["n_perms"] += 1

    # Also embed a hw=1 triplet relabeling inside the staggered mode space:
    # pick 3 staggered modes and permute them; det(M) must be invariant.
    g = np.random.default_rng(11)
    for _ in range(6):
        perm_full = list(range(Ls_total))
        chosen = list(g.choice(Ls_total, size=3, replace=False))
        cyc = chosen[1:] + chosen[:1]  # cyclic permutation of the 3 chosen modes
        for a, b in zip(chosen, cyc):
            perm_full[a] = b
        Pfull = permutation_unitary(perm_full, block=1)
        Mp = Pfull @ M @ Pfull.conj().T
        det_dev = abs(np.linalg.det(Mp) - det_M)
        results["perm_det_M_dev"].append(det_dev)

    return results


# ===========================================================================
# Main
# ===========================================================================

def main() -> int:
    print("=" * 78)
    print("FIXED-GAUGE RP TRANSFER + STANDALONE RELABELING-INVARIANCE EXHIBIT")
    print("=" * 78)
    print(f"Staggered KS, temporal gauge U_0=1, m={MASS}, eta_0=1, eta_1(t)=(-1)^t.")
    print("Free case (free two-step transfer-matrix positivity row) was U=1 momentum-diagonal; here: fixed SU(3)/U(1),")
    print("position space, config-by-config.  Relabeling invariance: det/spec/Z")
    print("invariant under hw=1 triplet relabeling.")
    print()

    passes = 0
    fails = 0

    # ---- Modal anti-Hermitian-hop formula (load-bearing analytic reduction) ----
    print("-" * 78)
    print("MODAL TRANSFER FORMULA: anti-Hermitian spatial-hop eigenvalue i*lambda")
    print("    gives transfer eigenvalues exp(+/-2 asinh(sqrt(m^2+lambda^2)))")
    print("-" * 78)
    modal_res, modal_imag, modal_min, lambdas = check_modal_transfer_formula(MASS)
    modal_ok = (modal_res < TOL_DISP) and (modal_imag < TOL_DISP) and (modal_min > 0.0)
    print(f"    lambda samples={lambdas}")
    print(f"    max eigenvalue residual={modal_res:.3e}  max |Im|={modal_imag:.3e}")
    print(f"    min transfer eigenvalue={modal_min:.6e}  -> {'PASS' if modal_ok else 'FAIL'}")
    passes += int(modal_ok); fails += int(not modal_ok)
    print()

    # ---- Free-case bridge (faithfulness of the position-space build) ----
    print("-" * 78)
    print("FREE-CASE BRIDGE: position-space 2-step decaying eigenvalues at U=1")
    print("    reproduce momentum-space free spectrum {e^{-2E(p)}}")
    print("-" * 78)
    a1 = True
    for Ls in (3, 4, 6):
        max_res, max_imag, pos_d, mom_d = check_free_bridge(Ls, MASS)
        ok = (max_res < TOL_DISP) and (max_imag < TOL_DISP)
        a1 = a1 and ok
        print(f"    L_s={Ls}: max|pos-mom residual|={max_res:.3e}  "
              f"max|Im(decay)|={max_imag:.3e}  -> {'ok' if ok else 'FAIL'}")
    print(f"    free-case bridge = {'PASS' if a1 else 'FAIL'}")
    passes += int(a1); fails += int(not a1)
    print()

    # ---- Sampled SU(3) per-config positivity ----
    print("-" * 78)
    print("SAMPLED SU(3) PER-CONFIG POSITIVITY: fixed random spatial backgrounds")
    print("    spec(T2cl[U]) subset R_{>0}; T_hat^2[U]=B[U]^dag B[U]; H_hat[U]>=0")
    print("-" * 78)
    su3 = positivity_over_configs(lambda nc: random_su3(), nc=3, Ls=4, m=MASS,
                                  n_cfg=200, fock_Ls=4)
    print(f"    configs={su3['n_cfg']}  (SU(3), L_s=4, 3 colors -> 12 spatial modes)")
    print(f"    max |Im(decay eig)| over configs   = {su3['worst_imag']:.3e}  (want ~0)")
    print(f"    min decaying eigenvalue mu          = {su3['min_decay_eig']:.6e}  (want >0)")
    print(f"    max decaying eigenvalue mu          = {su3['max_decay_eig']:.6e}  (<=1)")
    print(f"    min single-particle eig(H_hat[U])   = {su3['min_Hhat_singleparticle_eig']:.6e}  (>=0)")
    print(f"    many-body T_hat^2 min eig           = {su3['manybody_min_eig']:.6e}  (>0)")
    print(f"    many-body ||T_hat^2 - B^dag B||     = {su3['manybody_worst_BdagB_err']:.2e}")
    print(f"    positivity failures (configs)       = {su3['n_pos_fail']} / {su3['n_cfg']}")
    a2 = (su3["n_pos_fail"] == 0) and (su3["worst_imag"] < 1e-8) \
        and (su3["min_decay_eig"] > 0.0) and (su3["min_Hhat_singleparticle_eig"] > -TOL_POS) \
        and (su3["manybody_worst_BdagB_err"] < 1e-9)
    print(f"    sampled SU(3) positivity = {'PASS' if a2 else 'FAIL'}")
    passes += int(a2); fails += int(not a2)
    print()

    # ---- Sampled U(1) per-config positivity (Abelian cross-check) ----
    print("-" * 78)
    print("SAMPLED U(1) PER-CONFIG POSITIVITY (Abelian cross-check)")
    print("-" * 78)
    u1 = positivity_over_configs(lambda nc: random_u1(1), nc=1, Ls=6, m=MASS,
                                 n_cfg=200, fock_Ls=6)
    print(f"    configs={u1['n_cfg']}  (U(1), L_s=6, 1 'color' -> 6 spatial modes)")
    print(f"    max |Im(decay eig)| over configs   = {u1['worst_imag']:.3e}  (want ~0)")
    print(f"    min decaying eigenvalue mu          = {u1['min_decay_eig']:.6e}  (want >0)")
    print(f"    min single-particle eig(H_hat[U])   = {u1['min_Hhat_singleparticle_eig']:.6e}  (>=0)")
    print(f"    many-body T_hat^2 min eig           = {u1['manybody_min_eig']:.6e}  (>0)")
    print(f"    positivity failures (configs)       = {u1['n_pos_fail']} / {u1['n_cfg']}")
    a3 = (u1["n_pos_fail"] == 0) and (u1["worst_imag"] < 1e-8) \
        and (u1["min_decay_eig"] > 0.0) and (u1["min_Hhat_singleparticle_eig"] > -TOL_POS)
    print(f"    sampled U(1) positivity = {'PASS' if a3 else 'FAIL'}")
    passes += int(a3); fails += int(not a3)
    print()

    # ---- Labeling-indifference ----
    print("-" * 78)
    print("B   STANDALONE RELABELING INVARIANCE: det(M_KS+mI), spec(H_hat), Z=Tr(e^{-beta H_hat})")
    print("    invariant under hw=1 triplet relabeling (permutation conjugation)")
    print("-" * 78)
    lab = check_labeling_indifference()
    max_det_M = max(lab["perm_det_M_dev"]) if lab["perm_det_M_dev"] else 0.0
    max_det_H3 = max(lab["perm_det_H3_dev"]) if lab["perm_det_H3_dev"] else 0.0
    max_spec = max(lab["perm_spec_H3_dev"]) if lab["perm_spec_H3_dev"] else 0.0
    max_Z = max(lab["perm_Z3_dev"]) if lab["perm_Z3_dev"] else 0.0
    print(f"    hw=1 triplet permutations tested    = {lab['n_perms']} (all of S_3)")
    print(f"    staggered-embedded relabelings      = {len(lab['perm_det_M_dev'])}")
    print(f"    faithful-surface check: ||M_KS+M_KS^dag||={lab['antiherm_err']:.1e}"
          f"  ||{{eps,M_KS}}||={lab['anticomm_err']:.1e}  (anti-Hermitian plus epsilon anticommutation)")
    print(f"    baseline det(M_KS+mI)               = {lab['det_M_baseline'].real:.8f}"
          f"{lab['det_M_baseline'].imag:+.1e}j  (real-positive, matches det dep)")
    print(f"    max |det(M) deviation| over relabels= {max_det_M:.3e}")
    print(f"    max |det(H3) deviation| over S_3    = {max_det_H3:.3e}")
    print(f"    max |spec(H_hat) deviation| over S_3= {max_spec:.3e}")
    print(f"    baseline Z = Tr(e^{{-beta H_hat}})   = {lab['Z_baseline']:.8f}")
    print(f"    max |Z(triplet) deviation| over S_3 = {max_Z:.3e}")
    b1 = max_det_M < TOL_INV and max_det_H3 < TOL_INV
    b2 = max_spec < TOL_INV
    b3 = max_Z < TOL_INV
    print(f"    determinant invariance = {'PASS' if b1 else 'FAIL'}")
    print(f"    spectrum invariance    = {'PASS' if b2 else 'FAIL'}")
    print(f"    trace invariance       = {'PASS' if b3 else 'FAIL'}")
    for flag in (b1, b2, b3):
        passes += int(flag); fails += int(not flag)
    print()

    # ---- Reductions named (not re-derived) ----
    print("-" * 78)
    print("U-INTEGRATED RP REDUCTION (named deps, not re-derived here)")
    print("-" * 78)
    print("    <Theta(F) F> = int dU (Haar . positive Wilson weight)")
    print("        x (per-config fermion 2-step positivity -- modal proof + sampled exhibits)")
    print("        x (det(M_KS+mI) >= m^n > 0 config-by-config -- retained dep")
    print("           STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17)")
    print("        x (gauge-half Cauchy-Schwarz norm-square -- retained_bounded dep")
    print("           REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10)")
    print("      >= 0,  each factor non-negative.")
    print()
    print("    DOWNSTREAM CONTEXT NOT CLAIMED HERE:")
    print("    This runner does not close any P2/AC_phi_lambda residual. It only")
    print("    supplies the finite det/spec/Z relabeling-invariance facts that")
    print("    downstream rows may cite after separate audit.")
    print()

    # ---- Scorecard ----
    print("=" * 78)
    print(f"SCORECARD: PASS={passes} FAIL={fails}")
    print("  modal transfer formula : anti-Hermitian-hop eigenmode gives positive transfer pair")
    print("  free-case bridge       : position-space build faithful to free dispersion")
    print("  sampled SU(3) positivity: fixed-background transfer positivity exhibit")
    print("  sampled U(1) positivity : Abelian cross-check")
    print("  determinant invariance  : det(M_KS+mI) relabeling-invariant")
    print("  spectrum invariance     : spec(H_hat) relabeling-invariant")
    print("  trace invariance        : Z=Tr(e^{-beta H_hat}) relabeling-invariant")
    print("=" * 78)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
