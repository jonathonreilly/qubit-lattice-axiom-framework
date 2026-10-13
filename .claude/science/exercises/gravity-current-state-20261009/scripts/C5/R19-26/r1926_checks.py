"""R19-26 checks of the re-placed kernel (lib1926.patch()), with the R19-16 kernel as control.  Usage: r1926_checks.py r
 C1  W1 (physical block, lib199.w1_resid, and an independent SVD transverse frame as in the referee's script):
     referee seam point, exact-zero legs, 3000 dense random pairs (hard/hard, soft legs, corner annulus), cut points.
 C2  cut continuity with the placement factor: 300 random cut crossings per axis l (q_l -> +-pi, k1, k2 interior),
     incl. soft k1 or soft k2; max PLACE jump on the full block and the physical block, at eps = 1e-7 and 1e-9.
 C3  BZ-face continuity (twist T_l, R19-9 r199_fiber_check.py's test) at 1e-9 from the face, 120 pairs.
 C4  line scans (801 points, step 1e-4) across the cut: max second difference of the placement-restored kernel.
 C5  cubic covariance (R19-9 r199_cov.py's test, 300 pairs per rotation)."""
import sys, numpy as np, lib1926 as R
L = R.L
r = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
rng = np.random.default_rng(192626)

def tframe(k):
    s = L.sig(k); _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True); e = vh[1:].T
    Q = np.zeros((6, 4)); Q[:3, :2] = e; Q[3:, 2:] = e; return Q

def w1_both(k1, k2):
    M = L.glued(k1, k2, r)
    a = max(x[0] for x in L.w1_resid(M, k1, k2)) if min(np.linalg.norm(k1), np.linalg.norm(k2)) > 0 else float('nan')  # projs() needs w > 0
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2))
    Q1 = tframe(k1) if np.linalg.norm(k1) > 0 else np.eye(6); Q2 = tframe(k2) if np.linalg.norm(k2) > 0 else np.eye(6)
    b = max(np.abs(Q1.T @ (h1 @ M[0, nu] - M[0, nu] @ h2 - sum(d[j]*M[1 + j, nu] for j in range(3))) @ Q2).max() for nu in range(4))
    return a, b, np.isfinite(M).all()

def rand_k(kind):
    if kind == 'hard': return rng.uniform(-np.pi, np.pi, 3)
    v = rng.normal(size=3); v /= np.linalg.norm(v)
    if kind == 'soft': return v*rng.uniform(0, r/8)
    if kind == 'annulus': return v*rng.uniform(r/4, 2*r)

def C1():
    out = {}
    m = np.array([3.05, 1.0, 0.7]); k1, k2 = m.copy(), m.copy(); k1[0] += 9.99e-8/2; k2[0] -= 9.99e-8/2
    out['referee seam'] = w1_both(k1, k2)
    z = np.zeros(3); h = np.array([0.9, -1.3, 0.4])
    out['exact zero leg (left)'] = w1_both(z, h); out['exact zero leg (right)'] = w1_both(h, z); out['both zero'] = w1_both(z, z)
    for kinds in (('hard', 'hard'), ('soft', 'hard'), ('hard', 'soft'), ('annulus', 'annulus'), ('annulus', 'hard')):
        worst = [0, 0, True]
        for _ in range(600):
            a, b, f = w1_both(rand_k(kinds[0]), rand_k(kinds[1])); worst = [max(worst[0], a), max(worst[1], b), worst[2] and f]
        out['dense %s x %s (600)' % kinds] = tuple(worst)
    for k, v in out.items(): print('C1 W1 %-30s w1_resid %.2e | indep. frame %.2e | finite %s' % (k, v[0], v[1], v[2]))
    return out

def cut_pair(l, eps, kind):
    """k1, k2 in the zone interior with q_l = k1_l - k2_l -> -pi from both sides (sides a: q_w = pi - eps, b: -pi + eps)."""
    while True:
        k2 = rand_k('hard') if kind != 'soft2' else rand_k('soft')
        k1 = rand_k('hard') if kind != 'soft1' else rand_k('soft')
        if kind == 'soft1':          # k1 soft: put k2_l near pi so that k1_l - k2_l ~ -pi
            k2[l] = k1[l] + np.pi
            if not (-np.pi + 1e-3 < k2[l] < np.pi - 1e-3): continue
        else:
            if kind != 'soft2': k2[l] = rng.uniform(0.05, np.pi - 0.05)
            elif k2[l] <= 0: k2[l] = -k2[l]
        ka, kb = k1.copy(), k1.copy(); ka[l] = k2[l] - np.pi - eps; kb[l] = k2[l] - np.pi + eps
        if kind == 'soft1':
            ka, kb = k1.copy(), k1.copy(); ka[l] = k1[l] - eps; kb[l] = k1[l] + eps
        if all(-np.pi < x[l] < np.pi for x in (ka, kb)): return ka, kb, k2

