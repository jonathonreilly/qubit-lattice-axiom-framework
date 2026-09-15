import sympy as s,itertools,json
from pathlib import Path
# Gauge-free construction using integer bitmask vertices and oriented cellular boundaries.
V=list(range(16));E=[(v,v|(1<<a),a) for v in V for a in range(4) if not(v>>a&1)];idx={(v,a):i for i,(v,w,a) in enumerate(E)}
F=[];weights=[];sources=[]
for a,b in itertools.combinations(range(4),2):
 for v in V:
  if (v>>a&1) or (v>>b&1):continue
  row=s.zeros(1,32)
  for base,axis,sign in [(v,a,1),(v|1<<a,b,1),(v|1<<b,a,-1),(v,b,-1)]:row[0,idx[base,axis]]=sign
  if (a,b)==(0,1) and not(v>>2&1):sources.append((v>>3,row))
  else:F.append(row);weights.append(s.Rational(1,1 if b==3 else 2))
B=s.Matrix.vstack(*F);S=s.Matrix.vstack(*[row for t,row in sorted(sources,key=lambda x:x[0])]);D=s.zeros(32,15)
for i,(v,w,a) in enumerate(E):
 if v:D[i,v-1]=-1
 if w:D[i,w-1]=1
assert B*D==s.zeros(22,15) and S*D==s.zeros(2,15)
Q=B.T*s.diag(*weights)*B
# Add gauge-only precision, which cannot alter source covariance on cycles.
C=s.simplify(S*(Q+D*D.T).inv()*S.T)
assert C==s.Matrix([[64,46],[46,64]])/11
C2=S*(Q+7*D*D.T).inv()*S.T;assert C2==C
# Independent rooted tree: delete lowest active bit from each nonzero vertex.
tr=[]
for w in V[1:]:
 a=next(a for a in range(4) if w>>a&1);tr.append(idx[(w^(1<<a),a)])
ch=[i for i in range(32) if i not in tr];H=Q.extract(ch,ch)
assert H.det()==s.Rational(55,2)
full=S*(Q+S.T*S/2+D*D.T).inv()*S.T;assert full==s.Matrix([[77,23],[23,77]])/60
wrong=S*(B.T*B+D*D.T).inv()*S.T;assert wrong==s.Matrix([[16,9],[9,16]])/5
Sigma=3*C;prec=Sigma.inv();a=prec[0,0]/2;b=-prec[0,1];omega=s.sqrt(4*a*a-b*b);theta=s.simplify(b/(2*a+omega))
assert a==s.Rational(8,135) and b==s.Rational(23,270) and omega==s.sqrt(55)/90
# Direct Cartan Vandermonde polynomial integration with exact independent Gaussian moments.
u,y=s.symbols('u y');t1=u-y/2;t2=y;t3=-t1-t2
poly=s.Poly(s.expand(((t1-t2)*(t1-t3)*(t2-t3))**2),u,y)
def moment(n,var):return 0 if n%2 else s.factorial2(n-1)*var**(n//2) if n else 1
moment_value=sum(coef*moment(i,s.Rational(1,2))*moment(j,s.Rational(2,3)) for (i,j),coef in poly.terms())
cartan_int=moment_value*2*s.pi/s.sqrt(3);j0=s.simplify(cartan_int/(6*(2*s.pi)**2)/(2*s.pi)**4)
assert j0==1/(16*s.sqrt(3)*s.pi**5)
const=(2*s.pi)**-8*Sigma.det()**-4/j0
lam=s.simplify(const*(s.pi/(a+omega/2))**4)
expected=s.sqrt(3)*s.pi*(11/(6*(32+3*s.sqrt(55))))**4;assert s.simplify(lam-expected)==0
# Complete square in ground-state convolution, and test invariant degree-two oscillator.
c=a+omega/2;assert s.simplify(-a+b*b/(4*c)+omega/2)==0
# E[|Y|²-8/(2omega)] under shifted Gaussian kernel, conditional mean bX/(2c).
x2=s.symbols('x2');image=8/(2*c)+(b/(2*c))**2*x2-8/(2*omega)
assert s.simplify(image-theta**2*(x2-8/(2*omega)))==0
# Cubic invariant is harmonic (no invariant linear polynomial), hence theta³ branch.
assert 0<float(theta)<1 and float(6**4*lam)<.01
out={'C':str(C),'detH':str(H.det()),'restored_C':str(full),'wrong_halfweight_C':str(wrong),'Sigma':str(Sigma),'a':str(a),'b':str(b),'omega':str(omega),'theta':str(theta),'j0':str(j0),'lambda0':str(lam),'lambda0_numeric':float(lam),'beta6_leading':float(6**4*lam),'degree2_eigenfunction_control':'PASS','gauge_only_precision_invariance':'PASS'}
Path('/private/tmp/review-drain-20260915/check8016/independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
