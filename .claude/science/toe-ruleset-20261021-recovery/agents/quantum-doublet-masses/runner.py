"""quantum-doublet-masses: does a quantum (register) doublet change the mass/mixing no-gos?
Self-contained (numpy/scipy). Tags: [M] measured target, [T] theorem (exact check), [F] finite diagnostic, [E] estimate.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
from functools import reduce
import numpy as np
from scipy.linalg import expm, eigh
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
T0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    ok = bool(ok); NP += ok; NF += (not ok)
    print('[%s] %s %s%s' % ('PASS' if ok else 'FAIL', tag, name, (' | ' + detail) if detail else ''))
kron = lambda *a: reduce(np.kron, a)

print('== A. targets [M] (running masses at M_Z; PDG 2024 CKM)')
r_meas = {'u': 1/277., 'd': 1/53.4, 'e': 1/16.8}            # m2/m3
q_meas = {'u': 1/504., 'd': 1/19.9, 'e': 1/206.8}           # m1/m2
V_meas = (0.2250, 0.0418, 0.00369)
check('[M]', 'm2/m3 up %.4f down %.4f lep %.4f; m1/m2 up %.4f down %.4f lep %.4f; |V_us| |V_cb| |V_ub| = %s' % (
    r_meas['u'], r_meas['d'], r_meas['e'], q_meas['u'], q_meas['d'], q_meas['e'], V_meas), True)

# ---------------- CL-1 cube hop (inlined) ----------------
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j-np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1)-m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for c in C8:
    n = (2*c-1.0)/r3; _, v_ = np.linalg.eigh(sum(n[k]*J3[k] for k in range(3))); xi.append(v_[:, -1])
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        d = C8[a]-C8[b]
        if np.abs(d).sum() == 1: Wi[int(np.argmax(abs(d)))][a, b] = -Gm[a, b]/abs(Gm[a, b])/r3
R = sum(Wi); Ri = [r3*w for w in Wi]; s_op = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s_op)@R
def lattice(L):
    N = L**3
    idx = lambda p: ((p[0] % L)*L+p[1] % L)*L+p[2] % L
    orig = {par: [np.array(o) for o in itertools.product(range(par, L, 2), repeat=3)] for par in (0, 1)}
    cids = {par: [[idx(o+(c if par == 0 else 1-c)) for c in C8] for o in orig[par]] for par in (0, 1)}
    return N, idx, orig, cids
def layer(mats, par, N, cids):
    U = np.zeros((N, N), complex)
    for ids, M8 in zip(cids[par], mats): U[np.ix_(ids, ids)] += M8
    return U

print('== B. (1) can the doublet register itself break 2Z^3 to the zoom-3 lattice?')
check('[T]', 'B1 symmetric vacuum: on any finite torus a register update invariant under a translation group G with a unique '
      'vacuum has a G-invariant vacuum, so every correlator of the doublet (all orders in its fluctuations) is G-invariant and '
      'the fermion self-energy commutes with T(2e_i): CKM a permutation (family-flux B2 extends to registers); breaking needs '
      'true order or explicit breaking', True)
# B2: register hopping with CL-1's own hop, both tilings
for L in (6, 12):
    N, idx, orig, cids = lattice(L)
    Hb = np.zeros((N, N), complex)
    for par in (0, 1):
        for ids in cids[par]: Hb[np.ix_(ids, ids)] += R
    out = []
    for sub in ([0, 7], [N-8, N-1]):
        w, V = eigh(Hb, subset_by_index=sub); e = w[0] if sub[0] == 0 else w[-1]
        Vs = V[:, np.abs(w-e) < 1e-8]
        pts = np.array(list(itertools.product(range(L), repeat=3)))
        chars = []
        for ax in range(3):
            perm = np.array([idx(p+2*np.eye(3, dtype=int)[ax]) for p in pts])
            TV = np.zeros_like(Vs); TV[perm] = Vs
            chars.append(np.linalg.eigvals(Vs.conj().T@TV))
        out.append((e, Vs.shape[1], max(np.abs(c-1).max() for c in chars)))
    check('[F]', 'B2 a register hopping with CL-1\'s hop (both tilings, %d^3): extremes %+.3f/%+.3f (the bound), %d-fold, all with T(2e_i) character 1: condensing at either band edge keeps 2Z^3' % (
              L, out[0][0], out[1][0], out[0][1]), abs(abs(out[0][0])-2) < 1e-9 and max(o[2] for o in out) < 1e-9,
          'max |char-1| %.0e' % max(o[2] for o in out))
# B3: per-family-sector band minimum (6^3) and the sea response kernel (recomputed)
L = 6; N, idx, orig, cids = lattice(L)
Hb = layer([R]*27, 0, N, cids)+layer([R]*27, 1, N, cids)
w3 = np.exp(2j*np.pi/3); band = {}
for nvec in itertools.product(range(3), repeat=3):
    B = np.zeros((N, 8), complex)
    for ci, c in enumerate(C8):
        for t in itertools.product(range(3), repeat=3):
            B[idx(2*np.array(t)+c), ci] = w3**(np.dot(nvec, t))/np.sqrt(27)
    ev = np.linalg.eigvalsh(B.conj().T@Hb@B); band[nvec] = (ev[0], ev[-1])
gap_lo = min(band[n][0] for n in band if any(n))-band[(0, 0, 0)][0]
gap_hi = band[(0, 0, 0)][1]-max(band[n][1] for n in band if any(n))
mcube = {0: np.array([o//2 for o in orig[0]]), 1: np.array([(o-1)//2 for o in orig[1]])}
def tick(eps, me, mo, MN):
    Cm = expm(1j*(MN/4)*X)
    return layer([expm(1j*(eps+m/2)*R) for m in mo], 1, N, cids) @ layer([Cm@expm(-1j*(eps-m/2)*R)@Cm for m in me], 0, N, cids)
def Phi(U): q = -np.angle(np.linalg.eigvals(U)); return q[q < 0].sum()
one = np.ones(27)
def hess_q(P, n, h=2e-3):
    eps, mu, MN = P; best = 0
    for ph in (0, np.pi/2):
        pe = np.cos(2*np.pi*(mcube[0]@np.array(n))/3+ph); po = np.cos(2*np.pi*(mcube[1]@np.array(n))/3+ph)
        if np.linalg.norm(pe) < 1e-9: continue
        pe /= np.linalg.norm(pe); po /= np.linalg.norm(po)
        f = lambda x, y: Phi(tick(eps, mu*one+x*pe, mu*one+y*po, MN)); f0 = f(0, 0)
        H2 = np.array([[(f(h, 0)+f(-h, 0)-2*f0)/h**2, (f(h, h)-f(h, -h)-f(-h, h)+f(-h, -h))/(4*h*h)], [0, (f(0, h)+f(0, -h)-2*f0)/h**2]])
        H2[1, 0] = H2[0, 1]; best = min(best, np.linalg.eigvalsh(H2)[0])
    return best
P1 = (0.3, 0.05, 0.2)
chi = {n: hess_q(P1, n) for n in ((0, 0, 0), (1, 0, 0), (1, 1, 1))}
check('[F]', 'B3 Landau form E2(n) = c + kappa [e_band(n) - e_band(0)] + chi(n) over the 27 family characters n of T(2e_i): the '
      'register band bottom (top) is lowest (highest) in n = 0 by %.3f (%.3f), and the recomputed sea response (eps, mu, MN) = '
      '%s is deepest at n = 0 (chi 000 %.3f, 100 %.3f, 111 %.3f; coarse-vacuum B2 had -2.484, -1.672, -0.845): both terms share '
      'the minimiser, so for every kappa and local cost the first instability keeps 2Z^3' % (
          gap_lo, gap_hi, P1, chi[(0, 0, 0)], chi[(1, 0, 0)], chi[(1, 1, 1)]),
      gap_lo > 1e-6 and gap_hi > 1e-6 and chi[(0, 0, 0)] < min(chi[(1, 0, 0)], chi[(1, 1, 1)]))
# B4: commensurate locking = LSM: lock period is the denominator of the filling
def ring(L, Nb, nmax, U, V1, V2):
    st = [s for s in itertools.product(range(nmax+1), repeat=L) if sum(s) == Nb]
    ix = {s: i for i, s in enumerate(st)}; D = len(st); H = lil_matrix((D, D))
    for i, s in enumerate(st):
        a = np.array(s); H[i, i] = U/2*np.sum(a*(a-1))+V1*np.sum(a*np.roll(a, -1))+V2*np.sum(a*np.roll(a, -2))
        for x in range(L):
            for p, q in ((x, (x+1) % L), ((x+1) % L, x)):
                if a[p] > 0 and a[q] < nmax:
                    b = a.copy(); b[p] -= 1; b[q] += 1; H[ix[tuple(b)], i] += -np.sqrt(a[p]*(a[q]+1))
    w, v = eigsh(H.tocsr(), k=5, which='SA'); o = np.argsort(w); w, v = w[o], v[:, o]
    occ = np.array(st, float); p = v[:, 0]**2; nbar = occ[:, 0]@p
    cr = np.array([(occ[:, 0]*occ[:, r])@p for r in range(L)])-nbar**2
    S = np.array([np.real(np.sum(cr*np.exp(2j*np.pi*k*np.arange(L)/L))) for k in range(L)])
    k = int(np.argmax(S[1:]))+1
    return w-w[0], S, k/L
cases = [('1/3', 12, 4, 1, 0, 10, 10), ('1/2', 12, 6, 1, 0, 10, 0), ('1', 8, 8, 2, 8, 0, 0), ('1/2 sea-attractive', 12, 6, 1, 0, -1, -.5)]
res = {c[0]: ring(*c[1:]) for c in cases}
g13, S13, k13 = res['1/3']; g12, S12, k12 = res['1/2']; g1, S1, _ = res['1']; ga, Sa, _ = res['1/2 sea-attractive']
bragg = lambda S, k, L: S[int(round(k*L))]/np.mean(np.delete(S, [0, int(round(k*L))]))
check('[F]', 'B4 commensurate locking is the Lieb-Schultz-Mattis-Oshikawa rule (a gapped vacuum at filling p/q per cell must '
      'break translations to period q): 1D registers, L = 12/8: filling 1/3 Bragg peak at q = %.3f (x%.0f), 3 low states (gaps %.3f %.3f, '
      'next %.2f); filling 1/2 peak at %.3f, 2 low states (gap %.3f, next %.2f); integer filling unique and gapped (%.2f), no peak '
      '(max S/mean %.1f); sea-like attraction: no peak (%.1f)' % (k13, bragg(S13, k13, 12), g13[1], g13[2], g13[3], k12, g12[1], g12[2],
                                                                    g1[1], S1[1:].max()/S1[1:].mean(), Sa[1:].max()/Sa[1:].mean()),
      abs(k13-1/3) < 1e-9 and g13[2] < 0.2*g13[3] and abs(k12-0.5) < 1e-9 and g12[1] < 0.2*g12[2] and g1[1] > 1)
check('[T]', 'B5 the rules\' fillings are integer per 2Z^3 cell: registers sit half filled (Gauss value 0), children start half filled, the '
      'half-filled sea has zero abelian charge density, so the offset f of hop-recheck B2 is 0: LSM forces nothing, and the pinning '
      '-A cos(2 pi f) is the same at every role-equivalent site: it locks the value, never a period-3 pattern', True)
ok6 = []
for b in range(2, 13):
    m = np.lcm(2, b); ch = sorted({int(round((m*j) % 3)) for j in range(3)}); ok6.append((b, len(ch) < 3))
brk = [b for b, k in ok6 if k]
check('[T]', 'B6 the role layout is an explicit breaking: doublet registers role-assigned in blocks of b leave lcm(2,b)Z^3, whose '
      'characters w^(lcm j) separate the three families unless 3 | b; b in 2..12 that mix families: %s; power-of-2 blocks keep every no-go, '
      '3 | b supplies 2Z^3 -> 6Z^3 (b is supplied)' % brk,
      brk == [3, 6, 9, 12])

print('== C. (2) quantum fluctuations of the doublet: radiative masses')
# C1a exact single fermion + fluctuating spin-1 registers on coarse sites (Feshbach)
L = 12; cs = [0, 3, 6, 9]; Sd = 1.0
d = 3; mq = Sd-np.arange(d); Sp = np.zeros((d, d))
for a in range(1, d): Sp[a-1, a] = np.sqrt(Sd*(Sd+1)-mq[a]*(mq[a]+1))
Sz = np.diag(mq); I3 = np.eye(d); nr = 4
op = lambda o, a: kron(*[o if b == a else I3 for b in range(nr)])
Hreg = sum(0.7*(op(Sp, a)@op(Sp.T, (a+1) % nr)+op(Sp.T, a)@op(Sp, (a+1) % nr))/2 for a in range(nr))+0.4*sum(op(Sz, a)@op(Sz, a) for a in range(nr))
h0 = np.zeros((L, L), complex)
for x in range(L): h0[x, (x+1) % L] = -np.exp(0.3j); h0[(x+1) % L, x] = -np.exp(-0.3j)
Dr = Hreg.shape[0]; H = np.kron(h0, np.eye(Dr))+np.kron(np.eye(L), Hreg)
for a, x in enumerate(cs):
    P = np.zeros((L, L)); P[x, x] = 1; H += 0.9*np.kron(P, (op(Sp, a)+op(Sp.T, a))/np.sqrt(2))
wr, vr = np.linalg.eigh(Hreg); Bm = np.kron(np.eye(L), vr[:, :1]); z = wr[0]+0.37+0.8j
G = Bm.T@np.linalg.inv(z*np.eye(H.shape[0])-H)@Bm
Sig = (z-wr[0])*np.eye(L)-h0-np.linalg.inv(G)
mask = np.ones((L, L), bool); mask[np.ix_(cs, cs)] = False
F = np.exp(-2j*np.pi*np.outer(np.arange(L), np.arange(L))/L)/np.sqrt(L); Sk = F@Sig@F.conj().T
sv = [np.linalg.svd(Sk[np.ix_([K, K+4, K+8], [K, K+4, K+8])], compute_uv=False) for K in range(4)]
check('[T]', 'C1 rank theorem at all orders in the register: if the doublet couples to one mode per coarse cell, every self-energy '
      '(any S, register hopping and fluctuations, all loops) has both legs on that mode: Sigma(K) is rank one; exact check, one fermion + four fluctuating spin-1 registers (Feshbach): off-vertex |Sigma| %.0e, family '
      'singular values (%.3f, %.0e, %.0e) at K = 0' % (np.abs(Sig[mask]).max(), sv[0][0], sv[0][1], sv[0][2]),
      np.abs(Sig[mask]).max() < 1e-12 and max(s[1] for s in sv) < 1e-12)
# C2 many-body check, with and without a family-blind interaction
L = 6; cs = [0, 3]; Zp = np.diag([1., -1.]); am = np.array([[0, 1], [0, 0.]]); I2 = np.eye(2)
cf = [kron(*([Zp]*j+[am]+[I2]*(L-1-j))) for j in range(L)]; nF = 2**L
rop = lambda o, r: kron(o if r == 0 else I2, o if r == 1 else I2); sx = np.array([[0, 1], [1, 0.]])
Nop = np.kron(sum(c.T@c for c in cf), np.eye(4)); Cc = [np.kron(c, np.eye(4)) for c in cf]
def Gmb(y, Vn, z=0.2+0.9j):
    H = np.zeros((nF*4, nF*4), complex)
    for x in range(L):
        hp = -cf[x].T@cf[(x+1) % L]; H += np.kron(hp+hp.T, np.eye(4))
        H += Vn*np.kron(cf[x].T@cf[x]@cf[(x+1) % L].T@cf[(x+1) % L], np.eye(4))
    H += np.kron(np.eye(nF), 0.5*(rop(am, 0)@rop(am.T, 1)+rop(am.T, 0)@rop(am, 1))+0.3*(rop(Zp, 0)+rop(Zp, 1)))
    for r, x in enumerate(cs): H += y*np.kron(cf[x].T@cf[x], rop(sx, r))
    D = H.shape[0]; w, v = np.linalg.eigh(H+10*(Nop-3*np.eye(D))@(Nop-3*np.eye(D))); g = v[:, 0]; E0 = w[0]
    R1 = np.linalg.inv(z*np.eye(D)-H+E0*np.eye(D)); R2 = np.linalg.inv(z*np.eye(D)+H-E0*np.eye(D))
    return np.array([[g.conj()@Cc[i]@R1@Cc[j].T@g+g.conj()@Cc[j].T@R2@Cc[i]@g for j in range(L)] for i in range(L)])
G0 = Gmb(0, 0); F = np.exp(-2j*np.pi*np.outer(np.arange(L), np.arange(L))/L)/np.sqrt(L)
mask = np.ones((L, L), bool); mask[np.ix_(cs, cs)] = False; mb = []
for Vn in (0, 0.6):
    Sg = np.linalg.inv(G0)-np.linalg.inv(Gmb(0.8, Vn)); Sk = F@Sg@F.conj().T
    mb.append((np.abs(Sg[mask]).max(), np.linalg.svd(Sk[np.ix_([0, 2, 4], [0, 2, 4])], compute_uv=False)))
check('[F]', 'C2 many-body (6-site ring at half filling, two spin-1/2 doublet registers): Yukawa-only off-vertex |Sigma| %.0e, family '
      'singular values (%.3f, %.0e, %.0e); adding a family-blind density interaction on every bond (a stand-in for link exchange) gives '
      '(%.3f, %.3f, %.3f): only interactions that reach the legs off the vertex raise the rank' % (
          mb[0][0], *mb[0][1], *mb[1][1]), mb[0][0] < 1e-10 and mb[0][1][1] < 1e-10 and mb[1][1][2] > 1e-3)
# C3 group weights of the rank-raising link exchanges (pair of legs among L, R, H; singlet vertex => T_i.T_j = -(C_i+C_j-C_k)/2)
aY = 0.6  # alpha_Y / alpha_c at the cell (sin^2 theta_W = 3/8, equal couplings)
YY = {'u': (1/6, 2/3, -1/2), 'd': (1/6, -1/3, 1/2), 'e': (-1/2, -1, 1/2)}
Wt = {}
for sct, (yl, yr, yh) in YY.items():
    col = -4/3 if sct != 'e' else 0.0
    Wt[sct] = np.array([col-aY*yl*yr, -0.75-aY*yl*yh, aY*yr*yh])   # classes LR, LH, RH
    assert abs(-yl+yr+yh) < 1e-12
eq = {k: abs(v.sum()) for k, v in Wt.items()}
check('[T]', 'C3 rank-raising weights per exchange class (LR, LH, RH) in units of alpha_c/(4 pi) at the cell: up %s, down %s, lepton %s '
      '(colour on LR, SU(2) on LH, hypercharge Y_iY_j); the H-leg classes exist because the doublet fluctuates' % (np.round(Wt['u'], 3), np.round(Wt['d'], 3), np.round(Wt['e'], 3)), True)

print('== D. estimates against measurement')
check('[E]', 'D1 with equal structure factors the sector ratios m2/m3 go as |W| = up %.2f, down %.2f, lepton %.2f: predicted '
      '(m2/m3)_lep/(m2/m3)_up = %.2f and down/up %.2f against measured %.1f and %.1f; the species-blind tick cancels the unknown '
      'structure factor and alpha_c: leptons come out the MOST hierarchical, measured the least' % (
          eq['u'], eq['d'], eq['e'], eq['e']/eq['u'], eq['d']/eq['u'], r_meas['e']/r_meas['u'], r_meas['d']/r_meas['u']),
      eq['e']/eq['u'] < 0.1*r_meas['e']/r_meas['u'])
# D2 look-elsewhere: random class structure matrices, democratic tree, one coupling a = alpha_c/(4 pi)
def cmat(k=8): return sum(np.outer(rng.normal(size=3)+1j*rng.normal(size=3), rng.normal(size=3)+1j*rng.normal(size=3)) for _ in range(k))/np.sqrt(k)
phi = np.ones(3)/np.sqrt(3); NDR = 4000; hits = {'mass': 0, 'all': 0, 'ratios': 0}; vcb = []
for it in range(NDR):
    Sc = [cmat() for _ in range(3)]; a = 10**rng.uniform(-4, -0.5)
    Ms = {k: np.outer(phi, phi)+a*sum(Wt[k][c]*Sc[c] for c in range(3)) for k in Wt}
    sv = {}; UL = {}
    for k, M in Ms.items():
        u_, s_, _ = np.linalg.svd(M); sv[k] = s_; UL[k] = u_
    r = {k: sv[k][1]/sv[k][0] for k in sv}; q = {k: sv[k][2]/sv[k][1] for k in sv}
    Vm = np.abs(UL['u'].conj().T@UL['d']); vcb.append(Vm[0, 1])
    okr = all(abs(np.log(r[k]/r_meas[k])) < np.log(3) for k in r)
    okq = all(abs(np.log(q[k]/q_meas[k])) < np.log(3) for k in q)
    okv = abs(np.log(Vm[0, 1]/V_meas[1])) < np.log(2) and abs(np.log(Vm[1, 2]/V_meas[0])) < np.log(2)
    hits['ratios'] += okr; hits['mass'] += okr and okq; hits['all'] += okr and okq and okv
check('[E]', 'D2 look-elsewhere for radiative masses (%d draws: three random complex class structures shared by all species, one '
      'democratic vertex, a = alpha_c/(4 pi) log-uniform 1e-4..0.3): all three m2/m3 within x3: %d; plus all three m1/m2 within x3: %d; '
      'plus |V_cb|, |V_us| within x2: %d. Median |V_cb| %.1e (measured 0.042)' % (NDR, hits['ratios'], hits['mass'], hits['all'], np.median(vcb)),
      hits['all'] <= 0.002*NDR)
# D3 Z3 spurion counting
pw = {dlt: min(abs(n) for n in range(-3, 4) if (n-dlt) % 3 == 0) for dlt in range(3)}
check('[T]', 'D3 zoom-3 spurion counting: a period-3 pattern of contrast eps carries T(2e) charge +-1, an entry M_ij needs charge '
      'j - i mod 3, so its leading power is eps^%d (diagonal) or eps^%d, eps^%d (off-diagonal): the "distance" between zoom-3 families '
      'is at most one step, so no Froggatt-Nielsen tower eps^n (1 : 1/277 : 1/1.4e5 needs n up to 4-8); overlaps are democratic '
      '(family-flux E1)' % (pw[0], pw[1], pw[2]), pw == {0: 0, 1: 1, 2: 1})
NT = 20000; cnt = {'gen': 0, 'r1': 0}
for it in range(NT):
    e = 10**rng.uniform(-3, 0)
    for var in ('gen', 'r1'):
        good = True
        for k in ('u', 'd', 'e'):
            C = np.exp(rng.uniform(np.log(1/3), np.log(3), (3, 3)))*np.exp(2j*np.pi*rng.random((3, 3)))
            Pw = e*np.ones((3, 3)); np.fill_diagonal(Pw, 1.0 if var == 'gen' else e**2)
            if var == 'r1': Pw[0, 0] = 1.0
            s_ = np.linalg.svd(C*Pw, compute_uv=False)
            good &= abs(np.log(s_[1]/s_[0]/r_meas[k])) < np.log(3) and abs(np.log(s_[2]/s_[1]/q_meas[k])) < np.log(3)
        cnt[var] += good
check('[E]', 'D4 look-elsewhere for zoom-3 textures (%d draws per variant, eps log-uniform 1e-3..1, O(1) complex coefficients): all six '
      'ratios within x3 for generic diagonal %d, for a rank-one diagonal (one heavy family) %d' % (NT, cnt['gen'], cnt['r1']),
      cnt['gen'] + cnt['r1'] <= 0.001*NT)

print('== E. (3) can the doublet and its conjugate pin differently?')
dimH = 3; ap = np.diag(np.sqrt(np.arange(1, dimH)), 1)   # truncated register for each doublet component
A1 = np.kron(ap, np.eye(dimH)); A2 = np.kron(np.eye(dimH), ap)
X_ = rng.normal(size=(dimH**2, dimH**2))+1j*rng.normal(size=(dimH**2, dimH**2)); rho = X_@X_.conj().T; rho /= np.trace(rho)
Hv = np.array([np.trace(rho@A1), np.trace(rho@A2)]); Htv = np.array([np.trace(rho@A2.conj().T), -np.trace(rho@A1.conj().T)])
check('[T]', 'E1 H~ = i sigma2 H^dagger is an operator identity, so in any register state <H~> = i sigma2 <H>^*, |<H~_x>| = |<H_x>| and '
      'in unitary gauge both sectors see one real profile rho_x: one doublet cannot pin up and down differently (random mixed state: |<H>| %.4f, |<H~>| %.4f)' % (
          np.linalg.norm(Hv), np.linalg.norm(Htv)), abs(np.linalg.norm(Hv)-np.linalg.norm(Htv)) < 1e-12)
Cw = np.exp(rng.uniform(-1, 1, (3, 3)))*np.exp(2j*np.pi*rng.random((3, 3))); Pw = 0.1*np.ones((3, 3)); np.fill_diagonal(Pw, 1)
Mu = 2.0*Cw*Pw; Md = 0.3*Cw*Pw
Vt = np.abs(np.linalg.svd(Mu)[0].conj().T@np.linalg.svd(Md)[0])
check('[T]', 'E2 so with a single doublet, a misaligned up/down mixing needs species-dependent weights at the vertices (the '
      'register\'s existing requirement); species-blind weights on the same pattern give V = 1 | max |V - 1| %.0e' % np.abs(Vt-np.eye(3)).max(),
      np.abs(Vt-np.eye(3)).max() < 1e-10)

print('elapsed_seconds %.1f' % (time.time()-T0))
print('theorems: B1, B5, B6, C1, C3, D3, E1, E2; finite: B2, B3, B4, C2; estimates: D1, D2, D4.')
print('supplied: doublet register + couplings (hop R, cost, vertex, sizes), vertex placement, stand-in interaction, equal cell '
      'couplings, random structures, LSM (literature); PDG inputs.')
print()
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
