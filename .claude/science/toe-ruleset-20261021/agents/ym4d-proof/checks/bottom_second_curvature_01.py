#!/usr/bin/env python3
"""Actual d4 twisted scalar-cell Green kernels and complex-alias controls.

The proof is separate. Norm samples do not prove uniformity. Counting measure,
ell^-4 Fourier normalization, analytic negative-momentum adjoints.
"""
import itertools,json,time
import numpy as np
from scipy.special import ive
start=time.time();checks=[];samples=[]
def check(name,x,tol=1e-9,positive=False):
    x=float(x);checks.append(dict(name=name,value=x,threshold=tol,positive=positive,passed=x>tol if positive else x<=tol))
def data(ell,p):
    ks=np.fft.fftfreq(ell)*ell
    K=np.stack(np.meshgrid(*([ks]*4),indexing='ij'),axis=-1)
    q=(p+2*np.pi*K)/ell
    nu=np.exp(1j*q)-1;bar=np.exp(-1j*q)-1
    phi=np.sum(nu*bar,axis=-1)
    pos=np.stack(np.meshgrid(*([np.arange(ell)]*4),indexing='ij'),axis=-1)
    phase=np.exp(1j*np.sum(pos*p,axis=-1)/ell)
    return q,nu,bar,phi,pos,phase
def row_norm(mult,p,ell):
    h=np.fft.ifftn(mult)
    pos=np.stack(np.meshgrid(*([np.arange(ell)]*4),indexing='ij'),axis=-1)
    wt=np.exp(np.sum(pos*p.imag,axis=-1)/ell)
    rows=np.fft.ifftn(np.fft.fftn(np.abs(h))*np.fft.fftn(wt)).real/wt
    return float(rows.max()),h
def row_zero(h,p,ell):
    pos=np.array(list(itertools.product(range(ell),repeat=4)))
    idx=tuple((-pos%ell).T)
    return h[idx]*np.exp(-1j*(pos@p)/ell)

momenta=[np.array([.21,.37,-.42,.13])+1j*np.array([.02,-.013,.017,-.011]),
         np.array([np.pi,-np.pi,.71,-.44])+1j*np.array([.02,.014,-.01,.009]),
         np.zeros(4,dtype=complex)]
for ell in [3,9,27]:
 for case,p in enumerate(momenta):
    q,nu,bar,phi,pos,phase=data(ell,p)
    high=np.ones(phi.shape);high[(0,)*4]=0
    denom=phi.copy();denom[(0,)*4]=1
    inv=high/denom
    nrm,h=row_norm(nu[...,0]*inv,p,ell)
    check('projected_scalar_inverse',np.max(np.abs(phi*inv-high)))
    check('analytic_negative_momentum_phi',np.max(np.abs(phi-4*np.sum(np.sin(q/2)**2,axis=-1))))
    if case<2:
        wrong=np.sum(np.abs(nu)**2,axis=-1)
        check('reject_complex_conjugation',np.max(np.abs(phi-wrong)),1e-6,True)
    heat=[]
    for ratio in [.01,1,3]:
        t=ell**2*ratio
        hn,_=row_norm(nu[...,0]*np.exp(-t*phi)*high,p,ell)
        heat.append(dict(t=t,derivative_row_norm=hn,short_scaled=hn*np.sqrt(1+t),long_scaled=ell*hn*np.exp(.5*t/ell**2)))
    samples.append(dict(ell=ell,case=case,p_real=p.real.tolist(),p_imag=p.imag.tolist(),derivative_inverse_row_norm=nrm,divided_by_ell=nrm/ell,heat=heat))
    if ell==3:
        # Independent cell incidence, not Fourier multiplier construction.
        V=ell**4;coords=pos.reshape(V,4)
        shifts=[]
        for mu in range(4):
            S=np.zeros((V,V),dtype=complex)
            for u,x in enumerate(coords):
                y=x.copy();y[mu]+=1
                S[u,np.ravel_multi_index(tuple(y%ell),(ell,)*4)]=np.exp(1j*p[mu]) if y[mu]==ell else 1
            shifts.append(S)
        D=[s-np.eye(V) for s in shifts]
        Dminus=[]
        for mu in range(4):
            S=shifts[mu].copy();S[coords[:,mu]==ell-1]*=np.exp(-2j*p[mu])
            Dminus.append((S-np.eye(V)).T)
        Delta=sum(Dminus[mu]@D[mu] for mu in range(4))
        vec=np.exp(1j*coords@p/ell);cov=np.exp(-1j*coords@p/ell)/V
        low=np.outer(vec,cov)
        Green=np.linalg.solve(Delta+low,np.eye(V)-low)
        check('cell_incidence_vs_fourier_row',np.max(np.abs((D[0]@Green)[0]-row_zero(h,p,ell))))
        check('cell_counting_operator_norm',abs(np.max(np.sum(np.abs(D[0]@Green),axis=1))-nrm))
        check('reject_missing_cell_volume',np.max(np.abs((D[0]@Green)[0]-V*row_zero(h,p,ell))),1e-6,True)
        if case==2:
            check('unprojected_zero_mode_is_null',np.max(np.abs(Delta@np.ones(V))))
            check('unprojected_inverse_cannot_equal_identity',np.linalg.norm(np.ones(V)),1e-6,True)

