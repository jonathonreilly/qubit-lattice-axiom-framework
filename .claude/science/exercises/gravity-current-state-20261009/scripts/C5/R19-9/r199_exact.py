"""R19-9 (a): build the glued exact photon stress (lib199) and check W1 on the physical block to machine precision,
plus symmetry, Hermiticity, (H-E), forward values, pair-kernel identity with VW outside U_r, soft-leg continuity, face wraps."""
import sys, time, numpy as np
import lib199 as L
sys.path.insert(0, L.os.path.join(L.HERE, 'arch18_13'))
import vwface as V
t0 = time.time(); rng = np.random.default_rng(199)
r = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
print(f'photon {L.LAW.name}; root a={L.A_R}, (wd, wo)=({L.WD_R}, {L.WO_R}); corner radius r={r}; SIGN={L.SIGN}')

# 0. vertex generalization == R18-13 vertex_geo (unmodified archive)
worst = 0.0
for _ in range(300):
    c1, c2, s = rng.uniform(0, 1, 3), rng.uniform(0, 1, 3), rng.uniform(-np.pi, np.pi, 3)
    e = rng.normal(size=(3, 3)); e = e + e.T
    A = V.vertex_geo(e, c1, c2, s, L.A_R, L.WD_R, L.WO_R)
    B = L.vertex(e, c1, c2, L.Pstencil(s, L.A_R), L.ustencil(s, L.WD_R), L.ustencil(s, L.WO_R))
    worst = max(worst, np.abs(A[0]-B[0]).max(), np.abs(A[1]-B[1]).max())
print(f'[0] vertex(P,u arrays) vs archived vwface.vertex_geo, 300 random: max diff {worst:.1e}')
# linearity: sum_ij e_ij M^{ij} == vertex_geo(e)
k1, k2 = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
Msp = L.spatial_VW(k1, k2); e = rng.normal(size=(3, 3)); e = e + e.T
ME, MB = V.vertex_geo(e, L.cfun(k1), L.cfun(k2), k1 - k2, L.A_R, L.WD_R, L.WO_R)
lin = max(np.abs(L.SIGN*np.einsum('ij,ijab->ab', e, Msp)[:3, :3] - ME).max(), np.abs(L.SIGN*np.einsum('ij,ijab->ab', e, Msp)[3:, 3:] - MB).max())
print(f'    component kernels recombine to vertex_geo(e): {lin:.1e}')

def ball(n, rad):
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    return v*rad*rng.uniform(0, 1, n)[:, None]**(1/3)

# 1. continuum kernel conservation (sigma = k, d = q in U_r), both signs reported to fix the convention
for sgn in (-1.0, 1.0):
    L.SIGN = sgn; mx = 0.0
    for _ in range(200):
        k1, k2 = ball(1, r)[0], ball(1, r)[0]
        mx = max(mx, max(x[1] for x in L.w1_resid(L.continuum(k1, k2), k1, k2)))
    print(f'[1] continuum Maxwell kernel, SIGN={sgn:+.0f}: max relative W1 residual over 200 corner pairs = {mx:.2e}')
L.SIGN = -1.0

# 2. glued kernel, W1 on the physical block, sample families
fams = {}
fams['torus uniform'] = [(rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)) for _ in range(400)]
nl = []
for _ in range(200):   # near the scattering shell w1 = w2 (both hard): k2 = rotation-ish of k1 with |sigma| matched by bisection
    k1 = rng.uniform(-np.pi, np.pi, 3); u = rng.normal(size=3); u /= np.linalg.norm(u)
    lo, hi = 0.0, 2*np.pi
    f = lambda t: L.omega(L.wrap(t*u)) - L.omega(k1)
    if f(hi*0.999) < 0: continue
    for _ in range(80):
        mid = 0.5*(lo + hi); lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    nl.append((k1, L.wrap(lo*u) + 1e-9*rng.normal(size=3)))
fams['near shell |w1-w2|<~1e-9'] = nl
fw = []
for _ in range(200):   # forward diagonal, incl. exact coordinate planes q_l = 0 (removable limits)
    k2 = rng.uniform(-np.pi, np.pi, 3); q = rng.normal(size=3)*10.0**rng.uniform(-9, -1)
    q[rng.integers(0, 3)] = 0.0
    if rng.uniform() < 0.3: q[:] = 0.0; q[rng.integers(0, 3)] = 10.0**rng.uniform(-9, -1)
    fw.append((L.wrap(k2 + q), k2))
