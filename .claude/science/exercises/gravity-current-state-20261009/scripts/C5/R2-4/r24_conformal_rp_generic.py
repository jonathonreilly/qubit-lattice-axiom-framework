"""R2-4 check G3 (generic spatial momentum (3/5,-2/5,1/3)): can the conformal mode be removed covariantly to get a POSITIVE graviton Gaussian
that is still reflection positive?  Compare, on gauge-invariant linearised Riemann correlators:
 (B) linearised GR (indefinite Gaussian; correlators defined by the de Donder covariance, gauge-independent
     on Riemann), and
 (A) the positive, normalisable, O(4)/W(B4)-covariant Gaussian obtained by restricting h to the 4D
     transverse-traceless subspace {p.h = 0, tr h = 0} (Landau gauge + trace removed: this kills the
     negative spin-0 direction found in G1).
OS check (continuum, exact residues): fixed spatial momentum q e_1, functionals F_a(t) = Riemann component a
at time t>0; Theta F_a(t) = r_a F_a(-t), r_a = (-1)^(# of time indices).  RP <=> the matrix
M[(a,t),(b,t')] = r_a C_ab(t+t') is PSD.  C_ab(tau) = i Res_{p4=iq} e^{i p4 tau} Chat_ab(p4) for tau>0.
"""
import itertools, numpy as np, sympy as sp
p4 = sp.Symbol('p4'); tau = sp.Symbol('tau', positive=True)
q1, q2, q3 = sp.Rational(3,5), sp.Rational(-2,5), sp.Rational(1,3)
q = sp.sqrt(q1**2+q2**2+q3**2)
p = [q1, q2, q3, p4]
pairs = [(m, n) for m in range(4) for n in range(m, 4)]
idx = {pr: i for i, pr in enumerate(pairs)}
def hcomp(H, m, n):   # component h_mn from 10-vector (plain components, no sqrt2)
    return H[idx[(min(m, n), max(m, n))]]
p2 = sum(x*x for x in p)
# Quadratic form K (plain components): build via symbolic differentiation
hs = sp.symbols('h0:10')
def hm(m, n): return hs[idx[(min(m, n), max(m, n))]]
trh = sum(hm(m, m) for m in range(4))
ph = [sum(p[m]*hm(m, n) for m in range(4)) for n in range(4)]
pph = sum(p[m]*p[n]*hm(m, n) for m in range(4) for n in range(4))
hh = sum(hm(m, n)**2 for m in range(4) for n in range(4))
Kq = sp.Rational(1, 2)*p2*hh - sum(x*x for x in ph) + pph*trh - sp.Rational(1, 2)*p2*trh**2
Kmat = sp.Matrix(10, 10, lambda i, j: sp.diff(Kq, hs[i], hs[j]) / 2)
F = sp.Matrix([[sp.diff(ph[n] - sp.Rational(1, 2)*p[n]*trh, hs[i]) for i in range(10)] for n in range(4)])
CB = (Kmat + F.T*F).inv()            # de Donder covariance of plain components (up to normalisation)
CB = CB.applyfunc(sp.simplify)
# (A): positive Gaussian on V = {p.h = 0, tr h = 0}: covariance = V (V^T K V)^{-1} V^T
cons = sp.Matrix([[sp.diff(e, hs[i]) for i in range(10)] for e in ph + [trh]])
V = cons.nullspace()
V = sp.Matrix.hstack(*V)
KV = (V.T*Kmat*V).applyfunc(sp.simplify)
print("eigen-check (A): K restricted to 4D-TT subspace is p^2/2 * Gram? ->",
      sp.simplify(KV - sp.Rational(1, 2)*p2*(V.T*V)) == sp.zeros(5, 5))
CA = (V*KV.inv()*V.T).applyfunc(sp.simplify)
# linearised Riemann: R_mnrs = 1/2 (p_n p_r h_ms + p_m p_s h_nr - p_m p_r h_ns - p_n p_s h_mr)  (i^2 absorbed)
bi = [(m, n) for m in range(4) for n in range(m+1, 4)]
comps = [(A, B) for i, A in enumerate(bi) for j, B in enumerate(bi) if j >= i]
def riem_row(m, n, r, s):
    expr = sp.Rational(1, 2)*(p[n]*p[r]*hm(m, s) + p[m]*p[s]*hm(n, r) - p[m]*p[r]*hm(n, s) - p[n]*p[s]*hm(m, r))
    return [sp.diff(expr, hs[i]) for i in range(10)]
Lm = sp.Matrix([riem_row(A[0], A[1], B[0], B[1]) for (A, B) in comps])
rsign = np.array([(-1)**sum(1 for x in (A[0], A[1], B[0], B[1]) if x == 3) for (A, B) in comps])
def Ctau(Ch):
    Chat = (Lm*Ch*Lm.T)
    n = Chat.shape[0]
    out = [[None]*n for _ in range(n)]
    for a in range(n):
        for b in range(a, n):
            e = sp.together(sp.simplify(Chat[a, b]))
            r = sp.residue(sp.exp(sp.I*p4*tau)*e, p4, sp.I*q)
            f = sp.lambdify(tau, sp.simplify(sp.I*r), 'numpy')
            out[a][b] = out[b][a] = f
    return out
ts = np.arange(0.25, 3.01, 0.25)
for name, Ch in (("B: linearised GR (de Donder)", CB), ("A: positive 4D-TT Gaussian", CA)):
    Cf = Ctau(Ch)
    n = len(comps); N = n*len(ts)
    M = np.zeros((N, N), dtype=complex)
    for a in range(n):
        for b in range(n):
            for i, t in enumerate(ts):
                for j, tp in enumerate(ts):
                    M[a*len(ts)+i, b*len(ts)+j] = rsign[a]*complex(Cf[a][b](t+tp))
    herm = np.max(np.abs(M - M.conj().T))
    ev = np.linalg.eigvalsh((M + M.conj().T)/2)
    print(f"{name}: OS matrix {N}x{N}, hermiticity defect {herm:.1e}, min eig {ev.min():.3e}, max eig {ev.max():.3e},"
          f" #eig < -1e-9*max: {int(np.sum(ev < -1e-9*ev.max()))}")
