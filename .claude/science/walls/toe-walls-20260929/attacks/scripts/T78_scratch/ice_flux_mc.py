"""T78 scratch: uniform-ice plaquette-flip Monte Carlo in fixed flux sectors.

Model (supplied, as in docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_..._2026-09-03.md):
  cubic torus L^3, one qubit per link, s[a,x,y,z] = +1 if the arrow points from v to v+e_a, else -1.
  Ice rule: out-degree 3 at every vertex.  Plaquette (v,a<b) is flippable iff its four links circulate;
  a flip reverses the four links.  Flips preserve the ice rule and the section fluxes W_a.
  Uniform measure on a flip component = the RK ground state weights (H_RK = sum_p (F_p^2 - F_p)).
  N_f = number of flippable plaquettes.
Flux convention: W_x = sum over the L^2 x-links of one plane of s ; W_x = 2 q ; Phi = q.
"""
import numpy as np
import numba as nb
from numba import njit, prange


@njit(cache=True)
def _xs(state):
    # xorshift64*
    x = state[0]
    x ^= x >> np.uint64(12)
    x ^= x << np.uint64(25)
    x ^= x >> np.uint64(27)
    state[0] = x
    return x * np.uint64(2685821657736338717)


@njit(cache=True)
def seed_config(L, q):
    s = np.empty((3, L, L, L), dtype=np.int8)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s[0, x, y, z] = 1 if ((y + z) % 2 == 0) else -1
                s[1, x, y, z] = 1 if ((z + x) % 2 == 0) else -1
                s[2, x, y, z] = 1 if ((x + y) % 2 == 0) else -1
    # reverse q x-lines (y+z odd) spread evenly over the cross-section
    odd = np.empty(L * L // 2, dtype=np.int64)
    n = 0
    for y in range(L):
        for z in range(L):
            if (y + z) % 2 == 1:
                odd[n] = y * L + z
                n += 1
    for k in range(q):
        idx = odd[(k * n) // max(q, 1)] if q > 0 else 0
        y = idx // L
        z = idx % L
        for x in range(L):
            s[0, x, y, z] = 1
    return s


@njit(cache=True)
def plaq_links(a, b, x, y, z, L):
    # returns coordinates of the 4 links of plaquette (v,a,b): (v,a),(v+ea,b),(v+eb,a),(v,b)
    return 0


@njit(cache=True)
def flippable(s, a, b, x, y, z, L):
    # positions
    xa = x; ya = y; za = z
    if a == 0: xa = (x + 1) % L
    elif a == 1: ya = (y + 1) % L
    else: za = (z + 1) % L
    xb = x; yb = y; zb = z
    if b == 0: xb = (x + 1) % L
    elif b == 1: yb = (y + 1) % L
    else: zb = (z + 1) % L
    s1 = s[a, x, y, z]
    s2 = s[b, xa, ya, za]
    s3 = s[a, xb, yb, zb]
    s4 = s[b, x, y, z]
    return (s1 == s2) and (s1 == -s3) and (s1 == -s4)


@njit(cache=True)
def flip(s, a, b, x, y, z, L):
    xa = x; ya = y; za = z
    if a == 0: xa = (x + 1) % L
    elif a == 1: ya = (y + 1) % L
    else: za = (z + 1) % L
    xb = x; yb = y; zb = z
    if b == 0: xb = (x + 1) % L
    elif b == 1: yb = (y + 1) % L
    else: zb = (z + 1) % L
    s[a, x, y, z] = -s[a, x, y, z]
    s[b, xa, ya, za] = -s[b, xa, ya, za]
    s[a, xb, yb, zb] = -s[a, xb, yb, zb]
    s[b, x, y, z] = -s[b, x, y, z]


@njit(cache=True)
def count_flippable(s, L):
    n = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                if flippable(s, 0, 1, x, y, z, L): n += 1
                if flippable(s, 1, 2, x, y, z, L): n += 1
                if flippable(s, 0, 2, x, y, z, L): n += 1
    return n


@njit(cache=True)
def sweep(s, L, rng):
    npl = 3 * L * L * L
    for _ in range(npl):
        r = _xs(rng)
        site = np.int64((r >> np.uint64(8)) % np.uint64(L * L * L))
        o = np.int64((r >> np.uint64(40)) % np.uint64(3))
        x = site // (L * L)
        y = (site // L) % L
        z = site % L
        if o == 0: a = 0; b = 1
        elif o == 1: a = 1; b = 2
        else: a = 0; b = 2
        if flippable(s, a, b, x, y, z, L):
            flip(s, a, b, x, y, z, L)


@njit(cache=True)
def check_ice_and_flux(s, L):
    # returns (max |out-3| over vertices, Wx, Wy, Wz at plane 0 and max deviation across planes)
    bad = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                out = 0
                if s[0, x, y, z] == 1: out += 1
                if s[1, x, y, z] == 1: out += 1
                if s[2, x, y, z] == 1: out += 1
                if s[0, (x - 1) % L, y, z] == -1: out += 1
                if s[1, x, (y - 1) % L, z] == -1: out += 1
                if s[2, x, y, (z - 1) % L] == -1: out += 1
                d = abs(out - 3)
                if d > bad: bad = d
    W = np.zeros(3, dtype=np.int64)
    dev = 0
    for a in range(3):
        base = 0
        for p in range(L):
            tot = 0
            for u in range(L):
                for w in range(L):
                    if a == 0: tot += s[0, p, u, w]
                    elif a == 1: tot += s[1, u, p, w]
                    else: tot += s[2, u, w, p]
            if p == 0:
                base = tot
                W[a] = tot
            else:
                if abs(tot - base) > dev: dev = abs(tot - base)
    return bad, W[0], W[1], W[2], dev


@njit(parallel=True, cache=True)
def run_replicas(L, qs, nrep, burn, nsamp, gap, seed0):
    """qs: array of q per replica (length nrep). returns samples[nrep, nsamp] of N_f and diagnostics."""
    out = np.zeros((nrep, nsamp), dtype=np.float64)
    diag = np.zeros((nrep, 5), dtype=np.int64)
    for r in prange(nrep):
        q = qs[r]
        s = seed_config(L, q)
        rng = np.empty(1, dtype=np.uint64)
        rng[0] = np.uint64(seed0 + 7919 * (r + 1)) * np.uint64(0x9E3779B97F4A7C15) + np.uint64(12345)
        for _ in range(20):
            _xs(rng)
        for _ in range(burn):
            sweep(s, L, rng)
        for k in range(nsamp):
            for _ in range(gap):
                sweep(s, L, rng)
            out[r, k] = count_flippable(s, L)
        bad, w0, w1, w2, dev = check_ice_and_flux(s, L)
        diag[r, 0] = bad
        diag[r, 1] = w0
        diag[r, 2] = w1
        diag[r, 3] = w2
        diag[r, 4] = dev
    return out, diag
