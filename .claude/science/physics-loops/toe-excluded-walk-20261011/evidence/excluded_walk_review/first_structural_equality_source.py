"""Independent finite controls for the Cook bridge; not an infinite scattering computation."""
from fractions import Fraction
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
import mpmath as mp
import numpy as np
from scipy.linalg import expm
import sympy as s

CHECK_TIMEOUT_SECONDS=90
checks=0
def check(value,label):
    global checks
    assert bool(value),label
    checks+=1
def zero_matrix(m):return all(s.simplify(z)==0 for z in m)

# Generic codimension-one compression, from an actual self-adjoint matrix.
H0=s.diag(-1,0,1);c=s.Matrix([1,1,1])/s.sqrt(3)
C=c*c.H;P=s.eye(3)-C;h=H0*c;H=P*H0*P;V=H-H0
V_expected=-h*c.H-c*h.H
check(zero_matrix(V-V_expected),'rank-two perturbation identity')
check((c.H*h)[0]==0 and V.rank()==2,'orthogonal contact vector and true rank')
check(s.factor(V.charpoly().as_expr())==s.Symbol('lambda')*(s.Symbol('lambda')**2-s.Rational(2,3)),'actual rank-two eigenvalues')
check(zero_matrix(H*c),'auxiliary contact eigenstate has zero energy')

# Actual Pauli/singlet calculation, independent of the scalar compression fixture.
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
singlet=s.Matrix([0,1,-1,0])/s.sqrt(2)
a=s.symbols('a0:3',real=True);b=s.symbols('b0:3',real=True)
spinH=sum((a[j]*s.kronecker_product(pauli[j],s.eye(2))+b[j]*s.kronecker_product(s.eye(2),pauli[j]) for j in range(3)),s.zeros(4))
spin_h=spinH*singlet
check(zero_matrix(spin_h-sum(((a[j]-b[j])*s.kronecker_product(pauli[j],s.eye(2))*singlet for j in range(3)),s.zeros(4,1))),'singlet spin difference without a multiplicity')
check(s.simplify((singlet.H*spin_h)[0])==0,'pointwise zero singlet energy expectation')
check(s.simplify((spin_h.H*spin_h)[0]-sum((a[j]-b[j])**2 for j in range(3)))==0,'pointwise Pauli norm of contact coupling')
q=s.symbols('q',real=True);k=s.symbols('k',real=True)
check(s.trigsimp(s.sin(k/2+q)-s.sin(k/2-q)-2*s.cos(k/2)*s.sin(q))==0,'relative-momentum trigonometric difference')
torus_average=s.integrate(s.sin(q)**2,(q,-s.pi,s.pi))/(2*s.pi)
check(torus_average==s.Rational(1,2),'normalized torus spectral-coupling norm')
norm_coefficient=4*torus_average
check(norm_coefficient==2,'C2 coefficient from spin and torus normalization')
for K in product([0,s.pi],repeat=3):
    squared=norm_coefficient*sum(s.cos(x/2)**2 for x in K)
    check(0<=squared<=6,'corner contact-coupling norm bound')
    check((squared==0)==all(x==s.pi for x in K),'all-pi unperturbed fiber')

# Projection/normalization is calculated directly, including nearly removed states.
P2=s.diag(0,1)
for loss in [s.Rational(0),s.Rational(1,4),s.Rational(3,4),s.Rational(99,100)]:
    chi=s.Matrix([s.sqrt(loss),s.sqrt(1-loss)])
    prepared=P2*chi/s.sqrt((chi.H*P2*chi)[0])
    distance=s.simplify(((prepared-chi).H*(prepared-chi))[0])
    check(s.simplify(distance-2*(1-s.sqrt(1-loss)))==0,'normalized projected-state distance identity')
    check(bool(distance<=2*loss),'projection distance upper bound')

# Check the time-derivative sign through independent centered finite differences.
Hn=np.array(H,dtype=complex);H0n=np.array(H0,dtype=complex);Vn=np.array(V,dtype=complex)
def comparison(t):return expm(1j*t*Hn)@expm(-1j*t*H0n)
t0=0.37
predicted=1j*expm(1j*t0*Hn)@Vn@expm(-1j*t0*H0n)
errors=[]
for step in [0.001,0.0005]:
    measured=(comparison(t0+step)-comparison(t0-step))/(2*step)
    errors.append(float(np.linalg.norm(measured-predicted)))
check(errors[1]<errors[0]/3.8 and errors[1]<1e-7,'Cook comparison derivative sign and second-order finite difference')
print('Floating Duhamel derivative errors:',errors)

# An independent absolutely continuous scalar spectral model: H0=E on
# L2([-1,1],dE), c=1/sqrt(2), normalized psi proportional to (1-E^2)^2.
# The zero extension is W^(2,1), since both the polynomial and its first
# derivative vanish at the two endpoints. No finite matrix is treated as ac.
E=s.symbols('E',real=True);t=s.symbols('t',positive=True);T=s.symbols('T',positive=True)
polynomial=(1-E**2)**2
normalization=s.sqrt(1/s.integrate(polynomial**2,(E,-1,1)))
constant=normalization/s.sqrt(2)
check(normalization==s.sqrt(315)/16,'normalized absolutely continuous packet')
for endpoint in [-1,1]:
    check(polynomial.subs(E,endpoint)==0 and s.diff(polynomial,E).subs(E,endpoint)==0,'whole-line W21 boundary traces')
