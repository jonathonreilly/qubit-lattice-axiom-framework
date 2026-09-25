"""Author spectral contraction of the exact selected-power polynomial.

The finite sums and Hessian factorization are controls of the new author
calculation, not an independent reconstruction or full evolution.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from itertools import product
import hashlib,json,time
import numpy as np


def canon_word(raw,L):
    out=defaultdict(int)
    for xa,xb,n in raw:
        a=tuple(x if x<L//2 else x-L for x in xa);b=tuple(x if x<L//2 else x-L for x in xb)
        step=tuple(y-x for x,y in zip(a,b));assert sum(abs(s)for s in step)==1
        mu=next(i for i,x in enumerate(step)if x);s=step[mu]
        out[a if s==1 else b,mu]+=s*n
    return tuple(sorted((e,n)for e,n in out.items()if n))

def ft(w,k):
    a=np.zeros((len(k),3),dtype=complex)
    for (x,mu),n in w:a[:,mu]+=float(n)*np.exp(1j*(k@np.array(x)))
    return a

def run():
    p=Path(__file__).with_name('POWER_POLYNOMIAL_RESULTS.json');data=json.loads(p.read_text())
    words=[]
    for row in data['rows']:
        words.append({canon_word(x['word'],row['L']):Fraction(x['coefficient']) for x in row['words']})
    assert words[0]==words[1];poly=words[0]
    c=(((0,0,0),0),1),(((1,0,0),1),1),(((0,1,0),0),-1),(((0,0,0),1),-1)
    cd=dict(c);H=defaultdict(Fraction)
    for w,a in poly.items():
        for e,n in w:
            for f,m in w:H[e,f]-=a*n*m
    H={ef:a for ef,a in H.items()if a};edges=sorted(set(e for e,_ in H)|set(f for _,f in H)|set(cd))
    hc={e:sum(H.get((e,f),0)*cf for f,cf in c)for e in edges}
    chc=sum(cd.get(e,0)*hc[e] for e in edges)
    t={e:hc[e]/4-cd.get(e,0)*chc/32 for e in edges};t={e:n for e,n in t.items() if n}
    residual=[]
    for e in edges:
        for f in edges:
            v=H.get((e,f),0)-cd.get(e,0)*t.get(f,0)-t.get(e,0)*cd.get(f,0)
            if v:residual.append((e,f,str(v)))
    assert not residual
    assert all(x.denominator==1 for x in t.values())
    div=defaultdict(Fraction)
    for (x,mu),n in t.items():
        y=list(x);y[mu]+=1;div[x]+=n;div[tuple(y)]-=n
    assert all(n==0 for n in div.values())
    rows=[]
    for L in (16,32,64):
        axis=2*np.pi*np.arange(L)/L;k=np.array(list(product(axis,repeat=3)))
        D=4*np.sin(k/2)**2;om=np.sqrt(D.sum(axis=1));keep=om>0;k=k[keep];om=om[keep];V=L**3
        C=ft(c,k);T=ft(tuple(t.items()),k);weights=np.sum(C*np.conj(T),axis=1)/(2*V*om)
        covariance=np.sum(weights);assert abs(covariance.imag)<1e-10
        vp=float(np.sum(abs(C)**2/om[:,None])/(2*V))
        local=[]
        for eps in (.2,.4,.7,1.,2.,3.5):
            band=om<=eps;vlow=float(np.sum(abs(C[band])**2/om[band,None])/(2*V))
            if vlow==0:local.append({'epsilon':eps,'empty':True});continue
            chi_p=np.sqrt(vlow);chi_t=np.sum(weights[band])/chi_p;assert abs(chi_t.imag)<1e-10
            excess=2*float(np.real(chi_p*np.conj(chi_t)))
            local.append({'epsilon':eps,'empty':False,'reference_mu':float(np.sum(abs(C[band])**2)/(2*V*vlow)),
              'vacuum_magnetic_power_units':float(covariance.real),'one_minus_vacuum_power_units':excess,
              'one_magnetic_power_units':float(covariance.real)+excess})
        rows.append({'L':L,'v_p':vp,'vacuum_covariance_cp_t':float(covariance.real),'rows':local})
    return {'scope':__doc__,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'polynomials_identical_between_signs':True,'hessian_nonzero_entries':len(H),'hessian_cp_contraction':str(chc),
      'hessian_exact_factorization':'H=c_p t^T+t c_p^T; Cmag quadratic term=(c_p A)(t A)',
      't_vector':[{'positive_edge_origin':e[0],'axis':e[1],'coefficient':str(n)}for e,n in sorted(t.items())],
      'units':'All power rows are in kappa/(4 tau); electric contribution tends to zero, proof pending.',
      'rows':rows}

if __name__=='__main__':
    tic=time.perf_counter();d=run();d['elapsed_seconds']=time.perf_counter()-tic;print(json.dumps(d,indent=2))
