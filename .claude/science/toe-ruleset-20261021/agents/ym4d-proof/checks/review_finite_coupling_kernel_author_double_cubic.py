#!/usr/bin/env python3
"""Finite falsification controls for the actual SU(N) normalizer. Not a proof."""
import itertools
import json
import math
import platform
import sys
import time
from pathlib import Path
import numpy as np
from scipy.linalg import expm, logm
from scipy.special import iv, ive
from numpy.polynomial.legendre import leggauss

start=time.monotonic(); rows=[]; details={}
base=Path(__file__).resolve().parent
def check(name,value,passed,kind='ordinary'):
    rows.append(dict(name=name,value=value,passed=bool(passed),kind=kind))
def rel(a,b): return float(abs(a-b)/max(abs(b),1e-300))
def cx(z): return [float(np.real(z)),float(np.imag(z))]
def basis(n):
    out=[]
    for j in range(n):
        for k in range(j+1,n):
            a=np.zeros((n,n),complex);a[j,k]=1;a[k,j]=1
            out.append(1j*a/np.sqrt(2))
            a=np.zeros((n,n),complex);a[j,k]=-1j;a[k,j]=1j
            out.append(1j*a/np.sqrt(2))
    for j in range(1,n):
        a=np.diag([1]*j+[-j]+[0]*(n-j-1))/np.sqrt(j*(j+1))
        out.append(1j*a)
    return np.array(out)
def p0(x): return x-np.trace(x)/len(x)*np.eye(len(x))
def saddle(p,q):
    y=np.zeros_like(p)
    for _ in range(100):
        yn=y+.5*p0(expm(-y)@p-q@expm(y))
        if np.linalg.norm(yn-y)<1e-15: y=yn;break
        y=yn
    w=expm(y);e=np.linalg.solve(w,p);f=q@w
    return w,e,f
def phase(w,p,q): return np.trace(np.linalg.solve(w,p)+q@w)/(2*len(w))
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
def quat(m): return np.array([np.trace(m)/2]+[np.trace(m@s)/(2j) for s in sig])
def coeff(p,q):
    a=quat(p);b=quat(q)
    return np.r_[(a[0]+b[0])/2,(a[1:]-b[1:])/2]
def sph_integral(h,t):
    # Full S3 probability Haar; theta, z=cos(polar angle), azimuth.
    x,w=leggauss(64);theta=np.pi*(x+1)/2
    z,wz=leggauss(36);az=2*np.pi*np.arange(48)/48
    n=np.stack(np.broadcast_arrays(np.sqrt(1-z[:,None]**2)*np.cos(az)[None,:],
                                  np.sqrt(1-z[:,None]**2)*np.sin(az)[None,:],z[:,None]),axis=-1)
    hv=n@h[1:]
    vals=np.exp(t*(np.cos(theta)[:,None,None]*h[0]+np.sin(theta)[:,None,None]*hv))
    return np.sum((w*np.sin(theta)**2)[:,None,None]*(wz/2)[None,:,None]*vals)/48

# A deliberately wider nonunitary/noncommuting algebra check. The exact
# cycle identity and SU2 formula are global; this is not a certified radius.
b2=basis(2)
p=np.eye(2)+.038*b2[0]+(.019+.011j)*b2[1]+(.012-.008j)*np.eye(2)
q=np.eye(2)-.021*b2[2]+(.008+.014j)*b2[0]+(.006+.009j)*np.eye(2)
w,e,f=saddle(p,q);h=coeff(p,q);r=np.sqrt(h@h)
check('SU2 saddle determinant',float(abs(np.linalg.det(w)-1)),abs(np.linalg.det(w)-1)<2e-12)
check('SU2 saddle traceless residual',float(np.linalg.norm(p0(e-f))),np.linalg.norm(p0(e-f))<2e-12)
check('SU2 noncommuting/nonunitary witness',[float(np.linalg.norm(p@q-q@p)),float(np.linalg.norm(w.conj().T@w-np.eye(2)))],np.linalg.norm(p@q-q@p)>1e-5 and np.linalg.norm(w.conj().T@w-np.eye(2))>1e-4)
ints=[]
for t in (3.,12.,40.):
    exact=2*iv(1,t*r)/(t*r)
    direct=sph_integral(h,t)
    translated=sph_integral(coeff(e,f),t)
    err=max(rel(direct,exact),rel(translated,exact))
    check('SU2 full Haar and translated cycle t='+str(t),err,err<2e-8)
    ints.append(dict(t=t,exact=cx(exact),direct=cx(direct),translated=cx(translated)))
