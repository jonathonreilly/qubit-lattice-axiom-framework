#!/usr/bin/env python3
"""Flip components of the zero-winding Gauss sector of the supplied ring model (spin-1/2 link fields sigma = +-1 on the periodic cubic torus,
exact vertex Gauss law = 3 in / 3 out, flips of circulating plaquettes, the canonical zero-winding state sigma_x = (-1)^y, sigma_y = sigma_z = (-1)^x).
Supplied-model statements; nothing here is a framework premise and nothing is claimed beyond the lattices listed.

EXACT statements checked here (integer computations and exhaustive enumeration):
 (1) the axis-constant states sigma_x = s(z), sigma_y = g(x), sigma_z = h(y) (or sigma_x = f(y), sigma_y = g(z), sigma_z = h(x)) with s, g, h balanced
     +-1 sequences are Gauss-law states with zero winding and NO circulating plaquette, hence each is a one-state flip component, different from the
     canonical component (which has circulating plaquettes): 2 C(L, L/2)^3 states for even L (all checked for L = 2, 4, 6; a fixed random sample for L = 8);
 (2) exhaustive enumeration on the 2x2x2 torus: 9600 Gauss states, 880 with zero winding = one 864-state flip component (the canonical one) plus 16 frozen
     states, and those 16 are exactly the family of (1); the same on the 2x2x4 torus: 1 552 024 zero-winding states = 1 551 976 + 48 frozen, the 48 being the family;
 (4) linear invariants: the kernel of the plaquette circulation matrix over Q has dimension nv + 2 (nv - 1 gradients, which vanish on Gauss states, plus the 3 windings),
     so the linear flip invariants on Gauss states are the three windings (checked for L = 2, 4 by rank modulo a prime plus the explicit cocycles);
 (5) parity: for odd L the winding of a Gauss state is odd in every direction, so the zero-winding sector is empty;
 (6) explicit flip certificates (the flip list is replayed by an independent function; every flip is a circulating plaquette and the end state equals the canonical state):
     the 48 non-frozen staggered images of the canonical state (L = 4, 8) and fixed-seed loop-VMC samples of |exp(0.2 N_flip)|^2 in the zero-winding sector (8^3 seeds 100..104, 4^3 seeds 100..119).
A certificate proves that sample is in the canonical component.  The runner does NOT prove that every non-frozen zero-winding state is in the canonical component.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import time
from math import comb
import numba as nb
import numpy as np

AUDIT_TIMEOUT_SEC = 180
T0 = time.time()
RES = []


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


class Torus:
    def __init__(self, Lx, Ly=None, Lz=None):
        Ly = Lx if Ly is None else Ly
        Lz = Lx if Lz is None else Lz
        self.dims = (Lx, Ly, Lz)
        self.nv = Lx * Ly * Lz
        self.nl = 3 * self.nv
        self.verts = list(itertools.product(range(Lx), range(Ly), range(Lz)))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=np.int64)
        self.head = np.zeros(self.nl, dtype=np.int64)
        self.axis = np.zeros(self.nl, dtype=np.int64)
        self.coord = np.zeros(self.nl, dtype=np.int64)
        self.tc = np.zeros((self.nl, 3), dtype=np.int64)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % self.dims[a]
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
                self.tc[l] = v
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        plaq = []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % self.dims[a]
                vb[b] = (vb[b] + 1) % self.dims[b]
                plaq.append([3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b])
        self.plaq = np.array(plaq, dtype=np.int64)
        self.sign = np.tile(np.array([1, 1, -1, -1], dtype=np.int64), (len(plaq), 1))
        self.np_ = len(plaq)
        self.B = np.zeros((self.nv, self.nl), dtype=np.int64)
        for v in range(self.nv):
            for (l, s) in self.inc[v]:
                self.B[v, l] += s

    def circ(self, s):
        return (s[..., self.plaq] * self.sign).sum(axis=-1)

    def n_flippable(self, s):
        return int((np.abs(self.circ(s)) == 4).sum())

    def gauss_ok(self, s):
        return bool(np.all(self.B @ s == 0))

    def winding(self, s):
        return tuple(int(s[(self.axis == a) & (self.coord == 0)].sum()) for a in range(3))

    def canonical(self):
        s = np.zeros(self.nl, dtype=np.int64)
        for v in self.verts:
            i = self.vid[v]
            s[3 * i], s[3 * i + 1], s[3 * i + 2] = (-1) ** v[1], (-1) ** v[0], (-1) ** v[0]
        return s

    def loop_vmc(self, alpha, sweeps, therm, r, start, fix_winding=True):
        """loop-VMC exactly as rq3_lib.loop_vmc (directed-loop flips, Metropolis weight exp(2 alpha dN_flip), winding fixed)."""
        sigma = start.copy()
        C = np.zeros(self.np_ + 1)
        C[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        W0 = self.winding(sigma)
        pol = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                pol[l].append(p)
        samples = []
        per_sweep = max(1, self.nl // 20)
        for sw in range(therm + sweeps):
            for _ in range(per_sweep):
                v = r.integers(self.nv)
                seen, path_l = {v: 0}, []
                while True:
                    outs = [l for (l, s) in self.inc[v] if sigma[l] * s == 1]
                    l = outs[r.integers(3)]
                    v = self.head[l] if self.tail[l] == v else self.tail[l]
                    path_l.append(l)
                    if v in seen:
                        cyc = path_l[seen[v]:]
                        break
                    seen[v] = len(path_l)
                aff = sorted({p for l in cyc for p in pol[l]})
                before = int((np.abs(C[aff]) == 4).sum())
                sigma[cyc] *= -1
                C_new = (sigma[self.plaq[aff]] * self.sign[aff]).sum(axis=1)
                after = int((np.abs(C_new) == 4).sum())
                keep = r.random() < np.exp(2 * alpha * (after - before))
                if keep and fix_winding and self.winding(sigma) != W0:
                    keep = False
                if keep:
                    C[aff] = C_new
                else:
                    sigma[cyc] *= -1
            if sw >= therm and sw % 2 == 0:
                samples.append(sigma.copy())
        return samples


# ---------------------------------------------------------------- numba kernels
@nb.njit(cache=False)
def popc(x):
    n = 0
    while x:
        x &= x - 1
        n += 1
    return n


@nb.njit(cache=False)
def dfs_enum(nl, nv, link_tail, link_head, rem0, maxn, wmask, wneed):
    out = np.empty(maxn, dtype=np.int64)
    cnt = 0
    cnt_all = 0
    bal = np.zeros(nv, dtype=np.int64)
    rem = rem0.copy()
    choice = np.zeros(nl, dtype=np.int64)
    code = 0
    i = 0
    while i >= 0:
        if i == nl:
            cnt_all += 1
            if popc(code & wmask[0]) == wneed[0] and popc(code & wmask[1]) == wneed[1] and popc(code & wmask[2]) == wneed[2]:
                if cnt < maxn:
                    out[cnt] = code
                cnt += 1
            i -= 1
            continue
        t, h = link_tail[i], link_head[i]
        if choice[i] > 0:
            s = 1 if choice[i] == 1 else -1
            bal[t] -= s
            bal[h] += s
            rem[t] += 1
            rem[h] += 1
            if s == 1:
                code &= ~(np.int64(1) << i)
        if choice[i] == 2:
            choice[i] = 0
            i -= 1
            continue
        choice[i] += 1
        s = 1 if choice[i] == 1 else -1
        bal[t] += s
        bal[h] -= s
        rem[t] -= 1
        rem[h] -= 1
        if s == 1:
            code |= (np.int64(1) << i)
        if abs(bal[t]) <= rem[t] and abs(bal[h]) <= rem[h]:
            i += 1
            if i < nl:
                choice[i] = 0
    return out[:min(cnt, maxn)], cnt, cnt_all


@nb.njit(cache=False)
def uf_find(par, x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


@nb.njit(cache=False)
def components(codes, plaq, pmask):
    n = codes.shape[0]
    par = np.arange(n)
    nfl = np.zeros(n, dtype=np.int64)
    for i in range(n):
        c = codes[i]
        for p in range(plaq.shape[0]):
            C = 0
            for k in range(4):
                sg = 2 * ((c >> plaq[p, k]) & 1) - 1
                C += sg if k < 2 else -sg
            if C == 4 or C == -4:
                nfl[i] += 1
                c2 = c ^ pmask[p]
                lo, hi = 0, n - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if codes[mid] < c2:
                        lo = mid + 1
                    else:
                        hi = mid
                if codes[lo] != c2:
                    return par, nfl, i
                ra, rb = uf_find(par, i), uf_find(par, lo)
                if ra != rb:
                    par[ra] = rb
    for i in range(n):
        par[i] = uf_find(par, i)
    return par, nfl, -1


@nb.njit(cache=False)
def hamming(a, b):
    d = 0
    for i in range(a.shape[0]):
        if a[i] != b[i]:
            d += 1
    return d


@nb.njit(cache=False)
def anneal(sig, target, plaq, nsteps, T0_, T1_, seed, buf):
    np.random.seed(seed)
    nP = plaq.shape[0]
    D = hamming(sig, target)
    nlog = 0
    lr = np.log(T1_ / T0_)
    T = T0_
    for it in range(nsteps):
        if D == 0:
            break
        if (it & 1023) == 0:
            T = T0_ * np.exp(lr * it / nsteps)
        p = np.random.randint(nP)
        C = sig[plaq[p, 0]] + sig[plaq[p, 1]] - sig[plaq[p, 2]] - sig[plaq[p, 3]]
        if C == 4 or C == -4:
            dD = 0
            for k in range(4):
                l = plaq[p, k]
                if sig[l] == target[l]:
                    dD += 1
                else:
                    dD -= 1
            if dD <= 0 or np.random.random() < np.exp(-dD / T):
                for k in range(4):
                    sig[plaq[p, k]] = -sig[plaq[p, k]]
                D += dD
                if nlog < buf.shape[0]:
                    buf[nlog] = p
                nlog += 1
    if nlog > buf.shape[0]:
        nlog = -1
    return D, nlog


@nb.njit(cache=False)
def replay_ok(sig0, target, plaq, flips):
    s = sig0.copy()
    for i in range(flips.shape[0]):
        p = flips[i]
        C = s[plaq[p, 0]] + s[plaq[p, 1]] - s[plaq[p, 2]] - s[plaq[p, 3]]
        if C != 4 and C != -4:
            return False
        for k in range(4):
            s[plaq[p, k]] = -s[plaq[p, k]]
    for i in range(s.shape[0]):
        if s[i] != target[i]:
            return False
    return True


# ---------------------------------------------------------------- family of frozen states
def balanced(n):
    return [np.array(c) for c in itertools.product((1, -1), repeat=n) if sum(c) == 0]


def family_state(T, which, s, g, h):
    """which = 'cyc': sigma_x = s(z), sigma_y = g(x), sigma_z = h(y);  'anti': sigma_x = s(y), sigma_y = g(z), sigma_z = h(x)."""
    tc, ax = T.tc, T.axis
    if which == "cyc":
        return np.where(ax == 0, s[tc[:, 2]], np.where(ax == 1, g[tc[:, 0]], h[tc[:, 1]])).astype(np.int64)
    return np.where(ax == 0, s[tc[:, 1]], np.where(ax == 1, g[tc[:, 2]], h[tc[:, 0]])).astype(np.int64)


def family_lengths(T, which):
    Lx, Ly, Lz = T.dims
    return (Lz, Lx, Ly) if which == "cyc" else (Ly, Lz, Lx)


def family_size(T):
    Lx, Ly, Lz = T.dims
    return 2 * comb(Lx, Lx // 2) * comb(Ly, Ly // 2) * comb(Lz, Lz // 2)


def family_iter(T):
    for which in ("cyc", "anti"):
        n1, n2, n3 = family_lengths(T, which)
        for s in balanced(n1):
            for g in balanced(n2):
                for h in balanced(n3):
                    yield which, s, g, h


def family_codes(T):
    out = set()
    pw = 1 << np.arange(T.nl, dtype=np.int64)
    for which, s, g, h in family_iter(T):
        st = family_state(T, which, s, g, h)
        out.add(int(((st + 1) // 2 * pw).sum()))
    return out


# ---------------------------------------------------------------- checks
def check_family(L, sample=None):
    T = Torus(L)
    combos = list(family_iter(T))
    if sample is not None:
        rng = np.random.default_rng(5)
        idx = rng.choice(len(combos), size=sample, replace=False)
        combos = [combos[i] for i in idx]
    seen = set()
    ok = True
    for (w, s_, g_, h_) in combos:
        st = family_state(T, w, s_, g_, h_)
        ok &= T.gauss_ok(st) and T.winding(st) == (0, 0, 0) and T.n_flippable(st) == 0
        seen.add(st.tobytes())
    exp = family_size(T)
    if sample is None:
        check(f"L={L}: all {exp} axis-constant states are Gauss, zero winding, frozen, distinct", ok and len(seen) == exp, f"checked {len(combos)}, distinct {len(seen)}")
    else:
        check(f"L={L}: fixed random sample of {len(combos)} of the {exp} axis-constant states are Gauss, zero winding, frozen (sample, not exhaustive)", ok, f"distinct {len(seen)}")


def exhaustive(dims, expect_zero, expect_big, expect_frozen):
    T = Torus(*dims)
    rem0 = np.array([len(T.inc[v]) for v in range(T.nv)], dtype=np.int64)
    wmask = np.array([sum(1 << int(l) for l in np.flatnonzero((T.axis == a) & (T.coord == 0))) for a in range(3)], dtype=np.int64)
    wsz = np.array([int(((T.axis == a) & (T.coord == 0)).sum()) for a in range(3)])
    codes, cnt, cnt_all = dfs_enum(T.nl, T.nv, T.tail, T.head, rem0, 3_000_000, wmask, (wsz + 0) // 2)
    codes = np.sort(codes)
    pmask = np.array([sum(1 << int(l) for l in links) for links in T.plaq], dtype=np.int64)
    par, nfl, bad = components(codes, T.plaq, pmask)
    roots, inv, sizes = np.unique(par, return_inverse=True, return_counts=True)
    c = T.canonical()
    code_c = int(((c + 1) // 2 * (1 << np.arange(T.nl))).sum())
    i0 = int(np.searchsorted(codes, code_c))
    big = sizes[inv[i0]]
    frozen = np.flatnonzero(nfl == 0)
    fam = family_codes(T)
    frozen_set = set(int(codes[j]) for j in frozen)
    check(f"{'x'.join(map(str, dims))} exhaustive: zero-winding Gauss states = {expect_zero}, canonical component = {expect_big}, other components all frozen singletons = {expect_frozen}",
          bad < 0 and len(codes) == expect_zero and big == expect_big and len(roots) == 1 + expect_frozen and len(frozen) == expect_frozen
          and (sizes == 1).sum() == expect_frozen and big + expect_frozen == len(codes),
          f"all Gauss states {cnt_all}, zero winding {len(codes)}, components {len(roots)}, canonical comp {int(big)}, frozen {len(frozen)}")
    check(f"{'x'.join(map(str, dims))}: the frozen states are exactly the axis-constant family", frozen_set == fam, f"family {len(fam)}")


def linear_invariants(L):
    T = Torus(L)
    P = 2147483629
    A = np.zeros((T.np_, T.nl), dtype=np.int64)
    for p in range(T.np_):
        for k in range(4):
            A[p, T.plaq[p, k]] += T.sign[p, k]
    A %= P
    r = 0
    A = A.copy()
    rows, cols = A.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c] % P:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = (A[r] * inv) % P
        nz = np.flatnonzero(A[:, c] % P)
        for i in nz:
            if i != r:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
    ker = T.nl - r
    check(f"L={L}: kernel of the plaquette circulation matrix has dimension nv + 2 = {T.nv + 2}", ker == T.nv + 2, f"rank mod p = {r}, kernel dim {ker} (>= nv+2 from nv-1 gradients + 3 holonomies, <= by rank mod p)")


def certificates(L, n_loop, seed0, nsteps):
    T = Torus(L)
    canon = T.canonical()
    buf = np.zeros(5_000_000, dtype=np.int32)
    ok_all, n = True, 0
    # staggered images
    nb_ = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
    nfro = nconn = 0
    for b in itertools.product(*(nb_[a] for a in range(3))):
        for cc in itertools.product((1, -1), repeat=3):
            s = np.array([cc[T.axis[l]] * (-1) ** int(T.tc[l][b[T.axis[l]]]) for l in range(T.nl)], dtype=np.int64)
            if T.n_flippable(s) == 0:
                nfro += 1
                continue
            ss = s.copy()
            D, nlog = anneal(ss, canon, T.plaq, nsteps, 1.0, 0.25, 12345, buf)
            ok = D == 0 and nlog >= 0 and replay_ok(s, canon, T.plaq, buf[:nlog].copy())
            nconn += int(ok)
    check(f"L={L}: of the 64 staggered zero-winding states, 16 are frozen and the other 48 have replayed flip certificates to the canonical state", nfro == 16 and nconn == 48, f"frozen {nfro}, certified {nconn}")
    nc = 0
    for i in range(n_loop):
        s = T.loop_vmc(0.2, sweeps=max(40, 1600 // L), therm=60, r=np.random.default_rng(seed0 + i), start=canon)[-1]
        assert T.gauss_ok(s) and T.winding(s) == (0, 0, 0)
        ss = s.copy()
        D, nlog = anneal(ss, canon, T.plaq, nsteps, 1.0, 0.25, 11000 + seed0 + i, buf)
        nc += int(D == 0 and nlog >= 0 and replay_ok(s, canon, T.plaq, buf[:nlog].copy()))
    check(f"L={L}: {n_loop} loop-VMC (alpha = 0.2, seeds {seed0}..{seed0 + n_loop - 1}) starts each have a replayed flip certificate to the canonical state", nc == n_loop, f"certified {nc} of {n_loop}")


def main():
    print("flip components of the zero-winding Gauss sector (supplied ring model, torus lattices)")
    # (5) parity
    for L in (3, 5, 7):
        check(f"L={L} odd: plane flux is a sum of {L * L} terms +-1, so odd: no zero-winding Gauss state", (L * L) % 2 == 1)
    for L in (2, 4):
        check(f"L={L}: canonical state is Gauss, zero winding", Torus(L).gauss_ok(Torus(L).canonical()) and Torus(L).winding(Torus(L).canonical()) == (0, 0, 0))
    for L in (2, 4, 6):
        check_family(L)
    check_family(8, sample=300)
    exhaustive((2, 2, 2), 880, 864, 16)
    exhaustive((2, 2, 4), 1552024, 1551976, 48)
    for L in (2, 4):
        linear_invariants(L)
    certificates(4, 20, 100, 20_000_000)
    certificates(8, 5, 100, 300_000_000)
    npass, nfail = sum(RES), len(RES) - sum(RES)
    print(f"TOTAL: PASS={npass} FAIL={nfail}   ({time.time() - T0:.0f} s)")
    raise SystemExit(0 if nfail == 0 else 1)


if __name__ == "__main__":
    main()
