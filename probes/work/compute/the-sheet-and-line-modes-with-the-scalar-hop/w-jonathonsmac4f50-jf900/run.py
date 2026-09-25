#!/usr/bin/env python3
"""Block 86's walls in the alternation, with block 77's scalar hop a through the same bonds.

One-axis operators on a ring of L: h = (1/2i)(t T - T^dag t) (the walk's hop) and g = t T + T^dag t (the scalar hop, symbol 2 cos k at
t = 1), t_x on the bond x -> x+1: t_x = 1 + delta s_x (-1)^x (linear) or exp(delta s_x (-1)^x) (log rates, block 89), s_x = +1 without
walls, +1 / -1 on the two halves with walls (a weak-weak and a strong-strong wall).  H = sum_j sigma_j (x) h_j + a sum_j g_j (x) 1.
Exact part (sympy, 4^3): the staggered sign eps = (-1)^(x+y+z) anticommutes with H for every a (both terms hop one step), so the
spectrum is symmetric; at a = 0 the 16 zero modes (three crossing walls) split 8 + 8 by chirality: index 0, no protection.
Floating point: dense spectra on 8^3 and 12^3.
"""
import itertools, sys
import numpy as np
import sympy as sp

def out(s): print(s, flush=True)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]

def bonds(L, delta, walls, param):
    s = np.ones(L) if not walls else np.array([1.0] * (L // 2) + [-1.0] * (L - L // 2))
    alt = delta * s * (-1.0) ** np.arange(L)
    return (1 + alt) if param == "linear" else np.exp(alt)
def one_axis(L, t):
    h = np.zeros((L, L), complex); g = np.zeros((L, L))
    for x in range(L):
        y = (x + 1) % L
        h[x, y] += t[x] / 2j; h[y, x] += -t[x] / 2j       # (1/2i)(t T - T^dag t): row x picks t_x psi(x+1), row x+1 picks -t_x psi(x)/(2i)
        g[x, y] += t[x]; g[y, x] += t[x]
    return h, g
def full(L, delta, wall_axes, a, param):
    I = np.eye(L); I2 = np.eye(2)
    H = np.zeros((2 * L ** 3, 2 * L ** 3), complex)
    for j in range(3):
        h, g = one_axis(L, bonds(L, delta, j in wall_axes, param))
        ops = [I, I, I]; ops[j] = h
        H += np.kron(np.kron(np.kron(ops[0], ops[1]), ops[2]), SIG[j])
        ops = [I, I, I]; ops[j] = g
        H += a * np.kron(np.kron(np.kron(ops[0], ops[1]), ops[2]), I2)
    return H

# ------------------------------------------------------------------ exact: chiral symmetry and the index of the a = 0 zero modes
# (one-axis operators on the ring of four with rational amplitudes; the 3D statements follow by tensor products)
d4 = sp.Rational(3, 10)
def sp_one_axis(t):
    L = len(t); h = sp.zeros(L, L); g = sp.zeros(L, L)
    for x in range(L):
        y = (x + 1) % L
        h[x, y] += t[x] / (2 * sp.I); h[y, x] += -t[x] / (2 * sp.I); g[x, y] += t[x]; g[y, x] += t[x]
    return h, g
tw = [1 + d4 * s * (-1) ** x for x, s in enumerate([1, 1, -1, -1])]      # two walls: weak-weak and strong-strong
h1, g1 = sp_one_axis(tw)
e1 = sp.diag(*[(-1) ** x for x in range(4)])
anti1 = (e1 * h1 * e1 + h1 == sp.zeros(4, 4)) and (e1 * g1 * e1 + g1 == sp.zeros(4, 4))
out("X exact (ring of four, delta = 3/10, two walls): eps h eps = -h and eps g eps = -g (both hop one step); with eps = eps_x eps_y eps_z "
    "and sigma_j unchanged, every term of H = sum sigma_j h_j + a sum g_j anticommutes with eps: chiral symmetry for every a: %s" % ("PASS" if anti1 else "FAIL"))
ns1 = h1.nullspace()
par = []
for v in ns1:
    ev = [k for k in range(4) if v[k] != 0]
    par.append(sorted(set(k % 2 for k in ev)))
ok1 = len(ns1) == 2 and sorted(par) == [[0], [1]]
out("X exact: the one-axis h has exactly two zero modes, one on each sublattice (even: weak-weak wall, odd: strong-strong): %s (%s)" % ("PASS" if ok1 else "FAIL", par))
# the 16 three-axis zero modes are products (block 86 T4): chirality eps = product of the three sublattice signs; count
chir = [(-1) ** (px + py + pz) for px in (0, 1) for py in (0, 1) for pz in (0, 1) for coin in (0, 1)]
out("X exact: chiralities of the 16 product zero modes: %d with eps = +1, %d with eps = -1: index %d, so nothing protects them once a != 0"
    % (chir.count(1), chir.count(-1), sum(chir)))

# ------------------------------------------------------------------ numerics
def mass(delta, param): return delta if param == "linear" else np.sinh(delta)
out("N dense spectra; separable (a = 0) least |E|: bulk sqrt(3) m, sheet sqrt(2) m, line m, point 0, with m = delta (linear) or sinh(delta) (log)")
res = []
for L in (8, 12):
    for param in ("linear", "log"):
        for delta in (0.3, 0.5):
            m = mass(delta, param)
            for walls, name, sep in (((), "bulk", np.sqrt(3) * m), ((0,), "sheet (wall across x)", np.sqrt(2) * m), ((0, 1), "line (x and y)", m), ((0, 1, 2), "point (x, y, z)", 0.0)):
                row = []
                for a in (0.0, 0.1, 0.25):
                    E = np.linalg.eigvalsh(full(L, delta, walls, a, param))
                    ae = np.abs(E)
                    nz = int((ae < 1e-9).sum()); least = ae.min()
                    sym = np.allclose(np.sort(E), -np.sort(E)[::-1], atol=1e-9)
                    row.append((a, nz, least, sym))
                    res.append((L, param, delta, name, a, nz, least, sep, sym))
                out("N L=%-2d %-6s delta=%.1f %-22s separable %.4f | " % (L, param, delta, name, sep) + " | ".join(
                    "a=%.2f: zero modes %d, least |E| %.3e%s" % (a, nz, least, "" if sym else " (asym!)") for a, nz, least, sym in row))
ok0 = all(abs(r[6] - r[7]) < 1e-9 and (r[5] == (16 if r[3].startswith("point") else 0)) for r in res if r[4] == 0.0)
out("N a = 0 reproduces block 86 (least |E| = separable value, 16 zero modes at the point, none elsewhere) on 8^3 and 12^3: %s" % ok0)
splits = [(r[0], r[1], r[2], r[4], r[6]) for r in res if r[3].startswith("point") and r[4] > 0]
out("N point: least |E| with a != 0 (zero modes split): " + "; ".join("L=%d %s d=%.1f a=%.2f: %.2e" % s for s in splits))
# gap closing: bulk least |E| against a (the scalar hop's species offsets against the alternation mass)
for L in (8, 12):
    for param, delta in (("linear", 0.3), ("log", 0.3), ("linear", 0.5)):
        m = mass(delta, param); scan = []
        for a in np.arange(0.0, 0.205, 0.01):
            E = np.linalg.eigvalsh(full(L, delta, (), a, param)); scan.append((a, np.abs(E).min()))
        drop = next((a for a, e in scan if e < 0.5 * np.sqrt(3) * m), None)
        out("N gap scan L=%d %s delta=%.1f (bulk mass %.4f): least |E| by a: %s -> falls below half the bulk mass at a = %s"
            % (L, param, delta, np.sqrt(3) * m, " ".join("%.2f:%.3f" % t for t in scan[::2]), ("%.2f" % drop) if drop is not None else "none <= 0.2"))
print()
pt = [r for r in res if r[3].startswith("point") and r[4] > 0]
print("SUMMARY: the scalar hop keeps the chiral symmetry (exact) but the 16 point zero modes carry index 0 (8 + 8, exact), and a != 0 lifts them all; "
      "it also closes the bulk gap once its species offsets reach the alternation mass (gap scan), so least |E| at a = 0.1, 0.25 is a finite-size number: "
      "least |E| %s at L = 8 and %s at L = 12 (tunnelling between crossing points); sheet and line masses shift with a (table); a = 0 reproduces "
      "block 86 exactly" % (", ".join("%.1e" % r[6] for r in pt if r[0] == 8), ", ".join("%.1e" % r[6] for r in pt if r[0] == 12)))