details['SU2_complex_pair']=dict(M_plus=[list(map(cx,row)) for row in p],M_minus=[list(map(cx,row)) for row in q],integrals=ints,scope='wider algebra control, not the conservative fixed-neighborhood certificate')
bad=(quat(p)+quat(q))/2;bad_r=np.sqrt(bad@bad)
mutation=rel(2*iv(1,12*bad_r)/(12*bad_r),2*iv(1,12*r)/(12*r))
check('wrong dual-quaternion sign',mutation,mutation>1e-5,'mutation')
for t in (40.,80.,160.):
    zscaled=2*ive(1,t)/t
    er=np.log(zscaled*t**1.5/np.sqrt(2/np.pi))
    c=ive(2,t)/ive(1,t)
    check('SU2 logarithmic remainder t='+str(t),float(t*er),abs(t*er+3/8)<.03)
    check('SU2 finite-u spread coefficient t='+str(t),float(t*t*(1-c-3/(2*t))),abs(t*t*(1-c-3/(2*t))+3/8)<.05)
s=1.1;t=160
zs=2*ive(1,t*s)/(t*s)*t**1.5
wrongA=np.sqrt(2/np.pi)*s**(-3)
mutation=abs(zs/wrongA-1)
check('wrong Gaussian determinant power',float(mutation),mutation>.05,'mutation')

def weyl3(n,t=0,s=1+0j,lam=0j,haar=True):
    th=2*np.pi*np.arange(n)/n
    a,b=np.meshgrid(th,th,indexing='ij');c=-a-b
    ang=np.stack([a,b,c]);v=np.exp(1j*ang)
    vand=np.ones((n,n))
    for j,k in itertools.combinations(range(3),2): vand*=abs(v[j]-v[k])**2
    f=s*(1-np.cos(ang).sum(axis=0)/3)+1j*lam*np.sin(ang).sum(axis=0)/3
    return np.mean(np.exp(-t*f)*(vand/6 if haar else 1))
norm=weyl3(256)
check('SU3 full Weyl Haar normalization',cx(norm),abs(norm-1)<2e-12)
eta3=min(1/64,1/(8*(4+2*16*3**3)))
complexpair=(1+eta3*(.1+.05j),eta3*(.04+.02j))
su3=[];A3=27*np.sqrt(3)/np.pi
for s,lam in ((1+0j,0j),complexpair):
    for t in (40.,80.,160.):
        z1=weyl3(256,t,s,lam);z2=weyl3(384,t,s,lam)
        check('SU3 grids t='+str(t)+' s='+str(s),rel(z1,z2),rel(z1,z2)<2e-8)
        er=np.log(z2*t**4/(A3*s**(-4)))
        if s==1: check('SU3 eight-colour remainder t='+str(t),cx(t*er),abs(t*er+1)<.12)
        su3.append(dict(t=t,s=cx(s),lam=cx(lam),Z_centered=cx(z2),tE=cx(t*er)))
details['SU3_full_Haar']=dict(A_identity=A3,samples=su3)
mut=abs(weyl3(256,80,haar=False)*80**4/A3-1)
check('discard SU3 Haar Vandermonde',float(mut),mut>.1,'mutation')

b3=basis(3);ident=np.eye(3)
y=eta3*(.08*b3[0]+(.05+.03j)*b3[3])
ss=ident+eta3*(.07*b3[1]+(.05+.02j)*b3[6])
lam=eta3*(.03+.02j);ww=expm(y)
pp=ww@(ss+lam*ident);qq=(ss-lam*ident)@np.linalg.inv(ww)
sol,e,f=saddle(pp,qq)
domain=max(np.linalg.norm(pp-ident),np.linalg.norm(qq-ident))
check('SU3 constructed pair inside proved domain',float(domain/eta3),domain<eta3)
check('SU3 noncommuting SL saddle',float(np.linalg.norm(sol-ww)),np.linalg.norm(sol-ww)<2e-12)
H=np.array([[-np.trace(ss@(a@b+b@a))/6 for b in b3] for a in b3])
def fval(x):
    xx=np.einsum('a,aij->ij',x,b3);uu=expm(xx);ui=expm(-xx)
    return np.trace(ss@(ident-(uu+ui)/2))/3-lam*np.trace(ui-uu)/6
hf=2e-4;eye=np.eye(8);Hfd=np.zeros((8,8),complex)
for j in range(8):
    Hfd[j,j]=(fval(hf*eye[j])+fval(-hf*eye[j])-2*fval(np.zeros(8)))/hf**2
    for k in range(j):
        Hfd[j,k]=Hfd[k,j]=(fval(hf*(eye[j]+eye[k]))-fval(hf*(eye[j]-eye[k]))-fval(hf*(-eye[j]+eye[k]))+fval(-hf*(eye[j]+eye[k])))/(4*hf**2)
