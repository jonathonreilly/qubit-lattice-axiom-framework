"""Exact 4x4 Clifford basis map and two-dimer bond checks."""
import numpy as np,json
from pathlib import Path
I=np.eye(2,dtype=complex); X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex)
k=np.kron
# columns encode |t,r> -> physical |z1=t,z2=t xor r>.
U=np.zeros((4,4))
for t in range(2):
 for r in range(2):U[2*t+(t^r),2*t+r]=1
actual=[U.T@k(A,I)@U for A in (X,Y,Z)]+[U.T@k(I,A)@U for A in (X,Y,Z)]
expected=[k(X,X),k(Y,X),k(Z,I),k(I,X),k(Z,Y),k(Z,Z)]
assert all(np.array_equal(a,b) for a,b in zip(actual,expected))
assert np.array_equal(actual[0]@actual[3],k(X,I))
# Two separate neighboring dimers: all inter-dimer terms remain explicitly.
checks={
 'inter_x':(k(actual[3],actual[0]),k(k(I,X),k(X,X))),
 'y_first':(k(actual[1],actual[1]),k(k(Y,X),k(Y,X))),
 'y_second':(k(actual[4],actual[4]),k(k(Z,Y),k(Z,Y))),
 'z_first':(k(actual[2],actual[2]),k(k(Z,I),k(Z,I))),
 'z_second':(k(actual[5],actual[5]),k(k(Z,Z),k(Z,Z)))}
assert all(np.array_equal(a,b) for a,b in checks.values())
result=dict(single_site_maps=['X1=tx rx','Y1=ty rx','Z1=tz','X2=rx','Y2=tz ry','Z2=tz rz'],bond_checks=list(checks),exact=True,scope='Unitary regrouping of two original sites, not two qubits per physical site or a projection')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
