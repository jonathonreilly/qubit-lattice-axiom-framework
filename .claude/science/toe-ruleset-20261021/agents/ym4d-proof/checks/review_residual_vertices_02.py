"""Exact independent nonflat SU(2) Wilson-row and noncommuting determinant controls."""
import sympy as s,json,sys
from datetime import datetime,timezone
checks={};details={};started=datetime.now(timezone.utc).isoformat()
def ck(n,v):checks[n]=bool(v)
def zero(M):return all(s.cancel(x)==0 for x in M)
def det(M):return M.det(method='domain-ge')
def prod(xs):
 out=s.eye(xs[0].rows)
 for x in xs:out=out*x
 return out
def realtrace(M):return s.expand_complex(s.trace(M)).as_real_imag()[0].expand()
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
T=[s.I*x/2 for x in pauli];eye=s.eye(2)
U=[s.Rational(3,5)*eye+s.I*s.Rational(4,5)*pauli[0],s.Rational(5,13)*eye+s.I*s.Rational(12,13)*pauli[1],s.Rational(8,17)*eye+s.I*s.Rational(15,17)*pauli[2],(eye+s.I*sum(pauli,s.zeros(2)))/2]
ck('noncommuting_SU2_links_unitary',all(zero(x.H*x-eye) and det(x)==1 for x in U))
ck('noncommuting_SU2_fixture',not zero(U[0]*U[1]-U[1]*U[0]))
V=[U[0],U[1],U[2].H,U[3].H]
def first(l,c):return U[l]*T[c] if l<2 else -T[c]*U[l].H
def second(l,c,e):
 sym=(T[c]*T[e]+T[e]*T[c])/2
 return U[l]*sym if l<2 else sym*U[l].H
Grad=s.zeros(12,1);H=s.zeros(12)
for i in range(12):
 l,c=divmod(i,3);arr=V.copy();arr[l]=first(l,c);Grad[i]=-realtrace(prod(arr))
 for j in range(12):
  m,e=divmod(j,3);arr=V.copy()
  if l==m:arr[l]=second(l,c,e)
  else:arr[l]=first(l,c);arr[m]=first(m,e)
  H[i,j]=-realtrace(prod(arr))
def coords(X):return s.Matrix([-2*s.trace(t*X) for t in T])
edges=[(0,1),(1,2),(3,2),(0,3)];D=s.zeros(12);Target=s.zeros(12);WrongEndpoint=s.zeros(12)
for l,(x,y) in enumerate(edges):
 Ad=s.Matrix.hstack(*[coords(U[l].H*t*U[l]) for t in T]);D[3*l:3*l+3,3*x:3*x+3]=Ad;D[3*l:3*l+3,3*y:3*y+3]=-s.eye(3)
 E=sum((Grad[3*l+c]*T[c] for c in range(3)),s.zeros(2))
 for c in range(3):
  X=U[l].H*T[c]*U[l];Y=T[c]
  Target[3*l:3*l+3,3*x+c]=coords(-(E*X-X*E)/2)
  Target[3*l:3*l+3,3*y+c]=coords(-(E*Y-Y*E)/2)
  WrongEndpoint[3*l:3*l+3,3*x+c]=coords(-(E*X-X*E)/2)
ck('actual_Wilson_gradient_nonzero',not zero(Grad))
ck('actual_nonflat_Wilson_endpoint_row',zero(H*D-Target))
ck('missing_Wilson_offshell_row_control',not zero(H*D))
ck('wrong_endpoint_half_control',not zero(H*D-2*Target))
ck('missing_endpoint_control',not zero(H*D-WrongEndpoint))
ck('Wilson_gauge_first_derivative',zero(D.T*Grad))
# Colour identity with a genuinely nonzero cubic real trace.
X,Y,Z=[2*t for t in T]
ck('nonzero_commutator_cubic_fixture',realtrace(X*Y*Z)!=0)
ck('actual_cubic_realtrace_commutator',realtrace(X*Y*Z)==realtrace(X*(Y*Z-Z*Y))/2)
ck('commutator_trace_zero',s.trace(X*Y-Y*X)==0)
details['nonflat_Wilson']={'action':str(2-realtrace(prod(V))),'gradient_norm2':str((Grad.T*Grad)[0]),'row_norm2':str(s.trace(Target.T*Target)),'cubic_real_trace':str(realtrace(X*Y*Z))}
# A dense noncommuting gauge-change derivative, independently by determinant polynomials.
t=s.symbols('t',real=True)
D=s.Matrix([[1,0,1],[0,2,1],[1,1,0],[1,0,2],[0,1,1],[2,1,1]])
F0=D.T;Fd=s.Matrix([[1,0,2,0,-1,1],[0,1,-1,2,0,1],[1,2,0,-1,1,0]])
H=s.diag(2,3,4,5,6,7)
for j in range(5):H[j,j+1]=H[j+1,j]=s.Rational(1,3)
F=F0+t*Fd;Q=H+F.T*F;B=F*D;dq=det(Q);db=det(B)
for it,x in enumerate([s.Rational(0),s.Rational(1,7)]):
 qq=Q.subs(t,x);bb=B.subs(t,x);ff=F.subs(t,x)
 direct=s.cancel((s.diff(dq,t)/(2*dq)-s.diff(db,t)/db).subs(t,x))
 nielsen=-s.trace(qq.inv()*H*D*bb.inv()*Fd)
 ck(f'noncommuting_V2_direct_determinant_{it}',s.cancel(direct-nielsen)==0)
 ck(f'dropping_equation_of_motion_row_control_{it}',direct!=0)
 unnormalized=s.cancel((s.diff(dq,t)/(2*dq)).subs(t,x))
 ck(f'missing_scalar_normalizer_control_{it}',unnormalized!=direct)
