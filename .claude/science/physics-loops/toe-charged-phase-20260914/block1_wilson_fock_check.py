"""The two-orbital Wilson carrier, full CAR signs and modulo-Gauss sectors."""
from pathlib import Path
import itertools,json
import numpy as np
from scipy.linalg import expm

def second_quantize(h):
    n=h.shape[0];out=np.zeros((2**n,2**n),complex)
    for f in range(2**n):
        for j in range(n):
            if not (f>>j)&1:continue
            f1=f^(1<<j);sg1=(-1)**((f&((1<<j)-1)).bit_count())
            for i in range(n):
                if (f1>>i)&1 or abs(h[i,j])==0:continue
                f2=f1|(1<<i);sg2=(-1)**((f1&((1<<i)-1)).bit_count())
                out[f2,f]+=sg1*sg2*h[i,j]
    return out

sx=np.array([[0,1],[1,0]],complex);sz=np.diag([1.,-1.]);onsite=2.6*sz;hop=(-sz-1j*sx)/2*np.exp(-.7j);beta=.49;rate=.37;r=.6
out=[]
for N in [3,5]:
    om=np.exp(2j*np.pi/N);X=np.roll(np.eye(N),1,axis=0);hs=[];blocks=[]
    for q in range(N):
        h=r*np.block([[onsite,hop*om**q],[hop.conj().T*om**(-q),onsite]])
        hs.append(h);blocks.append(second_quantize(np.block([[h,np.zeros((4,4))],[np.zeros((4,4)),h.conjugate()]])))
    charges=[];valid=[]
    for f in range(256):
        ns=[(f>>i)&1 for i in range(8)]
        q0=sum(ns[:2])-sum(ns[4:6]);q1=sum(ns[2:4])-sum(ns[6:])
        charges.append((q0,q1))
        if (q0+q1)%N==0:valid.append(f)
    Q=np.zeros((N*256,len(valid)),complex)
    for j,f in enumerate(valid):
        for q in range(N):Q[q*256+f,j]=om**(charges[f][0]*q)/np.sqrt(N)
    assert np.linalg.norm(Q.conj().T@Q-np.eye(len(valid)))<1e-12
    He=np.kron(rate*(2*np.eye(N)-X-X.T),np.eye(256));Hm=np.zeros_like(He,dtype=complex)
    for q in range(N):Hm[q*256:(q+1)*256,q*256:(q+1)*256]=blocks[q]
    er=Q.conj().T@He@Q;mr=Q.conj().T@Hm@Q
    assert np.linalg.norm(He@Q-Q@er)<1e-11
    assert np.linalg.norm(Hm@Q-Q@mr)<1e-11
    for site,d in enumerate([1,-1]):
        rg=np.diag([om**z[site] for z in charges]);GG=np.kron(np.linalg.matrix_power(X,d),rg)
        assert np.linalg.norm(GG@Q-Q)<1e-11
    data={'N':N,'full_dimension':N*256,'physical_dimension':len(valid),'nonzero_integer_total_charge_states':sum(sum(charges[f])!=0 for f in valid),'traces':[]}
    for M in [1,2,3]:
        dt=beta/M;K=expm(-dt*rate*(2*np.eye(N)-X-X.T));A=[expm(-dt*h) for h in hs]
        direct=np.trace(np.linalg.matrix_power(expm(-dt*er)@expm(-dt*mr),M));total=0
        for s in itertools.product(range(N),repeat=2):
            R=np.diag(np.repeat(om**np.array(s),2));shift=s[0]-s[1]
            for qs in itertools.product(range(N),repeat=M):
                B=np.eye(4,dtype=complex)
                for q in qs:B=A[q]@B
                w=K[(qs[0]-shift)%N,qs[-1]]
                for j in range(M-1):w*=K[qs[j+1],qs[j]]
                total+=w*abs(np.linalg.det(np.eye(4)+R@B))**2/N**2
        assert abs(direct-total)<1e-10*max(1,abs(direct))
        data['traces'].append({'M':M,'full_Fock_projected_trace':direct.real,'history_sum':total,'relative_error':abs(direct-total)/abs(direct)})
    out.append(data)
Path(__file__).with_name('BLOCK1_WILSON_FOCK_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
for z in out:print(z)
