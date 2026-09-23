"""Exact physical cube H2 fibers, without importing the ring factorization."""
from pathlib import Path
import importlib.util,hashlib,json,time
import numpy as np
import sympy as sp
D=Path(__file__).resolve().parent
p=D.parent/'second_event_author/second_event_probe.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='4827171a51e018b306302b0fac315c000c63bb7311e69fcab18ad666916f1f25'
s=importlib.util.spec_from_file_location('paths',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
edges,aset=m.graph('cube')
tree=[(0,1),(0,2),(0,4),(1,3),(1,5),(2,6),(3,7)]
chords=[e for e in edges if e not in tree]
assert len(chords)==5
words=m.charges(6)
P=[q for q in words if all(q[a] for a in aset)]
Q=[q for q in words if sum(q[a]==0 for a in aset)==1]
ix={q:i for i,q in enumerate(Q)}
assert (len(P),len(Q))==(36,96)
x=sp.symbols('x')

def exact_matrix(turns):
    n=[0]*12
    for e,v in zip(chords,turns):n[edges.index(e)]=v
    A=sp.zeros(96,36)
    for j,q in enumerate(P):
        for qq,shift in m.legal_hops(q,edges):
            assert m.gauss_difference(q,qq,shift,edges)
            exponent=sum(a*b for a,b in zip(n,shift))%4
            A[ix[qq],j]-=sp.I**exponent
    H=-A.conjugate().T*A
    assert H==H.conjugate().T
    assert all(H[i,i]==-6 for i in range(36))
    return H.applyfunc(sp.expand)

numeric=[]
for values in ([0.]*5,[.19,.53,.87,1.11,1.63],[.41,1.03,1.29,2.17,2.71]):
    theta=np.zeros(12)
    for e,v in zip(chords,values):theta[edges.index(e)]=v
    pw,H,H4,B,G=m.target_matrices('cube',theta)
    vals=np.linalg.eigvalsh(H)
    numeric.append({'chord_angles':values,'H2_eigenvalues':vals.tolist(),
                    'distance_to_diagonal_energy_minus6':float(min(abs(vals+6))),
                    'determinant_H2_plus6':float(np.linalg.det(H+6*np.eye(36)).real)})
rows=[];gcd=None
for turns in [(0,0,0,0,0),(1,0,0,0,0),(1,2,0,1,3),(2,1,3,0,1),(1,1,1,1,1)]:
    start=time.monotonic();H=exact_matrix(turns)
    polynomial=sp.Poly(H.charpoly(x).as_expr(),x,domain=sp.QQ)
    gcd=polynomial if gcd is None else sp.gcd(gcd,polynomial).monic()
    row={'quarter_turns':turns,'characteristic_polynomial_factorization':str(sp.factor(polynomial.as_expr())),
         'characteristic_coefficients':[str(c) for c in polynomial.all_coeffs()],
         'cumulative_gcd':str(sp.factor(gcd.as_expr())),'gcd_degree':gcd.degree(),
         'elapsed_seconds':time.monotonic()-start}
    rows.append(row);print(json.dumps(row),flush=True)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'edges':edges,'tree':tree,'chords':chords,
     'P_words':P,'W1_words':Q,'numeric_fibers':numeric,'exact_rows':rows,
     'final_gcd':str(sp.factor(gcd.as_expr())),'final_gcd_degree':gcd.degree(),
     'scope':'Exact finite-fiber spectral certificate candidate. The physical analytic/direct-integral inference is a separate proof obligation.'}
p=D/'CUBE_POINT_SPECTRUM_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