fams['forward, q_l = 0 planes'] = fw
fams['single soft left'] = [(ball(1, r/4)[0], rng.uniform(-np.pi, np.pi, 3)) for _ in range(200)]
fams['single soft right'] = [(rng.uniform(-np.pi, np.pi, 3), ball(1, r/4)[0]) for _ in range(200)]
fams['corner U_r (both < r)'] = [(ball(1, r)[0], ball(1, r)[0]) for _ in range(300)]
cs = []
for _ in range(200):   # corner shell: |k1| = |k2| inside U_r, plus tiny offset
    u, v = rng.normal(size=3), rng.normal(size=3); rad = r*rng.uniform(0.05, 1.0)
    cs.append((u/np.linalg.norm(u)*rad, v/np.linalg.norm(v)*rad*(1 + 1e-10*rng.normal())))
fams['corner, on shell'] = cs
fams['annulus r/2..2r'] = [(ball(1, 2*r)[0], ball(1, 2*r)[0]) for _ in range(300)]
fams['one leg in r/16..r/4, other in r/4..2r'] = [(ball(1, r/4)[0], ball(1, 2*r)[0]) for _ in range(300)]
wr = []
for _ in range(100):   # near BZ faces
    k1 = rng.uniform(-np.pi, np.pi, 3); k1[rng.integers(0, 3)] = np.pi*(1 - 1e-6*rng.uniform())*rng.choice([-1, 1])
    wr.append((k1, rng.uniform(-np.pi, np.pi, 3)))
fams['near BZ faces'] = wr
glob = 0.0; globabs = 0.0
for name, pts in fams.items():
    mx = 0.0; mxa = 0.0; used = set()
    for (k1, k2) in pts:
        M, u, _ = L.glued(k1, k2, r, parts=True); used |= set(u)
        res = L.w1_resid(M, k1, k2)
        mx = max(mx, max(x[1] for x in res)); mxa = max(mxa, max(x[0] for x in res))
    glob = max(glob, mx); globabs = max(globabs, mxa)
    print(f'[2] W1 glued, {name:40s} n={len(pts):3d} pieces {sorted(used)}: max rel {mx:.2e}  max abs {mxa:.2e}')
print(f'    ALL FAMILIES: max relative W1 residual {glob:.2e}, max absolute {globabs:.2e}')

# 3. symmetry, Hermiticity (physical block), (H-E), forward values (Lemma F), pair kernel == VW outside U_r
herm = 0.0; sym = 0.0
for (k1, k2) in fams['torus uniform'][:150] + fams['corner U_r (both < r)'][:100] + fams['single soft left'][:50]:
    M = L.glued(k1, k2, r); Mt = L.glued(k2, k1, r)
    _, _, _, _, PT1, _ = L.projs(k1); _, _, _, _, PT2, _ = L.projs(k2)
    for mu in range(4):
        for nu in range(4):
            herm = max(herm, np.abs(PT1 @ (M[mu, nu] - Mt[mu, nu].conj().T) @ PT2).max())
            sym = max(sym, np.abs(M[mu, nu] - M[nu, mu]).max())
print(f'[3] mu-nu symmetry max {sym:.1e}; exchange Hermiticity (physical block) max {herm:.2e}')
he = 0.0; fv = 0.0
for _ in range(100):
    k = rng.uniform(-np.pi, np.pi, 3)
    if np.linalg.norm(k) < r: continue
    M = L.glued(k, k, r); h, w, Pp, Pm, PT, _ = L.projs(k)
    he = max(he, np.abs(PT @ M[0, 0] @ PT - 0.5*PT).max())
    v = L.sig(k)*L.cfun(k)/w                               # group velocity grad(w^2/2)/w
    sc = lambda X: Pp @ X @ Pp + Pm @ X @ Pm
    fv = max(fv, max(np.abs(sc(M[0, 1+j]) - v[j]*0.5*(Pp - Pm)).max() for j in range(3)),
             max(np.abs(sc(M[1+i, 1+j]) - v[i]*v[j]*0.5*PT).max() for i in range(3) for j in range(3)))
