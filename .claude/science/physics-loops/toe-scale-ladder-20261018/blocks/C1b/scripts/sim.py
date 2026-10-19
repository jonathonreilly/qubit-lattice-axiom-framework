"""Replica container, measurements and parallel tempering driver for ctqmc."""
import numpy as np
import time, json, os
from ctqmc import Lat, sweep, ibar, states_at, check_config, nb_seed, cube_tables, cube_moves


class Replica:
    def __init__(self, lat, s0):
        self.s0 = s0.astype(np.int64).copy()
        self.ft = np.zeros(16)
        self.fp = np.zeros(16, dtype=np.int64)
        self.nF = 0
        self.Ib = None


def scramble(lat, s0, nloop, rng_seed):
    """random ice loops at beta=0 (classical) to randomise the start, using the same code (beta tiny)."""
    r = Replica(lat, s0)
    A = lat.arrays()
    for _ in range(nloop):
        r.ft, r.fp, r.nF, st, _, _m1, _m2, _m3 = sweep(r.s0, r.ft, r.fp, r.nF, 1e-9, 1.0, 0.0, A[0], A[2], A[3], A[4],
                                         A[5], A[6], 20, 0.5)
    return r.s0


def rot_state(lat, s):
    L = lat.L
    out = np.zeros_like(s)
    for v in range(lat.nv):
        c = lat.coords[v]
        for a in range(3):
            cc = np.array([c[2], c[0], c[1]])
            out[3 * (((cc[0] % L) * L + cc[1] % L) * L + cc[2] % L) + (a + 1) % 3] = s[3 * v + a]
    assert np.all(lat.div(out) == 0)
    return out


def reverse_xline(lat, s):
    """reverse a directed straight x-line (y=z=0 if directed, else search) -> changes W_x by +-1"""
    L = lat.L
    for y in range(L):
        for z in range(L):
            ls = [3 * ((x * L + y) * L + z) + 0 for x in range(L)]
            if abs(s[ls].sum()) == L:
                t = s.copy()
                t[ls] *= -1
                assert np.all(lat.div(t) == 0)
                return t
    raise RuntimeError("no directed x-line")


class Meas:
    def __init__(self, lat, nslice=4):
        self.lat = lat
        self.us = (np.arange(nslice) + 0.5) / nslice
        L = lat.L
        self.qs = []
        # q1 = 2pi/L e_b, q2 = 4pi/L e_b (if distinct from q1 mod 2pi and not 0)
        for m in (1, 2):
            if m % L == 0:
                continue
            self.qs.append(m)
        self.ph = {}
        for m in self.qs:
            self.ph[m] = np.exp(1j * 2 * np.pi * m / L * lat.lpos)  # (nl,3)
        self.dirs = [lat.ldir == a for a in range(3)]

    def __call__(self, r, beta, V):
        lat = self.lat
        out = {}
        out["nF"] = r.nF
        Ib = ibar(r.s0, r.ft, r.fp, r.nF, lat.plinks)
        out["Ib"] = Ib
        out["E"] = -r.nF / beta + V * Ib
        w = lat.winding(r.s0)
        out["Wx"], out["Wy"], out["Wz"] = (int(x) for x in w)
        sts = states_at(r.s0, r.ft, r.fp, r.nF, lat.plinks, self.us)
        circ = (sts[:, lat.plinks] * lat.psign).sum(axis=2)
        out["Nc"] = float((np.abs(circ) == 4).sum(axis=1).mean())
        for m in self.qs:
            ph = self.ph[m]
            acc = 0.0
            for b in range(3):
                for a in range(3):
                    sel = self.dirs[a]
                    Ea = (sts[:, sel] * 0.5) @ ph[sel, b]
                    acc += (np.abs(Ea) ** 2).mean()
            out[f"S{m}"] = acc / (3 * lat.nv)
        return out


