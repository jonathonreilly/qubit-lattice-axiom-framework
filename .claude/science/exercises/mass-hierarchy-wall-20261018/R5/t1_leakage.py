#!/usr/bin/env python3
"""R5 T1: leakage exponent of a protected logical mode under four readings of a rung.

Codes: bit-flip repetition code (n = 3, 5, 7; distance n against X) and the [[5,1,3]] code.
(a) Hamiltonian gap protection: ground-doublet splitting vs eps.
(b) coherent rung U = exp(-i eps sum h_j) followed by syndrome measurement + min-weight correction:
    logical transfer-matrix eigenvalue lambda = |lambda| e^{i theta}; theta (mass-like) and 1-|lambda| (width-like).
(c) Pauli rung (stochastic flips p) + decoder: theta == 0, 1-lambda vs p.
(d) passive: N Pauli rungs, one decode at the end.
"""
import itertools
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P1 = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def pauli(word):
    return kron(*[P1[c] for c in word])


def slope(xs, ys):
    lx, ly = np.log(xs), np.log(np.abs(ys))
    return np.polyfit(lx[:3], ly[:3], 1)[0]  # smallest-eps three points


# ---------------- repetition code ----------------
def rep_setup(n):
    stabs = [pauli('I' * i + 'ZZ' + 'I' * (n - i - 2)) for i in range(n - 1)]
    Xs = [pauli('I' * i + 'X' + 'I' * (n - i - 1)) for i in range(n)]
    v0 = np.zeros(2 ** n, complex); v0[0] = 1
    v1 = np.zeros(2 ** n, complex); v1[-1] = 1
    V = np.stack([v0, v1], axis=1)  # encoder 2^n x 2
    # syndrome classes: pairs {x, x^all}; correction = flip to nearest codeword
    corr = []
    for x in range(2 ** (n - 1)):  # representatives with top bit 0
        bits = [(x >> (n - 1 - k)) & 1 for k in range(n)]
        w = sum(bits)
        xc = x ^ (2 ** n - 1)
        Pm = np.zeros((2 ** n, 2 ** n), complex)
        Pm[x, x] = 1; Pm[xc, xc] = 1
        # minimum-weight error: x itself if w <= n//2, else its complement
        e = bits if w <= n // 2 else [1 - b for b in bits]
        C = kron(*[X if b else I2 for b in e])
        corr.append((Pm, C))
    return stabs, Xs, V, corr


def logical_ptm(channel, V):
    """channel acts on full density matrices; V encodes. Returns 3x3 Bloch transfer matrix."""
    paulis = [X, Y, Z]
    R = np.zeros((3, 3))
    for j, Pj in enumerate(paulis):
        rhoL = 0.5 * (I2 + Pj)
        out = channel(V @ rhoL @ V.conj().T)
        outL = V.conj().T @ out @ V
        for i, Pi in enumerate(paulis):
            R[i, j] = np.real(np.trace(Pi @ outL))
    return R


def spiral_pair(R):
    ev = np.linalg.eigvals(R)
    k = int(np.argmax(np.abs(ev.imag)))
    lam = ev[k]
    if abs(lam.imag) < 1e-300:
        # no complex pair: report the smallest real eigenvalue
        lam = ev[np.argmin(ev.real)]
    return lam, ev


print('=== repetition code (distance n against X) ===')
for n in (3, 5, 7):
    stabs, Xs, V, corr = rep_setup(n)
    H0 = -sum(stabs)
    HX = sum(Xs)
    # (a) Hamiltonian splitting
    epsA = np.array([0.02, 0.03, 0.045, 0.07, 0.1]) if n == 7 else np.array([0.005, 0.0075, 0.011, 0.02, 0.04])
    split = []
    for e in epsA:
        w = np.linalg.eigvalsh(H0 + e * HX)
        split.append(w[1] - w[0])
    print(f'n={n} (a) Hamiltonian splitting slope = {slope(epsA, np.array(split)):.3f} (pred {n}); '
          f'split/eps^n at smallest eps = {split[0]/epsA[0]**n:.3f}')
    # (b) coherent rung + decoder
    epsB = np.array([0.01, 0.015, 0.022, 0.035, 0.05]) if n < 7 else np.array([0.03, 0.045, 0.065, 0.09, 0.12])
    th, dmp = [], []
    for e in epsB:
        u1 = np.cos(e) * I2 - 1j * np.sin(e) * X
        U = kron(*([u1] * n))
        def ch(rho, U=U):
            r = U @ rho @ U.conj().T
            return sum(C @ Pm @ r @ Pm @ C.conj().T for Pm, C in corr)
        R = logical_ptm(ch, V)
        lam, ev = spiral_pair(R)
        th.append(abs(np.angle(lam))); dmp.append(1 - abs(lam))
    print(f'      (b) coherent+decoder: theta slope = {slope(epsB, np.array(th)):.3f} (pred {n}); '
          f'1-|lam| slope = {slope(epsB, np.array(dmp)):.3f} (pred {n+1}); theta/eps^n = {th[0]/epsB[0]**n:.3f}')
    # (c) Pauli rung + decoder, exact
    ps = np.array([1e-4, 2e-4, 4e-4, 1e-3, 3e-3]) if n < 7 else np.array([2e-3, 3e-3, 4.5e-3, 7e-3, 1e-2])
    t = (n + 1) // 2
    lamc, thc = [], []
    for p in ps:
        def chp(rho, p=p):
            r = rho
            for j in range(n):
                r = (1 - p) * r + p * Xs[j] @ r @ Xs[j]
            return sum(C @ Pm @ r @ Pm @ C.conj().T for Pm, C in corr)
        R = logical_ptm(chp, V)
        ev = np.linalg.eigvals(R)
        thc.append(np.max(np.abs(np.angle(ev[np.abs(ev) > 1e-12]))))
        lamc.append(1 - np.min(ev.real))
    print(f'      (c) Pauli+decoder: max |theta| = {max(thc):.1e} (pred 0); 1-lambda slope = '
          f'{slope(ps, np.array(lamc)):.3f} (pred {t})')
    # (d) passive accumulation: N rungs then one decode; analytic flip prob per qubit q_N
    p = 1e-3
    from math import comb
    out = []
    for N in (1, 10, 100):
        q = (1 - (1 - 2 * p) ** N) / 2
        PL = sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(t, n + 1))
        out.append((N, PL, PL / N))
    print('      (d) passive, p=1e-3: ' + '; '.join(f'N={N}: P_L={PL:.2e}, P_L/N={r:.2e}' for N, PL, r in out))