print(f'[3] (H-E) P_T M00(k,k) P_T = P_T/2 (so int T00 = H): max dev {he:.1e}; forward scattering values = Lemma F (v_j, v_i v_j): max dev {fv:.1e}')
pk = 0.0; pkc = 0.0
for (k1, k2) in fams['torus uniform'][:200] + fams['single soft left'][:50] + fams['annulus r/2..2r'][:200]:
    n1, n2 = np.linalg.norm(k1), np.linalg.norm(k2)
    M = L.glued(k1, k2, r); h1, w1, Pp1, Pm1, PT1, _ = L.projs(k1); h2, w2, Pp2, Pm2, PT2, _ = L.projs(k2)
    if max(n1, n2) >= r:
        ref = L.spatial_VW(k1, k2)
    elif max(n1, n2) <= r/2:
        ref = L.continuum(k1, k2)[1:, 1:]
    else:
        continue
    dev = max(np.abs(Pp1 @ (M[1+i, 1+j] - ref[i, j]) @ Pm2).max() + np.abs(Pm1 @ (M[1+i, 1+j] - ref[i, j]) @ Pp2).max() for i in range(3) for j in range(3))
    if max(n1, n2) >= r: pk = max(pk, dev)
    else: pkc = max(pkc, dev)
print(f'[3] spatial PAIR blocks: == VW (root a, wd, wo) where a leg is outside U_r: max dev {pk:.1e}; == continuum inside U_(r/2): {pkc:.1e}')

# 4. single soft leg: the full-left solution is analytic in h(k1): eigen-sum == Neumann series, and the k1 -> 0 limit is
#    direction independent (the transverse projector P_T(k1) is not, but the kernel is).
k2 = np.array([0.9, -1.3, 0.4]); Msp0 = lambda k1: L.spatial_VW(k1, k2)
ag = 0.0
for _ in range(50):
    k1 = ball(1, r/4)[0]
    A1 = L.piece_A(k1, k2, Msp0(k1), True); A2 = L.piece_A(k1, k2, Msp0(k1), True, series=True)
    ag = max(ag, np.abs(A1 - A2).max())
print(f'[4] soft left leg: eigen-sum Sylvester vs Neumann series in h(k1): max diff {ag:.1e}')
for t in (1e-2, 1e-4, 1e-6, 1e-8):
    vals = []
    for _ in range(6):
        u = rng.normal(size=3); u /= np.linalg.norm(u); k1 = t*u
        vals.append(L.piece_A(k1, k2, Msp0(k1), True, series=True))
    spread = max(np.abs(vv - vals[0]).max() for vv in vals)
    PTs = []
    for _ in range(2):
        u = rng.normal(size=3); u /= np.linalg.norm(u); PTs.append(L.projs(t*u)[4])
    print(f'    |k1| = {t:.0e}: spread of the full-left kernel over 6 directions {spread:.2e} (vs spread of P_T(k1) {np.abs(PTs[0]-PTs[1]).max():.2f})')
M0 = L.piece_A(np.zeros(3) + 1e-300, k2, Msp0(np.zeros(3)), True, series=True)

# 5. face wrap covariance of the glued kernel: k1_l -> k1_l - 2 pi multiplies psi(k1) by T_l (E_l and B_m, m != l, flip)
for off in (1e-7, 1e-9):
    wc = 0.0
    for _ in range(60):
        l = rng.integers(0, 3); k1 = rng.uniform(-np.pi, np.pi, 3); k1[l] = np.pi - off; k2 = rng.uniform(-np.pi, np.pi, 3)
        k1b = k1.copy(); k1b[l] = -np.pi + off
        T = np.ones(6); T[l] = -1; T[3:] = -1; T[3+l] = 1
        Ma = L.glued(k1, k2, r); Mb = L.glued(k1b, k2, r)
        wc = max(wc, np.abs(Ma - np.einsum('a,mnab->mnab', T, Mb)).max())
    print(f'[5] across the BZ face (rotated-frame twist T_l), 60 pairs at {off:.0e} from the face: max jump {wc:.2e} (scales with the gap 2x{off:.0e})')
print(f'time {time.time()-t0:.0f} s')