class PT:
    def __init__(self, L, betas, V=0.0, seed=1, start="canonical", nloops=None, giant_frac=0.5):
        self.lat = Lat(L)
        self.A = self.lat.arrays()
        self.betas = np.array(betas, dtype=float)
        self.V = V
        nb_seed(seed)
        self.rng = np.random.default_rng(seed + 12345)
        s = self.lat.canonical()
        if start == "scrambled":
            s = scramble(self.lat, s, 200, seed)
        if start.startswith("mixW"):
            # alternate replicas between W=0 and W=(1,0,0) starts (directed x-line y=0,z=0 reversed);
            # mixW_rot: same with the axes of the canonical state cyclically rotated (x->y->z)
            if start == "mixW_rot":
                s = rot_state(self.lat, s)
            s1 = reverse_xline(self.lat, s)
            self.reps = [Replica(self.lat, s if k % 2 == 0 else s1) for k in range(len(betas))]
        else:
            self.reps = [Replica(self.lat, s) for _ in betas]
        self.where = np.arange(len(betas))  # where[k] = replica index at beta k
        self.label = np.arange(len(betas))  # label of walker at beta k (for round trips)
        self.dirn = np.zeros(len(betas), dtype=np.int64)  # walker direction state: +1 last visited lowest beta index 0
        self.trips = 0
        self.nloops = nloops if nloops is not None else max(4, self.lat.nv // 4)
        self.giant_frac = giant_frac
        self.meas = Meas(self.lat)
        self.nsw = 0
        self.swap_acc = np.zeros(len(betas) - 1)
        self.swap_try = np.zeros(len(betas) - 1)
        self.stats = np.zeros((len(betas), 10))
        self.cf, self.cl, self.pc = cube_tables(self.lat)
        self.cube_frac = 0.5
        self.cstats = np.zeros((len(betas), 2))

    def sweep_all(self):
        A = self.A
        for k, b in enumerate(self.betas):
            r = self.reps[self.where[k]]
            r.ft, r.fp, r.nF, st, _, _m1, _m2, _m3 = sweep(r.s0, r.ft, r.fp, r.nF, b, 1.0, self.V, A[0], A[2], A[3], A[4],
                                             A[5], A[6], self.nloops, self.giant_frac)
            self.stats[k] += st
            if self.V == 0.0 and self.cube_frac > 0 and r.nF >= 3:
                a, v = cube_moves(r.s0, r.ft, r.fp, r.nF, A[0], A[2], self.cf, self.cl, self.pc,
                                  max(1, int(self.cube_frac * r.nF)))
                self.cstats[k] += (a, v)
        self.nsw += 1

    def swaps(self):
        V = self.V
        start = self.nsw % 2
        for k in range(start, len(self.betas) - 1, 2):
            i, j = self.where[k], self.where[k + 1]
            ri, rj = self.reps[i], self.reps[j]
            bi, bj = self.betas[k], self.betas[k + 1]
            lw = (ri.nF - rj.nF) * np.log(bj / bi)
            if V != 0.0:
                Ii = ibar(ri.s0, ri.ft, ri.fp, ri.nF, self.lat.plinks)
                Ij = ibar(rj.s0, rj.ft, rj.fp, rj.nF, self.lat.plinks)
                lw += -V * (bj - bi) * (Ii - Ij)
            self.swap_try[k] += 1
            if lw >= 0 or self.rng.random() < np.exp(lw):
                self.swap_acc[k] += 1
                self.where[k], self.where[k + 1] = j, i
                self.label[k], self.label[k + 1] = self.label[k + 1], self.label[k]
        # round trips: walker touching the lowest beta (index 0) then the highest
        K = len(self.betas) - 1
        for k in (0, K):
            lab = self.label[k]
            if k == 0:
                self.dirn[lab] = 1
            elif self.dirn[lab] == 1:
                self.dirn[lab] = 2
                self.trips += 1

    def measure(self, ks, full=None):
        out = {}
        for k in ks:
            r = self.reps[self.where[k]]
            if full is None or k in full:
                out[int(k)] = self.meas(r, self.betas[k], self.V)
            else:  # lite: energy (V=0 estimator) and winding only
                w = self.lat.winding(r.s0)
                out[int(k)] = {"nF": r.nF, "E": -r.nF / self.betas[k], "Wx": int(w[0]), "Wy": int(w[1]), "Wz": int(w[2])}
        return out

    def check(self):
        A = self.A
        for r in self.reps:
            c = check_config(r.s0, r.ft, r.fp, r.nF, A[0], A[5], A[6])
            if c != 0:
                return c
        return 0

    # ---- checkpointing ----
    def save(self, fn):
        d = {"betas": self.betas, "where": self.where, "label": self.label, "dirn": self.dirn,
             "trips": self.trips, "nsw": self.nsw, "swap_acc": self.swap_acc, "swap_try": self.swap_try}
        for i, r in enumerate(self.reps):
            d[f"s0_{i}"] = r.s0
            d[f"ft_{i}"] = r.ft[:r.nF]
            d[f"fp_{i}"] = r.fp[:r.nF]
        tmp = fn + ".tmp.npz"
        np.savez_compressed(tmp, **d)
        os.replace(tmp, fn)

    def load(self, fn):
        d = np.load(fn)
        assert np.allclose(d["betas"], self.betas)
        self.where, self.label, self.dirn = d["where"].copy(), d["label"].copy(), d["dirn"].copy()
        self.trips, self.nsw = int(d["trips"]), int(d["nsw"])
        self.swap_acc, self.swap_try = d["swap_acc"].copy(), d["swap_try"].copy()
        for i, r in enumerate(self.reps):
            r.s0 = d[f"s0_{i}"].copy()
            r.ft = np.concatenate([d[f"ft_{i}"], np.zeros(16)])
            r.fp = np.concatenate([d[f"fp_{i}"], np.zeros(16, dtype=np.int64)])
            r.nF = len(d[f"ft_{i}"])
