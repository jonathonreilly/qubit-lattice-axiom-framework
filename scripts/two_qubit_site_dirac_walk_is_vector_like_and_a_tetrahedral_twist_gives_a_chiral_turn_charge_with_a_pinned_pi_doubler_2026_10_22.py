AUDIT_INPUT_PATHS = ('docs/TWO_QUBIT_SITE_DIRAC_WALK_IS_VECTOR_LIKE_AND_A_TETRAHEDRAL_TWIST_GIVES_A_CHIRAL_TURN_CHARGE_WITH_A_PINNED_PI_DOUBLER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Two-qubit-site cubic walks versus the turn-charge / mirror-separation clash.

Site C^2 (flavor tau) (x) C^2 (spin sigma). Walks U = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma.
Part A: the landed O-covariant member (coin 1 (x) D(R), b* of the 2026-10-16 note): light content,
chirality, mass freedom, turn charge.  Part B: the tetrahedral-twisted coin rho(R) (x) D(R), rho = Z3
character of T on the flavor qubit: the exact nearest-neighbour member f = sum c/3,
h1 - i h2 = (sqrt2/3) E1, g = s/sqrt3; its nodes, chiralities and turn charges.
Free bands only. Self-contained, deterministic (seed 20261022).
"""
import numpy as np

AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(20261022)
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(('PASS ' if ok else 'FAIL ') + name + (' [' + detail + ']' if detail else ''))


I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
kr = np.kron
w = np.exp(2j * np.pi / 3)


def su2(axis, ang):
    n = np.array(axis, float) / np.linalg.norm(axis)
    return np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sum(n[i] * SIG[i] for i in range(3))


def rot(axis, ang):
    n = np.array(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


C3 = (rot([1, 1, 1], 2 * np.pi / 3), su2([1, 1, 1], 2 * np.pi / 3))
C2x = (rot([1, 0, 0], np.pi), su2([1, 0, 0], np.pi))
C4z = (rot([0, 0, 1], np.pi / 2), su2([0, 0, 1], np.pi / 2))
dok = max(np.abs(D @ SIG[a] @ D.conj().T - sum(R[b, a] * SIG[b] for b in range(3))).max()
          for R, D in (C3, C2x, C4z) for a in range(3))
check('A0 D(R) sigma_a D(R)^+ = sum_b R_ba sigma_b for the turn, a 2-fold and a 4-fold', dok < 1e-14, '%.0e' % dok)


def phi(k):
    c = np.cos(k)
    return np.array([1., c.sum(), c[0] * c[1] + c[1] * c[2] + c[2] * c[0], c.prod()])


def vecs(k):
    c, s = np.cos(k), np.sin(k)
    return [s, np.array([s[a] * (c[(a + 1) % 3] + c[(a + 2) % 3]) for a in range(3)]),
            np.array([s[a] * c[(a + 1) % 3] * c[(a + 2) % 3] for a in range(3)])]


def walk(f, h1, h2, g):
    return (f * np.eye(4) + 1j * (h1 * kr(sx, I2) + h2 * kr(sy, I2))
            + 1j * sum(g[a] * kr(sz, SIG[a]) for a in range(3)))


def weyl(node, Uf):
    """chirality of each tau3 block at a node from H_a = i U0^-1 dU/dk_a (U = U0 e^{-iH})"""
    U0 = Uf(node); out = {}
    e = 1e-5
    H = [1j * np.linalg.inv(U0) @ (Uf(node + e * np.eye(3)[a]) - Uf(node - e * np.eye(3)[a])) / (2 * e) for a in range(3)]
    for tz, idx in ((+1, [0, 1]), (-1, [2, 3])):
        x = sum(np.trace(H[a][np.ix_(idx, idx)] @ SIG[a]).real for a in range(3)) / 6
        out[tz] = int(np.sign(x))
    return out


# ---------------- Part A: the landed O-covariant member b* ----------------
def Gram(b0, b1, b2):
    G = np.zeros((4, 4))
    G[0, 0] = 1 - 3 * b0**2; G[0, 1] = -2 * b0 * b1; G[0, 2] = b1**2 - b0**2 - b0 * b2
    G[0, 3] = -3 * b1 * (b0 - b2); G[1, 1] = b0**2 - 2 * b1**2; G[1, 2] = b1 * (b0 - b2)
    G[1, 3] = b0 * b2 - b1**2 + b2**2; G[2, 2] = 2 * b1**2 - b2**2; G[2, 3] = 2 * b1 * b2; G[3, 3] = 3 * b2**2
    return G + np.triu(G, 1).T


b0, b2 = 11 / 30, 3 / 20
us = np.linspace(0.01, 0.09, 5)
coef = np.polyfit(us, [np.linalg.det(Gram(b0, np.sqrt(u), b2)) for u in us], 4)
roots = sorted(r.real for r in np.roots(coef) if abs(r.imag) < 1e-12 and r.real > 0)
ustar = roots[0]
b = (b0, np.sqrt(ustar), b2)
G = Gram(*b)
ev, V = np.linalg.eigh(G)
check('A1 G(b*) is PSD of rank 3 (u* = %.7f)' % ustar, abs(ev[0]) < 1e-12 and ev[1] > 1e-3,
      'eig ' + ' '.join('%.4f' % e for e in ev))
F = (np.sqrt(ev[1:])[:, None] * V[:, 1:].T)
F0 = F @ phi(np.zeros(3))
v = F0 - np.array([1, 0, 0]); Q = np.eye(3) - 2 * np.outer(v, v) / (v @ v) if v @ v > 1e-20 else np.eye(3)
F = Q @ F
spd = b[0] + 2 * b[1] + b[2]


def UA(k, Fm=F):
    f, h1, h2 = Fm @ phi(k)
    g = sum(b[j] * vecs(k)[j] for j in range(3))
    return walk(f, h1, h2, g)


ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(40)]
uerr = max(np.abs(UA(k) @ UA(k).conj().T - np.eye(4)).max() for k in ks)
deg = max(np.abs(np.diff(np.sort(np.angle(np.linalg.eigvals(UA(k)))))[[0, 2]]).max() for k in ks)
check('A2 unitary; every band doubly degenerate (X^2 = scalar), so every node is a 4-fold Dirac point',
      uerr < 1e-13 and deg < 1e-12, 'unit %.0e, split %.0e' % (uerr, deg))
cov = max(np.abs(kr(I2, D) @ UA(k) @ kr(I2, D).conj().T - UA(R @ k)).max() for R, D in (C3, C2x, C4z) for k in ks)
check('A3 exactly O-covariant with coin 1 (x) D(R)', cov < 1e-13, '%.0e' % cov)
n = 24
gr = 2 * np.pi * np.arange(n) / n
mind = 9.
for i in gr:
    for j in gr:
        for l in gr:
            if i == j == l == 0:
                continue
            mind = min(mind, 1 - abs(F[0] @ phi(np.array([i, j, l]))))
check('A4 the only node on a 24^3 grid is k = 0 (1-|f| > 0 elsewhere)', mind > 1e-3, 'min 1-|f| = %.3f' % mind)
kk = np.array([0, 0, 1e-4])
lin = (UA(kk) - UA(-kk)) / (2e-4)
chA = weyl(np.zeros(3), UA)
check('A5 at k = 0: linear part i s tau3 (x) sigma.k; chirality tau3=+1 -> %+d, tau3=-1 -> %+d: L and R Weyls at the SAME momentum' % (chA[1], chA[-1]),
      np.abs(lin - 1j * spd * kr(sz, sz)).max() < 1e-6 and chA[1] == -chA[-1], 's = %.4f' % spd)
m = 0.3
Fm = np.array([[np.cos(m), -np.sin(m), 0], [np.sin(m), np.cos(m), 0], [0, 0, 1]]) @ F
covm = max(np.abs(kr(I2, D) @ UA(k, Fm) @ kr(I2, D).conj().T - UA(R @ k, Fm)).max() for R, D in (C3, C2x, C4z) for k in ks)
gap = np.abs(np.angle(np.linalg.eigvals(UA(np.zeros(3), Fm)))).min()
check('A6 an O-invariant mass (h1(0) = sin m) is allowed: covariant, gap at k=0 equals m (vector-like light Dirac)',
      covm < 1e-13 and abs(gap - m) < 1e-12, 'gap %.3f' % gap)
W3 = kr(I2, C3[1])
dets = [np.linalg.det(W3[np.ix_(idx, idx)]) for idx in ([0, 1], [2, 3])]
check('A7 turn charge: det(W_turn | tau3 block) = 1 on both blocks, so q_L = q_R = 0',
      max(abs(d - 1) for d in dets) < 1e-14)
rho = np.diag([w.conjugate(), w])
tw = max(np.abs(kr(rho, C3[1]) @ UA(k) @ kr(rho, C3[1]).conj().T - UA(C3[0] @ k)).max() for k in ks)
check('A8 the Z3-twisted turn rho (x) D is NOT a symmetry of the O member (invariant h breaks it)', tw > 1e-2,
      'residual %.2f' % tw)

# ---------------- Part B: tetrahedral-twisted nearest-neighbour walk ----------------
def UB(k):
    c, s = np.cos(k), np.sin(k)
    hm = np.sqrt(2) / 3 * (c[0] + w * c[1] + w.conjugate() * c[2])      # hm = h1 - i h2
    return walk(c.sum() / 3, hm.real, -hm.imag, s / np.sqrt(3))


ub = max(np.abs(UB(k) @ UB(k).conj().T - np.eye(4)).max() for k in ks)
check('B1 NN walk f = sum c/3, h1 - i h2 = (sqrt2/3)(c1 + w c2 + wbar c3), g = s/sqrt3 is exactly unitary', ub < 1e-14,
      '%.0e' % ub)
WB = lambda R, D, r: kr(r, D)
grp = [(C3[0], C3[1], rho), (C2x[0], C2x[1], I2)]
cB = max(np.abs(WB(*gg) @ UB(k) @ WB(*gg).conj().T - UB(gg[0] @ k)).max() for gg in grp for k in ks)
check('B2 T-covariant (turn with rho = diag(wbar, w) on flavor, 2-folds untwisted)', cB < 1e-14, '%.0e' % cB)
c4 = min(max(np.abs(kr(r, C4z[1]) @ UB(k) @ kr(r, C4z[1]).conj().T - UB(C4z[0] @ k)).max() for k in ks)
         for r in (I2, sx, sy, sz, rho))
u3 = max(np.abs(kr(I2, C3[1]) @ UB(k) @ kr(I2, C3[1]).conj().T - UB(C3[0] @ k)).max() for k in ks)
check('B3 neither the untwisted turn nor any tested 4-fold coin is a symmetry (T, not O)', c4 > 1e-2 and u3 > 1e-2,
      '4-fold %.2f, untwisted turn %.2f' % (c4, u3))
hd = max(abs(np.cos(t) * (1 + w + w.conjugate())) for t in np.linspace(0, np.pi, 9))
check('B4 h vanishes on the whole body diagonal (1 + w + wbar = 0): mass at k=0 forbidden, R node forced', hd < 1e-15)
fg = [abs(np.cos(np.array([i, j, l])).sum() / 3) for i in gr for j in gr for l in gr]
nodes = [(i, j, l) for i in gr for j in gr for l in gr if abs(abs(np.cos(np.array([i, j, l])).sum() / 3) - 1) < 1e-12]
check('B5 nodes (|f| = 1) on the 24^3 grid: exactly k = 0 (f=+1, quasienergy 0) and R = pi(1,1,1) (f=-1, quasienergy pi)',
      len(nodes) == 2 and abs(np.cos(np.pi) * 1 + 1) < 1e-15, 'next |f| = %.3f' % sorted(fg)[-3])


ch0, chR = weyl(np.zeros(3), UB), weyl(np.pi * np.ones(3), UB)
check('B6 chirality per tau3 block is the SAME at both nodes: tau3=+1 -> %+d,%+d ; tau3=-1 -> %+d,%+d'
      % (ch0[1], chR[1], ch0[-1], chR[-1]), ch0 == chR and ch0[1] == -ch0[-1])
dB = {tz: np.linalg.det(kr(rho, C3[1])[np.ix_(idx, idx)]) for tz, idx in ((+1, [0, 1]), (-1, [2, 3]))}
q = {tz: [qq for qq in range(3) if abs(w**(2 * qq) - dB[tz]) < 1e-12][0] for tz in dB}
check('B7 turn charge (det = w^2q): tau3=+1 block q = %d, tau3=-1 block q = %d; L and R differ, both nonzero'
      % (q[1], q[-1]), q[1] != q[-1] and 0 not in q.values())
# Schur: turn+2-fold invariant on-site 4x4 operators are tau3-block diagonal (no L-R bilinear at a node)
Mr = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
gens = [kr(rho, C3[1]), kr(I2, C2x[1]), kr(I2, su2([0, 1, 0], np.pi))]
els = [np.eye(4)]
for _ in range(4):
    els = els + [g @ e for g in gens for e in els]
    uniq = []
    for e in els:
        if not any(np.abs(e - u).max() < 1e-9 for u in uniq):
            uniq.append(e)
    els = uniq
Mav = sum(e @ Mr @ e.conj().T for e in els) / len(els)
off = np.abs(Mav[:2, 2:]).max()
diag_sc = max(np.abs(Mav[:2, :2] - Mav[0, 0] * I2).max(), np.abs(Mav[2:, 2:] - Mav[2, 2] * I2).max())
check('B8 every T-invariant on-site bilinear (%d-element group average) is tau3-diagonal and scalar per block:'
      ' no light-mirror mass at either node, only node shifts' % len(els), off < 1e-12 and diag_sc < 1e-12,
      'off %.0e' % off)
P = kr(np.diag([1., 0]), I2)
leak = [np.abs(P @ UB(np.array([0, 0.6, 0.8]) * t) - UB(np.array([0, 0.6, 0.8]) * t) @ P).max() for t in (0.02, 0.04)]
check('B9 on-site chirality filter (1+tau3)/2 commutes with the walk up to O(k^2) (h ~ k^2; glide filter leaked O(k))',
      3.9 < leak[1] / leak[0] < 4.1, 'leak %.1e, %.1e' % tuple(leak))
filt = [(1 - np.cos(kk).sum() / 3) / 2 for kk in (np.zeros(3), np.pi * np.ones(3))]
check('B10 momentum filter (1 - sum c/3)/2 is 0 at k=0 and 1 at R: it separates the two NODES, not L from R',
      filt == [0.0, 1.0])
tL = [tz for tz in (1, -1) if ch0[tz] < 0][0]
check('B11 Weyl census (chirality -1 = L): L at 0 and at R both q=%d, R at 0 and at R both q=%d; the R node is a'
      ' pi-mode doubler pair pinned at a T-fixed point with q_L != q_R, so no small T-keeping term gaps it'
      % (q[tL], q[-tL]), ch0 == chR and q[tL] != q[-tL])
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