def C2():
    for patched in (False, True):
        (R.patch if patched else R.unpatch)()
        for l in range(3):
            s = R.cut_sign(l)
            for eps in (1e-7, 1e-9):
                worst_full = worst_T = 0.0; w1 = 0.0
                for t in range(300 if patched else 60):
                    kind = ('hard', 'soft1', 'soft2')[t % 3]
                    ka, kb, k2 = cut_pair(l, eps, kind)
                    qa, qb = L.wrap(ka - k2)[l], L.wrap(kb - k2)[l]
                    assert qa > 3 and qb < -3, (qa, qb)
                    Ma, Mb = L.glued(ka, k2, r), L.glued(kb, k2, r)
                    PTa, PTb, PT2 = L.projs(ka)[4], L.projs(kb)[4], L.projs(k2)[4]
                    worst_full = max(worst_full, np.abs(Ma - s[:, :, None, None]*Mb).max())
                    worst_T = max(worst_T, max(np.abs(PTa @ Ma[m, n] @ PT2 - s[m, n]*(PTb @ Mb[m, n] @ PT2)).max()
                                               for m in range(4) for n in range(4)))
                    if patched: w1 = max(w1, max(x[0] for x in L.w1_resid(Ma, ka, k2)), max(x[0] for x in L.w1_resid(Mb, kb, k2)))
                print('C2 %-8s axis %d eps %.0e: max PLACE jump full %.3e | physical block %.3e%s' % (
                    'REPLACED' if patched else 'R19-16', l, eps, worst_full, worst_T, (' | W1 at cut %.2e' % w1) if patched else ''))
    R.patch()

def C3():
    mx = 0.0
    for t in range(120):
        l = t % 3; k1 = rng.uniform(-np.pi, np.pi, 3); k1[l] = np.pi - 1e-9; k2 = rng.uniform(-np.pi, np.pi, 3)
        if t % 4 == 0: k2 = rand_k('soft')
        k1b = k1.copy(); k1b[l] = -np.pi + 1e-9; T = R.face_T(l)
        Ma, Mb = L.glued(k1, k2, r), L.glued(k1b, k2, r)
        mx = max(mx, np.abs(Ma - np.einsum('a,mnab->mnab', T, Mb)).max())
        # right leg face
        k2a = rng.uniform(-np.pi, np.pi, 3); k2a[l] = np.pi - 1e-9; k2b = k2a.copy(); k2b[l] = -np.pi + 1e-9; k1c = rng.uniform(-np.pi, np.pi, 3)
        Ma, Mb = L.glued(k1c, k2a, r), L.glued(k1c, k2b, r)
        mx = max(mx, np.abs(Ma - np.einsum('mnab,b->mnab', Mb, T)).max())
    print('C3 BZ-face continuity (twist T_l, both legs, 1e-9 from the face, 240 crossings): max jump %.2e' % mx)

def C4():
    for l in range(3):
        s = R.cut_sign(l)
        k2 = rng.uniform(-np.pi, np.pi, 3); k2[l] = rng.uniform(0.2, 3.0); k1 = rng.uniform(-np.pi, np.pi, 3)
        ts = np.arange(-400, 401)*1e-4
        Ns = []
        for t in ts:
            k = k1.copy(); k[l] = k2[l] - np.pi + t
            M = L.glued(k, k2, r)
            qw = float(L.wrap(k - k2)[l])                             # graviton representative (tie q = -pi -> +pi)
            Ns.append(M*(s[:, :, None, None] if qw > 0 else 1.0))    # placement-restored: undo the required flip on one side
        Ns = np.array(Ns); d2 = np.abs(Ns[2:] - 2*Ns[1:-1] + Ns[:-2]).max(); mag = np.abs(Ns).max()
        d1 = np.abs(Ns[1:] - Ns[:-1]).max()
        print('C4 line scan across q_%d = -pi (801 pts, step 1e-4): max |M| %.3f, max first diff %.2e, max second diff %.2e' % (l, mag, d1, d2))

def C5():
    Rs = {'C4z': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.]]), 'C3(111)': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.]]),
          'C2(110)': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.]])}
    for name, Rm in Rs.items():
        Lam = np.eye(4); Lam[1:, 1:] = Rm; Rt = np.kron(np.eye(2), Rm); mx = 0.0
        for t in range(300):
            if t % 2: k1, k2 = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
            else:
                v1, v2 = rng.normal(size=3), rng.normal(size=3); k1 = v1/np.linalg.norm(v1)*2*r*rng.uniform(); k2 = v2/np.linalg.norm(v2)*2*r*rng.uniform()
            A = L.glued(Rm @ k1, Rm @ k2, r); B = np.einsum('ma,nb,xy,abyz,wz->mnxw', Lam, Lam, Rt, L.glued(k1, k2, r), Rt)
            mx = max(mx, np.abs(A - B).max())
        print('C5 covariance %-8s max |M(Rk1,Rk2) - R.M(k1,k2)| over 300 pairs = %.2e' % (name, mx))

if __name__ == '__main__':
    print('r = %g' % r)
    R.patch(); C1(); C2(); C3(); C4(); C5()
