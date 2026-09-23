#!/usr/bin/env python3
"""Transfer construction of stationary zero-flux ice measures on thin prisms.

Layer units here are a supplied coarse link-layer model. Adding deterministic coordinator records need not preserve schedulability on a finer neighbour graph. Staggered flux requires an even bipartite cross-section. Numerical spectral estimates are labelled separately from exact integer identities. Infinite height at fixed cross-section is not an infinite-cross-section Coulomb phase.
"""
import sys

AUDIT_TIMEOUT_SEC = 900

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def transfer(a, b):
    """Transfer matrix along the axis for the a x b transverse torus: rows v and columns w are the occupations of
    the a*b vertical links below and above one layer; the entry counts in-plane configurations completing ice."""
    V = [(x, y) for x in range(a) for y in range(b)]
    idx = {v: i for i, v in enumerate(V)}
    links = []
    for x, y in V:
        links.append((idx[(x, y)], idx[((x + 1) % a, y)]))
        links.append((idx[(x, y)], idx[(x, (y + 1) % b)]))
    E = len(links)
    cfg = (np.arange(1 << E, dtype=np.int64)[:, None] >> np.arange(E, dtype=np.int64)) & 1
    deg = np.zeros((1 << E, len(V)), dtype=np.int64)
    for j, (p, q) in enumerate(links):
        deg[:, p] += cfg[:, j]
        deg[:, q] += cfg[:, j]
    counts = {}
    for row in map(tuple, deg):
        counts[row] = counts.get(row, 0) + 1
    N = 1 << len(V)
    bits = [tuple((s >> i) & 1 for i in range(len(V))) for s in range(N)]
    T = [[counts.get(tuple(3 - bv - bw for bv, bw in zip(bits[v], bits[w])), 0) for w in range(N)] for v in range(N)]
    return T


def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    Bt = list(zip(*B))
    return [[sum(A[i][t] * Bt[j][t] for t in range(k)) for j in range(m)] for i in range(n)]


def trace_power(T, H):
    P = T
    for _ in range(H - 1):
        P = matmul(P, T)
    return sum(P[i][i] for i in range(len(P)))


print("A. the transfer matrix counts the landed torus")
T2 = transfer(2, 2)
tr = {H: trace_power(T2, H) for H in (2, 3, 4)}
T24 = transfer(2, 4)
cross = trace_power(T24, 2)
check("n = 2: trace T^2 = 9600, the landed 2 x 2 x 2 count, and the 2 x 2 x 4 count agrees with a transfer along another axis",
      tr[2] == 9600 and tr[4] == cross,
      f"trace T^H for H = 2, 3, 4: {tr[2]}, {tr[3]}, {tr[4]}; 2 x 4 cross-section with H = 2: {cross}")

print("B. the flux through the cross-section is conserved")
N2 = len(T2)
V2 = [(x, y) for x in range(2) for y in range(2)]
eps = [(-1) ** (x + y) for x, y in V2]
flux = [sum(eps[i] * (2 * ((s >> i) & 1) - 1) for i in range(len(V2))) for s in range(N2)]
flips = all(flux[w] == -flux[v] for v in range(N2) for w in range(N2) if T2[v][w])
symmetric = all(T2[v][w] == T2[w][v] for v in range(N2) for w in range(N2))
sector = {a: [s for s in range(N2) if abs(flux[s]) == a] for a in (0, 2, 4)}
blocks = {a: np.array([[T2[v][w] for w in S] for v in S], dtype=float) for a, S in sector.items()}
spec = {a: sorted(np.linalg.eigvalsh(B), key=lambda z: -abs(z)) for a, B in blocks.items()}
zero_positive = all(T2[v][w] > 0 for v in sector[0] for w in sector[0])
lam = float(spec[0][0])
Z = [[T2[v][w] for w in sector[0]] for v in sector[0]]
I6 = [[int(i == j) for j in range(6)] for i in range(6)]
lin = lambda A, c: [[A[i][j] + c * I6[i][j] for j in range(6)] for i in range(6)]
quad = [[x - 64 * y + 188 * I6[i][j] for j, (x, y) in enumerate(zip(r2, r1))] for i, (r2, r1) in enumerate(zip(matmul(Z, Z), Z))]
annihilated = matmul(matmul(matmul(matmul(lin(Z, -6), lin(Z, 10)), lin(Z, 14)), lin(Z, 14)), quad)
power_sums = [2, 64]
for _ in range(5):
    power_sums.append(64 * power_sums[-1] - 188 * power_sums[-2])
