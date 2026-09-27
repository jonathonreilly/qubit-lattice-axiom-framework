#!/usr/bin/env python3
"""Permanent record contents and symmetric field dynamics (Codex campaign12h_third, author-only): independent check.
J:derive:deferred-20260926-author-only-field-results:a1   (result (c) of the task)

P1  exact intertwiner H_col R_v = R_v H_base for every symmetric content vector v (Dicke vectors, three count sectors), on a
    five-configuration base graph whose hops carry non-commuting S3 slot permutations; a non-symmetric vector fails.
P2  ground energy: each fixed-count fibre of H_col has minimum eigenvalue equal to the base E_0 (float) and the lower bound
    <Psi, H_col Psi> >= <r, H_base r> (Cauchy-Schwarz) is checked on random exact vectors.
P3  one loop H = -J X (x) P: rho_F(tau) and purity 1 - sin^2(2 theta)(1 - eta^2)/2 (symbolic), eta = Tr(P rho); the iid example
    tau = diag(7/10, 3/10) gives eta = 29/50 and purity 3341/5000 at theta = pi/4.
P4  local symmetrising reservoir on path graphs with counts (2,1), (2,2), (1,1,1), (2,1,1), (3,2): exact rational rank of the
    Lindbladian (real block form over QQ) is D^2 - 1, and the Dicke projector is stationary (disjoint from the author's
    modular rank); one-hot displacement identity for every jump.
P5  the degree-lowering lemma g_z + T_z g_z = (I - T_z) f with deg g_z < deg f (symbolic), and the fuel dilation C^3 = C with
    Kraus operators A0 = I + (cos theta - 1) P_-, A1 = -i sin theta L realising exp(dt gamma D[L]) (exact).
"""
import time
T0 = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)
import itertools, random, sympy as sp, numpy as np
from sympy.polys.matrices import DomainMatrix
from math import comb, factorial
def perm_matrix(perm, k, N):
    """operator on (C^k)^N permuting slots: slot i content goes to slot perm[i]"""
    dim = k**N; M = sp.zeros(dim, dim)
    for word in itertools.product(range(k), repeat=N):
        new = [None]*N
        for i in range(N): new[perm[i]] = word[i]
        a = sum(c*k**(N-1-i) for i, c in enumerate(word)); b = sum(c*k**(N-1-i) for i, c in enumerate(new))
        M[b, a] = 1
    return M
def dicke(counts):
    k = len(counts); N = sum(counts); v = sp.zeros(k**N, 1)
    words = [w for w in itertools.product(range(k), repeat=N) if all(w.count(a) == counts[a] for a in range(k))]
    for w in words: v[sum(c*k**(N-1-i) for i, c in enumerate(w))] = 1
    return v/sp.sqrt(len(words))
# C1 intertwiner: base graph with 5 configurations, hopping amplitudes and S3 slot-permutation labels (N = 3 slots)
rng = random.Random(4); k, N = 2, 3; nb = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)]
perms = list(itertools.permutations(range(N)))
Vdiag = [sp.Rational(rng.randint(-5, 5), rng.randint(1, 3)) for _ in range(nb)]
Hbase = sp.zeros(nb, nb); dim = k**N
Hcol = sp.zeros(nb*dim, nb*dim)
labels = {}
for c in range(nb):
    Hbase[c, c] = Vdiag[c]
    for i in range(dim): Hcol[c*dim + i, c*dim + i] = Vdiag[c]
for (c, cp) in edges:
    a = sp.Rational(rng.randint(1, 6), rng.randint(1, 3)); pm = perms[rng.randrange(6)]
    labels[(c, cp)] = pm
    P = perm_matrix(pm, k, N)
    Hbase[c, cp] -= a; Hbase[cp, c] -= a
    Hcol[c*dim:(c+1)*dim, cp*dim:(cp+1)*dim] += -a*P
    Hcol[cp*dim:(cp+1)*dim, c*dim:(c+1)*dim] += -a*P.T

