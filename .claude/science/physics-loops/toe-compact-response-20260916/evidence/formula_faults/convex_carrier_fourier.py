#!/usr/bin/env python3
"""Check the explicit extension and the actual interpolated time carrier.

This checks algebra, derivative matching, Fourier normalization and selected
finite-grid bridge Hessians. It does not certify a compact-measure comparison.
"""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
from scipy.integrate import quad
from bridge_cubic_check import two_face_quantities


def chi(x,alpha):
    y=abs(x);sgn=1 if x>=0 else -1
    if y<=alpha:return (x,1.,0.)
    if y>=2*alpha:return (sgn*1.5*alpha,0.,0.)
    u=(y-alpha)/alpha
    return (sgn*alpha*(1+u-u**3+u**4/2),1-3*u*u+2*u**3,
            sgn*(-6*u+6*u*u)/alpha)


def extension(x,alpha):
    y=abs(x)
    return quad(lambda s:(y-s)*math.cos(chi(s,alpha)[0]),0,y,
                points=[a for a in (alpha,2*alpha) if a<y],epsabs=2e-12)[0]


def extension_checks():
    rows=[]
    for alpha in (.05,.2,.6):
        for x in np.linspace(-3*alpha,3*alpha,121):
            c,d,dd=chi(x,alpha)
            assert abs(c)<=1.5*alpha+1e-15 and -1e-15<=d<=1+1e-15
            assert math.cos(1.5*alpha)-1e-14<=math.cos(c)<=1+1e-14
            assert abs(math.sin(c)*d)<=math.sin(1.5*alpha)+1e-14
            step=alpha*1e-4
            cp,dp,_=chi(x+step,alpha);cm,dm,_=chi(x-step,alpha)
            assert abs((cp-cm)/(2*step)-d)<2e-7
            assert abs((dp-dm)/(2*step)-dd)<4e-3
            if abs(x)<=alpha+1e-14:
                assert abs(extension(x,alpha)-(1-math.cos(x)))<2e-12
        rows.append(dict(alpha=alpha,minimum_curvature=math.cos(1.5*alpha),
                         cubic_upper=math.sin(1.5*alpha),sample_count=121))
    return rows


def carrier_checks():
    rows=[]
    rng=np.random.default_rng(81716)
    for N in (3,4,7,12):
        for T in (.08,.25):
            a=rng.normal(size=(N,5));nxt=np.roll(a,-1,axis=0)
            # Integrate affine interpolants independently by Gauss-Legendre.
            nodes,w=np.polynomial.legendre.leggauss(3)
            integral=0.
            for node,weight in zip((nodes+1)/2,w/2):
                integral+=T*weight*np.sum(((1-node)*a+node*nxt)**2)/2
            algebra=T*np.sum(a*a+a*nxt+nxt*nxt)/6
            fourier=np.fft.fft(a,axis=0,norm='ortho')
            omega=2*np.pi*np.arange(N)/N
            b=(1+np.cos(omega))/3
            spectral=T*np.sum(b[:,None]*abs(fourier)**2)/2
            assert abs(integral-algebra)<1e-12 and abs(spectral-algebra)<1e-12
            kinetic=np.sum((nxt-a)**2)/(2*T)
            kinetic_spectral=np.sum((4*np.sin(omega/2)**2)[:,None]*abs(fourier)**2)/(2*T)
            assert abs(kinetic-kinetic_spectral)<2e-12
            # Wrong one-slice magnetic carrier must actually be distinguishable.
            wrong=T*np.sum(a*a)/2
            assert abs(wrong-algebra)>1e-3
            rows.append(dict(slices=N,T=T,integrated=integral,algebra=algebra,
                             spectral=float(spectral),wrong_one_slice=wrong,
                             kinetic=kinetic,kinetic_spectral=float(kinetic_spectral)))
    return rows


def bridge_hessian_checks():
    rows=[]
    g,T=.45,.2
    end=np.array([[.6,-.25],[.9,.4]])
    h=np.array([[1.,.2],[-.1,.4]]);k=np.array([[.3,-.5],[.7,.1]])
    l=np.array([[.2,.6],[-.2,.3]])
    r=2*T*T;d0=r+g*g*T/(2*(1-r));d2=d0+r/(1-r)
    for shift in (0.,1.,3.):
        f=end+shift
        result=two_face_quantities(g,T,f,h,k,l,16)
        blend=lambda a:np.array([(2*a[0]+a[1])/3,(a[0]+2*a[1])/3])
        ff,hh,kk=map(blend,(f,h,k))
        p2=T/3*np.sum(np.cos(ff)*hh*kk)
        qh=T/3*np.sum(hh*hh);qk=T/3*np.sum(kk*kk)
        error=result['hessian']-p2
        bound=d2*math.sqrt(qh*qk)
        assert abs(error)<=bound+1e-12
        rows.append(dict(shift=shift,hessian=result['hessian'],straight=p2,
                         correction=error,correction_bound=bound))
    constants=[]
    for alpha,T,g in ((.1,.1,.003),(.2,.1,.003),(.1,.05,.01)):
        r=2*T*T;d0=r+g*g*T/(2*(1-r));d2=d0+r/(1-r)
        d3=d0+(1-r)**(-3)-1
        contrast=1-math.cos(1.5*alpha)+d2
        cubic=g*(math.sin(1.5*alpha)+d3)
        assert contrast<1
        constants.append(dict(alpha=alpha,T=T,g=g,relative_contrast=contrast,
                              cubic_chain_coefficient=cubic))
    return dict(hessian=rows,examples=constants)


def main():
    start=time.monotonic()
    files=[Path(__file__),Path(__file__).with_name('bridge_cubic_check.py')]
    out=dict(status='PERSONAL_CHECKS_COMPLETED',scope=__doc__,
             input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             extension=extension_checks(),carrier=carrier_checks(),
             bridge=bridge_hessian_checks())
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
