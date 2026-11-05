#!/usr/bin/env python3
"""Can the record/response layer (CL-3 records, CL-4 transport, CL-5 response) give net chirality?
1 free 1D Margolus tick: det U(k) constant, per-quasi-energy balance, real-space flow 0;
2 pathwise flow under the full layer (2 fermion relays, CL-4 transport, CL-5-style links and lengths, adversarial demon);
3 CL-4 Born tracking under CL-5 feedback (exact branching) and inversion covariance of the whole layer;
4 the variant the laws forbid: records condition the odds, ratchet feedback (drift vs coherence);
5 averaged (Born-mean) propagators of index-0 histories: point-gap winding and its damping price;
6 register bypass: a chiral flow on matter needs coherent blank registers carrying the reverse flow;
7 3D: CL-2 tick W3 with frames and histories; magnetic flow index = W3 x N_phi (control) and 0 for the tick;
8 against measurement.  Supplied models, finite diagnostics; no physical identification."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from scipy.sparse.csgraph import connected_components

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ============================================================== 1D Margolus tick (CL-2 analogue)
def blk(a): return np.array([[np.cos(a), -1j*np.sin(a)], [-1j*np.sin(a), np.cos(a)]])
def Uk1(k, eps, mu):
    Be = blk(eps - mu/2); b = -(eps + mu/2); c, s = np.cos(b), -1j*np.sin(b)
    return np.array([[c, s*np.exp(1j*k)], [s*np.exp(-1j*k), c]]) @ Be     # odd block couples B_n with A_{n+1}
def half_ring(L, off, B):
    M = np.zeros((L, L), complex)
    for n in range(L//2):
        i, j = (2*n+off) % L, (2*n+1+off) % L; M[np.ix_([i, j], [i, j])] = B
    return M
def flow(V, L, w, cut=0):
    """net probability crossing the cut left->right from the uniform state (window w around one cut of the ring)"""
    x = (np.arange(L) - cut) % L; x = np.where(x >= L//2, x - L, x); P = np.abs(V)**2
    R = (x >= 0) & (x < w); Lf = (x < 0) & (x >= -w)
    return P[np.ix_(R, Lf)].sum() - P[np.ix_(Lf, R)].sum()

print('== 1. free 1D Margolus tick')
ks = np.linspace(-np.pi, np.pi, 2001) + 1e-4; W1max = 0.0; bal = []
for eps, mu in ((np.pi/2, 0.0), (1.2, 0.0), (1.2, 0.3)):
    d = np.array([np.linalg.det(Uk1(k, eps, mu)) for k in ks]); W1max = max(W1max, abs(np.sum(np.angle(d[1:]/d[:-1]))/(2*np.pi)))
    ws = np.array([np.angle(np.linalg.eigvals(Uk1(k, eps, mu))) for k in ks]); ws.sort(axis=1)
    for w0 in (0.5, 2.0):
        nR = nL = 0
        for b_ in range(2):
            e = ws[:, b_]; dd = np.angle(np.exp(1j*(e - w0)))
            for i in np.where((np.sign(dd[1:]) != np.sign(dd[:-1])) & (abs(dd[1:] - dd[:-1]) < 1))[0]:
                nR += e[i+1] > e[i]; nL += e[i+1] < e[i]
        bal.append((int(nR), int(nL)))
check('det U(k) constant (W1 = 0) and every quasi-energy crossing balanced, for 3 (eps, mu)',
      W1max < 1e-9 and all(a == b for a, b in bal) and sum(a for a, _ in bal) > 0, f'max|W1| {W1max:.1e}; (nR,nL) {bal[:4]}')
L1 = 32; U1 = half_ring(L1, 1, blk(-1.5)) @ half_ring(L1, 0, blk(1.2)); Usw = half_ring(16, 1, blk(-np.pi/2)) @ half_ring(16, 0, blk(np.pi/2))
e4 = np.zeros(16); e4[4] = 1; e5 = np.zeros(16); e5[5] = 1
check('real-space flow of U^3 = 0; swap tick moves even sites +2 (right-movers), odd sites -2 (left-movers)',
      abs(flow(np.linalg.matrix_power(U1, 3), L1, 8)) < 1e-12 and np.argmax(abs(Usw @ e4)) == 6 and np.argmax(abs(Usw @ e5)) == 3,
      f'flow {flow(np.linalg.matrix_power(U1, 3), L1, 8):+.1e}')

# ============================================================== 2-fermion ring with the record/response layer
class Ring:
    def __init__(self, L):
        self.L = L; self.confs = list(itertools.combinations(range(L), 2)); self.NC = len(self.confs)
        self.cidx = {c: i for i, c in enumerate(self.confs)}
        occ = np.array([[1 if s in c else 0 for s in range(L)] for c in self.confs]); self.occ = occ
        self.HAM = 4 - 2*(occ @ occ.T)                                           # changed mode occupations
        self.A = np.array([c[0] for c in self.confs]); self.B = np.array([c[1] for c in self.confs])
    def bonds(self, off): return [((2*n+off) % self.L, (2*n+1+off) % self.L) for n in range(self.L//2)]
    def half(self, off, phi, a):
        V = np.zeros((self.L, self.L), complex)
        for bi, (x, y) in enumerate(self.bonds(off)):
            V[x, x] = V[y, y] = np.cos(a[bi]); V[y, x] = -1j*np.sin(a[bi])*np.exp(1j*phi[bi]); V[x, y] = -1j*np.sin(a[bi])*np.exp(-1j*phi[bi])
        return V
    def wedge(self, V):
        A, B = self.A, self.B; return V[np.ix_(A, A)]*V[np.ix_(B, B)] - V[np.ix_(A, B)]*V[np.ix_(B, A)]
    def amp(self, Psi, a, b):
        return 0j if a == b else (Psi[self.cidx[(a, b)]] if a < b else -Psi[self.cidx[(b, a)]])
    def plan_row(self, p, q, M, X):
        """CL-4 on X's support component: support of M (stays included), fewest changed occupations, max entropy"""
        S = np.abs(M) > 1e-13; nc, lab = connected_components(sp.csr_matrix(S | S.T), directed=False)
        comp = np.where(lab == lab[X])[0]; n = len(comp)
        if n == 1: return comp, np.array([1.0]), 0.0
        pc = p[comp]/p[comp].sum(); qc = q[comp]/q[comp].sum()
        tgt, src = np.nonzero(S[np.ix_(comp, comp)]); keep = (pc[src] > 1e-15) & (qc[tgt] > 1e-15); src, tgt = src[keep], tgt[keep]
        pc = np.where(pc > 1e-15, pc, 0); qc = np.where(qc > 1e-15, qc, 0); pc /= pc.sum(); qc /= qc.sum()
        cost = self.HAM[comp[tgt], comp[src]].astype(float); m = len(src)
        Aeq = sp.vstack([sp.csr_matrix((np.ones(m), (src, np.arange(m))), shape=(n, m)),
                         sp.csr_matrix((np.ones(m), (tgt, np.arange(m))), shape=(n, m))]).tocsr()
        r = linprog(cost, A_eq=Aeq, b_eq=np.concatenate([pc, qc]), bounds=(0, None), method='highs')
        y = r.eqlin.marginals; f = cost - y[src] - y[n+tgt] < 1e-9; fs, ft = src[f], tgt[f]; u = np.ones(n); v = np.ones(n)
        for it in range(20000):
            rs = np.bincount(fs, v[ft], minlength=n); u = np.where(rs > 0, pc/np.where(rs > 0, rs, 1), 0)
            cs = np.bincount(ft, u[fs], minlength=n); v = np.where(cs > 0, qc/np.where(cs > 0, cs, 1), 0)
            if it % 20 == 19 and abs(np.bincount(fs, u[fs]*v[ft], minlength=n) - pc).max() < 1e-14: break
        J = u[fs]*v[ft]; err = max(abs(np.bincount(fs, J, minlength=n)-pc).max(), abs(np.bincount(ft, J, minlength=n)-qc).max())
        ix = np.where(comp[fs] == X)[0]; w = J[ix]; return comp[ft[ix]], w/w.sum(), err
    def cond_current(self, Psi, X, off, phi, a):
        """CL-5 source: summed currents of each relay's odds conditioned on the other relay's actual site"""
        Jb = np.zeros(self.L//2); dens = np.zeros(self.L); s1, s2 = self.confs[X]
        for other in (s2, s1):
            chi = np.array([self.amp(Psi, yv, other) for yv in range(self.L)]); nr = np.vdot(chi, chi).real
            if nr < 1e-30: continue
            chi /= np.sqrt(nr); dens += abs(chi)**2
            for bi, (x, y) in enumerate(self.bonds(off)):
                Jb[bi] -= 2*np.sin(a[bi])*np.imag(np.exp(-1j*phi[bi])*np.conj(chi[x])*chi[y])
        return Jb, dens
    def packets(self, c1, c2, k0, w2=3.0):
        xs = np.arange(self.L); f1 = np.exp(-(xs-c1)**2/w2 + 1j*k0*xs); f2 = np.exp(-(xs-c2)**2/w2 - 1j*k0*xs)
        Psi = np.array([f1[c]*f2[d] - f1[d]*f2[c] for c, d in self.confs]); return Psi/np.linalg.norm(Psi)

def run_layer(R, Psi0, T, g2, h, eps, demon, rng):
    L = R.L; Psi = Psi0.copy(); X = rng.choice(R.NC, p=np.abs(Psi)**2)
    phi = [np.zeros(L//2), np.zeros(L//2)]; pold = [np.zeros(L//2), np.zeros(L//2)]
    base = [np.full(L//2, eps), np.full(L//2, -eps)]; a = [base[0].copy(), base[1].copy()]
    Vh = np.eye(L, dtype=complex); err = 0.0; hops = 0; records = []
    for t in range(2*T):
        off = t % 2; Jb, dens = R.cond_current(Psi, X, off, phi[off], a[off])
        if demon:      # adversarial feedback: each active bond phase chosen to maximise its rightward conditional current
            for bi in range(L//2):
                best = (-9, 0.0)
                for ph in np.linspace(-np.pi, np.pi, 9):
                    phi[off][bi] = ph; best = max(best, (R.cond_current(Psi, X, off, phi[off], a[off])[0][bi], ph))
                phi[off][bi] = best[1]
        else:
            new = 2*phi[off] - pold[off] + g2*Jb; pold[off] = phi[off].copy(); phi[off] = new
            a[off] = base[off]*(1 + h*np.array([dens[x] + dens[y] for x, y in R.bonds(off)]))
        V = R.half(off, phi[off], a[off]); M = R.wedge(V); Psi1 = M @ Psi
        tg, pr, e_ = R.plan_row(np.abs(Psi)**2, np.abs(Psi1)**2, M, X); err = max(err, e_)
        Xn = tg[rng.choice(len(pr), p=pr)]; hops += Xn != X; records.append(R.occ[Xn])     # CL-3 record, never fed back
        X = Xn; Psi = Psi1; Vh = V @ Vh
    return dict(Vh=Vh, Psi=Psi, err=err, hops=hops, nrec=len(records))

print('== 2. pathwise flow under the full record/response layer (2 fermion relays, ring L=40, 6 ticks)')
R40 = Ring(40); rng = np.random.default_rng(2026); P0 = R40.packets(12.0, 27.0, 0.4)
x40 = np.arange(40); out = {}
for tag, g2, h, dm in (('none', 0.0, 0.0, False), ('links g2=1', 1.0, 0.0, False), ('links g2=3 + lengths', 3.0, 0.6, False), ('demon', 0.0, 0.0, True)):
    out[tag] = run_layer(R40, P0, 6, g2, h, 1.2, dm, rng)
real = max(np.linalg.norm(R40.wedge(o['Vh']) @ P0 - o['Psi']) for o in out.values())
def gam(R, Psi):     # Born mean over the other relay's site of the conditional odds = one-body reduced state
    A_ = np.array([[R.amp(Psi, y, z) for z in range(R.L)] for y in range(R.L)]); return A_ @ A_.conj().T
gdev = max(abs(gam(R40, o['Psi']) - o['Vh'] @ gam(R40, P0) @ o['Vh'].conj().T).max() for o in out.values())
check('every realised history is a free block circuit, Psi(t) = Lambda^2(V_hist) Psi(0); the Born mean of the conditional odds is V_hist gamma(0) V_hist^dag',
      real < 1e-12 and gdev < 1e-12, f'max dev {real:.1e}, {gdev:.1e}')
fl = {k: flow(o['Vh'], 40, 13) for k, o in out.items()}
def bmean(o): Pv = np.abs(o['Psi'])**2; return float(sum(Pv[i]*(c[0]+c[1]) for i, c in enumerate(R40.confs)))
check('flow of every realised history = 0 (links, lengths, adversarial demon), although feedback moves the odds',
      max(abs(v) for v in fl.values()) < 1e-12 and abs(bmean(out['demon']) - bmean(out['none'])) > 0.05,
      f'flows {[f"{v:+.0e}" for v in fl.values()]}; Born sum-position free {bmean(out["none"]):.2f} demon {bmean(out["demon"]):.2f}')
check('CL-4 plans keep their marginals; relays hop; one record per mode per half-tick',
      max(o['err'] for o in out.values()) < 1e-12 and min(o['hops'] for o in out.values()) > 0 and all(o['nrec'] == 12 for o in out.values()),
      f"max marginal err {max(o['err'] for o in out.values()):.1e}; hops {[int(o['hops']) for o in out.values()]}")

# ============================================================== 3. exact branching: Born tracking and inversion covariance
def branch_law(R, Psi0, NH, g2, eps=1.2):
    L = R.L; p0 = np.abs(Psi0)**2; z = np.zeros(L//2)
    br = [(p0[X], Psi0, X, (z, z), (z, z), ()) for X in range(R.NC) if p0[X] > 1e-14]
    for t in range(NH):
        off = t % 2; a = np.full(L//2, eps if off == 0 else -eps); new = {}
        for w, Psi, X, phi, po, hist in br:
            Jb, _ = R.cond_current(Psi, X, off, phi[off], a)
            ph = [phi[0].copy(), phi[1].copy()]; pp_ = [po[0].copy(), po[1].copy()]
            ph[off] = 2*phi[off] - po[off] + g2*Jb; pp_[off] = phi[off].copy()
            M = R.wedge(R.half(off, ph[off], a)); Psi1 = M @ Psi
            tg, pr, _ = R.plan_row(np.abs(Psi)**2, np.abs(Psi1)**2, M, X); kh = hist + (tuple(np.round(ph[off], 11)),)
            for Xn, q in zip(tg, pr):
                if q*w < 1e-15: continue
                key = (Xn, kh)
                new[key] = (new[key][0] + w*q,) + new[key][1:] if key in new else (w*q, Psi1, Xn, tuple(ph), tuple(pp_), kh)
        br = list(new.values())
    P = np.zeros(R.NC); Bm = np.zeros(R.NC); groups = {}
    for w, Psi, X, phi, po, hist in br:
        P[X] += w; Bm += w*np.abs(Psi)**2; groups.setdefault(hist, []).append((w, X, Psi))
    ctv = 0.0
    for lst in groups.values():
        W = sum(x[0] for x in lst); Pg = np.zeros(R.NC)
        for w, X, _ in lst: Pg[X] += w/W
        ctv += W*0.5*abs(Pg - np.abs(lst[0][2])**2).sum()
    return P, Bm, ctv, len(groups)

print('== 3. CL-4 under CL-5 feedback: exact branching (ring L=8, 2 relays, 4 half-ticks)')
R8 = Ring(8); Q0 = R8.packets(2.0, 5.0, 0.4)
res = {g2: branch_law(R8, Q0, 4, g2) for g2 in (0.0, 0.3, 1.0)}
tv = {g2: 0.5*abs(r[0] - r[1]).sum() for g2, r in res.items()}
check('no feedback (g2=0): law of the configuration = Born mean of the odds, one history', tv[0.0] < 1e-12 and res[0.0][3] == 1, f'TV {tv[0.0]:.1e}')
check('CL-5 c-number feedback breaks CL-4 Born tracking: TV(law X, Born mean) > 0, growing with g2; given the link history the configuration is far from its odds',
      1e-3 < tv[0.3] < tv[1.0] and min(res[0.3][2], res[1.0][2]) > 0.5,
      f'TV {tv[0.3]:.2e} (g2=.3), {tv[1.0]:.2e} (g2=1); conditional TV {res[0.3][2]:.3f}, {res[1.0][2]:.3f}; histories {res[1.0][3]}')
Iinv = lambda x: (1 - x) % 8
QI = np.array([R8.amp(Q0, Iinv(a), Iinv(b)) for a, b in R8.confs]); PI = branch_law(R8, QI, 4, 1.0)[0]
mir = np.array([res[1.0][0][R8.cidx[tuple(sorted((Iinv(a), Iinv(b))))]] for a, b in R8.confs])
check('the whole layer (CL-4 transport, conditional source, link response) is inversion covariant: law from I.Psi0 = mirror of law from Psi0',
      abs(PI - mir).max() < 1e-9 and abs(res[1.0][0] - mir).max() > 1e-3, f'max diff {abs(PI - mir).max():.1e}; asymmetry of the law itself {abs(res[1.0][0] - mir).max():.2e}')

# ============================================================== 4. forbidden variant: records condition the odds
print('== 4. records that condition the odds (rate kappa per half-tick) + ratchet feedback (ring L=48)')
L4 = 48; Bf = [half_ring(L4, 0, blk(1.2)), half_ring(L4, 1, blk(-1.2))]
fmap = [np.array([(x + 1) % L4 if (x - off) % 2 == 0 else x for x in range(L4)]) for off in (0, 1)]
def chan(rho, off, kap):
    return (1-kap)*Bf[off] @ rho @ Bf[off].conj().T + kap*np.diag(np.bincount(fmap[off], np.diag(rho).real, minlength=L4)).astype(complex)
SW = np.array([[0, 1], [1, 0]], complex); rr = np.random.default_rng(1).normal(size=(L4, L4)) + 0j; rr = rr @ rr.T; kraus = 0
for x in range(L4):
    Rx = half_ring(L4, 0, SW) if x % 2 == 0 else np.eye(L4); Px = np.zeros((L4, L4)); Px[x, x] = 1; kraus = kraus + Rx @ Px @ rr @ Px @ Rx.T
kdev = abs(0.7*Bf[0] @ rr @ Bf[0].conj().T + 0.3*kraus - chan(rr, 0, 0.3)).max()
def sdisp(x, y): d = (x - y) % L4; return d - L4 if d > L4//2 else d
D4 = np.array([[sdisp(x, y) for y in range(L4)] for x in range(L4)])
def drift(off, kap, pdiag):
    T_ = (1-kap)*np.abs(Bf[off])**2 + kap*(np.arange(L4)[:, None] == fmap[off][None, :])
    return float((T_*D4*pdiag[None, :]).sum()), T_ @ pdiag
xs4 = np.arange(L4); fpk = np.exp(-(xs4-12.)**2/2)*(xs4 % 2 == 1) + np.exp(-(xs4-36.)**2/2)*(xs4 % 2 == 0); fpk /= np.linalg.norm(fpk)
row = []
for kap in (0.0, 0.01, 0.1, 1.0):
    vinf = drift(0, kap, np.full(L4, 1/L4))[0]; pd = np.full(L4, 1/L4); vs = []
    for t in range(40):
        v_, pd = drift(t % 2, kap, pd); vs.append(v_)
    rc = np.outer(fpk, fpk.conj()); rf = rc.copy()
    for t in range(6): rc = chan(rc, t % 2, kap); rf = Bf[t % 2] @ rf @ Bf[t % 2].conj().T
    coh = np.linalg.norm(rc[np.ix_(xs4 < 18, xs4 >= 30)])/np.linalg.norm(rf[np.ix_(xs4 < 18, xs4 >= 30)])
    unit = abs(chan(np.eye(L4, dtype=complex), 0, kap) - np.eye(L4)).max()
    row.append((kap, vinf, np.mean(vs[20:]), coh, unit))
check('channel = explicit measure-then-feedback Kraus sum (feedback blocks: swap or identity, index 0)', kdev < 1e-12, f'{kdev:.1e}')
check('infinite-temperature drift = kappa/2 sites per half-tick; stationary drift reaches 1 at kappa=1; non-unital by kappa',
      all(abs(v - k/2) < 1e-12 and abs(u - k) < 1e-12 for k, v, _, _, u in row) and abs(row[-1][2] - 1) < 1e-12,
      '; '.join(f'k={k}: v_inf {v:+.3f} v_stat {s:+.3f}' for k, v, s, _, _ in row) + f'; v_stat/kappa at 0.01 = {row[1][2]/0.01:.2f}')
check('long-range coherence = (1-kappa)^6 x the free circuit exactly: the coherent part is the index-0 free tick',
      all(abs(c - (1-k)**6) < 1e-12 for k, _, _, c, _ in row), '; '.join(f'{c:.6f}' for *_, c, _ in row))

# ============================================================== 5. averaged propagators of index-0 histories
print('== 5. Born-mean propagators K = sum p_j U_j of index-0 depth-4 circuits (2-band, 1D)')
rng5 = np.random.default_rng(3); NK = 541; ks5 = np.linspace(0, 2*np.pi, NK); e1k = np.exp(1j*ks5)
def haar2(r):
    z = (r.normal(size=(2, 2)) + 1j*r.normal(size=(2, 2)))/np.sqrt(2); q, t = np.linalg.qr(z); return q*(np.diag(t)/abs(np.diag(t)))
def circ(r, D=4):
    M = np.broadcast_to(np.eye(2, dtype=complex), (NK, 2, 2)).copy()
    for l in range(D):
        B = haar2(r)
        if l % 2 == 0: M = np.einsum('ij,kjl->kil', B, M)
        else:
            Bo = np.zeros((NK, 2, 2), complex); Bo[:, 0, 0] = B[1, 1]; Bo[:, 0, 1] = B[1, 0]/e1k; Bo[:, 1, 0] = B[0, 1]*e1k; Bo[:, 1, 1] = B[0, 0]
            M = Bo @ M
    return M
def wnd(f): return int(np.round(np.sum(np.angle(f[1:]/f[:-1]))/(2*np.pi)))
found = []; two_w = 0; base_w = 0
for trial in range(2500):
    J = 2 + trial % 4; Us = [circ(rng5) for _ in range(J)]; base_w = max(base_w, max(abs(wnd(np.linalg.det(u))) for u in Us))
    p = rng5.dirichlet(np.ones(J)); K = sum(pi*u for pi, u in zip(p, Us)); dK = np.linalg.det(K)
    if np.min(abs(dK)) < 1e-6: continue
    w = wnd(dK)
    if J == 2: two_w = max(two_w, abs(w))
    if w != 0: found.append((J, 1 - np.linalg.svd(K, compute_uv=False).min(), 1 - np.linalg.svd(K, compute_uv=False).max()))
dmin = min(f[1] for f in found); nb = 2*2*2
check('averaging index-0 histories CAN wind det K (point-gap winding); never with 2 terms (rederived)',
      base_w == 0 and len(found) > 0 and two_w == 0 and min(f[0] for f in found) >= 3, f'{len(found)} of 2500 mixtures wind')
check('every winding average is far from unitary: damping >= rigidity bound 1/(8 n^2), n = 2rd = 8',
      dmin >= 1/(8*nb**2), f'min over winding mixtures of 1 - s_min = {dmin:.3f} (bound {1/(8*nb**2):.4f}); best band 1 - s_max down to {min(f[2] for f in found):.3f}')

# ============================================================== 6. register bypass
print('== 6. register bypass: matter sites m_j, fresh register sites a_j; layer1 swap(m_j,a_j), layer2 swap(a_j,m_{j+1})')
L6 = 16; N6 = 2*L6; l1 = np.zeros((N6, N6)); l2 = np.zeros((N6, N6))
for j in range(L6):
    for (u_, v_), lay in (((j, L6+j), l1), ((L6+j, (j+1) % L6), l2)):
        lay[u_, v_] = lay[v_, u_] = 1
V6 = l2 @ l1; Pm = np.arange(N6) < L6
leak = abs(V6[np.ix_(~Pm, Pm)]).max(); fm = flow(V6[np.ix_(Pm, Pm)], L6, 4); fr = flow(V6[np.ix_(~Pm, ~Pm)], L6, 4)
check('finite-depth circuit on matter + blank registers: matter flow +1, register flow -1, total 0; registers return blank',
      leak == 0 and abs(fm - 1) < 1e-12 and abs(fr + 1) < 1e-12, f'matter {fm:+.0f}, registers {fr:+.0f}, leak {leak:.0f}')

# ============================================================== 7. 3D: CL-2 spin-3/2 Margolus tick
print('== 7. 3D: W3 and the magnetic flow index')
Cc = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1) - m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J32 = Jm(1.5); XI = []
for i in range(8):
    nv = (2*Cc[i]-1.0)/np.sqrt(3); w_, v_ = np.linalg.eigh(sum(nv[k]*J32[k] for k in range(3))); XI.append(v_[:, -1])
W8 = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(Cc[a]-Cc[b])) == 1: g = XI[a].conj() @ XI[b]; W8[a, b] = -g/abs(g)/np.sqrt(3)
def Wm(a): return np.cos(a)*W8 + 1j*np.sin(a)*np.eye(8)
def tick_k(k, mu=0.0, b=0.3, fe=None, fo=None):
    """2^3 cell, residue labelling; odd cube's residue-r site lies in cell n + (1 - r)"""
    Ue = Wm(mu/2 + b); Ph = np.diag(np.exp(1j*((1 - Cc) @ k))); Uo = Ph.conj() @ Wm(mu/2 - b) @ Ph
    if fe is not None: Ue = np.diag(np.exp(-1j*fe)) @ Ue @ np.diag(np.exp(1j*fe))
    if fo is not None: Uo = np.diag(np.exp(-1j*fo)) @ Uo @ np.diag(np.exp(1j*fo))
    return Uo @ Ue
mu7, b7 = 0.13, 0.21; A7, B7 = (np.cos(2*b7)+np.cos(mu7))/2, (np.cos(2*b7)-np.cos(mu7))/2
bd = max(abs(np.cos(np.angle(np.linalg.eigvals(tick_k(k, mu7, b7)))) - (A7*np.mean(np.cos(k)) - B7)).max()
         for k in np.random.default_rng(1).uniform(-np.pi, np.pi, (12, 3)))
check('CL-2 tick on the 2^3 cell reproduces the band law cos w = A S(k) - B', bd < 1e-12, f'{bd:.1e}')
def W3(Uf, n, h=1e-5):
    g = (np.arange(n)+0.5)*2*np.pi/n; tot = 0.0
    for k in itertools.product(g, g, g):
        k = np.array(k); Ui = np.linalg.inv(Uf(k)); A = []
        for i in range(3):
            e = np.zeros(3); e[i] = h; A.append(Ui @ (Uf(k+e) - Uf(k-e))/(2*h))
        tot += np.trace(A[0] @ (A[1] @ A[2] - A[2] @ A[1]))
    return float((tot*(2*np.pi/n)**3/(8*np.pi**2)).real)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
def qloc(k, m):
    n0 = m + np.cos(k).sum(); nv = np.sin(k); return (n0*np.eye(2) - 1j*(nv[0]*sx + nv[1]*sy + nv[2]*sz))/np.sqrt(n0**2 + (nv**2).sum())
wq = {m: W3(lambda k: qloc(k, m), 16) for m in (-2.0, 0.5, 4.5)}
check('control: quasi-local walk W3 = -1, +2, 0 at m = -2, 0.5, 4.5', abs(wq[-2.0]+1) < 1e-3 and abs(wq[0.5]-2) < 1e-2 and abs(wq[4.5]) < 1e-3,
      ', '.join(f'{v:+.4f}' for v in wq.values()))
r7 = np.random.default_rng(11); fe7, fo7 = r7.uniform(-np.pi, np.pi, 8), r7.uniform(-np.pi, np.pi, 8)
Fs = [(r7.uniform(-np.pi, np.pi, 8), r7.uniform(-np.pi, np.pi, 8), r7.uniform(0, 1), r7.uniform(0, 1.5)) for _ in range(3)]
def hist3(k):
    U = np.eye(8, dtype=complex)
    for fe_, fo_, m_, b_ in Fs: U = tick_k(k, m_, b_, fe_, fo_) @ U
    return U
w3t = [W3(lambda k: tick_k(k, 0.1, 0.3, fe7, fo7), 10), W3(hist3, 10)]
check('CL-2 tick W3 = 0 with random frames, and for a 3-tick history with different frames, masses and steps',
      max(abs(v) for v in w3t) < 1e-9, f'{w3t[0]:+.1e}, {w3t[1]:+.1e}')
def mag_T(L, Nphi):
    phi = 2*np.pi*Nphi/L**2; idx = lambda x, y: (x % L)*L + (y % L); Tx = np.zeros((L*L, L*L), complex); Ty = Tx.copy()
    for x in range(L):
        for y in range(L):
            Ty[idx(x, y+1), idx(x, y)] = np.exp(1j*phi*x); Tx[idx(x+1, y), idx(x, y)] = np.exp(-1j*phi*L*y) if x == L-1 else 1.0
    return Tx, Ty, phi
def qloc_field(L, Nphi, m, kz):
    Tx, Ty, _ = mag_T(L, Nphi); I = np.eye(L*L)
    N0 = m*I + (Tx+Tx.conj().T)/2 + (Ty+Ty.conj().T)/2 + np.cos(kz)*I
    M = np.kron(N0, np.eye(2)) - 1j*(np.kron((Tx-Tx.conj().T)/2j, sx) + np.kron((Ty-Ty.conj().T)/2j, sy) + np.kron(np.sin(kz)*I, sz))
    w_, V_ = np.linalg.eigh(M.conj().T @ M); return M @ (V_/np.sqrt(w_)) @ V_.conj().T
def winding(Uf, nk=181):
    d = np.array([np.linalg.det(Uf(k)) for k in np.linspace(0, 2*np.pi, nk)]); d = d/abs(d); return np.sum(np.angle(d[1:]/d[:-1]))/(2*np.pi)
def crossings(Uf, nk=401):
    kk = np.linspace(0, 2*np.pi, nk) + 1e-3; up = dn = 0; w_, V_ = np.linalg.eig(Uf(kk[0])); ph = np.angle(w_)
    for k in kk[1:]:
        w2, V2 = np.linalg.eig(Uf(k)); ph2 = np.angle(w2); mt = np.argmax(abs(V_.conj().T @ V2), axis=1)
        for a in range(len(ph)):
            p0, p1 = ph[a], ph2[mt[a]]
            if abs(p0) < 0.6 and abs(p1) < 0.6 and np.sign(p0) != np.sign(p1): up += p1 > p0; dn += p1 < p0
        V_, ph = V2, ph2
    return int(up), int(dn)
def cl2_field(L, kz, fo, mu=0.0, b=0.3):
    sites = list(itertools.product(range(L), range(L), range(2))); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    def layer(off, Wb):
        M = np.zeros((N, N), complex)
        for a, b_ in itertools.product(range(0, L, 2), range(0, L, 2)):
            X = np.array([a, b_, 0]) + off + Cc; ids = [ix[(v[0] % L, v[1] % L, v[2] % 2)] for v in X]
            rs = [int((v % 2) @ [4, 2, 1]) for v in X]; ph = np.exp(1j*kz*(X[:, 2] // 2))
            M[np.ix_(ids, ids)] += Wb[np.ix_(rs, rs)]*np.outer(ph.conj(), ph)
        return M
    Do = np.diag(np.exp(1j*fo)); return Do.conj() @ layer(1, Wm(mu/2 - b)) @ Do @ layer(0, Wm(mu/2 + b))
Tx4, Ty4, ph4 = mag_T(4, 1); G4 = np.linalg.inv(Ty4) @ np.linalg.inv(Tx4) @ Ty4 @ Tx4
cases = [(-2.0, 1), (-2.0, 2), (0.5, 1), (4.5, 1)]; wf = [winding(lambda k: qloc_field(4, nf, m, k)) for m, nf in cases]
cr = crossings(lambda k: qloc_field(4, 1, -2.0, k))
check('control: flux N_phi on a 4x4 torus; winding of det U(kz) = W3 x N_phi; signed crossings of w=0 agree',
      np.allclose(G4, G4[0, 0]*np.eye(16)) and np.allclose(wf, [-1, -2, 2, 0], atol=1e-6) and cr[0] - cr[1] == -1,
      f'windings {[round(float(v), 6) for v in wf]}; m=-2, N_phi=1 crossings (up,down) {cr}')
fo4 = np.random.default_rng(5).uniform(-np.pi, np.pi, 32); Uf4 = lambda k: cl2_field(4, k, fo4)
w4 = winding(Uf4); c4 = crossings(Uf4)
check('CL-2 tick in a random frame field: winding 0, crossings of w=0 present and balanced (both chiralities)',
      abs(w4) < 1e-9 and c4[0] == c4[1] > 0, f'winding {w4:+.1e}; (up,down) {c4}')

# ============================================================== 8. against measurement (estimates)
print('== 8. against measurement (estimates; inputs listed)')
lP = 1.616e-35; a_lat = 5*lP; Lkam = 1.8e5; Vmin = 0.9          # a: register's untested 'few Planck lengths'; KamLAND-type baseline
Nh = 2*Lkam/a_lat; kap_max = -np.log(Vmin)/Nh
check('neutrino coherence over 180 km (visibility >= 0.9, a = 5 l_P): kappa per half-tick is tiny; at most 1 - V of neutrinos are ever conditioned',
      kap_max < 1e-30, f'half-ticks {Nh:.1e}; kappa < {kap_max:.1e}; the coherent fraction evolves by the index-0 tick (section 4)')
Nnu, sNnu = 2.9840, 0.0082                                       # LEP invisible Z width
check('index 0 in every charge sector puts a light mirror partner beside each nu_L: N_nu = 6 against LEP 2.9840 +- 0.0082',
      (6 - Nnu)/sNnu > 100, f'{(6 - Nnu)/sNnu:.0f} sigma')
print(f'runtime {time.monotonic()-T0:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
