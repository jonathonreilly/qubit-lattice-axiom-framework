#!/usr/bin/env python3
"""Exact finite supplied quartic; integer-complex basis action, no eigensolver."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('docs/EIGHT_MAJORANA_QUARTIC_FINITE_SPECTRUM_NOTE_2026-10-16.md',)
from itertools import combinations

TERMS = [(1,(0,1,2,3)),(1,(0,1,4,5)),(1,(0,1,6,7)),(1,(0,2,4,6)),
         (-1,(0,2,5,7)),(-1,(0,3,4,7)),(-1,(0,3,5,6)),(1,(4,5,6,7)),
         (1,(2,3,6,7)),(1,(2,3,4,5)),(1,(1,3,5,7)),(-1,(1,3,4,6)),
         (-1,(1,2,5,6)),(-1,(1,2,4,7))]

def word(indices, state):
    phase = 1
    for a in reversed(indices):
        j, odd = divmod(a, 2)
        bit = 3-j
        phase *= (-1)**((state >> (bit+1)).bit_count())
        if odd:
            phase *= 1j * (-1)**((state >> bit) & 1)
        state ^= 1 << bit
    return state, phase

def apply(indices, v):
    out = [0]*16
    for state, value in enumerate(v):
        dest, phase = word(indices,state)
        out[dest] += phase*value
    return out

def anti(v):
    return apply((1,3,5,7), [complex(z).conjugate() for z in v])

def omega(v, terms=TERMS):
    out = [0]*16
    for sign, indices in terms:
        for j, value in enumerate(apply(indices,v)):
            out[j] += sign*value
    return out

def expected(v):
    out = [0]*16
    for j in range(16):
        if j.bit_count()==2:out[j]=2*v[j]
    out[0],out[15]=-6*v[0]+8*v[15],8*v[0]-6*v[15]
    return out

def main():
    basis = [[int(i==j) for i in range(16)] for j in range(16)]
    for v in basis:
        assert omega(v)==expected(v)
        assert anti(anti(v))==v
        assert anti(omega(anti(v)))==omega(v)
        for a in range(8):
            assert anti(apply((a,),anti(v)))==apply((a,),v)
            for b in range(8):
                left=apply((a,b),v);right=apply((b,a),v)
                assert [x+y for x,y in zip(left,right)]==[2*int(a==b)*z for z in v]
        for a,b in combinations(range(8),2):
            bil=lambda x:[1j*z for z in apply((a,b),x)]
            assert anti(bil(anti(v)))==[-z for z in bil(v)]
    ground=[1]+[0]*14+[-1]  # unnormalized
    assert omega(ground)==[-14*z for z in ground]
    for a,b in combinations(range(8),2):
        assert sum(x.conjugate()*1j*y for x,y in zip(map(complex,ground),apply((a,b),ground)))==0
    mutated=list(TERMS);mutated[4]=(1,mutated[4][1])
    assert any(omega(v,mutated)!=expected(v) for v in basis)
    print('PASS: all 16 basis columns, 64 Clifford pairs, T squared, T symmetry, all 28 bilinears and sign mutation.')
    print('Spectrum: -14 (1), 0 (8), 2 (7); H=W Omega, W>0: unique ground and gap 14W.')
    print('per_element: exact complete sixteen-dimensional matrix and all twenty-eight bilinear entries')
    print('per_site: one supplied four-qubit cluster with the complete sixteen-dimensional state space')
    print('per_mode: all eight supplied Majorana operators with all sixty-four Clifford pairs')
    print('per_block: full even and odd parity sectors of the supplied sixteen-dimensional Hamiltonian')
    print('lattice_wide: checked and not executed — no lattice theorem is claimed')

if __name__=='__main__':main()
