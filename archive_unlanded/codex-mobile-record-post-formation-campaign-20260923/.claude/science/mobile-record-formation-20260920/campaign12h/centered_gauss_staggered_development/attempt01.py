#!/usr/bin/env python3
"""Exact algebra and finite Fourier controls; no microscopic photon claim."""
from pathlib import Path
from itertools import product
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent;checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
def cross(v):
    return s.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])

L=6;rng=np.random.default_rng(202609211034)
xyz=np.moveaxis(np.indices((L,L,L)),0,-1)
labels=np.vstack([np.zeros(3,dtype=int),np.eye(3,dtype=int),-np.eye(3,dtype=int)])
E=labels[rng.integers(0,7,size=(L,L,L))]
def div(F):return sum(np.roll(F[...,i],-1,axis=i)-np.roll(F[...,i],1,axis=i) for i in range(3))
fourier=np.fft.fftn(E,axes=(0,1,2));errors=[]
for eta in product((0,1),repeat=3):
    eta=np.array(eta);phase=(-1)**np.sum(xyz*eta,axis=-1);sign=(-1)**eta
    transformed=phase[...,None]*sign*E
    assert np.array_equal(div(transformed),phase*div(E))
    assert np.array_equal(np.sum(transformed**2,axis=-1),np.sum(E**2,axis=-1))
    shifted=np.roll(fourier,tuple((eta*L//2).tolist()),axis=(0,1,2))*sign
    errors.append(float(np.max(np.abs(np.fft.fftn(transformed,axes=(0,1,2))-shifted))))
check('all_eight_stagger_maps_preserve_capacity_and_transform_divergence_and_Fourier',max(errors)<1e-12,dict(max_Fourier_error=max(errors)))

# One exact closed four-record loop, then all transformed closed states.
F=np.zeros((L,L,L,3),dtype=int);center=np.array([2,2,2]);i,j=np.eye(3,dtype=int)[:2]
for position,axis,value in [(center-j,0,1),(center+j,0,-1),(center-i,1,-1),(center+i,1,1)]:F[tuple(position)+(axis,)]=value
assert not np.any(div(F))
for eta in product((0,1),repeat=3):
    eta=np.array(eta);T=(-1)**np.sum(xyz*eta,axis=-1)[...,None]*((-1)**eta)*F
    assert not np.any(div(T)) and np.count_nonzero(T)==4
check('closed_loop_stagger_orbit_is_admissible_and_weight_preserving',True)

parities=set()
for x in product((0,1),repeat=3):
    for i in range(3):
        left=np.array(x)-np.eye(3,dtype=int)[i];right=np.array(x)+np.eye(3,dtype=int)[i]
        assert np.array_equal(left%2,right%2);parities.add(tuple(left%2))
check('charge_graph_has_eight_parity_sectors',len(parities)==8)

a=s.symbols('a0:3',real=True);b=s.symbols('b0:3',real=True)
v=s.Matrix([a[i]+s.I*b[i] for i in range(3)]);Cp=cross(v);Cm=Cp.conjugate().T;norm=(v.conjugate().T*v)[0]
assert (Cp.conjugate().T*Cp-norm*s.eye(3)+v*v.conjugate().T).applyfunc(s.expand)==s.zeros(3)
assert (Cp*Cp.conjugate().T-norm*s.eye(3)+v.conjugate()*v.T).applyfunc(s.expand)==s.zeros(3)
assert v.T*Cp==s.zeros(1,3) and (-v.conjugate()).T*Cm==s.zeros(1,3)
G=s.zeros(6);G[:3,3:]=Cm;G[3:,:3]=-Cp
check('general_complex_cross_singular_values_Gauss_identities_and_energy_adjointness',G.conjugate().T+G==s.zeros(6))

spectral_errors=[]
for k in [(0.,0.,0.),(.17,.49,.81),(np.pi,0.,0.),(np.pi,np.pi,np.pi),(0.,.3,1.2)]:
    vv=np.exp(1j*np.array(k))-1;cp=np.array(cross(vv),dtype=complex);cm=cp.conj().T
    g=np.block([[np.zeros((3,3)),cm],[-cp,np.zeros((3,3))]])
    eig=np.linalg.eigvalsh(1j*g);w=np.linalg.norm(vv);expected=np.array([-w,-w,0,0,w,w])
    spectral_errors.append(float(np.max(abs(eig-expected))))
check('adjoint_wave_spectra_at_generic_axis_and_corner_modes',max(spectral_errors)<1e-12,dict(max_error=max(spectral_errors)))

for size in (6,8):
    centered=forward=0
    for n in product(range(size),repeat=3):
        k=2*np.pi*np.array(n)/size
        centered+=np.linalg.norm(np.sin(k))<1e-12;forward+=np.linalg.norm(np.exp(1j*k)-1)<1e-12
    assert centered==8 and forward==1
check('full_even_torus_zero_census_centered_eight_adjoint_one',True)

# The symmetric-exchange floor has a different symbol from centered curl.
floor=[]
for eta in product((0,1),repeat=3):
    k=np.pi*np.array(eta);value=-4*sum(np.sin(k/2)**2)
    assert abs(value+4*sum(eta))<1e-12;floor.append(value)
check('exchange_floor_does_not_vanish_at_nonzero_centered_corners',all(x<0 for x in floor[1:]),dict(multiplier_at_k_pi_eta=floor))

(HERE/'CENTERED_GAUSS_STAGGERED_RESULTS.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,scope='Author operator and symmetry controls only. The static symmetry proof, finite-difference comparison and full stochastic dynamics have separate scopes.'),indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
