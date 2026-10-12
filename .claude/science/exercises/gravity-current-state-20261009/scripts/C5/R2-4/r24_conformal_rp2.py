"""G3b: compare Riemann (and Ricci) correlators of (A) the positive 4D-TT Gaussian and (B) linearised GR,
at separated times, for a generic spatial momentum; and the momentum-space difference Chat_A - Chat_B
(is it a polynomial in p, i.e. a pure contact term?)."""
import numpy as np, sympy as sp
src = open('r24_conformal_rp.py').read()
src = src.replace("q = sp.Integer(1)\np = [q, sp.Integer(0), sp.Integer(0), p4]",
                  "q1, q2, q3 = sp.Rational(3,5), sp.Rational(-2,5), sp.Rational(1,3)\nq = sp.sqrt(q1**2+q2**2+q3**2)\np = [q1, q2, q3, p4]")
src = src.split("ts = np.arange")[0]
exec(src)
D = (Lm*(CA - CB)*Lm.T).applyfunc(lambda e: sp.cancel(sp.together(e)))
nonpoly = [(i, j) for i in range(D.shape[0]) for j in range(i, D.shape[0]) if sp.denom(sp.together(D[i, j])).free_symbols]
print("Riemann: #component pairs where Chat_A - Chat_B is NOT a polynomial in p4 (non-contact):", len(nonpoly), "of", D.shape[0]*(D.shape[0]+1)//2)
# Ricci check: R_mn = sum_r R_rmrn (Euclidean)
def ricci_rows():
    rows = []
    for m in range(4):
        for n in range(m, 4):
            expr = 0
            for r in range(4):
                expr += sp.Rational(1,2)*(p[m]*p[r]*hm(r, n) + p[r]*p[n]*hm(m, r) - p[r]*p[r]*hm(m, n) - p[m]*p[n]*hm(r, r))
            rows.append([sp.diff(expr, hs[i]) for i in range(10)])
    return sp.Matrix(rows)
Rc = ricci_rows()
for name, Ch in (("A", CA), ("B", CB)):
    Cr = (Rc*Ch*Rc.T).applyfunc(lambda e: sp.cancel(sp.together(e)))
    nonpoly = sum(1 for i in range(10) for j in range(i, 10) if sp.denom(sp.together(Cr[i, j])).free_symbols)
    print(f"Ricci-Ricci, model {name}: # non-contact (non-polynomial in p4) entries: {nonpoly} of 55")