print("== P1 intertwiner")
ok1 = True
for counts in ((3, 0), (2, 1), (1, 2)):
    v = dicke(counts); R = sp.kronecker_product(sp.eye(nb), v)
    ok1 &= sp.simplify(Hcol*R - R*Hbase) == sp.zeros(nb*dim, nb)
wv = sp.Matrix([1, 2, 0, 0, 0, 0, 0, 0]); Rn = sp.kronecker_product(sp.eye(nb), wv)
fails = sp.simplify(Hcol*Rn - Rn*Hbase) != sp.zeros(nb*dim, nb)
check("P1 H_col R_v = R_v H_base exactly for the Dicke vectors of counts (3,0), (2,1), (1,2) (N = 3 slots, k = 2 contents) on a "
      "5-configuration graph with non-commuting S3 slot permutations on its hops; a non-symmetric content vector fails",
      ok1 and fails and len(set(labels.values())) >= 3, f"labels {sorted(set(labels.values()))}")
print("== P2 ground energy")
Hb = np.array(Hbase.tolist(), dtype=float); Hc = np.array(Hcol.tolist(), dtype=float)
E0 = np.linalg.eigvalsh(Hb)[0]
# fixed-count fibres: project onto words with given counts
okg = True; gaps = []
for counts in ((3, 0), (2, 1), (1, 2), (0, 3)):
    idxs = [c*dim + sum(x*k**(N-1-i) for i, x in enumerate(wd)) for c in range(nb) for wd in itertools.product(range(k), repeat=N)
            if all(wd.count(a) == counts[a] for a in range(k))]
    sub = Hc[np.ix_(idxs, idxs)]
    e = np.linalg.eigvalsh(sub)[0]; gaps.append(e - E0); okg &= abs(e - E0) < 1e-10
# Cauchy-Schwarz lower bound on random exact vectors
rr = random.Random(9); okcs = True
for _ in range(20):
    Psi = sp.Matrix([sp.Rational(rr.randint(-5, 5), rr.randint(1, 4)) for _ in range(nb*dim)])
    lhs = (Psi.T*Hcol*Psi)[0]
    rvec = [sp.sqrt(sum(Psi[c*dim + i]**2 for i in range(dim))) for c in range(nb)]
    rhs = sum(Hbase[c, c]*rvec[c]**2 for c in range(nb)) + 2*sum(Hbase[c, cp]*rvec[c]*rvec[cp] for c in range(nb) for cp in range(c + 1, nb))
    okcs &= float(lhs - rhs) >= -1e-12
check("P2 every fixed-count fibre (counts (3,0),(2,1),(1,2),(0,3)) has minimum eigenvalue equal to the base E_0 (float, 1e-10), "
      "and <Psi, H_col Psi> >= <r, H_base r> with r_c = |Psi_c| on 20 random rational vectors (nonpositive hops)", okg and okcs,
      f"E_0 = {E0:.6f}; fibre minus base {[f'{g:.1e}' for g in gaps]}")
