#!/usr/bin/env python3
"""Mobile-record geometric formation and waves: can the actual empty-start formation law prepare a nontrivial smooth
inhomogeneous colour profile with o(K) conditional entropy (the hypothesis of #8610's nonlinear Euler theorem)?
J:derive:mobile-record-geometric-formation-waves:a1   (sources: Codex drafts #8589 #8594 #8600 #8604 #8610, frozen heads)

O  obstruction (proof in ATTEMPT): the actual law is invariant under the even translations of the torus (homogeneous birth
   colour law p, translation-covariant rates, empty start), so for any profile p(x), at every time,
   H(mu | rho x prod_u p(u/N)) >= sum_u KL(q || p(u/N)) >= (1/2) sum_u |p(u/N) - pbar_N|^2 (q the common one-site marginal),
   = +infinity at every deterministic time (vacancies have positive probability), and no TV-approximation below 1/2 helps.
   Finite ingredients checked here exactly (sympy): binary Pinsker, the chain rule, the Gibbs variational identity, the
   Hoeffding second derivative, KL <= chi^2, and the explicit bound h0/K >= 1/1568 for a cosine profile at every even N.
F  #8604 Part I input: padded fibre counts, R_hat formula and R_hat <= U_j (exact integers) on four bipartite graphs.
C  #8604 (6)-(7): Var_hat(F) >= w Var_B(g) and D_hat(F) <= w m_hat (h+2) D_B(g) (exact rationals, random integer g).
S  numerical screens (floats, not load-bearing): the imported Broder gap bound (4), the comparison (8), the physical-slide
   comparison gap(S_j) >= gap(B_j)/C_j, slide-layer connectivity, and the killed-chain bound (9).
"""
import itertools, random, math, sys, time
from fractions import Fraction as Fr
from collections import defaultdict
import numpy as np
import sympy as sp
T0 = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

print("== O obstruction: exact ingredients")
s, r = sp.symbols('s r', positive=True)
g = s*sp.log(s/r) + (1 - s)*sp.log((1 - s)/(1 - r)) - 2*(s - r)**2
check("O1 binary Pinsker: g(r) = KL((s,1-s)||(r,1-r)) - 2(s-r)^2 has g(s) = 0 and g'(r) = (r-s)(1-2r)^2/(r(1-r)), so g >= 0; "
      "with the log-sum reduction to A = {q > p} this is KL(q||p) >= (1/2)|q-p|_1^2",
      sp.simplify(g.subs(r, s)) == 0 and sp.simplify(sp.diff(g, r) - (r - s)*(1 - 2*r)**2/(r*(1 - r))) == 0)
m11, m12, m21, p1, p2 = sp.symbols('m11 m12 m21 p1 p2', positive=True)
m22 = 1 - m11 - m12 - m21
mu = {(0, 0): m11, (0, 1): m12, (1, 0): m21, (1, 1): m22}
pa = [p1, 1 - p1]; pb = [p2, 1 - p2]
mu1 = [m11 + m12, m21 + m22]; mu2 = [m11 + m21, m12 + m22]
H = lambda P, Qf: sum(P[x]*sp.log(P[x]/Qf(x)) for x in P)
lhs = H(mu, lambda x: pa[x[0]]*pb[x[1]])
rhs = H(mu, lambda x: mu1[x[0]]*mu2[x[1]]) + sum(mu1[i]*sp.log(mu1[i]/pa[i]) for i in (0, 1)) + sum(mu2[i]*sp.log(mu2[i]/pb[i]) for i in (0, 1))
check("O2 chain rule H(mu | p_1 x p_2) = H(mu | mu_1 x mu_2) + H(mu_1|p_1) + H(mu_2|p_2) (symbolic, two sites x two colours)",
      sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0)
