from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
import sympy as s
from check import one_color_operators, extract
edges = [(0,1),(1,2),(2,3),(0,3)]
H0 = s.zeros(16)
H0[5,5] = H0[10,10] = 1
_, full = one_color_operators(4,edges,edges,1,1,1)
full -= s.I*(s.kronecker_product(s.eye(16),H0)-s.kronecker_product(H0.T,s.eye(16)))
h2 = [z for z in range(16) if z.bit_count()==2]
K = extract(full,16,h2)
vT = -K.inv(method='DM').conjugate().T*s.eye(6).vec()
residual = K.conjugate().T*vT+s.eye(6).vec()
reduced = residual.applyfunc(s.simplify)
assert reduced == s.zeros(36,1)
result = {'structurally_nonzero_entries':[[i,str(v)] for i,v in enumerate(residual) if v!=0],
          'simplified_residual_exactly_zero':True,
          'diagnosis':'The inherited exact helper used structural matrix equality. New complex detuning leaves algebraically cancelling terms unsimplified. The defining residual is exactly zero after simplification. Keep the sealed helper unchanged and simplify this new comparison-only residual.'}
(HERE/'DIAGNOSIS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
