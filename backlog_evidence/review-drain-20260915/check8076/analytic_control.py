from fractions import Fraction as Q
import json
from pathlib import Path
# Independent exact checks of stated rational propagation/error allocations.
def B(z,m):return z*(Q(7,30)+Q(7*m,15))+Q(4,3*2**m)
assert B(Q(1,10000),15)<Q(1,1000)
assert 398*B(Q(1,10**7),25)<Q(1,1000)
# Factor bound below .0042 can be tested without rounding sqrt.
e=Q(5,10**12); b=Q(42,10000); lin=1608*e
assert b>lin and 4*536*1608*e<(b-lin)**2
# qA,qC,qd: disjoint two-link signed supports, two unselected neighbors.
a=[1,-1,0,0,0,0];c=[0,0,1,-1,0,0];d=[1,-1,1,-1,1,-1]
g=[[Q(sum(x*y for x,y in zip(u,v)),4) for v in [a,c,d]] for u in [a,c,d]]
assert g==[[Q(1,2),0,Q(1,2)],[0,Q(1,2),Q(1,2)],[Q(1,2),Q(1,2),Q(3,2)]]
assert 2*sum(g[i][i] for i in range(3))==5
# Uniform ellipse constants and catalog analytic radii.
assert Q(3200,2759)<Q(27,25)**2
R=Q(20,3)*(4+Q(4800,961))*Q(4,25)**26
width=Q(100,157)*(2*R+Q(12**27,53*8**53)+Q(1,2**64)+Q(1,10**25))+Q(1,10**35)
assert width<Q(2,10**19)
out={'status':'PASS','poisson_bounds':[str(B(Q(1,10000),15)),str(398*B(Q(1,10**7),25))],'new_gram':[[str(x) for x in row] for row in g],'mu_predata_width':str(width),'scope':'Independent rational arithmetic controls of displayed analytic constants; not primary/runtime replay.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS rational analytic controls')
