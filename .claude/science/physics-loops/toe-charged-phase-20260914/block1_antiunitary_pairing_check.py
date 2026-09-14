"""Fock-space challenge of the actual antiunitary and neutral pairing."""
from pathlib import Path
from itertools import combinations
import json
import numpy as np
from scipy.linalg import expm

def annihilator(mode,nmodes):
    a=np.zeros((2**nmodes,2**nmodes),complex)
    for n in range(2**nmodes):
        if (n>>mode)&1:
            a[n^(1<<mode),n]=(-1)**((n&((1<<mode)-1)).bit_count())
    return a

def second_quantization(u):
    n=len(u); ans=np.zeros((2**n,2**n),complex)
    for k in range(n+1):
        for rows in combinations(range(n),k):
            for cols in combinations(range(n),k):
                i=sum(1<<x for x in rows);j=sum(1<<x for x in cols)
                ans[i,j]=np.linalg.det(u[np.ix_(rows,cols)])
    return ans

m=2;cs=[annihilator(i,2*m) for i in range(2*m)]
nums=[c.conj().T@c for c in cs]
Q=sum(nums[:m])-sum(nums[m:]);nt=sum(nums)
r=np.block([[np.zeros((m,m)),np.eye(m)],[-np.eye(m),np.zeros((m,m))]])
f=second_quantization(r);parity=np.diag([(-1)**n.bit_count() for n in range(2**(2*m))])
h=np.array([[.31,.4+.7j],[.4-.7j,-.62]])
hn=sum(h[i,j]*cs[i].conj().T@cs[j]+h[i,j].conjugate()*cs[i+m].conj().T@cs[j+m] for i in range(m) for j in range(m))
create=sum(cs[i].conj().T@cs[i+m].conj().T for i in range(m));pair=.23*(create+create.conj().T)
metrics={
 'fock_antiunitary_square_parity_error':np.linalg.norm(f@f.conjugate()-parity),
 'normal_antiunitary_error':np.linalg.norm(f@hn.conjugate()@f.conj().T-hn),
 'pair_antiunitary_error':np.linalg.norm(f@pair.conjugate()@f.conj().T-pair),
 'pair_charge_commutator':np.linalg.norm(Q@pair-pair@Q),
 'pair_number_commutator':np.linalg.norm(nt@pair-pair@nt),
}
for phi in [.3,1.7]:
 g=expm(1j*phi*Q)
 assert np.linalg.norm(f@g.conjugate()@f.conj().T-g)<1e-12
for key in ['fock_antiunitary_square_parity_error','normal_antiunitary_error','pair_antiunitary_error','pair_charge_commutator']:
 assert metrics[key]<1e-12
assert metrics['pair_number_commutator']>.5
Path(__file__).with_name('BLOCK1_ANTIUNITARY_PAIRING_CHECK.json').write_text(json.dumps(metrics,indent=2)+'\n')
print(metrics)
