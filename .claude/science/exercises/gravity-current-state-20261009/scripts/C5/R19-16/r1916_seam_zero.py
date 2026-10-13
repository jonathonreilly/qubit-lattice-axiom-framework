"""R19-16 targeted checks of the REPAIRED kernel (lib1916), r from argv (default 0.1):
 S1  the referee's seam: midpoint (3.05, 1.0, 0.7), q along each axis, |q| = 0 and 1e-16 .. 1 (60 log-spaced values, incl.
     5e-8, 9.99e-8, 1e-7, 1.001e-7, 1 +- 1e-12 (graviton plateau edge)); W1 on the physical block by lib199.w1_resid AND by the referee's
     independent SVD transverse-frame contraction.
 S2  300 random hard midpoints (1/3 in the transition |k_j| in (b, pi), 1/3 within 1e-6 of a BZ face, 1/3 uniform), small q in
     1, 2 or 3 components (|q_j| in {0} U [1e-16, 1]), and exact k_j = 0 planes.
 S3  kernel continuity: |M(q) - M(q')| at the old switch (0.999e-7 vs 1.001e-7) and at the graviton plateau edge |q| = 1 (1 -+ 1e-9), compared with the
     smooth slope |dM/dq| * |q - q'| estimated by a wide central difference.
 Z1  exact zero soft legs: k1 = 0 (and k2 = 0) with the other leg (a) the referee's (0.9, -1.3, 0.4), (b) 100 random hard,
     (c) 100 in the corner annulus r/2..r (continuum + soft piece both active), (d) k1 = k2 = 0; finiteness (no warnings),
     W1 residual on (FULL left) x P_T2 [resp. P_T1 x FULL right] -- the limit of the physical-block identity from every
     direction -- and the limit |M(eps n, k2) - M(0, k2)| for 8 directions, eps = 1e-2 .. 1e-12.
 Z2  eigen-sum Sylvester vs Neumann series (both sides), away from k = 0, on the physical block."""
import sys, time, warnings, numpy as np
import lib1916 as R
L = R.L
r = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
rng = np.random.default_rng(191600 + int(1000*r)); t0 = time.time()
warnings.simplefilter('error')                     # any RuntimeWarning (0/0, overflow) aborts the run

def tframe(k):
    s = L.sig(k); _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True); e = vh[1:].T
    out = np.zeros((6, 4)); out[:3, :2] = e; out[3:, 2:] = e; return out
def w1_both(k1, k2):
    M, used, _ = L.glued(k1, k2, r, parts=True)
    res = L.w1_resid(M, k1, k2); a = max(x[0] for x in res); rel = max(x[1] for x in res)
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2)); q1, q2 = tframe(k1), tframe(k2)
    ind = max(np.abs(q1.T @ (h1 @ M[0, nu] - M[0, nu] @ h2 - sum(d[j]*M[1+j, nu] for j in range(3))) @ q2).max() for nu in range(4))
    return a, rel, ind, used, M

# S1 the referee's seam
mid = np.array([3.05, 1.0, 0.7])
qs = sorted(set(np.r_[0.0, np.logspace(-16, 0, 49), [5e-8, 9.99e-8, 1e-7, 1.001e-7, 1 - 1e-12, 1 + 1e-12, 0.5, 0.999]]))
mx = [0.0, 0.0, 0.0]; used_all = set(); rows = []
for ax in range(3):
    for q in qs:
        k1, k2 = mid.copy(), mid.copy(); k1[ax] += q/2; k2[ax] -= q/2
        a, rel, ind, used, _ = w1_both(L.wrap(k1), L.wrap(k2)); used_all |= set(used)
        mx = [max(mx[0], a), max(mx[1], rel), max(mx[2], ind)]
        if ax == 0 and q in (5e-8, 9.99e-8, 1.001e-7, 0.0): rows.append((q, a, ind))
print(f'S1 referee seam midpoint {mid}, q along x, y, z at {len(qs)} values (0, 1e-16..1): pieces {sorted(used_all)}')
for q, a, ind in rows:
    print(f'   q_x = {q:.4e}: physical abs residual {a:.3e} (lib199.w1_resid), {ind:.3e} (independent SVD frame)  [old lib199: '
          f'{ {5e-8: "8.02e-13", 9.99e-8: "1.60e-12", 1.001e-7: "1.97e-16", 0.0: "-"}[q]}]')
print(f'   max over all {3*len(qs)}: abs {mx[0]:.2e}, rel {mx[1]:.2e}, independent-frame abs {mx[2]:.2e}')

# S2 random hard midpoints, small q in 1..3 components, exact planes
mx = [0.0, 0.0, 0.0]; cnt = {}
for i in range(300):
    m = rng.uniform(-np.pi, np.pi, 3)
    if i % 3 == 0: m = rng.choice([-1, 1], 3)*rng.uniform(R.BG, np.pi, 3)
    elif i % 3 == 1: l = rng.integers(0, 3); m[l] = rng.choice([-1, 1])*(np.pi - 1e-6*rng.uniform())
    if np.linalg.norm(m) < 2*r: continue
    q = np.zeros(3); nq = rng.integers(1, 4)
    for j in rng.choice(3, nq, replace=False):
        q[j] = rng.choice([-1, 1])*(0.0 if rng.uniform() < 0.15 else 10**rng.uniform(-16, 0))
    if rng.uniform() < 0.1: m[rng.integers(0, 3)] = 0.0; q[:] = 0.0          # exact k_j = 0 plane, forward
    k1, k2 = L.wrap(m + q/2), L.wrap(m - q/2)
    a, rel, ind, used, _ = w1_both(k1, k2)
    for u in used: cnt[u] = cnt.get(u, 0) + 1
    mx = [max(mx[0], a), max(mx[1], rel), max(mx[2], ind)]
