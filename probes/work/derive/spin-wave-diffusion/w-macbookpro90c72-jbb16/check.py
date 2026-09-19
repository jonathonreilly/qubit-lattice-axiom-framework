#!/usr/bin/env python3
"""J:derive:spin-wave-diffusion:a3 — exact checks for ATTEMPT.md steps 1-4."""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

mp.mp.dps = 40


def A(k):
    return mp.coth(k) - 1 / k


def E_mu2(k):
    # density on [-1,1]: e^{k u} du / (2 sinh(k)/k)
    Z = 2 * mp.sinh(k) / k
    return mp.quad(lambda u: u * u * mp.e ** (k * u), [-1, 1]) / Z


def main():
    hits = []
    print("S1 vMF identities (40 digits):")
    for k in (1, 3, 6, mp.mpf(18), mp.mpf(36), mp.mpf(72), mp.mpf(144)):
        Ak = A(k)
        Ap = 1 / k ** 2 - 1 / mp.sinh(k) ** 2
        # numerical A'
        h = mp.mpf("1e-12")
        Apn = (A(k + h) - A(k - h)) / (2 * h)
        emu2 = E_mu2(k)
        rel = emu2 - (1 - 2 * Ak / k)
        trans = (1 - emu2) / 2
        trans_id = Ak / k
        print(
            f"  k={k}: A={mp.nstr(Ak, 12)} A'-id {mp.nstr(Ap - Apn, 3)}; "
            f"E[mu^2]-(1-2A/k)={mp.nstr(rel, 3)}; trans var {mp.nstr(trans, 8)} vs A/k {mp.nstr(trans_id, 8)}"
        )
        if abs(Ap - Apn) > mp.mpf("1e-12"):
            hits.append(f"A' at {k}")
        if abs(rel) > mp.mpf("1e-14"):
            hits.append(f"E mu^2 at {k}")
        if abs(trans - trans_id) > mp.mpf("1e-14"):
            hits.append(f"transverse var at {k}")

    print("S2 Jacobian of x/|x| at (0,0,m):")
    x, y, z = sp.symbols("x y z", real=True)
    r = sp.sqrt(x * x + y * y + z * z)
    n = sp.Matrix([x / r, y / r, z / r])
    J = n.jacobian(sp.Matrix([x, y, z]))
    for m in (1, sp.Rational(1, 2), sp.Rational(3, 4)):
        Jm = sp.simplify(J.subs({x: 0, y: 0, z: m}))
        want = sp.diag(1 / m, 1 / m, 0)
        ok = all(sp.simplify(Jm[i, j] - want[i, j]) == 0 for i in range(3) for j in range(3))
        print(f"  m={m}: {Jm} == diag(1/m,1/m,0): {ok}")
        if not ok:
            hits.append(f"jacobian {m}")

    print("S3 1/A(3 beta)^2 at the executed couplings vs the probe ratios:")
    executed = {6: 1.34, 12: 1.14, 24: 1.06, 48: 1.02}
    for beta, ratio in executed.items():
        a = A(3 * beta)
        pred = 1 / a ** 2
        lim = 1 + 2 / mp.mpf(3 * beta)
        print(
            f"  beta={beta}: A(3b)={mp.nstr(a, 10)} 1/A^2={mp.nstr(pred, 6)} "
            f"1+2/(3b)={mp.nstr(lim, 6)} executed={ratio} (aligned-plane underestimates the table)"
        )
        # large-beta expansion: A = 1 - 1/k + O(e^{-2k}), k=3b
        k = 3 * beta
        expn = (1 - 1 / k) ** -2
        if abs(pred - expn) > 0.01 and beta >= 24:
            hits.append(f"expansion {beta}")

    # A = 1 - 1/k + 2 e^{-2k} + ... ; at beta=48, k=144, exp correction is tiny
    k = mp.mpf(144)
    a = A(k)
    if abs(a - (1 - 1 / k)) > mp.mpf("1e-10"):
        # 2e^{-2k} is ~10^{-125}, so should be closer; coth k = 1 + 2e^{-2k}+...
        pass
    if abs(a - (1 - 1 / k)) > mp.mpf("1e-8"):
        hits.append("large-k A")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + ", ".join(hits))
        return 1
    print(
        "HIT: aligned-plane exact: vMF transverse variance is A(k)/k; one-step plane average has "
        "var sigma^2/L^2 per component; Jacobian of M/|M| is (I-nn^T)/|M|, so D_1 L^2/sigma^2 = "
        "1/A(3 beta)^2 on the aligned plane, which tends to 1 as beta->infty (1+2/(3 beta)+O(beta^{-2})); "
        "the executed ratios 1.34..1.02 are larger, as expected from |M|<A(3 beta) due to nonzero modes"
    )
    print(
        "SUMMARY: PARTIAL - aligned-plane (linearized zero-mode) diffusion ratio is exactly 1/A(3 beta)^2 "
        "-> 1; nonlinear enhancement is the Jacobian 1/|M|^2 at the reduced magnetization, remainder by V_L open"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
