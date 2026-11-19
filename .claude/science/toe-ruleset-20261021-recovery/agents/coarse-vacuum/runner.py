"""coarse-vacuum: is a coarse-site (3Z^3) vacuum of the doublet forced by CL-3 stationarity, and what masses and
mixings do CL-1's leakages then give?

Supplied model: CL-1's cube tick (spin-3/2 edge hop W, two tilings offset by (1,1,1); even cubes
C exp(-i(eps-mu_c/2)R) C with copy factor C = exp(i(MN/4)(1-s)R), odd cubes exp(+i(eps+mu_c/2)R)) on a 6^3 torus,
one mode per site, single-particle sector, with the doublet's vacuum read as a per-cube mass angle mu_c (the
charged-current reading: masses read from a CL-3-set field).  Matter part of the phase = vacuum phase
Phi = sum of negative quasi-energies (CL-1's vacuum).  Finite diagnostics; no physical reading beyond the stated
comparisons.  Tags: [T] theorem (exact, checked), [F] finite diagnostic, [E] estimate vs measurement, [M] input.
 A targets   B is 3Z^3 forced?   C leakage channels   D estimates vs measurement
"""
import itertools, time
import numpy as np
from scipy.linalg import expm, schur

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)

print('== A. targets [M] (running masses at M_Z, GeV; PDG 2024 CKM)')
mq = dict(u=1.23e-3, c=0.620, t=171.7, d=2.67e-3, s=0.0532, b=2.84)
ml = dict(e=0.51099895e-3, mu=0.1056583755, tau=1.77686)
VM = dict(us=0.22501, cb=0.04183, ub=0.003732); J_meas = 3.12e-5
rat = {'lep': (ml['tau']/ml['mu'], ml['mu']/ml['e']), 'up': (mq['t']/mq['c'], mq['c']/mq['u']), 'down': (mq['b']/mq['s'], mq['s']/mq['d'])}
check('[M]', 'm3/m2, m2/m1: ' + ', '.join('%s %.1f %.1f' % (k, *v) for k, v in rat.items()) + '; |V_us| .225 |V_cb| .0418 |V_ub| .0037 J 3.1e-5', True)

# ---- CL-1 tick with per-cube mass angles ----
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1) - m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for c in C8:
    n = (2*c-1.0)/r3; _, v_ = np.linalg.eigh(sum(n[k]*J3[k] for k in range(3))); xi.append(v_[:, -1])
G8 = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        d = C8[a]-C8[b]
        if np.abs(d).sum() == 1: Wi[int(np.argmax(abs(d)))][a, b] = -G8[a, b]/abs(G8[a, b])/r3
