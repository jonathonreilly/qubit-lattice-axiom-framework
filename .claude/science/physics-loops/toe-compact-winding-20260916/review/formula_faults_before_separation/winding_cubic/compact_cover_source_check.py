#!/usr/bin/env python3
"""Compact circle image/Fourier derivatives and finite rotor Ward identities.

Fourier cutoffs are finite challenges. They neither prove a thermodynamic phase
nor identify a background-source partition ratio with an observable MGF.
"""
AUDIT_TIMEOUT_SEC=120
from itertools import product
from pathlib import Path
import hashlib,json,math,time
import mpmath as mp
import numpy as np
from scipy.linalg import eigh


def circle_images(g,T,z,cut):
    d=[z+2*mp.pi*n for n in range(-cut,cut+1)]
    weights=[mp.exp(-x*x/(2*g*g*T)) for x in d];Z=mp.fsum(weights)
    w=[x/Z for x in weights];mean=mp.fsum(a*b for a,b in zip(w,d))
    var=mp.fsum(a*(b-mean)**2 for a,b in zip(w,d))
    third=mp.fsum(a*(b-mean)**3 for a,b in zip(w,d))
    return dict(kernel=mp.sqrt(2*mp.pi/(g*g*T))*Z,first=mean/T,
                second=1/T-var/(g*g*T*T),third=-third/(g**4*T**3))


def circle_fourier(g,T,z,cut):
    n=list(range(1,cut+1));a=[mp.exp(-g*g*T*k*k/2) for k in n]
    q=1+2*mp.fsum(v*mp.cos(k*z) for k,v in zip(n,a))
    q1=-2*mp.fsum(k*v*mp.sin(k*z) for k,v in zip(n,a))
    q2=-2*mp.fsum(k*k*v*mp.cos(k*z) for k,v in zip(n,a))
    q3=2*mp.fsum(k**3*v*mp.sin(k*z) for k,v in zip(n,a))
    assert q>0
    return dict(kernel=q,first=-g*g*q1/q,second=-g*g*(q2/q-(q1/q)**2),
                third=-g*g*(q3/q-3*q1*q2/q**2+2*(q1/q)**3))


def circle_checks():
    mp.mp.dps=120;rows=[]
    for g,T in ((mp.mpf('.7'),mp.mpf('.2')),(mp.mpf('1'),mp.mpf('.5'))):
        points=[mp.mpf('.2'),mp.pi,mp.pi-g*g*T/(2*mp.pi),mp.pi+g*g*T/(2*mp.pi)]
        for z in points:
            a=circle_images(g,T,z,8);b=circle_images(g,T,z,10)
            c=circle_fourier(g,T,z,120);d=circle_fourier(g,T,z,160)
            errors={}
            for key in a:
                denominator=max(abs(b[key]),mp.mpf('1e-30'))
                assert abs(a[key]-b[key])/denominator<mp.mpf('1e-70')
                assert abs(c[key]-d[key])/denominator<mp.mpf('1e-70')
                errors[key]=abs(b[key]-d[key])/denominator
                assert errors[key]<mp.mpf('1e-60')
            if z==mp.pi:assert b['second']<0 and abs(b['third'])<mp.mpf('1e-60')
            if z in points[2:]:assert abs(b['third'])>1
            rows.append(dict(g=str(g),T=str(T),z=str(z),image={k:str(v) for k,v in b.items()},
                             relative_errors={k:str(v) for k,v in errors.items()},
                             per_lift_hessian=str(1/T),per_lift_cubic='0'))
    # Free one-link trace: electric eigenbasis versus spatial winding images.
    traces=[]
    for g,beta in ((mp.mpf('.4'),mp.mpf('2')),(mp.mpf('.9'),mp.mpf('.3'))):
        spectral=mp.fsum(mp.exp(-beta*g*g*k*k/2) for k in range(-160,161))
        cover=circle_images(g,beta,mp.mpf(0),12)['kernel']
        assert abs(spectral-cover)<mp.mpf('1e-80')
        traces.append(dict(g=str(g),beta=str(beta),spectral=str(spectral),cover=str(cover)))
    return dict(kernels=rows,traces=traces)


