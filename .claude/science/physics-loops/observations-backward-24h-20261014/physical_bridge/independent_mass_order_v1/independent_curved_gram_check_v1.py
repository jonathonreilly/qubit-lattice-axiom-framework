#!/usr/local/bin/python3
"""Exact overlap and independently sorted-interval massless comparison Gram."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value,**detail):
    row={'name':name,'passed':bool(value),**detail};checks.append(row)
    if not value:raise AssertionError(row)

z,s,H=sp.symbols('z s H',real=True)
L=sp.Rational(3,5);times=[sp.Rational(7,5)+i for i in range(4)];gamma=[-1,3,-3,1]
coeff=[];knots=[]
for g,t in zip(gamma,times):
    coeff += [g*(1-H*(t-2*L)+z*(1-H*s)),g*(-1+H*t+z*(1-H*s)),-2*z*g*(1-H*(s+z*L))]
    knots += [t-2*L,t,t-L-z*L]
check('total_step_coefficient_zero',sp.expand(sum(coeff))==0)
check('all_knots_positive',all(k.subs(z,end)>0 for k in knots for end in [-1,1]))
total=sp.Integer(0);global_cuts={sp.Integer(-1),sp.Integer(1)};piece_count=0
for i in range(12):
    for j in range(i,12):
        cuts=[sp.Integer(-1),sp.Integer(1)]
        difference=sp.Poly(knots[i]-knots[j],z)
        if difference.degree()==1:
            cross=-difference.nth(0)/difference.nth(1)
            if -1<cross<1:cuts.insert(1,cross);global_cuts.add(cross)
        product=sp.Poly((1 if i==j else 2)*coeff[i]*coeff[j],s)
        primitive_s=product.integrate().as_expr()
        for lo,hi in zip(cuts[:-1],cuts[1:]):
            mid=(lo+hi)/2
            smaller=knots[i] if (knots[i]-knots[j]).subs(z,mid)<=0 else knots[j]
            overlap=sp.expand(primitive_s.subs(s,smaller)-primitive_s.subs(s,0))
            primitive_z=sp.Poly(overlap,z).integrate().as_expr()
            total+=primitive_z.subs(z,hi)-primitive_z.subs(z,lo);piece_count+=1
pi_gram=sp.Poly(sp.expand(total/4),H)
check('degree_exactly_two',pi_gram.degree()==2)
g0,g1,g2=[pi_gram.nth(i) for i in range(3)]
check('flat_limit_exact',g0==sp.Rational(329,54),coefficient=str(g0))
check('gram_coefficient_diagonals_positive',g0>0 and g2>0)
det=sp.factor(g0*g2-g1*g1/4)
check('gram_cauchy_determinant_nonnegative',det>=0,determinant=str(det))

# Distinct representation: sum active steps between sorted knots, then square.
# Temporal polynomial degree is 2; direction degree per ordering cell <= 7.
zn,zw=leggauss(9);sn,sw=leggauss(2)
float_times=np.array([float(t) for t in times]);float_gamma=np.array(gamma,float)
float_L=float(L);cuts=sorted(float(t) for t in global_cuts)
def sorted_integral(h):
    value=0.
    for za,zb in zip(cuts[:-1],cuts[1:]):
        for zz,wz in zip((za+zb)/2+(zb-za)/2*zn,(zb-za)/2*zw):
            kk=np.column_stack([float_times-2*float_L,float_times,float_times-float_L-zz*float_L]).ravel()
            edges=np.unique(kk)
            inner=0.
            for sa,sb in zip(edges[:-1],edges[1:]):
                ss=(sa+sb)/2+(sb-sa)/2*sn
                hh=[]
                for st in ss:
                    aa=np.column_stack([float_gamma*(1-h*(float_times-2*float_L)+zz*(1-h*st)),
                        float_gamma*(-1+h*float_times+zz*(1-h*st)),
                        -2*zz*float_gamma*(1-h*(st+zz*float_L))]).ravel()
                    hh.append(np.sum(aa[st<kk])**2)
                inner+=(sb-sa)/2*np.dot(sw,hh)
            value+=wz*inner
    return value/4
rows=[]
for h in [sp.Integer(0),sp.Rational(1,25),sp.Rational(1,10),sp.Rational(1,5)]:
    exact=pi_gram.as_expr().subs(H,h);numeric=sorted_integral(float(h))
    check('sorted_interval_agreement_H_'+str(h),abs(float(exact)-numeric)<2e-11,
        exact_pi_gram=str(exact),numeric_pi_gram=float(numeric),absolute_error=abs(float(exact)-numeric))
    rows.append({'H':str(h),'pi_gram':str(exact),'numeric_pi_gram':float(numeric)})
result={'checks_passed':len(checks),'checks':checks,'pi_gram_polynomial':str(pi_gram.as_expr()),
    'pi_gram_coefficients_ascending':[str(v) for v in [g0,g1,g2]],'piece_count':piece_count,
    'direction_ordering_cuts':[str(v) for v in sorted(global_cuts)],'numeric_sorted_intervals':rows,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'precheck_sha256':hashlib.sha256((HERE/'CURVED_GRAM_PRECHECK_v1.md').read_bytes()).hexdigest(),
    'exposure':'No author composition note or curved implementation read before this execution.',
    'scope':'The massless comparison operator of curved-derived weights, not the actual curved KG norm.'}
with (HERE/'INDEPENDENT_CURVED_GRAM_RESULTS_v1.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'checks_passed':len(checks),'pi_gram':str(pi_gram.as_expr()),'source_sha256':result['source_sha256']}))