check('SU3 full eight-colour Hessian',float(np.linalg.norm(H-Hfd)),np.linalg.norm(H-Hfd)<3e-6)
X=.2j*np.diag([1,1,-2])/np.sqrt(6);ll=.04j
f3=ll*np.trace(X@X@X)/9
odd=ll*np.trace(expm(X)-expm(-X))/6
plus=lambda xx: np.trace(ident-(expm(xx)+expm(-xx))/2)/3-ll*np.trace(expm(-xx)-expm(xx))/6
check('SU3 genuine odd cubic and parity',[cx(f3),float(abs(f3+ll*np.trace((-X)@(-X)@(-X))/18)),float(abs((plus(X)-plus(-X))/2-odd))],abs(f3)>1e-7 and abs(f3+ll*np.trace((-X)@(-X)@(-X))/18)<2e-12 and abs((plus(X)-plus(-X))/2-odd)<2e-12)
polar=np.exp(1j*np.arctan(.04))*ident
mutation=abs(np.linalg.det(polar)-1)
check('U(N) polar violates SU3 constraint',float(mutation),mutation>1e-3,'mutation')

# Actual centered 4D L3 paired S4-prime contour family.
L=3;mu=0;root=(0,0,0,0);end=(3,0,0,0);words=[]
def axial(root,offset,perm):
    at=list(root);word=[]
    for nu in perm:
        for _ in range(abs(offset[nu])):
            if offset[nu]>0: word.append((tuple(at),nu,1));at[nu]+=1
            else: at[nu]-=1;word.append((tuple(at),nu,-1))
    return word,at
for off in itertools.product((-1,0,1),repeat=4):
    for perm in itertools.permutations(range(4)):
        left,at=axial(root,off,perm);straight=[]
        for _ in range(L):straight.append((tuple(at),mu,1));at[mu]+=1
        right,_=axial(end,off,perm)
        words.append(left+straight+[(p,nu,-sg) for p,nu,sg in right[::-1]])
keys=sorted(set((p,nu) for w in words for p,nu,sg in w))
Gs=[expm(.31*b2[0]),expm(.27*b2[1]),expm(.22*b2[2]),expm(.19*(b2[0]+b2[2]))]
rng=np.random.default_rng(104729);dirs={}
for key in keys:
    z=rng.normal(size=3)+.6j*rng.normal(size=3);z/=np.linalg.norm(z)
    dirs[key]=np.einsum('a,aij->ij',z,b2)
def means(amp):
    links={k:expm(amp*dirs[k])@(Gs[k[1]] if k[0][k[1]]%L==1 else np.eye(2)) for k in keys}
    inverses={k:np.linalg.inv(v) for k,v in links.items()}
    mats=[]
    for word in words:
        v=np.eye(2,dtype=complex)
        for p,nu,sg in word:v=v@(links[(p,nu)] if sg==1 else inverses[(p,nu)])
        mats.append(v)
    return np.mean(mats,axis=0),np.mean([np.linalg.inv(v) for v in mats],axis=0),mats
m,mi,paths=means(0)
check('actual S4 count and length',[len(words),max(map(len,words)),len(keys)],len(words)==1944 and max(map(len,words))<=11)
flat=max(np.linalg.norm(p-Gs[0]) for p in paths)
check('arbitrary-holonomy brick lift exact contours',float(flat),flat<2e-12)
eta2=min(1/64,1/(8*(4+2*16*2**3)))
amp=np.log(1+eta2/(4*np.sqrt(2)))/12
m,mi,_=means(amp)
domain=max(np.linalg.norm(np.linalg.solve(Gs[0],m)-np.eye(2)),np.linalg.norm(mi@Gs[0]-np.eye(2)))
check('actual complex S4 in fixed matrix domain',float(domain/eta2),domain<eta2/2)
m,mi,_=means(.035)
errors=[float(np.linalg.norm(mi-np.linalg.inv(m))),float(np.linalg.norm(mi-m.conj().T))]
check('inverse mean and conjugate are both wrong',errors,min(errors)>1e-6)
mutation=np.linalg.norm(4*Gs[0]-Gs[0])
check('wrong S4 divisor 6L^4',float(mutation),mutation>.5,'mutation')
details['S4']=dict(count=len(words),distinct_reader_links=len(keys),inside_link_radius=amp,inside_parameter_ratio=domain/eta2,wider_probe_amplitude=.035,wider_probe_errors=errors)

result=dict(criteria='finite_coupling_kernel_criteria.md',program=Path(__file__).name,
            runtime=dict(python=sys.version,numpy=np.__version__,platform=platform.platform(),elapsed=time.monotonic()-start),
            passed=sum(r['passed'] for r in rows),total=len(rows),checks=rows,details=details)
(base/'review_finite_coupling_kernel_author_double_cubic_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(0 if result['passed']==result['total'] else 1)
