"""Independent finite exterior-power representation controls; no primary import."""
import sympy as s, itertools, json,time
start=time.monotonic(); rows=[]
def ck(n,b):
 assert b,n
 rows.append(n)
pairs=list(itertools.combinations(range(4),2)); I=s.eye(2)
def wedge(T):return s.Matrix([[T.extract(a,b).det() for b in pairs] for a in pairs])
Bz=s.diag(2,s.Rational(1,2));Bx=s.Matrix([[s.Rational(5,4),s.Rational(3,4)],[s.Rational(3,4),s.Rational(5,4)]])
Uz=s.diag((3+4*s.I)/5,(3-4*s.I)/5);Ux=s.Matrix([[s.Rational(3,5),4*s.I/5],[4*s.I/5,s.Rational(3,5)]])
boosts=[wedge(s.diag(B,B.inv())) for B in [Bz,Bx]];rots=[wedge(s.diag(U,U)) for U in [Uz,Ux]]
E=lambda i,j:s.eye(6)[:,i]*s.eye(6)[j,:]
K=2*(E(1,1)+E(4,4)+E(2,3)+E(3,2));basis=[E(0,0),E(5,5),E(0,5)+E(5,0),s.I*(E(0,5)-E(5,0)),K]
for i,A in enumerate(basis):
 ck('Hermitian_'+str(i),A==A.H)
 for j,W in enumerate(boosts+rots):ck('finite_Lorentz_'+str((i,j)),s.simplify(W.H*A*W-A)==s.zeros(6))
def equations(Ws):
 return s.Matrix.vstack(*[s.Matrix.hstack(*[s.Matrix(W.H*E(i,j)*W-E(i,j)).reshape(36,1) for i in range(6) for j in range(6)]) for W in Ws])
ck('finite_group_invariant_dimension_5',36-equations(boosts+rots).rank()==5)
ck('rotation_invariant_dimension_10',36-equations(rots).rank()==10)
valley=wedge(s.diag(2,2,s.Rational(1,2),s.Rational(1,2)))
# Valley phase, not real rescaling, acts on conjugates.
valley=wedge(s.diag(s.I,s.I,-s.I,-s.I)) # This special phase is blind to pair transfer; use generic unit phase below.
t=(3+4*s.I)/5;valley=wedge(s.diag(t,t,1/t,1/t))
ck('separate_valley_dimension_3',36-equations(boosts+rots+[valley]).rank()==3)
# Native onsite phase-zero pair annihilator has r,l and mixed (03+12) channels.
v=s.Matrix([0,0,1,1,0,0]); onsite=E(0,0)+E(5,5)+v*v.T
ck('onsite_boost_not_invariant',boosts[0].H*onsite*boosts[0]!=onsite)
# Coefficient matrix obtained by normal-ordered pair occupations/exchange.
a,b,c,A,B,C=s.symbols('a b c A B C',real=True)
D=b*(E(0,0)+E(5,5)+E(2,2)+E(3,3))+(a-A)*E(1,1)+(c-C)*E(4,4)+B*(E(2,3)+E(3,2))
sol=s.linsolve(list(boosts[0].H*D*boosts[0]-D)+list(boosts[1].H*D*boosts[1]-D)+list(rots[0].H*D*rots[0]-D)+list(rots[1].H*D*rots[1]-D),(a,b,c,A,B,C))
ck('density_conditions',sol==s.FiniteSet((A+B,0,B+C,A,B,C)))
ck('density_image',D.subs({a:A+B,b:0,c:B+C})==B*K/2)
ck('mean_zero_density_sign',D.subs({a:0,b:0,c:0,A:1,B:-1,C:1})==-K/2)
k=s.symbols('k',real=True)
ck('stencil_transfer',s.trigsimp(s.cos(2*k)-s.cos(4*k)-2*s.sin(3*k)*s.sin(k))==0)
ck('endpoint_zero',s.simplify((s.cos(2*k)-s.cos(4*k)).subs(k,s.pi/3))==0)
# Determinantal Slater correlation: direct term cancels in equal/opposite stencil weights;
# exchange uses sigma3 on left wave, so signed overlap becomes u†v.
u=s.Matrix([1,1])/s.sqrt(2);v=s.Matrix([3,4])/5;Z=s.diag(1,-1)
ck('coherent_spinor_mutation_discriminates',abs((u.H*v)[0])**2!=abs((u.H*Z*v)[0])**2)
ck('two_particle_normalization_factor',(s.Symbol('a')**s.Rational(3,2)/s.sqrt(s.Symbol('v')))**4*s.Symbol('v')/s.Symbol('a')**3/s.Symbol('a')==s.Symbol('a')**2/s.Symbol('v'))
print(json.dumps({'status':'ok','checks':rows,'count':len(rows),'elapsed_seconds':time.monotonic()-start,'scope':'Finite SL(2,C) exterior-square invariance and independent coefficient matrices, not primary rerun.'},indent=2))
