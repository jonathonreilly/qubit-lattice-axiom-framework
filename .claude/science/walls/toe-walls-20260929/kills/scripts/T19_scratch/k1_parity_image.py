"""Kill check K1: do the SAT models of Test A encode BOTH fermion-parity sectors?
For an exact encoding of the even Majorana algebra on the full Fock space, the total fermion parity
P ~ prod_{u != ref} a_u (up to phase) must map to a NON-identity Pauli (traceless), otherwise the
n-qubit space carries only one parity sector twice.  We test the SAT models the attacker reports."""
import sys, itertools, numpy as np
import sat_lemmaS as M

def parity_image(dims, r):
    out = M.solve(dims, r)
    if out[0] != 'SAT': return out[0], None
    n = int(np.prod(dims)); coords = list(itertools.product(*[range(d) for d in dims]))
    model = out[3]; nmaj = 2*n
    tot = np.zeros(2*n, dtype=np.uint8)
    for u in range(1, nmaj):
        for q in range(n):
            for t in (0,1):
                if model[(u,q,t)]: tot[t*n+q] ^= 1
    return 'SAT', int(tot.sum())

if __name__ == '__main__':
    for spec, r in [((4,),0), ((8,),0), ((2,2),1), ((2,3),1), ((3,3),1), ((3,4),1), ((4,4),2)]:
        st, w = parity_image(spec, r)
        print(spec, 'r=%d'%r, st, 'weight of prod a_u (0 => parity image is identity) =', w, flush=True)
