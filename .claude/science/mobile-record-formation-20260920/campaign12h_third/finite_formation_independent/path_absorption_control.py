"""Selective exact transient observability check, reusing only own sector builder."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json
import sympy as s
from finite_control import model,effective

p=Path(__file__).resolve().parent
results=[]
for spin in (1,2):
    m=model(4,{0,2},[(0,1),(2,1),(2,3)],spin)
    transient=[i for i,n in enumerate(m['Ns']) if n==2]
    free=[i for i in transient if m['Gamma'][i,i]==0]
    loss=[i for i in transient if m['Gamma'][i,i]!=0]
    A=m['T'].extract(loss,free)
    F=m['T'].extract(free,free)
    null=A.nullspace()
    assert len(null)==1 and A*F*null[0]!=s.zeros(len(loss),1)
    # W is diagonal and preserves the one-dimensional candidate kernel;
    # therefore arbitrary positive detuning cannot cancel the boundary escape.
    Wf=m['W'].extract(free,free)
    assert A*Wf*null[0]==s.zeros(len(loss),1)
    assert A.col_join(A*F).rank()==len(free)
    P,X,Z,H,J=effective(m)
    init=m['states'].index(((0,0,0),(1,0,1,0)))
    v=P.T*s.eye(len(m['states']))[:,init]
    rate=s.simplify(sum((v.H*j.H*j*v)[0] for j in J))
    results.append({'spin':spin,'full_sector_dimension':len(m['states']),'transient_dimension':len(transient),'lossless_transient_dimension':len(free),'boundary_rank':A.rank(),'boundary_plus_one_hop_rank':A.col_join(A*F).rank(),'lossless_kernel_in_free_order':list(map(str,null[0])),'second_step_boundary':list(map(str,A*F*null[0])),'effective_initial_birth_rate_delta_kappa_1':str(rate),'conclusion':'No nonzero invariant subspace inside kernel loss; every N=2 state eventually forms one pair and fills this finite path for positive epsilon,delta,kappa. The argument is identical for every integer spin>=1 because the N=2 hopping block is unchanged and its positive-loss support is unchanged.'})
out={'method':'exact boundary-invariance elimination, not finite-time extrapolation','rows':results}
(p/'PATH_ABSORPTION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
