#!/usr/bin/env python3
"""Independent finite challenges for reflection/path steps in Blocks01-03.

The 12-link binary-clock strip tests the reflection/chessboard ALGEBRA only.
It cannot validate the Brownian exp(-constant/g^2) estimate. A separate
clock countercontrol illustrates that limitation. Fourth moments are
checked in a genuine compact single-rotor Schrödinger ground process.
"""
AUDIT_TIMEOUT_SEC = 120

# Scientific inputs are defined below; the only repository integrity read
# is this source file for its SHA256. Raw outputs are not audit caches.

from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
import time

import mpmath as mp
import numpy as np
from scipy.linalg import eigh_tridiagonal, expm
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh


def xor_operator(nbits, masks):
    states=np.arange(1<<nbits)
    return coo_matrix((np.ones(len(states)*len(masks)),
                      (np.tile(states,len(masks)),
                       np.concatenate([states^m for m in masks]))),
                     shape=(len(states),len(states))).tocsr()


def clock_strip():
    # A periodic strip of FOUR square plaquettes, height ONE with free
    # top/bottom boundaries. Vertical links v_x:bits0..3; bottom h_x:4..7;
    # top h_x:8..11. This is NOT the three-dimensional rotor Hamiltonian.
    states=np.arange(4096,dtype=np.int64)
    face_masks=[(1<<x)|(1<<((x+1)%4))|(1<<(4+x))|(1<<(8+x)) for x in range(4)]
    parity=np.array([int(i).bit_count()%2 for i in states])
    bad=np.array([parity[states&m] for m in face_masks]).T
    face_bits=bad@(1<<np.arange(4))
    full_flip=xor_operator(12,[1<<i for i in range(12)])
    reduced_states=np.arange(16)
    single=xor_operator(4,[1<<i for i in range(4)])
    pair=xor_operator(4,[(1<<i)|(1<<((i+1)%4)) for i in range(4)])
    rows=[]
    # Closed positive half between vertex planes x=0,2 includes shared
    # boundary vertical links0,2. Reflection sends h_x to h_(-x-1).
    half=[0,1,2,4,5,8,9]
    reflected=[0,3,2,6,7,11,10]
    encode=lambda indices:sum(((states>>i)&1)<<j for j,i in enumerate(indices))
    left,right=encode(half),encode(reflected)
    for r,v in ((.7,.3),(.2,1.1),(1.3,2.0)):
        H=diags(12*r+2*v*bad.sum(axis=1))-r*full_flip
        values,vectors=eigsh(H,k=1,which='SA',v0=np.ones(4096),tol=1e-12)
        psi=vectors[:,0]
        if psi.sum()<0:psi=-psi
        assert psi.min()>0
        residual=np.linalg.norm(H@psi-values[0]*psi)
        assert residual<2e-10
        probability=psi*psi
        physical=np.bincount(face_bits,weights=probability,minlength=16)
        Hr=np.diag(12*r+2*v*np.array([int(i).bit_count() for i in reduced_states]))-r*(2*single+pair).toarray()
        vr,ur=np.linalg.eigh(Hr)
        assert abs(vr[0]-values[0])<2e-11
        assert np.max(np.abs(physical-ur[:,0]**2))<2e-11
        rp=np.zeros((128,128))
        np.add.at(rp,(left,right),probability)
        assert np.max(np.abs(rp-rp.T))<2e-12
        minimum=float(np.linalg.eigvalsh((rp+rp.T)/2).min())
        assert minimum>=-2e-12
        dense=float(probability[np.all(bad==1,axis=1)].sum())
        ratios=[]
        for k in range(1,5):
            for subset in combinations(range(4),k):
                actual=float(probability[np.all(bad[:,subset]==1,axis=1)].sum())
                bound=dense**(k/4)
                assert actual<=bound+2e-12
                ratios.append(actual/bound)
        # Removing the reflection action from the second argument is not
        # a valid generic test, since the resulting ordinary Gram matrix
        # is also positive. Instead use the actual shared-boundary algebra.
        rows.append(dict(jump_rate=r,magnetic_coefficient=v,ground_energy=float(values[0]),
                         residual=float(residual),full_to_reduced_max_error=float(np.max(np.abs(physical-ur[:,0]**2))),
                         RP_matrix_dimension=128,RP_min_eigenvalue=minimum,
                         dense_bad_probability=dense,max_chessboard_ratio=max(ratios)))
    return dict(model='Four-plaquette 12-binary-link periodic strip, all half-link indicators',rows=rows)