print(f'S2 300 random hard midpoints (transition / near-face / uniform), |q_j| in {{0}} U [1e-16, 1], exact planes: pieces {cnt}; '
      f'max abs {mx[0]:.2e}, rel {mx[1]:.2e}, independent-frame abs {mx[2]:.2e}')

# S3 continuity at the old switch and at |q| = 1
def Mq(q, ax=0, m=mid):
    k1, k2 = m.copy(), m.copy(); k1[ax] += q/2; k2[ax] -= q/2; return L.glued(L.wrap(k1), L.wrap(k2), r)
for (qa, qb, lab) in ((0.999e-7, 1.001e-7, 'old 1e-7 switch'), (1 - 1e-9, 1 + 1e-9, '|q| = 1 edge')):
    jump = np.abs(Mq(qa) - Mq(qb)).max()
    hh = max(1e-4*qa, 1e-9); slope = np.abs(Mq(0.5*(qa + qb) + hh) - Mq(0.5*(qa + qb) - hh)).max()/(2*hh)
    print(f'S3 {lab:16s}: |M(q={qa:.6e}) - M(q={qb:.6e})| = {jump:.2e}; smooth expectation |dM/dq|*dq = {slope*(qb - qa):.2e} '
          f'(old lib199 at 1e-7: 1.49e-05)')

# Z1 exact zero legs
def resid_fullside(M, k1, k2, soft):
    """W1 residual with FULL left (soft == 'L') or FULL right (soft == 'R') and P_T on the hard side; relative to term size."""
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2))
    if soft == 'L': PL, PR = np.eye(6), L.projs(k2)[4]
    elif soft == 'R': PL, PR = L.projs(k1)[4], np.eye(6)
    else: PL = PR = np.eye(6)
    a = 0.0; sc = 1e-300
    for nu in range(4):
        lhs = h1 @ M[0, nu] - M[0, nu] @ h2; rhs = np.einsum('j,jab->ab', d, M[1:, nu])
        a = max(a, np.abs(PL @ (lhs - rhs) @ PR).max()); sc = max(sc, np.abs(PL @ lhs @ PR).max(), np.abs(PL @ rhs @ PR).max())
    return a, a/sc
def ball(rad):
    v = rng.normal(size=3); return v/np.linalg.norm(v)*rad
z = np.zeros(3)
fam = {'referee k2=(0.9,-1.3,0.4)': [np.array([0.9, -1.3, 0.4])],
       'random hard k2': [rng.uniform(-np.pi, np.pi, 3) for _ in range(100)],
       'corner annulus |k2| in r/2..r': [ball(r*rng.uniform(0.5, 1.0)) for _ in range(100)]}
for name, k2s in fam.items():
    fin = True; mxa = mxr = 0.0; lim = {e: 0.0 for e in (1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12)}; used_all = set()
    for k2 in k2s:
        for side in ('L', 'R'):
            a1, a2 = (z, k2) if side == 'L' else (k2, z)
            M, used, _ = L.glued(a1, a2, r, parts=True); used_all |= set(used)
            fin &= bool(np.isfinite(M).all())
            a, rel = resid_fullside(M, a1, a2, side); mxa = max(mxa, a); mxr = max(mxr, rel)
            for eps in lim:
                for _ in range(8 if name.startswith('referee') else 1):
                    n = ball(eps)
                    Me = L.glued(n, k2, r) if side == 'L' else L.glued(k2, n, r)
                    lim[eps] = max(lim[eps], np.abs(Me - M).max())
    print(f'Z1 exact zero leg, {name:32s} ({len(k2s)} x both sides) pieces {sorted(used_all)}: all finite {fin}; '
          f'W1 (full soft side x P_T hard side) max abs {mxa:.2e} rel {mxr:.2e}')
    print('     limit |M(eps n, k) - M(0, k)| max over directions: ' + ', '.join(f'eps={e:.0e}: {v:.1e}' for e, v in lim.items()))
M00 = L.glued(z, z, r); print(f'Z1 k1 = k2 = 0: finite {bool(np.isfinite(M00).all())}, pieces {L.glued(z, z, r, parts=True)[1]}, '
                              f'W1 full x full residual {resid_fullside(M00, z, z, "F")[0]:.1e}')

# Z2 eigen-sum vs Neumann on the physical block, away from 0, both sides
ag = 0.0
for _ in range(100):
    ks = ball(r/8*rng.uniform(0.01, 1.0)); kh = rng.uniform(-np.pi, np.pi, 3)
    if np.linalg.norm(kh) < r/2: continue
    for left in (True, False):
        k1, k2 = (ks, kh) if left else (kh, ks)
        Msp = L.spatial_VW(k1, k2); P1 = L.projs(k1)[4]; P2 = L.projs(k2)[4]
        A = R.piece_A(k1, k2, Msp, left, series=True); B = R.piece_A(k1, k2, Msp, left, series=False)
        ag = max(ag, max(np.abs(P1 @ (A[m, n] - B[m, n]) @ P2).max() for m in range(4) for n in range(4)))
print(f'Z2 Neumann series vs eigen-sum Sylvester (physical block, both sides, 0.01..1 x r/8): max diff {ag:.1e}')
print(f'time {time.time() - t0:.0f}s')
