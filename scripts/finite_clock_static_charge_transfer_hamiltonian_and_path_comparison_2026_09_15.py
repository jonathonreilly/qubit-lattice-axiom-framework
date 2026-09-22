#!/usr/bin/env python3
"""Author finite checks for static charged transfer constructions.
All fixtures are internal; the only file read is this source for integrity.
Infinite-volume and Hilbert-space statements require independent review.
"""
AUDIT_TIMEOUT_SEC = 300

from pathlib import Path
import hashlib,itertools,json
import numpy as np
from scipy.special import logsumexp

def check_inverse_moments():
    cases=[]
    for N,beta in [(2,.3),(2,.85),(3,.4),(3,1.1),(4,.8)]:
        config=np.array(list(itertools.product(range(N),repeat=4)))
        count=len(config)
        theta=2*np.pi*np.arange(N)/N
        w=np.exp(logsumexp(-beta*(theta[:,None]+2*np.pi*np.arange(-10,11))**2/2,axis=1))
        coeff=np.fft.fft(w).real/N
        assert np.max(abs(np.fft.fft(w).imag))/N<1e-13 and coeff.min()>0
        ks=np.arange(-50,51)
        alias=np.array([np.exp(-ks[ks%N==k]**2/(2*beta)).sum() for k in range(N)])
        assert np.max(abs(coeff/coeff[0]-alias/alias[0]))<3e-13
        # Nonconstant spatial weight, as in a physical spatial square.
        V=w[config.sum(axis=1)%N];root=np.sqrt(V)
        diff=(config[:,None,:]-config[None,:,:])%N
        C=np.prod(w[diff],axis=2)/count
        T=root[:,None]*C*root[None,:]
        eig,vec=np.linalg.eigh(T);largest=eig[-1];Omega=vec[:,-1]
        if Omega.sum()<0:Omega=-Omega
        assert Omega.min()>0 and eig[0]>0
        # Product characters diagonalize C independently of eigh(T).
        fourier=np.exp(2j*np.pi*(config@config.T)/N)/np.sqrt(count)
        ceig=np.prod(coeff[config],axis=1)
        assert np.linalg.norm(C@fourier-fourier*ceig[None,:])<2e-12
        for j in [np.array([q,0,0,0]) for q in (0,1,N-1,N)]+[np.array([1,1,0,0]),np.ones(4,dtype=int)]:
            phase=np.exp(2j*np.pi*(config@j)/N);psi=phase*Omega
            ratios=coeff[config]/coeff[(config+j)%N]
            K=float(np.prod([max(coeff/coeff[(np.arange(N)+int(q))%N]) for q in j]))
            assert K>=1-1e-13 and abs(K-ratios.prod(axis=1).max())<2e-11*max(1,K)
            inverse=largest*float(np.vdot(psi,np.linalg.solve(T,psi)).real)
            spectral=float(np.sum(abs(vec.conj().T@psi)**2*largest/eig))
            assert abs(inverse-spectral)<3e-9*max(1,inverse)
            assert inverse<=K*(1+3e-10) and inverse>=1-3e-10
            # Whitened C-inverse comparison has exactly the local ratios.
            cinv=(fourier/ceig[None,:])@fourier.conj().T
            csqrt=(fourier*np.sqrt(ceig)[None,:])@fourier.conj().T
            shifted=np.conj(phase)[:,None]*cinv*phase[None,:]
            whitened=csqrt@shifted@csqrt
            high=float(np.linalg.eigvalsh(whitened)[-1])
            assert abs(high-K)<3e-9*max(1,K)
            weights=abs(vec.conj().T@psi)**2;energies=-np.log(eig/largest)
            moments=[float(np.sum(weights*energies**p)) for p in (1,2,3)]
            for p,moment in zip((1,2,3),moments):
                import math
                assert moment<=math.factorial(p)*K*(1+3e-10)
            if np.all(j%N==0):assert abs(inverse-1)<3e-10 and abs(K-1)<1e-13
            cases.append({'N':N,'beta':beta,'j':j.tolist(),'dimension':count,'K':K,'inverse_moment':inverse,
                'spectral_inverse_moment':spectral,'direct_spectral_relative_error':abs(inverse-spectral)/max(1,inverse),
                'whitened_comparison_norm':high,'energy_moments_1_2_3':moments})
    # A zero-shift comparison K=1 is actually false for a charged insertion.
    assert max(x['inverse_moment'] for x in cases)>1.1
    result={'status':'personal_floating_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'cases':cases,'limits':'Finite floating comparisons, no interval proof of matrix positivity or infinite-volume passage.'}
    return result

from pathlib import Path
import hashlib,itertools,json
import numpy as np

def check_positive_paths():
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
    return result

from pathlib import Path
import hashlib,itertools,json
import numpy as np

def check_mixed_moments():
    D=np.zeros((4,4),dtype=int)
    for e in range(4):D[e,e]=-1;D[e,(e+1)%4]=1
    j=np.array([1,0,0,0]);loop=np.ones(4,dtype=int)
    paths=[j,j-loop,j+2*loop]
    assert all(np.array_equal(D.T@v,D.T@j) for v in paths)
    rows=[]
    for N,beta in [(2,.4),(3,.6),(4,.8)]:
        config=np.array(list(itertools.product(range(N),repeat=4)));count=len(config)
        angles=2*np.pi*np.arange(N)/N
        w=np.sum(np.exp(-beta*(angles[:,None]+2*np.pi*np.arange(-10,11))**2/2),axis=1)
        V=w[config.sum(axis=1)%N];root=np.sqrt(V)
        diff=(config[:,None,:]-config[None,:,:])%N
        C=np.prod(w[diff],axis=2)/count
        T=root[:,None]*C*root[None,:]
        eigen,vec=np.linalg.eigh(T);lam=eigen[-1];Omega=vec[:,-1]
        if Omega.sum()<0:Omega=-Omega
        tau=T/lam
        # Explicit temporal-link integration with the common charge profile.
        K=np.zeros_like(C,dtype=complex)
        wrong=np.zeros_like(C,dtype=complex)
        for eta in config:
            shift=D@eta
            term=np.prod(w[(diff+shift)%N],axis=2)/count
            K+=term*np.exp(-2j*np.pi*(j@shift)/N)/count
            wrong+=term/count
        charged=root[:,None]*K*root[None,:]/lam
        wrong=root[:,None]*wrong*root[None,:]/lam
        columns=np.column_stack([np.exp(2j*np.pi*(config@path)/N)*Omega for path in paths])
        mixed=[]
        for n in range(7):
            direct=columns.conj().T@np.linalg.matrix_power(charged,n)@columns
            temporal=columns.conj().T@np.linalg.matrix_power(tau,n)@columns
            discrepancy=float(np.max(abs(direct-temporal)))
            assert discrepancy<4e-12
            mixed.append(temporal)
        size=9
        gram=np.empty((size,size),dtype=complex);shifted=gram.copy();shifted_twice=gram.copy()
        for a in range(size):
            m,i=divmod(a,3)
            for b in range(size):
                n,k=divmod(b,3)
                gram[a,b]=mixed[m+n][i,k]
                shifted[a,b]=mixed[m+n+1][i,k]
                shifted_twice[a,b]=mixed[m+n+2][i,k]
        bounds={name:float(np.linalg.eigvalsh(A)[0]) for name,A in
            [('gram',gram),('positive_shift',shifted),('contractive_form',gram-shifted),('contractive_norm',gram-shifted_twice)]}
        assert min(bounds.values())>-5e-12
        # A literal generator realization is separately constructed by powers.
        vectors=np.column_stack([np.linalg.matrix_power(tau,m)@columns[:,i] for m in range(3) for i in range(3)])
        assert np.max(abs(vectors.conj().T@vectors-gram))<4e-12
        # Removing the temporal charge phases changes the actual mixed kernel.
        wrong_value=columns.conj().T@wrong@columns
        fault=float(np.max(abs(wrong_value-mixed[1])))
        assert fault>1e-4
        rho=D.T@j;charge_error=0.
        for vertex in range(4):
            eta=np.eye(4,dtype=int)[vertex]
            index=np.ravel_multi_index(((config+D@eta)%N).T,(N,)*4)
            expect=np.exp(2j*np.pi*(rho@eta)/N)*columns
            charge_error=max(charge_error,float(np.max(abs(columns[index]-expect))))
        assert charge_error<4e-12
        alias=np.exp(2j*np.pi*(config@(j+N*loop))/N)*Omega
        assert np.max(abs(alias-columns[:,0]))<4e-12
        rows.append({'N':N,'beta':beta,'dimension':count,'paths':[x.tolist() for x in paths],
            'gram_dimension':size,'minimum_eigenvalues':bounds,'wrong_temporal_phase_effect':fault,
            'maximum_gauge_character_error':charge_error,
            'mixed_moments':[[[{'real':float(z.real),'imag':float(z.imag)} for z in row] for row in M] for M in mixed]})
    result={'status':'personal_finite_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'cases':rows,'limits':'Floating finite matrices; the common infinite-space construction and threshold proof are analytic.'}
    return result

def general_path_green():
    rows=[]
    paths=[[(0,(0,0,0)),(0,(1,0,0)),(1,(2,0,0))],
           [(1,(0,0,0)),(0,(0,1,0)),(0,(1,1,0))]]
    for size in (24,40,64):
        grid=2*np.pi*(np.arange(size)+.5)/size-np.pi
        ks=np.stack(np.meshgrid(grid,grid,grid,indexing='ij'),axis=-1)
        d=np.exp(-1j*ks)-1;lam=np.sum(abs(d)**2,axis=-1)
        root=np.sqrt(lam*(lam+4));decay=2/(lam+2+root)
        g0=1/root
        rho_expected=np.exp(-1j*(2*ks[...,0]+ks[...,1]))-1
        for index,path in enumerate(paths):
            eta=np.zeros(ks.shape,dtype=complex)
            for direction,position in path:
                eta[...,direction]+=np.exp(-1j*np.sum(ks*np.array(position),axis=-1))
            rho=np.sum(d*eta,axis=-1)
            assert np.max(abs(rho-rho_expected))<4e-15
            norm=np.sum(abs(eta)**2,axis=-1);longitudinal=abs(rho)**2/lam
            assert np.min(norm-longitudinal)>-3e-14
            static=float(np.mean(longitudinal));last=None
            for time in (1,2,5,12):
                direct_time=sum(decay**abs(a-b)*g0 for a in range(time) for b in range(time))
                direct=float(np.mean(abs(rho)**2*direct_time+2*norm*g0*(1-decay**time)))
                end=float(np.mean(2*g0*(1-decay**time)*(norm-longitudinal)))
                reduced=time*static+end
                assert abs(direct-reduced)<3e-12*max(1,direct)
                assert 0<=end<=2*len(path)**2*float(np.mean(g0))+3e-12
                if last is not None:assert reduced/time<last
                last=reduced/time
                rows.append({'grid_side':size,'path_index':index,'T':time,'direct_time_sum':direct,
                    'reduced_energy':reduced,'static_limit':static,'positive_remainder':end})
    return rows


def main():
    result={'inverse_moments':check_inverse_moments(),'positive_paths':check_positive_paths(),
            'mixed_moments':check_mixed_moments(),'general_path_green':general_path_green()}
    print('EVIDENCE_JSON: '+json.dumps(result,sort_keys=True))
    print('per_element: clock Fourier aliases, coefficient ratios and inverse moments are evaluated at finite N and beta.')
    print('per_site: actual temporal-link gauge sums are matched to same-charge insertion matrix elements on spatial squares.')
    print('per_mode: finite inverse spectra, positive insertion vectors and moment Gram contractions are compared independently.')
    print('per_block: fixed spatial surfaces and general path Green energies are checked on finite Fourier and transfer fixtures.')
    print('lattice_wide: checked and not executed — common Hilbert reconstruction, no zero atom and infinite static thresholds use the written proofs.')
    print('TOTAL: PASS=4 FAIL=0')
if __name__=='__main__':main()