bp=s.diff(polynomial,E,2);ebp=s.diff(E*polynomial,E,2)
root=s.sqrt(s.Rational(1,3));root_e=s.sqrt(s.Rational(3,5))
A=s.simplify(2*constant*(-s.integrate(bp,(E,0,root))+s.integrate(bp,(E,root,1))))
B=s.simplify(2*constant*(-s.integrate(ebp,(E,0,root_e))+s.integrate(ebp,(E,root_e,1))))
check(s.simplify(A-constant*32/(3*s.sqrt(3)))==0,'exact L1 second derivative of contact density')
check(s.simplify(B-constant*s.Rational(26,5))==0,'exact L1 second derivative of energy-weighted density')
base_transform=2*s.sin(t)/t
fourier_polynomial=s.simplify(base_transform+2*s.diff(base_transform,t,2)+s.diff(base_transform,t,4))
amplitude=constant*fourier_polynomial
amplitude_prime=s.diff(amplitude,t)
amplitude_function=s.lambdify(t,amplitude,'mpmath');derivative_function=s.lambdify(t,amplitude_prime,'mpmath')
mp.mp.dps=65
cn=mp.mpf(str(s.N(constant,70)));An=mp.mpf(str(s.N(A,70)));Bn=mp.mpf(str(s.N(B,70)))
Dn=An/mp.sqrt(3)+Bn
max_fourier_error=mp.mpf(0)
for time in [mp.mpf('0.25'),1,3,7,11,31]:
    direct=mp.quad(lambda e:cn*(1-e*e)**2*mp.exp(-1j*time*e),[-1,0,1])
    h_inner=mp.quad(lambda e:e*cn*(1-e*e)**2*mp.exp(-1j*time*e),[-1,0,1])
    av=amplitude_function(time);dv=derivative_function(time)
    discrepancy=max(abs(av-direct),abs(1j*dv-h_inner));max_fourier_error=max(max_fourier_error,discrepancy)
    check(discrepancy<mp.mpf('1e-50'),'Fourier-density normalization and h equals i a-prime')
    check(abs(av)<=An/time**2 and abs(dv)<=Bn/time**2,'both independent spectral regularity bounds')
    actual_norm=mp.sqrt(abs(av)**2/3+abs(dv)**2)
    check(actual_norm<=Dn/time**2,'full two-contact Cook integrand bound')
for order in [2,3,5]:
    actual=s.integrate(t**(-order),(t,T,s.oo))
    claimed=1/((order-1)*T**(order-1))
    check(s.simplify(actual-claimed)==0,'Cook-tail integrated power and denominator')
print('AC Fourier fixture:',json.dumps({'A2':str(A),'B2':str(B),'largest_high_precision_quadrature_difference':str(max_fourier_error)},sort_keys=True))

# C11 from actual complex matrices, including the adjoint orientation.
v=s.Matrix([1,s.I,2])/s.sqrt(6);g=s.diag(-2,1,5)
G=s.Integer(2)+3*s.I;phase=s.conjugate(G)/G
Sc=s.eye(3)+(phase-1)*v*v.H
w=(g-(v.H*g*v)[0]*s.eye(3))*v
actual_change=s.simplify(Sc.H*g*Sc-g)
claimed_change=(phase-1)*w*v.H+(s.conjugate(phase)-1)*v*w.H
check(zero_matrix(actual_change-claimed_change),'rank-one scattering-current identity with adjoints')
check(zero_matrix(Sc.H*Sc-s.eye(3)) and (v.H*w)[0]==0,'phase unitarity and centered current vector')
variance=s.simplify((w.H*w)[0]);norm_squared=s.simplify((phase-1)*s.conjugate(phase-1)*variance)
x=s.symbols('x')
check(s.factor(actual_change.charpoly(x).as_expr()-x*(x*x-norm_squared))==0,'current-change norm from actual characteristic polynomial')
packet=s.Matrix([1,2-s.I,3*s.I])
check(s.simplify((v.H*Sc*packet)[0]-phase*(v.H*packet)[0])==0,'outgoing scalar contact density multiplication')
check(s.simplify((phase-1)*s.conjugate(phase-1)-36/abs(G)**2)==0,'contact phase magnitude from positive resolvent imaginary part')
print('Exact scattering-current fixture: variance =',variance,'norm squared =',norm_squared)

# The direct-integral normalization warning, as an exact two-fiber example.
psi=s.Matrix([1,0,0,1])/s.sqrt(2);proj=s.diag(0,1,0,1)
eta=proj*psi/s.sqrt((psi.H*proj*psi)[0])
old_probs=[s.simplify(sum(abs(psi[j])**2 for j in inds)) for inds in [(0,1),(2,3)]]
actual_new=[s.simplify(sum(abs(eta[j])**2 for j in inds)) for inds in [(0,1),(2,3)]]
losses=[s.Rational(1,2),s.Rational(0)];loss=sum(losses)
reported_new=[(old_probs[j]-losses[j])/(1-loss) for j in range(2)]
check(actual_new==reported_new,'global projection reweights total-momentum fibers')
tv=sum(abs(a-b) for a,b in zip(actual_new,old_probs))/2
check(old_probs!=actual_new and tv==loss==s.Rational(1,2),'unchanged-K-law claim fails and TV-loss bound is sharp')
print('Exact global-normalization discriminator: old =',old_probs,'new =',actual_new,'TV = loss =',tv)
print('Scope: exact finite algebra and an explicit ac Fourier packet; floating finite-time derivative control; no finite-matrix claim of infinite wave operators or threshold proof.')
print('TOTAL: PASS='+str(checks)+' FAIL=0')
print('Helper SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
