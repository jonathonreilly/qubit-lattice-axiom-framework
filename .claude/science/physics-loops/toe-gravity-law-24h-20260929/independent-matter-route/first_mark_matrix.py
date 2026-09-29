"""Small exact first-vector matrix certificate for full H4 minus vacuum mean."""
from fractions import Fraction
from pathlib import Path
import json
import birth_work_exact as b

v=b.birth(b.ORIGIN,(1,0,0),(-1,1));states=sorted(v);n=len(states)
mat=[[0]*n for _ in range(n)]
for a,c in b.candidate_pairs(v):
    columns=[b.apply_pair({s:1},a,c) for s in states]
    vacuum=36-len(set(b.nb(a))&set(b.nb(c)))
    for i in range(n):
        for j in range(n):
            gram=sum(z*columns[j].get(s,0) for s,z in columns[i].items())
            mat[i][j]-=2*(gram-(vacuum if i==j else 0))
assert all(mat[i][j]==mat[j][i] for i in range(n) for j in range(n))
sectors={}
for name,sigmas in [('minus',(-1,)),('plus',(1,)),('coherent',(-1,1))]:
    indices=[states.index(s) for s in b.birth(b.ORIGIN,(1,0,0),sigmas)]
    val=Fraction(sum(mat[i][j] for i in indices for j in indices),len(indices))
    sectors[name]={'indices':indices,'energy':str(val)}
print('full H4 - vacuum scalar restricted to original ten first coordinate words')
for row in mat:print(row)
print(json.dumps(sectors,indent=2))
print('TOTAL: PASS=1 FAIL=0 (exact ten-word matrix Hermiticity and full first-vector contractions)')
Path(__file__).with_suffix('.json').write_text(json.dumps({'states':states,'matrix':mat,'sectors':sectors},indent=2)+'\n')