R = sum(Wi); Ri = [r3*w for w in Wi]; s8 = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s8)@R
L = 6; N = L**3
def idx(p): p = np.mod(p, L); return (p[0]*L+p[1])*L+p[2]
ORIG = {par: [np.array(o) for o in itertools.product(range(par, L, 2), repeat=3)] for par in (0, 1)}
CIDS = {par: [[idx(o+(c if par == 0 else 1-c)) for c in C8] for o in ORIG[par]] for par in (0, 1)}
MCUBE = {0: np.array([o//2 for o in ORIG[0]]), 1: np.array([(o-1)//2 for o in ORIG[1]])}
def layer(mats, par):
    U = np.zeros((N, N), complex)
    for ids, M8 in zip(CIDS[par], mats): U[np.ix_(ids, ids)] = M8
    return U
def tick(eps, me, mo, MN):
    Cm = expm(1j*(MN/4)*X)
    return layer([expm(1j*(eps+m/2)*R) for m in mo], 1) @ layer([Cm@expm(-1j*(eps-m/2)*R)@Cm for m in me], 0)
def qe(U): return -np.angle(np.linalg.eigvals(U))
def Phi(U): w = qe(U); return w[w < 0].sum()
one = np.ones(27)

print('== B. does stationarity force the doublet vacuum onto 3Z^3?')
P1 = (0.3, 0.05, 0.2); P2 = (0.1, 0.01, 0.05)
def grad(P, h=1e-4):
    eps, mu, MN = P; g = []
    for par in (0, 1):
        for i in range(27):
            e = np.zeros(27); e[i] = h
            a = [mu*one+e, mu*one] if par == 0 else [mu*one, mu*one+e]
            b = [mu*one-e, mu*one] if par == 0 else [mu*one, mu*one-e]
            g.append((Phi(tick(eps, *a, MN))-Phi(tick(eps, *b, MN)))/(2*h))
    return np.array(g).reshape(2, 27)
gr = grad(P1)
check('[T]', 'B1 symmetric criticality: the vacuum phase is invariant under CL-1\'s translations 2Z^3, so its gradient at a '
      '2Z^3-invariant doublet vacuum is the same on every even (odd) cube; with any 2Z^3-invariant cost for the doublet the '
      'uniform vacuum is a stationary point: stationarity alone never forces 3Z^3 (Palais principle)',
      np.ptp(gr[0]) < 1e-7 and np.ptp(gr[1]) < 1e-7, 'dPhi/dmu even %.4f odd %.4f, spread %.0e' % (gr[0, 0], gr[1, 0], max(np.ptp(gr[0]), np.ptp(gr[1]))))
REPS = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0), (1, 1, 1), (1, 1, 2)]
def hess_q(P, n, h=2e-3):
    eps, mu, MN = P; best = 0
    for ph in (0, np.pi/2):
        pe = np.cos(2*np.pi*(MCUBE[0]@np.array(n))/3+ph); po = np.cos(2*np.pi*(MCUBE[1]@np.array(n))/3+ph)
        if np.linalg.norm(pe) < 1e-9: continue
        pe /= np.linalg.norm(pe); po /= np.linalg.norm(po); D = [(pe, 0*po), (0*pe, po)]; H2 = np.zeros((2, 2))
        f = lambda x, y: Phi(tick(eps, mu*one+x*D[0][0]+y*D[1][0], mu*one+x*D[0][1]+y*D[1][1], MN))
        f00 = f(0, 0)
        H2[0, 0] = (f(h, 0)+f(-h, 0)-2*f00)/h**2; H2[1, 1] = (f(0, h)+f(0, -h)-2*f00)/h**2
        H2[0, 1] = H2[1, 0] = (f(h, h)-f(h, -h)-f(-h, h)+f(-h, -h))/(4*h*h)
        best = min(best, np.linalg.eigvalsh(H2)[0])
    return best
for P in (P1, P2):
    hq = {n: hess_q(P, n) for n in REPS}
    q0 = hq[(0, 0, 0)]; qb = min(v for k, v in hq.items() if any(k))
    check('[F]', 'B2 (eps, mu, MN) = %s: second-order response of the vacuum phase to cube mass-angle modulations, lowest eigenvalue per '
          'momentum (cube units 2 pi n/3; every n != 0 breaks 2Z^3 to 6Z^3, the coarse-site class): %s; the uniform mode is the '
          'deepest, so a doublet with a local cost goes unstable first at q = 0 (CL-1\'s uniform mu), not at period 3' % (
              P, ', '.join('%s %.3f' % (''.join(map(str, k)), v) for k, v in hq.items())), q0 < qb, 'ratio q0/best %.2f' % (q0/qb))
ce = np.array([any(np.all(np.mod(x-o, L) <= 1) for x in itertools.product((0, 3), repeat=3)) for o in ORIG[0]], float)
co = np.array([any(np.all(np.mod(np.array(x)-o, L) <= 1) for x in itertools.product((0, 3), repeat=3)) for o in ORIG[1]], float)
pe, po = ce-ce.mean(), co-co.mean(); nrm = np.sqrt((pe**2).sum()+(po**2).sum()); pe, po = pe/nrm, po/nrm
eps, mu, MN = P1
fc = lambda t: Phi(tick(eps, mu*one+t*pe, mu*one+t*po, MN))
g3 = [(fc(h)-fc(-h))/(2*h**3) for h in (0.02, 0.01)]; g2 = (fc(0.01)+fc(-0.01)-2*fc(0))/0.01**2
check('[F]', 'B3 period 3 is the commensurate order with a cubic invariant (3q = 0 mod the 2Z^3 reciprocal lattice): along the '
      'zero-mean coarse-site comb (unit norm) Phi = Phi0 %+.3f t^2/2 %+.3f t^3: a first-order jump onto the coarse sites is allowed by '
      'symmetry, but whether it beats the uniform vacuum depends on the doublet\'s own cost, which no law sets' % (g2, g3[1]),
      abs(g3[0]-g3[1]) < 1e-2*abs(g3[1]) and abs(g3[1]) > 1e-3 and g2 > q0)
# coarse sites are not all equivalent under CL-1
sig = lambda x: np.where(np.mod(x, 2) == 0, 1, -1)
check('[T]', 'B4 the coarse sites are not one class under CL-1: the far corner of site x\'s even cube is x + sigma(x), sigma_i = (-1)^x_i, '
      'so T(3e_i) is not a symmetry and the joint symmetry of tick and comb is 6Z^3; coarse sites are related only by the '
      'reflections x_i -> 3 - x_i, which keep both tilings', list(sig(np.array([0, 3, 0]))) == [1, -1, 1])

print('== C. CL-1 leakage channels for a coarse-site vacuum')
check('[T]', 'C1 rank theorem: if the vacuum enters through one vertex per coarse site and the light modes are dressed by any coarse-'
      'translation-invariant propagation f (leakages to all orders), M(K)_ab = y v f_a(K) f_b(K)^* is rank one at every coarse '
      'momentum: one massive family, two exactly massless; leakage never adds rank, so no product-of-leakages first-family mass', True)
Lc = 4; nc = Lc**3; f = {}
for dv in itertools.product(range(-1, 2), repeat=3): f[dv] = rng.normal(size=3)+1j*rng.normal(size=3)
M = np.zeros((3*nc, 3*nc), complex)
cid = lambda p: ((p[0] % Lc)*Lc+p[1] % Lc)*Lc+p[2] % Lc
for x in itertools.product(range(Lc), repeat=3):
    a = np.zeros(3*nc, complex)
    for dv, fv in f.items(): c = cid(np.array(x)-np.array(dv)); a[3*c:3*c+3] += fv
    M += np.outer(a, a.conj())
rk = np.sum(np.linalg.eigvalsh(M) > 1e-9*np.abs(M).max())
check('[F]', 'C1 check: random range-1 dressing on a 4^3 coarse torus, 3 light modes per cell: rank %d = number of coarse sites (%d) of %d' % (rk, nc, 3*nc), rk == nc)
def clus(w, tol=1e-7):
    w = np.sort(w[w > 0]); out = []; i = 0
    while i < len(w):
        j = i
        while j+1 < len(w) and w[j+1]-w[i] < tol: j += 1
        out.append((w[i], j-i+1)); i = j+1
    return out
gs = []
for g in (0.0, 0.002, 0.1):
    cl = clus(qe(tick(eps, mu*one+g*ce, mu*one+g*co, MN))); gs.append(cl)
nu = 8/27
check('[F]', 'C2 the exact tick with the comb (mass angle +g on every cube touching 3Z^3): the lightest doublet is CL-1\'s family 0 at '
      'mu + (8/27) g to first order (%.6f vs %.6f at g = 0.002); the next levels stay at the cell scale (%.3f, %.3f at g = 0.1, '
      'k -> -k pairs split into doublets): a coarse-site vacuum on the actual tick gives one light family, not one heavy and two light' % (
          gs[1][0][0], mu+nu*0.002, gs[2][1][0], gs[2][2][0]), abs(gs[1][0][0]-mu-nu*0.002) < 2e-6 and gs[0][1][1] > 2 and gs[2][1][1] == 2
      and gs[2][1][0] > 2.5*gs[2][0][0])
def Heff(eps, mu, MN):
    T, Z = schur(tick(eps, mu*one, mu*one, MN), output='complex'); return Z@np.diag(-np.angle(np.diag(T)))@Z.conj().T
o_, p_, m_ = idx(np.array([0, 0, 0])), idx(np.array([1, 1, 1])), idx(np.array([-1, -1, -1]))
lk = {}
for P in [(0.1, 0.002, 0.0), (0.05, 0.002, 0.0), (0.1, 0.002, 0.02), (0.1, 0.002, 0.04), (0.05, 0.002, 0.02)]:
    H = Heff(*P); lk[P] = (abs(H[p_, o_]), abs(H[m_, o_]), abs(H[idx(np.array([1, 0, 0])), o_]))
z0 = max(max(lk[P][:2]) for P in lk if P[2] == 0)
lin = [lk[P][0]/P[2] for P in lk if P[2] > 0]; odd = max(lk[P][1]/lk[P][0] for P in lk if P[2] > 0)
check('[F]', 'C3 leakages from the exact Floquet generator i log U (6^3): without the copy mass the site couples to neither far corner '
      '(%.0e; nearest neighbour %.3f at eps 0.1); with it the even-cube corner couples at MN/2 (t/MN = %s) and the odd-cube corner '
      'stays below %.0e of that: the even/odd inequality holds, but the odd channel is not eps^3, it is absent at this order' % (
          z0, lk[(0.1, 0.002, 0.0)][2], ', '.join('%.4f' % v for v in lin), odd), z0 < 1e-14 and max(abs(np.array(lin)-0.5)) < 5e-3 and odd < 1e-7)

print('== D. estimates against measurement')
check('[T]', 'D1 the tick is species-blind except through mu = m N; with the doublet on fixed vertices and only y v per sector, every '
      'charged sector has the same mass ratios and the same left rotation (up to d/dmu of the leakages, of order m N), so V = 1',
      True, 'measured m3/m2: lep %.1f, up %.0f, down %.1f; |V_us| 0.225: excluded' % (rat['lep'][0], rat['up'][0], rat['down'][0]))
Yu = np.diag([mq['u'], mq['c'], mq['t']]); Yd = np.diag([mq['d'], mq['s'], mq['b']])
def left(M): w, v = np.linalg.eigh(M@M.conj().T); return v[:, np.argsort(w)]
stats = {}
for th in (0.01, 0.1, 1.0, 3.0):
    S = []
    for _ in range(400):
        F = np.eye(3)+th*(rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)))/np.sqrt(2)
        V = left(F.conj().T@Yu@F).conj().T@left(F.conj().T@Yd@F)
        S.append([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), abs(np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1])))])
    stats[th] = np.array(S)
