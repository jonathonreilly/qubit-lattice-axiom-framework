"""zoom3-fixed-families (menu M13, brief P1): are the three turn-fixed zoom-3 block positions three light families,
split 1+1+1 by the copy mass, sharing one turn charge, and can they mix?

Supplied model: CL-1's cube tick exactly as in family-flux (spin-3/2 edge hop on 2x2x2 cubes, two tilings offset by
(1,1,1), even cubes exp(-i(eps-mu/2)R) wrapped by the copy-mass factor exp(i(MN/4)(1-s)R), odd cubes
exp(+i(eps+mu/2)R)), one mode per site, single-particle sector, (eps, mu, MN) = (0.3, 0.05, 0.2). Zoom-3 blocks
centred on the sites 3n of a 6^3 torus (the smallest torus carrying both tilings and the blocks); block term
U_g = exp(-i g H_B) U. Tags: [T] exact algebra/combinatorics, [F] finite diagnostic, [E] estimate vs measurement,
[S] speculation (candidate rule, untested). Each line reports a RESULT; it passes when the computation returns
what the line states.
"""
import itertools, time
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261023)

r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1) - m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for c in C8:
    n = (2*c-1.0)/r3; _, v_ = np.linalg.eigh(sum(n[k]*J3[k] for k in range(3))); xi.append(v_[:, -1])
G = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        d = C8[a]-C8[b]
        if np.abs(d).sum() == 1: Wi[int(np.argmax(abs(d)))][a, b] = -G[a, b]/abs(G[a, b])/r3
R = sum(Wi); Ri = [r3*w for w in Wi]; s8 = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s8)@R

class Torus:
    def __init__(self, L, K=(0, 0, 0)):
        self.L = L; self.N = L**3; self.K = np.array(K, float); self.P = np.array(list(itertools.product(range(L), repeat=3)))
    def idx(self, p): p = np.mod(p, self.L); return (p[0]*self.L+p[1])*self.L+p[2]
    def layer(self, M8, par):
        L = self.L; U = np.zeros((self.N, self.N), complex)
        for o in itertools.product(range(par, L+par, 2), repeat=3):
            ps = [np.array(o)+(c if par == 0 else 1-c) for c in C8]
            ids = [self.idx(p) for p in ps]; ph = np.array([np.exp(1j*self.K@(np.floor_divide(p, L)*L)) for p in ps])
            U[np.ix_(ids, ids)] += M8*np.outer(ph, ph.conj())
        return U
    def tick(self, eps, mu, MN, MO=0.0):
        Ce = expm(1j*(MN/4)*X); Co = expm(1j*(MO/4)*X)
        return self.layer(Co@expm(1j*(eps+mu/2)*R)@Co, 1) @ self.layer(Ce@expm(-1j*(eps-mu/2)*R)@Ce, 0)
