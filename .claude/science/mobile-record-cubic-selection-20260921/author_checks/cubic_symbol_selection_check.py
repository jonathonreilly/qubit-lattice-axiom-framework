"""Exact algebra for additional, explicitly conditional selection premises."""
from pathlib import Path
import hashlib,json
import sympy as s

root=Path(__file__).resolve().parent
x,y,z,a,b,m,u,v=s.symbols('x y z a b m u v',real=True)
q=s.Matrix([x,y,z]);C=s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
D=[s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)]
Q=[]
for i,j in [(0,1),(0,2),(1,2)]:
    M=s.zeros(3);M[i,j]=M[j,i]=1/s.sqrt(2);Q.append(M)
K=s.Matrix.hstack(a*q,b*q,m*C,*[u*d*q for d in D],*[v*t*q for t in Q],s.zeros(3,1))
A=s.zeros(14);A[:3,3:]=K;A[3:,:3]=K.T
T=s.diag(*([-1]*3+[1]*11))
assert T*A*T==-A
assert q.T*C==s.zeros(1,3)
# Exact polynomial equations, including all coefficients in x,y,z.
def equations(matrix):
    out=[]
    for expression in matrix:
        out.extend(s.Poly(s.expand(expression),x,y,z).coeffs())
    return out
other=s.Matrix.hstack(K[:,0:2],K[:,5:])
raw_conditions=s.solve(equations(q.T*other),[a,b,u,v],dict=True)
curl_conditions=s.solve(equations(C*other),[a,b,u,v],dict=True)
assert raw_conditions==[{a:0,b:0,u:0,v:0}]
assert curl_conditions==[{u:0,v:0}]
# Derivative observable map in the same coordinate order as A.
P=s.zeros(6,14);P[:3,5:8]=s.I*C;P[3:,:3]=-s.I*C
G=s.zeros(6);G[:3,3:]=-s.I*m*C;G[3:,:3]=s.I*m*C
residual=(P*(-s.I*A)-G*P).applyfunc(s.expand)
assert residual.subs({u:0,v:0})==s.zeros(6,14)
assert s.solve(equations(residual),[a,b,u,v],dict=True)==[{u:0,v:0}]
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'exact_reversal_identity':True,
        'raw_vector_Gauss_invariant_subspace_conditions':['a1=0','a2=0','u=0','v=0'],
        'curl_readout_closed_conditions':['u=0','v=0'],
        'curl_readout_evolution_residual_exact':True,
        'scope':'Additional premises on the stated linear symbol; no new microscopic constraint, hydrodynamic theorem, state selection or physical Maxwell claim.'}
(root/'CUBIC_SYMBOL_SELECTION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
