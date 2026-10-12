"""C4 / RW / W3 part C2 (fast rebuild of part C's symbol with fields depending on (t, x) only, k along x;
identical Lagrangian).  Questions:
 (S4) masses = 0, breaking terms only: healthy at all k?
 (S5) how small can the spatial-diffeo-breaking two-derivative terms be while the completion stays healthy
      at all k?  Random search with |c_j| ~ 10^U(-p-1, -p), p = 0..4, masses ~ |a| 10^U(-3,1), wider k grid.
 (S6) which breaking terms are needed: for each healthy hit, zero each c_j in turn and re-test.
 (S7) TT speed: breaking terms that touch the TT sector (c0: (d h_ij)^2, c4: hdot_ij^2) shift c_T^2 by
      (1 + 4 c0)/(1 + 4 c4) - 1 in this normalisation (checked symbolically below)."""
import sys, time, pickle; sys.path.insert(0, '.')
import sympy as sp, numpy as np
from w3_lib import w, k, spectrum_tools, classify

t, x, y, z = sp.symbols('t x y z', real=True); X = (x, y, z)
Fn = lambda nm: sp.Function(nm)(t, x)
grad = lambda f: [sp.diff(f, v) for v in X]
dot = lambda u, v: sum(p*q for p, q in zip(u, v))
dt = lambda f: sp.diff(f, t)
def fourier_matrix(L, fields):
    L = sp.expand(L.doit()); n = len(fields)
    def sym(fac):
        if isinstance(fac, sp.Derivative):
            mult = 1
            for var, cnt in fac.variable_count:
                mult *= (-sp.I*w)**cnt if var == t else (sp.I*k)**cnt
            return fields.index(fac.expr), mult
        return fields.index(fac), 1
    M = sp.zeros(n, n)
    for term in sp.Add.make_args(L):
        coeff, facs = sp.Integer(1), []
        for fac in sp.Mul.make_args(term):
            if isinstance(fac, sp.Derivative) or (isinstance(fac, sp.Function) and fac.args == (t, x)):
                facs.append(fac)
            elif isinstance(fac, sp.Pow) and fac.exp == 2 and (isinstance(fac.base, sp.Derivative) or (isinstance(fac.base, sp.Function) and fac.base.args == (t, x))):
                facs += [fac.base, fac.base]
            else:
                coeff *= fac
        if not facs: continue
        (ia, s1), (ib, s2) = sym(facs[0]), sym(facs[1])
        M[ib, ia] += coeff*s1*sp.conjugate(s2)/4; M[ia, ib] += coeff*sp.conjugate(s1)*s2/4
    return M.applyfunc(sp.expand)

lam, eta, a = sp.symbols('lam eta a', real=True)
ms = sp.symbols('m0:5', real=True); cs = sp.symbols('c0:13', real=True)
Phi, s, Psi, E = [Fn(n) for n in ('Phi', 's', 'Psi', 'E')]
B = s + dt(E); R = range(3)
Kij = [[-dt(Psi)*(1 if i == j else 0) - sp.diff(s, X[i], X[j]) for j in R] for i in R]
Ktr = sum(Kij[i][i] for i in R); KK = sum(Kij[i][j]**2 for i in R for j in R)
L_KH = sp.Rational(1, 2)*(KK - lam*Ktr**2) + (dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi))) + eta/2*dot(grad(Phi), grad(Phi))
Fa = a*(-dot(grad(Phi), grad(E)) - sp.Rational(1, 2)*dot(grad(s), grad(s)))
h00 = Phi; h0 = grad(B)
hij = [[-2*Psi*(1 if i == j else 0) + 2*sp.diff(E, X[i], X[j]) for j in R] for i in R]
tr = sum(hij[i][i] for i in R)
masses = [h00**2, dot(h0, h0), sum(hij[i][j]**2 for i in R for j in R), tr**2, h00*tr]
two = [sum(sp.diff(hij[i][j], X[l])**2 for i in R for j in R for l in R), sum(sp.diff(tr, X[l])**2 for l in R),
       sum(sum(sp.diff(hij[i][j], X[i]) for i in R)**2 for j in R), sum(sp.diff(hij[i][j], X[i], X[j]) for i in R for j in R)*tr,
       sum(dt(hij[i][j])**2 for i in R for j in R), dt(tr)**2, sum(sp.diff(h0[j], X[i])**2 for i in R for j in R),
       sum(sp.diff(h0[i], X[i]) for i in R)**2, sum(h0[i]*sp.diff(dt(hij[i][j]), X[j]) for i in R for j in R),
       sum(h0[i]*sp.diff(dt(tr), X[i]) for i in R), sum(sp.diff(h00, X[i])*sp.diff(tr, X[i]) for i in R),
       sum(sp.diff(h00, X[i])*sp.diff(hij[i][j], X[j]) for i in R for j in R), dot(grad(h00), grad(h00))]
