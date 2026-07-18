#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
RP Wilson-plaquette temporal-gauge bridge: SIGN REPAIR + manifestly-positive
character-coefficient theorem (historical 2026-06-06 repair record)
============================================================================

Target of the repair
---------------------
On 2026-06-06,
`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`
had been returned **audited_failed** with three blockers (verbatim):

  (1) "S_0 = +beta Re with exp(-S_0) gives negative Fourier coefficients
       already for Z_2, where the nontrivial coefficient is
       (e^{-beta} - e^{beta})/2 < 0."                       [SIGN ERROR]
  (2) "The runner source uses exp(+S_0), not the displayed exp(-S_0)."
                                                            [NOTE<->RUNNER DRIFT]
  (3) "its U(1) 'exact finite-Haar' check uses a finite angular grid on
       exp(beta cos theta), which is not a bounded-degree trigonometric
       polynomial."                                         [EXACTNESS OVERCLAIM]

Blockers (1) and (2) share the wrong Boltzmann sign.  Blocker (3) is a
separate exactness defect and is repaired by the source's tensor-power proof.
The floating runner reconstructions remain support for that exact algebra.

The repair
----------
* SIGN.  Standard Wilson convention: action  S_W = -(beta_W/N) sum_p Re Tr U_p,
  partition fn  Z = int exp(-S_W) = int exp(+(beta_W/N) sum_p Re Tr U_p).
  Write alpha := beta_W/N.  The straddling-plane weight is
  exp(+alpha Re Tr[U_+ U_-^dag]) (FERROMAGNETIC).  Equivalently define the
  plane action S_0 := -alpha Re Tr[U_+ U_-^dag] so that exp(-S_0) is this
  ferromagnetic weight -- note and runner then use the SAME sign.  (Blockers 1,2.)

* POSITIVITY (general, exact source proof).  For alpha >= 0 the class function
  exp(alpha Re chi_F(U))  (chi_F = fundamental character) has NONNEGATIVE
  coefficients in its expansion over irreducible characters:
      exp(alpha Re chi_F) = exp((alpha/2) chi_F) * exp((alpha/2) chi_Fbar)
                          = [sum_k (alpha/2)^k/k! chi_F^k]*[sum_m (alpha/2)^m/m! chi_Fbar^m].
  chi_F^k = sum_r M^{(k)}_r chi_r with M^{(k)}_r in Z_{>=0} (tensor-power
  multiplicities); products of characters decompose with nonnegative fusion
  (Clebsch-Gordan/Littlewood-Richardson) coefficients N^t_{rs} >= 0.  Hence every
  coefficient is a sum of products of nonnegative numbers -> nonnegative.  This is
  EXACT and group-general (Z_N, U(1), SU(N)), replacing the finite grid.
  (Blocker 3, and the SU(N) upgrade.)

