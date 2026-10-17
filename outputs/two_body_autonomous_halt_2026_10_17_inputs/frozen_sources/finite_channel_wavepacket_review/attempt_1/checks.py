#!/usr/bin/env python3
"""Exact local discriminators for selected steps of the generic proof.

This is not a scattering fit, interval certificate, or numerical proof of
the infinite-time theorem. The analytical review is in REVIEW.md.
"""
from pathlib import Path
import hashlib, json, platform, resource, sys, time
resource.setrlimit(resource.RLIMIT_CPU,(15,15))
import sympy as s
started=time.monotonic()
J,z,q,r,alpha,sk=s.symbols('J z q r alpha sin_k',nonzero=True)
open_recurrence=s.simplify((z+1/z)*(z**-2+r*z**2)
                          -(z**-3+r*z**3)-(z**-1+r*z))
closed_recurrence=s.simplify((q+1/q)*alpha-alpha*q-alpha/q)
assert open_recurrence==closed_recurrence==0
D=J*(z+1/z)
M=s.Matrix([[D,-J,0],[-J,D,-J*z**2],[0,-J,J*z]])
rhs=s.Matrix([0,J/z**2,-J/z])
free=s.Matrix([1-z**2,1/z-z**3,-z**2])
assert s.simplify(M*free-rhs)==s.zeros(3,1)
ztest=s.Rational(3,5)+s.I*s.Rational(4,5)
wrong_free_residual=s.simplify((z-1/z).subs(z,ztest))
assert wrong_free_residual!=0  # Replacing the row-zero free phase by -1 fails.
omitted_incoming=s.simplify(M*free-s.Matrix([0,J/z**2,0]))
assert omitted_incoming!=s.zeros(3,1)
qprime=2*sk*q**2/(1-q**2)
assert s.simplify(qprime*(1-q**-2)+2*sk)==0
assert s.simplify(-qprime/q**2+2*sk/(1-q**2))==0
x=s.symbols('x')
geometric=s.simplify(s.diff(x*s.diff(1/(1-x),x),x))
assert s.simplify(geometric-(1+x)/(1-x)**3)==0

sigma=s.symbols('sigma',positive=True)
y=s.symbols('y',real=True)
f=s.sqrt(15)/(4*s.sqrt(sigma))*(1-y*y)
packet_l2=s.simplify(s.integrate(f*f*sigma,(y,-1,1)))
packet_l1=s.simplify(s.integrate(f*sigma,(y,-1,1)))
packet_derivative_l1=s.simplify(2*s.integrate(-s.diff(f,y),(y,0,1)))
assert packet_l2==1
assert packet_l1==s.sqrt(15*sigma)/3
assert packet_derivative_l1==s.sqrt(15)/(2*s.sqrt(sigma))

# Direct-action discriminator, rather than the author's Gram eigenvalue test.
P=s.ones(2,2)/2;I=s.eye(2);unit_phase=s.Rational(3,5)+4*s.I/5
U=I+(unit_phase-1)*P;E=U-I;v=s.Matrix([1,1])/s.sqrt(2)
assert s.simplify(U.conjugate().T*U)==I
column_sq=s.simplify((E[:,0].conjugate().T*E[:,0])[0])
joint_sq=s.simplify(((E*v).conjugate().T*(E*v))[0])
assert column_sq==s.Rational(2,5) and joint_sq==s.Rational(4,5)
assert joint_sq>column_sq

# Exact finite-polynomial locality with noncommuting internal interactions.
jt=s.Rational(1,4);B=s.diag(1,3)
V0=s.Matrix([[0,s.Rational(1,3)],[s.Rational(1,3),0]])
V1=s.diag(s.Rational(1,5),-s.Rational(1,5))
assert B*V0-V0*B!=s.zeros(2)
def hamiltonian(length):
    hc=s.eye(length)*2*jt
    for n in range(length-1):hc[n,n+1]=hc[n+1,n]=-jt
    H=s.kronecker_product(hc,s.eye(2))+s.kronecker_product(s.eye(length),B)
    H[:2,:2]+=V0;H[2:4,2:4]+=V1
    return H
N=2;Mclock=4;L=7;distance=Mclock-N+1
H=hamiltonian(L);HM=hamiltonian(Mclock)
c=s.Rational(5,2);rho=s.Rational(11,6)
A=(H-c*s.eye(2*L))/rho;AM=(HM-c*s.eye(2*Mclock))/rho
incoming=s.zeros(2*L,2);incoming[2*(N-1):2*N,:]=s.eye(2)
small=incoming[:2*Mclock,:]
def embed(value):return value.col_join(s.zeros(2*(L-Mclock),value.cols))
differences=[]
for k in range(distance+1):
    diff=A**k*incoming-embed(AM**k*small)
    differences.append(diff)
    if k<distance:assert diff==s.zeros(2*L,2)
expected=s.zeros(2*L,2);expected[2*Mclock:2*(Mclock+1),:]=(-jt/rho)**distance*s.eye(2)
assert differences[distance]==expected and expected!=s.zeros(2*L,2)
cheb3=4*A**3*incoming-3*A*incoming
cheb3_small=4*AM**3*small-3*AM*small
assert cheb3-embed(cheb3_small)==4*expected

result=dict(
    scope='Exact local algebra and convention discriminators only; no whole-theorem numerical certification',
    matching=dict(open_bulk_recurrence=str(open_recurrence),closed_bulk_recurrence=str(closed_recurrence),
                  free_reflection='r0=-z**2',free_matching_residual='zero 3-vector',
                  wrong_constant_reflection_entrance_residual=str(wrong_free_residual),
                  omitted_incoming_term_residual=str(omitted_incoming),
                  q_derivative=str(qprime),q_inverse_derivative=str(s.simplify(-qprime/q**2))),
    tail_and_packet=dict(geometric_derivative_sum=str(geometric),L2_squared=str(packet_l2),
                         F0=str(packet_l1),F1=str(packet_derivative_l1)),
    column_norm=dict(each_column_squared=str(column_sq),aligned_input_squared=str(joint_sq),
                     max_column_rule_rejected=bool(joint_sq>column_sq)),
    finite_locality=dict(J=str(jt),B=str(B),V0=str(V0),V1=str(V1),
                         B_V0_commutator=str(B*V0-V0*B),N=N,M=Mclock,comparison_length=L,
                         first_omitted_hop=distance,exact_agreement_degrees=list(range(distance)),
                         first_nonzero_power_amplitude=str((-jt/rho)**distance),
                         first_nonzero_Chebyshev_amplitude=str(4*(-jt/rho)**distance),
                         equality_one_degree_too_far_rejected=True),
    versions=dict(python=sys.version,sympy=s.__version__,platform=platform.platform()),
    dimensions=dict(maximum_matrix_dimension=14,matching_dimension=3,logical_dimension=2),
    cpu_seconds_cap=15,elapsed_seconds_after_import=time.monotonic()-started,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(result,indent=2))
