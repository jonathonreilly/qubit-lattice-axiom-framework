# Case split using exact 1D restrictions on group-fixed circles.
import sympy as sp, pickle, sys, os
free, Fs, coeqs = pickle.load(open('q1.pkl','rb'))
c = sp.symbols('c1:4'); s = sp.symbols('s1:4'); t = sp.Symbol('t')
u,w,u2,w2 = sp.symbols('u w u2 w2')
def restrict(F, k):
    e = F.subs({c[a]: sp.cos(k[a]) for a in range(3)} | {s[a]: sp.sin(k[a]) for a in range(3)})
    return sp.expand(sp.expand_trig(e))
def tcoeffs(e):
    # coefficients w.r.t. cos(t), sin(t) polynomial representation after rewriting into exponentials
    e = sp.expand(e.rewrite(sp.exp))
    z = sp.Symbol('z')
    e = sp.expand(e.subs(sp.exp(sp.I*t), z).subs(sp.exp(-sp.I*t), 1/z))
    e = sp.expand(e*z**8)
    P = sp.Poly(e, z)
    out=[]
    for co in P.coeffs():
        co = sp.expand(co); out += [sp.re(co).expand(), sp.im(co).expand()] if co.has(sp.I) else [co]
    return [o for o in out if o!=0]
nhat = [1/sp.sqrt(3)]*3; mhat = [1/sp.sqrt(2), -1/sp.sqrt(2), 0]
diag = [restrict(F,(t,t,t)) for F in Fs]
L0 = [restrict(F,(t,-t,0)) for F in Fs]
Lpi = [restrict(F,(t,-t,sp.pi)) for F in Fs]
pickle.dump((diag,L0,Lpi), open('q1_restr.pkl','wb'))
print(diag[0]); print(L0[1])
