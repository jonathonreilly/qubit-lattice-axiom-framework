"""Independent F4 recomputation of P, J, and S2.

This deliberately does not import scripts/f1_lib.py or scripts/f4_lib.py.  It
uses only the archived one-dimensional D1 and Gph symbols.  Vertices are built
by enumerating the six axis orders and their legs.  Diagonal seagulls are built
from the pairwise products of those leg currents:

  1/2 [D(p+e_j/M) - 2 D(p) + D(p-e_j/M)].

For a W-average the two legs come from the same path before the path average;
for J they come from two independent members of the six-path mean current.
This is a separate implementation path from f4_lib.py's closed corner sums.
"""

from itertools import permutations
import json
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "arch"))
from dirac import D1  # noqa: E402
from sublum import SymG  # noqa: E402


PI = np.pi
ROOT = (0.909103708, 0.555604226)
CPH = 2.9435
ORDERS = tuple(permutations(range(3)))


def rk4(rhs, state, steps):
    h = 1.0 / steps
    for _ in range(steps):
        k1 = rhs(state)
        k2 = rhs(tuple(y + 0.5 * h * k for y, k in zip(state, k1)))
        k3 = rhs(tuple(y + 0.5 * h * k for y, k in zip(state, k2)))
        k4 = rhs(tuple(y + h * k for y, k in zip(state, k3)))
        state = tuple(
            y + (h / 6.0) * (a + 2.0 * b + 2.0 * c + d)
            for y, a, b, c, d in zip(state, k1, k2, k3, k4)
        )
    return state


def panel_grid(order):
    """Independent composite GL grid with the narrow photon edge resolved."""
    b = ROOT[0]
    fixed = [
        0.0,
        0.0025,
        0.005,
        0.01,
        0.02,
        0.04,
        0.08,
        0.16,
        0.32,
        b,
        2.0 * b,  # S2's half-corner crosses the inner D1 box edge here.
        PI - b,
        CPH,
        PI,
    ]
    fixed.extend(CPH + i * (PI - CPH) / 6.0 for i in range(1, 6))
    fixed = sorted(set(x for x in fixed if 0.0 <= x <= PI))
    edges = [fixed[0]]
    for lo, hi in zip(fixed[:-1], fixed[1:]):
        count = max(1, int(np.ceil((hi - lo) / 0.25)))
        edges.extend(lo + (hi - lo) * k / count for k in range(1, count + 1))
    gx, gw = np.polynomial.legendre.leggauss(order)
    xs, ws = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        xs.append(0.5 * (hi - lo) * gx + 0.5 * (hi + lo))
        ws.append(0.5 * (hi - lo) * gw / PI)
    return np.concatenate(xs), np.concatenate(ws)


class Law:
    def __init__(self):
        self.fermion = D1(*ROOT)
        self.photon = SymG(CPH)
        self.mflow = 0.01

    def flow_f(self, x, y, wz, t, steps=4):
        x = np.asarray(x, dtype=float) + 0.0 * y + 0.0 * wz
        y = np.asarray(y, dtype=float) + 0.0 * x + 0.0 * wz
        if t == 0.0:
            return x, y

        def rhs(state):
            xx, yy = state
            mass = self.mflow + self.fermion.W(xx) + self.fermion.W(yy) + wz
            px = self.fermion.S(xx) * self.fermion.dS(xx) + mass * self.fermion.dW(xx)
            py = self.fermion.S(yy) * self.fermion.dS(yy) + mass * self.fermion.dW(yy)
            return 0.5 * t * px, -0.5 * t * py

        return rk4(rhs, (x, y), steps)

    def flow_g(self, q, sign, t, steps=4):
        q = np.asarray(q, dtype=float)
        if t == 0.0 or sign == 0:
            return q

        def rhs(state):
            z = state[0]
            return (0.5 * sign * t * self.photon.h(z) * self.photon.dh(z),)

        return rk4(rhs, (q,), steps)[0]

    def operator(self, kx, ky, kz, t, steps=4):
        wz = self.fermion.W(kz)
        fx, fy = self.flow_f(kx, ky, wz, t, steps)
        return (
            self.fermion.S(fx),
            self.fermion.S(fy),
            self.fermion.S(kz) + 0.0 * fx,
            self.fermion.W(fx) + self.fermion.W(fy) + wz + 0.0 * fx,
        )


def base_vector(order, axis, round_index, rounds):
    b = np.full(3, round_index / rounds, dtype=float)
    for prior in order[: order.index(axis)]:
        b[prior] += 1.0 / rounds
    return b


