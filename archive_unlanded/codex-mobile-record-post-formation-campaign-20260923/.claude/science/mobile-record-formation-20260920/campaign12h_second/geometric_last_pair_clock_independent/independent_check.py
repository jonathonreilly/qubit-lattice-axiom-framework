#!/usr/bin/env python3
"""Independent clock, Schur complement, correction and monomer-count checks.

No author clock checker or output is imported. Only the previously sealed
independent matching primitives are reused; no writes outside --out occur.
"""
import sys
sys.dont_write_bytecode=True
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
PRIMITIVES=HERE.parent/'geometric_partner_independent/independent_check.py'
assert hashlib.sha256(PRIMITIVES.read_bytes()).hexdigest()=='1b6c73b87789df05d5cafc03beff72ed7973ddfc22c3b0327128c0476bfd4c8f'
spec=importlib.util.spec_from_file_location('own_prior_matching_primitives',PRIMITIVES)
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
edge=own.edge

def matching_system(n,edges):
    states=own.all_matchings(n,edges);K=n//2
    near=[m for m in states if len(m)==K-1];full=[m for m in states if len(m)==K]
    ind={m:i for i,m in enumerate(near)};fi={m:i for i,m in enumerate(full)}
    S=s.zeros(len(near));A=s.zeros(len(near),len(full))
    for m,i in ind.items():
        for kind,data,target in own.channels(m,edges):
            if kind=='birth':A[i,fi[target]]+=1
            else:S[i,ind[target]]+=1;S[i,i]-=1
    h=A*s.ones(len(full),1)
    assert S==S.T and S*s.ones(len(near),1)==s.zeros(len(near),1)
    assert all(x in (0,1) for x in h)
    assert all(x==K for x in list(s.ones(1,len(near))*A))
    return near,full,S,A,h

def joint_laplace_controls():
    beta,z=s.symbols('beta z',positive=True);rows=[]
    for n in (4,6):
        edges={edge(i,(i+1)%n) for i in range(n)}
        near,full,S,A,h=matching_system(n,edges);H=s.diag(*h);p=sum(h)/len(near)
        U=(((-S+beta*(H+z*s.eye(len(near)))).inv(method='DM'))*beta*A).applyfunc(s.factor)
        assert (-S+beta*(H+z*s.eye(len(near))))*U==beta*A or ((-S+beta*(H+z*s.eye(len(near))))*U-beta*A).applyfunc(s.simplify)==s.zeros(len(near),len(full))
        expected=p/(p+z)/len(full)
        assert U.applyfunc(lambda x:s.simplify(s.limit(x,beta,0)-expected))==s.zeros(len(near),len(full))
        total=U*s.ones(len(full),1)
        assert total.subs(z,0).applyfunc(s.simplify)==s.ones(len(near),1)
        mean=(-S+beta*H).inv(method='DM')*s.ones(len(near),1)
        assert (-total.diff(z).subs(z,0)-beta*mean).applyfunc(s.simplify)==s.zeros(len(near),1)
        row={'cycle_size':n,'near_states':len(near),'full_matchings':len(full),'p':str(p),
             'joint_transform_limit_per_target':str(s.factor(expected)),
             'scaled_mean_from_Laplace_derivative_matches_direct_mean':True}
        if n==4:
            start=near.index(frozenset({(0,1)}));target=next(i for i,m in enumerate(full) if (0,1) in m)
            assert total.applyfunc(lambda x:s.simplify(x-1/(1+z)))==s.zeros(len(near),1)
            gap=s.factor(U[start,target]-U[start,target].subs(z,0)/(1+z))
            assert s.factor(gap-2*beta*z/((beta+4)*(z+1)*(beta*(z+1)+4)))==0
            row['finite_beta_independence_countercontrol']=str(gap)
            row['meaning']='Waiting time is exactly Exp(beta), yet the exit and waiting time need not be independent until the slow limit.'
        rows.append(row)
    return rows

def schur_controls(S,h):
    n=len(h);one=s.ones(n,1);P=one*one.T/n;Q=s.eye(n)-P;L=-S;H=s.diag(*h)
    p=sum(h)/n;q=h-p*one
    R0=(L+P).inv(method='DM')-P;w0=R0*q;C0=(q.T*w0)[0]/n
    assert L*w0==q and (one.T*w0)[0]==0
    correction=C0/p**2*one-w0/p
    checks=[]
    for beta in (s.Rational(1,2),s.Rational(1,10)):
        R=(L+beta*Q*H*Q+P).inv(method='DM')-P
        assert Q*R==R and R*Q==R
        w=R*q;C=(q.T*w)[0]/n;denominator=p-beta*C
        assert C>=0 and denominator>0
        formula=(one-beta*w)/(beta*denominator)
        direct=(L+beta*H).inv(method='DM')*one
        assert direct==formula and all(x>0 for x in direct)
        c=(one.T*direct)[0]/n;assert c>=1/(beta*p)
        checks.append({'beta':str(beta),'stationary_mean':str(c),'mean_lower_bound':str(1/(beta*p)),
                       'C_beta':str(C),'positive_schur_factor_p_minus_beta_C_beta':str(denominator)})
    return p,w0,C0,correction,checks

