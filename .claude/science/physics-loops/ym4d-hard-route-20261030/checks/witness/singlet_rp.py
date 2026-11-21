#!/usr/bin/env python3
"""W4: leading term of E[Theta F F] for singlet bilinears of Gaussian potentials.

(1) Exact pairing count: for colour 3-vectors with independent colours,
    E[(x.y)(z.w)] = 9 C_xy C_zw + 3 C_xz C_yw + 3 C_xw C_yz.
(2) Toy with the kernel chosen by hand: two pairs of loop fluxes with reflected correlation +rho and -rho,
    independent between pairs, so R = diag(rho, -rho), P = 1, F = B(1,2), c offdiagonal, Tr cP = 0.
    Holonomy W_i = exp(i h x_i . sigma / 2), v_i = sin(h |x_i| / 2) xhat_i, B = v_1 . v_2.
    Leading term (h^4/16)[6 Tr(cRcR)] with c = [[0,1/2],[1/2,0]]: Tr(cRcR) = 2 (1/4) r1 r2 = -rho^2/2,
    so E[Theta F F] = -(3/16) h^4 rho^2 + O(h^6).
"""
import itertools, json, os
import numpy as np


def pairing_check():
    ok = True
    idx = [0, 1, 2]
    # enumerate colour sums of the three pairings of four vectors
    c = {"xy|zw": 0, "xz|yw": 0, "xw|yz": 0}
    for a in idx:
        for b in idx:
            # (x_a y_a)(z_b w_b)
            c["xy|zw"] += 1  # delta_aa delta_bb
            c["xz|yw"] += (a == b)  # delta_ab delta_ab
            c["xw|yz"] += (a == b)
    return c


def toy(h, rho, n, seed):
    rng = np.random.default_rng(seed)
    means = []
    for chunk in range(20):
        m = n // 20
        def pair(r):
            z1 = rng.standard_normal((m, 3))
            z2 = rng.standard_normal((m, 3))
            return z1, r * z1 + np.sqrt(1 - r * r) * z2
        x, xr = pair(rho)
        y, yr = pair(-rho)
        def v(a):
            t = np.linalg.norm(a, axis=1, keepdims=True)
            return np.sin(h * t / 2) * a / t
        F = (v(x) * v(y)).sum(1)
        Fr = (v(xr) * v(yr)).sum(1)
        means.append((F * Fr).mean())
    means = np.array(means)
    return float(means.mean()), float(means.std(ddof=1) / np.sqrt(len(means)))


def main():
    out = {"pairings": pairing_check()}
    print(out)
    rows = []
    for h in [0.6, 0.4]:
        m, se = toy(h, 0.8, 8_000_000, 7)
        lead = -(3.0 / 16.0) * h**4 * 0.8**2
        rows.append(dict(h=h, mean=m, se=se, leading=lead, zscore=m / se, ratio=m / lead))
        print(rows[-1], flush=True)
    out["toy"] = rows
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "singlet_rp.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
