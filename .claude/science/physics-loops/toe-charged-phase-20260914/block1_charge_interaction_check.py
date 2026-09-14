"""Exact discrete charge-field decomposition versus full projected Fock trace."""
from pathlib import Path
import itertools,json
import numpy as np
from scipy.linalg import expm
from block1_positive_trace_check import annihilator
N=3;beta=.63;tel=.39;u=np.array([.7,1.1]);omega=np.exp(2j*np.pi/N)
X=np.roll(np.eye(N),1,axis=0);aa=[annihilator(i,4) for i in range(4)];num=[a.conj().T@a for a in aa]
Q=[num[0]-num[2],num[1]-num[3]];uf=sum(u[i]*Q[i]@Q[i]/2 for i in range(2));HU=np.kron(np.eye(N),uf)
He=np.kron(tel*(2*np.eye(N)-X-X.T),np.eye(16));hs=[];Hm=np.zeros_like(He,dtype=complex)
for q in range(N):
    h=np.array([[.23,(.6+.29j)*omega**q],[(.6-.29j)*omega**(-q),-.41]])
    hs.append(h);Hm[q*16:(q+1)*16,q*16:(q+1)*16]=sum(h[i,j]*aa[i].conj().T@aa[j]+h[i,j].conjugate()*aa[i+2].conj().T@aa[j+2] for i in range(2) for j in range(2))
G=[np.kron(np.linalg.matrix_power(X,d),expm(2j*np.pi*Q[j]/N)) for j,d in enumerate([1,-1])]
P=sum(np.linalg.matrix_power(G[0],s0)@np.linalg.matrix_power(G[1],s1) for s0,s1 in itertools.product(range(N),repeat=2))/N**2
exact=np.trace(P@expm(-beta*(He+HU+Hm)));out=[]
for M in [1,2,3]:
    dt=beta/M;theta=np.arccos(np.exp(-dt*u/2));A=[expm(-dt*h) for h in hs];K=expm(-dt*tel*(2*np.eye(N)-X-X.T))
    for j in range(2):
        assert np.linalg.norm(expm(-dt*u[j]*Q[j]@Q[j]/2)-(expm(1j*theta[j]*Q[j])+expm(-1j*theta[j]*Q[j]))/2)<1e-12
    HS=[np.diag(np.exp(1j*theta*np.array(z))) for z in itertools.product([-1,1],repeat=2)]
    direct=np.trace(P@np.linalg.matrix_power(expm(-dt*(He+HU))@expm(-dt*Hm),M));total=0;smallest=1e9
    for s0,s1 in itertools.product(range(N),repeat=2):
        R=np.diag([omega**s0,omega**s1]);shift=s0-s1
        for qs in itertools.product(range(N),repeat=M):
            scalar=K[(qs[0]-shift)%N,qs[-1]]
            for j in range(M-1):scalar*=K[qs[j+1],qs[j]]
            for fields in itertools.product(range(4),repeat=M):
                B=np.eye(2,dtype=complex)
                for q,field in zip(qs,fields):B=HS[field]@A[q]@B
                weight=scalar*abs(np.linalg.det(np.eye(2)+R@B))**2/(N*N*4**M)
                total+=weight;smallest=min(smallest,weight)
    assert abs(direct-total)<5e-11
    out.append({'M':M,'operator_trace':direct.real,'positive_HS_sum':total,'difference':abs(direct-total),'minimum_weight':smallest,'trotter_error':abs(direct-exact)})
Path(__file__).with_name('BLOCK1_CHARGE_INTERACTION_CHECK.json').write_text(json.dumps({'exact_Gibbs_partition':exact.real,'u':u.tolist(),'cases':out},indent=2)+'\n')
for z in out:print(z)
