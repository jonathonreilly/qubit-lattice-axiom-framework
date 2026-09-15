#!/usr/bin/env python3
"""Positive Fourier insertion vectors and time-uniform surface comparisons."""
from pathlib import Path
import hashlib,itertools,json
import numpy as np

def main():
    rows=[]
    for N,beta in [(2,.3),(2,1.2),(3,.5),(3,1.4),(4,.8)]:
        configs=np.array(list(itertools.product(range(N),repeat=4)));count=len(configs)
        roots=2*np.pi*np.arange(N)/N
        w=np.sum(np.exp(-beta*(roots[:,None]+2*np.pi*np.arange(-10,11))**2/2),axis=1)
        coeff=np.fft.fft(w).real/N;assert coeff.min()>0
        fourier=np.exp(2j*np.pi*(configs@configs.T)/N)/np.sqrt(count)
        cprod=np.prod(coeff[configs],axis=1);croot=np.sqrt(cprod)
        V=w[configs.sum(axis=1)%N];rootV=np.sqrt(V)
        Vhat=fourier.conj().T@(V[:,None]*fourier)
        assert np.max(abs(Vhat.imag))<2e-13 and Vhat.real.min()>-2e-13
        Vhat=Vhat.real
        C=(fourier*cprod[None,:])@fourier.conj().T
        T=rootV[:,None]*C*rootV[None,:]
        # The exact neutral Fourier sector is ker(d0*) mod N. Restrict
        # before solving: a nearly degenerate full eigensolve contaminated
        # zero charge components at9e-13 in the preserved first fixture.
        D=np.zeros((4,4),dtype=int)
        for edge in range(4):D[edge,edge]=-1;D[edge,(edge+1)%4]=1
        neutral=np.flatnonzero(np.all((configs@D)%N==0,axis=1))
        assert len(neutral)==N
        tilde=croot[:,None]*Vhat*croot[None,:]
        vals,vecs=np.linalg.eigh(tilde[np.ix_(neutral,neutral)])
        lam=vals[-1];neutral_vec=vecs[:,-1]
        if neutral_vec.sum()<0:neutral_vec=-neutral_vec
        Psi=np.zeros(count);Psi[neutral]=neutral_vec
        assert Psi.min()>=0 and Psi[neutral].min()>0
        Omega=rootV*(fourier@(croot*Psi))/np.sqrt(lam)
        assert np.max(abs(Omega.imag))<3e-13 and Omega.real.min()>0
        assert abs(np.linalg.norm(Omega)-1)<3e-13
        assert np.linalg.norm(T@Omega-lam*Omega)<3e-13
        assert abs(lam-np.linalg.eigvalsh(T)[-1])<3e-13
        assert np.linalg.norm(tilde@Psi-lam*Psi)<3e-13
        # One plaquette: b=(1,1,1,1) is its oriented boundary.
        j=np.array([1,0,0,0]);loop=np.ones(4,dtype=int)
        vectors=[];probs=[]
        for charge in (0,1,2):
            path=j-charge*loop
            phase=np.exp(2j*np.pi*(configs@path)/N)
            direct=croot*(fourier.conj().T@(rootV*phase*Omega))
            indexes=np.ravel_multi_index(((configs-path)%N).T,(N,)*4)
            positive=croot*(Vhat@(croot*Psi)[indexes])/np.sqrt(lam)
            assert np.max(abs(direct-positive))<4e-13
            assert np.max(abs(positive.imag))<4e-13 and positive.real.min()>-4e-13
            vectors.append(positive.real)
            values=[]
            for time in (1,2,4,9):
                original=np.vdot(phase*Omega,np.linalg.matrix_power(T/lam,time)@(phase*Omega))
                transformed=np.vdot(positive,np.linalg.matrix_power(tilde/lam,time-1)@positive)/lam
                assert abs(original-transformed)<5e-13
                values.append(float(original.real))
            probs.append(values)
        comparisons=[]
        for shift in (1,2):
            R=float(max(coeff/coeff[(np.arange(N)+shift)%N]))
            v0,v1=vectors[0],vectors[shift]
            assert np.max(v1-R*v0)<4e-13 and np.max(v0/R-v1)<4e-13
            for p0,p1 in zip(probs[0],probs[shift]):
                assert p1<=R*R*p0+5e-13 and p1>=p0/(R*R)-5e-13
            # Check the coefficient fiber bijection directly on the one-face
            # Fourier coefficients, including unsupported noncycle currents.
            coeff_compare=[]
            for q in range(N):
                low=coeff[q]/R;value=coeff[(q-shift)%N];high=coeff[q]*R
                assert low-3e-13<=value<=high+3e-13
                coeff_compare.append([float(low),float(value),float(high)])
            comparisons.append({'surface_multiple':shift,'R':R,'coefficient_bounds':coeff_compare,
                'max_component_difference_if_R_omitted':float(np.max(abs(v1-v0))),
                'path0_W':probs[0],'other_W':probs[shift]})
        rows.append({'N':N,'beta':beta,'dimension':count,'minimum_V_fourier_entry':float(Vhat.min()),
            'minimum_positive_insertion_entry':min(float(v.min()) for v in vectors),'comparisons':comparisons})
    assert max(c['max_component_difference_if_R_omitted'] for r in rows for c in r['comparisons'])>1e-3
    result={'status':'personal_floating_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'cases':rows,'limitations':'Finite matrices and coefficient sums; the general surface bijection and common-space limits are written proofs.'}
    dest=Path(__file__).with_name('BLOCK35_POSITIVE_FOURIER_PATH_CHECKS.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(rows),'comparisons':sum(len(r['comparisons']) for r in rows),'output':str(dest)}))
if __name__=='__main__':main()