x1, x2, x3, a1, a2, a3, f1, f2, f3 = sp.symbols('x1 x2 x3 a1 a2 a3 f1 f2 f3', positive=True)
nu = [x1, x2, x3]; n0 = [a1, a2, a3]; fv = [f1, f2, f3]
Zf = sum(n0[i]*sp.exp(fv[i]) for i in range(3))
Hn = lambda P, Qv: sum(P[i]*sp.log(P[i]/Qv[i]) for i in range(3))
ident = Hn(nu, [n0[i]*sp.exp(fv[i])/Zf for i in range(3)]) - (Hn(nu, n0) - sum(nu[i]*fv[i] for i in range(3)) + sp.log(Zf))
check("O3 Gibbs identity H(nu | nu0 e^f/Z) = H(nu|nu0) - E_nu f + log E_nu0 e^f (sum nu = sum nu0 = 1), giving the entropy "
      "inequality E_nu f <= H(nu|nu0) + log E_nu0 e^f", sp.simplify(sp.expand_log(ident, force=True).subs({x3: 1 - x1 - x2, a3: 1 - a1 - a2})) == 0)
t, pp = sp.symbols('t pp', positive=True)
psi = sp.log(1 - pp + pp*sp.exp(t)) - t*pp
qq = pp*sp.exp(t)/(1 - pp + pp*sp.exp(t))
check("O4 Hoeffding: psi(t) = log(1-p+pe^t) - tp has psi(0) = psi'(0) = 0 and psi'' = q(1-q) <= 1/4",
      sp.simplify(psi.subs(t, 0)) == 0 and sp.simplify(sp.diff(psi, t).subs(t, 0)) == 0 and sp.simplify(sp.diff(psi, t, 2) - qq*(1 - qq)) == 0)
qv = sp.symbols('q1:4', positive=True); pv = sp.symbols('r1:4', positive=True)
chi_id = sum(qv[i]*(qv[i]/pv[i] - 1) for i in range(3)) - sum((qv[i] - pv[i])**2/pv[i] for i in range(3))
check("O5 KL <= chi^2: sum q (q/p - 1) = sum (q-p)^2/p when sum q = sum p = 1 (with log z <= z - 1)",
      sp.simplify(chi_id.subs({qv[2]: 1 - qv[0] - qv[1], pv[2]: 1 - pv[0] - pv[1]})) == 0)
# explicit profile: 14 colours, pbar uniform, p(x) = pbar + eps v cos(2 pi x_1), v = e_(A,+1) - e_(A,-1), eps = 1/28
eps = sp.Rational(1, 28); okP = True; vals = []
for N in (4, 8, 12, 16, 20):
    cs = [sp.nsimplify(sp.cos(2*sp.pi*u/N)) for u in range(N)]
    mean_c = sp.simplify(sum(cs)/N); mean_c2 = sp.simplify(sum(c**2 for c in cs)/N)
    lb = sp.Rational(1, 2)*2*eps**2*mean_c2            # (1/2) K^-1 sum_u |p(u/N) - pbar_N|^2, |v|^2 = 2, black sites: N^2/2 per x_1
    okP &= mean_c == 0 and mean_c2 == sp.Rational(1, 2); vals.append(lb)
    okP &= all(sp.Rational(1, 14) - eps*abs(c) > 0 for c in cs)
check("O6 cosine profile (eps = 1/28): strictly positive, pbar_N = pbar exactly and every translation-invariant law has "
      "h0/K >= (1/2)eps^2|v|^2 <cos^2> = 1/1568 at N = 4..20 (exact; the same at every even N >= 4)", okP and all(v == sp.Rational(1, 1568) for v in vals), str(vals[0]))

print("== F, C, S: #8604 Part I inputs on small bipartite graphs")
def matchings(Lv, Rv, E, size):
    """all matchings with exactly `size` edges; E list of (l, r)."""
    adj = defaultdict(list)
    for l, r in E: adj[l].append(r)
    Ls = sorted(Lv, key=str); out = []
    def rec(i, used, cur):
        if len(cur) == size: out.append(frozenset(cur)); return
        if len(cur) + (len(Ls) - i) < size: return
        l = Ls[i]
        rec(i + 1, used, cur)                       # l unmatched
        for r in adj[l]:
            if r not in used:
                used.add(r); cur.append((l, r)); rec(i + 1, used, cur); cur.pop(); used.discard(r)
    rec(0, set(), []); return out
