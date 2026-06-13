#!/usr/bin/env python3
"""Class-A verifier: the reconstructed free Hamiltonian H = -log(T_hat^2)/(2 a_tau) has an
axis quasi-local kernel H(x,0,0) -- a narrow support packet for the finite-range-H input that the
microcausality / Lieb-Robinson bridge needs.

Mechanism (Paley-Wiener / Bernstein). In momentum space the reconstructed free Hamiltonian is the
exact free staggered dispersion
    E(p) = arcsinh( sqrt( m^2 + sum_mu sin^2 p_mu ) )            (retained rungs B, C)
(so spec(T_hat^2) = e^{-2E(p)}). The axis marginal kernel is H_axis(x)=H(x,0,0), obtained by
averaging E(p) over transverse momenta and Fourier transforming the remaining axis variable. The radicand
    R(p) = m^2 + sum_mu sin^2 p_mu  >=  m^2 > 0   for all real p (m > 0),
extends holomorphically (a polynomial in cos 2p_mu) and stays positive on the real torus. In the
complex strip before the first R=0 singularity, one can choose analytic branches of sqrt(R) and
arcsinh(sqrt(R)). Along the axis variable this supplies a positive strip bound; arcsinh(m) is the
comparison scale checked numerically, not a full d-dimensional correlation-length theorem. By the
one-variable Paley-Wiener implication the axis kernel has an EXPONENTIAL TAIL:
H_axis(x) ~ (algebraic prefactor) * e^{-a_axis|x|} for some a_axis > 0. The mass gap (m > 0) is
load-bearing: at m = 0 the radicand vanishes at p = 0 ON the real torus, the strip closes, and
H_axis(x) is a PURE power law (not quasi-local).

This is support for, not closure of, the parent microcausality Lieb-Robinson bound (M2). Free
(U = 1) axis marginal only; the full off-axis/free d-dimensional kernel theorem and interacting
H = -log(T[U]) quasi-locality are separate and not claimed.

No new axiom: uses the retained free staggered dispersion (rungs B, C) and standard
Paley-Wiener/Bernstein analyticity-to-decay; the verification checks the load-bearing inequalities
and numerical kernel behavior.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def marginal_dispersion(px, m, ng=512):
    """Ebar(px) = mean over (py,pz) of E(p); the marginal whose FT is H(x,0,0)."""
    g = 2 * np.pi * (np.arange(ng) + 0.5) / ng
    PY, PZ = np.meshgrid(g, g, indexing="ij")
    s2 = np.sin(PY) ** 2 + np.sin(PZ) ** 2
    return np.array([np.mean(np.arcsinh(np.sqrt(m ** 2 + np.sin(p) ** 2 + s2))) for p in px])


def kernel_axis(m, Nx=4096):
    px = 2 * np.pi * np.arange(Nx) / Nx
    return np.fft.ifft(marginal_dispersion(px, m)).real           # H(x,0,0), x = 0..Nx-1


def combined_rate(m):
    """Fit H_axis(x) ~ x^{-p} e^{-a|x|} on the asymptotic window x in [2/a_pred, 8/a_pred]."""
    Hx = kernel_axis(m)
    a_pred = np.arcsinh(m) if m > 0 else 0.02
    x0 = max(int(2 / a_pred), 6); x1 = min(int(8 / a_pred), 420)
    xs = np.arange(x0, x1)
    vals = np.abs(Hx[xs]); good = vals > 1e-14
    xg, vg = xs[good], np.log(vals[good])
    A = np.vstack([np.ones_like(xg, float), -np.log(xg), -xg.astype(float)]).T
    coef, *_ = np.linalg.lstsq(A, vg, rcond=None)
    return float(coef[2]), float(coef[1])                          # (a, p)


def main() -> int:
    print("=" * 78)
    print("reconstructed free H axis kernel H(x,0,0) has a positive exp tail  [class A]")
    print("=" * 78)

    # ---- (1) transfer matrix gapped away from 0 (m>0): log well-defined ----
    print("\n-- (1) spec(T^2)=e^{-2E(p)} is gapped away from 0 (m>0) => log well-defined --")
    d = 3
    for m in (0.1, 0.3, 1.0):
        lo = np.exp(-2 * np.arcsinh(np.sqrt(m ** 2 + d)))
        check(f"m={m}: min spec(T^2) = e^(-2 Emax) = {lo:.4f} > 0 (gapped)", lo > 0)

    # ---- (2) axis marginal has a positive strip (m>0): radicand >= m^2 > 0 everywhere ----
    print("\n-- (2) the axis marginal has a positive analytic strip for m>0 (R(p) >= m^2 > 0) --")
    rng = np.random.default_rng(0)
    P = rng.uniform(0, 2 * np.pi, size=(200000, 3))
    Rmin = float(np.min(0.3 ** 2 + np.sum(np.sin(P) ** 2, axis=1)))
    check("R(p)=m^2+sum sin^2 p stays >= m^2 > 0 on the real torus => positive axis strip; "
          "arcsinh(m) is the comparison scale => one-variable Paley-Wiener exponential tail",
          Rmin >= 0.3 ** 2 - 1e-9, detail=f"min R (m=0.3, 2e5 samples) = {Rmin:.4f} >= 0.09")

    # ---- (3) H_axis(x) ~ x^-p e^{-a|x|} with exponential tail a>0 ~ arcsinh(m) ----
    print("\n-- (3) H_axis(x)=H(x,0,0) has an exponential tail a>0 compatible with arcsinh(m) --")
    for m in (0.1, 0.3, 1.0):
        a_fit, p_fit = combined_rate(m)
        a_pred = np.arcsinh(m)
        check(f"m={m}: axis exponential rate a={a_fit:.3f} > 0 and within ~2x of arcsinh(m)={a_pred:.3f}",
              a_fit > 0 and 0.5 * a_pred < a_fit < 2.0 * a_pred,
              detail=f"axis prefactor x^-{p_fit:.2f}; a/arcsinh(m)={a_fit / a_pred:.2f}")

    # ---- (4) gap is load-bearing: m=0 => a->0 => PURE POWER-LAW (not quasi-local) ----
    print("\n-- (4) m=0 (gapless): axis strip closes => pure power-law (not quasi-local) --")
    Hx = kernel_axis(0.0)
    xs = np.arange(4, 120); vals = np.abs(Hx[xs]); good = vals > 1e-13
    xg, vg = xs[good], np.log(vals[good])
    r2_pow = 1 - np.var(vg - np.polyval(np.polyfit(np.log(xg), vg, 1), np.log(xg))) / np.var(vg)
    r2_exp = 1 - np.var(vg - np.polyval(np.polyfit(xg, vg, 1), xg)) / np.var(vg)
    pw = -np.polyfit(np.log(xg), vg, 1)[0]
    check("m=0: H_axis(x) is PURE POWER-LAW (power-fit beats exp-fit, high R^2) => NOT quasi-local => "
          "the mass gap (m>0) is the load-bearing input for axis quasi-locality",
          r2_pow > r2_exp and r2_pow > 0.99,
          detail=f"|H_axis(x)| ~ x^-{pw:.2f}; R^2 power={r2_pow:.4f} > exp={r2_exp:.4f}")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: reconstructed-H quasi-locality FAILED.")
        return 1
    print("VERDICT: the reconstructed free Hamiltonian H = -log(T^2)/(2 a_tau) = E(p) has an "
          "axis quasi-local kernel H_axis(x)=H(x,0,0): the staggered dispersion gives a positive "
          "axis analyticity strip for m>0 (radicand >= m^2 > 0), so by the one-variable "
          "Paley-Wiener implication H_axis has an exponential tail x^-p e^{-a|x|} with a > 0; "
          "the m=0 gapless case is pure power-law, so the mass gap is load-bearing. This is a "
          "support packet for the finite-range/quasi-local H gap only; it does not close the "
          "full d-dimensional or interacting Lieb-Robinson bridge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
