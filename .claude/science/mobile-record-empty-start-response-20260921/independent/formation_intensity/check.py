#!/usr/bin/env python3
"""Independent epsilon-coefficient check with the complete motion semigroup."""
from fractions import Fraction as F
from itertools import product
from math import factorial, prod
from pathlib import Path
import json
import mpmath as mp
import numpy as np
import scipy
from scipy.sparse import csr_matrix, bmat
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import eigh

mp.mp.dps=70


def mf(x):
    return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(str(x))


def integral_I(rate,t):
    """Exact elementary expression for integral (t-v)^3 (1-exp(-rate*v))."""
    r,t=mf(rate),mf(t)
    if r==0:
        return mp.mpf(0)
    return t**4/4-t**3/r+3*t*t/r**2-6*t/r**3+6*(-mp.expm1(-r*t))/r**4


def axes_W():
    return [[F(3,2) if a==b else F(1,2) if (a^1)==b else F(1)
             for b in range(6)] for a in range(6)]


def construct(edges,W):
    n=3
    adj=[[] for _ in range(n)]
    for x,y,rate in edges:
        assert rate>0
        adj[x].append(y);adj[y].append(x)
    assert all(sum(row)==6 for row in W)
    assert all(W[a][b]==W[b][a]>0 for a,b in product(range(6),repeat=2))
    states=list(product(range(-1,6),repeat=n));ids={s:i for i,s in enumerate(states)}
    counts=[sum(a>=0 for a in s) for s in states]
    weights=[prod(W[s[x]][s[y]] for x,y,_ in edges if s[x]>=0 and s[y]>=0)
             for s in states]
    H=[];B=[]
    for i,s in enumerate(states):
        hr={};br={}
        for x,y,proposal in edges:
            if (s[x]<0)!=(s[y]<0):
                t=list(s);t[x],t[y]=t[y],t[x];j=ids[tuple(t)]
                hr[j]=hr.get(j,F(0))+proposal*weights[j]/(weights[i]+weights[j])
        for x in range(n):
            if s[x]<0:
                for a in range(6):
                    t=list(s);t[x]=a;j=ids[tuple(t)]
                    rate=prod(W[a][s[y]] for y in adj[x] if s[y]>=0)
                    assert weights[i]*rate==weights[j]
                    br[j]=rate
        hr[i]=-sum(hr.values());br[i]=-sum(br.values())
        H.append(hr);B.append(br)
    for i,row in enumerate(H):
        assert sum(row.values())==0
        for j,rate in row.items():
            assert weights[i]*rate==weights[j]*H[j].get(i,F(0))
    hazards=[-B[i][i] for i in range(len(states))]

    def multiply(row,matrix):
        out={}
        for i,value in row.items():
            for j,rate in matrix[i].items():
                out[j]=out.get(j,F(0))+value*rate
        return {i:v for i,v in out.items() if v}
    rows=[{ids[(-1,-1,-1)]:F(1)}]
    for _ in range(4):
        rows.append(multiply(rows[-1],B))
    assert not multiply(rows[0],H)
    assert not multiply(rows[1],H)
    assert not multiply(rows[2],H)
    coefficients=[sum(v*counts[i] for i,v in row.items())/F(factorial(r))
                  for r,row in enumerate(rows)]
    Hb=[sum(rate*hazards[j] for j,rate in row.items()) for row in H]
    level=[i for i in range(len(states)) if counts[i]==2]
    D=-sum(weights[i]*hazards[i]*Hb[i] for i in level)
    Ddirect=sum(weights[i]*rate*(hazards[j]-hazards[i])**2
                for i in level for j,rate in H[i].items())/2
    assert D==Ddirect>=0

    # Exact class centering, then an independent symmetric-matrix spectrum.
    centered={};unseen=set(level);classes=0
    while unseen:
        start=next(iter(unseen));component={start};todo=[start]
        while todo:
            i=todo.pop()
            for j,rate in H[i].items():
                if j!=i and rate>0 and j not in component:
                    component.add(j);todo.append(j)
        unseen-=component;classes+=1
        mean=sum(weights[i]*hazards[i] for i in component)/sum(weights[i] for i in component)
        centered.update({i:hazards[i]-mean for i in component})
    V=sum(weights[i]*centered[i]**2 for i in level)
    matrix=np.array([[-float(H[i].get(j,F(0)))*np.sqrt(float(weights[i]/weights[j]))
                      for j in level] for i in level])
    assert np.max(np.abs(matrix-matrix.T))<1e-13
    eigenvalues,eigenvectors=eigh(matrix)
    assert min(eigenvalues)>-1e-12
    v=np.array([np.sqrt(float(weights[i]))*float(centered[i]) for i in level])
    amplitudes=eigenvectors.T@v
    spectral=[(float(lam),float(c*c)) for lam,c in zip(eigenvalues,amplitudes)
              if lam>1e-10 and c*c>1e-25]
    assert abs(sum(c for _,c in spectral)-float(V))<1e-10
    assert abs(sum(lam*c for lam,c in spectral)-float(D))<1e-10

    def sparse(rows):
        rr=[];cc=[];data=[]
        for i,row in enumerate(rows):
            for j,value in row.items():
                if value:
                    rr.append(i);cc.append(j);data.append(float(value))
        return csr_matrix((data,(rr,cc)),shape=(len(states),len(states)))
    return {'states':states,'counts':counts,'weights':weights,'H':sparse(H),'B':sparse(B),
            'rows':rows,'pure_coefficients':coefficients,'energy':D,'variance':V,
            'spectrum':spectral,'classes':classes,'empty':ids[(-1,-1,-1)]}


def semigroup_coefficient(model,kappa,t):
    return sum(mf(c)*integral_I(mf(kappa)*mf(lam),t)
               for lam,c in model['spectrum'])/3