G=Q.subs(t,0).inv();Q1=F0.T*Fd+Fd.T*F0;Q2=Fd.T*Fd
coef=s.cancel((s.diff(dq,t,2)/dq-(s.diff(dq,t)/dq)**2).subs(t,0)/2)
ck('half_bubble_coefficient',s.cancel(coef-s.trace(G*Q2)+s.trace(G*Q1*G*Q1)/2)==0)
ck('missing_half_bubble_control',s.cancel(coef-s.trace(G*Q2)+s.trace(G*Q1*G*Q1))!=0)
# V1 with H D nonzero: the off-shell normalized face is algebra, not a null-row assumption.
D=s.Matrix([[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,2],[1,1,1,0],[0,1,1,1]])
I=s.eye(4)[:,:2];J=s.eye(4)[:,2:];De=D.T*D;Di=I.T*De*I
Dc=s.Matrix([[1,1],[0,2],[1,0],[2,1]]);Cov=s.Matrix([[3,1,0,0],[1,4,1,0],[0,1,5,1],[0,0,1,6]])
P=s.eye(6)-D*De.inv()*D.T;mix=s.Matrix([[1,2,0,1,-1,0],[0,1,3,0,1,2],[2,0,1,2,0,-1],[1,-1,0,1,2,1]])
M=Dc*J.T*De.inv()*D.T+mix*P;H=s.diag(2,3,4,5,6,7);W=H+D*D.T
Gc=Dc.T*Cov.inv()*Dc;Dc2=Dc.T*Dc;Rc=(s.eye(2)+Dc.T*Cov*Dc).inv()
local=(H+M.T*Cov.inv()*M).row_join(-M.T*Cov.inv()).col_join((-Cov.inv()*M).row_join(Cov.inv()))
LH=local+s.diag(D*I*I.T*D.T,Dc*Dc.T)
Rface=det(LH)/det(W)*(det(De)/det(Di))**2/det(Gc)*det(Cov)*det(Gc)/det(Dc2)**2
Q1=H+D*I*I.T*D.T+M.T*Dc*Rc*Dc.T*M
GammaRatio=det(Q1)/det(W)*det(De)**2/(det(Di)**2*det(Dc2)**2*det(Rc))
ck('off_shell_V1_normalized_face',Rface==GammaRatio)
ck('off_shell_V1_is_not_zero',Rface!=1)
ck('V1_with_nonzero_Wilson_row',not zero(H*D))
# Tuned curve and partial versus total derivative; no 80x80 author implementation reused.
z=s.symbols('z',real=True);den=10-8*z*z;u=2*z/den;v=(1-z)*(10-8*z)/den;a=9*u+v
ck('rational_path_constraint',s.cancel(a*a-1-80*u*u)==0)
ck('path_endpoint_0',u.subs(z,0)==0 and v.subs(z,0)==1)
ck('path_endpoint_1',u.subs(z,1)==1 and v.subs(z,1)==0)
partial=s.diff(a,z)-s.diff(u,z)*u*80*a/(1+80*u*u)
ck('partial_dotF_leading_cancellation',s.cancel(partial)==0)
total=s.diff(a/(1+80*u*u),z)
ck('total_derivative_wrong_control',s.cancel(total).subs(z,s.Rational(1,2))!=0)
ck('straight_path_25_over_21_control',s.Rational(5)**2/(1+s.Rational(1,4)*80)==s.Rational(25,21))
# Separate-centre domination, with no transfer of numerator powers between centres.
x,y=s.symbols('x y',positive=True)
ck('mixed_pole_Young_bound_exact',s.expand(x**3+2*y**3-3*x*y*y-(x-y)**2*(x+2*y))==0)
p=s.symbols('p',positive=True)
ck('double_residual_log_suppressed',s.limit(p*p*(1+s.log(1/p)),p,0,dir='+')==0)
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'passed':sum(checks.values()),'total':len(checks),'details':details,'scope':'Exact nonflat SU2 Wilson row and finite determinant/path identities; analytic Ward/locality/limit arguments are reviewed separately.'}
print(json.dumps(result,indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
