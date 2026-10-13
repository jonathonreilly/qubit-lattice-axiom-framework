"""Recompute F4 mixture polynomials and the positive detour-family zero."""

import ast
import json
import numpy as np


D = 0.003


def load(path):
    raw = json.load(open(path, encoding="utf-8"))
    out = {}
    for ts, row in raw.items():
        out[float(ts)] = {
            "base": row["base"],
            "Tad": {ast.literal_eval(k) if k.startswith("(") else k: v for k, v in row["Tad"].items()},
            "E": {ast.literal_eval(k): v for k, v in row["E"].items()},
        }
    return out


def rich(values):
    h1 = 2.0 * (values[D] - values[0.0]) / D**2
    h2 = 2.0 * (values[2 * D] - values[0.0]) / (2 * D) ** 2
    return (4.0 * h1 - h2) / 3.0


def mixed_hessian(raw, b, lam):
    vals = {}
    for t, row in raw.items():
        e11 = row["E"][(1, 1)]
        e1b = row["E"].get((1, b), e11)
        ebb = row["E"].get((b, b), e11)
        tad = (1.0 - lam) * row["Tad"][("M", 1)] + lam * row["Tad"].get(("M", b), row["Tad"]["J"])
        exch = (1.0 - lam) ** 2 * e11 + 2.0 * lam * (1.0 - lam) * e1b + lam**2 * ebb
        vals[t] = row["base"] + tad + exch
    return rich(vals)


def polynomial(path, b):
    raw = load(path)
    hp = mixed_hessian(raw, b, 0.0)
    plus = mixed_hessian(raw, b, 1.0)
    minus = mixed_hessian(raw, b, -1.0)
    linear = 0.5 * (plus - minus)
    quad = 0.5 * (plus + minus) - hp
    roots = np.roots([quad, linear, hp]) if abs(quad) > 1e-14 else np.array([-hp / linear])
    return hp, linear, quad, roots


def main():
    hp, lj, qj, rj = polynomial("raw_J344.json", "J")
    print("P-J344 H_P %.12e L %.12e Q %.12e roots %s" % (hp, lj, qj, rj))
    for path, b, label in (("raw_B150.json", 4, "P-S4"), ("raw_SL88.json", 32, "P-S32")):
        h, linear, quad, roots = polynomial(path, b)
        print("%s H_P %.12e L %.12e Q %.12e roots %s" % (label, h, linear, quad, roots))

    # P and J have the same mean current.  If C is Psym's path-current
    # covariance, H_P = H_J + response(C).  The genuine paths
    # Gamma_ij^(n)=(gamma_i gamma_j^-1)^n gamma_i, averaged uniformly over
    # independent i,j, retain the same mean current and have covariance
    # c_n C, c_n=(n+1)^2+n^2.
    hj = hp + lj
    cstar = hj / (hj - hp)
    c11 = 2 * 11**2 + 2 * 11 + 1
    c12 = 2 * 12**2 + 2 * 12 + 1
    theta = (cstar - c11) / (c12 - c11)
    check = hj + ((1.0 - theta) * c11 + theta * c12) * (hp - hj)
    print("detour covariance c*=%.12f, c11=%d, c12=%d, theta12=%.12f, Hmix=%.3e" % (cstar, c11, c12, theta, check))


if __name__ == "__main__":
    main()
