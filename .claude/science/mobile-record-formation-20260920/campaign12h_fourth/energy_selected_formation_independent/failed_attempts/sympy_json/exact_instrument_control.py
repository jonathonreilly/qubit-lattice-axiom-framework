"""Exact finite-spin filter countercontrol and first-sector Hamiltonian check."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json
import hashlib
from collections import defaultdict
import sympy as sy
import numpy as np
from filter_controls import pb, fp, first_outputs, first_matrices, q0, HERE


def hop(v, grade, spin=None):
    result=defaultdict(lambda:sy.Integer(0))
    for (q,f),amp in v.items():
        for qq,d,e,k,g in pb.hop_data(q):
            if pb.grade(qq)!=grade:continue
            if spin is None:w=sy.Integer(1)
            else:
                E=f+g
                w=sy.sqrt(1-sy.Rational(E*(E+k),spin*(spin+1))) if abs(E)<=spin and abs(E+k)<=spin else sy.Integer(0)
            result[qq,f+d]-=amp*w
    return {s:sy.simplify(a) for s,a in result.items() if sy.simplify(a)!=0}


def h2(v,spin=None):return {s:-a for s,a in hop(hop(v,1,spin),0,spin).items()}


def h4(v,spin=None):
    out=defaultdict(lambda:sy.Integer(0),h2(h2(v,spin),spin));z=v
    for g in (1,2,1,0):z=hop(z,g,spin)
    for s,a in z.items():out[s]-=a/2
    return {s:sy.simplify(a) for s,a in out.items() if sy.simplify(a)!=0}


def main():
    assert not (HERE/'EXACT_INSTRUMENT_RESULTS.json').exists()
    rows=[]
    for spin in (1,2,4):
        for f in range(-spin,spin+1):
            seed={(q0,f):sy.Integer(1)}
            got=h2(seed,spin);target=-8+sy.Rational(8*f*f,spin*(spin+1))
            assert got=={(q0,f):target}
            assert h4(seed)=={(q0,f):sy.Integer(24)}
            rows.append({'S':spin,'f':f,'H2_exact':str(target),'rotor_H4':24})
    # S1 nonzero link amplitudes are integers, so the following matrix is exact.
    p6,n8,H2,H4,B6,R6=pb.finite_operators(1)
    A=2*(H2.toarray()+4*np.eye(len(p6)))+H4.toarray()
    assert np.max(abs(A-np.round(A)))==0
    A=sy.Matrix(A.astype(int));x=sy.Symbol('x')
    polynomial=A.charpoly(x).as_expr();factors=sy.factor_list(polynomial)[1]
    factor_rows=[{'factor':str(f),'multiplicity':m,'degree':sy.degree(f,x)} for f,m in factors]
    print(json.dumps({'spin1_dimension':len(p6),'exact_shifted_Hamiltonian_factors':factor_rows}),flush=True)
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'first_hamiltonian_checks':rows,'spin1_dimension':len(p6),
            'spin1_parameters':{'K':1,'delta':1,'eta':2},
            'exact_shifted_Hamiltonian_factors':factor_rows}
    (HERE/'EXACT_INSTRUMENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
