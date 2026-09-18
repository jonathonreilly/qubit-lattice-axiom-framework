#!/usr/bin/env python3
"""Personal C3 bridge challenges: Bessel/Fourier, quadrature, finite differences.

The finite time grids are declared test objects. They do not prove the
continuous-time or all-volume theorem. No external scientific input is read;
this file is read for its source hash. Outputs are not audit-cache envelopes.
"""
AUDIT_TIMEOUT_SEC=120
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import ive


def cumulant3(a,b,c,w):
    a0=a-np.dot(w,a);b0=b-np.dot(w,b);c0=c-np.dot(w,c)
    return float(np.dot(w,a0*b0*c0))


def covariance(a,b,w):
    return float(np.dot(w,(a-np.dot(w,a))*(b-np.dot(w,b))))


def one_face_quadrature(g,T,phi,order):
    nodes,weights=hermgauss(order)
    delta=T/2
    z=phi+math.sqrt(2*g*g*T)*nodes
    S=delta*(1-np.cos(z));raw=weights/np.sqrt(np.pi)*np.exp(-S/(g*g))
    w=raw/raw.sum()
    A=delta*np.sin(z);B=delta*np.cos(z);D=-delta*np.sin(z)
    c3=float(np.dot(w,D)-3*covariance(A,B,w)/(g*g)+cumulant3(A,A,A,w)/(g**4))
    return dict(cubic=c3,correction=c3+delta*math.sin(phi),partition=float(raw.sum()))


def one_face_bessel(g,T,phi,cutoff):
    # Actual sampled Brownian flux variance is FOUR times link variance:
    # 4g^2*(T/4)=g^2 T. Exp[-delta(1-cos)/g^2] has ive Fourier weights.
    n=np.arange(1,cutoff+1)
    b=T/(2*g*g)
    a=ive(n,b)*np.exp(-g*g*T*n*n/2)
    q0=float(ive(0,b)+2*np.dot(a,np.cos(n*phi)))
    q1=float(-2*np.dot(n*a,np.sin(n*phi)))
    q2=float(-2*np.dot(n*n*a,np.cos(n*phi)))
    q3=float(2*np.dot(n**3*a,np.sin(n*phi)))
    assert q0>0
    c3=-g*g*(q3/q0-3*q1*q2/(q0*q0)+2*(q1/q0)**3)
    return dict(cubic=c3,correction=c3+(T/2)*math.sin(phi),partition=q0)


def one_face_checks():
    rows=[]
    for g,T,phi in product((.2,.5,1.),(.1,.4),(.3,1.2,2.7)):
        q32=one_face_quadrature(g,T,phi,32)
        q48=one_face_quadrature(g,T,phi,48)
        b48=one_face_bessel(g,T,phi,48)
        b64=one_face_bessel(g,T,phi,64)
        assert abs(q32['cubic']-q48['cubic'])<1e-11
        assert abs(b48['cubic']-b64['cubic'])<1e-11
        assert abs(b64['cubic']-q48['cubic'])<5e-9
        assert abs(b64['partition']-q48['partition'])<2e-13
        r=2*T*T;delta0=r+g*g*T/(2*(1-r));delta3=delta0+(1-r)**(-3)-1
        assert abs(q48['cubic'])<=(T/2)/(1-r)**3+1e-12
        assert abs(q48['correction'])<=(T/2)*delta3+1e-12
        rows.append(dict(g=g,T=T,phi=phi,quadrature32=q32,quadrature48=q48,
                         bessel48=b48,bessel64=b64,cubic_bound=(T/2)/(1-r)**3,
                         correction_bound=(T/2)*delta3))
    return rows


def time_precision():
    rows=[]
    for m,T,g in product((2,3,5,8,17),(.1,.4),(.2,.7)):
        delta=T/m;t=np.arange(1,m)*delta
        D=(2*np.eye(m-1)-np.eye(m-1,k=1)-np.eye(m-1,k=-1))/(delta*delta)
        G=np.linalg.inv(D)
        expected=t*(T-t)/2
        assert np.max(np.abs(G@np.ones(m-1)-expected))<2e-14
        assert G.min()>0 and np.max(G.sum(axis=1))<=T*T/8+2e-14
        # Independent covariance identity from Brownian bridge conditioning.
        cov=g*g*(np.minimum(t[:,None],t[None,:])-np.outer(t,t)/T)
        noise=2*g*g/delta
        residual=float(np.max(np.abs(D@cov+cov@D-noise*np.eye(m-1))))
        assert residual<2e-10
        assert np.max(np.abs(cov-g*g/delta*G))<2e-13
        rows.append(dict(m=m,T=T,g=g,max_green_row=float(G.sum(axis=1).max()),
                         row_upper=T*T/8,OU_covariance_residual=residual))
    return rows