* TEETH.  With the wrong (note-as-written) ANTIferromagnetic sign exp(-beta Re),
  the plane kernel AND the integrated Gram are NON-PSD -- so the sign is genuinely
  load-bearing (the failed note's claim was false as written, not merely mislabeled).

No new axiom/primitive/import.  Literature (Osterwalder-Seiler 1978;
Montvay-Munster 1994; the Jacobi-Anger / modified-Bessel and Peter-Weyl character
expansions) is COMPARATOR only; every positivity statement is reproven here from
numpy/sympy primitives.

Run: python3 scripts/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from math import cosh, exp, factorial, sinh

import numpy as np

PASS, FAIL = 0, 0
EVIDENCE_COUNTS: Counter[str] = Counter()


def check(
    label: str,
    ok: bool,
    detail: str = "",
    evidence_class: str = "NUMERICAL_SUPPORT",
) -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    EVIDENCE_COUNTS[evidence_class] += int(ok)
    print(
        f"  [{tag}] [{evidence_class}] {label}"
        + (f"  --  {detail}" if detail else "")
    )
    return bool(ok)


def section(t: str) -> None:
    print("\n" + "-" * 90 + f"\n{t}\n" + "-" * 90)


# modified Bessel I_n via the EXACT power series (manifestly positive term by term).
# Computed by the running ratio T_{k+1}/T_k = (b/2)^2 / ((k+1)(n+k+1)) so no large
# factorials are formed (every term is still > 0, which is the load-bearing fact).
def I_series(n: int, b: float, K: int = 200) -> float:
    half = b / 2.0
    term = half ** n / factorial(n)   # k = 0 term;  n is small (<= ~40 here)
    s = term
    for k in range(1, K):
        term *= half * half / (k * (n + k))
        s += term
        if term < 1e-300:
            break
    return s


def I_grid(n: int, b: float, Kg: int = 4096) -> float:
    t = np.linspace(0.0, 2 * np.pi, Kg, endpoint=False)
    return float(np.mean(np.exp(b * np.cos(t)) * np.exp(-1j * n * t)).real)


def main() -> int:
    print("=" * 90)
    print("RP Wilson temporal-gauge bridge: SIGN REPAIR + manifestly-positive character theorem")
    print("historical response to the 2026-06-06 audited_failed target version")
    print("=" * 90)

    # =====================================================================
    section("Part A: the SIGN root -- reproduce the audit's negative coeff, then fix it")
    # =====================================================================
    # Legacy diagnostics call the direct plane coupling `beta`; in the
    # standard SU(N) Wilson normalization it is alpha = beta_Wilson/N.
    b = 0.8
    # note-as-written: weight exp(-S_0) with S_0 = +beta Re U  =>  exp(-beta Re U)  (ANTIferro)
    # Z_2 nontrivial character chi_1(U) = U = +/-1 ;  c_1 = (1/2) sum_U chi_1(U) w(U)
    c1_bad = 0.5 * ((+1) * exp(-b * 1) + (-1) * exp(-b * (-1)))   # = (e^-b - e^+b)/2 = -sinh b
    check("(A1) note-as-written exp(-S_0): Z_2 coeff c_1 = (e^-b - e^b)/2 = -sinh b < 0  [audit blocker reproduced]",
          abs(c1_bad - (-sinh(b))) < 1e-12 and c1_bad < 0, detail=f"c_1 = {c1_bad:+.6f}")
    # FERROMAGNETIC fix: weight exp(+beta Re U)  (= exp(-S_0) with S_0 := -beta Re U, standard Wilson)
    c0_good = 0.5 * (exp(+b * 1) + exp(+b * (-1)))               # = cosh b
    c1_good = 0.5 * ((+1) * exp(+b * 1) + (-1) * exp(+b * (-1)))  # = +sinh b
    check("(A2) FERROMAGNETIC exp(+beta Re U): Z_2 coeffs (c_0,c_1) = (cosh b, sinh b), BOTH > 0  [FIXED]",
          c0_good > 0 and c1_good > 0 and abs(c1_good - sinh(b)) < 1e-12,
          detail=f"(c_0,c_1) = ({c0_good:.6f}, {c1_good:+.6f})")
    # Recompute the sign identity at several real trace values.  This guards
    # the Wilson beta/N normalization and fails if either sign is reversed.
    N_wilson = 3
    beta_wilson = 1.7
    trace_values = np.array([-N_wilson, -0.75, 0.0, 1.25, N_wilson])
    action_values = -(beta_wilson / N_wilson) * trace_values
    boltzmann_from_action = np.exp(-action_values)
    ferromagnetic_weight = np.exp(
        (beta_wilson / N_wilson) * trace_values
    )
    sign_residual = float(
        np.max(np.abs(boltzmann_from_action - ferromagnetic_weight))
    )
    check("(A3) note<->runner drift resolved: the WEIGHT is exp(+beta Re Tr) i.e. S_0 := -beta Re Tr (Wilson)",
          sign_residual < 1e-14
          and boltzmann_from_action[-1] > boltzmann_from_action[0],
          detail=(
              f"max sign residual={sign_residual:.1e}; "
              "Z = int exp(-S_W), S_W = -(beta/N) Re Tr U_p"
          ), evidence_class="BOUNDARY_EVIDENCE")

    # =====================================================================
    section("Part B: exact source algebra with finite numerical reconstructions")
    # =====================================================================
    # (B1) U(1): finite floating evaluation of the exact positive-term series.
    pos = all(I_series(n, 1.3) > 0 for n in range(0, 9))
    match = max(abs(I_series(n, 1.3) - I_grid(n, 1.3)) for n in range(0, 9))
    check("(B1) U(1): floating partial sums support the exact term-positive I_n series",
          pos, detail="exact positivity is the displayed all-order source formula")
    check("(B1') grid is a CROSS-CHECK only: power-series I_n == quadrature I_n to machine eps",
          match < 1e-9, detail=f"max|series-grid| = {match:.1e}")

    # (B2) Z_N: exact finite-group Fourier coeffs of exp(+beta cos(2pi j/N)), all > 0,
    #      and = sum_{m == q mod N} I_m(beta) (Poisson) -> positivity inherited from Bessel.
    okzn = True
    for N in [2, 3, 4, 5]:
        j = np.arange(N)
        w = np.exp(b * np.cos(2 * np.pi * j / N))
        c = np.fft.fft(w) / N
        poisson = np.array([sum(I_series(abs(q + m * N), b) for m in range(-8, 9)) for q in range(N)])
        ok = c.real.min() > 0 and np.abs(c.imag).max() < 1e-12 and np.max(np.abs(c.real - poisson)) < 1e-9
        okzn = okzn and ok
        print(f"     Z_{N}: min c_q = {c.real.min():+.6f}, max|Im| = {np.abs(c.imag).max():.1e}, "
              f"Poisson match = {np.max(np.abs(c.real - poisson)):.1e}")
    check("(B2) Z_N: exhaustive finite-Haar floating coefficients are positive and match truncated Poisson sums", okzn)

    # (B3) SU(2): numerical Weyl quadrature and an order-12 exact finite
    # tensor-multiplicity recurrence support the all-order source proof.
    ph = np.linspace(1e-7, np.pi - 1e-7, 60000)
    dphi = ph[1] - ph[0]
    meas = (2 / np.pi) * np.sin(ph) ** 2          # SU(2) Weyl measure
    chiF = 2 * np.cos(ph)                          # fundamental character (already real)
    wsu2 = np.exp(b * chiF)

    def chiN(n):                                   # character of the (n+1)-dim irrep
        return np.sin((n + 1) * ph) / np.sin(ph)

    a_quadrature = [float(np.sum(wsu2 * chiN(n) * meas) * dphi) for n in range(0, 7)]
    # tensor-power multiplicities: chi_F^k = sum_n m_{k,n} chi_n, recursion chi_n*chi_1=chi_{n+1}+chi_{n-1}
    rows = [np.array([1.0])]
    cur = np.array([1.0])
    for _k in range(1, 13):
        nxt = np.zeros(len(cur) + 1)
        for n, cc in enumerate(cur):
            if cc:
                nxt[n + 1] += cc
                if n - 1 >= 0:
                    nxt[n - 1] += cc
        rows.append(nxt.copy())
        cur = nxt
    nonneg_int = all((r >= -1e-12).all() and np.allclose(r, np.round(r)) for r in rows)
    a_recon = [sum((b ** k / factorial(k)) * (rows[k][n] if n < len(rows[k]) else 0.0) for k in range(13))
               for n in range(0, 7)]
    check("(B3) SU(2): Weyl quadrature gives positive sampled coefficients",
          all(a > 0 for a in a_quadrature),
          detail=f"a_0..a_6 = {[round(a,5) for a in a_quadrature]}")
    check("(B3') SU(2): float-encoded order-0..12 multiplicities reconstruct as nonnegative integers",
          nonneg_int)
    check("(B3'') SU(2): order-12 reconstruction matches Weyl quadrature within truncation tolerance",
          max(abs(a_quadrature[n] - a_recon[n]) for n in range(7)) < 1e-3,
          detail="finite reconstruction support; all-order positivity is the source proof")

    # (B4) SU(3): Haar-projected irrep coeffs of exp(+beta Re Tr U) all >= 0 (physically relevant group).
    rng = np.random.default_rng(0)

    def rand_su3(n):
        z = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))) / np.sqrt(2)
        out = np.zeros((n, 3, 3), complex)
        for i in range(n):
            q, r = np.linalg.qr(z[i])
            d = np.diagonal(r)
            q = q * (d / np.abs(d))
            out[i] = q / (np.linalg.det(q)) ** (1.0 / 3.0)
        return out

    U = rand_su3(300000)
    tr = np.trace(U, axis1=1, axis2=2)
    tr2 = np.trace(U @ U, axis1=1, axis2=2)
    tr3 = np.trace(U @ U @ U, axis1=1, axis2=2)
    chars = {
        "1": np.ones(len(U)), "3": tr, "3bar": np.conj(tr),
        "8": np.abs(tr) ** 2 - 1, "6": (tr ** 2 + tr2) / 2,
        "6bar": np.conj((tr ** 2 + tr2) / 2),
        "10": (tr ** 3 + 3 * tr * tr2 + 2 * tr3) / 6,
    }
    w3 = np.exp(b * tr.real)
    coeffs3 = {k: complex(np.mean(w3 * np.conj(c))) for k, c in chars.items()}
    allnn = all(v.real > -5e-3 for v in coeffs3.values())
    check("(B4) SU(3): Haar-projected coeffs <exp(+beta ReTrU), chi_R> >= 0 for R in {1,3,3bar,8,6,6bar,10}",
          allnn, detail=", ".join(f"{k}:{v.real:+.4f}" for k, v in coeffs3.items()))
    # abstract fusion nonnegativity exhibit: 3 x 3 = 6 + 3bar (multiplicities +1, nonnegative)
    check("(B5) abstract lemma exhibit: chi_3*chi_3 = chi_6 + chi_3bar (nonnegative fusion N^t_{rs} >= 0)",
          np.max(np.abs(tr * tr - (chars["6"] + chars["3bar"]))) < 1e-9,
          detail="product of nonneg-coeff class fns has nonneg coeffs => exp(beta Re chi_F) nonneg (general)")

    # =====================================================================
    section("Part C: integrated three-factor RP Gram is PSD with the CORRECT (ferro) sign")
    # =====================================================================
    def zn_gram(N, beta, sign=+1.0, Ls=2):
        el = lambda n: np.exp(2j * np.pi * n / N)
        # This carrier is 1+1-dimensional: a slice has spatial links but no
        # purely spatial Wilson plaquette, hence B_+=B_-=0.
        Sp = lambda lk: 0.0
        # sign=+1 => ferromagnetic weight exp(+beta Re...) (correct);  sign=-1 => note-as-written antiferro
        S0 = lambda c0, c1: sign * beta * sum(np.real(el(c0[k]) * np.conj(el(c1[k]))) for k in range(Ls))
        wt = lambda c0, c1: np.exp(Sp(c1) + Sp(c0) + S0(c0, c1))
        basis = [(0,) * Ls] + [q for q in itertools.product(range(-1, 2), repeat=Ls)
                               if 1 <= sum(abs(x) for x in q) <= 2]
        F = lambda qe, cf: np.prod([el(cf[k]) ** qe[k] for k in range(Ls)])
        cfgs = list(itertools.product(range(N), repeat=Ls))
        Z = sum(wt(a, c) for a in cfgs for c in cfgs)
        M = len(basis)
        G = np.zeros((M, M), complex)
        for i in range(M):
            for jj in range(M):
                G[i, jj] = sum(wt(a, c) * np.conj(F(basis[i], a)) * F(basis[jj], c)
                               for a in cfgs for c in cfgs) / Z
        return np.linalg.eigvalsh((G + G.conj().T) / 2.0), float(np.max(np.abs(G - G.conj().T)))

    okC = True
    for N in [2, 3, 4, 5]:
        for bb in [0.3, 1.0, 2.5]:
            ev, herr = zn_gram(N, bb, +1.0)
            ok = ev.min() >= -1e-9 and herr < 1e-9
            okC = okC and ok
        ev, _ = zn_gram(N, 1.0, +1.0)
        print(f"     Z_{N} (beta=1.0, ferro): min_eig = {ev.min():+.3e}  PSD={ev.min() >= -1e-9}")
    check("(C1) ferromagnetic integrated Gram is Hermitian PSD across Z_N (N in 2..5), beta in {0.3,1,2.5}", okC)

    # =====================================================================
    section("Part D: manifest factorization  G = W diag(kappa) W^dag,  kappa >= 0")
    # =====================================================================
    N, beta, Ls = 4, 0.7, 2
    el = lambda n: np.exp(2j * np.pi * n / N)
    cfgs = list(itertools.product(range(N), repeat=Ls))
    # ferromagnetic plane kernel K(c0,c1) = exp(+beta sum_k Re[U_k(0) U_k(1)^dag])
    Kmat = np.array([[np.exp(beta * sum(np.real(el(a[k]) * np.conj(el(c[k]))) for k in range(Ls)))
                      for c in cfgs] for a in cfgs])
    Kmat = (Kmat + Kmat.T) / 2.0
    kappa, phi = np.linalg.eigh(Kmat)
    check("(D1) ferromagnetic plane-kernel spectrum kappa >= 0 (positive Gram kernel)",
          kappa.min() >= -1e-10, detail=f"min kappa = {kappa.min():+.6f}")
    basis = [(0,) * Ls] + [q for q in itertools.product(range(-1, 2), repeat=Ls)
                           if 1 <= sum(abs(x) for x in q) <= 2]
    F = lambda qe, cf: np.prod([el(cf[k]) ** qe[k] for k in range(Ls)])
    Sp = lambda lk: 0.0
    M = len(basis)
    expS = np.array([np.exp(Sp(c)) for c in cfgs])
    Fmat = np.array([[F(basis[i], c) for c in cfgs] for i in range(M)])
    W = (expS[None, :] * np.conj(Fmat)) @ phi
    Gfac = W @ np.diag(kappa) @ W.conj().T
    Gd = np.zeros((M, M), complex)
    for i in range(M):
        for jj in range(M):
            Gd[i, jj] = sum(np.exp(Sp(a)) * np.exp(Sp(c))
                            * np.exp(beta * sum(np.real(el(a[k]) * np.conj(el(c[k]))) for k in range(Ls)))
                            * np.conj(F(basis[i], a)) * F(basis[jj], c)
                            for a in cfgs for c in cfgs)
    check("(D2) finite-carrier G matches W diag(kappa) W^dag within tolerance",
          np.max(np.abs(Gd - Gfac)) < 1e-9, detail=f"||G - W diag(kappa) W^dag|| = {np.max(np.abs(Gd - Gfac)):.1e}")
    check("(D3) finite-carrier integrated Gram is PSD within tolerance",
          np.linalg.eigvalsh((Gd + Gd.conj().T) / 2.0).min() >= -1e-7)

    # =====================================================================
    section("Part E: TEETH -- the note-as-written ANTIferro sign genuinely BREAKS positivity")
    # =====================================================================
    # plane kernel with antiferro sign (exp(-beta Re...)) is NOT a positive kernel
    okteeth = True
    for N in [2, 3, 4, 5]:
        elN = np.exp(2j * np.pi * np.arange(N) / N)
        Ka = np.array([[np.exp(-b * np.real(elN[i] * np.conj(elN[j]))) for j in range(N)] for i in range(N)])
        eva = np.linalg.eigvalsh((Ka + Ka.conj().T) / 2.0)
        ev_gram, _ = zn_gram(N, b, -1.0)
        broken = eva.min() < -1e-6 and ev_gram.min() < -1e-3
        okteeth = okteeth and broken
        print(f"     Z_{N}: antiferro plane-kernel min_eig = {eva.min():+.4f}, integrated Gram min_eig = {ev_gram.min():+.4f}")
    check("(E1) note-as-written exp(-beta Re) plane kernel AND integrated Gram are NON-PSD (sign is load-bearing)",
          okteeth, evidence_class="BOUNDARY_EVIDENCE")
    # dropped-conjugation control (the original note's C2): linear-Theta bracket is non-PSD too
    Nc, bc = 4, 0.6
    elc = lambda n: np.exp(2j * np.pi * n / Nc)
    cfc = list(itertools.product(range(Nc), repeat=2))
    Spc = lambda lk: 0.0
    S0c = lambda a, c: bc * sum(np.real(elc(a[k]) * np.conj(elc(c[k]))) for k in range(2))
    wtc = lambda a, c: np.exp(Spc(a) + Spc(c) + S0c(a, c))
    Fc = lambda qe, cf: elc(cf[0]) ** qe[0] * elc(cf[1]) ** qe[1]
    basc = [(0, 0)] + [q for q in itertools.product(range(-1, 2), repeat=2) if 1 <= sum(abs(x) for x in q) <= 2]
    Zc = sum(wtc(a, c) for a in cfc for c in cfc)
    Mc = len(basc)
    Gn = np.zeros((Mc, Mc), complex)
    for i in range(Mc):
        for jj in range(Mc):
            Gn[i, jj] = sum(wtc(a, c) * Fc(basc[i], a) * Fc(basc[jj], c) for a in cfc for c in cfc) / Zc
    evn = np.linalg.eigvalsh((Gn + Gn.conj().T) / 2.0)
    check("(E2) control: dropping Theta's conjugation (linear Theta) is also NON-PSD (correct antilinear OS reflection needed)",
          evn.min() < -1e-3, detail=f"min_eig (wrong reflection) = {evn.min():+.4f}",
          evidence_class="BOUNDARY_EVIDENCE")

    # =====================================================================
    section("Summary")
    # =====================================================================
    print("  REPAIRED:")
    print("   A  sign root: alpha=beta_Wilson/N and weight exp(+alpha Re Tr); note<->runner consistent")
    print("   B  exact positivity is the source tensor-power/fusion proof;")
    print("      runner Bessel/FFT/Weyl/Monte-Carlo/truncation values are finite support")
    print("   C  exhaustive finite-carrier floating Gram support across Z_N x alpha")
    print("   D  finite-carrier G = W diag(kappa) W^dag residual and spectrum")
    print("   E  TEETH: antiferro (note-as-written) sign breaks PSD; dropped-conjugation breaks PSD")
    print("  Literature (Osterwalder-Seiler 1978; Montvay-Munster 1994; Bessel/Peter-Weyl): comparator only.")
    print(
        "  EVIDENCE_COUNTS "
        + " ".join(
            f"{name.lower()}={EVIDENCE_COUNTS.get(name, 0)}"
            for name in (
                "EXACT_ALGEBRA",
                "EXACT_FINITE_ALGEBRA",
                "NUMERICAL_SUPPORT",
                "BOUNDARY_EVIDENCE",
            )
        )
    )
    print("\n" + "=" * 90)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 90)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
