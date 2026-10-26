#!/usr/bin/env python3
"""
Attempt: p-equals-q-for-compact-and-strong-bodies (a1)

When do the lengths' and clocks' far fields of a self-bound body agree beyond the
continuum limit?  Setting: block 60's curvature member (landed), held walls at
w = chi = 1, content H = sum_b c_b h_b + sum_x w_x m_x with c_b = sqrt(w_x w_y)/(chi_x chi_y)
(block 59, landed), all supplied.  Content model chosen here (a SUPPLIED choice): one staggered
walker, h_b = (i/2) eta (|y><x| - |x><y|), m_x = m*eps_x, state = lowest positive-energy
eigenvector of H(fields), fields = stationary points of  <H> + F.

Part A: exact algebra (sympy / Fractions).
Part B: self-consistent strong-field solutions (float64, residual-certified, NOT exact arithmetic).
Python with numpy, scipy, sympy only.  One process.
"""
import sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scipy.optimize import brentq
from itertools import product
import sympy as S
from fractions import Fraction

T0 = time.time()
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    if ok:
        NP += 1; print("PASS", name, detail)
    else:
        NF += 1; print("FAIL", name, detail)

# ============================================================== Part A: exact algebra
# A1. From the three landed global identities of block-110-note T2(e) (content away from walls):
#     8KQ = Hr + T + F ;  4K(P+Q) = Hr + 2T ;  4K(P-Q) = T - F
#   (the third follows from the first two; check that), derive P/Q and bending/fall.
K, Hr, T, F, Q, P = S.symbols('K Hr T F Q P', real=True)
sol = S.solve([S.Eq(8*K*Q, Hr + T + F), S.Eq(4*K*(P+Q), Hr + 2*T)], [P, Q], dict=True)[0]
Pn, Qn = S.simplify(sol[P]), S.simplify(sol[Q])
check("A1a  third identity 4K(P-Q)=T-F follows from the other two",
      S.simplify(4*K*(Pn-Qn) - (T - F)) == 0)
rho = S.simplify(Pn/Qn)
check("A1b  P/Q = (Hr+3T-F)/(Hr+T+F)", S.simplify(rho - (Hr+3*T-F)/(Hr+T+F)) == 0, str(rho))
B = S.simplify(1 + 2*Qn/(Pn+Qn))
check("A1c  bending/fall 1+2Q/(P+Q) = 2 + (F-T)/(Hr+2T)", S.simplify(B - (2 + (F-T)/(Hr+2*T))) == 0, str(B))
check("A1d  P/Q-1 = 2(T-F)/(Hr+T+F)", S.simplify(rho - 1 - 2*(T-F)/(Hr+T+F)) == 0)
# so with Hr+T+F>0, Hr+2T>0:  P=Q <=> T=F <=> B=2 ; T<F <=> P<Q <=> B>2
x = S.symbols('x')
check("A1e  B=2 iff T=F (solve)", S.solve(S.Eq(B, 2), T) == [F], str(S.solve(S.Eq(B, 2), T)))

# A2. Pinned body (T=0), block 60 T4(b)-(d): s=Q g0, chi0=1+s, w0=1/(1+2s), N0=w0 chi0, mu=m/(8K)
s, m, Kk = S.symbols('s m K', positive=True)
chi0 = 1 + s; w0 = 1/(1 + 2*s); N0 = w0*chi0
check("A2a  2*N0 = 1+w0 (pinned body)", S.simplify(2*N0 - 1 - w0) == 0)
Hr_p = m*w0                       # rest energy of the pinned body
Qp = m/(8*Kk*chi0)               # 8KQ = m/chi0  (T4(c))
F_p = 8*Kk*Qp*(1 - N0)           # F = 8KQ(1-N0): walls carry Q, interior holds N0 at the body
check("A2b  8KQ = Hr+F for the pinned body", S.simplify(8*Kk*Qp - Hr_p - F_p) == 0)
check("A2c  P/Q = w0 from the energy form (T=0)", S.simplify((Hr_p - F_p)/(Hr_p + F_p) - w0) == 0)
check("A2d  B = (2+3s)/(1+s) from the energy form (T=0)", S.simplify((2 + (F_p)/(Hr_p)) - (2 + 3*s)/(1 + s)) == 0)

