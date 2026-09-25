#!/usr/bin/env python3
"""Exact primitive cube series and a separate scalar continuous-source control.

No author builder, matrix source, parent control or candidate is imported.
The word calculation checks only coefficients through cubic order. The scalar
age model tests moment bookkeeping, not the cube's finite-spin limit.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import comb, exp, expm1
from pathlib import Path
import hashlib
import json
import time

HERE=Path(__file__).resolve().parent
A=(0,3,5,6)
B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
ZERO=(F(0),F(0))
ONE=(F(1),F(0))


def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,y):return (x[0]*y,x[1]*y)
def clean(v):return {w:c for w,c in v.items() if c!=ZERO}


def plus(*vectors):
    out={}
    for vec in vectors:
        for word,c in vec.items():out[word]=add(out.get(word,ZERO),c)
    return clean(out)


def scaled(vec,c):return clean({w:mul(v,c) for w,v in vec.items()})
def norm2(vec):return sum((c[0]*c[0]+c[1]*c[1] for c in vec.values()),F(0))
def grade(word):return sum(word[0][a]==0 for a in A)


def gauss(word):
    q,E=word;div=[0]*8
    for e,(a,b) in enumerate(EDGES):div[a]+=E[e];div[b]-=E[e]
    return tuple(div)==tuple(q[v]-int(v in A) for v in range(8))


@lru_cache(None)
def hops(word,outward,center=None):
    q,E=word;result=[]
    for e,(a,b) in enumerate(EDGES):
        if center is not None and a!=center:continue
        origin,dest=(a,b) if outward else (b,a)
        if q[origin] and not q[dest]:
            s=q[origin];qq=list(q);ee=list(E)
            qq[origin]=0;qq[dest]=s;ee[e]+=(-s if outward else s)
            new=(tuple(qq),tuple(ee));assert gauss(new)
            result.append(new)
    return tuple(result)


def apply_hop(vec,outward=True,center=None):
    out={}
    for w,c in vec.items():
        for z in hops(w,outward,center):out[z]=add(out.get(z,ZERO),c)
    return clean(out)


def apply_mark(vec,kind):
    e=0;a,b=EDGES[e];signs=(1,-1) if kind=='coherent' else ((1,) if kind=='plus' else (-1,))
    out={}
    for w,c in vec.items():
        q,E=w
        if q[a] or q[b]:continue
        for s in signs:
            qq=list(q);ee=list(E);qq[a]=s;qq[b]=-s;ee[e]+=s
            z=(tuple(qq),tuple(ee));assert gauss(z)
            out[z]=add(out.get(z,ZERO),c)
    return clean(out)


def gamma(word):
    q,_=word
    return 2*sum(not q[a] and not q[b] for a,b in EDGES)


@lru_cache(None)
def perturbation(word,degree,loss):
    if degree==1:
        out={}
        for z in hops(word,True)+hops(word,False):out[z]=add(out.get(z,ZERO),(F(-1),F(0)))
        return tuple(clean(out).items())
    out={}
    if grade(word)==0:
        # Rotor gated compensation C=P F*F P, reconstructed from paths.
        for z in hops(word,True):
            for zz in hops(z,False):
                if grade(zz)==0:out[zz]=add(out.get(zz,ZERO),ONE)
    if loss and gamma(word):out[word]=add(out.get(word,ZERO),(F(0),F(-gamma(word))))
    return tuple(clean(out).items())


@lru_cache(None)
def compositions(n):
    if n==0:return ((),)
    return tuple((d,)+tail for d in (1,2) if d<=n for tail in compositions(n-d))


@lru_cache(None)
def residue(counts,band):
    """Exact residue of product_g (z-g)^(-counts[g]) at z=band."""
    pole=counts[band]
    if pole==0:return F(0)
    degree=pole-1;series=[F(1)]+[F(0)]*degree
    for g,m in enumerate(counts):
        if g==band or m==0:continue
        terms=[F((-1)**k*comb(m+k-1,k),(band-g)**(m+k)) for k in range(degree+1)]
        series=[sum((series[j]*terms[k-j] for j in range(k+1)),F(0)) for k in range(degree+1)]
    return series[degree]


def projector_coefficient(vec,order,band,loss):
    out={}
    for comp in compositions(order):
        states={}
        for word,c in vec.items():
            counts=[0]*5;counts[grade(word)]=1
            states[(word,tuple(counts))]=c
        for degree in comp:
            new={}
            for (word,counts),c in states.items():
                for z,d in perturbation(word,degree,loss):
                    nn=list(counts);nn[grade(z)]+=1;key=(z,tuple(nn))
                    new[key]=add(new.get(key,ZERO),mul(c,d))
            states={k:v for k,v in new.items() if v!=ZERO}
        for (word,counts),c in states.items():
            cc=scale(c,residue(counts,band))
            out[word]=add(out.get(word,ZERO),cc)
    return clean(out)


def apply_projector_series(vec_series,band,loss,max_order=3):
    return [plus(*(projector_coefficient(vec_series[k],n-k,band,loss) for k in range(n+1)))
            for n in range(max_order+1)]


def select(vec,r):return {w:c for w,c in vec.items() if grade(w)==r}


def exact_source_checks():
    q=tuple(int(v in A) for v in range(8))
    zero=(q,(0,)*12)
    fields=[0]*12
    # Closed face 0->1->3->2->0, in the fixed A-to-B orientation.
    for a,b,s in [(0,1,1),(3,1,-1),(3,2,1),(0,2,-1)]:fields[EDGES.index((a,b))]=s
    circulation=(q,tuple(fields))
    rows=[]
    for name,word in [('zero',zero),('one_face_circulation',circulation)]:
        assert gauss(word)
        base=[{word:ONE},{},{},{}]
        hermitian_low=apply_projector_series(base,0,False)
        noevent_low=apply_projector_series(hermitian_low,0,True)
        high=apply_projector_series(hermitian_low,1,True)
        expected={z:(F(0),F(-gamma(z))) for z in hops(word,True)}
        assert high[0]==high[1]==high[2]=={}
        assert high[3]==expected
        for r in (2,3,4):
            assert all(not v for v in apply_projector_series(hermitian_low,r,True))
        for kind,b,r in [('plus',2,4),('minus',2,2),('coherent',4,6)]:
            marked=[apply_mark(v,kind) for v in noevent_low]
            first=apply_projector_series(marked,1,True)
            second=apply_projector_series(marked,2,True)
            birth=apply_mark(apply_hop({word:ONE}),kind)
            recoil=scaled(apply_hop(birth,True,0),(F(-1),F(0)))
            assert norm2(birth)==b and norm2(recoil)==r
            assert select(first[0],1)==select(first[1],1)==select(first[3],1)=={}
            assert select(first[2],1)==recoil
            assert all(not select(v,2) for v in second)
            # Independently form the cubic remote-hop cancellation.
            v0={word:ONE};v1=apply_hop(v0);v2=apply_hop(v1);v3=apply_hop(v2)
            left=scaled(apply_mark(v3,kind),(F(1,6),F(0)))
            middle=scaled(apply_hop(apply_mark(v2,kind)),(F(-1,2),F(0)))
            right=scaled(apply_hop(apply_hop(apply_mark(v1,kind))),(F(1,2),F(0)))
            assert plus(left,middle,right)=={}
            altered=plus(left,scaled(middle,(F(2),F(0))),right)
            assert norm2(altered)>0
            rows.append({'input':name,'mark':kind,'B_norm2':str(norm2(birth)),
                         'R_norm2':str(norm2(recoil)),
                         'first_high_grade_row_coefficient_norm2_orders_0_to_3':[str(norm2(select(v,1))) for v in first],
                         'second_high_grade_row_coefficient_norm2_orders_0_to_3':[str(norm2(select(v,2))) for v in second],
                         'altered_cubic_middle_coefficient_norm2':str(norm2(altered))})
    return {'rows':rows,'initial_first_high_coefficient':'-i Gamma_1 F on both checked physical inputs',
            'initial_higher_noevent_coefficients':'zero through cubic order for grades 2,3,4',
            'arithmetic':'Exact Gaussian rational coefficients and exact contour residues',
            'scope':'Two physical rotor inputs and three edge-01 marks; no complete matrix construction, finite-spin simulation or uniform-time numerical proof.'}


def scalar_continuous_source_checks():
    # An explicitly separate three-state classical source toy: the high state
    # has energy delta epsilon^-4, is fed with rate kappa*r*epsilon^2*q(t),
    # and loses probability at rate gamma/epsilon^2. Its complement is zero-energy.
    delta=1.3;kappa=.07;r=3.0;gam=1.8;lam=.4;rows=[]
    for eps,t in product((.2,.1,.05,.025),(.2,.7,1.4)):
        rate=gam/eps**2-lam
        high_p=kappa*r*eps**2*exp(-lam*t)*(-expm1(-rate*t))/rate
        assert 0<high_p<1
        mean=delta*eps**-4*high_p
        scaled_second=delta**2*eps**-4*high_p
        scaled_var=scaled_second-eps**4*mean**2
        target_mean=kappa*delta*r*exp(-lam*t)/gam
        target_second=delta*target_mean
        # A direct age quadrature, resolved on fast age, separate from the ODE formula.
        upper=min(t/eps**2,24/gam);n=12000;step=upper/n
        values=[exp(-gam*(j*step))*exp(-lam*(t-eps**2*j*step)) for j in range(n+1)]
        integ=step*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))/3
        quad_mean=kappa*delta*r*integ
        assert abs(quad_mean-mean)<2e-11
        rows.append({'epsilon':eps,'t':t,'mean':mean,'mean_limit':target_mean,
                     'eps4_second':scaled_second,'eps4_variance':scaled_var,
                     'eps4_second_and_variance_limit':target_second,
                     'age_quadrature_absolute_mean_error':abs(quad_mean-mean)})
    return {'rows':rows,'scope':'Separate scalar injection/depletion toy, not the cube; tests continuous-age scaling and mixed variance bookkeeping.'}


def envelope_checks():
    rows=[]
    for eps in (1e-1,1e-2,1e-3,1e-4,1e-5):
        cutoff=1/eps
        young_error_square=eps**4*((1+cutoff)**2.5-1)/2.5
        endpoint=(1+cutoff)**(-1.25)+eps**2*(1+cutoff)**.75
        old_age_bound=eps**-2*endpoint**2
        rows.append({'epsilon':eps,'young_error_square_integral':young_error_square,
                     'young_divided_by_eps_1_5':young_error_square/eps**1.5,
                     'old_age_square_integral_bound':old_age_bound,
                     'old_divided_by_sqrt_eps':old_age_bound/eps**.5,
                     'persistent_Oeps3_source_scaled_contribution_at_T1':1,
                     'persistent_Oeps4_source_scaled_contribution_at_T1':eps**2})
    assert all(row['young_divided_by_eps_1_5']<.51 and row['old_divided_by_sqrt_eps']<4.02 for row in rows)
    return {'rows':rows,'scope':'Arithmetic control of the analytic age-envelope exponents; no empirical cube decay fit.'}


def main():
    started=time.monotonic()
    result={'primitive_graded_sources':exact_source_checks(),
            'scalar_age_moments':scalar_continuous_source_checks(),
            'age_envelope_exponents':envelope_checks(),
            'elapsed_seconds':time.monotonic()-started,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'author_code_imported':False}
    data=json.dumps(result,indent=2)+'\n'
    (HERE/'INDEPENDENT_SOURCE_AGE_RESULTS.json').write_text(data)
    print(data,end='')


if __name__=='__main__':main()