def cube_mean_controls():
    coords=list(it.product((0,1),repeat=3))
    edges={edge(i,j) for i in range(8) for j in range(i+1,8) if sum(abs(a-b) for a,b in zip(coords[i],coords[j]))==1}
    near,full,S,A,h=matching_system(8,edges)
    p,w0,C0,correction,checks=schur_controls(S,h)
    assert p==s.Rational(9,11) and C0==s.Rational(30,1331)
    def kind(m,i):
        axes={next(j for j in range(3) if coords[a][j]!=coords[b][j]) for a,b in m}
        return 0 if len(axes)==1 else (1 if h[i] else 2)
    types=[kind(m,i) for i,m in enumerate(near)];assert Counter(types)=={0:12,1:24,2:8}
    rows={};hb={}
    for i,t in enumerate(types):
        row=[sum(S[i,j] for j,u in enumerate(types) if u==v) for v in range(3)]
        if t in rows:assert row==rows[t] and h[i]==hb[t]
        else:rows[t]=row;hb[t]=h[i]
    Sbar=s.Matrix([rows[t] for t in range(3)]);Hbar=s.diag(*(hb[t] for t in range(3)))
    beta=s.symbols('beta',positive=True)
    tbar=((-Sbar+beta*Hbar).inv(method='DM')*s.ones(3,1)).applyfunc(s.factor)
    lift=s.Matrix([tbar[t] for t in types])
    assert ((-S+beta*s.diag(*h))*lift-s.ones(len(near),1)).applyfunc(s.factor)==s.zeros(len(near),1)
    expected_corrections=[s.Rational(-1,27),s.Rational(1,54),s.Rational(5,27)]
    for i,t in enumerate(types):
        assert correction[i]==expected_corrections[t]
        assert s.limit(lift[i]-1/(beta*p),beta,0)==correction[i]
    remainder_coefficients=[s.limit((tbar[i]-1/(beta*p)-expected_corrections[i])/beta,beta,0) for i in range(3)]
    stationary=s.factor(sum(lift)/len(near));stationary_correction=s.limit(stationary-1/(beta*p),beta,0)
    assert stationary_correction==C0/p**2==s.Rational(10,297)
    assert s.factor(tbar[0]-1/(beta*p)+2/(9*(beta+6)))==0
    return {'near_states':len(near),'full_matchings':len(full),'p':str(p),'leading_scaled_mean':str(1/p),
            'C_0':str(C0),'stationary_first_correction':str(stationary_correction),'pointwise_checks':checks,
            'mean_classes':[{'class':i,'states':types.count(i),'exact_mean':str(tbar[i]),
                            'first_correction':str(expected_corrections[i]),'next_coefficient':str(remainder_coefficients[i])} for i in range(3)],
            'pointwise_lower_bound_countercontrol':'The all-parallel three-edge start has mean 11/(9 beta)-2/[9(beta+6)], below 1/(beta p). The note correctly restricts the one-sided mean bound to stationary entrance.'}

def elementary_clock_controls():
    rows=[]
    for n,edges,name in [(2,{(0,1)},'single_near_state'),(4,{(0,1),(1,2),(2,3),(0,3)},'constant_hazard_C4')]:
        near,full,S,A,h=matching_system(n,edges);p,w,C,correction,checks=schur_controls(S,h)
        assert p==1 and C==0 and w==s.zeros(len(near),1) and correction==w
        rows.append({'case':name,'near_states':len(near),'exact_mean':'1/beta','first_correction':'0'})
    beta,z=s.symbols('beta z',positive=True)
    S=beta*s.Matrix([[-1,1],[1,-1]]);h=s.Matrix([1,0]);H=s.diag(*h)
    scaled_mean=beta*((-S+beta*H).inv()*s.ones(2,1));assert scaled_mean==s.Matrix([2,3])
    laplace=((-S+beta*(H+z*s.eye(2))).inv()*beta*h).applyfunc(s.factor)
    assert laplace[0].subs(z,1)==s.Rational(2,5)
    reducible=s.zeros(2);assert (-reducible+beta*H).det()==0
    return {'positive_controls':rows,'loss_of_fixed_relaxation_countercontrol':{'generator':'S_beta=beta*[[-1,1],[1,-1]], h=(1,0)',
            'scaled_means':list(map(str,scaled_mean)),'stationary_rate_prediction':'1/p=2',
            'transform_at_s_1_start_0':str(laplace[0].subs(z,1)),'exponential_prediction_at_s_1':'1/3'},
            'reducibility_countercontrol':'S=0,h=(1,0) has p>0 but its killed matrix is singular and its zero-hazard component never forms.'}

