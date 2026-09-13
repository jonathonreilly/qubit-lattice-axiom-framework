#!/usr/bin/env python3
"""Different implementation: native AP Fourier covariance -> small Fock vectors.

The selected one-particle span contains all field derivatives used before the
fifth D action. Compressing H0 to it therefore preserves these finite moments.
No formal Clifford normal ordering or recurrence helper evaluates the states.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from functools import lru_cache
import hashlib,json,time
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();L=16;shape=(L,)*3;coords=np.indices(shape);M=L**3
    theta=(2*np.pi*coords+np.pi)/L;frequency=2*np.sqrt(np.sum(np.sin(theta)**2,axis=0))
    twist=np.exp(1j*np.pi*np.sum(coords,axis=0)/L)
    def radial(f,power):
        out=twist*np.fft.ifftn(np.fft.fftn(f/twist)*frequency**power)
        return out if np.iscomplexobj(f) else out.real
    def K(f):
        out=np.zeros(shape)
        for ax in range(3):
            sign=(-1.)**np.sum(coords[:ax],axis=0) if ax else 1.
            plus=np.where(coords[ax]==L-1,-1.,1.);minus=np.where(coords[ax]==0,-1.,1.)
            out+=sign*(np.roll(f,-1,axis=ax)*plus-np.roll(f,1,axis=ax)*minus)
        return out
    a=np.zeros(shape);a[0,0,0]=1
    assert np.linalg.norm(K(K(a))+radial(a,2))<1e-12
    radial_moments={r:float(np.mean(frequency**r)) for r in (-2,-1,1,3,5,7,9)}
    # Local even radial moments through6 have no alias on this AP grid.
    from math import comb,factorial
    for n in range(7):
        exact=sum(factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))*comb(2*i,i)*comb(2*j,j)*comb(2*(n-i-j),n-i-j) for i in range(n+1) for j in range(n-i+1))
        assert abs(np.mean(frequency**(2*n))-exact)/(1+exact)<2e-14
    raw=json.loads((HERE/'BLOCK12_MOMENT_FORMULAS.json').read_text());rows=[]
    for kind,sites in {'P':((1,0,0),(0,1,0)),'O':((1,0,0),(L-1,0,0))}.items():
        d=np.zeros(shape);ka=K(a)
        for site in sites:d[site]=ka[site]
        w=-6*K(radial(d,-2));bank=[];aa=a;dd=d
        for n in range(6):bank.extend((aa,dd));aa=K(aa);dd=K(dd)
        bank.append(w);fields=np.stack(bank).reshape(13,M)
        gamma=np.stack([K(radial(f,-1)) for f in bank]).reshape(13,M)
        dot=fields@fields.T;kap=fields@gamma.T;scales=np.sqrt(np.diag(dot))
        scale_matrix=scales[:,None]*scales[None,:];C=(dot+1j*kap)/scale_matrix
        # gamma.T columns are Gamma f_j; the contraction is <f_i,Gamma f_j>.
        # Work with actual positive-frequency one-particle vectors. A Gram
        # eigensolve squares the source condition number unnecessarily.
        physical=(fields+1j*gamma).T/np.sqrt(2)
        U,singular,Vh=np.linalg.svd(physical/scales[None,:],full_matrices=False)
        keep=singular>max(singular)*1e-10;basis=U[:,keep];rank=int(sum(keep))
        Z=basis.conj().T@physical
        reconstruction=np.linalg.norm((Z.conj().T@Z)/scale_matrix-C)/np.linalg.norm(C)
        assert reconstruction<2e-11,reconstruction
        abs_basis=np.stack([radial(basis[:,j].reshape(shape),1).ravel() for j in range(rank)],axis=1)
        hm=basis.conj().T@abs_basis
        hermitian_error=np.linalg.norm(hm-hm.conj().T)/np.linalg.norm(hm)
        assert hermitian_error<2e-9,hermitian_error
        hm=(hm+hm.conj().T)/2;energies,V=np.linalg.eigh(hm);assert min(energies)>0
        # On all needed derivatives through order4, H0 gamma(f)Omega=i gamma(Kf)Omega.
        commutator_error=max(np.linalg.norm(hm@Z[:,j]-1j*Z[:,j+2])/(1+np.linalg.norm(Z[:,j+2])) for j in range(10))
        commutator_error=max(commutator_error,np.linalg.norm(hm@Z[:,12]-6j*Z[:,1])/(1+6*np.linalg.norm(Z[:,1])))
        assert commutator_error<2e-8,commutator_error
        Z=V.conj().T@Z;dimension=1<<rank;indices=np.arange(dimension);mode_data=[];energy=np.zeros(dimension)
        for j,e in enumerate(energies):
            low=indices[(indices&(1<<j))==0];high=low+(1<<j)
            signs=np.array([(-1)**int(i&((1<<j)-1)).bit_count() for i in low])
            mode_data.append((low,high,signs));energy+=e*((indices>>j)&1)
        def majorana(vector,state):
            out=np.zeros(dimension,dtype=complex)
            for coefficient,(low,high,signs) in zip(vector,mode_data):
                out[high]+=coefficient*signs*state[low]
                out[low]+=np.conjugate(coefficient)*signs*state[high]
            return out
        def D(state):return energy*state+1j*majorana(Z[:,0],majorana(Z[:,1],state))
        vacuum=np.zeros(dimension,dtype=complex);vacuum[0]=1
        maximum=0.;checks=[]
        local={s.Symbol('A0'):radial_moments[-2],s.Symbol('C0'):radial_moments[-1]}
        local.update({s.Symbol('L'+str(r)):radial_moments[r] for r in (1,3,5,7,9)})
        for source,initial in (('vacuum',vacuum),('ward',majorana(Z[:,12],vacuum))):
            states=[initial]
            for _ in range(5):states.append(D(states[-1]))
            for n in range(11):
                actual=np.vdot(states[n//2],states[n-n//2])
                expected=float(s.sympify(raw['moments'][kind][source][n]).subs(local))
                error=abs(actual-expected)/(1+abs(expected));maximum=max(maximum,error)
                assert error<2e-8,(kind,source,n,error,actual,expected)
                checks.append({'source':source,'order':n,'scaled_error':error})
        rows.append({'class':kind,'modes':rank,'Fock_dimension':dimension,'Gram_reconstruction_error':reconstruction,
                     'free_generator_hermiticity_error':hermitian_error,'free_commutator_error':commutator_error,
                     'max_moment_scaled_error':maximum,'checks':checks})
    return {'status':'passed','finite_AP_L':L,'moment_checks':44,'rows':rows,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'formula_sha256':hashlib.sha256((HERE/'BLOCK12_MOMENT_FORMULAS.json').read_bytes()).hexdigest(),
            'scope':'different finite native Fock implementation checks the moment identities; infinite gap/scalar truth remains conditional, independent human/source review pending'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_NATIVE_FOCK_MOMENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    for row in result['rows']:print(row['class'],'modes',row['modes'],'max_error',row['max_moment_scaled_error'])
    print('checks',result['moment_checks'],'seconds',result['seconds'])
