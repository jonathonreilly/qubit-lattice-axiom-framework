#!/usr/bin/env python3
"""Mixed static kernels: direct temporal gauge sums and moment Gram matrices."""
from pathlib import Path
import hashlib,itertools,json
import numpy as np

def main():
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
    dest=Path(__file__).with_name('BLOCK34_MIXED_STATIC_TRANSFER_CHECKS.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(rows),'max_gram_negative_roundoff':min(min(r['minimum_eigenvalues'].values()) for r in rows),'output':str(dest)}))
if __name__=='__main__':main()