L = L_KH + Fa + sum(m*q for m, q in zip(ms, masses)) + sum(c*q for c, q in zip(cs, two))
t0 = time.time()
M = fourier_matrix(L, [Phi, s, Psi, E])
pickle.dump(M, open('w3_c2_symbol.pkl', 'wb'))
pars = (lam, eta, a) + ms + cs
cf, Mf, dMf, poly = spectrum_tools(M, pars)
print(f"symbol built in {time.time()-t0:.1f}s; det degree in w^2 = {poly.degree()}")

# (S7) TT check: h_ij = e_ij(t,x) TT polarisation (e_yz); the GR TT action in this normalisation is
# 1/2 K_ij K_ij - (1/2)... -> use L_KH tensor part: K_ij = 1/2 hdot_ij, R-term -> -(1/4)(d h)^2 ... check speed:
hT = Fn('hT')
hTT = [[0, 0, 0], [0, 0, hT], [0, hT, 0]]
KT = [[sp.Rational(1, 2)*dt(hTT[i][j]) for j in R] for i in R]
L_T = sp.Rational(1, 2)*sum(KT[i][j]**2 for i in R for j in R) - sp.Rational(1, 8)*sum(sp.diff(hTT[i][j], X[l])**2 for i in R for j in R for l in R) \
      + cs[0]*sum(sp.diff(hTT[i][j], X[l])**2 for i in R for j in R for l in R) + cs[4]*sum(dt(hTT[i][j])**2 for i in R for j in R)
MT = fourier_matrix(L_T, [hT])
cT2 = sp.solve(sp.Eq(MT[0, 0], 0), w**2)
print("(S7) TT dispersion w^2 =", [sp.factor(r) for r in cT2], " -> c_T^2 = (1 - 8 c0)/(1 + 8 c4) with GR TT normalised to c_T = 1")

ks = np.logspace(-4, 5, 28)
def health(pv, ks=ks):
    bad = 0
    for kv in ks:
        try: out = classify(cf, Mf, dMf, kv, pv)
        except Exception: return 99
        bad += sum(1 for tg, _ in out if tg != 'healthy')
        if bad: return bad
    return bad
rng = np.random.default_rng(7)
def logu(lo, hi, n): return np.sign(rng.uniform(-1, 1, n))*10**rng.uniform(lo, hi, n)
z13 = np.zeros(13)
# S4
n4 = 0; N = 2000
for i in range(N):
    pv = (1.05, 0.5, -1.0) + (0.0,)*5 + tuple(logu(-3, 0, 13))
    if health(pv) == 0: n4 += 1
print(f"(S4) masses = 0, breaking O(1e-3..1), lam=1.05 eta=0.5: {n4}/{N} healthy at all k in [1e-4, 1e5]")
# S5
hits_by_p = {}
for p in range(0, 5):
    hits = []
    for i in range(2500):
        pv = (1 + rng.uniform(0.001, 0.095), rng.uniform(0.01, 1.99), -1.0) + tuple(logu(-3, 1, 5)) + tuple(logu(-p - 1, -p, 13))
        if health(pv) == 0: hits.append(pv)
    hits_by_p[p] = hits
    print(f"(S5) breaking |c| ~ 1e-{p+1}..1e-{p}, lam-1 in (0.001,0.095), eta in (0,2): {len(hits)}/2500 healthy at all k")
pickle.dump(hits_by_p, open('w3_c2_hits.pkl', 'wb'))
# S6: necessity of each breaking term / mass for the hits
allhits = [h for p in hits_by_p for h in hits_by_p[p]]
need_c = np.zeros(13); need_m = np.zeros(5)
for pv in allhits[:40]:
    for j in range(13):
        q = list(pv); q[8 + j] = 0.0
        if health(tuple(q)) != 0: need_c[j] += 1
    for j in range(5):
        q = list(pv); q[3 + j] = 0.0
        if health(tuple(q)) != 0: need_m[j] += 1
print(f"(S6) over {min(40, len(allhits))} hits: # hits that break when term j is zeroed")
print("     masses (h00^2, h0i^2, hij^2, hii^2, h00 hii):", need_m.astype(int).tolist())
print("     breaking c0..c12:", need_c.astype(int).tolist())
for pv in allhits[:6]:
    print(f"   hit lam={pv[0]:.4f} eta={pv[1]:.3f} m={np.round(np.array(pv[3:8]), 4).tolist()} max|c|={np.max(np.abs(pv[8:])):.2e} c0={pv[8]:+.2e} c4={pv[12]:+.2e}")