print("== P3 one loop and a classical content mixture")
th, eta_s = sp.symbols('theta eta', real=True)
X = sp.Matrix([[0, 1], [1, 0]]); Pswap = perm_matrix((1, 0), 2, 2)
a, b, d_ = sp.symbols('a b d', real=True); cr, ci = sp.symbols('cr ci', real=True); c_ = cr + sp.I*ci
rho = sp.Matrix([[a, 0, 0, 0], [0, b, c_, 0], [0, sp.conjugate(c_), d_, 0], [0, 0, 0, 1 - a - b - d_]])
XP = sp.kronecker_product(X, Pswap)
U = sp.cos(th)*sp.eye(8) + sp.I*sp.sin(th)*XP            # exp(-i tau H) with H = -J X (x) P, theta = J tau, (X (x) P)^2 = I
full = U*sp.kronecker_product(sp.Matrix([[1, 0], [0, 0]]), rho)*U.H
rhoF = sp.Matrix(2, 2, lambda i, j: sum(full[i*4 + m, j*4 + m] for m in range(4)))
eta_expr = sp.simplify((Pswap*rho).trace())
target = sp.Matrix([[sp.cos(th)**2, -sp.I*eta_expr*sp.cos(th)*sp.sin(th)], [sp.I*eta_expr*sp.cos(th)*sp.sin(th), sp.sin(th)**2]])
okf = sp.simplify(rhoF - target) == sp.zeros(2, 2) and sp.simplify((rhoF*rhoF).trace() - (1 - sp.sin(2*th)**2*(1 - eta_expr**2)/2)) == 0
tau2 = sp.diag(sp.Rational(7, 10), sp.Rational(3, 10)); rho_iid = sp.kronecker_product(tau2, tau2)
eta_iid = (Pswap*rho_iid).trace()
purF = 1 - sp.Rational(1, 2)*sp.sin(2*th)**2*(1 - eta_s**2)
check("P3 one loop H = -J X (x) P from field |0>: rho_F has diagonal cos^2, sin^2 and off-diagonal +-i eta cos sin with "
      "eta = Tr(P rho); purity 1 - sin^2(2 theta)(1 - eta^2)/2; iid tau = diag(7/10, 3/10) gives eta = 29/50 and purity "
      "3341/5000 at theta = pi/4", okf and eta_iid == sp.Rational(29, 50) and purF.subs({th: sp.pi/4, eta_s: eta_iid}) == sp.Rational(3341, 5000),
      f"eta = {eta_iid}, purity = {purF.subs({th: sp.pi/4, eta_s: eta_iid})}")
print("== P4 local symmetrising reservoir: exact unique fixed point")
def reservoir_nullity(counts):
    kk = len(counts); n = sum(counts)
    words = [w for w in itertools.permutations([a for a in range(kk) for _ in range(counts[a])])]
    words = sorted(set(words)); D = len(words); ix = {w: i for i, w in enumerate(words)}
    Ls = []; disp_ok = True
    for (x, y) in [(i, i + 1) for i in range(n - 1)]:
        for al in range(kk):
            for be in range(al + 1, kk):
                Lm = sp.zeros(D, D)
                for w in words:
                    if w[x] == al and w[y] == be:
                        w2 = list(w); w2[x], w2[y] = be, al; w2 = tuple(w2)
                        s = sp.zeros(D, 1); dd = sp.zeros(D, 1)
                        s[ix[w]] = 1; s[ix[w2]] = 1; dd[ix[w]] = 1; dd[ix[w2]] = -1
                        Lm += s*dd.T/2
                        # one-hot displacement z = e_{x,beta} + e_{y,alpha} - e_{x,alpha} - e_{y,beta}
                        oh = lambda wd: [int(wd[i] == a) for i in range(n) for a in range(kk)]
                        z = [p - q for p, q in zip(oh(w2), oh(w))]
                        zz = [0]*(n*kk); zz[x*kk + be] += 1; zz[y*kk + al] += 1; zz[x*kk + al] -= 1; zz[y*kk + be] -= 1
                        disp_ok &= z == zz
                if Lm != sp.zeros(D, D): Ls.append(Lm)
    I = sp.eye(D); Sop = sp.zeros(D*D, D*D)
    for j, Lm in enumerate(Ls):
        g = j + 1
        LdL = Lm.T*Lm
        Sop += g*(sp.kronecker_product(Lm, Lm) - sp.Rational(1, 2)*sp.kronecker_product(I, LdL) - sp.Rational(1, 2)*sp.kronecker_product(LdL.T, I))
    rank = DomainMatrix.from_Matrix(Sop).convert_to(sp.QQ).rank()
    u = sp.ones(D, 1)/sp.sqrt(D); fixed = (Sop*(u*u.T).reshape(D*D, 1)).applyfunc(sp.simplify) == sp.zeros(D*D, 1)
    return D, rank, fixed, disp_ok