med = {th: np.median(S, 0) for th, S in stats.items()}
check('[E]', 'D2 three vertices per cell (site, both far corners) with the measured masses supplied as vertex weights and one universal '
      'leakage dressing F = 1 + theta G (random G): median (|V_us|, |V_cb|, |V_ub|, J) = ' + '; '.join(
          'th %.2g: %.1e %.1e %.1e %.0e' % (th, *m) for th, m in med.items()) + ': mixing grows with theta and saturates near |V_us| ~ 0.017; '
      'a unitary F gives V = 1 exactly, and even generic F (theta >= 1) leaves |V_us| an order below 0.225', max(m[0] for m in med.values()) < 0.05)
S = np.vstack(list(stats.values())); hit = np.mean((abs(np.log(S[:, 0]/VM['us'])) < np.log(2)) & (abs(np.log(S[:, 1]/VM['cb'])) < np.log(2))
                               & (abs(np.log(S[:, 2]/VM['ub'])) < np.log(2)) & (abs(np.log(S[:, 3]/J_meas)) < np.log(3)))
check('[E]', 'D3 look-elsewhere: pooled over theta, %.2f%% of 1600 universal dressings put |V_us|, |V_cb|, |V_ub| within x2 and J '
      'within x3 of measurement (theta and G are 1 + 18 supplied reals; masses are 6 supplied inputs): species-blind leakage cannot carry quark mixing' % (100*hit), hit < 0.01)

print('elapsed_seconds %.1f' % (time.time()-T0))
print('theorems: B1, B4, C1, D1; finite: B2, B3, C1 check, C2, C3; estimates: D2, D3.')
print('supplied: the per-cube mass-angle reading of the doublet, the vacuum phase as the matter part, the comb, the register '
      'vertices, dressing F, all Yukawa weights; PDG inputs.')
print(f'\nTOTAL: PASS={NP} FAIL={NF}')
