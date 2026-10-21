"""Exact minimum-order path sum for reversing two longitudinal columns."""
from fractions import Fraction
import json
from pathlib import Path
rows=[]
for L in range(2,17):
 full=(1<<L)-1;f=[Fraction(0) for _ in range(1<<L)];f[0]=1
 for mask in range(1,full+1):
  value=sum(f[mask^(1<<i)] for i in range(L) if mask>>i&1)
  walls=sum(((mask>>i)^(mask>>(i+1)))&1 for i in range(L-1))
  f[mask]=value if mask==full else value/Fraction(4*walls)
 assert f[full]==Fraction(1,2**(L-1))
 rows.append(dict(L=L,path_denominator_sum=str(f[full]),coefficient='-Jperp^L/(2Jz)^(L-1)'))
(Path(__file__).resolve().parent/'neutral_strong_tunnel.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