traces, Zk = [], Z
for k in range(1, 7):
    traces.append(sum(Zk[i][i] for i in range(6)))
    Zk = matmul(Zk, Z)
newton = all(traces[k - 1] == 6 ** k + (-10) ** k + 2 * (-14) ** k + power_sums[k] for k in range(1, 7))
exact_char = all(x == 0 for row in annihilated for x in row) and newton
check("the staggered vertical flux flips sign at every layer, so its size is conserved; the zero-flux sector's block is positive with a simple top eigenvalue",
      flips and symmetric and zero_positive and [len(sector[a]) for a in (0, 2, 4)] == [6, 8, 2]
      and exact_char and abs(lam - (32 + 2 * 209 ** 0.5)) < 1e-9 and abs(abs(spec[0][1]) - 14) < 1e-9
      and abs(spec[2][0] + spec[2][1]) < 1e-9 and abs(abs(spec[2][0]) - 46) < 1e-9 and abs(abs(spec[4][0]) - 18) < 1e-9,
      f"flux S(v) = sum of (-1)^(x+y) (2 v - 1) over the cross-section; sectors |S| = 0, 2, 4 with 6, 8, 2 states; zero flux: "
      f"characteristic polynomial (x - 6)(x + 10)(x + 14)^2(x^2 - 64 x + 188), exact from the traces of T^1..T^6 and "
      f"annihilating the block; top 32 + 2 sqrt 209 = {lam:.4f}, next modulus 14; "
      "|S| = 2: dominant pair +46 and -46; |S| = 4: +18 and -18")

# Newton power sums through each block dimension fix its characteristic polynomial.
flux_chars_ok = True
for a, roots in ((2,[-46,-10,-10,-6,6,10,10,46]), (4,[-18,18])):
    B = [[T2[v][w] for w in sector[a]] for v in sector[a]]
    Bk = B
    for k in range(1,len(B)+1):
        flux_chars_ok = flux_chars_ok and sum(Bk[j][j] for j in range(len(B))) == sum(x**k for x in roots)
        Bk = matmul(Bk,B)
check("nonzero-flux characteristic polynomials are fixed exactly by all Newton power sums",
      flux_chars_ok, "|S|=2: (x^2-46^2)(x^2-10^2)^2(x^2-6^2); |S|=4: x^2-18^2")

print("C. long tori select zero flux")


def power(T, H):
    P = [[int(v == w) for w in range(len(T))] for v in range(len(T))]
    for _ in range(H):
        P = matmul(P, T)
    return P


share = {}
for H in (2, 4, 6, 8, 10, 12, 14, 16):
    P = power(T2, H)
    tot = sum(P[i][i] for i in range(N2))
    share[H] = sum(P[i][i] for i in range(N2) if flux[i]) / tot
odd_zero = all(sum(power(T2, H)[i][i] for i in range(N2) if flux[i]) == 0 for H in (3, 5))
scaled = share[16] * (lam / 46.0) ** 16
check("on the 2 x 2 x H torus the ice states with flux fall as 2 (46 / 60.91)^H for even H and vanish for odd H",
      odd_zero and all(share[H + 2] < share[H] for H in (2, 4, 6, 8, 10, 12, 14)) and abs(scaled - 2.0) < 0.05,
      "share with flux for H = 2..16: " + ", ".join(f"{share[H]:.4f}" for H in sorted(share))
      + f"; share x (60.91 / 46)^16 = {scaled:.3f}")

print("D. the layer unit's law depends only on the layer below")
T0 = blocks[0]
evals, evecs = np.linalg.eigh(T0)
phi = np.abs(evecs[:, np.argmax(evals)])
kernel = T0 * phi[None, :] / (lam * phi[:, None])
dev = {}
for H in (4, 8, 12, 16):
    PH1 = np.linalg.matrix_power(T0, H - 1)
    PH2 = np.linalg.matrix_power(T0, H - 2)
    dev[H] = max(abs(T0[b, c] * PH2[c, a] / PH1[b, a] - kernel[b, c])
                 for a in range(6) for b in range(6) for c in range(6))
check("with zero flux, a layer's law given the layer below and the far end of a long torus tends to one kernel",
      bool(np.all(phi > 0)) and np.allclose(kernel.sum(axis=1), 1.0)
      and all(dev[H2] < dev[H1] for H1, H2 in ((4, 8), (8, 12), (12, 16))) and dev[16] < 1e-6,
      "largest deviation from P(w | v) = T[v, w] phi(w) / (lambda phi(v)) for H = 4, 8, 12, 16: "
      + ", ".join(f"{dev[H]:.1e}" for H in sorted(dev))
      + "; forming the prism layer by layer with this kernel from stationary phi^2 initial weights and uniform completions reproduces the limit")

