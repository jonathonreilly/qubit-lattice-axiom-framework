"""Independent exact determinant and interval checks of corrected-operator bounds."""
from pathlib import Path
from fractions import Fraction as F
import json
P=Path(__file__).parent

def count(diagonal,off):
    determinants=[F(1),diagonal[0]]
    for k in range(1,len(diagonal)):
        determinants.append(diagonal[k]*determinants[-1]-off[k-1]**2*determinants[-2])
    if any(d==0 for d in determinants):raise ArithmeticError('Zero leading determinant')
    return sum((a<0)!=(b<0) for a,b in zip(determinants,determinants[1:]))

def enclosure_count(row,E,alter=False):
    L=row['L'];K=F(row['K']);d=F(row['delta']);x=F(row['x'])
    assert K>0 and d>0 and 0<=x<F(1,4)
    assert x==d/(K*row['S']*(row['S']+1))
    diag=[4*K*n*n-4*d+x*(8*d-8*K*n*n)-E for n in range(-L,L+1)]
    off=[-2*d+x*(4*d+4*K*n*(n+1)) for n in range(-L,L)]
    t=-2*d+x*(4*d+4*K*L*(L+1))
    lower_tail=4*K*(1-4*x)*(L+1)**2-8*d
    assert lower_tail>E
    beta=t*t/(lower_tail-E)
    if alter:off=[F(99,100)*v for v in off]
    upper_count=count(diag,off)
    diag[0]-=beta;diag[-1]-=beta
    lower_count=count(diag,off)
    assert upper_count==lower_count
    return upper_count

corrected=[json.loads(s) for s in (P/'corrected_operator_certificate.jsonl').read_text().splitlines()]
finite=[json.loads(s) for s in (P/'rational_spectral_certificate.jsonl').read_text().splitlines()]
errors=json.loads((P/'corrected_operator_error_bounds.json').read_text())
table=['.004987235265','.000136754425','.000004229203','6.647658236470','.281239142371','.009192992163']
results=[]
for i,row in enumerate(corrected):
    key=lambda r:(r['S'],F(r['delta']))
    base=next(r for r in finite if key(r)==key(row));err=next(r for r in errors if key(r)==key(row))
    intervals=[tuple(map(F,pair)) for pair in row['energy_intervals']]
    counts=[[enclosure_count(row,E) for E in pair] for pair in intervals]
    assert counts==[[j,j+1] for j in range(7)]
    assert all(b-a==F(2,10**9) for a,b in intervals)
    gaps=[(a-intervals[0][1],b-intervals[0][0]) for a,b in intervals[1:]]
    assert gaps==[tuple(map(F,pair)) for pair in row['gap_intervals']]
    truegaps=[tuple(map(F,pair)) for pair in base['gap_intervals']]
    difference=[(a-d,b-c) for (a,b),(c,d) in zip(truegaps,gaps)]
    assert difference==[tuple(map(F,pair)) for pair in err['gap_difference_intervals']]
    bound=max(abs(v) for pair in difference for v in pair)
    assert bound==F(err['maximum_absolute_gap_error_upper_bound'])
    scaled=bound*10**12;rounded=F(-(-scaled.numerator//scaled.denominator),10**12)
    assert rounded==F(table[i]) and rounded>=bound
    fault=[enclosure_count(row,E,True) for E in intervals[0]]
    assert fault!=[0,1]
    results.append(dict(S=row['S'],delta=row['delta'],counts=counts,exact_error_bound=str(bound),upward_decimal=table[i],off_diagonal_fault_counts=fault))
print(json.dumps(results,indent=2))