def graph_bip(name):
    if name == 'C6':
        L = ['l0', 'l1', 'l2']; R = ['r0', 'r1', 'r2']
        E = [('l0','r0'),('l1','r0'),('l1','r1'),('l2','r1'),('l2','r2'),('l0','r2')]
    elif name.startswith('grid'):
        a, b = map(int, name[4:].split('x'))
        V = [(i, j) for i in range(a) for j in range(b)]
        L = [v for v in V if (v[0] + v[1]) % 2 == 0]; R = [v for v in V if (v[0] + v[1]) % 2 == 1]
        E = [(u, v) for u in L for v in R if abs(u[0]-v[0]) + abs(u[1]-v[1]) == 1]
    elif name == 'Q3':
        V = list(itertools.product((0, 1), repeat=3))
        L = [v for v in V if sum(v) % 2 == 0]; R = [v for v in V if sum(v) % 2 == 1]
        E = [(u, v) for u in L for v in R if sum(abs(x - y) for x, y in zip(u, v)) == 1]
    return L, R, E
def check_graph(name, rng):
    L, R, E = graph_bip(name); K = len(L); m = len(E)
    a = [len(matchings(L, R, E, r)) for r in range(K + 1)]
    Rr = Fr(a[K-1], a[K])
    res = []
    for j in range(1, K):
        k = j + 1; h = K - k
        Ld = [('dl', i) for i in range(h)]; Rd = [('dr', i) for i in range(h)]
        Eh = E + [(dl, r) for dl in Ld for r in R] + [(l, dr) for l in L for dr in Rd]
        mh = len(Eh); Lh = L + Ld; Rh = R + Rd
        perf = matchings(Lh, Rh, Eh, K + h); near = matchings(Lh, Rh, Eh, K + h - 1)
        orig = set(L) | set(R)
        proj = lambda M: frozenset(e for e in M if e[0] in orig and e[1] in orig)
        f0 = math.factorial(h)**2
        fib = defaultdict(lambda: defaultdict(int))
        for M in perf: fib['perfect'][proj(M)] += 1
        for M in near:
            covL = {e[0] for e in M}; covR = {e[1] for e in M}
            hl = [v for v in Lh if v not in covL][0]; hr = [v for v in Rh if v not in covR][0]
            cls = 'oo' if (hl in orig and hr in orig) else ('dd' if (hl not in orig and hr not in orig) else 'od')
            fib[cls][proj(M)] += 1
        expect = {'perfect': (k, f0), 'oo': (j, (h+1)**2*f0), 'od': (k, 2*h*f0), 'dd': (k+1, f0)}
        ok = True
        for cls, (rank, cnt) in expect.items():
            if h == 0 and cls in ('dd', 'od'): ok &= len(fib[cls]) == 0; continue
            ok &= all(len(U) == rank and c == cnt for U, c in fib[cls].items()) and len(fib[cls]) == a[rank]
        Rhat = Fr(len(near), len(perf))
        Rhat_formula = (h+1)**2*Fr(a[j], a[k]) + 2*h + (Fr(a[k+1], a[k]) if k + 1 <= K else 0)
        Uj = (h+1)*Rr + 2*h + Fr(m, k+1)
        ok &= Rhat == Rhat_formula and Rhat <= Uj
        # comparison steps (6)-(7) for random integer g on B_j = Omega_j u Omega_k
        Om = [M for M in matchings(L, R, E, j)] + [M for M in matchings(L, R, E, k)]
        idx = {M: i for i, M in enumerate(Om)}
        Bedges = set()
        for M in Om:
            for e in M:
                if len(M) == k: Bedges.add(frozenset((M, M - {e})))
            for e in E:
                if e in M: continue
                if all(e[0] != f[0] and e[1] != f[1] for f in M) and len(M) == j: Bedges.add(frozenset((M, M | {e})))
                for f in M:
                    Mf = M - {f}
                    if all(e[0] != g[0] and e[1] != g[1] for g in Mf): Bedges.add(frozenset((M, Mf | {e})))
        Bedges = [tuple(x) for x in Bedges if len(x) == 2]
        # Broder_hat transitions
        states = perf + near; sidx = {M: i for i, M in enumerate(states)}
        Hedges = set()
        adjh = defaultdict(list)
        for l, r in Eh: adjh[l].append(r); adjh[r].append(l)
        for M in perf:
            for e in M: Hedges.add(frozenset((M, M - {e})))
        for M in near:
            covL = {e[0] for e in M}; covR = {e[1] for e in M}
            u = [v for v in Lh if v not in covL][0]; v = [x for x in Rh if x not in covR][0]
            mate = {}
            for (x, y) in M: mate[x] = y; mate[y] = x
            for w in adjh[u]:
                if w == v: Hedges.add(frozenset((M, M | {(u, v)})))
                else: z = mate[w]; Hedges.add(frozenset((M, (M - {(z, w)}) | {(u, w)})))
            for w in adjh[v]:
                if w == u: continue
                z = mate[w]; Hedges.add(frozenset((M, (M - {(w, z)}) | {(w, v)})))
        Hedges = [tuple(x) for x in Hedges]
        assert all(x in sidx and y in sidx for x, y in Hedges)
        ZB = len(Om); Zh = len(states); fmin = (2*h+1)*f0; w = Fr(fmin*ZB, Zh)
        ok67 = True
        for trial in range(3):
            g = [rng.randint(-5, 5) for _ in Om]
            def F(M):
                U = proj(M)
                if len(U) in (j, k): return Fr(g[idx[U]])
                return Fr(sum(g[idx[U - {e}]] for e in U), k + 1)
            Fv = [F(M) for M in states]
            varh = sum(x*x for x in Fv)/Zh - (sum(Fv)/Zh)**2
            varB = Fr(sum(x*x for x in g), ZB) - Fr(sum(g), ZB)**2
            Dh = Fr(sum((Fv[sidx[x]] - Fv[sidx[y]])**2 for x, y in Hedges), Zh)
            DB = Fr(sum((g[idx[x]] - g[idx[y]])**2 for x, y in Bedges), ZB)
            ok67 &= varh >= w*varB and Dh <= w*mh*(h+2)*DB
        # gaps (float screens)
        def gap(n, edges, ix):
            Lm = np.zeros((n, n))
            for x, y in edges:
                i, jj = ix[x], ix[y]; Lm[i, jj] -= 1; Lm[jj, i] -= 1; Lm[i, i] += 1; Lm[jj, jj] += 1
            ev = np.linalg.eigvalsh(Lm); return ev[1]
        gH = gap(Zh, Hedges, sidx); gB = gap(ZB, Bedges, idx)
        # physical slides on Omega_j
        Oj = matchings(L, R, E, j); oix = {M: i for i, M in enumerate(Oj)}
        adjG = defaultdict(list)
        for l, r in E: adjG[l].append(r); adjG[r].append(l)
        Sedges = set()
        for M in Oj:
            cov = {x for e in M for x in e}
            for (x, y) in M:
                for b, c in ((x, y), (y, x)):
                    for av in adjG[b]:
                        if av not in cov:
                            e2 = (b, av) if b in L else (av, b)
                            Sedges.add(frozenset((M, (M - {(x, y)}) | {e2})))
        Sedges = [tuple(s) for s in Sedges]
        gS = gap(len(Oj), Sedges, oix) if len(Oj) > 1 else float('inf')
        Cj = 1 + (2*K - 2)*(m + m*m)*(k - 1)*(k + 1 + 2*m)
        okK = True                                  # killed-chain bound (9): lambda_min(L_S + beta H) >= 1/[2/(beta p) + (1 + 2m/p)/g]
        if len(Oj) > 1:
            Ls = np.zeros((len(Oj), len(Oj)))
            for x, y in Sedges:
                i_, j_ = oix[x], oix[y]; Ls[i_, j_] -= 1; Ls[j_, i_] -= 1; Ls[i_, i_] += 1; Ls[j_, j_] += 1
            hv = np.array([sum(1 for (l_, r_) in E if all(l_ != e[0] and r_ != e[1] for e in M)) for M in Oj], dtype=float)
            pbar = hv.mean()
            if pbar > 0:
                for beta in (0.01, 1.0, 100.0):
                    lam = np.linalg.eigvalsh(Ls + beta*np.diag(hv))[0]
                    okK &= lam >= 1/(2/(beta*pbar) + (1 + 2*m/pbar)/gS) - 1e-12
        b4 = 1/(256*mh*float(Rhat)**4)
        res.append(dict(name=name, j=j, fibers=ok, comp67=ok67, g4=bool(gH >= b4), g8=bool(gB >= gH/(mh*(h+2)) - 1e-12), gslide=bool(gS >= gB/Cj), killed=bool(okK), gH=gH, b4=b4, gB=gB, gS=gS, conn=bool(gS > 1e-9)))
    return res