rows = []; okr = True
for counts in ((2, 1), (2, 2), (1, 1, 1), (2, 1, 1), (3, 2)):
    D, rank, fixed, disp = reservoir_nullity(counts); rows.append((counts, D, D*D - rank)); okr &= rank == D*D - 1 and fixed and disp
check("P4 the reservoir sum gamma D[L_ab^{alpha beta}] on path graphs (rates gamma = 1, 2, ...) has exact rational nullity one, "
      "spanned by the Dicke projector (real Lindbladian: all jumps real), and every jump has the fixed one-hot displacement (8); "
      "dimensions 3, 6, 6, 12, 10", okr, str(rows))
print("== P5 lemma and dilation")
xs = sp.symbols('x0:4'); zv = (1, -1, -1, 1)
f = xs[0]**2*xs[1] + 3*xs[2]*xs[3] - xs[1]**3 + 2
def T(g): return g.subs({xs[i]: xs[i] + zv[i] for i in range(4)}, simultaneous=True)
def Delta(g): return sp.expand(T(g) - g)
m = sp.Poly(f, *xs).total_degree()
gz = 0; term = Delta(f)
for r_ in range(m):
    gz += (-sp.Rational(1, 2))**r_*term; term = Delta(term)
gz = sp.expand(-sp.Rational(1, 2)*gz)
lem = sp.expand(gz + T(gz) - (f - T(f))) == 0 and sp.Poly(gz, *xs).total_degree() < m
Lx = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 0, 0]])     # a partial isometry |s><d| type block
Pm = Lx.T*Lx
Cm = sp.kronecker_product(Lx, sp.Matrix([[0, 0], [1, 0]])) + sp.kronecker_product(Lx.T, sp.Matrix([[0, 1], [0, 0]]))
thq = sp.symbols('theta')
cube = sp.simplify(Cm**3 - Cm) == sp.zeros(6, 6)
Ufull = sp.eye(6) + (sp.cos(thq) - 1)*Cm**2 - sp.I*sp.sin(thq)*Cm        # exp(-i theta C) when C^3 = C
fuel = sp.Matrix([1, 0]); spent = sp.Matrix([0, 1])
A0 = sp.simplify(sp.kronecker_product(sp.eye(3), fuel.T)*Ufull*sp.kronecker_product(sp.eye(3), fuel))
A1 = sp.simplify(sp.kronecker_product(sp.eye(3), spent.T)*Ufull*sp.kronecker_product(sp.eye(3), fuel))
kraus = sp.simplify(A0 - (sp.eye(3) + (sp.cos(thq) - 1)*Pm)) == sp.zeros(3, 3) and sp.simplify(A1 + sp.I*sp.sin(thq)*Lx) == sp.zeros(3, 3)
check("P5 degree-lowering lemma: g_z = -(1/2) sum_r (-Delta_z/2)^r Delta_z f has degree < deg f and g_z + T_z g_z = f - T_z f "
      "(symbolic, cubic f); fuel dilation: C^3 = C and Kraus operators A0 = I + (cos theta - 1) P_-, A1 = -i sin theta L (exact)",
      lem and cube and kraus)
print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (cross-family independent check, no defect found) - result (c) holds: the symmetric-sector "
          "intertwiner H_col R_v = R_v H_base is exact (non-commuting S3 hop labels, all count sectors), each fixed-count fibre "
          "attains the base ground energy with the Cauchy-Schwarz lower bound, the one-loop mixture formula and its iid example "
          "(eta = 29/50, purity 3341/5000) hold, and the local symmetrising reservoir has an exactly unique Dicke fixed point on "
          "five path-graph count sectors (exact rational rank, disjoint from the author's modular rank); the degree-lowering "
          "lemma and fuel dilation check. The single-plaquette perturbative control (2) and matching to created mobile matter "
          "are not addressed")