def integrate(order):
    law = Law()
    x, w = panel_grid(order)
    node_count = len(x)
    results = {}

    for t in (0.0, 0.003, 0.006):
        dx = law.photon.h(law.flow_g(x, +1, t))
        dy = law.photon.h(law.flow_g(x, -1, t))
        dz = law.photon.h(x)
        totals = {
            "base": 0.0,
            "tad_P": 0.0,
            "tad_J": 0.0,
            "tad_S2": 0.0,
            "ex_P": 0.0,
            "ex_S2": 0.0,
            "ex_P_S2": 0.0,
            "ward_P": 0.0,
            "ward_S2": 0.0,
        }

        # Four-point z slabs keep the peak below 1 GB while avoiding tiny-slab
        # interpolation overhead.
        for z0 in range(0, node_count, 4):
            zi = slice(z0, min(z0 + 4, node_count))
            X = x[:, None, None]
            Y = x[None, :, None]
            Z = x[zi][None, None, :]
            WGT = w[:, None, None] * w[None, :, None] * w[zi][None, None, :]
            dvec = (
                dx[:, None, None] + 0.0 * Z,
                dy[None, :, None] + 0.0 * Z,
                dz[zi][None, None, :] + 0.0 * X + 0.0 * Y,
            )
            omega = np.sqrt(sum(v * v for v in dvec))
            cache = {}

            def dop(coeff):
                # Rounded tuple keys make independently generated rational bases coincide.
                key = tuple(round(float(v), 12) for v in coeff)
                if key not in cache:
                    cache[key] = law.operator(key[0] * X, key[1] * Y, key[2] * Z, t)
                return cache[key]

            dq = dop((1.0, 1.0, 1.0))
            c, mass = dq[:3], dq[3]
            energy = np.sqrt(sum(v * v for v in c) + mass * mass)
            denominator = 2.0 * energy * omega * (energy + omega)
            totals["base"] += float(np.sum(WGT * mass / denominator))

            vertices = {}
            seagulls = {}
            for rounds, name in ((1, "P"), (2, "S2")):
                verts = []
                seas = []
                for axis in range(3):
                    e = np.zeros(3)
                    e[axis] = 1.0 / rounds
                    vacc = [0.0, 0.0, 0.0, 0.0]
                    nacc = 0.0
                    for path_order in ORDERS:
                        bases = [base_vector(path_order, axis, rr, rounds) for rr in range(rounds)]
                        for bvec in bases:
                            hi, lo = dop(bvec + e), dop(bvec)
                            for comp in range(4):
                                vacc[comp] = vacc[comp] + (hi[comp] - lo[comp]) / len(ORDERS)
                        # Both photon legs belong to this same Wilson path.
                        for left in bases:
                            for right in bases:
                                p = left - right
                                nacc = nacc + 0.5 * (
                                    dop(p + e)[3] - 2.0 * dop(p)[3] + dop(p - e)[3]
                                ) / len(ORDERS)
                    verts.append(tuple(v / dvec[axis] for v in vacc))
                    seas.append(nacc)
                vertices[name] = verts
                seagulls[name] = seas

            # J is the square of the six-path mean current, hence independent
            # path choices for its two photon legs.
            jsea = []
            for axis in range(3):
                e = np.zeros(3)
                e[axis] = 1.0
                bases = [base_vector(path_order, axis, 0, 1) for path_order in ORDERS]
                nacc = 0.0
                for left in bases:
                    for right in bases:
                        p = left - right
                        nacc = nacc + 0.5 * (
                            dop(p + e)[3] - 2.0 * dop(p)[3] + dop(p - e)[3]
                        ) / (len(ORDERS) ** 2)
                jsea.append(nacc)
            seagulls["J"] = jsea

            for name in ("P", "J", "S2"):
                totals["tad_" + name] += float(
                    np.sum(
                        WGT
                        * sum(seagulls[name][j] / (dvec[j] ** 2) for j in range(3))
                        / (2.0 * omega)
                    )
                )

            def exchange(left_name, right_name):
                value = 0.0
                left, right = vertices[left_name], vertices[right_name]
                for axis in range(3):
                    va, vb = left[axis], right[axis]
                    dot = sum(va[k] * vb[k] for k in range(3))
                    value = value + (dot - va[3] * vb[3]) * mass
                    value = value - va[3] * sum(vb[k] * c[k] for k in range(3))
                    value = value - vb[3] * sum(va[k] * c[k] for k in range(3))
                return float(np.sum(WGT * value / denominator))

            totals["ex_P"] += exchange("P", "P")
            totals["ex_S2"] += exchange("S2", "S2")
            totals["ex_P_S2"] += exchange("P", "S2")

            for name in ("P", "S2"):
                for comp in range(4):
                    residual = sum(dvec[j] * vertices[name][j][comp] for j in range(3)) - dq[comp]
                    totals["ward_" + name] = max(
                        totals["ward_" + name], float(np.max(np.abs(residual)))
                    )

        totals["dm_P"] = totals["base"] + totals["tad_P"] + totals["ex_P"]
        totals["dm_J"] = totals["base"] + totals["tad_J"] + totals["ex_P"]
        totals["dm_S2"] = totals["base"] + totals["tad_S2"] + totals["ex_S2"]
        results[t] = totals
        print("completed t=%.3f on %d nodes" % (t, node_count), file=sys.stderr, flush=True)

    def richardson(key):
        f0, f1, f2 = (results[t][key] for t in (0.0, 0.003, 0.006))
        h1 = 2.0 * (f1 - f0) / 0.003**2
        h2 = 2.0 * (f2 - f0) / 0.006**2
        return (4.0 * h1 - h2) / 3.0

    hess = {name: richardson("dm_" + name) for name in ("P", "J", "S2")}
    tad_hess = {name: richardson("tad_" + name) for name in ("P", "J", "S2")}
    out = {
        "gauss_order": order,
        "nodes": node_count,
        "dm0": {name: results[0.0]["dm_" + name] for name in ("P", "J", "S2")},
        "hessian": hess,
        "shift": {name: hess[name] - hess["P"] for name in ("J", "S2")},
        "relative_shift": {name: (hess[name] - hess["P"]) / hess["P"] for name in ("J", "S2")},
        "seagull_shift": {name: tad_hess[name] - tad_hess["P"] for name in ("J", "S2")},
        "seagull_fraction": {
            name: (tad_hess[name] - tad_hess["P"]) / (hess[name] - hess["P"])
            for name in ("J", "S2")
        },
        "ward_max": {
            name: max(results[t]["ward_" + name] for t in results) for name in ("P", "S2")
        },
    }
    return out


def main():
    all_results = [integrate(5)]
    print(json.dumps(all_results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
