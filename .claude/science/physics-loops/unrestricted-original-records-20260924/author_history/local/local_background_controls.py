#!/usr/bin/env python3
"""Separate finite controls of locality and the dissipative Duhamel estimate.

Neither auxiliary system is the physical cubic gauge/record model. No photon
signal or microscopic limit is simulated. All numerical norm and quadrature
checks are floating point, without interval enclosure.
"""
from pathlib import Path
from itertools import product
import hashlib, json, time
import numpy as np
import scipy
from scipy import sparse
from scipy.linalg import eigh
from scipy.sparse.linalg import expm_multiply
from numpy.polynomial.legendre import leggauss
import sympy as sp


def diagonal_rotor_control():
    x,y,z=sp.symbols('x y z', integer=True)
    d=(x-y)**2+(y-z)**2
    difference=sp.expand(d.subs(x,x+1)-d)
    assert sp.diff(difference,z)==0
    rows=[]
    phase_time=.173
    for cutoff in (1,2,4,8):
        far=0.; near=0.; count=0
        for a,b,c in product(range(-cutoff,cutoff+1),repeat=3):
            if a==cutoff: continue
            f=lambda aa,bb,cc: (aa-bb)**2+(bb-cc)**2
            phase=lambda aa,bb,cc: np.exp(1j*phase_time*(f(aa+1,bb,cc)-f(aa,bb,cc)))
            if c<cutoff:
                far=max(far,abs(phase(a,b,c+1)-phase(a,b,c)));count+=1
            if b<cutoff:
                near=max(near,abs(phase(a,b+1,c)-phase(a,b,c)))
        expected=2*abs(np.sin(phase_time))
        assert far<1e-14 and abs(near-expected)<1e-13
        rows.append({'cutoff':cutoff,'valid_far_shift_columns':count,
                     'far_commutator_norm':far,'near_commutator_norm':near,
                     'near_exact_norm':expected})
    return {'diagonal':'(E1-E2)^2+(E2-E3)^2',
            'first_shift_energy_difference':str(difference),'rows':rows}


def local(n,index,op):
    result=sparse.csr_matrix([[1.]])
    for site in range(n):
        result=sparse.kron(result,op if site==index else sparse.eye(2),format='csr')
    return result


def hermitian_norm(a):
    residual=np.linalg.norm(a-a.conj().T,ord='fro')
    assert residual<1e-10
    return float(np.max(np.abs(np.linalg.eigvalsh((a+a.conj().T)/2))))


def chain_control(n,K,delta=.4,kappa=.07,t=.2):
    # Pair creation raises number by two; the exchange Hamiltonian preserves
    # number. This chain has no cubic Gauss law or first-pair Wilson effect.
    raise_op=sparse.csr_matrix([[0.,0.],[1.,0.]])
    create=[local(n,i,raise_op) for i in range(n)]
    number=[c@c.T for c in create]
    ident=sparse.eye(2**n,format='csr')
    diagonal=sum(number[i]@number[i+1] for i in range(n-1))
    hopping=sum(create[i]@create[i+1].T+create[i+1]@create[i].T for i in range(n-1))
    h=K*diagonal+delta*hopping
    jumps=[create[i]@create[i+1] for i in range(n-1)]
    loss=[j.T@j for j in jumps]
    dissipator=sum(sparse.kron(j.T,j.T,format='csr')-
        .5*sparse.kron(ident,q,format='csr')-
        .5*sparse.kron(q.T,ident,format='csr') for j,q in zip(jumps,loss))
    generator=1j*(sparse.kron(ident,h,format='csr')-
                   sparse.kron(h.T,ident,format='csr'))+kappa*dissipator
    o=number[0].toarray()
    eigenvalues,eigenvectors=eigh(h.toarray())
    def evolve(v):
        unitary=(eigenvectors*np.exp(-1j*v*eigenvalues))@eigenvectors.conj().T
        return unitary.conj().T@o@unitary
    full=expm_multiply(t*generator,o.ravel(order='F')).reshape(o.shape,order='F')
    difference=hermitian_norm(full-evolve(t))
    def integral(order):
        nodes,weights=leggauss(order)
        vals=[]
        for v in t*(nodes+1)/2:
            ov=evolve(v)
            norms=[hermitian_norm(j.T@ov@j-.5*(q@ov+ov@q))
                   for j,q in zip(jumps,loss)]
            vals.append(sum(norms))
        return kappa*t*float(np.dot(weights,vals))/2
    coarse,fine=integral(20),integral(32)
    quadrature_delta=abs(coarse-fine)
    # A numerical corroboration of Duhamel's norm inequality, not an
    # interval proof of the integral or of the rotor/locality theorem.
    assert difference<=fine+max(1e-10,3*quadrature_delta)
    assert difference<=2*kappa*(n-1)*t+1e-10
    return {'sites':n,'K':K,'delta':delta,'kappa':kappa,'time':t,
            'local_observable_full_vs_hamiltonian_norm':difference,
            'summed_disturbance_integral_20':coarse,
            'summed_disturbance_integral_32':fine,
            'quadrature_difference':quadrature_delta,
            'global_trivial_bound':2*kappa*(n-1)*t}


def main():
    start=time.monotonic()
    result={'scope':'Separate cutoff-rotor and finite-chain locality controls; not the original cubic model or observed photons.',
            'diagonal_rotor':diagonal_rotor_control(),
            'chain_rows':[chain_control(n,K,t=t) for n in (3,4,5,6)
                          for K in (0.,3.,30.) for t in (.2,.7)],
            'limitations':['No cubic Gauss law, original path coefficient, weak-field packet or microscopic limit is numerically tested.',
                           'Quadrature refinement and floating-point matrix norms are not interval enclosures.',
                           'Finite chain rows do not establish a uniform large-volume bound or an optimal velocity.'],
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy':np.__version__,'scipy':scipy.__version__,
            'elapsed_seconds':time.monotonic()-start,'all_assertions_passed':True}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'
    Path(__file__).with_name('LOCAL_BACKGROUND_CONTROL_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__': main()
