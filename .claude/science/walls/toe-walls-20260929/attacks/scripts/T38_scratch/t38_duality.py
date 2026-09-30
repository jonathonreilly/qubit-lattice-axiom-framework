"""T38 test 6: Kramers-Wannier-type self-duality on Z3 as a route to r = 1/2.
Duality = discrete Fourier transform between the circulant's defining vector c = (a, b, conj b) and its spectrum lam.
Self-dual point: lam = mu * c (or lam = mu * c up to the DFT^2 reflection).  Run: python3 t38_duality.py"""
import sympy as sp
a, b, mu = sp.symbols('a b mu')
w = sp.exp(2*sp.pi*sp.I/3)
# real-b slice (the only slice on which lam_k and c_k can both be real vectors of the same type)
lam = [a + b*w**k + b*w**(-k) for k in range(3)]
lam = [sp.simplify(sp.expand_complex(x)) for x in lam]           # a+2b, a-b, a-b
c = [a, b, b]
sol = sp.solve([lam[0]-mu*c[0], lam[1]-mu*c[1]], [mu, b], dict=True)
print("self-dual solutions (a=1):", [{k: sp.nsimplify(sp.simplify(v.subs(a,1))) for k, v in s.items()} for s in sol])
for s in sol:
    bb = sp.simplify(s[b].subs(a,1)); print("   b/a =", bb, "=", sp.N(bb, 8), " r = (b/a)^2 =", sp.N(bb**2, 8), " Q =", sp.N((1+2*bb**2)/3, 8))
# Potts q=3 check: weight (1,x,x) self-dual at x = 1/(1+sqrt3)
x = sp.symbols('x', positive=True); print("Potts q=3 self-dual x:", sp.solve(sp.Eq((1-x)/(1+2*x), x), x), " 1/(1+sqrt3) =", sp.N(1/(1+sp.sqrt(3))))
# complex b: lam_k real forces mu*c_1 real and mu*conj(c_1) real; check that a solution with Im b != 0 exists?
br, bi, mr, mi = sp.symbols('b_R b_I mu_R mu_I', real=True)
av = 1
lam_c = [av + 2*(br), av + 2*sp.re(sp.expand_complex((br+sp.I*bi)*w)), av + 2*sp.re(sp.expand_complex((br+sp.I*bi)*w**2))]
cvec = [av, br+sp.I*bi, br-sp.I*bi]
eqs = []
for k in range(3):
    e = sp.expand_complex(lam_c[k] - (mr+sp.I*mi)*cvec[k]); eqs += [sp.re(e), sp.im(e)]
sols = sp.solve(eqs, [br, bi, mr, mi], dict=True)
print("complex-b self-dual solutions:", [{k: sp.nsimplify(v) for k, v in s.items()} for s in sols])
print("=> every self-dual point has Im b = 0 (degenerate doublet); r = 0.134 (Q=0.423) or 1.866 (Q=1.577); none is r = 1/2")
