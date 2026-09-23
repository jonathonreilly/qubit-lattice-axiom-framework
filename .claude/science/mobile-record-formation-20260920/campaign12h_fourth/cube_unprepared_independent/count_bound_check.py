"""Independent algebra for the sequential hazard-cap count bound."""
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
k,t,s=sp.symbols('k t s',positive=True)
r1=48*k;r2=16*k
a=sp.exp(-r1*t)
g=sp.integrate(r1*sp.exp(-r1*s)*sp.exp(-r2*(t-s)),(s,0,t))
h=1-a-g
g_expected=sp.Rational(3,2)*(sp.exp(-16*k*t)-sp.exp(-48*k*t))
h_expected=1-sp.Rational(3,2)*sp.exp(-16*k*t)+sp.Rational(1,2)*sp.exp(-48*k*t)
positive_integral=sp.integrate(r2*sp.exp(-r2*(t-s))*(1-sp.exp(-r1*s)),(s,0,t))
assert sp.simplify(g-g_expected)==0
assert sp.simplify(h-h_expected)==0
assert sp.simplify(h-positive_integral)==0
assert sp.simplify(sp.diff(h,t)-r2*g)==0
result={'r1':str(r1),'r2_upper_hazard':str(r2),'limiting_N4':str(a),
        'liminf_N6_bound':str(g_expected),'finite_spin_N8_upper_bound':str(h_expected),
        'positive_integral_representation_equal':True,'boundary_derivative_identity_h_prime_equals_r2_g':True,
        'scope':'Algebraic verification of derived bounds. It does not identify the true N6/N8 limits or assert equality of either upper hazard.'}
(HERE/'COUNT_BOUND_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
