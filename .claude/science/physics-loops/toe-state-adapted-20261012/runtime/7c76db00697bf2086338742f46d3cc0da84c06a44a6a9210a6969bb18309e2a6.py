"""Post-observation exact half-angle resolution; originals remain untouched."""
import json,sys
import sympy as sy
x,v,a,m=sy.symbols('x v a m',real=True,nonzero=True)
gap=(m*m+16*v*v*sy.sin(x/2)**2/a**2)-(m*m+4*v*v*sy.sin(x)**2/a**2)
residual=gap-16*v*v*sy.sin(x/2)**4/a**2
original=sy.trigsimp(sy.expand_trig(residual))
print(json.dumps({'diagnostic':'original_trigsimp_expression','expression':str(original),
                  'literal_zero':bool(original==0)}),flush=True)
s,c=sy.symbols('s c',real=True)
half=residual.subs(sy.sin(x),2*sy.sin(x/2)*sy.cos(x/2))
polynomial=sy.expand((a*a/(16*v*v))*half.subs({sy.sin(x/2):s,sy.cos(x/2):c}))
rows=[{'name':'half_angle/normalized_residual_factor',
       'passed':bool(sy.expand(polynomial-s*s*(1-s*s-c*c))==0),'polynomial':str(polynomial)},
      {'name':'half_angle/unit_circle_zero',
       'passed':bool(sy.expand(polynomial.subs(c*c,1-s*s))==0)}]
for row in rows:print(json.dumps(row),flush=True)
failed=sum(not x['passed'] for x in rows)
print(json.dumps({'summary':True,'total':len(rows),'failed':failed,'passed':len(rows)-failed}),flush=True)
sys.exit(1 if failed else 0)