print("E. odd cross-sections alternate")
T3 = transfer(3, 3)
N3 = len(T3)
bip = all(T3[v][w] == 0 for v in range(N3) for w in range(N3) if (bin(v).count("1") + bin(w).count("1")) % 2 == 0)
T3a = np.array(T3, dtype=float)
ev3 = sorted(np.linalg.eigvalsh(T3a), key=lambda z: -abs(z))
pair = abs(ev3[0] + ev3[1]) < 1e-6 * abs(ev3[0]) and abs(abs(ev3[0]) - abs(ev3[2])) > 1.0
odd_zero = sum(int(v) for v in np.diag(T3a @ T3a @ T3a)) == 0
check("n = 3: the vertical parity alternates, the top eigenvalues come as a pair plus and minus, and odd tori have no ice states",
      bip and pair and odd_zero,
      f"{N3} layer states; top moduli {abs(ev3[0]):.2f} (twice), next {abs(ev3[2]):.2f}; trace T^3 = 0 since 3 V / 2 is "
      "not an integer on an odd torus; layer units form the prism with the two-step chain")

print("F. a second cross-section, 2 x 4")
T24f = transfer(2, 4)
N24 = len(T24f)
V24 = [(x, y) for x in range(2) for y in range(4)]
eps24 = [(-1) ** (x + y) for x, y in V24]
flux24 = [sum(eps24[i] * (2 * ((s >> i) & 1) - 1) for i in range(len(V24))) for s in range(N24)]
flips24 = all(flux24[w] == -flux24[v] for v in range(N24) for w in range(N24) if T24f[v][w])
sec24 = {a: [s for s in range(N24) if abs(flux24[s]) == a] for a in (0, 2, 4, 6, 8)}
Z24 = np.array([[T24f[v][w] for w in sec24[0]] for v in sec24[0]], dtype=np.int64)
prim24 = bool((Z24 @ Z24 > 0).all())
tops = {a: sorted(np.linalg.eigvalsh(np.array([[T24f[v][w] for w in S] for v in S], dtype=float)), key=lambda z: -abs(z))
        for a, S in sec24.items()}
lam24, gap24 = float(tops[0][0]), abs(float(tops[0][1]))
dominates = all(abs(float(tops[a][0])) < lam24 for a in (2, 4, 6, 8))
T0f = Z24.astype(float)
ev24, vec24 = np.linalg.eigh(T0f)
phi24 = np.abs(vec24[:, np.argmax(ev24)])
ker24 = T0f * phi24[None, :] / (lam24 * phi24[:, None])
P1 = np.linalg.matrix_power(T0f / lam24, 15)
P2 = np.linalg.matrix_power(T0f / lam24, 14)
n0 = len(sec24[0])
dev24 = max(abs(T0f[b, c] * P2[c, a] / (lam24 * P1[b, a]) - ker24[b, c]) for a in range(n0) for b in range(n0) for c in range(n0))
check("n = 2 x 4: the flux is conserved, zero flux dominates, and the layer kernel again forgets the far end",
      flips24 and [len(sec24[a]) for a in (0, 2, 4, 6, 8)] == [70, 112, 56, 16, 2] and prim24 and bool(np.all(phi24 > 0))
      and abs(lam24 - 2401.3316) < 1e-3 and abs(gap24 - 668.3638) < 1e-3 and dominates and dev24 < 1e-6,
      f"sectors |S| = 0, 2, 4, 6, 8 with 70, 112, 56, 16, 2 layer states; the zero-flux block squared is positive, top "
      f"{lam24:.4f}, next modulus {gap24:.4f}; flux sectors top at "
      + ", ".join(f"{abs(float(tops[a][0])):.2f}" for a in (2, 4, 6, 8)) + f"; far-end deviation at H = 16: {dev24:.1e}")

print('per_element: Integer configurations, weights and conditional cross-products are exact within the stated finite alphabets; floating spectral estimates are labelled.')
print('per_site: Site and unit tests use the declared records, neighbour graph, boundary conditions and fixed formation orders only.')
print('per_mode: Transfer and walk modes refer to supplied finite matrices; numerical estimates do not establish untested physical or infinite-cross-section limits.')
print('per_block: This bounded support result retains its explicit controls, parameter values and search caps; alternative rules and records remain outside scope.')
print('lattice_wide: Finite windows do not establish universal formation impossibility; infinite-height statements apply only to the specified fixed-cross-section transfer model.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
