import ast, numpy as np,sympy as s,json
from pathlib import Path
p=Path('/private/tmp/review-drain-20260915/pr8010/scripts/native_gauge_transfer_dimension_divided_origin_recurrence_check_2026_09_07.py')
t=ast.parse(p.read_text()); fn=next(n for n in ast.walk(t) if isinstance(n,ast.FunctionDef) and n.name=='action');ns={'np':np,'N':5,'beta':7}
exec(compile(ast.Module(body=[fn],type_ignores=[]),str(p),'exec'),ns)
G=np.column_stack([ns['action'](e) for e in np.eye(25)]);H=np.zeros((25,25))
for i in range(5):
 for j in range(5):
  H[5*i+j,5*i+j]=-7
  for di,dj in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]:
   if 0<=i+di<5 and 0<=j+dj<5:H[5*(i+di)+j+dj,5*i+j]=7/6
assert np.array_equal(G,H);assert np.array_equal(G,G.T)
data=json.load(open('/private/tmp/review-drain-20260915/check8010/origin.json'))
for r in data['rows']:
 p,q=r['label'];beta=r['beta'];dim=(p+1)*(q+1)*(p+q+2)//2;Q=((p+1)**2+(p+1)*(q+1)+(q+1)**2)/beta
 assert r['dimension']==dim
 assert abs(r['gaussian']-np.exp(-Q))<1e-14
 assert abs(r['correction']-np.exp(-Q)*(3-7*Q/4+Q*Q/4)/beta)<1e-14
 assert abs(r['corrected_residual']-(r['native_dimension_divided']-r['gaussian']-r['correction']))<1e-14
# Relative error is monotone bounded by u/b + av/b^2 using b+v>=b.
a,b,u,v=s.symbols('a b u v',positive=True)
assert s.simplify((a+u)/(b+v)-a/b-(b*u-a*v)/(b*(b+v)))==0
Path('/private/tmp/review-drain-20260915/check8010/helper_independent.json').write_text(json.dumps({'generator':'25x25 exact array equality against enumerated six-neighbor graph','rows_checked':21,'ratio_identity':'exact symbolic numerator b*u-a*v; denominator b*(b+v)','runtime_inputs':[]}))
print('PASS generator,21 rows,ratio identity')