print('\n=== [[5,1,3]] code ===')
gens = ['XZZXI', 'IXZZX', 'XIXZZ', 'ZXIXZ']
G = [pauli(g) for g in gens]
Pc = np.eye(32, dtype=complex)
for g in G:
    Pc = Pc @ (np.eye(32) + g) / 2
Xb, Zb = pauli('XXXXX'), pauli('ZZZZZ')
w, vecs = np.linalg.eigh(Pc)
code = vecs[:, w > 0.5]
# logical |0>: +1 eigenvector of Zbar within code
zb = code.conj().T @ Zb @ code
wz, uz = np.linalg.eigh(zb)
v0 = code @ uz[:, np.argmax(wz)]
v1 = Xb @ v0
V5 = np.stack([v0, v1], axis=1)
# syndrome table: weight <= 1 Paulis
single = [('I' * 5)] + ['I' * j + c + 'I' * (4 - j) for j in range(5) for c in 'XYZ']
table = {}
for word in single:
    E = pauli(word)
    s = tuple(int(np.real(np.trace(E.conj().T @ g @ E @ g)) / 32 < 0) for g in G)
    table[s] = E
assert len(table) == 16
syn = []
for s in itertools.product([0, 1], repeat=4):
    Pm = np.eye(32, dtype=complex)
    for k, g in enumerate(G):
        Pm = Pm @ (np.eye(32) + (-1) ** s[k] * g) / 2
    syn.append((Pm, table[s].conj().T))
rng = np.random.default_rng(7)
dirs = rng.normal(size=(5, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
loc = [sum(dirs[j, a] * pauli('I' * j + 'XYZ'[a] + 'I' * (4 - j)) for a in range(3)) for j in range(5)]
H0 = -sum(G); HV = sum(loc)
epsA = np.array([0.003, 0.005, 0.008, 0.015, 0.03])
split = []
for e in epsA:
    ww = np.linalg.eigvalsh(H0 + e * HV)
    split.append(ww[1] - ww[0])
print(f'(a) Hamiltonian splitting slope = {slope(epsA, np.array(split)):.3f} (pred 3)')
epsB = np.array([0.005, 0.0075, 0.011, 0.02, 0.04])
th, dmp = [], []
for e in epsB:
    U = kron(*[np.cos(e) * I2 - 1j * np.sin(e) * (dirs[j, 0] * X + dirs[j, 1] * Y + dirs[j, 2] * Z) for j in range(5)])
    def ch(rho, U=U):
        r = U @ rho @ U.conj().T
        return sum(C @ Pm @ r @ Pm @ C.conj().T for Pm, C in syn)
    R = logical_ptm(ch, V5)
    ev = np.linalg.eigvals(R)
    th.append(np.max(np.abs(np.angle(ev)))); dmp.append(1 - np.min(np.abs(ev)))
print(f'(b) coherent+decoder: theta slope = {slope(epsB, np.array(th)):.3f} (pred 3); '
      f'1-|lam| slope = {slope(epsB, np.array(dmp)):.3f} (pred 4)')
ps = np.array([1e-4, 2e-4, 4e-4, 1e-3, 3e-3])
lamc, thc = [], []
for p in ps:
    def chd(rho, p=p):
        r = rho
        for j in range(5):
            ops = [pauli('I' * j + c + 'I' * (4 - j)) for c in 'XYZ']
            r = (1 - p) * r + (p / 3) * sum(o @ r @ o for o in ops)
        return sum(C @ Pm @ r @ Pm @ C.conj().T for Pm, C in syn)
    R = logical_ptm(chd, V5)
    ev = np.linalg.eigvals(R)
    thc.append(np.max(np.abs(np.angle(ev)))); lamc.append(1 - np.min(ev.real))
print(f'(c) depolarising+decoder: max |theta| = {max(thc):.1e} (pred 0); 1-lambda slope = {slope(ps, np.array(lamc)):.3f} (pred 2)')