def constrained_kernel_control():
    # Kernel restricted to paths visiting state1. Paths staying in state0
    # have survival exp(-rT); subtract their kernel exactly.
    r,T=1.0,1.0
    H=np.array([[r,-r],[-r,r]])
    heat=expm(-T*H)
    K=heat-np.diag([math.exp(-r*T),0])
    spectrum=np.linalg.eigvalsh(K)
    assert K.min()>0 and spectrum[0]<-.05
    norm=max(abs(spectrum))
    trace2=float(np.trace(K@K))
    assert trace2<=float(np.trace(expm(-2*T*H)))+1e-13
    rows=[]
    for m in (2,4,6,10):
        actual=float(np.sum(spectrum**m));bound=norm**(m-2)*trace2
        assert 0<=actual<=bound+1e-13
        rows.append(dict(even_m=m,trace_power=actual,norm_HS_bound=bound))
    return dict(kernel=K.tolist(),spectrum=spectrum.tolist(),even_power_checks=rows,
                conclusion='Positive path kernel can have a negative eigenvalue; use the Hilbert-Schmidt even-power bound.')


def rotor_moment(g,h,cutoff):
    n=np.arange(-cutoff,cutoff+1)
    vals,vecs=eigh_tridiagonal(g*g*n*n/2+1/(g*g),np.full(2*cutoff,-.5/(g*g)))
    psi=vecs[:,0]
    correlations=[]
    for k in (1,2):
        shifted=np.zeros_like(psi)
        shifted[k:]=psi[:-k]
        coeff=vecs.T@shifted
        correlations.append(float(np.dot(coeff*coeff,np.exp(-h*(vals-vals[0])))))
    return 6-8*correlations[0]+2*correlations[1],correlations


def moments_and_clock_control():
    mp.mp.dps=70
    free=[]
    for x in (mp.mpf('1e-8'),mp.mpf('.001'),mp.mpf('.2'),mp.mpf(1),mp.mpf(10)):
        exact=6-8*mp.exp(-x/2)+2*mp.exp(-2*x)
        assert 0<exact<=12*x*x
        # A factor4 smaller than the sharp small-time coefficient fails.
        free.append(dict(variance=str(x),chord_fourth=str(exact),ratio_to_x_squared=str(exact/(x*x))))
    assert mp.mpf(free[0]['ratio_to_x_squared'])>mp.mpf('2.999999')
    rows=[]
    for g in (.2,.5,1.):
        for h in (.01,.1,1.):
            m32,c32=rotor_moment(g,h,32)
            m48,c48=rotor_moment(g,h,48)
            assert abs(m32-m48)<2e-10
            bound=12*g**4*h*h
            assert -2e-11<=m48<=bound+2e-11
            rows.append(dict(g=g,h=h,moment32=m32,moment48=m48,bound=bound,
                             ground_correlations=c48,ratio=m48/bound))
    clocks=[]
    for gs in ('.1','.03','.01'):
        g=mp.mpf(gs)
        # Actual isolated four-link binary plaquette: a flip on any of
        # four links changes its flux bit, so offdiag=-4g^2, potential
        # diagonal difference=2/g^2. No Brownian path assumption holds.
        r=4*g*g;v=1/(g*g)
        z=mp.sqrt(v*v+r*r)
        bad=r*r/(2*z*(z+v))  # stable form of (1-v/z)/2
        assert abs(bad/(4*g**8)-1)<mp.mpf('.001')
        clocks.append(dict(g=gs,binary_bad_probability=str(bad),leading_polynomial=str(4*g**8)))
    return dict(free_circle=free,interacting_single_rotor=rows,
                finite_clock_countercontrol=clocks,
                scope='Single-rotor moments test constants. Binary-clock probabilities must not be assigned Brownian exponential estimates.')


def main():
    start=time.monotonic()
    ans=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             reflection=clock_strip(),constrained_kernel=constrained_kernel_control(),
             moments=moments_and_clock_control())
    ans['elapsed_seconds']=time.monotonic()-start
    ans['status']='PERSONAL_CHECKS_COMPLETED'
    print(json.dumps(ans,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