rng = random.Random(1)
rows = []
for nm in ['C6', 'grid2x3', 'grid2x4', 'Q3']:
    rows += check_graph(nm, rng)
check(f"F1 padded fibre counts (h!)^2, (h+1)^2(h!)^2, 2h(h!)^2, (h!)^2 by class, every original matching of the right rank, "
      f"and R_hat = (h+1)^2 a_j/a_k + 2h + a_(k+1)/a_k <= U_j, exact on {len(rows)} (graph, stage) cases",
      all(x['fibers'] for x in rows), ", ".join(f"{x['name']}:j{x['j']}" for x in rows))
check("C1 comparison steps (6)-(7): Var_hat(F) >= w Var_B(g) and D_hat(F) <= w m_hat (h+2) D_B(g), exact rationals, 3 random "
      "integer g per case", all(x['comp67'] for x in rows))
check("S1 (screen) Broder gap on the padded graph >= 1/(256 m_hat R_hat^4) (the imported bound (4), kappa = 1)", all(x['g4'] for x in rows),
      "; ".join(f"{x['name']}j{x['j']}: {x['gH']:.3f} vs {x['b4']:.1e}" for x in rows[:3]))
check("S2 (screen) gap(B_j) >= gap(Broder_hat)/(m_hat(h+2)) (8)", all(x['g8'] for x in rows))
check("S3 (screen) every slide layer S_j connected and gap(S_j) >= gap(B_j)/C_j (the physical-slide comparison)",
      all(x['gslide'] and x['conn'] for x in rows))
