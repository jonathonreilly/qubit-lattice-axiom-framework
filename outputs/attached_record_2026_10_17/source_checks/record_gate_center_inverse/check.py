import sympy as s
import json
from pathlib import Path
rows=[]
for x in [1,-1]:
    inverses=[]
    for arm in [0,1]:
        D=s.zeros(12)
        D[0,0]=-x
        D[11,11]=s.I
        cells=[2,5] if arm else []
        for n in range(11):
            D[n,n+1]=D[n+1,n]=s.sqrt(2) if n in cells else 1
        for n in cells:
            D[n,n]=D[n+1,n+1]=-1
        R=D.inv().applyfunc(s.simplify)
        assert (D*R-s.eye(12)).applyfunc(s.simplify)==s.zeros(12)
        norm2=s.simplify(sum(s.conjugate(v)*v for v in R))
        col2=s.simplify(sum(s.conjugate(R[n,11])*R[n,11] for n in range(12)))
        rows.append(dict(x=x,arm=arm,frobenius_squared=str(norm2),port_column_squared=str(col2),port_diagonal=str(R[11,11])))
        inverses.append(R)
    g=s.simplify((inverses[0][11,11]+inverses[1][11,11])/2)
    assert g==-s.I/2
    rows.append(dict(x=x,twolead_input_diagonal=str(g),onelead_update_denominator=str(s.simplify(1-s.I*g))))
p=Path(__file__).with_name('RESULT.json');p.write_text(json.dumps({'method':'exact SymPy algebra, j scaled to 1; 12-site chains from checked lead unitary; no floating-point certificate','rows':rows},indent=2)+'\n')
print(p.read_text())