def direct_block_coefficients(model,kappa,t):
    # y_r(t) are actual Taylor COEFFICIENT rows (derivatives divided by r!).
    # y'_r=kappa y_r H+y_(r-1) B, implemented on transposed column blocks.
    blocks=[[None]*5 for _ in range(5)]
    for r in range(5):
        blocks[r][r]=float(kappa)*model['H'].T
        if r:
            blocks[r][r-1]=model['B'].T
    matrix=bmat(blocks,format='csr')
    size=len(model['states'])
    initial=np.zeros(5*size);initial[model['empty']]=1
    solution=expm_multiply(float(t)*matrix,initial,
                          traceA=float(t)*float(matrix.diagonal().sum()))
    density_rows=solution.reshape(5,size)
    numbers=density_rows@np.array(model['counts'])
    for r,row in enumerate(density_rows):
        assert abs(sum(row)-(1 if r==0 else 0))<1e-8
    return numbers,density_rows


def check_model(name,edges,W,parameters,exact_axis=False):
    model=construct(edges,W)
    checks=[]
    for kappa,t in parameters:
        actual,rows=direct_block_coefficients(model,kappa,t)
        base=[float(coef*t**r) for r,coef in enumerate(model['pure_coefficients'])]
        for r in range(4):
            assert abs(actual[r]-base[r])<2e-8,(name,r,actual[r],base[r])
        predicted=semigroup_coefficient(model,kappa,t)
        observed=actual[4]-base[4]
        assert abs(observed-float(predicted))<2e-8,(name,kappa,t,observed,predicted)
        item={'kappa':str(kappa),'time':str(t),'epsilon4_difference_block':observed,
              'epsilon4_difference_semigroup':mp.nstr(predicted,35),
              'absolute_discrepancy':abs(observed-float(predicted))}
        if exact_axis:
            exact=(mf(F(9,8))*integral_I(F(8,5)*kappa,t)
                   +mf(F(3,4))*integral_I(F(4,3)*kappa,t))/3
            assert abs(predicted-exact)<mp.mpf('2e-12')
            item['exact_two_mode_formula']=mp.nstr(exact,45)
            if kappa==1 and t==1:
                pure3=np.zeros(len(model['states']))
                for i,value in model['rows'][3].items():
                    pure3[i]=float(value*t**3/F(factorial(3)))
                assert np.max(np.abs(rows[3]-pure3))>1e-4
                item['epsilon3_full_law_changes_but_population_does_not']=True
        checks.append(item)
    kappas=[F(0),F(1,10),F(1,2),F(1),F(2),F(5)]
    values=[semigroup_coefficient(model,k,F(1)) for k in kappas]
    if model['energy']:
        assert all(x<y for x,y in zip(values,values[1:]))
        slopes=[(values[i+1]-values[i])/mf(kappas[i+1]-kappas[i]) for i in range(len(kappas)-1)]
        assert all(x>y for x,y in zip(slopes,slopes[1:]))
        assert all(0<=g<=mf(model['variance'])/12 for g in values)
        assert all(g<=mf(k)*mf(model['energy'])/60+mp.mpf('1e-30')
                   for k,g in zip(kappas,values))
    else:
        assert all(g==0 for g in values)
    return {'name':name,'states':len(model['states']),'two_record_classes':model['classes'],
            'pure_birth_coefficients_per_t_power':list(map(str,model['pure_coefficients'])),
            'unnormalized_energy':str(model['energy']),
            'unnormalized_class_centered_hazard_variance':str(model['variance']),
            'coefficient_checks':checks,
            'kappa_scan_time_one':[{ 'kappa':str(k),'coefficient':mp.nstr(g,35)}
                                    for k,g in zip(kappas,values)]}


def main():
    neutral=axes_W()
    c=[2,-1,-1,0,0,0];q=[0,0,0,1,-1,0]
    general=[[1+F(c[a]*c[b],4)+F(q[a]*q[b],10) for b in range(6)] for a in range(6)]
    path=[(0,1,F(1)),(1,2,F(1))]
    cases=[check_model('path3_axes',path,neutral,
                       [(k,t) for k in [F(1,10),F(1),F(3)] for t in [F(1,2),F(1),F(2)]],True),
           check_model('path3_general_unequal_proposals',[(0,1,F(1)),(1,2,F(2))],general,
                       [(k,t) for k in [F(1,3),F(2)] for t in [F(1,2),F(1)]]),
           check_model('path3_uniform',path,[[F(1)]*6 for _ in range(6)],[(F(1),F(1))]),
           check_model('triangle3_axes',path+[(0,2,F(1))],neutral,[(F(1),F(1))])]
    first=cases[0]
    assert first['unnormalized_energy']=='14/5'
    assert first['unnormalized_class_centered_hazard_variance']=='15/8'
    # Direct quadrature checks the elementary integral used in spectral evaluation.
    for r,t in [(F(1,10),F(1)),(F(8,5),F(2)),(F(4,3),F(1,2))]:
        quadrature=mp.quad(lambda v:(mf(t)-v)**3*(1-mp.exp(-mf(r)*v)),[0,mf(t)])
        assert abs(quadrature-integral_I(r,t))<mp.mpf('1e-60')
    result={'status':'all checks passed','coefficient_convention':'Taylor coefficient in epsilon, not raw epsilon derivative',
            'dependencies':{'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},
            'full_generator_block_checks':sum(len(c['coefficient_checks']) for c in cases),
            'floating_absolute_tolerance':2e-8,'mpmath_decimal_precision':mp.mp.dps,
            'cases':cases,'new_primary_calculations_read':False}
    text=json.dumps(result,indent=2)+'\n'
    (Path(__file__).parent/'RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':
    main()