def two_face_nodes(g,T,order):
    # Two actual adjacent plaquettes, with one oppositely oriented shared link.
    C=np.array([[1,1,-1,-1,0,0,0],[0,0,0,-1,1,-1,-1]],dtype=float)
    metric=C@C.T
    assert np.array_equal(metric,np.array([[4,-1],[-1,4]]))
    t=np.array([T/3,2*T/3])
    G=np.minimum(t[:,None],t[None,:])-np.outer(t,t)/T
    chol=np.linalg.cholesky(g*g*np.kron(G,metric))
    n,w=hermgauss(order)
    index=np.array(list(product(range(order),repeat=4)),dtype=int)
    X=math.sqrt(2)*n[index]@chol.T
    weights=np.prod(w[index],axis=1)/(math.pi**2)
    return X.reshape(-1,2,2),weights,metric


def two_face_quantities(g,T,ends,hends,kends,lends,order):
    eta,base,metric=two_face_nodes(g,T,order)
    blend=lambda ab: np.array([(2*ab[0]+ab[1])/3,(ab[0]+2*ab[1])/3])
    f,h,k,l=map(blend,(ends,hends,kends,lends))
    z=f+eta;delta=T/3
    S=delta*np.sum(1-np.cos(z),axis=(1,2))
    raw=base*np.exp(-S/(g*g));w=raw/raw.sum()
    first=lambda v:delta*np.sum(np.sin(z)*v,axis=(1,2))
    second=lambda v,u:delta*np.sum(np.cos(z)*v*u,axis=(1,2))
    third=-delta*np.sum(np.sin(z)*h*k*l,axis=(1,2))
    A,B,D=map(first,(h,k,l))
    c3=float(np.dot(w,third)
             -(covariance(second(h,k),D,w)+covariance(second(h,l),B,w)
               +covariance(second(k,l),A,w))/(g*g)
             +cumulant3(A,B,D,w)/(g**4))
    hessian=float(np.dot(w,second(h,k))-covariance(A,B,w)/(g*g))
    straight3=float(-delta*np.sum(np.sin(f)*h*k*l))
    return dict(cubic=c3,hessian=hessian,correction=c3-straight3,metric=metric.tolist())


def two_face_checks():
    g,T=.45,.2
    ends=np.array([[.6,-.25],[.9,.4]])
    h=np.array([[1.,.2],[-.1,.4]])
    k=np.array([[.3,-.5],[.7,.1]])
    l=np.array([[.2,.6],[-.2,.3]])
    a=two_face_quantities(g,T,ends,h,k,l,12)
    b=two_face_quantities(g,T,ends,h,k,l,16)
    assert abs(a['cubic']-b['cubic'])<2e-9
    step=2e-4
    plus=two_face_quantities(g,T,ends+step*l,h,k,l,16)['hessian']
    minus=two_face_quantities(g,T,ends-step*l,h,k,l,16)['hessian']
    fd=(plus-minus)/(2*step)
    assert abs(fd-b['cubic'])<2e-7
    blend=lambda ab:np.array([(2*ab[0]+ab[1])/3,(ab[0]+2*ab[1])/3])
    norms=[float(((T/3)*np.sum(np.abs(blend(z))**3))**(1/3)) for z in (h,k,l)]
    r=2*T*T;delta3=r+g*g*T/(2*(1-r))+(1-r)**(-3)-1
    bound=np.prod(norms)/(1-r)**3;correction=delta3*np.prod(norms)
    assert abs(b['cubic'])<=bound and abs(b['correction'])<=correction
    # Chain rule under f=g*C a supplies exactly one remaining factor g
    # after dividing the effective action by g^2.
    scaled=two_face_quantities(g,T,ends,g*h,g*k,g*l,16)['cubic']/(g*g)
    assert abs(scaled-g*b['cubic'])<1e-12
    return dict(g=g,T=T,quadrature12=a,quadrature16=b,hessian_difference=fd,
                difference_step=step,space_time_l3_norms=norms,cubic_bound=float(bound),
                correction_bound=float(correction),scaled_cubic=scaled,
                expected_scaled_cubic=g*b['cubic'])


def main():
    start=time.monotonic()
    result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope=__doc__,time_precision=time_precision(),single_face=one_face_checks(),
                adjacent_faces=two_face_checks())
    result.update(status='PERSONAL_CHECKS_COMPLETED',elapsed_seconds=time.monotonic()-start)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':main()