def rotor_model(g,N,metric,h):
    dim=len(h);sites=list(product(range(-N,N+1),repeat=dim));index={x:i for i,x in enumerate(sites)}
    n=np.array(sites,dtype=float);count=len(sites)
    kinetic=g*g/2*np.einsum('bi,ij,bj->b',n,metric,n)
    cosines=[];sines=[]
    for mu in range(dim):
        raise_op=np.zeros((count,count))
        for col,x in enumerate(sites):
            y=list(x);y[mu]+=1;y=tuple(y)
            if y in index:raise_op[index[y],col]=1
        cosines.append((raise_op+raise_op.T)/2)
        sines.append((raise_op-raise_op.T)/(2j))
    H=np.diag(kinetic+dim/(g*g))-sum(cosines)/(g*g)
    vals,vecs=eigh(H);psi=vecs[:,0];gaps=vals[1:]-vals[0]
    M=sum(weight*S for weight,S in zip(h,sines))/g
    H2=sum(weight*weight*C for weight,C in zip(h,cosines))
    amplitude=vecs[:,1:].T.conj()@(M@psi)
    inverse_moment=float(np.sum(abs(amplitude)**2/gaps))
    contact=float(np.vdot(psi,H2@psi).real)
    assert abs(2*inverse_moment-contact)<2e-11
    lam=.173;phases=np.exp(1j*g*lam*(n@h))
    shifted=np.diag(kinetic+dim/(g*g)).astype(complex)
    for weight,C,S in zip(h,cosines,sines):
        angle=g*lam*weight
        shifted-=(math.cos(angle)*C-math.sin(angle)*S)/(g*g)
    conjugate=phases[:,None]*H*phases.conj()[None,:]
    source_error=float(np.max(abs(shifted-conjugate)))
    assert source_error<2e-12
    first_moment=float(np.vdot(M@psi,(H-vals[0]*np.eye(count))@(M@psi)).real)
    comm=H@M-M@H
    double=M@comm-comm@M
    commutator_moment=float(np.vdot(psi,double@psi).real/2)
    assert abs(first_moment-commutator_moment)<2e-11
    # Full multiplication cosines on a padded Fourier box retain cutoff leakage.
    padded_shape=(2*N+5,)*dim;wave=np.zeros(padded_shape);core=(slice(2,-2),)*dim
    wave[core]=psi.reshape((2*N+1,)*dim)
    transformed=[(np.roll(wave,1,axis=i)+np.roll(wave,-1,axis=i))/2 for i in range(dim)]
    gradient_moment=sum(h[i]*h[j]*metric[i,j]*np.sum(transformed[i]*transformed[j])/2
                        for i in range(dim) for j in range(dim))
    return dict(g=g,N=N,metric=metric.tolist(),source=h.tolist(),dimension=count,
                energy=float(vals[0]),gap=float(gaps[0]),contact=contact,
                twice_inverse_moment=2*inverse_moment,source_conjugacy_error=source_error,
                first_moment=first_moment,double_commutator=commutator_moment,
                full_cosine_gradient_moment=float(gradient_moment),
                cutoff_gradient_difference=float(first_moment-gradient_moment))


def rotor_checks():
    rows=[]
    C=np.array([[1,1,-1,-1,0,0,0],[0,0,0,1,1,-1,-1]],dtype=float)
    metric=C@C.T;assert np.array_equal(metric,np.array([[4,-1],[-1,4]]))
    specifications=[(.35,(16,24),np.array([[4.]]),np.array([1.])),
                    (.7,(12,20),np.array([[4.]]),np.array([1.])),
                    (.6,(8,12),metric,np.array([1.,-.4])),
                    (1.,(6,10),metric,np.array([1.,-.4]))]
    for g,cuts,G,h in specifications:
        a=rotor_model(g,cuts[0],G,h);b=rotor_model(g,cuts[1],G,h)
        assert abs(a['energy']-b['energy'])<1e-7
        assert abs(a['contact']-b['contact'])<1e-7
        assert abs(b['cutoff_gradient_difference'])<1e-8
        assert b['gap']>0
        rows.append(dict(coarse=a,refined=b))
    return rows


def main():
    start=time.monotonic()
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope=__doc__,
             circle=circle_checks(),rotors=rotor_checks(),status='PERSONAL_CHECKS_COMPLETED')
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