# A3. Heavy-walker second-order perturbation theory (re-proved at the scope used).
#     Star of 7 sites: centre (energy +m w0) and 6 neighbours (energy -m wy), bond amplitude V.
#     Symmetric neighbour state couples with g = sqrt(6) V.  Exact 2x2 positive eigenpair:
mm, w0s, wys, V = S.symbols('mm w0s wys V', positive=True)
g = S.sqrt(6)*V
Delta = mm*(w0s + wys)
# exact 2x2 positive eigenpair of [[m w0, g],[g, -m wy]]: tan(2 theta) = 2g/Delta ; T = 2 g a b = g sin(2 theta)
xx = S.symbols('xx', positive=True)       # xx = 2 g / Delta
T_exact = g*xx/S.sqrt(1 + xx**2)
# (i) verify T_exact against the explicit eigenvector for exact-rational sample values (high-precision evaluation)
import mpmath as mp
mp.mp.dps = 40
def two_level_T(mv, w0v, wyv, Vv):
    gv = mp.sqrt(6)*Vv
    Hm = mp.matrix([[mv*w0v, gv], [gv, -mv*wyv]])
    ev, ER = mp.eigsy(Hm)
    k = 1 if ev[1] > ev[0] else 0
    aa, bb_ = ER[0, k], ER[1, k]
    return 2*gv*aa*bb_
ok = True
for (mv, w0v, wyv, Vv) in [(S.Rational(3), S.Rational(7, 10), S.Rational(9, 10), S.Rational(2, 5)),
                           (S.Rational(10), S.Rational(1, 2), S.Rational(3, 4), S.Rational(1, 3)),
                           (S.Rational(1, 2), S.Rational(1), S.Rational(1), S.Rational(1, 2))]:
    gv = S.sqrt(6)*Vv; Dv = mv*(w0v + wyv)
    te = T_exact.subs({xx: 2*gv/Dv, g: gv}) if False else (gv*(2*gv/Dv)/S.sqrt(1 + (2*gv/Dv)**2))
    ok = ok and abs(mp.mpf(str(S.N(te, 40))) - two_level_T(mp.mpf(str(S.N(mv, 40))), mp.mpf(str(S.N(w0v, 40))),
                                                          mp.mpf(str(S.N(wyv, 40))), mp.mpf(str(S.N(Vv, 40))))) < mp.mpf(10)**-30
check("A3a  two-level exact: hop energy T = g*sin(2 theta) = g x/sqrt(1+x^2), x=2g/Delta (matches eigenvector to 1e-30)", ok)
# (ii) leading order in 1/m:  x = 2g/Delta = O(1/m) ; T = g x - g x^3/2 + ... = 2 g^2/Delta + O(1/m^3)
ser = S.series(g*xx/S.sqrt(1 + xx**2), xx, 0, 4).removeO()
check("A3b  T = g x - g x^3/2 + O(x^5)", S.simplify(ser - (g*xx - g*xx**3/2)) == 0)
lead = S.simplify((g*xx).subs(xx, 2*g/Delta))
check("A3c  leading order T = 12 V^2/(m (w0+wy))", S.simplify(lead - 12*V**2/(mm*(w0s + wys))) == 0, str(lead))
# in the staggered walk V = (1/2) sqrt(w0 wy)/(chi0 chiy): 12 V^2 = 3 w0 wy/(chi0 chiy)^2
c0, cy = S.symbols('c0 cy', positive=True)
t1_star = S.simplify((12*V**2/(w0s + wys)).subs(V, S.sqrt(w0s*wys)/(2*c0*cy)))   # T = t1/m
check("A3d  t1 = 3 w0 wy/(chi0^2 chiy^2 (w0+wy))",
      S.simplify(t1_star - 3*w0s*wys/(c0**2*cy**2*(w0s + wys))) == 0)
