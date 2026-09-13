"""Small exact CAR and numerical cocycle controls; no native alpha evaluation."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import json,time
import sympy as s
import numpy as np
from scipy.linalg import expm,norm
start=time.perf_counter(); checks=[]; data={}
def req(name,p):
    if not p: raise AssertionError(name)
    checks.append(name)
def eq(name,A,B): req(name,(A-B).applyfunc(s.expand)==s.zeros(*A.shape))
I=s.I; X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-I],[I,0]]); Z=s.diag(1,-1); one=s.eye(2)
def kron(*a): return s.kronecker_product(*a)
g=[kron(X,one),kron(Y,one),kron(Z,X),kron(Z,Y)]
ident=s.eye(4)
for j in range(4):
    for k in range(4): eq('CAR_'+str((j,k)),g[j]*g[k]+g[k]*g[j],2*ident if j==k else s.zeros(4))

# Two active and two spectator Majoranas, full spectator algebra retained.
omega=s.Rational(7,3); alpha=s.Rational(5,4)
P=(ident+ kron(Z,one))/2; Pe=ident-P
H=omega*Pe; R=-Pe/omega
W=-I*alpha*(g[0]*g[2]+g[1]*g[3])
b=-2*alpha**2/omega
expected=-2*alpha**2/omega*P+b*I*P*g[2]*g[3]*P
eq('singleton_negative_inverse_and_closure',P*W*R*W*P,expected)
req('positive_inverse_mutation_detected',P*W*(-R)*W*P!=expected)
req('half_bilinear_mutation_detected',P*W*R*W*P!=(-2*alpha**2/omega*P+b*I*P*g[2]*g[3]*P/2))
G=s.Matrix([[1,I],[-I,1]])
T=alpha**2/omega*G
B=2*I*(T-T.T)
eq('realspace_transpose_B_normalization',B,s.Matrix([[0,2*b],[-2*b,0]]))
req('adjoint_in_place_of_transpose_mutation_detected',2*I*(T-T.conjugate().T)!=B)
data['singleton']={'omega':str(omega),'alpha':str(alpha),'coefficient_b':str(b),'B01':str(B[0,1])}

# Non-Hermitian odd-unitary family; direct density contraction vs two Gram maps.
c=s.Rational(3,5); z=s.Rational(4,5)
xs=[g[j]*(c*ident-z*g[(j+1)%4]*g[(j+2)%4]) for j in range(4)]
ys=[g[j]*(c*ident+z*g[(j+1)%4]*g[(j+2)%4]) for j in range(4)]
psi=s.Matrix([1,I,2,1+I]); psi=psi/s.sqrt((psi.conjugate().T*psi)[0])
VX=s.Matrix.hstack(*[a.conjugate().T*psi for a in xs])
VY=s.Matrix.hstack(*[a*psi for a in ys])
N=s.Matrix(4,4,lambda j,k:(psi.conjugate().T*xs[j]*ys[k]*psi)[0])
eq('nonhermitian_odd_Gram_factorization',N,VX.conjugate().T*VY)
req('X_is_not_assumed_Hermitian',any(a!=a.conjugate().T for a in xs))
for j,a in enumerate(xs+ys): eq('odd_family_unitarity_'+str(j),a.conjugate().T*a,ident)
wrong=s.Matrix.hstack(*[a*psi for a in xs])
req('wrong_Gram_adjoint_mutation_detected',(N-wrong.conjugate().T*VY).applyfunc(s.expand)!=s.zeros(4))
eq('disjoint_odd_graded_locality',g[0]*g[3]+g[3]*g[0],s.zeros(4))
req('ordinary_commutator_wrong_for_odd',g[0]*g[3]-g[3]*g[0]!=s.zeros(4))

# Exact power-series cocycle orientation on a coupled four-Majorana chain.
Hc=I*(g[0]*g[1]+2*g[1]*g[2]+3*g[2]*g[3])/2
Bx=I*g[0]*g[1]/3; By=I*g[2]*g[3]/5
order=5
def expseries(A): return [(A**j)/s.factorial(j) for j in range(order+1)]
def mulseries(a,b):
    return [sum((a[j]*b[n-j] for j in range(n+1)),s.zeros(4)).applyfunc(s.expand) for n in range(order+1)]
def useries(H,B): return mulseries(expseries(-I*(H+B)),expseries(I*H))
full=useries(Hc,Bx+By); fact=mulseries(useries(Hc,Bx),useries(Hc,By))
first=next(j for j in range(order+1) if full[j]!=fact[j])
req('coupled_disjoint_impurity_first_error_order3',first==3)
Hsep=I*(g[0]*g[1]+3*g[2]*g[3])/2
sep=useries(Hsep,Bx+By); sepf=mulseries(useries(Hsep,Bx),useries(Hsep,By))
for j in range(order+1): eq('uncoupled_exact_factorization_jet_'+str(j),sep[j],sepf[j])
data['cocycle_exact']={'first_coupled_error_order':first,'third_order_norm_squared_Frobenius':str(s.trace((full[3]-fact[3]).conjugate().T*(full[3]-fact[3])))}

# Independent matrix exponentials at both signs of time; a universal Duhamel floor.
arr=lambda A:np.array(A,dtype=complex)
hc,bx,by=map(arr,(Hc,Bx,By)); eye=np.eye(4)
def u(h,b,t): return expm(-1j*t*(h+b))@expm(1j*t*h)
vals=[]
for t in (.2,.1,-.1,-.2):
    err=norm(u(hc,bx+by,t)-u(hc,bx,t)@u(hc,by,t),2)
    safe=norm(bx,2)*norm(by,2)*t*t
    req('numerical_universal_Duhamel_'+str(t),0<err<safe+1e-14)
    vals.append({'t':t,'error':float(err),'universal_bound':float(safe)})
data['cocycle_numerical']=vals

# Exact fixed-time ordering underlying the five-filter identity, no quadrature.
h=np.diag([0.,1.,2.,3.]); vac=np.array([1,0,0,0],dtype=complex)
bs=[arr((j+1)*Bx+(5-j)*By+I*g[1]*g[2]/(j+2)) for j in range(5)]
ts=[.1,-.2,.07,.03,-.11]
direct=vac.copy()
for j in range(5): direct=expm(-1j*ts[j]*(h+bs[j]))@direct
product=eye.copy(); naive=eye.copy(); prefix_wrong=eye.copy()
for j in reversed(range(5)):
    sj=sum(ts[j+1:]); tau=lambda A,t:expm(-1j*t*h)@A@expm(1j*t*h)
    uj=u(h,bs[j],ts[j])
    product=product@tau(uj,sj)
    naive=naive@uj
    prefix_wrong=prefix_wrong@tau(uj,sum(ts[:j]))
res=float(norm(direct-product@vac))
req('five_cocycle_suffix_time_identity',res<2e-13)
req('omitted_base_dynamics_mutation_detected',norm(direct-naive@vac)>1e-5)
req('wrong_prefix_time_mutation_detected',norm(direct-prefix_wrong@vac)>1e-5)
data['five_cocycle']={'correct_residual':res,'omitted_dynamics_error':float(norm(direct-naive@vac)), 'prefix_time_error':float(norm(direct-prefix_wrong@vac))}

# The actual eight-component Clifford node convention, with synthetic D only.
Gam=[kron(X,one,one),kron(Z,X,one),kron(Z,Z,X)]
h0=(2*Gam[0]+Gam[1]+2*Gam[2])/3
Id8=s.eye(8); eq('node_Clifford_square',h0*h0,Id8)
A=Gam[0]+2*I*Gam[1]
e=s.symbols('e',positive=True,real=True); a=s.symbols('a',real=True)
Dp=a*Id8+e*A; Dm=a*Id8-e*A
Tp=Dp.conjugate().T*(Id8+h0)*Dp/e
Tm=Dm.conjugate().T*(Id8-h0)*Dm/e
BB=(2*I*(Tp-Tm.T)).applyfunc(s.expand)
lead=4*I*a*a*h0/e
rem=(BB-lead).applyfunc(s.expand)
req('node_only_stated_inverse_power',all(s.expand(x*e).subs(e,0)==0 for x in rem))
zero=BB.subs(a,0).applyfunc(s.expand)
scaled=(zero/e).applyfunc(s.expand)
req('zero_node_exact_linear_scaling',all(not x.has(e) for x in scaled))
req('nonzero_node_singular_coefficient',any(x!=0 for x in lead.subs(a,1)))
eq('singular_hermitian_symbol_square',(-4*h0)*(-4*h0),16*Id8)
data['node']={'scope':'symbolic arbitrary smooth form factor, not the actual native alpha', 'singular_iB_coefficient':'-4 alpha^2 h/omega^2','zero_alpha_order':'O(e)'}

out={'scope':'same-agent small algebra/identity checks; no native scalar, phase, or large-volume simulation',
     'check_groups':len(checks),'checks':checks,'data':data,'seconds':time.perf_counter()-start}
Path(__file__).with_name('BLOCK05_ALGEBRA_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'check_groups':len(checks),'seconds':out['seconds'],'data':data},indent=2))
