"""Independent full-Fock versus phase-history determinant challenge; exploratory."""
from pathlib import Path
import itertools,json
import numpy as np
from scipy.linalg import expm


def annihilator(mode,nmodes):
    a=np.zeros((2**nmodes,2**nmodes),complex)
    for n in range(2**nmodes):
        if (n>>mode)&1:
            a[n^(1<<mode),n]=(-1)**((n&((1<<mode)-1)).bit_count())
    return a


def fixture(N,beta=.71,tel=.43):
    X=np.roll(np.eye(N),1,axis=0);om=np.exp(2j*np.pi/N)
    Z=np.diag(om**np.arange(N));a=[annihilator(i,4) for i in range(4)]
    num=[z.conj().T@z for z in a];Q=[num[0]-num[2],num[1]-num[3]]
    He=np.kron(tel*(2*np.eye(N)-X-X.T),np.eye(16))
    h=[];hm=[]
    for q in range(N):
        hp=np.array([[.31,(.8+.37j)*om**q],[(.8-.37j)*om**(-q),-.67]])
        h.append(hp)
        block=sum(hp[i,j]*a[i].conj().T@a[j]+hp[i,j].conjugate()*a[i+2].conj().T@a[j+2] for i in range(2) for j in range(2))
        hm.append(block)
    Hm=np.zeros_like(He,dtype=complex)
    for q,block in enumerate(hm):Hm[q*16:(q+1)*16,q*16:(q+1)*16]=block
    gam=[np.kron(np.linalg.matrix_power(X,d),expm(2j*np.pi*Q[x]/N)) for x,d in enumerate([1,-1])]
    P=sum(np.linalg.matrix_power(gam[0],s0)@np.linalg.matrix_power(gam[1],s1) for s0,s1 in itertools.product(range(N),repeat=2))/N**2
    assert np.linalg.norm(P@P-P)<1e-12
    assert np.linalg.norm(P-P.conj().T)<1e-12
    for G in gam:
        assert np.linalg.norm(G@Hm-Hm@G)<1e-12
        assert np.linalg.norm(G@He-He@G)<1e-12
    H=He+Hm
    exact=np.trace(P@expm(-beta*H))
    out={'N':N,'physical_dimension':round(np.trace(P).real),'exact_partition':exact.real,'slices':[]}
    assert abs(exact.imag)<1e-12
    for M in [1,2,3,4]:
        delta=beta/M;K=expm(-delta*tel*(2*np.eye(N)-X-X.T));A=[expm(-delta*x) for x in h]
        assert K.min()>=0 and np.linalg.norm(K.sum(axis=0)-1)<1e-12
        T=expm(-delta*He)@expm(-delta*Hm)
        direct=np.trace(P@np.linalg.matrix_power(T,M))
        terms=[];maxsinglephase=0;badcomplex=0;badtotal=0j
        for s0,s1 in itertools.product(range(N),repeat=2):
            R=np.diag([om**s0,om**s1]);shift=s0-s1
            for qs in itertools.product(range(N),repeat=M):
                B=np.eye(2,dtype=complex)
                for q in qs:B=A[q]@B
                detplus=np.linalg.det(np.eye(2)+R@B)
                detminus=np.linalg.det(np.eye(2)+(R@B).conjugate())
                assert abs(detminus-detplus.conjugate())<1e-12
                maxsinglephase=max(maxsinglephase,abs(detplus.imag))
                end=(qs[0]-shift)%N
                weight=K[end,qs[-1]]
                for j in range(M-1):weight*=K[qs[j+1],qs[j]]
                val=weight*abs(detplus)**2/N**2
                terms.append(val)
                bad=detplus*np.linalg.det(np.eye(2)+R@B.conjugate())
                badcomplex=max(badcomplex,abs(bad.imag));badtotal+=weight*bad/N**2
        measure=sum(terms)
        assert abs(direct-measure)<2e-10
        out['slices'].append({'M':M,'operator_trace':direct.real,'positive_history_sum':measure,'min_summand':min(terms),'max_single_species_imaginary_part':maxsinglephase,'wrong_temporal_conjugation_max_imaginary_part':badcomplex,'wrong_temporal_conjugation_total':{'real':badtotal.real,'imag':badtotal.imag},'trotter_error':abs(direct-exact)})
    return out


if __name__=='__main__':
    result=[fixture(N) for N in [3,4,5]]
    p=Path(__file__).with_name('BLOCK1_POSITIVE_TRACE_CHECK.json');p.write_text(json.dumps(result,indent=2)+'\n')
    for r in result:
        print('N',r['N'],'physical_dimension',r['physical_dimension'],'partition',r['exact_partition'])
        for z in r['slices']:print(' slices',z['M'],'trace mismatch',abs(z['operator_trace']-z['positive_history_sum']),'trotter error',z['trotter_error'],'single phase',z['max_single_species_imaginary_part'],'wrong temporal phase',z['wrong_temporal_conjugation_max_imaginary_part'])