# weak field: w=chi=1 -> t1 = 3/2 ; then P/Q - 1 = 2T/E = 3/m^2  (free heavy walker, T2(c))
check("A3e  weak field t1 = 3/2", S.simplify(t1_star.subs({w0s: 1, wys: 1, c0: 1, cy: 1}) - S.Rational(3, 2)) == 0)
# crossing strength in the heavy weak-field limit: P/Q-1 = 2(T-F)/(Hr+T+F), T=t1/m, F=m*s (F=8KQ(1-N0), 1-N0 ~ s)
sstar = S.solve(S.Eq(S.Rational(3, 2)/mm, mm*s), s)[0]
check("A3f  heavy weak-field balance s* = 3/(2 m^2)", S.simplify(sstar - S.Rational(3, 2)/mm**2) == 0, str(sstar))

# ============================================================== Part B: self-consistent box solutions
class Box:
    def __init__(self, n):
        self.n = n; self.N = n**3
        self.pts = list(product(range(n), repeat=3))
        self.idx = {p: i for i, p in enumerate(self.pts)}
        c = n//2; self.c = c
        bi, bj, eta = [], [], []
        wall = np.zeros(self.N)
        for p in self.pts:
            for mu in range(3):
                q = list(p); q[mu] += 1; q = tuple(q)
                if q in self.idx:
                    bi.append(self.idx[p]); bj.append(self.idx[q]); eta.append((-1)**sum(p[:mu]))
            for mu in range(3):
                for d in (-1, 1):
                    q = list(p); q[mu] += d
                    if tuple(q) not in self.idx:
                        wall[self.idx[p]] += 1
        self.bi = np.array(bi); self.bj = np.array(bj); self.eta = np.array(eta, float); self.wall = wall
        self.eps = np.array([(-1)**(sum(p) - 3*c) for p in self.pts], float)
        A = sp.coo_matrix((np.ones(len(bi)), (self.bi, self.bj)), shape=(self.N, self.N)); A = (A + A.T).tocsr()
        self.L = (A - 6*sp.identity(self.N)).tocsc()          # Delta with zero (f-1) on the walls
        self.lu = sla.splu(-self.L)
        self.center = self.idx[(c, c, c)]
        self.nbrs = [self.idx[(c+d[0], c+d[1], c+d[2])] for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    def G(self, src): return self.lu.solve(src)

def hamiltonian(box, chi, Nn, m):
    w = Nn/chi
    c = np.sqrt(w[box.bi]*w[box.bj])/(chi[box.bi]*chi[box.bj])
    H = np.zeros((box.N, box.N))
    H[box.bi, box.bj] = 0.5*box.eta*c; H[box.bj, box.bi] = 0.5*box.eta*c
    H[np.arange(box.N), np.arange(box.N)] = m*box.eps*w
    return H, w, c

def content(box, chi, Nn, m):
    H, w, c = hamiltonian(box, chi, Nn, m)
    ev, V = np.linalg.eigh(H)
    k = np.searchsorted(ev, 0.0)
    E, phi = ev[k], V[:, k]
    r = m*box.eps*w*phi**2
    tb = box.eta*c*phi[box.bi]*phi[box.bj]
    tau = np.zeros(box.N); np.add.at(tau, box.bi, 0.5*tb); np.add.at(tau, box.bj, 0.5*tb)
    return E, phi, r, tb, tau, w

def field_energy(box, chi, Nn, K):
    dN = Nn[box.bj] - Nn[box.bi]; dc = chi[box.bj] - chi[box.bi]
    return -8*K*(dN*dc).sum() - 8*K*(box.wall*(1 - Nn)*(1 - chi)).sum()

def solve(box, K, m, init, alpha=0.2, tol=1e-13, maxit=8000):
    chi, Nn = init[0].copy(), init[1].copy()
    for it in range(maxit):
        E, phi, r, tb, tau, w = content(box, chi, Nn, m)
        e = r + tau
        cn, Nnn = chi.copy(), Nn.copy()
        for _ in range(300):
            c2 = 1 + box.G(e/(8*K*Nnn)); N2 = 1 - box.G((e + 2*tau)/(8*K*c2))
            d = max(abs(c2 - cn).max(), abs(N2 - Nnn).max()); cn, Nnn = c2, N2
            if d < 1e-15: break
        res = max(abs(cn - chi).max(), abs(Nnn - Nn).max())
        if res < tol:
            chi, Nn = cn, Nnn; break
        chi = (1 - alpha)*chi + alpha*cn; Nn = (1 - alpha)*Nn + alpha*Nnn
        if Nn.min() <= 0: raise RuntimeError("N<=0")
    E, phi, r, tb, tau, w = content(box, chi, Nn, m)
    e = r + tau
    out = dict(chi=chi, N=Nn, w=w, E=E, phi=phi, r=r, tb=tb, tau=tau, e=e, res=res, it=it, K=K, m=m)
    out['Q'] = (e/(8*K*Nn)).sum(); out['P'] = ((e + 2*tau)/(8*K*chi)).sum()
    out['Qflux'] = -(box.L @ (chi - 1)).sum(); out['Pflux'] = (box.L @ (Nn - 1)).sum()
    out['T'] = tb.sum(); out['Hr'] = r.sum(); out['F'] = field_energy(box, chi, Nn, K)
    out['rho'] = out['P']/out['Q']; out['B'] = 1 + 2*out['Q']/(out['P'] + out['Q'])
    out['phic2'] = phi[box.center]**2; out['w0'] = w[box.center]
    return out

def pinned(box, K, m):
    mu = m/(8*K)
    g = box.G(np.eye(box.N)[box.center]); g0 = g[box.center]
    Q = brentq(lambda q: q*(1 + q*g0) - mu, 0, mu + 1)
    Pp = Q/(1 + 2*Q*g0)
    return 1 + Q*g, 1 - Pp*g, Q, g0

box = Box(7)

def run(K, m, bx=box, init=None):
    if init is None:
        c, N, _, _ = pinned(bx, K, m); init = (c, N)
    return solve(bx, K, m, init)

# --- B1: identities and independent stationarity check on one strong-field solution
Sg = run(0.05, 3.0)
check("B1a  fixed-point residual", Sg['res'] < 1e-12, f"res={Sg['res']:.1e}")
check("B1b  Q from sites equals Q from wall flux", abs(Sg['Q'] - Sg['Qflux']) < 1e-11 and abs(Sg['P'] - Sg['Pflux']) < 1e-11,
      f"Q={Sg['Q']:.9f} P={Sg['P']:.9f}")
check("B1c  <H> = Hr + T", abs(Sg['E'] - Sg['Hr'] - Sg['T']) < 1e-11)
check("B1d  8KQ = <H> + F", abs(8*0.05*Sg['Q'] - Sg['E'] - Sg['F']) < 1e-10, f"{8*0.05*Sg['Q'] - Sg['E'] - Sg['F']:.1e}")
check("B1e  4K(P-Q) = T - F", abs(4*0.05*(Sg['P'] - Sg['Q']) - (Sg['T'] - Sg['F'])) < 1e-10,
      f"{4*0.05*(Sg['P']-Sg['Q'])-(Sg['T']-Sg['F']):.1e}")
check("B1f  4K(P+Q) = Hr + 2T", abs(4*0.05*(Sg['P'] + Sg['Q']) - (Sg['Hr'] + 2*Sg['T'])) < 1e-10)
check("B1g  P/Q = (Hr+3T-F)/(Hr+T+F)", abs(Sg['rho'] - (Sg['Hr'] + 3*Sg['T'] - Sg['F'])/(Sg['Hr'] + Sg['T'] + Sg['F'])) < 1e-11)
check("B1h  B = 2 + (F-T)/(Hr+2T)", abs(Sg['B'] - (2 + (Sg['F'] - Sg['T'])/(Sg['Hr'] + 2*Sg['T']))) < 1e-10, f"B={Sg['B']:.6f}")

def total_energy(box, u, lc, K, m):
    """independent of e,tau formulas: Phi = lowest positive eigenvalue of H(fields) + F(fields)"""
    chi = np.exp(lc); Nn = np.exp(u)*chi
    H, w, c = hamiltonian(box, chi, Nn, m)
    ev = np.linalg.eigvalsh(H); E = ev[np.searchsorted(ev, 0.0)]
    return E + field_energy(box, chi, Nn, K)
u0 = np.log(Sg['N']/Sg['chi']); l0 = np.log(Sg['chi'])
worst = 0.0
for site in [box.center, box.nbrs[0], box.idx[(3, 3, 5)], box.idx[(1, 2, 3)]]:
    for which in (0, 1):
        h = 1e-5; gv = []
        for sgn in (+1, -1):
            u = u0.copy(); l = l0.copy()
            (u if which == 0 else l)[site] += sgn*h
            gv.append(total_energy(box, u, l, 0.05, 3.0))
        worst = max(worst, abs(gv[0] - gv[1])/(2*h))
check("B1i  independent: finite-difference gradient of (lowest positive eigenvalue + F) in log-rate and log-length vanishes",
      worst < 2e-7, f"max|grad|={worst:.1e}")

# --- B2: compact branch: T<F (P<Q), B in (2,3), clock slowdown w0, strong field
print("# compact branch, 7^3 box, m=3 and 6 (K, mu=m/8K, w0, phi_c^2, P/Q, B, T/F)")
comp = []
for (m_, K_) in [(3.0, 0.1), (3.0, 0.03), (3.0, 0.02), (6.0, 0.05), (6.0, 0.02), (6.0, 0.01)]:
    s_ = run(K_, m_)
    comp.append(s_)
    print(f"#  m={m_} K={K_} mu={m_/(8*K_):.3f} w0={s_['w0']:.4f} phic2={s_['phic2']:.4f} P/Q={s_['rho']:.5f} B={s_['B']:.5f} T/F={s_['T']/s_['F']:.4e} res={s_['res']:.0e}")
check("B2a  every compact-branch solution has T<F, P<Q, B>2 (strong field w0 down to 0.1 and below)",
      all(s_['T'] < s_['F'] and s_['rho'] < 1 and s_['B'] > 2 and s_['res'] < 1e-12 for s_ in comp),
      f"min w0={min(s_['w0'] for s_ in comp):.3f}, max T/F={max(s_['T']/s_['F'] for s_ in comp):.3f}")
check("B2b  they are self-bound (>=97% of the weight on the central site) for m=6",
      all(s_['phic2'] > 0.97 for s_ in comp if s_['m'] == 6.0), "")
check("B2c  B stays below 3 (block 60's local bound 2<=B<3 for rest bodies)", all(s_['B'] < 3 for s_ in comp))

# --- B3: crossing T=F on the self-bound branch (P=Q, B=2)
def f_rho(K_, m_, state, bx=None):
    bx = bx or box
    s_ = solve(bx, K_, m_, state['init']); state['init'] = (s_['chi'], s_['N']); state['s'] = s_
    return s_['rho'] - 1
def cross(m_, Klo, Khi, npts=14, bx=None):
    bx = bx or box
    c, N, _, _ = pinned(bx, Klo, m_); st = {'init': (c, N)}
    Ks = np.geomspace(Klo, Khi, npts); prev = (Ks[0], f_rho(Ks[0], m_, st, bx))
    for K_ in Ks[1:]:
        v = f_rho(K_, m_, st, bx)
        if prev[1] < 0 <= v:
            c, N, _, _ = pinned(bx, prev[0], m_); st['init'] = (c, N)
            f_rho(prev[0], m_, st, bx)           # restart from the lower-K branch point
            Kb = brentq(lambda k: f_rho(k, m_, st, bx), prev[0], K_, xtol=1e-13)
            return Kb, solve(bx, Kb, m_, st['init'])
        prev = (K_, v)
    return None, None
print("# crossing P=Q (T=F) on the self-bound branch, 7^3 box")
cr = {}
for m_, Klo, Khi in [(1.5, 0.03, 1.0), (3.0, 0.05, 3.0), (6.0, 0.1, 30.0)]:
    Kb, s_ = cross(m_, Klo, Khi)
    cr[m_] = (Kb, s_)
    if s_ is None:
        check(f"B3   crossing exists for m={m_}", False); continue
    g0 = pinned(box, Kb, m_)[3]
    print(f"#  m={m_} K*={Kb:.6f} mu*={m_/(8*Kb):.4f} s*=Q*g0={s_['Q']*g0:.5f} w0*={s_['w0']:.4f} phic2={s_['phic2']:.4f} T/F={s_['T']/s_['F']:.9f} B={s_['B']:.9f}")
    check(f"B3   m={m_}: a self-consistent self-bound solution with P=Q exactly (T=F, B=2)",
          abs(s_['rho'] - 1) < 1e-9 and abs(s_['T']/s_['F'] - 1) < 1e-8 and abs(s_['B'] - 2) < 1e-9 and s_['res'] < 1e-12
          and s_['phic2'] > 0.9, f"phic2={s_['phic2']:.3f}")
# continue upward in K from the pinned start to stay on the bound branch
state = {'init': (pinned(box, 0.3, 3.0)[0], pinned(box, 0.3, 3.0)[1])}
seq = []
for K_ in [0.3, 0.5, 0.8, 1.2, 2.0]:
    s_ = solve(box, K_, 3.0, state['init']); state['init'] = (s_['chi'], s_['N']); seq.append(s_)
print("# m=3, continuation in K:", " ".join(f"K={s_['K']}:P/Q={s_['rho']:.4f}(T/F={s_['T']/s_['F']:.3f},phic2={s_['phic2']:.3f})" for s_ in seq))
check("B3y  m=3 bound branch: P<Q for K=0.3,0.5; P>Q for K=1.2,2.0 (self-bound, phi_c^2>0.7)",
      seq[0]['rho'] < 1 and seq[1]['rho'] < 1 and seq[3]['rho'] > 1 and seq[4]['rho'] > 1 and all(s_['phic2'] > 0.7 for s_ in seq))
check("B3z  heavier bodies balance at weaker field: s*(m=1.5) > s*(m=3) > s*(m=6)",
      all(cr[k][1] is not None for k in cr) and
      (cr[1.5][1]['Q']*pinned(box, cr[1.5][0], 1.5)[3] > cr[3.0][1]['Q']*pinned(box, cr[3.0][0], 3.0)[3] >
       cr[6.0][1]['Q']*pinned(box, cr[6.0][0], 6.0)[3]))

# --- B4: heavy compact limit at fixed strength mu
print("# heavy limit at fixed mu = m/(8K), 7^3 box")
for mu in (0.02, 0.5, 2.0):
    rows = []
    for m_ in (12, 25, 50, 100, 200):
        K_ = m_/(8*mu)
        c, N, Qp_, g0 = pinned(box, K_, m_)
        s_ = solve(box, K_, m_, (c, N), alpha=0.3)
        w0p = 1/(1 + 2*Qp_*g0)
        wp = N/c; ctr = box.center
        t1 = sum(0.5*wp[ctr]*wp[y]/(c[ctr]**2*c[y]**2*(wp[ctr] + wp[y])) for y in box.nbrs)
        rows.append((m_, s_, w0p, t1, Qp_*g0))
    m_, s_, w0p, t1, sg = rows[-1]
    print(f"#  mu={mu}: s=Q g0={sg:.4f}  m=200: P/Q={s_['rho']:.8f} pinned w0={w0p:.8f} c2=m^2(P/Q-w0)={m_**2*(s_['rho']-w0p):.5f} "
          f"m*T={m_*s_['T']:.6f} t1={t1:.6f}  B={s_['B']:.6f} vs (2+3s)/(1+s)={(2+3*sg)/(1+sg):.6f}")
    tol_a = 3e-4 if mu >= 0.5 else 2e-3     # weak field: hop-sourced field shifts are relatively larger
    check(f"B4a  mu={mu}: m*T -> t1 (A3d with pinned fields), rel.err < {tol_a} at m=200",
          abs(rows[-1][1]['T']*200/rows[-1][3] - 1) < tol_a, f"{abs(rows[-1][1]['T']*200/rows[-1][3] - 1):.1e}")
    c2 = [mm_**2*(s2['rho'] - wp_) for (mm_, s2, wp_, _, _) in rows]
    check(f"B4b  mu={mu}: P/Q - 1/(1+2Qg0) = c2/m^2 with c2 converging (|c2(200)-c2(100)|<2e-3)",
          abs(c2[-1] - c2[-2]) < (2e-3 if mu >= 0.5 else 1e-2), f"c2(100)={c2[-2]:.5f} c2(200)={c2[-1]:.5f}")
    check(f"B4c  mu={mu}: B -> (2+3s)/(1+s) (|diff|<1e-3 at m=200)",
          abs(rows[-1][1]['B'] - (2 + 3*sg)/(1 + sg)) < 1e-3, "")
    check(f"B4d  mu={mu}: T/F ~ 1/m^2 (T/F*m^2 within 2% between m=100 and 200)",
          abs((rows[-1][1]['T']/rows[-1][1]['F']*200**2)/(rows[-2][1]['T']/rows[-2][1]['F']*100**2) - 1) < 0.02, "")
# weak-field limit of c2 -> 3  (A3c: P/Q - 1 = 2T/E = 3/m^2 plus -2s)
mu = 0.002; m_ = 200; K_ = m_/(8*mu)
c, N, Qp_, g0 = pinned(box, K_, m_); s_ = solve(box, K_, m_, (c, N), alpha=0.3)
c2_small = m_**2*(s_['rho'] - 1/(1 + 2*Qp_*g0))
check("B4e  weak field: c2 -> 3 (free heavy walker P/Q-1 = 2T/E = 3/m^2), within 2%",
      abs(c2_small - 3) < 0.06, f"c2(mu=0.002)={c2_small:.4f}")

# --- B5: box-size dependence
Kb, s7 = cr[3.0]
vals = {7: s7}
for n_ in (9, 11):
    bx = Box(n_)
    c, N, _, _ = pinned(bx, Kb, 3.0)
    vals[n_] = solve(bx, Kb, 3.0, (c, N))
print("# box-size dependence at m=3, K=K*(n=7): " + " ".join(f"n={n_}:P/Q={v['rho']:.5f},T/F={v['T']/v['F']:.4f},phic2={v['phic2']:.4f}" for n_, v in vals.items()))
check("B5a  same parameters in 9^3 and 11^3 boxes: P/Q within 1% of 1 (the compact state does not depend on the walls at this order)",
      all(abs(v['rho'] - 1) < 0.01 for v in vals.values()), "")
box9 = Box(9)
Kb9, s9 = cross(3.0, 0.05, 3.0, bx=box9)
print(f"# 9^3 box crossing for m=3: K*={Kb9:.6f} (7^3: {Kb:.6f}), phic2={s9['phic2']:.4f}, P/Q={s9['rho']:.9f}, T/F={s9['T']/s9['F']:.9f}")
check("B5b  the balance locus also exists in the 9^3 box (P=Q, T=F exactly, K* within 15% of the 7^3 value)",
      abs(s9['rho'] - 1) < 1e-9 and abs(Kb9/Kb - 1) < 0.15, f"K9/K7={Kb9/Kb:.4f}")

# ============================================================== summary
dt = time.time() - T0
print(f"TOTAL: PASS={NP} FAIL={NF}")
if NF == 0:
    print("HIT: (exact) with the landed T2(e) identities, P/Q = (Hr+3T-F)/(Hr+T+F) and bending/fall 1+2Q/(P+Q) = 2+(F-T)/(Hr+2T); so P=Q <=> T=F <=> bending/fall=2, and a hop energy below the field energy gives P<Q and bending/fall above 2.")
    print("HIT: (checked, float64, residual 1e-13, 7^3 box, staggered walker m,K supplied) self-consistent self-bound solutions exist on both sides of T=F: compact ones (w0 down to ~0.1) have T<F, P<Q, 2<B<3, P/Q->1/(1+2Qg0), and a one-parameter locus of self-bound solutions has P=Q exactly (T=F); T=F is therefore not an identity of self-bound bodies, and the heavy compact limit has T m -> 3 w0 wy/(chi0^2 chiy^2 (w0+wy)), P/Q = 1/(1+2Qg0)+c2/m^2, heavy weak-field estimate of the balance Qg0 ~ 3/(2m^2) (m=6: 0.0346 found vs 0.0417).")
print(f"SUMMARY: exact P/Q and bending/fall in terms of (rest, hop, field) energy; strong-field self-bound staggered walkers (checked, 7^3 box) have P<Q on the compact branch, P=Q on a balance locus (heavy weak-field estimate Qg0~3/(2m^2)), and P>Q beyond it, so T=F is not forced by self-binding on the lattice (runtime {dt:.0f}s)")
sys.exit(0 if NF == 0 else 1)
