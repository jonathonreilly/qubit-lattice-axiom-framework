"""Rational witness that an energy filter can destroy newborn orthogonality."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as sy
from filter_controls import pb,first_matrices,HERE


def main():
    assert not (HERE/'EXACT_CROSS_RESULTS.json').exists()
    p,n8,H2,H4,B6,R6=pb.finite_operators(1)
    array=2*(H2.toarray()+4*np.eye(len(p)))+H4.toarray()
    assert np.max(abs(array-np.round(array)))==0
    A=sy.Matrix(array.astype(int));G=(sy.eye(len(p))+A*A).inv()
    B={ch:sy.Matrix(v.astype(int)) for ch,v in first_matrices(1,p).items()}
    assert all(np.max(abs(np.array(B[ch],float)-v))==0 for ch,v in first_matrices(1,p).items())
    GB={ch:G*b for ch,b in B.items()}
    zero=sy.zeros(3)
    unfiltered=sum((B[e,1].T*B[e,-1]+B[e,-1].T*B[e,1] for e in range(8)),zero)
    assert unfiltered==sy.zeros(3)
    difference=sum((GB[e,1].T*GB[e,-1]+GB[e,-1].T*GB[e,1] for e in range(8)),sy.zeros(3))
    cross=GB[0,1].T*GB[0,-1]
    assert cross!=sy.zeros(3) and difference!=sy.zeros(3)
    entries=[{'row_f':i-1,'column_f':j-1,'exact':str(difference[i,j]),
              'decimal':float(difference[i,j])} for i in range(3) for j in range(3) if difference[i,j]!=0]
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'S':1,'K':1,'delta':1,'eta':2,'dimension':len(p),
            'filter':'g(A)=(I+A^2)^(-1), A=H6,S+4 eta I',
            'fixed_edge0_opposite_orientation_cross_gram':[[str(cross[i,j]) for j in range(3)] for i in range(3)],
            'coherent_minus_resolved_loss_without_kappa':entries,
            'unfiltered_coherent_minus_resolved_loss_exactly_zero':True,
            'sharp_window_consequence':'g(x)^2=integral_0^infinity [4r/(1+r^2)^3] 1_(|x|<=r) dr. The exact nonzero filtered-loss difference therefore forces a nonzero difference for at least one centered sharp-window radius at this spin. This is an existence counterexample, not an exact identification of the S2 floating control radius.'}
    (HERE/'EXACT_CROSS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
