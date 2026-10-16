"""Bounded synthetic controls of the explicit context-transport candidate."""
from pathlib import Path
from itertools import product
import hashlib
import json
import math
import numpy as np
import mpmath as mp
import sympy as s

P=Path(__file__).resolve().parent
mp.mp.dps=55
checks=[]
def check(name,ok,**kw):
    assert ok,name
    checks.append({'name':name,'passed':True,**kw})

I=np.eye(2,dtype=complex)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]).astype(complex)]
def S(a):return sum((a[i]*sigma[i] for i in range(3)),np.zeros((2,2),complex))
def U(a,b):return (I+S(b)@S(a))/math.sqrt(2*(1+np.dot(a,b)))
def T(a,b,n,lam,k):
    angle=lam*np.dot(n,a-b)+k*np.dot(n,np.cross(a,b))
    return U(a,b)@(math.cos(angle/2)*I-1j*math.sin(angle/2)*S(a))
def loop(axes,n,lam,k):
    out=I.copy()
    for a,b in zip(axes[:-1],axes[1:]):out=T(a,b,n,lam,k)@out
    return out
def latitude(beta,N):
    phi=np.arange(N+1)*2*np.pi/N
    return np.column_stack([np.sin(beta)*np.cos(phi),np.sin(beta)*np.sin(phi),np.full(N+1,np.cos(beta))])

max_phase_error=0.;max_twist_error=0.
for beta,N in product([0.,.4,1.1,np.pi/2,2.4,np.pi],[3,4,8,64]):
    axes=latitude(beta,N);base=loop(axes,np.array([0.,0.,1.]),0.,0.)
    start=np.array([math.cos(beta/2),math.sin(beta/2)],complex)
    phase=np.vdot(start,base@start)
    gamma=-np.pi+N*math.atan(math.cos(beta)*math.tan(np.pi/N))
    max_phase_error=max(max_phase_error,abs(phase-np.exp(1j*gamma)))
    W=np.cross(axes[:-1],axes[1:]).sum(axis=0)
    expected=np.array([0,0,N*math.sin(beta)**2*math.sin(2*np.pi/N)])
    assert np.max(np.abs(W-expected))<3e-13
    n=np.array([2.,-1.,2.])/3;k=.73;lam=1.4
    actual=loop(axes,n,lam,k)
    th=k*np.dot(n,W)
    pred=base@(math.cos(th/2)*I-1j*math.sin(th/2)*S(axes[0]))
    max_twist_error=max(max_twist_error,float(np.max(np.abs(actual-pred))))
check('latitude loop phase and transported twists',max_phase_error<2e-12 and max_twist_error<2e-12,max_phase_error=max_phase_error,max_twist_error=max_twist_error)

def sinc(x):return mp.sin(x)/x if x else mp.mpf(1)
q=mp.mpf('1.3')
quadrature=mp.quad(lambda x:mp.cos(q*x),[-1,1])/2
check('uniform context characteristic function',abs(quadrature-sinc(q))<mp.mpf('1e-48'))
check('negative characteristic factor cannot be positive attenuation',sinc(mp.mpf(4))<0)
beta=mp.mpf('1.1');k=mp.mpf('0.8');asymptotic=[]
for N in [16,64,256,1024,4096]:
    delta=2*mp.pi/N;c=mp.cos(beta)**2+mp.sin(beta)**2*mp.cos(delta)
    cross=mp.sqrt(1-c*c);logc=N*mp.log(sinc(k*cross/2))
    leading=-k*k*mp.pi**2*mp.sin(beta)**2/(6*N)
    scaled=N*mp.log(sinc(k*mp.sqrt(N)*cross/2))
    limit=-k*k*mp.pi**2*mp.sin(beta)**2/6
    asymptotic.append({'N':N,'independent':float(mp.exp(logc)),'common':float(sinc(k*N*mp.sin(beta)**2*mp.sin(delta)/2)),'N3_remainder':float(N**3*(logc-leading)),'scaled_log_error':float(scaled-limit)})
check('fixed-resolution and scaled-limit controls',all(abs(r['N3_remainder'])<10 for r in asymptotic) and abs(asymptotic[-1]['scaled_log_error'])<1e-4,rows=asymptotic,scope='Finite controls; asymptotic justification is in the note.')

def phi(vs,k):
    value=np.linalg.norm(np.sum(vs,axis=0))*k/2
    return float(np.sinc(value/np.pi))
def renewal(vs,rho,k):
    N=len(vs);prefix=np.vstack([np.zeros(3),np.cumsum(vs,axis=0)]);F=np.ones(N+1)
    for j in range(1,N+1):
        v=prefix[j]-prefix[:j]
        ph=np.sinc(k*np.linalg.norm(v,axis=1)/(2*np.pi))
        weights=(1-rho)*rho**np.arange(j-1,-1,-1);weights[0]=rho**(j-1)
        F[j]=np.sum(weights*F[:j]*ph)
    return F[-1]
def enumerate_renewal(vs,rho,k):
    ans=0.;N=len(vs)
    for cuts in product([0,1],repeat=N-1):
        weight=rho**(N-1-sum(cuts))*(1-rho)**sum(cuts);start=0;value=1.
        for j in range(1,N+1):
            if j==N or cuts[j-1]:value*=phi(vs[start:j],k);start=j
        ans+=weight*value
    return ans
