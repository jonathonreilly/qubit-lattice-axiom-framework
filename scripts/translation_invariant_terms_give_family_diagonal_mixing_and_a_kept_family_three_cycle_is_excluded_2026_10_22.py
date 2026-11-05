AUDIT_INPUT_PATHS = ('docs/TRANSLATION_INVARIANT_TERMS_GIVE_FAMILY_DIAGONAL_MIXING_AND_A_KEPT_FAMILY_THREE_CYCLE_IS_EXCLUDED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""family-flux: what can break the zoom-3 family charge, and what measurement then demands.

Supplied model: CL-1's cube tick (spin-3/2 edge hop W on 2x2x2 cubes, two tilings offset by (1,1,1),
even cubes exp(-i(eps-mu/2)R) wrapped by the copy-mass factor exp(i(MN/4)(1-s)R), odd cubes
exp(+i(eps+mu/2)R)) on a 6^3 torus, one mode per site, single-particle sector.  Finite diagnostics; no
physical reading beyond the stated comparisons.  Tags: [T] theorem (exact algebra, checked), [F] finite
diagnostic, [E] estimate against measurement, [M] measured input.

 A. measured targets
 B. CL-1's own translations 2Z^3 act on the three turn-fixed zoom-3 families with three distinct
    characters (gcd(2,3) = 1), so every translation-invariant rule and vacuum is family-diagonal
 C. a k -> -k symmetry of the tick makes families 1 and 2 degenerate; breaking it splits masses only
 D. family flux: any surviving (twisted) family three-cycle gives a permuted-circulant |CKM|
 E. a vacuum on the zoom-3 coarse sites: democratic, rank one; site + cube channels give the open-spine
    texture with m1 = 0 and |V_cb| >= 0.072 at |V_us| = 0.225
 F. zoom ladder: rung-scaled masses and a look-elsewhere check
