"""Kill check: does the planar identity system discriminate? Replace the V2 normalisation target R2 by wrong quadratic forms,
and replace T2's DeWitt ratio c, then test consistency exactly (mod p) and in float."""
import sys
from fractions import Fraction as F
import solve, model
from model import V, XX, YY, ZZ, T2, bracket, fadd

def form(terms):
    out = {}
    for (c1, p1, c2, p2, coef) in terms:
        key = tuple(sorted([V('h', c1, p1), V('h', c2, p2)]))
        out[key] = out.get(key, F(0)) + F(coef)
    return out

R2_true = model.R2_S1()
variants = {
 'true R2': R2_true,
 '2*R2 (scale)': {k: 2*v for k, v in R2_true.items()},
 'mass h_yy h_zz (no derivs)': form([(YY,0,ZZ,0,1)]),
 'R2 + mass': {**R2_true, **{k: R2_true.get(k, F(0)) + v for k, v in form([(YY,0,ZZ,0,1)]).items()}},
 'h_yy^2 mass': form([(YY,0,YY,0,1)]),
 '(Dh_yy)^2 (gauge-inv? no cross)': form([(YY,0,YY,0,2),(YY,0,YY,1,-2)]),
 '(D h_xx)(D h_yy)': form([(XX,0,YY,0,2),(XX,0,YY,1,-1),(XX,1,YY,0,-1)]),
 '(D h_yy)(D h_zz) with wrong sign': {k: -v for k, v in R2_true.items()},
}
R = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for name, fn in variants.items():
    solve.R2_S1 = (lambda f=fn: f)
    res, _ = solve.analyse(R, 'full', exact=True, verbose=False)
    print(f"R={R} {name:38s} rows {res['rows']} cols {res['cols']} rank {res['float_rank']} resid {res['float_resid']:.2e} modOK {res['mod'][0][2]}", flush=True)