axes=latitude(1.2,8);vs=np.cross(axes[:-1],axes[1:])
for rho in [0.,.2,.7,1.]:assert abs(renewal(vs,rho,.9)-enumerate_renewal(vs,rho,.9))<1e-14
check('renewal recursion versus complete pattern enumeration',True,patterns_per_case=128,cases=4)
check('renewal endpoint limits',abs(renewal(vs,0.,.9)-np.prod([phi([v],.9) for v in vs]))<1e-14 and abs(renewal(vs,1.,.9)-phi(vs,.9))<1e-14)

# The second moment is checked by enumerating reset patterns and conditioning
# on each independent uniform segment, rather than using the recursion.
rho=.63;k=.82;enum_var=0.
for cuts in product([0,1],repeat=len(vs)-1):
    weight=rho**(len(vs)-1-sum(cuts))*(1-rho)**sum(cuts);start=0;variance=0.
    for j in range(1,len(vs)+1):
        if j==len(vs) or cuts[j-1]:
            seg=np.sum(vs[start:j],axis=0);variance+=k*k*np.dot(seg,seg)/12;start=j
    enum_var+=weight*variance
cov_var=k*k*sum(rho**abs(i-j)*np.dot(a,b) for i,a in enumerate(vs) for j,b in enumerate(vs))/12
check('renewal covariance and phase variance',abs(enum_var-cov_var)<1e-14)

moment_rows=[]
for q,alpha in product([mp.mpf('.3'),mp.mpf('1.3'),mp.mpf('3.5')],[mp.mpf('.4'),mp.pi/2]):
    p=lambda x:(1+mp.cos(alpha-q*x))/2
    mean=mp.quad(p,[-1,1])/2;var=mp.quad(lambda x:(p(x)-mean)**2,[-1,1])/2
    pred=(mp.mpf(1)/2*(1+sinc(2*q)*mp.cos(2*alpha))-sinc(q)**2*mp.cos(alpha)**2)/4
    assert abs(mean-(1+sinc(q)*mp.cos(alpha))/2)<mp.mpf('1e-45') and abs(var-pred)<mp.mpf('1e-45')
    L=20
    total=mp.quad(lambda x:L*p(x)*(1-p(x))+(L*p(x)-L*mean)**2,[-1,1])/2
    assert abs(total-L*mean*(1-mean)-L*(L-1)*var)<mp.mpf('1e-43')
    moment_rows.append({'q':float(q),'alpha':float(alpha),'mean':float(mean),'context_variance':float(var),'count_variance':float(total)})
check('slow-context record moments by independent quadrature',True,rows=moment_rows)

# The Poisson continuum coupling bound is analytic. The following deterministic
# context path verifies its integral and the non-expectation bound using the
# actual intervals containing changes; it does not simulate a Poisson proof.
def integrated_cross(beta,a,b):
    sb,cb=math.sin(beta),math.cos(beta)
    return np.array([-cb*sb*(math.sin(b)-math.sin(a)),cb*sb*(math.cos(b)-math.cos(a)),sb*sb*(b-a)])
breaks=[0.,.17,1.4,4.8,2*np.pi];marks=np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.],[-1.,0.,0.]])
beta=1.1;k=.9;continuous=-k/2*sum(np.dot(n,integrated_cross(beta,a,b)) for n,a,b in zip(marks,breaks[:-1],breaks[1:]))
couplings=[]
for N in [16,64,256,1024]:
    h=2*np.pi/N;axes=latitude(beta,N);vsn=np.cross(axes[:-1],axes[1:])
    ns=marks[np.searchsorted(breaks,np.arange(N)*h,side='right')-1]
    discrete=-k/2*np.sum(ns*vsn)
    M=abs(math.sin(beta));pathbound=abs(k)/2*(2*np.pi*h*M*M/2+2*M*h*(len(breaks)-2))
    assert abs(discrete-continuous)<=pathbound
    couplings.append({'N':N,'phase_error':abs(discrete-continuous),'deterministic_bound':pathbound})
check('piecewise context continuum integral and coupling controls',True,rows=couplings)

refinements=[]
for ell in [.3,1.,5.]:
    row={'ell':ell,'values':[]}
    for N in [32,64,128,256,512]:
        axes=latitude(1.1,N);vecs=np.cross(axes[:-1],axes[1:]);h=2*np.pi/N
        value=renewal(vecs,math.exp(-h/ell),.9)
        bound=.9/2*(2*np.pi)*h*(math.sin(1.1)**2/2+math.sin(1.1)/ell)
        row['values'].append({'N':N,'C':value,'continuum_error_bound':bound})
    for aa,bb in zip(row['values'][:-1],row['values'][1:]):assert abs(aa['C']-bb['C'])<=aa['continuum_error_bound']+bb['continuum_error_bound']
    refinements.append(row)
check('fixed correlation length refinement controls',True,rows=refinements,scope='Bounds refer to the declared continuum model, not an observation fit.')

# Explicit degenerate extension, separately supplied from the interior map.
def detector(u,p):
    if p==1:return 0,u
    if p==0:return 1,u
    return (0,u/p) if u<p else (1,(u-p)/(1-p))
for p,port in [(0.,1),(1.,0)]:
    for u in [0.,.2,.5,.9]:assert detector(u,p)==(port,u)
check('degenerate detector endpoint extension',True)

result={'source_sha256':hashlib.sha256((P/'NETWORK_EVOLUTION_BLOCK05_v2.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'summary':{'passed':len(checks),'failed':0},'empirical_test':False,'scope':'Conditional transport and specified context dynamics; correlation length and physical identification are not derived.'}
text=json.dumps(result,indent=2)+'\n';(P/'CONTEXT_LOOP_CONTROLS_v2.json').write_text(text);print(text,end='')