check("S4 (screen) killed-chain bound (9): lambda_min(L_S + beta H) >= 1/[2/(beta p) + (1+2m/p)/g] at beta = 0.01, 1, 100",
      all(x['killed'] for x in rows))

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (a no-go for the actual law) - the actual empty-start formation law cannot prepare any nonconstant colour profile: it is invariant "
          "under the even torus translations (homogeneous birth colours p, translation-covariant rates, empty start), so at "
          "every time H(mu | rho x prod p(u/N)) >= sum_u KL(q||p(u/N)) >= (1/2) sum_u |p(u/N) - pbar|^2 = Theta(K) (exact "
          "cosine example: h0/K >= 1/1568), it is +infinity at every deterministic time (vacancies), and no law within total "
          "variation 1/2 of an o(K)-entropy inhomogeneous preparation is translation invariant; so the empty-start -> #8604 "
          "-> #8610 chain delivers only the constant solution. A position-dependent birth-colour variant with exchanges "
          "started at completion has h0 <= (Lip^2/eps) E sum_u |b_u - u|^2/N^2 (proof; open: the displacement bound). "
          "#8604 Part I inputs: padded fibres, R_hat, and comparison steps (6)-(7) exact on 10 cases; gap screens pass")
    print("HIT: the actual empty-start paired-record formation law cannot prepare a nontrivial inhomogeneous colour profile "
          "with o(K) conditional entropy: exact translation-invariance lower bound h0 >= (1/2) sum_u |p(u/N) - pbar|^2")