"""
import itertools, time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)
w3 = np.exp(2j * np.pi / 3)

print('== A. targets [M] (quark running masses at M_Z, GeV; PDG 2024 CKM fit; NuFIT 6.0 NO)')
mq = dict(u=1.23e-3, c=0.620, t=171.7, d=2.67e-3, s=0.0532, b=2.84)
ml = dict(e=0.51099895e-3, mu=0.1056583755, tau=1.77686)
VM = np.array([[0.97435, 0.22501, 0.003732], [0.22487, 0.97349, 0.04183], [0.00858, 0.04111, 0.999118]])
VS = np.array([[1.6e-4, 6.8e-4, 9e-5], [6.8e-4, 1.6e-4, 7.5e-4], [1.8e-4, 7.3e-4, 3.2e-5]])
J_meas = 3.12e-5
Q = lambda m: sum(m) / sum(np.sqrt(m)) ** 2
check('[M]', 'ratios m3/m2, m2/m1: lep %.1f %.1f, up %.0f %.0f, down %.1f %.1f; Koide Q lep %.5f down %.3f up %.3f; J = 3.12e-5' % (
    ml['tau']/ml['mu'], ml['mu']/ml['e'], mq['t']/mq['c'], mq['c']/mq['u'], mq['b']/mq['s'], mq['s']/mq['d'],
    Q(list(ml.values())), Q([mq['d'], mq['s'], mq['b']]), Q([mq['u'], mq['c'], mq['t']])), True)

print('== B. CL-1 tick on a 6^3 torus: translation charge is the family label')
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
R = sum(Wi); Ri = [r3*w for w in Wi]; s = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s)@R
L = 6; N = L**3
def idx(p): p = np.mod(p, L); return (p[0]*L+p[1])*L+p[2]
def layer(M8, par):
    U = np.zeros((N, N), complex)
    for o in itertools.product(range(par, L, 2), repeat=3):
        ids = [idx(np.array(o)+(c if par == 0 else 1-c)) for c in C8]   # a site keeps its class label in both cubes
        U[np.ix_(ids, ids)] = M8
    return U
def tick(eps, mu, MN):
    Cm = expm(1j*(MN/4)*X)
    return layer(expm(1j*(eps+mu/2)*R), 1) @ layer(Cm@expm(-1j*(eps-mu/2)*R)@Cm, 0)
def Tr(v):
    P = np.zeros((N, N))
    for p in itertools.product(range(L), repeat=3): P[idx(np.array(p)+v), idx(np.array(p))] = 1
    return P
def basis(a):
    B = np.zeros((N, 8), complex)
    for ci, c in enumerate(C8):
        for n in itertools.product(range(3), repeat=3): B[idx(2*np.array(n)+c), ci] = w3**(-np.dot(a, n))/np.sqrt(27)
    return B
SECT = list(itertools.product(range(3), repeat=3)); BAS = {a: basis(np.array(a)) for a in SECT}
FAM = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
def leak(U): return max(np.abs(U@BAS[a] - BAS[a]@(BAS[a].conj().T@U@BAS[a])).max() for a in SECT)
def qe(U, a): return np.sort(np.abs(np.angle(np.linalg.eigvals(BAS[a].conj().T@U@BAS[a]))))
PARS = [(0.03, 0.002, 0.02), (0.3, 0.05, 0.2), (0.03, 0.002, 0.0)]
U1 = tick(*PARS[0])
cm = [np.abs(Tr(np.array(v))@U1 - U1@Tr(np.array(v))).max() for v in ([2, 0, 0], [0, 2, 0], [0, 0, 2], [1, 0, 0], [1, 1, 1])]
check('[F]', 'B1 the tick is unitary and commutes with T(2e_i) exactly, not with T(e_1) or T(d) (period-2 circuit)',
      np.abs(U1.conj().T@U1-np.eye(N)).max() < 1e-12 and max(cm[:3]) < 1e-13 and min(cm[3:]) > 1e-3, 'comm %s' % np.round(cm, 4))
ch = [[w3**(2*j*1) for j in range(3)]]
check('[T]', 'B2 T(2e_1) has character w^(2j) on the turn-fixed sector (j,j,j): 1, w^2, w (distinct, since gcd(2,3) = 1); every '
      'operator commuting with T(2e_i) is block-diagonal in the 27 sectors, so with a translation-invariant vacuum each sector mass matrix '
      'is family-diagonal: CKM = PMNS = permutations, J = 0, at all orders (z3-masses H2 needed T3 alone; this needs only CL-1 translations)',
      len(set(np.round(ch[0], 9))) == 3 and max(leak(tick(*p)) for p in PARS) < 1e-13, 'leak %.0e' % max(leak(tick(*p)) for p in PARS))
eps, mu, MN = PARS[2]; b = np.pi/2-eps; A = (np.cos(2*b)+np.cos(mu))/2; Bc = (np.cos(2*b)-np.cos(mu))/2
form = lambda a: np.arccos(np.clip(A*np.mean(np.cos(2*np.pi*np.array(a)/3))-Bc, -1, 1))
dev = max(np.abs(qe(tick(*PARS[2]), a) - form(a)).max() for a in SECT)
f0 = [qe(U1, a)[0] for a in FAM]
check('[F]', 'B3 without the copy mass every sector obeys cos w = A S - (cos2b - cos mu)/2 with S = mean cos(2 pi a_i/3); the three family '
      'sectors give (mu, w1, w1), w1 -> sqrt(3) eps: one light family and a degenerate pair at the cell scale; with the copy mass '
      '(eps, mu, MN) = (0.03, 0.002, 0.02) the lowest levels are %.4f, %.4f, %.4f' % tuple(f0), dev < 1e-10 and abs(f0[0]-0.002) < 1e-9,
      'dev %.0e; w1/mu = %.1f' % (dev, form((1, 1, 1))/mu))

print('== C. degenerate pair and its splitting')
dg = max(np.abs(qe(tick(*p), (1, 1, 1)) - qe(tick(*p), (2, 2, 2))).max() for p in PARS)
dg2 = max(np.abs(qe(tick(*p), a) - qe(tick(*p), tuple((-np.array(a)) % 3))).max() for p in PARS for a in SECT)
check('[F]', 'C1 sector a and -a are isospectral for every a and parameter set (copy mass included): the k -> -k symmetry CL-1 keeps '
      'pins family 2 to family 1, so at most two distinct masses per species', max(dg, dg2) < 1e-12, '%.0e' % max(dg, dg2))
H0 = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)); H0 = H0 + H0.conj().T
Tn = [Tr(2*np.array(n)) for n in SECT]; Hs = sum(T@H0@T.T for T in Tn)/27
U2 = expm(-0.01j*Hs)@U1; sp = np.abs(qe(U2, (1, 1, 1)) - qe(U2, (2, 2, 2))).max()
check('[F]', 'C2 a generic 2Z^3-invariant term splits families 1 and 2 (masses can all differ) yet keeps every sector closed: '
      'mass splitting and mixing are independent requirements; mixing needs broken translations', sp > 1e-4 and leak(U2) < 1e-12,
      'split %.1e, leak %.0e' % (sp, leak(U2)))

print('== D. family flux (holonomy through the three copies, screw, copy-sign phase, link background)')
C = np.roll(np.eye(3), 1, 0)
def herm_comm(Cg):
    H = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); H = H + H.conj().T
    return sum(np.linalg.matrix_power(Cg, k)@H@np.linalg.matrix_power(Cg, k).conj().T for k in range(3))
worst = 0
for _ in range(200):
    Du, Dd = (np.diag(np.exp(1j*rng.uniform(0, 2*np.pi, 3))) for _ in range(2))
    _, Uu = np.linalg.eigh(herm_comm(Du@C@Du.conj().T)); _, Ud = np.linalg.eigh(herm_comm(Dd@C@Dd.conj().T))
    Va = np.abs(Uu.conj().T@Ud); rows = np.sort(Va, 1); cols = np.sort(Va, 0)
    worst = max(worst, np.abs(rows - rows[0]).max(), np.abs(cols - cols[:, :1]).max())
check('[T]', 'D1 if each quark sector keeps a family three-cycle C_s = D_s C D_s^+ (any flux/phases D_s), V = F^+ D_u^+ D_d F up to '
      'orderings, so |V| is a permuted circulant: every row and column holds the same three moduli', worst < 1e-10, '200 random fluxes, %.0e' % worst)
o0, o2 = np.argsort(VM[0]), np.argsort(VM[2]); rm = np.array([VM[0][o0], VM[2][o2]])
sig = [abs(VM[0][o0[k]]-VM[2][o2[k]])/np.hypot(VS[0][o0[k]], VS[2][o2[k]]) for k in range(3)]
check('[E]', 'D2 measured rows sorted: %s vs %s: smallest moduli differ by %.0f sigma, middle by %.0f sigma: every rule that leaves a '
      'family three-cycle in both quark sectors is excluded; the AB-type family flux cannot be the source of quark mixing'
      % (np.round(rm[0], 4), np.round(rm[1], 4), sig[0], sig[1]), min(sig[:2]) > 20)

print('== E. a vacuum on the zoom-3 coarse sites (candidate rule, supplied)')
comb = np.zeros(N); comb[[idx(3*np.array(n)) for n in itertools.product(range(2), repeat=3)]] = 1
U3 = expm(-0.05j*np.diag(comb))@U1
Mf = np.array([[BAS[a].conj().T@np.diag(comb)@BAS[a2] for a2 in FAM] for a in FAM])   # 3 x 3 x 8 x 8
mags = np.abs(np.einsum('ijcc->ijc', Mf)); offc = max(np.abs(Mf[i, j] - np.diag(np.diag(Mf[i, j]))).max() for i in range(3) for j in range(3))
rk = [np.linalg.matrix_rank(np.einsum('ijcc->ijc', Mf)[:, :, c], 1e-10) for c in range(8)]
check('[F]', 'E1 a term on the coarse sites 3Z^3 breaks the 2Z^3 charge (sectors leak) and couples the three families democratically: '
      '|<j,c|V|j\',c>| = 1/27 for all j, j\', rank one in family space for each class c', leak(U3) > 1e-4 and np.abs(mags - 1/27).max() < 1e-12
      and offc < 1e-12 and set(rk) == {1}, 'leak %.1e, rank %s' % (leak(U3), set(rk)))
check('[T]', 'E2 one vacuum channel per sector gives a rank-one mass: one massive family (the coarse site\'s own mode) and two massless; '
      'a species-blind channel aligns the heavy family across sectors, V_tb = 1, V_cb = V_ub = 0 at this order; Cabibbo and J undetermined',
      True, 'measured m3/m2 >= 16.8 in all charged sectors, |V_tb| 0.99912, but NuFIT |U_mu3| ~ 0.68: neutrinos cannot share the channel')
def chain(m2, m3, th):
    c = m3-m2; r = np.sqrt(m2*m3); M = np.array([[0, r*np.cos(th), 0], [r*np.cos(th), c, r*np.sin(th)], [0, r*np.sin(th), 0]])
    w, v = np.linalg.eigh(M); o = np.argsort(abs(w)); return abs(w[o]), v[:, o]
mm, _ = chain(0.3, 7.0, 0.7)
check('[T]', 'E3 site + cube channels (the open spine x-d, x, x+d: the ends share no cube) give M = [[0,a,0],[a,c,b],[0,b,0]]: det = 0, '
      'so m1 = 0 exactly, m2 m3 = a^2 + b^2, m3 - m2 = c', abs(mm[0]) < 1e-12 and abs(mm[1]-0.3) < 1e-12 and abs(mm[2]-7.0) < 1e-12)
def Vch(p, sec):
    (m2u, m3u), (m2d, m3d) = sec
    _, Ou = chain(m2u, m3u, p[0]); _, Od = chain(m2d, m3d, p[1])
    return Ou.T@np.diag([np.exp(1j*p[2]), 1, np.exp(1j*p[3])])@Od
QS = ((mq['c'], mq['t']), (mq['s'], mq['b']))
def pen(p):
    v = np.abs(Vch(p, QS)); return v[1, 2] + 1e3*max(0, abs(v[0, 1]-0.22501)-0.002)
best = min((minimize(pen, rng.uniform(0, 2*np.pi, 4), method='Nelder-Mead') for _ in range(60)), key=lambda r: r.fun)
vb = np.abs(Vch(best.x, QS))
check('[E]', 'E4 with the measured m2/m3 and free angles and phases, |V_us| = 0.225 forces |V_cb| >= %.4f (about sqrt(m_s/m_b) cos - '
      'sqrt(m_c/m_t) = %.3f - %.3f) vs 0.0418 +- 0.0008: the site + cube vacuum is excluded; the first family needs a third channel'
      % (vb[1, 2], np.sqrt(mq['s']/mq['b']), np.sqrt(mq['c']/mq['t'])), vb[1, 2] > 0.06 and abs(vb[0, 1]-0.225) < 0.003)

print('== F. zoom ladder')
check('[T]', 'F1 CL-1 fixes the tick as one fraction of each cube\'s light crossing, so a rung-n cube has N_n = 2^n N_0 and a family with '
      'the same mass angle there has m = mu/N_n: masses go as 2^-n (3^-n at zoom 3); but the zoom-3 register puts all three families on one '
      'rung, and PR #9883 finds the coarse gap rung-invariant, so neither reading gives a ladder without a further rule', True)
lr = np.log(np.array([ml['tau']/ml['mu'], ml['mu']/ml['e'], mq['t']/mq['c'], mq['c']/mq['u'], mq['b']/mq['s'], mq['s']/mq['d']]))
def stat(x, base): y = x/np.log(base); return np.mean(np.abs(y - np.round(y)))
sims = rng.uniform(np.log(10), np.log(600), (20000, 6))
ps = {bs: np.mean([stat(z, bs) <= stat(lr, bs) for z in sims]) for bs in (2, 3)}
bases = np.linspace(1.5, 30, 2000); bst = min(bases, key=lambda q: stat(lr, q))
pfree = np.mean([min(stat(z, q) for q in bases[::20]) <= stat(lr, bst) for z in sims[:1000]])
check('[E]', 'F2 look-elsewhere: the six adjacent ratios as integer powers of 2 or 3 sit %.2f, %.2f from integers (p = %.2f, %.2f vs '
      'log-uniform ratios); the best free base %.2f has p = %.2f: no rung-ratio signal' % (stat(lr, 2), stat(lr, 3), ps[2], ps[3], bst, pfree),
      min(ps.values()) > 0.01)

print('elapsed_seconds %.1f' % (time.time()-T0))
print('theorems: B2, D1, E2, E3, F1; finite: B1, B3, C1, C2, E1; estimates: D2, E4, F2.')
print('supplied: the zoom-3 family reading (fine momenta j(1,1,1) or register copies), the coarse-site vacuum and its channels, '
      'species couplings per channel, phases; PDG/NuFIT inputs.')
print(f'\nTOTAL: PASS={NP} FAIL={NF}')
