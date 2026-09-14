"""Finite matrix challenge of Wilson evenness, gauge nulls and log curvature."""
from itertools import product,combinations
from pathlib import Path
from fractions import Fraction
import json,math
import numpy as np

sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);I=np.eye(2)
gamma=[np.kron(sx,s) for s in [sx,sy,sz]]+[np.kron(sy,I)]
B=gamma[0]@gamma[2];G5=gamma[0]@gamma[1]@gamma[2]@gamma[3]
for i in range(4):
    assert np.linalg.norm(B@gamma[i].T@B.conj().T+gamma[i])<1e-12
    for j in range(4):assert np.linalg.norm(gamma[i]@gamma[j]+gamma[j]@gamma[i]-2*(i==j)*np.eye(4))<1e-12


def majorant(d,m,q,nmax=100):
    q=Fraction(q);terms=[Fraction(m,2)*n**3*(2*n+1)**d*q**n for n in range(4,nmax+1)]
    nextterm=Fraction(m,2)*(nmax+1)**3*(2*nmax+3)**d*q**(nmax+1)
    ratio=q*Fraction(nmax+2,nmax+1)**(d+3)
    assert ratio<1
    partial=sum(terms);remainder=nextterm/(1-ratio)
    if d==4 and m==4 and q==Fraction(1,20):
        assert Fraction(1,100)*(partial+remainder)<Fraction('0.066164')
        assert remainder<Fraction('1.46e-116')
    return float(partial),float(remainder)

rng=np.random.default_rng(621017);results=[]
for d in [2,3,4]:
    sites=list(product(range(2),repeat=d));site={x:i for i,x in enumerate(sites)};links=[]
    for x in sites:
        for mu in range(d):
            if x[mu]==0:
                y=list(x);y[mu]=1;links.append((x,tuple(y),mu))
    ix={(x,mu):i for i,(x,y,mu) in enumerate(links)}
    curl=[]
    for x in sites:
        for mu,nu in combinations(range(d),2):
            if x[mu] or x[nu]:continue
            row=np.zeros(len(links));xm=list(x);xm[mu]=1;xn=list(x);xn[nu]=1
            row[ix[x,mu]]+=1;row[ix[tuple(xm),nu]]+=1
            row[ix[tuple(xn),mu]]-=1;row[ix[x,nu]]-=1;curl.append(row)
    C=np.array(curl);M=20.;e=.7;t0=1.;q=Fraction(2*d,20);cb,tail=majorant(d,4,q)
    phases=rng.normal(size=len(links))*2.1;direction=rng.normal(size=len(links));chi=rng.normal(size=len(sites))
    grad=np.array([chi[site[y]]-chi[site[x]] for x,y,mu in links])
    assert np.linalg.norm(C@grad)<1e-12
    def matrices(A,a):
        D=M*np.eye(4*len(sites),dtype=complex);first=np.zeros_like(D);second=np.zeros_like(D)
        for k,(x,y,mu) in enumerate(links):
            i,j=site[x],site[y];f=-t0*(np.eye(4)-gamma[mu])/2;back=-t0*(np.eye(4)+gamma[mu])/2
            for src,dst,T,sg in [(i,j,f,1),(j,i,back,-1)]:
                block=T*np.exp(1j*sg*e*A[k]);s1=slice(4*src,4*(src+1));s2=slice(4*dst,4*(dst+1))
                D[s1,s2]+=block;first[s1,s2]+=1j*sg*e*a[k]*block;second[s1,s2]-=e*e*a[k]*a[k]*block
        return D,first,second
    D,D1,D2=matrices(phases,direction);inv=np.linalg.inv(D)
    curvature=2*np.trace(inv@D2-inv@D1@inv@D1).real
    fullB=np.kron(np.eye(len(sites)),B);fullG5=np.kron(np.eye(len(sites)),G5)
    reverse=matrices(-phases,direction)[0]
    assert np.linalg.norm(reverse-fullB@D.T@fullB.conj().T)<1e-12
    assert np.linalg.norm(D.conj().T-fullG5@D@fullG5)<1e-12
    def logweight(A):return 2*np.linalg.slogdet(matrices(A,np.zeros(len(links)))[0]/M)[1]
    logw=logweight(phases)
    assert abs(logweight(-phases)-logw)<1e-12
    assert abs(logweight(phases+grad)-logw)<1e-12
    _,g1,g2=matrices(phases,grad);gaugecurvature=2*np.trace(inv@g2-inv@g1@inv@g1).real
    assert abs(gaugecurvature)<1e-12
    finite=[]
    for h in [.08,.04,.02]:
        fd=(logweight(phases+h*direction)-2*logw+logweight(phases-h*direction))/h**2
        finite.append({'step':h,'finite_difference':fd,'error':abs(fd-curvature)})
    assert finite[-1]['error']<max(1e-8,abs(curvature)*.02)
    assert finite[-1]['error']<finite[0]['error']*.2+1e-11
    bound=e*e*(cb+tail)*np.linalg.norm(C@direction)**2
    assert abs(curvature)<=bound+1e-12
    results.append({'d':d,'sites':len(sites),'links':len(links),'matrix_dimension':len(D),'q':float(q),'curvature':curvature,'curl_bound':bound,'majorant':cb,'majorant_tail_bound':tail,'gauge_null_curvature':gaugecurvature,'finite_differences':finite})
    print(results[-1],flush=True)
low,tail=majorant(4,4,Fraction(1,20));assert .01*(low+tail)<1
print('d4 m4 q=.05 e=.1 beta=1 alpha_upper',.01*(low+tail),'tail',tail)
Path(__file__).with_name('BLOCK2_WILSON_CURVATURE_CHECK.json').write_text(json.dumps({'matrices':results,'strict_point':{'dimension':4,'m':4,'q':.05,'e':.1,'beta':1,'alpha_upper':.01*(low+tail),'series_tail_upper':tail}},indent=2)+'\n')
