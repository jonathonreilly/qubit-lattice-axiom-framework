#!/usr/bin/env python3
"""CIB-R2: admissible mark family; independent symbolic construction."""
import json,sys
import sympy as s

z=s.Symbol('s',real=True)
t0=s.Rational(1,64)
t=t0*(1+z)
checks=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)})

# t>0 on the closed mark interval, so the maximum is its right endpoint.
derivatives=[s.diff(t,z,j) for j in range(4)]
row=max(2*abs(p.subs(z,b)) for p in derivatives for b in (-s.Rational(1,4),s.Rational(1,4)))
check('weighted_marked_row',row==s.Rational(5,128))
check('strict_marked_hypothesis',row<s.Rational(1,8))
check('uniform_precision_floor',1-t.subs(z,s.Rational(1,4))==s.Rational(251,256))
check('unscaled_mark_would_fail',2*abs(s.diff(z,z))>s.Rational(1,8))
values=[]
for d in (1,2,5):
    # Build the original 2d dimensional precision and differentiate its determinant.
    q=s.eye(2*d)
    for i in range(d):q[i,d+i]=q[d+i,i]=t
    determinant=q.det(method='domain-ge')
    f=s.log(determinant)/2
    first=s.simplify(s.diff(f,z).subs(z,0))
    second=s.simplify(s.diff(f,z,2).subs(z,0))
    check(f'first_chain_factor_{d}',first==-d*t0**2/(1-t0**2))
    check(f'second_chain_factor_{d}',second==-d*t0**2*(1+t0**2)/(1-t0**2)**2)
    check(f'first_omitted_chain_mutation_{d}',first!=-d*t0/(1-t0**2))
    check(f'second_omitted_chain_mutation_{d}',second!=-d*(1+t0**2)/(1-t0**2)**2)
    check(f'vacuum_constant_still_leaves_marks_{d}',s.simplify(s.diff(f-f.subs(z,0),z).subs(z,0))==first and first!=0)
    values.append({'d':d,'first':str(first),'second':str(second)})
out={'scope':'Generic marked-lemma witness, not actual optical source dependence','parameter':'t(s)=(1+s)/64, |s|<=1/4','marked_row':str(row),'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'values':values}
print(json.dumps(out,indent=2));sys.exit(not all(c['passed'] for c in checks))
