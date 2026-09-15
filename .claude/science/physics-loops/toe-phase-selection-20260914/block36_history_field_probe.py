#!/usr/bin/env python3
"""Finite author challenges for the history-field reconstruction; no review verdict."""
from pathlib import Path
import itertools,hashlib,json
import numpy as np

def main():
    rows=[]
    D=np.zeros((4,4),dtype=int)
    for e in range(4):D[e,e]=-1;D[e,(e+1)%4]=1
    j=np.array([1,0,0,0]);loop=np.ones(4,dtype=int);zero=np.zeros(4,dtype=int)
    histories=[ [('u',j)], [('u',j),('t',1),('u',loop)],
        [('u',loop),('t',2),('u',j)], [('u',j),('t',1),('u',-loop),('t',1)],
        [('u',2*j),('t',1),('u',-j)], [], [('u',loop),('t',1),('u',-loop)],
        [('u',-j),('t',1),('u',j)], [('u',j),('t',2),('u',j)] ]
    for N,beta in [(2,.4),(3,.6),(4,.8)]:
        a=np.array(list(itertools.product(range(N),repeat=4)));count=len(a)
        angles=2*np.pi*np.arange(N)/N
        weight=np.exp(-beta*(angles[:,None]+2*np.pi*np.arange(-10,11))**2/2).sum(axis=1)
        coeff=np.fft.fft(weight).real/N;assert coeff.min()>0
        delta=(a[:,None,:]-a[None,:,:])%N
        C=np.prod(weight[delta],axis=2)/count
        root=np.sqrt(weight[a.sum(axis=1)%N]);T=root[:,None]*C*root[None,:]
        eig,vec=np.linalg.eigh(T);lam=eig[-1];Omega=vec[:,-1]
        if Omega.sum()<0:Omega=-Omega
        assert Omega.min()>0 and eig[0]>0
        tau=T/lam
        projected={}
        def temporal(rho):
            key=tuple(rho%N)
            if key not in projected:
                value=np.zeros_like(C,dtype=complex)
                for eta in a:
                    kernel=np.prod(weight[(delta+D@eta)%N],axis=2)/count
                    value+=kernel*np.exp(-2j*np.pi*(rho@eta)/N)/count
                projected[key]=root[:,None]*value*root[None,:]/lam
            return projected[key]
        cols=[];profiles=[];checks=[]
        for index,history in enumerate(histories):
            original=Omega.astype(complex);direct=original.copy();wrong=original.copy();rho=zero.copy()
            for kind,arg in history:
                if kind=='u':
                    phase=np.exp(2j*np.pi*(a@arg)/N)
                    original*=phase;direct*=phase;wrong*=phase;rho+=D.T@arg
                else:
                    original=np.linalg.matrix_power(tau,arg)@original
                    direct=np.linalg.matrix_power(temporal(rho),arg)@direct
                    wrong=np.linalg.matrix_power(temporal(zero),arg)@wrong
            discrepancy=float(np.max(abs(original-direct)));assert discrepancy<3e-12
            cols.append(original);profiles.append(rho%N)
            final=history[-1][1] if history and history[-1][0]=='u' else zero
            K=float(np.prod([max(coeff/coeff[(np.arange(N)+int(q))%N]) for q in final]))
            norm=float(np.vdot(original,original).real)
            inverse=float(np.vdot(original,np.linalg.solve(tau,original)).real)
            spectral=float(np.sum(abs(vec.conj().T@original)**2*lam/eig))
            assert norm<=1+3e-12 and inverse<=K+3e-10
            assert abs(inverse-spectral)<3e-10*max(1,inverse)
            checks.append({'word':index,'final_insertion':final.tolist(),'charge':(rho%N).tolist(),
                'norm_squared':norm,'inverse_moment':inverse,'K_final_insertion':K,
                'temporal_link_discrepancy':discrepancy,'wrong_neutral_projector_error':float(np.linalg.norm(original-wrong))})
        W=np.column_stack(cols);gram=W.conj().T@W
        field=np.exp(2j*np.pi*(a@(j-loop))/N)
        prefixed=field[:,None]*W
        assert np.max(abs(prefixed.conj().T@prefixed-gram))<3e-12
        lower={'gram':float(np.linalg.eigvalsh(gram)[0]),
            'positive_transfer':float(np.linalg.eigvalsh(W.conj().T@tau@W)[0]),
            'contractive_form':float(np.linalg.eigvalsh(W.conj().T@(np.eye(count)-tau)@W)[0]),
            'contractive_norm':float(np.linalg.eigvalsh(gram-(tau@W).conj().T@(tau@W))[0])}
        assert min(lower.values())>-3e-12
        orthogonal=[]
        for i in range(len(histories)):
            for k in range(i):
                if not np.array_equal(profiles[i],profiles[k]):orthogonal.append(abs(gram[i,k]))
        assert max(orthogonal)<3e-12
        assert max(x['wrong_neutral_projector_error'] for x in checks)>1e-3
        assert checks[0]['inverse_moment']>1.01
        assert checks[3]['K_final_insertion']==1 and checks[3]['inverse_moment']<=1+3e-12
        rows.append({'N':N,'beta':beta,'dimension':count,'histories':checks,
            'gram_lower_eigenvalues':lower,'maximum_distinct_charge_overlap':float(max(orthogonal)),
            'temporal_charge_matrices':len(projected)})
    result={'status':'personal_finite_checks_not_independent_review',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows,
        'limits':'Finite words and explicit temporal sums; no finite check proves cofinal limits, time-zero cyclicity or equality of larger-sector bottoms.'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
