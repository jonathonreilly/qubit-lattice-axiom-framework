#!/usr/bin/env python3
"""Reviewer checks: (a) Lemma S on an own toy (non-TI, random U(1) gates);
(b) T acts on fixed-magnon-number sectors by pure site permutations (axis action
Q(R) = sgn(perm R) * |R|), and the full action reduces to pure permutations once
SU(2) symmetry is used.

(a) Ring of L=12 qubits. V = product of independent random U(1)-conserving 2-qubit
gates on bonds (0,1),(2,3),...; D = exp(i sum_x phi_x n_x n_{x+1}) with random phi_x.
U = V D V^dag freezes single magnons (D is trivial on <=1 magnon).  alpha(A)=U A U^dag
has range r=3 (V^dag spreads 1, D 1, V 1).  Check U|C u w> = (U|C>) (x) |w> and the
same for U^dag for every cluster C (|C|=2,3) and w with dist(w,C)>3; and that the
identity fails for many dist<=3 cases (discrimination)."""
import numpy as np, itertools
rng = np.random.default_rng(7)
PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + ('  ' + info if info else ''), flush=True)

L = 12
def apply2(psi, G, i, j):
    psi = psi.reshape([2] * L)
    psi = np.moveaxis(psi, (i, j), (0, 1)).reshape(4, -1)
    psi = (G @ psi).reshape([2, 2] + [2] * (L - 2))
    return np.moveaxis(psi, (0, 1), (i, j)).reshape(-1)
def rand_u1_gate():
    # block diag on |00>, span{|01>,|10>}, |11>
    G = np.zeros((4, 4), complex)
    G[0, 0] = np.exp(1j * rng.uniform(0, 6.3)); G[3, 3] = np.exp(1j * rng.uniform(0, 6.3))
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Q, _ = np.linalg.qr(A)
    G[1:3, 1:3] = Q
    return G
gates = [(rand_u1_gate(), i, (i + 1) % L) for i in range(0, L, 2)]
phis = rng.uniform(0, 6.3, size=L)
idx = np.arange(2 ** L)
bits = ((idx[:, None] >> (L - 1 - np.arange(L))[None, :]) & 1)   # site s = bit s (big endian)
Dphase = np.exp(1j * sum(phis[x] * bits[:, x] * bits[:, (x + 1) % L] for x in range(L)))
def V(psi):
    for G, i, j in gates: psi = apply2(psi, G, i, j)
    return psi
def Vd(psi):
    for G, i, j in gates: psi = apply2(psi, G.conj().T, i, j)
    return psi
def U(psi): return V(Dphase * Vd(psi))
def Ud(psi): return V(np.conj(Dphase) * Vd(psi))
def ket(C):
    v = np.zeros(2 ** L, complex); v[sum(1 << (L - 1 - s) for s in C)] = 1; return v
def d(a, b): return min(abs(a - b), L - abs(a - b))
def raise_at(psi, w):  # sigma^+_w on psi (assumes no magnon at w in support)
    out = np.zeros_like(psi); m = 1 << (L - 1 - w)
    sel = (idx & m) == 0; out[idx[sel] | m] = psi[sel]; return out
# singles frozen
sing = max(abs(abs(np.vdot(ket([x]), U(ket([x])))) - 1) for x in range(L))
check('single magnons frozen', sing < 1e-12, '%.1e' % sing)
mov = max(1 - abs(np.vdot(ket([x, y]), U(ket([x, y])))) for x in range(L) for y in range(x + 1, L))
check('pairs move (toy is non-trivial)', mov > 1e-2, 'max 1-|<xy|U|xy>| = %.3f' % mov)
far_ok = far_n = near_bad = near_n = 0
for k in (2, 3):
    for C in itertools.combinations(range(L), k):
        if k == 3 and rng.random() > 0.3: continue
        UC = U(ket(C)); UdC = Ud(ket(C))
        for w in range(L):
            if w in C: continue
            dw = min(d(w, c) for c in C)
            e1 = np.linalg.norm(U(ket(C + (w,))) - raise_at(UC, w))
            e2 = np.linalg.norm(Ud(ket(C + (w,))) - raise_at(UdC, w))
            if dw > 3:
                far_n += 1; far_ok += (e1 < 1e-10 and e2 < 1e-10)
            else:
                near_n += 1; near_bad += (e1 > 1e-6)
check('Lemma S (U and U^dag) holds for every dist(w,C) > r=3', far_ok == far_n and far_n > 0, '%d/%d' % (far_ok, far_n))
check('identity fails for many dist <= 3 cases (test discriminates)', near_bad > 50, '%d/%d fail' % (near_bad, near_n))

# (b) phases of T under the axis action
def parity(p): return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2
Tg = [(p, sg) for p in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)
      if parity(p) == 0 and sum(s < 0 for s in sg) % 2 == 0]
n = np.ones(3) / np.sqrt(3)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
sn = (sx + sy + sz) / np.sqrt(3)
ev, P = np.linalg.eigh(sn)       # columns: n-basis (|down_n>, |up_n>)
def su2_from_so3(Q):
    # find u with u sigma_j u^dag = sum_i Q_ij sigma_i (solve via averaging)
    S = [sx, sy, sz]
    M = sum(sum(Q[i, j] * S[i] for i in range(3)) @ np.eye(2) @ S[j] for j in range(3)) + np.eye(2)
    # u proportional to 1 + sum_j (Q sigma)_j sigma_j  (standard formula)
    u = M / np.sqrt(abs(np.linalg.det(M))) if abs(np.linalg.det(M)) > 1e-9 else None
    return u
allok = True; maxoff = 0
for p, sg in Tg:
    Rm = np.zeros((3, 3))
    for i in range(3): Rm[i, p[i]] = sg[i]
    Q = (-1) ** parity(p) * np.abs(Rm)          # axis action
    assert np.allclose(Q @ n, n)                # fixes n: vacuum direction preserved
    u = su2_from_so3(Q)
    if u is None:   # Q = rotation by pi (not in T image except identity); handle identity
        u = np.eye(2)
    for j, S in enumerate([sx, sy, sz]):
        assert np.allclose(u @ S @ u.conj().T, sum(Q[i, j] * [sx, sy, sz][i] for i in range(3)))
    un = P.conj().T @ u @ P                     # u in the n-basis
    maxoff = max(maxoff, abs(un[0, 1]), abs(un[1, 0]))
check('T under the axis action acts on-site by rotations about n (diagonal in n-basis)', maxoff < 1e-12,
      'max offdiag %.1e; hence phase depends only on magnon number -> pure permutation within each sector' % maxoff)
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
