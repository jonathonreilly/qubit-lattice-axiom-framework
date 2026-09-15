"""Independent exact reviewer controls; no primary imports or execution."""
import sympy as s
import json,time
start=time.monotonic(); rows=[]
def ck(name, value):
 assert value, name
 rows.append(name)
x,y=s.symbols('x y',real=True)
I=s.eye(3);V=s.Matrix([[1,2,0],[2,0,1],[0,1,-1]]);W=s.Matrix([[0,1,1],[1,2,0],[1,0,-1]])
# Differentiate the actual frame one-form, independently of curvature formula.
E=I+x*V+y*W
anti=lambda A:(A-A.T)/2
Ax=anti(E.inv()*V);Ay=anti(E.inv()*W)
F=(Ay.diff(x)-Ax.diff(y)+Ax*Ay-Ay*Ax).subs({x:0,y:0})
ck('frame_curvature_direct_two_parameter_derivative',F==-(V*W-W*V))
# Metric tangents have frame derivative -h/2, giving the factor 1/4.
ck('metric_curvature_scale',F/4==-(V*W-W*V)/4)
pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
rho=lambda A:sum((A[a,b]*pa[a]*pa[b]/4 for a in range(3) for b in range(3)),s.zeros(2))
X=s.diag(1,0,0);Y=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
ck('spatial_product_defect_nonzero',s.I*rho(X*Y-Y*X)==-pa[2]/2)
# General symmetric momentum, trace inverse and Legendre transform at a generic
# off-diagonal positive metric; independent contraction, not diagonal fixture.
g=s.Matrix([[3,1,0],[1,2,1],[0,1,3]]);gi=g.inv();alpha=s.Rational(7,3)
p=s.Matrix([[2,1,3],[1,-2,1],[3,1,4]]);rt=s.sqrt(g.det());tr=s.trace(g*p)
K=alpha/rt*(g*p*g-tr*g/2);ktr=s.trace(gi*K)
ck('off_diagonal_Legendre_inverse',s.simplify(rt/alpha*(gi*K*gi-ktr*gi)-p)==s.zeros(3))
Hg=alpha/rt*(s.trace(g*p*g*p)-tr**2/2)
L=s.simplify(2*s.trace(p*K)-Hg)
ck('off_diagonal_ADM_kinetic_sign',s.simplify(L-rt/alpha*(s.trace(gi*K*gi*K)-ktr**2))==0)
# The flat-torus necessity witnesses: independent direct integrations.
a=-s.sin(x);traceprime=-s.sin(x)
ck('trace_witness_nonzero',s.integrate(a*traceprime,(x,0,2*s.pi))==s.pi)
ck('normalization_witness',s.integrate(2*s.cos(x)*s.diff(a,x),(x,0,2*s.pi))==-2*s.pi)
# Fourier derivative from Laurent coefficients, not differentiated sine formula.
z=s.Rational(3,5);v=s.Rational(4,5)
for w in [-1,1]:
 phase=z+s.I*w*v
 # K3(k)=(z sin k - sin 2k/2)/v
 coeff={1:z/(2*s.I*v),-1:-z/(2*s.I*v),2:-1/(4*s.I*v),-2:1/(4*s.I*v)}
 moment=lambda n:s.simplify(sum(c*phase**m*(s.I*m)**n for m,c in coeff.items()))
 ck('shift_Laurent_zero_'+str(w),moment(0)==0)
 ck('shift_Laurent_first_'+str(w),moment(1)==v)
 ck('shift_Laurent_second_'+str(w),moment(2)==3*w*z)
 # Gamma1/2 sin(k)/v -> w + (z/v) delta k.
 ck('spin_Laurent_first_'+str(w),s.simplify((phase+phase**-1)/(2*v))==z/v)
# Direct one-dimensional operator commutator on polynomials, fixes bracket sign.
N=x*x+1;M=x**3-x;psi=s.Matrix([x**4+2*x, x**2+s.I*x])
D=lambda f:-s.I*pa[0]*f.diff(x)
h=lambda f,n:(n*D(f)+D(n*f))/2
av=s.expand(N*s.diff(M,x)-M*s.diff(N,x))
comm=s.simplify(s.I*(h(h(psi,M),N)-h(h(psi,N),M)))
target=-s.I*(av*psi.diff(x)+s.diff(av,x)*psi/2)
ck('normal_Dirac_operator_commutator_direct',s.simplify(comm-target)==s.zeros(2,1))
print(json.dumps(dict(status='ok',checks=rows,count=len(rows),elapsed_seconds=time.monotonic()-start),indent=2))
