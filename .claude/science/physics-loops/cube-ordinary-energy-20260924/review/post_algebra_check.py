#!/usr/bin/env python3
"""Independent POST checks of contour coefficients and scale arithmetic."""
from pathlib import Path
import sympy as s
import json
z=s.symbols('z')
a,b,c0,c1,c2,g=s.symbols('a b c0 c1 c2 g', real=True)
from functools import lru_cache
from math import factorial
@lru_cache(None)
def denominator_residue(counts):
    n0,n1,n2=counts
    if n2==0:return s.Integer(0)
    analytic=1/(z**n0*(z-1)**n1)
    return s.diff(analytic,z,n2-1).subs(z,2)/factorial(n2-1)
diagonal=(c0,c1-s.I*g,c2)
def coefficient(order,source):
    answer=s.Integer(0)
    counts=[0,0,0];counts[source]=1
    def walk(state,remaining,coeff,counts):
        nonlocal answer
        if remaining==0:
            if state==2:answer+=coeff*denominator_residue(tuple(counts))
            return
        for new,weight in ((state-1,-a if state==1 else -b),(state+1,-a if state==0 else -b)):
            if 0<=new<=2:
                cc=counts.copy();cc[new]+=1
                walk(new,remaining-1,coeff*weight,cc)
        if remaining>=2:
            cc=counts.copy();cc[state]+=1
            walk(state,remaining-2,coeff*diagonal[state],cc)
    walk(source,order,s.Integer(1),counts)
    return s.expand(answer)
row=[[coefficient(n,j) for j in range(3)] for n in range(5)]
assert row[0]==[0,0,1]
assert row[1]==[0,-b,0]
assert row[2][0]==a*b/2
assert row[2][1]==0
assert row[3][0]==0 and row[3][2]==0
assert row[4][1]==0
assert s.diff(row[2][0],g)==0 and s.diff(row[1][1],g)==0
# A wrong sign or denominator is rejected by the exact symbolic residual.
assert s.simplify(row[2][0]-a*b)!=0
assert s.simplify(row[1][1]-b)!=0
alpha=s.symbols('alpha',real=True)
exponents={
 'relative_spin_error':2-2*alpha,
 'relative_coordinate_error':2-s.Rational(5,4)*alpha,
 'mean_high':-2+s.Rational(5,2)*alpha,
 'second_moment_high':-6+s.Rational(5,2)*alpha,
 'second_high_to_first_high_second_moment':4-s.Rational(5,2)*alpha,
 'mean_square_ratio_fast_term':2+s.Rational(5,2)*alpha,
 'mean_square_ratio_slow_term':6-s.Rational(5,2)*alpha,
}
assert s.solve(exponents['mean_high'],alpha)==[s.Rational(4,5)]
assert 2-s.Rational(4,5)==s.Rational(6,5)
assert exponents['second_moment_high'].subs(alpha,s.Rational(4,5))==-4
for k in ['relative_spin_error','relative_coordinate_error','second_high_to_first_high_second_moment','mean_square_ratio_fast_term','mean_square_ratio_slow_term']:
    assert exponents[k].subs(alpha,s.Rational(1,2))>0
    # Every listed exponent is linear; endpoint nonnegativity plus interior positivity suffices.
    assert exponents[k].subs(alpha,0)>=0 and exponents[k].subs(alpha,1)>=0
assert exponents['relative_spin_error'].subs(alpha,2)==-2
result={'contour':'Exact residue of (z-W-epsilon T-epsilon^2 Ceff)^(-1) at z=2, generic three-grade coefficients.',
        'projector_row_coefficients_through_order_four':[[str(x) for x in rr] for rr in row],
        'leading_row':'Pi2 E2 Pi0 = epsilon^2 ba/2; Pi2 E2 Pi1 = -epsilon b; Pi2 E2 Pi2=1+O(epsilon^2)',
        'exponents_for_tau_epsilon_minus_alpha':{k:str(v) for k,v in exponents.items()},
        'crossover_alpha':'4/5','crossover_physical_exponent':'6/5','crossover_variance_exponent':'-4',
        'fixed_physical_time_alpha_two_relative_error_exponent':'-2 (does not tend to zero)',
        'scope':'Exact symbolic coefficient and exponent arithmetic; not a substitute for the full operator proof or actual finite-spin propagation.'}
Path('POST_ALGEBRA_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('All stated exact symbolic assertions completed without failure.')