def counting_dp(n,edges):
    neighbor=[0]*n
    for a,b in edges:neighbor[a]|=1<<b;neighbor[b]|=1<<a
    @lru_cache(None)
    def perfect(mask):
        if not mask:return 1
        bit=mask&-mask;x=bit.bit_length()-1;rest=mask^bit;choices=neighbor[x]&rest;total=0
        while choices:
            ybit=choices&-choices;choices^=ybit;total+=perfect(rest^ybit)
        return total
    @lru_cache(None)
    def polynomial(mask):
        if not mask:return (1,)
        bit=mask&-mask;x=bit.bit_length()-1;rest=mask^bit;out=list(polynomial(rest));choices=neighbor[x]&rest
        while choices:
            ybit=choices&-choices;choices^=ybit;coeff=polynomial(rest^ybit)
            if len(out)<len(coeff)+1:out.extend([0]*(len(coeff)+1-len(out)))
            for k,value in enumerate(coeff):out[k+1]+=value
        return tuple(out)
    mask=(1<<n)-1;poly=polynomial(mask);assert poly[n//2]==perfect(mask)
    return mask,perfect,poly

def monomer_count_controls():
    rows=[]
    for d,N in ((1,4),(1,6),(1,8),(2,4)):
        coords=list(it.product(range(N),repeat=d));index={x:i for i,x in enumerate(coords)};edges=set()
        for x in coords:
            for axis in range(d):
                y=list(x);y[axis]=(y[axis]+1)%N;edges.add(edge(index[x],index[tuple(y)]))
        V=len(coords);K=V//2;L=[index[x] for x in coords if sum(x)%2==0];R=[i for i in range(V) if i not in L]
        mask,perfect,poly=counting_dp(V,edges);Z=perfect(mask);Omega=poly[K-1]
        hole_counts={v:perfect(mask^(1<<0)^(1<<v)) for v in R};chi=F(sum(hole_counts.values()),Z)
        assert chi==F(Omega,K*Z)
        pair_sum=sum(perfect(mask^(1<<u)^(1<<v)) for u in L for v in R);assert pair_sum==Omega
        double_sum=sum(perfect(mask^(1<<u)^(1<<v)) for u in range(V) for v in range(V) if (sum(coords[u])+sum(coords[v]))%2)
        assert double_sum==2*Omega
        adj={b if a==0 else a for a,b in edges if 0 in (a,b)}
        assert len(adj)==2*d and all(F(hole_counts[v],Z)==F(1,2*d) for v in adj)
        p=F(K*Z,Omega);assert p==1/chi
        rows.append({'dimension':d,'side':N,'volume':V,'Z':Z,'near_matchings':Omega,'chi':str(chi),'p':str(p),
                     'neighbor_Xi':str(F(1,2*d)),'ordered_all_vertex_hole_count':double_sum,
                     'external_Theorem_2_1_applicable':False,'purpose':'Exact counting and factor-of-two control only; these finite low-dimensional controls do not test the imported d>2 asymptotic theorem.'})
    n=4;edges={(0,1),(1,2),(2,3)};mask,perfect,poly=counting_dp(n,edges)
    chi_origin=F(sum(perfect(mask^(1<<0)^(1<<v)) for v in (1,3)),perfect(mask))
    ratio=F(poly[1],2*perfect(mask));assert chi_origin==2 and ratio==F(3,2)
    d,r=s.symbols('d r',positive=True)
    lower_per_side=(1-r/2)/(2*d);upper_per_side=1/(2*d)
    assert s.factor(lower_per_side/2-(1-r/2)/(4*d))==0 and upper_per_side/2==1/(4*d)
    return {'tori':rows,'translation_hypothesis_countercontrol':{'graph':'P4','origin_chi':str(chi_origin),'Omega_over_K_Z':str(ratio)},
            'conversion_to_total_volume':{'K_over_V':'1/2','lower':'(1-r_d/2)/(4*d)','upper':'1/(4*d)'},
            'r_definition':'Strictly positive-time expected returns, not the Green function including the initial visit.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result={}
    for name,fn in [('joint_laplace',joint_laplace_controls),('cube_mean',cube_mean_controls),
                    ('elementary_clocks',elementary_clock_controls),('monomer_counts',monomer_count_controls)]:
        result[name]=fn();print(json.dumps({name:result[name]},indent=2),flush=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n');print('PASS: independent clock/mean/count controls.',flush=True)