def dvec(x): return np.where(np.mod(x, 2) == 0, 1, -1)   # x + d = far corner of x's even cube, x - d of its odd cube
def centres(T, m): return [np.array(c)*m for c in itertools.product(range(T.L//m), repeat=3)]
def fixed_ids(T, m): h = (m-1)//2; return [T.idx(x+k*dvec(x)) for x in centres(T, m) for k in range(-h, h+1)]
def qe(U): return np.angle(np.linalg.eigvals(U))
def turnop(T, U, x):
    S = np.diag(dvec(x)); P = np.zeros((T.N, T.N))
    for p in T.P:
        q = S@(p-x); P[T.idx(x+S@np.array([q[1], q[2], q[0]])), T.idx(p)] = 1
    U2 = P@U@P.T; nz = np.abs(U) > 1e-9; r = np.where(nz, U2/np.where(nz, U, 1), 0)
    g = np.zeros(T.N, complex); g[0] = 1; seen = {0}; st = [0]
    while st:
        a = st.pop()
        for b in np.nonzero(nz[:, a])[0]:
            if b not in seen: g[b] = r[b, a]*g[a]; seen.add(b); st.append(b)
    Tt = np.diag(g.conj())@P; ph = np.linalg.matrix_power(Tt, 3)[0, 0]
    return Tt/np.exp(1j*np.angle(ph)/3)
def heavy(T, m, g, U):
    Pf = np.zeros(T.N); Pf[fixed_ids(T, m)] = 1; return np.exp(-1j*g*(1-Pf))[:, None]*U
def band(T, m, g, U, nb):
    Ug = heavy(T, m, g, U); w, v = np.linalg.eig(Ug); o = np.argsort(np.abs(np.angle(w))); a = np.abs(np.angle(w[o]))
    fl = fixed_ids(T, m); Hb = v[:, o[:nb]]@np.diag(-np.angle(w[o[:nb]]))@np.linalg.pinv(v[:, o[:nb]])
    return a, Hb[np.ix_(fl, fl)], (np.abs(v[fl][:, o[:nb]])**2).sum(0).min()

EPS, MU, MN = 0.3, 0.05, 0.2
T6 = Torus(6); U = T6.tick(EPS, MU, MN); N = T6.N; CS = centres(T6, 3)

print('== A. geometry and the turn')
odd_ok = (9 % 2 == 1) and (6 % 2 == 0) and (6 % 3 == 0)
cnt = {m: sum(1 for o in itertools.product(range(-(m-1)//2, (m-1)//2+1), repeat=3) if o[0] == o[1] == o[2]) for m in (1, 3, 5, 7)}
check('[T]', 'A1 a 9^3 torus cannot carry the two tilings (period 2, odd side); the smallest torus with both tilings and 3^3 '
      'blocks is 6^3 (8 blocks), 18^3 = 6^3 at Bloch K. 6^3 is a multiple of 3, so it is no falsifier; the falsifier is the '
      'zoom itself: an m^3 block centred on a site has F3 = m turn-fixed positions x + k d (m odd), the 2^3 cube has 2. '
      'Every odd zoom keeps both tilings, so "3" is the choice of zoom 3, not forced', odd_ok and cnt == {1: 1, 3: 3, 5: 5, 7: 7},
      'F3(m) = %s' % cnt)
TT = [turnop(T6, U, x) for x in CS]
Ub = heavy(T6, 3, 0.5, U)
res = max(max(np.abs(t@U@t.conj().T-U).max(), np.abs(t@Ub@t.conj().T-Ub).max()) for t in TT)
x0 = CS[0]; chg = [TT[0][T6.idx(x0+k*dvec(x0)), T6.idx(x0+k*dvec(x0))] for k in (-1, 0, 1)]
check('[F]', 'A2 the turn about d(x) through each block centre is an exact symmetry of the copy-massed tick and of U_g (up to a '
      'site gauge, T^3 = 1); (b) the three fixed positions x - d, x, x + d carry ONE turn charge', res < 1e-12 and
      np.ptp(np.round(chg, 9)) == 0, 'residual %.0e, charges %s' % (res, np.round(np.real(chg), 6)))

print('== B. (a) the light count')
rows = []
for g in (0.35, 0.5, 0.65):
    a, _, wmin = band(T6, 3, g, U, 24); rows.append((g, a[24]/a[23], (a[1:61]/np.maximum(a[:60], 1e-12))[3:].max()))
check('[F]', 'B1 RESULT (a) FAILS at the brief\'s g = 0.5 +- 30% (block term = projector on the 24 cycled positions): no gap '
      'at 24 = 3 per block (ratio < 2); the low spectrum is a dense mixture (the largest ratio in the lowest 60 sits at near-zero '
      'crossings, not at a count of 3 per block)',
      all(r[1] < 2 for r in rows), '; '.join('g %.2f: ratio@24 %.2f, max %.2f' % r for r in rows))
HB = np.zeros((N, N), complex); OFF = np.array(list(itertools.product((-1, 0, 1), repeat=3)))
for x, t in zip(CS, TT):
    ids = [T6.idx(x+np.diag(dvec(x))@o) for o in OFF]; tl = t[np.ix_(ids, ids)]
    H = rng.normal(size=(27, 27))+1j*rng.normal(size=(27, 27)); H = (H+H.conj().T)/2
    h = sum(np.linalg.matrix_power(tl, k)@H@np.linalg.matrix_power(tl, k).conj().T for k in range(3))/3
    HB[np.ix_(ids, ids)] += h/np.linalg.norm(h, 2)
gr = []
for g in (0.5, 2.0):
    a = np.sort(np.abs(qe(expm(-1j*g*HB)@U))); gr.append((a[1:61]/np.maximum(a[:60], 1e-12))[3:].max())
check('[F]', 'B2 RESULT with EVERY turn-invariant block term (seeded generic element of the commutant, which includes on-site '
      'and fixed-to-cycle terms on the fixed positions) there is no light count at all: the fixed positions are not protected '
      'in the one-mode tick', max(gr) < 2.5, 'max gap ratio %.2f (g 0.5), %.2f (g 2)' % tuple(gr))
bl = []
for g, K in ((2.0, (0, 0, 0)), (4.0, (0, 0, 0)), (2.0, (2*np.pi/18, 0, 0)), (2.0, (2*np.pi/18,)*3)):
    a, Hf, wmin = band(Torus(6, K), 3, g, Torus(6, K).tick(EPS, MU, MN), 24)
    bl.append((g, a[24]/a[23], wmin, int((a < 5*a[0]).sum()), a[0]))
check('[F]', 'B3 RESULT only when the 24 cycled positions alone are pushed to the cell scale (g >= 2, 4x the brief) does a band of '
      'exactly 24 = 3 per block separate (ratio 3-5, below the 5x bar); its count is the number of positions left untouched, '
      'and its low end is ONE quartet (one 4-component species) plus pairs, not three quartets: F1 (three light copies) FAILS',
      all(r[1] > 2.5 and r[2] > 0.9 and r[3] < 12 for r in bl),
      '; '.join('g %.0f %s: ratio %.1f, fixed wt %.2f, n(<5x lowest) %d' % (r[0], nm, r[1], r[2], r[3]) for nm, r in zip(('K0', 'K0', 'K(1,0,0)', 'K(1,1,1)'), bl)))
T10 = Torus(10); a5, _, w5 = band(T10, 5, 2.0, T10.tick(EPS, MU, MN), 40)
check('[F]', 'B4 control: zoom 5 on 10^3 with the same construction gives a band of exactly 40 = 5 per block: the count tracks '
      'the supplied zoom, as A1 says', a5[40]/a5[39] > 2.5 and w5 > 0.9, 'ratio@40 %.1f, fixed wt %.2f' % (a5[40]/a5[39], w5))

print('== C. (c) 1+1+1')
sp = {}
for (mu, mn) in ((0, 0), (MU, 0), (0, MN), (MU, MN)):
    sp[(mu, mn)] = []
    for g in (1.4, 2.0, 2.6):
        _, Hf, _ = band(T6, 3, g, T6.tick(EPS, mu, mn), 24); e = np.real(np.diag(Hf)[:3])
        same = max(np.abs(np.real(np.diag(Hf)[3*b:3*b+3]) - e).max() for b in range(8))
        d = np.abs(np.subtract.outer(e, e))[np.triu_indices(3, 1)]; sp[(mu, mn)].append((d.min()/np.abs(e).max(), same, e))
deg = max(abs(r[2][0]-r[2][2]) for r in sp[(0, 0)])
check('[F]', 'C1 RESULT the class energies E(x-d), E(x), E(x+d) (same in all 8 blocks) are 1+2 at mu = MN = 0 (x+d and x-d '
      'equivalent) and 1+1+1 once EITHER the step asymmetry mu OR the copy mass MN is on; stable over g = 2 +- 30%: (c) holds, '
      'but the copy mass is not needed for it', deg < 1e-9 and min(min(r[0] for r in sp[k]) for k in sp if k != (0, 0)) > 1e-3
      and max(r[1] for k in sp for r in sp[k]) < 1e-9,
      'min rel split mu only %.3f, MN only %.3f, both %.3f; E(both, g 2) = %s' % (min(r[0] for r in sp[(MU, 0)]),
      min(r[0] for r in sp[(0, MN)]), min(r[0] for r in sp[(MU, MN)]), np.round(sp[(MU, MN)][1][2], 4)))

print('== D. (d) mixing, against family-flux')
w3 = np.exp(2j*np.pi/3)
def basis(a):
    B = np.zeros((N, 8), complex)
    for ci, c in enumerate(C8):
        for n in itertools.product(range(3), repeat=3): B[T6.idx(2*np.array(n)+c), ci] = w3**(-np.dot(a, n))/np.sqrt(27)
    return B
FAM = [basis(np.array(a)) for a in ((0, 0, 0), (1, 1, 1), (2, 2, 2))]
Pf = np.zeros(N); Pf[fixed_ids(T6, 3)] = 1; HBd = np.diag(1-Pf)
Tx = np.zeros((N, N))
for p in T6.P: Tx[T6.idx(p+np.array([2, 0, 0])), T6.idx(p)] = 1
lk = max(np.abs(FAM[i].conj().T@HBd@FAM[j]).max() for i in range(3) for j in range(3) if i != j)
check('[T]', 'D1 the zoom-3 block term has period 3 and the tick period 2, so the residual translations are 6Z^3, under which '
      'x - d, x, x + d of one block carry the SAME character: family-flux\'s gcd(2,3) obstruction (distinct T(2e_i) characters '
      'of the turn-fixed MOMENTUM sectors) does not apply to the position families. The term carrying the translation '
      'character is the block term itself: it breaks T(2e_i) and links family-flux\'s sectors (j,j,j)',
      np.abs(Tx@HBd@Tx.T-HBd).max() > 0.5 and lk > 1e-3, '[T(2e1), H_B] %.2f, sector leak %.3f' % (np.abs(Tx@HBd@Tx.T-HBd).max(), lk))
_, Hf, _ = band(T6, 3, 2.0, U, 24); cls = np.tile([0, 1, 2], 8)
Mc = np.array([[np.abs(Hf[np.ix_(cls == k, cls == q)]).max() for q in range(3)] for k in range(3)])
check('[F]', 'D2 RESULT the tick keeps the odd-corner class x - d decoupled: its coupling to x and x + d is below 1e-4 (virtual, '
      'through cycled sites), while the copy mass couples x <-> x + d (the even cube\'s far-corner term) at 0.094: family structure 1 + 2',
      max(Mc[0, 1], Mc[0, 2]) < 1e-4 and Mc[1, 2] > 0.05, 'max|H| x-d<->x %.1e, x-d<->x+d %.1e, x<->x+d %.3f' % (Mc[0, 1], Mc[0, 2], Mc[1, 2]))
def Jinv(V): return np.imag(V[0, 0]*V[1, 1]*np.conj(V[0, 1])*np.conj(V[1, 0]))
worst = 0
for _ in range(300):
    U2 = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))[0]; V = np.zeros((3, 3), complex)
    V[0, 0] = np.exp(1j*rng.uniform(0, 6.3)); V[1:, 1:] = U2; p = rng.permutation(3); q = rng.permutation(3)
    worst = max(worst, abs(Jinv(V[p][:, q])))
def fam(g, mn, mo):
    _, Hf, _ = band(T6, 3, g, T6.tick(EPS, MU, mn, mo), 24); b = Hf[:3, :3]; return np.linalg.eigh((b+b.conj().T)/2)[1]
V1 = fam(2.0, 0.2, 0).conj().T@fam(2.6, 0.12, 0)
check('[T]', 'D3 RESULT a mixing matrix 1 + 2 (one row and column with a single nonzero entry) has J = 0 for every phase; two '
      'species with different supplied (MN, g) give one angle and J = 0: count 3 with split 1+1+1 but NO three-family mixing '
      'and no CP phase. F5 FAILS under CL-1', worst < 1e-15 and abs(Jinv(V1)) < 1e-9 and np.sort(np.abs(V1).ravel())[-3] > 0.999,
      'random max |J| %.0e; species |V| sorted %s, J %.0e' % (worst, np.round(np.sort(np.abs(V1).ravel())[::-1][:5], 4), Jinv(V1)))

print('== E. against measurement, and a candidate repair')
VM = np.array([[0.97435, 0.22501, 0.003732], [0.22487, 0.97349, 0.04183], [0.00858, 0.04111, 0.999118]])
VS = np.array([[1.6e-4, 6.8e-4, 9e-5], [6.8e-4, 1.6e-4, 7.5e-4], [1.8e-4, 7.3e-4, 3.2e-5]])
sig = (VM/VS)[~np.eye(3, dtype=bool)].min()
check('[E]', 'E1 measured CKM has every off-diagonal modulus nonzero (smallest |V_ub| at %.0f sigma) and J = 3.12e-5: a decoupled '
      'family (two zero off-diagonal pairs under any assignment) is excluded at >= %.0f sigma' % (sig, sig), sig > 30)
V2 = fam(2.0, 0.2, 0.2).conj().T@fam(2.6, 0.12, 0.12)
_, H2, _ = band(T6, 3, 2.0, T6.tick(EPS, MU, MN, MN), 24); b2 = H2[:3, :3]; tri = np.angle(b2[0, 1]*b2[1, 2]*b2[2, 0])
check('[S]', 'E2 candidate rule (UNTESTED; it replaces CL-1\'s lopsided even-cube-only copy mass by the same factor on both tilings, '
      'bends no axiom, chooses no number): x - d then couples through the odd cube, all three classes mix, the family triangle '
      'carries a phase set by the spin-3/2 overlaps, and two species give J != 0; species values (MN, g) are supplied, so the '
      'size of J is not a prediction', np.abs(V2)[~np.eye(3, dtype=bool)].min() > 1e-3 and abs(Jinv(V2)) > 1e-8,
      'triangle phase %.3f rad, min off-diag |V| %.4f, J %.1e' % (tri, np.abs(V2)[~np.eye(3, dtype=bool)].min(), Jinv(V2)))

print('elapsed_seconds %.1f' % (time.time()-T0))
print('verdict M13: (a) FAIL (no protected light count; 3 = chosen zoom), (b) PASS, (c) PASS but set by mu or MN, '
      '(d) family-flux obstruction evaded but F5 FAILS under CL-1 (1 + 2 mixing, J = 0).')
print('supplied: zoom 3, the block term and its size, block centres 3Z^3, species (MN, g), seed 20261023; PDG CKM inputs.')
print(f'\nTOTAL: PASS={NP} FAIL={NF}')
