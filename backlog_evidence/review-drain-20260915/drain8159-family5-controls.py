"""Bounded independent review controls. No campaign imports or primary runs."""
import itertools, json, math
from fractions import Fraction as F
import sympy as s
out={}
q,k=s.symbols('q k',real=True)
m=lambda t:s.exp(q*t*(t-2)/8)
assert s.simplify(m(k+2)/m(k)-s.exp(k*q/2))==0
assert m(2)==1 and m(4)==s.exp(q)
out['gaussian_rate_moment_recurrence']='exact; m2=1, m4=exp(q), mean=exp(-q/8)'
# An independent signed-loop counterexample, exact rationals.
H=s.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])/2
terms=[H[j,i]*H[j,l]*H[n,l]*H[n,i] for i,j,l,n in itertools.product(range(4),repeat=4)]
assert sum(terms)==4 and sum(map(abs,terms))==16 and sum(t for t in terms if t>0)==10
out['bounded_residual_control']={'signed':4,'absolute':16,'positive_indicator':10}
# Finite BKAR cancellation for indirect incompatibility (13 only).
a,b,c,u,v=s.symbols('a b c u v',real=True)
f=(1-b)*(1-a*c); values=[]
for tree in [(a,b),(a,c),(b,c)]:
 val=0
 missing=next(x for x in (a,b,c) if x not in tree)
 for first,second in [tree,tree[::-1]]:
  integrand=s.diff(f,*tree).subs({first:u,second:v,missing:v},simultaneous=True)
  val+=s.integrate(s.integrate(integrand,(v,0,u)),(u,0,1))
 values.append(val)
assert sorted(values)==[-s.Rational(2,3),s.Rational(1,3),s.Rational(1,3)] and sum(values)==0
out['indirect_contact_tree_cancellation']=list(map(str,values))
# Exact Gram determinant mixed derivative versus explicit permutation expansion.
a,b,c=s.symbols('a b c'); G=s.Matrix([[1,a,b],[a,1,c],[b,c,1]])
assert s.expand(G.det()-(1-a*a-b*b-c*c+2*a*b*c))==0
assert s.diff(G.det(),a,c)==2*b
assert G.subs({a:1,b:1,c:0}).det()==-1
out['gram_scope_and_contact']={'mixed_derivative':'2b','non_psd_cube_determinant':-1}
# Binary parent rank calculation by integrating t: each designated neighbor has probability 1/7.
p=sum(F(math.comb(5,j),j+1)*F(math.factorial(j+1)*math.factorial(5-j),math.factorial(7)) for j in range(6))
assert p==F(1,7) and 2*p*F(1,2)/4==F(1,28)
P=s.ones(3)/3; U=s.Matrix([1,-1,0]);V=s.Matrix([1,1,-2]);K=P+U*V.T/12
assert K*K==P and K!=K.T and min(K)>0
out['record_controls']={'local_parent_probability':str(p),'covariance_gap':'1/28','nonreversible_square_projection_escape':True}
# Real algebra shear fixed space and Borel opposite-corner escape.
x,y,z,w,t=s.symbols('x y z w t');M=s.Matrix([[x,y],[z,w]]);I=s.eye(2);E=s.Matrix([[0,1],[0,0]]);L=E.T
constraints=list((I+E)*M*(I-E)-M)+list((I+L)*M*(I-L)-M)
sol=s.linsolve(constraints,(x,y,z,w));assert sol==s.FiniteSet((w,0,0,w))
C=L/t;T=t*E;assert T*C==s.diag(1,0) and C*T==s.diag(0,1)
out['naturality_controls']={'both_shear_fixed_space':'complex scalar matrices','inverse_corner':'E21/t; non-tight Gaussian corner variance t^-2'}
# Auxiliary identity on a nontrivial one-dimensional magnetic subspace.
B=s.Matrix([[1,-1,1]]);c=s.Rational(1,32);G=s.Rational(1,3);A=G-c;T=1/(1-3*c);R=(s.eye(3)-c*B.T*B).inv();P=s.eye(3)-B.T*B/3
assert A*T==G and B.T*(A*T*T)*B==R-P and R*P==P
out['auxiliary_resolvent_identity']='A T=G, B* T A T B=R-P, RP=P exactly'
z=s.symbols('z',real=True);eps=s.Rational(1,16);mgf=s.exp(z*z/4)*(1+eps*z**4/4)
assert s.diff(s.log(mgf),z,4).subs(z,0)==s.Rational(3,8)
out['self_dual_nongaussian_fourth_cumulant']='3/8'
out['status']='PASS_bounded_independent_math_controls_only'
print(json.dumps(out,indent=2))
