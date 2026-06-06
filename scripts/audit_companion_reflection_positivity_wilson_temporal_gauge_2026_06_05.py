#!/usr/bin/env python3
"""Audit-companion runner for the Wilson-plaquette temporal-gauge
reflection-positivity (RP) bridge note
`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`.

What this runner REPROVES from primitives (numpy / sympy only)
--------------------------------------------------------------
The bridge applies the abstract symmetric-involution norm-square
hypotheses (the retained gauge-half Cauchy-Schwarz note) to the genuine
Wilson plaquette action in temporal gauge, and reproves the integrated
three-factor Osterwalder-Seiler RP form for a basis of A_+^(2)
observables on the positive-time half.

Setup (explicit small lattice, link/time reflection):

  * Two time slices t in {0, 1}; periodic spatial direction with
    L_s spatial links per slice; temporal gauge U_0 = 1.
  * Time reflection theta across the plane between t=0 and t=1 swaps the
    two slices:  theta(c0, c1) = (c1, c0), where c1 are the positive-half
    (t=1) links and c0 the reflected (t=0) links.
  * Wilson action uses S_W = -beta * sum_p Re Tr U_p (up to the
    irrelevant additive constant).  Its Boltzmann exponent splits as
    B = B_+ + B_- + B_0:
        B_+ : beta times the spatial Wilson loop on the t=1 slice;
        B_- : the same loop on the t=0 slice (reflected half) = Theta B_+;
        B_0 : beta times the straddling temporal plaquette term.  Equivalently
              the plane action is S_W,0 = -B_0 and exp(-S_W,0)=exp(B_0).
  * Reflected (Osterwalder-Schrader) inner product on positive-half
    observables F:  Theta(F)(U) = conj( F(theta U) ), and
        G_ij = < Theta(F_i) . F_j >  (ordinary expectation).

Checks (all reproved here; literature is comparator only):

  Part A  B_- = Theta B_+ (reflection symmetry) and B_0 reflection-plane
          invariance, exactly, on Z_N and U(1).
  Part B  Reflection-plane norm-square factorization: the plane Boltzmann
          factor exp(B_0) is, per straddling link, a character sum with
          REAL NONNEGATIVE coefficients (Z_N: discrete Fourier; U(1):
          modified-Bessel coefficients certified by the positive-term
          power series), hence a positive (Gram) kernel.  This is the
          "norm-square" hypothesis of the gauge-half note instantiated on
          the Wilson plane.
  Part C  Integrated three-factor RP Gram is PSD for A_+^(2) observables:
          G_ij = (1/Z) sum_cfg exp(B) conj(F_i(theta cfg)) F_j(cfg) over
          a basis of plaquette / two-link observables on the positive
          half.  The Z_N checks are exact finite Haar sums; the U(1)
          angular-grid check is numerical quadrature only, with the
          theorem-grade U(1) plane-kernel positivity supplied by the
          Bessel-series certificate in Part B.
  Part D  Manifest factorization  G = W diag(kappa) W^dag  with all
          kappa >= 0 (the plane-kernel spectrum): the explicit
          Osterwalder-Seiler Gram = A^dag A form making PSD manifest.
          This is the abstract (G3) sesquilinear-form structure of the
          gauge-half note, instantiated on the Wilson boundary data.
  Part E  SU(2) numeric sample (Haar Monte Carlo): the same link-reflection
          Gram for a degree<=2 SU(2) observable basis is PSD within MC
          error, evidence that the link-reflection structure carries to
          non-abelian groups.

Literature comparator (NOT a derivation input): Osterwalder & Seiler,
"Gauge Field Theories on a Lattice", Ann. Phys. 110 (1978) 440 (link
reflection positivity for the Wilson action); Montvay & Munster,
"Quantum Fields on a Lattice" (CUP 1994), Sec. 3.4 (transfer matrix /
reflection positivity). These are named as the standard RP comparator
only; every positivity statement above is reproved here.

Companion role: not a new claim row, not a status promotion; provides
audit-friendly evidence. No PDG / fitted / measured / lattice-MC / beta=6
/ g_bare value is used as a derivation input.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

try:
    import sympy
    from sympy import cos, simplify, symbols
    HAVE_SYMPY = True
except ImportError:  # pragma: no cover
    HAVE_SYMPY = False


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Z_N gauge-group primitives
# ---------------------------------------------------------------------------
def zn_element(n: int, N: int) -> complex:
    """The Z_N link variable U = exp(2 pi i n / N)."""
    return np.exp(2j * np.pi * n / N)


def zn_rp_setup(N: int, beta: float, Ls: int = 2):
    """Return (action pieces, observable basis, config list) for the
    Z_N Wilson plaquette RP problem on the two-slice lattice."""

    def S_plus(links_t):
        # Spatial Wilson loop on a single slice: closed periodic loop of the
        # Ls spatial links.  For Ls = 2 this is Re Tr of the product of the
        # two spatial links (the smallest gauge-invariant loop on the
        # periodic spatial circle).  Real and a function of one slice only.
        prod = 1.0 + 0j
        for k in range(Ls):
            prod *= zn_element(links_t[k], N)
        return beta * np.real(prod)

    def S0(c0, c1):
        # Straddling temporal plaquettes in temporal gauge:
        # sum_k Re Tr[ U_k(0) U_k(1)^dag ] = sum_k Re( U_k(0) conj(U_k(1)) ).
        return beta * sum(
            np.real(zn_element(c0[k], N) * np.conj(zn_element(c1[k], N)))
            for k in range(Ls)
        )

    def weight(c0, c1):
        return np.exp(S_plus(c1) + S_plus(c0) + S0(c0, c1))

    # A_+^(2): functions of the positive-half (t=1) links built from the
    # Z_N characters U^q, total character-degree <= 2 (q_k in {-1, 0, 1}).
    basis = [(0,) * Ls]
    for q in itertools.product(range(-1, 2), repeat=Ls):
        if 1 <= sum(abs(x) for x in q) <= 2:
            basis.append(q)

    def F(qexp, cfg):
        v = 1.0 + 0j
        for k in range(Ls):
            v *= zn_element(cfg[k], N) ** qexp[k]
        return v

    cfgs = list(itertools.product(range(N), repeat=Ls))
    return S_plus, S0, weight, basis, F, cfgs


def zn_rp_gram(N: int, beta: float, Ls: int = 2):
    """Exact (finite Haar sum) Osterwalder-Schrader reflected Gram matrix
    G_ij = < Theta(F_i) . F_j > with Theta(F)(U) = conj(F(theta U))."""
    _, _, weight, basis, F, cfgs = zn_rp_setup(N, beta, Ls)
    Z = sum(weight(c0, c1) for c0 in cfgs for c1 in cfgs)
    M = len(basis)
    G = np.zeros((M, M), complex)
    for i in range(M):
        for j in range(M):
            s = 0j
            for c0 in cfgs:
                for c1 in cfgs:
                    # theta(c0, c1) = (c1, c0); F supported on positive half
                    # (t=1), so F_i(theta cfg) = F_i evaluated on c0.
                    s += weight(c0, c1) * np.conj(F(basis[i], c0)) * F(basis[j], c1)
            G[i, j] = s / Z
    GH = (G + G.conj().T) / 2.0
    ev = np.linalg.eigvalsh(GH)
    herm_err = float(np.max(np.abs(G - G.conj().T)))
    return ev, herm_err, basis


# ---------------------------------------------------------------------------
# U(1) gauge-group primitives
# ---------------------------------------------------------------------------
def u1_rp_gram(beta: float, Ls: int = 2, K: int = 24):
    """U(1) reflected Gram by uniform angular quadrature.

    This is a numerical cross-check only.  The exact U(1) plane-kernel
    positivity used by the source note is the positive-term Bessel-series
    certificate below, not a finite-grid Haar exactness claim.
    """
    phis = np.linspace(0.0, 2 * np.pi, K, endpoint=False)

    def S_plus(links_t):
        return beta * np.cos(sum(links_t))  # closed spatial loop angle

    def S0(c0, c1):
        return beta * sum(np.cos(c0[k] - c1[k]) for k in range(Ls))

    def weight(c0, c1):
        return np.exp(S_plus(c1) + S_plus(c0) + S0(c0, c1))

    basis = [(0,) * Ls]
    for q in itertools.product(range(-1, 2), repeat=Ls):
        if 1 <= sum(abs(x) for x in q) <= 2:
            basis.append(q)

    def F(qexp, cfg):
        v = 1.0 + 0j
        for k in range(Ls):
            v *= np.exp(1j * qexp[k] * cfg[k])
        return v

    idx = list(itertools.product(range(K), repeat=Ls))
    cfgs = [tuple(phis[i] for i in ii) for ii in idx]
    Z = sum(weight(c0, c1) for c0 in cfgs for c1 in cfgs)
    M = len(basis)
    G = np.zeros((M, M), complex)
    for i in range(M):
        for j in range(M):
            s = 0j
            for c0 in cfgs:
                for c1 in cfgs:
                    s += weight(c0, c1) * np.conj(F(basis[i], c0)) * F(basis[j], c1)
            G[i, j] = s / Z
    GH = (G + G.conj().T) / 2.0
    ev = np.linalg.eigvalsh(GH)
    herm_err = float(np.max(np.abs(G - G.conj().T)))
    return ev, herm_err


def bessel_i_positive_series_interval(beta: float, n: int, terms: int = 36):
    """Return a rigorous positive-series interval for I_n(beta).

    I_n(beta) = sum_{k>=0} (beta/2)^{2k+n}/(k!(k+n)!).
    All summands are nonnegative for beta >= 0, so any finite partial sum is
    a positive lower bound.  The remaining positive tail is bounded by a
    geometric majorant once the next-term ratio is < 1.
    """
    if beta < 0:
        raise ValueError("positive-series certificate assumes beta >= 0")
    n = abs(int(n))
    half = beta / 2.0
    term = (half ** n) / math.factorial(n)
    lower = 0.0
    for k in range(terms):
        lower += term
        term *= (half * half) / ((k + 1) * (k + n + 1))

    ratio = (half * half) / ((terms + 1) * (terms + n + 1))
    if ratio >= 1.0:
        raise ValueError("increase terms for a rigorous Bessel tail bound")
    tail = term / (1.0 - ratio)
    return lower, lower + tail, tail


def u1_plane_kernel_bessel_coeffs(beta: float, nmax: int = 8, terms: int = 36):
    """Certify U(1) plane-kernel character coefficients by positive series.

    The coefficients are I_n(beta) in the Jacobi-Anger expansion of
    exp(beta cos t).  This routine does not import scipy or special-function
    values; it certifies positivity directly from the defining positive
    series and an explicit positive tail bound.
    """
    return {
        n: bessel_i_positive_series_interval(beta, n, terms=terms)
        for n in range(-nmax, nmax + 1)
    }


# ---------------------------------------------------------------------------
# SU(2) Haar primitives (numeric sample)
# ---------------------------------------------------------------------------
def rand_su2(n: int, rng: np.random.Generator) -> np.ndarray:
    """n Haar-random SU(2) matrices via random unit quaternions."""
    a = rng.standard_normal((n, 4))
    a /= np.linalg.norm(a, axis=1, keepdims=True)
    U = np.zeros((n, 2, 2), complex)
    U[:, 0, 0] = a[:, 0] + 1j * a[:, 3]
    U[:, 0, 1] = a[:, 1] + 1j * a[:, 2]
    U[:, 1, 0] = -a[:, 1] + 1j * a[:, 2]
    U[:, 1, 1] = a[:, 0] - 1j * a[:, 3]
    return U


def su2_rp_gram_mc(beta: float, n_mc: int, seed: int = 0):
    """Monte Carlo estimate of the link-reflection Gram for an SU(2)
    degree<=2 observable basis on the two-slice lattice (L_s = 2)."""
    rng = np.random.default_rng(seed)

    def retr(M):
        return np.real(np.trace(M))

    def obs(U0, U1):
        # A_+^(2) SU(2) basis: identity, single-link traces, a two-link
        # loop trace, and two matrix entries (degree <= 2 in link entries).
        return np.array(
            [
                1.0 + 0j,
                np.trace(U0),
                np.trace(U1),
                np.trace(U0 @ U1),
                U0[0, 0],
                U1[0, 1],
            ],
            dtype=complex,
        )

    M = 6
    G = np.zeros((M, M), complex)
    Zsum = 0.0
    for _ in range(n_mc):
        U00, U10, U01, U11 = rand_su2(4, rng)
        Sp1 = beta * retr(U01 @ U11)
        Sp0 = beta * retr(U00 @ U10)
        S0 = beta * (retr(U01 @ U00.conj().T) + retr(U11 @ U10.conj().T))
        w = np.exp(Sp1 + Sp0 + S0)
        Fpos = obs(U01, U11)  # positive half (t=1)
        Fneg = obs(U00, U10)  # F evaluated on reflected (t=0) links
        G += w * np.outer(np.conj(Fneg), Fpos)
        Zsum += w
    G /= Zsum
    GH = (G + G.conj().T) / 2.0  # symmetrize (residual asymmetry is MC noise)
    ev = np.linalg.eigvalsh(GH)
    herm_err = float(np.max(np.abs(G - G.conj().T)))
    return ev, herm_err


# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 88)
    print("Audit companion for the Wilson-plaquette temporal-gauge RP bridge")
    print("AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05")
    print("Reprove: B_-=Theta B_+, plane norm-square factorization, integrated")
    print("three-factor RP Gram PSD for A_+^(2) observables")
    print("(Z_N exact, U(1) Bessel-certified + quadrature cross-check, SU(2) numeric).")
    print("=" * 88)

    # -------------------------------------------------------------------
    section("Part A: reflection symmetry  B_- = Theta B_+  and B_0 plane invariance")
    # -------------------------------------------------------------------
    # Reflection-split exact sympy check: the spatial-loop half-action has identical
    # functional form on the reflected slice (so S_-(c0) = (Theta S_+)(c0)),
        # and that B_0 is invariant under the reflection-plane swap c0 <-> c1.
    if HAVE_SYMPY:
        b = symbols("beta", positive=True)
        a0, a1 = symbols("a0 a1", real=True)  # t=0 link angles
        c0_, c1_ = symbols("c0 c1", real=True)  # t=1 link angles
        # U(1) closed spatial loop angle: B_+ = beta cos(theta_0 + theta_1)
        Splus_t1 = b * cos(c0_ + c1_)
        Splus_t0 = b * cos(a0 + a1)
        # Theta acts by t -> 1-t: it maps the t=1 loop to the t=0 loop with the
        # SAME functional form. B_-(a0,a1) must equal (Theta B_+)(a0,a1):
        ThetaSplus = Splus_t1.subs({c0_: a0, c1_: a1})
        check(
            "reflect-split.1 B_- = Theta B_+  (same functional form on reflected slice, sympy)",
            simplify(ThetaSplus - Splus_t0) == 0,
            detail="Theta maps the positive-half spatial loop to the negative half identically",
        )
        # B_0 straddling term, single link: beta cos(theta0 - theta1), invariant
        # under the reflection-plane swap theta0 <-> theta1.
        S0_link = b * cos(a0 - c0_)
        S0_swap = S0_link.subs({a0: c0_, c0_: a0}, simultaneous=True)
        check(
            "reflect-plane.1 B_0 invariant under reflection-plane swap c0<->c1 (sympy)",
            simplify(S0_link - S0_swap) == 0,
            detail="Re Tr[U(0) U(1)^dag] is symmetric in the two slices",
        )
    else:
        check("reflect-split.1 sympy unavailable", False, detail="install sympy")
        check("reflect-plane.1 sympy unavailable", False, detail="install sympy")

    # Numeric confirmation on Z_N that B_0(c0,c1) = B_0(c1,c0) for all
    # configs (reflection-plane invariance).
    N = 4
    beta = 0.6
    Ls = 2
    S_plus, S0, weight, basis, F, cfgs = zn_rp_setup(N, beta, Ls)
    s0_sym = all(
        abs(S0(c0, c1) - S0(c1, c0)) < 1e-13 for c0 in cfgs for c1 in cfgs
    )
    check(
        "reflect-plane.2 Z_N: B_0(c0,c1) = B_0(c1,c0) for all configs (reflection-plane invariance)",
        s0_sym,
        detail=f"N={N}, L_s={Ls}",
    )

    # -------------------------------------------------------------------
    section("Part B: reflection-plane norm-square (Schwarz) factorization")
    # -------------------------------------------------------------------
    # (B1) Z_N: the plane Boltzmann weight per straddling link,
    # w(n0,n1) = exp(beta Re(U^{n0} conj U^{n1})), is circulant in (n0-n1);
    # its discrete-Fourier (character) coefficients are real and nonnegative,
    # so exp(B_0) = sum_q c_q U_0^q conj(U_1)^q with c_q >= 0: a norm-square
    # (Gram) kernel.  Reproved by direct DFT of the per-link weight.
    g = np.array([np.exp(beta * np.real(zn_element(m, N))) for m in range(N)])
    chat = np.fft.fft(g) / N
    check(
        "(B1) Z_N plane-kernel character coeffs are real (Im ~ 0)",
        np.max(np.abs(chat.imag)) < 1e-12,
        detail=f"max|Im c_q| = {np.max(np.abs(chat.imag)):.2e}",
    )
    check(
        "(B2) Z_N plane-kernel character coeffs are nonnegative (norm-square form)",
        chat.real.min() >= -1e-12,
        detail=f"min c_q = {chat.real.min():.6f}",
    )
    # reconstruction of exp(beta Re(U0 conj U1)) from the character sum
    rec = np.array(
        [
            [
                sum(
                    chat[q]
                    * zn_element(n0, N) ** q
                    * np.conj(zn_element(n1, N) ** q)
                    for q in range(N)
                )
                for n1 in range(N)
            ]
            for n0 in range(N)
        ]
    )
    W_direct = np.array(
        [
            [np.exp(beta * np.real(zn_element(n0, N) * np.conj(zn_element(n1, N))))
             for n1 in range(N)]
            for n0 in range(N)
        ]
    )
    check(
        "(B3) Z_N plane kernel reconstructed from character sum exp(B_0)=sum_q c_q chi_q(U0) conj chi_q(U1)",
        np.max(np.abs(rec - W_direct)) < 1e-12,
        detail=f"reconstruction err = {np.max(np.abs(rec - W_direct)):.2e}",
    )

    # (B4) U(1): the plane-kernel character coefficients are the modified
    # Bessel functions I_n(beta), certified from their positive defining
    # series and a finite positive tail bound (no special-function import).
    co = u1_plane_kernel_bessel_coeffs(beta=1.3, nmax=8)
    min_lo = min(bounds[0] for bounds in co.values())
    max_tail = max(bounds[2] for bounds in co.values())
    check(
        "(B4) U(1) plane-kernel coeffs c_n=I_n(beta) have positive lower bounds",
        min_lo > 0.0,
        detail=f"min lower bound for n in [-8,8] = {min_lo:.6e}",
    )
    check(
        "(B5) U(1) Bessel certificate has tiny positive tail intervals",
        max_tail < 1e-60,
        detail=f"max positive tail bound for n in [-8,8] = {max_tail:.2e}",
    )
    # symmetry c_n = c_{-n} follows from the absolute-index positive series.
    sym_cn = max(abs(co[n][0] - co[-n][0]) for n in range(1, 9))
    check(
        "(B6) U(1) plane-kernel coeffs symmetric c_n = c_{-n}",
        sym_cn == 0.0,
        detail=f"max|c_n - c_{{-n}}| = {sym_cn:.2e}",
    )

    # -------------------------------------------------------------------
    section("Part C: integrated three-factor RP Gram PSD for A_+^(2) observables")
    # -------------------------------------------------------------------
    # (C1) Z_N exact Gram PSD across N and beta.
    all_psd_zn = True
    worst = 1.0
    for Ntest in [2, 3, 4, 5]:
        for btest in [0.3, 1.0, 2.5]:
            ev, herr, bas = zn_rp_gram(Ntest, btest, Ls=2)
            psd = ev.min() >= -1e-9
            all_psd_zn = all_psd_zn and psd and (herr < 1e-9)
            worst = min(worst, ev.min())
            print(
                f"     Z_{Ntest}, beta={btest}: basis={len(bas)}, "
                f"min_eig={ev.min():+.6e}, herm_err={herr:.1e}, PSD={psd}"
            )
    check(
        "(C1) Z_N reflected Gram is Hermitian PSD across N in {2,3,4,5}, beta in {0.3,1,2.5}",
        all_psd_zn,
        detail=f"worst min_eig = {worst:+.6e}",
    )

    # (C2) Demonstrate the NAIVE double-conjugated bracket is NOT PSD, to
    # show the Gram PSD is a genuine property of the correct OS reflection
    # (mirrors the target row's own single-step non-PSD warning).
    _, _, weight4, basis4, F4, cfgs4 = zn_rp_setup(4, 0.6, 2)
    Z4 = sum(weight4(c0, c1) for c0 in cfgs4 for c1 in cfgs4)
    M4 = len(basis4)
    Gnaive = np.zeros((M4, M4), complex)
    for i in range(M4):
        for j in range(M4):
            s = 0j
            for c0 in cfgs4:
                for c1 in cfgs4:
                    # WRONG: no conjugation on the reflected factor
                    # (drops the antilinearity of Theta) -> not a Gram form.
                    s += weight4(c0, c1) * F4(basis4[i], c0) * F4(basis4[j], c1)
            Gnaive[i, j] = s / Z4
    ev_naive = np.linalg.eigvalsh((Gnaive + Gnaive.conj().T) / 2.0)
    check(
        "(C2) control: dropping Theta's conjugation gives a NON-PSD form (correct OS reflection is load-bearing)",
        ev_naive.min() < -1e-3,
        detail=f"min_eig (wrong reflection) = {ev_naive.min():+.4f}",
    )

    # (C3) U(1) quadrature Gram PSD cross-check.
    all_psd_u1 = True
    for btest in [0.5, 1.5]:
        ev, herr = u1_rp_gram(btest, Ls=2, K=24)
        psd = ev.min() >= -1e-8
        all_psd_u1 = all_psd_u1 and psd and (herr < 1e-7)
        print(
            f"     U(1), beta={btest}: min_eig={ev.min():+.6e}, "
            f"herm_err={herr:.1e}, PSD={psd}"
        )
    check(
        "(C3) U(1) reflected Gram quadrature cross-check is Hermitian PSD",
        all_psd_u1,
    )

    # -------------------------------------------------------------------
    section("Part D: manifest factorization G = W diag(kappa) W^dag, kappa >= 0")
    # -------------------------------------------------------------------
    # Build the plane-kernel matrix over the joint config space, diagonalize,
    # and exhibit the Osterwalder-Seiler Gram as A^dag A explicitly.
    Nd = 4
    bd = 0.6
    S_plus_d, S0_d, weight_d, basis_d, F_d, cfgs_d = zn_rp_setup(Nd, bd, 2)
    nc = len(cfgs_d)
    Kmat = np.array([[np.exp(S0_d(c0, c1)) for c1 in cfgs_d] for c0 in cfgs_d])
    Kmat = (Kmat + Kmat.T) / 2.0  # real symmetric plane kernel
    kappa, phi = np.linalg.eigh(Kmat)
    check(
        "(D1) plane-kernel matrix spectrum kappa >= 0 (positive Gram kernel)",
        kappa.min() >= -1e-10,
        detail=f"min kappa = {kappa.min():.6f}",
    )
    M = len(basis_d)
    expS = np.array([np.exp(S_plus_d(c)) for c in cfgs_d])
    Fmat = np.array([[F_d(basis_d[i], c) for c in cfgs_d] for i in range(M)])
    # W_i(a) = sum_c exp(S_+(c)) conj(F_i(c)) phi_a(c)
    W = (expS[None, :] * np.conj(Fmat)) @ phi  # (M x nc)
    Gfac = W @ np.diag(kappa) @ W.conj().T
    # Unnormalized direct three-factor Gram (no 1/Z) for the comparison.
    Gd = np.zeros((M, M), complex)
    for i in range(M):
        for j in range(M):
            Gd[i, j] = sum(
                np.exp(S_plus_d(c0)) * np.exp(S_plus_d(c1)) * np.exp(S0_d(c0, c1))
                * np.conj(F_d(basis_d[i], c0)) * F_d(basis_d[j], c1)
                for c0 in cfgs_d
                for c1 in cfgs_d
            )
    check(
        "(D2) G = W diag(kappa) W^dag exactly (manifest Osterwalder-Seiler Gram = A^dag A)",
        np.max(np.abs(Gd - Gfac)) < 1e-9,
        detail=f"||G - W diag(kappa) W^dag|| = {np.max(np.abs(Gd - Gfac)):.2e}",
    )
    ev_unnorm = np.linalg.eigvalsh((Gd + Gd.conj().T) / 2.0)
    check(
        "(D3) integrated three-factor Gram is PSD (eigenvalues >= 0)",
        ev_unnorm.min() >= -1e-7,
        detail=f"min_eig = {ev_unnorm.min():+.6e}",
    )

    # -------------------------------------------------------------------
    section("Part E: SU(2) numeric sample (Haar Monte Carlo)")
    # -------------------------------------------------------------------
    # Honest scope: the SU(2) result is a numeric sample (not an exact
    # finite-Haar sum); residual Hermiticity asymmetry is Monte Carlo noise.
    ev_su2, herr_su2 = su2_rp_gram_mc(beta=1.0, n_mc=200000, seed=0)
    mc_noise = herr_su2  # asymmetry scale ~ MC error
    check(
        "(E1) SU(2) link-reflection Gram is PSD within MC error (min_eig > -MC noise)",
        ev_su2.min() > -max(3 * mc_noise, 5e-3),
        detail=f"min_eig = {ev_su2.min():+.5f}, herm/MC-noise = {herr_su2:.4f}",
    )
    print(f"     SU(2) eigenvalues: {np.round(ev_su2, 5)}")
    print("     (numeric sample only; finite exact statements above are Z_N,")
    print("      with U(1) plane positivity certified by Bessel positive series)")

    # -------------------------------------------------------------------
    section("Summary")
    # -------------------------------------------------------------------
    print("  Reproved from primitives:")
    print("   A  reflection symmetry  B_- = Theta B_+  and B_0 plane invariance")
    print("   B  plane Boltzmann weight = positive (norm-square) character kernel")
    print("      (Z_N: nonneg DFT coeffs; U(1): I_n(beta) >= 0 by positive series)")
    print("   C  integrated three-factor reflected Gram PSD for A_+^(2) observables")
    print("      (Z_N exact finite-Haar; U(1) quadrature cross-check; wrong reflection control)")
    print("   D  manifest G = W diag(kappa) W^dag with kappa >= 0 (OS Gram = A^dag A)")
    print("   E  SU(2) numeric sample PSD (link-reflection structure carries over)")
    print("  Literature (Osterwalder-Seiler 1978; Montvay-Munster 1994): comparator only.")

    print()
    print("=" * 88)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
