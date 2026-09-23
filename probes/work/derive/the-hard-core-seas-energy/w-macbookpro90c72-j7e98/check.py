#!/usr/bin/env python3
"""J:derive:the-hard-core-seas-energy:a1 -- worker w-macbookpro90c72-j7e98 (claude-opus-5-5).

Records under one-per-site exclusion (either exchange sign) against block 76's free sea.
Exact checks (Fractions, Gaussian rationals, sympy) are the 'ok' lines; 'note' lines are floating point
(dense diagonalisation, second-order perturbation theory in the degenerate ground level).
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

# ------------------------------------------------------------------ lattices (block 78's conventions)
# one-body H = sum_bonds |x><y| (x) B + h.c.; ring: <x|H|x+1> = (-i/2) sigma3 (H = sigma3 S, S = (T - T^t)/2i);
# torus: <x|H|x+e0> = (-i/2) sigma1, <x|H|x+e1> = (-i/2) sigma2 (H = sigma1 S_x + sigma2 S_y). B[(c', c)] = <x c'|H|y c>.
Z, H_ = Fr(0), Fr(1, 2)
B_RING = {(0, 0): (Z, -H_), (1, 1): (Z, H_)}
B_S1 = {(0, 1): (Z, -H_), (1, 0): (Z, -H_)}
B_S2 = {(0, 1): (-H_, Z), (1, 0): (H_, Z)}
def adj(B):
    return {(j, i): (v[0], -v[1]) for (i, j), v in B.items()}
def ring(L):
    return L, [(x, (x + 1) % L, B_RING) for x in range(L)], [(x,) for x in range(L)], (L,)
def torus(L):
    bonds = []
    for a in range(L):
        for b in range(L):
            bonds.append((a * L + b, ((a + 1) % L) * L + b, B_S1)); bonds.append((a * L + b, a * L + (b + 1) % L, B_S2))
    return L * L, bonds, [(a, b) for a in range(L) for b in range(L)], (L, L)

def basis(n, N):
    st = []
    for sites in itertools.combinations(range(n), N):
        for coins in itertools.product((0, 1), repeat=N):
            st.append(sum(1 << (2 * s + c) for s, c in zip(sites, coins)))
    st.sort(); return st, {m: i for i, m in enumerate(st)}

def below(m, k):
    return bin(m & ((1 << k) - 1)).count("1")

def hops(n, bonds, N, stat):
    """every nonzero entry of the hard-core N-record generator: (row, col, bond, amplitude (re, im)) at unit rates."""
    st, idx = basis(n, N); out = []
    for bi, (x, y, B) in enumerate(bonds):
        for (src, dst, Bm) in ((y, x, B), (x, y, adj(B))):
            for j, m in enumerate(st):
                o = (m >> (2 * src)) & 3
                if o == 0 or (m >> (2 * dst)) & 3:
                    continue
                c = 0 if o == 1 else 1; mp = 2 * src + c
                for (cp, c0), a in Bm.items():
                    if c0 != c:
                        continue
                    mq = 2 * dst + cp; m2 = m & ~(1 << mp)
                    s = (-1) ** (below(m, mp) + below(m2, mq)) if stat == "f" else 1
                    out.append((idx[m2 | (1 << mq)], j, bi, (a[0] * s, a[1] * s)))
    return st, out

def spinless_amp(L, src, dst):
    """<dst|h|src> for the up-coin species on the ring: <x|h|x+1> = -i/2."""
    return (Z, -H_) if dst == (src - 1) % L else (Z, H_)

# ------------------------------------------------------------------ X.pack / X.sign: packing, trace, the volume term's sign
good = True
for (n, bonds, _, _), N in ((ring(8), 8), (torus(3), 9), (torus(4), 16)):
    good &= len(hops(n, bonds, N, "f")[1]) == 0
for (n, bonds, _, _), N in ((ring(8), 4), (torus(3), 5)):
    st, hp = hops(n, bonds, N, "f")
    good &= all(r != c for r, c, _, _ in hp) and len(hp) > 0
ok("X.pack", good, "at N = sites (half of the one-body states) the hard-core generator is identically zero (ring 8, 3x3, 4x4); for "
   "0 < N < sites it is traceless (no on-site term) and nonzero, so its ground energy, the volume term, is strictly negative")

# ------------------------------------------------------------------ X.chess: a chessboard of clocks under exclusion
good = True
for (n, bonds, coords, _), N in ((ring(8), 4), (torus(4), 3)):
    phi = [Fr(3, 2) ** (1 if sum(c) % 2 == 0 else -1) for c in coords]
    good &= all(phi[x] * phi[y] == 1 for (x, y, _) in bonds)
    rnd = [Fr(k % 7 + 2, k % 5 + 3) for k in range(n)]                 # a generic rational rate field
    st, hp = hops(n, bonds, N, "f")
    ent = {}
    for r, c, b, a in hp:
        x, y, _ = bonds[b]; w = rnd[x] * rnd[y]
        ent[(r, c)] = (a[0] * w, a[1] * w)
    good &= all(ent[(r, c)] == (ent[(c, r)][0], -ent[(c, r)][1]) for (r, c) in ent)   # Hermitian at every rate field
ok("X.chess", good, "the clocked generator P dGamma(phi H phi) P depends on the rates only through the bond products phi_x phi_y "
   "(each hop carries its own bond's product); a chessboard phi = c^(+-1) has every bond product exactly 1 on the ring of 8 and the "
   "4x4 torus, so the hard-core sea, every eigenvalue and every second variation are unchanged at any amplitude (odd tori have no chessboard)")

# ------------------------------------------------------------------ X.ring: exclusion on a ring = one spinless band with a twist
def decode(m, L):
    xs, ss = [], []
    for s in range(L):
        o = (m >> (2 * s)) & 3
        if o:
            xs.append(s); ss.append(0 if o == 1 else 1)
    return xs, ss
good = True; checked = 0
for L, N in ((8, 4), (8, 6), (7, 3)):
    n, bonds, _, _ = ring(L)
    w = [Fr(k % 5 + 1, k % 3 + 2) for k in range(L)]
    for stat in "fb":
        st, hp = hops(n, bonds, N, stat)
        for r, c, b, a in hp:
            xs, ss = decode(st[c], L); xs2, ss2 = decode(st[r], L)
            src = (set(xs) - set(xs2)).pop(); dst = (set(xs2) - set(xs)).pop()
            gc = (-1) ** sum(x for x, s in zip(xs, ss) if s); gr = (-1) ** sum(x for x, s in zip(xs2, ss2) if s)
            val = (a[0] * gc * gr * w[b], a[1] * gc * gr * w[b])
            sa = spinless_amp(L, src, dst); wrap = {src, dst} == {0, L - 1}
            pred = (sa[0] * w[b], sa[1] * w[b])
            if not wrap:
                good &= ss2 == ss and val == pred
            else:
                fwd = src == L - 1
                mover = ss[-1] if fwd else ss[0]
                good &= ss2 == ([ss[-1]] + ss[:-1] if fwd else ss[1:] + [ss[0]])
                f = (-1) ** (N - 1)                                                       # spinless-fermion wrap sign
                f *= 1 if stat == "f" else (-1) ** (N - 1)                                # bosons: Jordan-Wigner
                f *= (-1) if (L % 2 and mover) else 1                                     # odd ring: down coin's sign
                good &= val == (pred[0] * f, pred[1] * f)
            checked += 1
ok("X.ring", good, f"{checked} entries (rings 8 and 7, N = 3, 4, 6, both exchange signs, generic rational rates): after the gauge "
   "(-1)^x on down coins, every hop is the up-coin spinless hop with the coin sequence unchanged, and every hop across the wrap "
   "bond rotates the sequence with a fixed sign; so H = h_open (x) 1 + h_wrap (x) R + h.c. and the records are ONE spinless band "
   "whose wrap bond carries an eigenvalue of R")

# twist sets and multiplicities: R = (sign) x rotation on coin sequences; an R-orbit of period p whose signs multiply to sigma
# carries the p-th roots of sigma once each (exact integer arithmetic; twists in units of 2pi)
def twist_mults(L, N, stat):
    def sign(s):
        return ((-1) ** (N - 1) if stat == "b" else 1) * ((-1) if (L % 2 and s[-1]) else 1)
    seen, out = set(), {}
    for s in itertools.product((0, 1), repeat=N):
        if s in seen:
            continue
        t, sg, p = s, 1, 0
        while True:
            sg *= sign(t); t = (t[-1],) + t[:-1]; p += 1; seen.add(t)
            if t == s:
                break
        for j in range(2 * N):                       # candidate twist j/(2N): its p-th power must be sigma
            r = Fr(j * p, N)                         # = 2 j p/(2N): even iff rho^p = 1, odd iff rho^p = -1
            if r.denominator == 1 and (r.numerator % 2 == 0) == (sg == 1):
                out[Fr(j, 2 * N)] = out.get(Fr(j, 2 * N), 0) + 1
    return out
good = True
tw = {}
for L, N in ((8, 4), (8, 6), (7, 3), (7, 6)):
    mf, mb = twist_mults(L, N, "f"), twist_mults(L, N, "b")
    tw[(L, N)] = (mf, mb)
    good &= set(mf) == set(mb) and sum(mf.values()) == 2 ** N == sum(mb.values())
    good &= len(mf) == (N if L % 2 == 0 else 2 * N)
good &= tw[(8, 6)][0][Fr(1, 2)] == 10 and tw[(8, 6)][1][Fr(1, 2)] == 14
ok("X.twists", good, "R's eigenvalues give the wrap twists: all N-th roots of unity on even rings, all 2N-th on odd rings, the SAME "
   "set for fermions and bosons (only multiplicities differ, e.g. 10 against 14 at the twist -1 on the ring of 8 with 6 records), so "
   "the two exchange signs have the same ground energy and the same second variation for every rate field on every ring")

# ------------------------------------------------------------------ X.holes: the free sea's filling under exclusion
good = True
def zero_kpoints(shape):
    return math.prod(2 if La % 2 == 0 else 1 for La in shape)
for (n, bonds, coords, shape), d in ((ring(8), 1), (ring(7), 1), (torus(3), 2)):
    h = zero_kpoints(shape); Nneg = n - h
    st, hp = hops(n, bonds, Nneg, "f")
    rows = {}
    for r, c, b, a in hp:
        rows[r] = rows.get(r, 0) + 1
        good &= a[0] * a[0] + a[1] * a[1] == Fr(1, 4)
    good &= max(rows.values()) * Fr(1, 2) <= h * d
good &= zero_kpoints((4, 4)) == 4 and zero_kpoints((6, 6, 6)) == 8
ok("X.holes", good, "the walk's one-body zeros are the k with every sin k_a = 0, 2^(number of even sides) points, so the free sea's "
   "filling N_neg = sites - h leaves h empty sites under exclusion (1 on ring 7 and 3x3, 2 on ring 8, 4 on even 2D tori, 8 on even "
   "3D tori); every entry has modulus w_b/2 and a row has at most 2dh of them, so |E| <= h d max w_b: O(1), not O(sites)")

# ------------------------------------------------------------------ X.half: the half-filled ring in the thermodynamic limit
t, q = sp.symbols("t q", positive=True)
good = sp.simplify(sp.diff(sp.log(sp.sec(t) + sp.tan(t)) - sp.sin(t), t) - sp.sin(t) ** 2 / sp.cos(t)) == 0
held = -sp.cos(q / 2) ** 2 / (4 * sp.pi)                                          # (1/2pi) int_{-pi}^0 sin k dk * cos^2(q/2)/4
relax = -(sp.cos(q / 2) ** 2 / (8 * sp.pi * sp.sin(q / 2))) * 2 * (sp.log(sp.sec(q / 2) + sp.tan(q / 2)) - sp.sin(q / 2))
Pi_hc = sp.simplify(held + relax)
closed = -sp.cos(q / 2) ** 2 * sp.log(sp.sec(q / 2) + sp.tan(q / 2)) / (4 * sp.pi * sp.sin(q / 2))
good &= sp.simplify(Pi_hc - closed) == 0
ser = sp.series(closed, q, 0, 4).removeO()
c0h = sp.nsimplify(4 * ser.subs(q, 0)); kh = sp.nsimplify(4 * ser.coeff(q, 2))
good &= c0h == -1 / sp.pi and kh == 1 / (6 * sp.pi)
ok("X.half", good, "one spinless band half filled: Pi(q) = held -cos^2(q/2)/(4pi) + relaxation "
   "-(cos^2(q/2)/(4pi sin(q/2)))[ln(sec+tan)(q/2) - sin(q/2)] = -cos^2(q/2) ln(sec(q/2)+tan(q/2))/(4pi sin(q/2)) = -1/(4pi) + q^2/(24pi) "
   "+ ...: volume term -1/pi and kappa = 1/(6pi); the free sea is two such bands (one per coin): -2/pi and 1/(3pi)")

# ------------------------------------------------------------------ X.sea: which record number is the hard-core sea on a ring
Xs = sp.symbols("X"); good = True
for Lr_, M_ in ((8, 4), (12, 6), (8, 3), (12, 5)):
    # sum_m sin(a + 2 pi m/L) = A sin a + B cos a; compare A, B with the closed form exactly (minimal polynomial of the difference)
    A = sum(sp.cos(2 * sp.pi * m / Lr_) for m in range(M_)); B = sum(sp.sin(2 * sp.pi * m / Lr_) for m in range(M_))
    s = sp.sin(sp.pi * M_ / Lr_) / sp.sin(sp.pi / Lr_); c = sp.pi * (M_ - 1) / Lr_
    good &= sp.minimal_polynomial(A - sp.cos(c) * s, Xs) == Xs and sp.minimal_polynomial(B - sp.sin(c) * s, Xs) == Xs
xx = sp.symbols("x", positive=True)
good &= sp.simplify(sp.cot(xx) - 1 / sp.sin(xx) - (sp.cos(xx) - 1) / sp.sin(xx)) == 0      # < 0 on (0, pi)
ok("X.sea", good, "a window of M consecutive points of the twisted grid sums sin to sin(centre) sin(pi M/L)/sin(pi/L) >= -1/sin(pi/L), "
   "with equality only for M = L/2 centred at -pi/2 (twist pi, allowed when 4 | L): so the lowest state over ALL record numbers, "
   "the hard-core sea in block 76's sense, is half filled with E = -1/sin(pi/L), against the free sea's -2 cot(pi/L)")

# ------------------------------------------------------------------ X.edge: the free sea's smallest mode on an even ring
Lr = sp.symbols("L", positive=True)
a_ = sp.pi / Lr
E0f = -2 * sp.cot(a_)                              # two coins, negative states only
held_g = -(E0f / 4) * sp.sin(a_) ** 2              # held part minus the volume term: (E0/4)(cos^2 - 1)
relax_e = 2 * (-sp.sin(2 * a_) / 8)                # per coin: two transitions into the zero modes k = 0, pi
good = sp.simplify(held_g + relax_e) == 0
ok("X.edge", good, "on every even ring the free sea's mode q = 2pi/L has gradient part exactly 0: its only relaxation channels are "
   "the two transitions into the exact zero modes, which give -sin(2pi/L)/8 per coin, cancelling the held gradient term "
   "cot(pi/L) sin^2(pi/L)/4 exactly; smallest-mode stiffnesses on even rings measure the zero modes, not the sea")

# ------------------------------------------------------------------ floating point: exact diagonalisation (notes)
S1 = np.array([[0, 1], [1, 0]], complex); S2 = np.array([[0, -1j], [1j, 0]]); S3 = np.diag([1.0 + 0j, -1.0])
def fbonds(name, L):
    if name == "ring":
        return L, [(x, (x + 1) % L, -0.5j * S3) for x in range(L)], [(x,) for x in range(L)], (L,)
    bs = []
    for a in range(L):
        for b in range(L):
            bs.append((a * L + b, ((a + 1) % L) * L + b, -0.5j * S1)); bs.append((a * L + b, a * L + (b + 1) % L, -0.5j * S2))
    return L * L, bs, [(a, b) for a in range(L) for b in range(L)], (L, L)
def onebody(n, bonds, w):
    Hm = np.zeros((2 * n, 2 * n), complex)
    for i, (x, y, B) in enumerate(bonds):
        Hm[2 * x:2 * x + 2, 2 * y:2 * y + 2] += w[i] * B; Hm[2 * y:2 * y + 2, 2 * x:2 * x + 2] += w[i] * B.conj().T
    return Hm
def modes(coords, shape, qv):
    return np.array([math.cos(sum(2 * math.pi * qa * xa / La for qa, xa, La in zip(qv, c, shape))) for c in coords])
def q2lat(shape, qv):
    return sum(2 * (1 - math.cos(2 * math.pi * qa / La)) for qa, La in zip(qv, shape))
def free_pt(n, bonds, u, occ):
    lam, V = np.linalg.eigh(onebody(n, bonds, np.ones(len(bonds))))
    a = np.array([(u[x] + u[y]) / 2 for (x, y, _) in bonds])
    h1, h2 = onebody(n, bonds, a), onebody(n, bonds, a * a / 2)
    o = occ(lam); Vo, Vu = V[:, o], V[:, ~o]; X = Vu.conj().T @ h1 @ Vo
    return lam[o].sum(), np.real(np.trace(Vo.conj().T @ h2 @ Vo)) + np.sum(np.abs(X) ** 2 / (lam[o][None, :] - lam[~o][:, None]))
def hc_pt(n, bonds, N, stat, us):
    st, hp = hops(n, bonds, N, stat)                    # exact amplitudes, converted once to floating point
    D = len(st); rows = np.array([h[0] for h in hp]); cols = np.array([h[1] for h in hp]); bix = np.array([h[2] for h in hp])
    amp = np.array([float(h[3][0]) + 1j * float(h[3][1]) for h in hp])
    def build(wb):
        M = np.zeros((D, D), complex); np.add.at(M, (rows, cols), amp * wb[bix]); return M
    w, V = np.linalg.eigh(build(np.ones(len(bonds)))); E0 = w[0]; g = int(np.sum(w < E0 + 1e-8)); P0 = V[:, :g]
    res = []
    for u in us:
        a = np.array([(u[x] + u[y]) / 2 for (x, y, _) in bonds])
        X = V.conj().T @ (build(a) @ P0); M1 = (X[:g] + X[:g].conj().T) / 2
        mu = np.linalg.eigvalsh(M1)[0]
        M2 = P0.conj().T @ (build(a * a / 2) @ P0) + X[g:].conj().T @ (X[g:] / (E0 - w[g:])[:, None])
        res.append((mu, np.linalg.eigvalsh((M2 + M2.conj().T) / 2)[0]))
    return E0, g, res
def run(name, L, Ns, qs):
    n, fb, coords, shape = fbonds(name, L); eb = (ring(L) if name == "ring" else torus(L))[1]
    us = [modes(coords, shape, qv) for qv in qs]; q2 = [q2lat(shape, qv) for qv in qs]
    neg = lambda lam: lam < -1e-9
    Ef = free_pt(n, fb, np.zeros(n), neg)[0]; Pf = [free_pt(n, fb, u, neg)[1] / n for u in us]
    line = f"{name}{L}: free c0 {Ef / n:+.4f} G " + " ".join(f"{(p - Ef / n / 4) / qq:+.4f}" for p, qq in zip(Pf, q2))
    for N in Ns:
        parts = []
        for stat in "fb":
            E0, g, res = hc_pt(n, eb, N, stat, us)
            Gs = " ".join((f"{(r[1] / n - E0 / n / 4) / qq:+.4f}" if abs(r[0]) < 1e-9 else f"lin{-abs(r[0]):+.4f}") for r, qq in zip(res, q2))
            parts.append((f"{E0 / n:+.4f}", g, Gs))
        if parts[0][0] == parts[1][0] and parts[0][2] == parts[1][2]:
            line += f"; N={N} c0 {parts[0][0]} g {parts[0][1]}/{parts[1][1]} G {parts[0][2]} (f=b)"
        else:
            line += f"; N={N} f c0 {parts[0][0]} G {parts[0][2]} | b c0 {parts[1][0]} G {parts[1][2]}"
    print("note (floating) " + line)
run("ring", 7, (3, 4, 6), [(1,), (2,), (3,)])
run("ring", 8, (4, 6), [(1,), (2,), (3,)])
run("torus", 3, (4, 5, 8), [(1, 0), (1, 1)])
import scipy.sparse as sps, scipy.sparse.linalg as spla
n3, b3, _, _ = torus(3); row = []
for stat in "fb":
    es = []
    for N in range(1, 9):
        st, hp = hops(n3, b3, N, stat)
        Hs = sps.csr_matrix(([float(h[3][0]) + 1j * float(h[3][1]) for h in hp], ([h[0] for h in hp], [h[1] for h in hp])), shape=(len(st),) * 2)
        es.append(spla.eigsh(Hs, k=4, which="SA", tol=1e-12, return_eigenvectors=False).min())
    row.append(f"{stat}: lowest at N = {1 + int(np.argmin(es))} ({min(es):.4f}), N = 8 gives {es[7]:.4f}")
print("note (floating) 3x3 ground energy over N = 1..8: " + "; ".join(row))

# 1D limit through the exact reduction (floating): twisted spinless bands
def hspin(L, th, w):
    hm = np.zeros((L, L), complex)
    for x in range(L):
        y = (x + 1) % L; av = -0.5j * w[x] * (np.exp(1j * th) if y == 0 else 1.0); hm[x, y] += av; hm[y, x] += np.conj(av)
    return hm
def spin_pt(L, th, u, occ):
    a = (u + np.roll(u, -1)) / 2; lam, V = np.linalg.eigh(hspin(L, th, np.ones(L))); o = occ(lam)
    if o.sum() < L and (~o).sum() and lam[~o].min() - lam[o].max() < 1e-9:
        return None
    X = V[:, ~o].conj().T @ hspin(L, th, a) @ V[:, o]
    return lam[o].sum(), np.real(np.trace(V[:, o].conj().T @ hspin(L, th, a * a / 2) @ V[:, o])) + np.sum(np.abs(X) ** 2 / (lam[o][None, :] - lam[~o][:, None]))
def hc1(L, N, u):
    best = None
    for j in range(N):
        r = spin_pt(L, 2 * math.pi * j / N, u, lambda lam: np.arange(L) < N)
        if r and (best is None or r[0] < best[0] - 1e-9 or (abs(r[0] - best[0]) < 1e-9 and r[1] < best[1])):
            best = r
    return best
L = 256; x = np.arange(L); row = []
for m in (32, 64):
    qq = 2 * math.pi * m / L; u = np.cos(qq * x)
    Ef, Ef2 = [2 * v for v in spin_pt(L, 0.0, u, lambda lam: lam < -1e-9)]; Eh, Eh2 = hc1(L, L // 2, u)
    cf = float(closed.subs(q, qq))
    row.append(f"q={qq:.3f}: Pi_hc/Pi_free {Eh2 / Ef2:.5f}, Pi_hc {Eh2 / L:+.6f} vs closed form {cf:+.6f}")
rng = np.random.default_rng(7); gaps = []
for Lb in (8, 12, 16):
    for _ in range(20):
        uu = rng.normal(0, 0.7, Lb); wb = np.exp((uu + np.roll(uu, -1)) / 2)
        Efree = 2 * np.linalg.eigvalsh(hspin(Lb, 0, wb))[:Lb // 2 - 1].sum()
        Ehc = min(np.linalg.eigvalsh(hspin(Lb, 2 * math.pi * j / (Lb // 2), wb))[:Lb // 2].sum() for j in range(Lb // 2))
        gaps.append((Efree / 2 - Ehc) / wb.max())
print(f"note (floating) 1D, L = 256, N = L/2 (twist pi): c0 ratio {Eh / Ef:.5f}; " + "; ".join(row)
      + f"; random rate fields on rings 8-16: 0 <= (E_free/2 - E_hc)/max w in [{min(gaps):.3f}, {max(gaps):.3f}] (bound 2)")
row = []
for Lb in (32, 128):
    xb = np.arange(Lb); ub = np.cos(2 * math.pi * xb / Lb); uf = np.cos(math.pi * xb / 2)
    E2s = hc1(Lb, Lb - 2, ub); E2f = hc1(Lb, Lb - 2, uf)
    row.append(f"L={Lb}: c0 {E2s[0] / Lb:+.4f}, Pi(2pi/L) x 8pi^2/L {E2s[1] / Lb * 8 * math.pi ** 2 / Lb:+.3f}, Pi(pi/2) {E2f[1] / Lb:+.5f}")
print("note (floating) 1D free-sea filling N = L-2 (two holes): " + "; ".join(row))
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL on a ring the axioms' records are exactly one spinless band with a coin-set twist (both exchange signs "
      "alike): their sea is half filled and carries exactly half the free sea's volume term and clock stiffness, same sign; at the "
      "free sea's filling exclusion leaves 2^d holes and the energy per site vanishes")
print("HIT: on a ring with the reduced walk, N records under exclusion are, for every rate field and either exchange sign, one "
      "spinless band whose wrap bond carries an eigenvalue of the coin-sequence rotation (one twist set for both signs); their sea "
      "is half filled, E = -1/sin(pi/L) (4 | L), 0 <= E_free/2 - E_hc <= 2 max w at every rate field, and Pi_hc(q) -> "
      "-cos^2(q/2) ln(sec+tan)(q/2)/(4 pi sin(q/2)) = Pi_free/2: volume term -1/pi, kappa = 1/(6 pi), half the free sea's, same sign.")
print("HIT: at the free sea's filling exclusion leaves h = 2^(even sides) empty sites (8 on even 3D tori) and |E| <= h d max w: the "
      "volume term vanishes per site; the executed smallest-mode gradient parts there are negative (ring 7 -0.157, ring 8 -0.070, "
      "3x3 -0.027 against the free +0.021, 0, +0.025), a few-hole response growing like L^3, not a stiffness; the 3x3 sea (N = 5) "
      "has +0.009, +0.012 (fermionic).")