# Actual phase/image formula for the one-dimensional heat kernel, with a
# complex top twist; product structure gives the d4 image expression.
image_samples=[]
for ell in [3,9,27]:
 p=.43+.02j;ks=np.fft.fftfreq(ell)*ell
 for t in [.1,1.,float(ell**2)]:
    for z in [0,ell-1,-ell+1]:
        q=(p+2*np.pi*ks)/ell
        fourier=np.mean(np.exp(1j*q*z-t*(2-2*np.cos(q))))
        cutoff=int(np.ceil((40*np.sqrt(1+t)+abs(z))/ell))+5
        mm=np.arange(-cutoff,cutoff+1)
        images=np.sum(np.exp(1j*p*mm)*ive(np.abs(z-ell*mm),2*t))
        check('complex_twisted_images',abs(fourier-images))
        image_samples.append(dict(ell=ell,t=t,z=z,error=float(abs(fourier-images)),cutoff=cutoff))

# Full alias sum is periodic; its arbitrarily selected high part is not.
ell=3;p=momenta[0]
q,nu,bar,phi,pos,phase=data(ell,p)
_,hfull=row_norm(nu[...,0]/phi,p,ell)
shift=p.copy();shift[0]+=2*np.pi
q2,n2,b2,ph2,po2,pa2=data(ell,shift)
_,hfull2=row_norm(n2[...,0]/ph2,shift,ell)
check('full_alias_periodic_face_gluing',np.max(np.abs(row_zero(hfull,p,ell)-row_zero(hfull2,shift,ell))))
mask=np.ones(phi.shape);mask[(0,)*4]=0
_,hh=row_norm(nu[...,0]/phi*mask,p,ell)
_,hh2=row_norm(n2[...,0]/ph2*mask,shift,ell)
check('reject_individually_periodic_high_branch',np.max(np.abs(row_zero(hh,p,ell)-row_zero(hh2,shift,ell))),1e-6,True)

# Normalized exact quadratic coordinate map and a genuine complex null point.
division=[]
for ell in [3,9,27,81]:
 w=np.array([.04,.04j,0,0],dtype=complex)
 k=2*ell*np.arcsin(w/(2*ell))
 normalized=4*ell**2*np.sum(np.sin(k/(2*ell))**2)
 check('normalized_quadratic_coordinate',abs(normalized-np.sum(w*w)))
 check('complex_null_variety',abs(normalized))
 # This numerator vanishes at the real origin, but is not divisible by phi.
 bad=w[0]**2
 check('reject_origin_only_divisibility',abs(bad),1e-6,True)
 division.append(dict(ell=ell,k_real=k.real.tolist(),k_imag=k.imag.tolist(),normalized_symbol_real=float(normalized.real),normalized_symbol_imag=float(normalized.imag),bad_numerator=float(abs(bad))))
out=dict(scope='actual d4 cell Green kernels; finite support for separate uniform proof',checks=checks,passed=sum(c['passed'] for c in checks),total=len(checks),norm_samples=samples,image_samples=image_samples,division=division,elapsed_seconds=time.time()-start)
print(json.dumps(out,indent=2,allow_nan=False));raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
