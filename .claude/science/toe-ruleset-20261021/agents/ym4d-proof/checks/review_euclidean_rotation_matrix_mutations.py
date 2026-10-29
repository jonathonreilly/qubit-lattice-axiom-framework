"""Post-inspection explicit-matrix cross-check and falsifying source mutations.
The initial independent controls and criteria remain unchanged.
"""
from pathlib import Path
import contextlib,io,json,hashlib
import sympy as s

# Explicit matrix multiplication gives a different path from both quaternion
# implementations; new rational inputs avoid relying on the matching fixture.
def su2(w,x,y,z):return s.Matrix([[w+s.I*x,y+s.I*z],[-y+s.I*z,w-s.I*x]])
a=su2(s.Rational(9,41),s.Rational(40,41),0,0)
b=su2(s.Rational(20,29),0,s.Rational(21,29),0)
c=su2(s.Rational(12,37),0,0,s.Rational(35,37))
d=su2(s.Rational(11,61),s.Rational(60,61),0,0)
for A in [a,b,c,d]:assert s.simplify(A.H*A)==s.eye(2) and s.simplify(A.det())==1
P=a*b;Q=c*d;loop=s.simplify(s.re(s.trace(a*b*d.H*c.H)))
feature=s.simplify(sum((P[i,j]*s.conjugate(Q[i,j])+s.conjugate(P[i,j])*Q[i,j])/2 for i in range(2) for j in range(2)))
wrong=s.simplify(s.re(s.trace(a*b*d*c)))
assert loop==feature and wrong!=loop
lam=s.log(2)/2;gram=s.Matrix([[s.exp(2*lam),s.exp(-2*lam)],[s.exp(-2*lam),s.exp(2*lam)]])
negative=gram.subs(s.log(2),-s.log(2));v=s.Matrix([1,-1]);assert (v.T*gram*v)[0]==3 and (v.T*negative*v)[0]==-3

source=Path(__file__).with_name('euclidean_rotation_import_exact.py').read_text()
cases=[
 ('diagonal_reflection_sign','y[j], y[k] = -sign * x[k], -sign * x[j]','y[j], y[k] = sign * x[k], sign * x[j]','diagonal_geometry'),
 ('path_adjoint','qconj(d)), qconj(c))','d), qconj(c))','path_algebra'),
 ('wilson_trace_factor','direct = 2*qmul','direct = qmul','path_algebra'),
 ('negative_crossing_coefficient','negative_gram = sp.Matrix([[sp.Rational(1,2),2],[2,sp.Rational(1,2)]])','negative_gram = sp.Matrix([[2,sp.Rational(1,2)],[sp.Rational(1,2),2]])','path_algebra'),
 ('strict_block_buffer','center = (L, 0, 0, 0)','center = (L-1, 0, 0, 0)','support_footprints'),
 ('torus_boundary','w[j] = (w[j]+sign) % n','w[j] = w[j]+sign','torus_geometry'),
 ('gaussian_mass_normalization','lap = 5*sp.eye(n*n)','lap = 6*sp.eye(n*n)','gaussian_torus_control'),
 ('rational_rotation_coefficient','c=sp.Rational(3,5);s=sp.Rational(4,5)','c=sp.Rational(4,5);s=sp.Rational(4,5)','analytic_controls'),
]
results=[]
for label,old,new,fn in cases:
 assert source.count(old)==1,(label,source.count(old))
 modified=source.replace(old,new);ns={'__name__':'review_mutant'}
 exec(compile(modified,'review_mutant_'+label,'exec'),ns)
 try:ns[fn]()
 except AssertionError as e:
  results.append({'mutation':label,'function':fn,'rejected_by':'AssertionError','message':str(e),'mutant_sha256':hashlib.sha256(modified.encode()).hexdigest()})
 else:raise AssertionError('SURVIVED '+label)
print(json.dumps({'explicit_matrix_check':{'loop':str(loop),'feature':str(feature),'wrong_adjoint':str(wrong),'positive_quadratic':3,'negative_quadratic':-3},'mutations':results,'scope':'Each listed mutation rejected; not an exhaustive every-statement mutation certificate.'},indent=2))
