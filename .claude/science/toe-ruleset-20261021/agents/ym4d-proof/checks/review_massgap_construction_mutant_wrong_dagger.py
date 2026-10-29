#!/usr/bin/env python3
"""Finite author controls only. See mass_gap_construction_criteria.md."""
import json
import math
import platform
from fractions import Fraction

import numpy as np
import scipy
from scipy.special import iv
import sympy as sp

checks = []
diagnostics = {}

def check(name, passed, detail, kind="check"):
    checks.append({"name": name, "kind": kind, "passed": bool(passed), "detail": detail})

z = sp.Symbol("z")
mom = {2*k: sp.catalan(k)/sp.Integer(4)**k for k in range(8)}
Z_mom = sum(mom[2*k]*z**(2*k)/sp.factorial(2*k) for k in range(8))
Z_bes = sum(z**(2*k)/(sp.Integer(4)**k*sp.factorial(k)*sp.factorial(k+1)) for k in range(8))
check("Haar_moment_Bessel_normalizer", sp.expand(Z_mom-Z_bes)==0,
      "Independent Catalan-moment and Bessel defining-series normalizers agree through z^14.")
b_mom = sp.series(sp.diff(Z_mom,z)/Z_mom,z,0,12).removeO()
I1 = z*Z_bes/2
I2 = sum((z/2)**(2*k+2)/(sp.factorial(k)*sp.factorial(k+2)) for k in range(8))
b_bes = sp.series(I2/I1,z,0,12).removeO()
check("normalized_first_moment", sp.expand(b_mom-b_bes)==0,
      str(b_mom))
check("first_three_coefficients", [b_mom.coeff(z,k) for k in (1,3,5)] ==
      [sp.Rational(1,4),-sp.Rational(1,96),sp.Rational(1,1536)],
      "z/4-z^3/96+z^5/1536")
# Two gauge-averaged center sectors, both plaquette signs equal the common sign.
image_cov = sp.series(b_mom**8,z,0,12).removeO().expand()
unnormalized_cov = sp.series(sp.diff(Z_mom,z)**8,z,0,12).removeO().expand()
check("disjoint_plaquette_order_eight", image_cov.coeff(z,8)==sp.Rational(1,4**8),
      str(image_cov))
check("normalizer_omission_control", image_cov.coeff(z,10)!=unnormalized_cov.coeff(z,10),
      {"correct_order_10":str(image_cov.coeff(z,10)),
       "omitted_Z_order_10":str(unnormalized_cov.coeff(z,10))}, "negative_control")
check("repeated_link_product_control", mom[2] != 0**2,
      "E_Haar[w(V)^2]=1/4, while E_Haar[w(V)]^2=0.","negative_control")

# Deterministic Haar quadrature, independent of the power series.
Q=600
th=np.arange(1,Q+1)*np.pi/(Q+1)
x=np.cos(th)
w=2*np.sin(th)**2/(Q+1)
quad_rows=[]
for zz in (0.,.125,.5,1.,3.,8.):
    weighted=w*np.exp(zz*x)
    zq=float(weighted.sum())
    m1=float((weighted*x).sum()/zq)
    m2=float((weighted*x*x).sum()/zq)
    if zz==0:
        zb=1.; b=0.; c2=.25
    else:
        zb=float(2*iv(1,zz)/zz)
        b=float(iv(2,zz)/iv(1,zz))
        # Independent analytic identity: Z''/Z=1-3 b/z (S^3 radial ODE).
        c2=1-3*b/zz
    err=max(abs(zq-zb),abs(m1-b),abs(m2-c2))
    check(f"Haar_quadrature_z_{zz}",err<2e-11,{"maximum_absolute_error":err})
    quad_rows.append({"z":zz,"Z":zq,"mean":m1,"second_moment":m2,"max_error":err})
diagnostics["Haar_quadrature"]=quad_rows

# Exact noncommuting rational unit-quaternion control.
def qmul(a,b):
    return (a[0]*b[0]-sum(a[i]*b[i] for i in (1,2,3)),
      a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
      a[0]*b[2]+a[2]*b[0]+a[3]*b[1]-a[1]*b[3],
      a[0]*b[3]+a[3]*b[0]+a[1]*b[2]-a[2]*b[1])
def qad(a): return a
def loop(es): return qmul(qmul(qmul(es[0],es[1]),qad(es[2])),qad(es[3]))
F=Fraction
qs=[(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0)),
    (F(8,17),F(0),F(0),F(15,17)),(F(7,25),F(24,25),F(0),F(0))]
check("rational_quaternion_unit",all(sum(v*v for v in q)==1 for q in qs),
      "Four exact noncommuting SU(2) unit quaternions.")
correct=loop(qs)[0]
wrong=qmul(qmul(qmul(qs[0],qs[1]),qs[2]),qad(qs[3]))[0]
check("orientation_dagger_control",correct!=wrong,
      {"oriented_trace":str(correct),"wrong_dagger_trace":str(wrong)},"negative_control")
h=[qs[1],qs[2],qs[3],qs[0]]
ends=[(0,1),(1,2),(3,2),(0,3)]
gauged=[qmul(qmul(h[i],q),qad(h[j])) for q,(i,j) in zip(qs,ends)]
check("loop_root_gauge_covariance",loop(gauged)[0]==correct,
      "Exact rational vertex gauge transformation preserves the loop trace.")
noise_rows=[]
for ll in (.125,.5,1.,3.):
    b=float(iv(2,ll)/iv(1,ll))
    cov=b**8
    check(f"two_sector_noise_lambda_{ll}",cov>0,
          {"coarse_loop_covariance_at_every_separation":cov})
    noise_rows.append({"lambda":ll,"covariance":cov})
diagnostics["two_sector_noise"]=noise_rows
J,H=sp.symbols("J H",real=True)
mgf=(sp.exp(J+H)+sp.exp(-J-H))/2
source_cov=sp.diff(sp.log(mgf),J,H).subs({J:0,H:0})
check("lambda_zero_source_only_term",source_cov==1,
      "At K_0=1, the coarse field is Haar but d_J d_H log Z(J,H)=1.")
check("discard_source_only_term_control",source_cov != 0,
      "Dropping the source-dependent field-independent term changes the exact mixed derivative.","negative_control")

# Single spatial cycle: a controlled class-function implementation of the
# complete finite transfer, not a spatial three-dimensional box calculation.
def cycle_transfer(beta,D,Q):
    theta=np.arange(1,Q+1)*np.pi/(Q+1)
    weights=2*np.sin(theta)**2/(Q+1)
    chars=np.sin(np.arange(1,D+1)[:,None]*theta)/np.sin(theta)
    mult=np.exp((beta/2)*np.cos(theta)) # field-independent factor omitted
    mat=(chars*(weights*mult))@chars.T
    r=iv(np.arange(1,D+1),beta)/iv(1,beta)
    trans=(mat*(r**4))@mat.T
    eig=np.linalg.eigvalsh(trans)
    ratio=float(eig[-2]/eig[-1])
    return eig,ratio,r,trans
cycle_rows=[]
for beta in (.25,1.,3.,8.):
    e,r,rs,T=cycle_transfer(beta,36,160)
    ee,rr,_,_=cycle_transfer(beta,48,240)
    error=max(abs(float(e[-1]/ee[-1])-1),abs(r-rr))
    symmetry=float(np.max(np.abs(T-T.T)))
    positivity=float(e[0])
    bound=-math.expm1(-8*beta)
    check(f"cycle_convergence_beta_{beta}",error<2e-9,
          {"leading_value_relative_or_ratio_error":error})
    check(f"cycle_positive_symmetric_beta_{beta}",symmetry<2e-12 and positivity>-2e-12,
          {"symmetry_error":symmetry,"smallest_numeric_eigenvalue":positivity})
    check(f"cycle_full_gap_bound_beta_{beta}",0<r<1 and (1-r)>math.exp(-8*beta) and e[-1]>e[-2],
          {"ratio":r,"minorization_ratio_upper_bound_float":bound,
           "spectral_ratio_gap":1-r,"minorization":math.exp(-8*beta)})
    cycle_rows.append({"beta":beta,"top_eigenvalue":float(e[-1]),"ratio":r,
        "kinetic_only_ratio":float(rs[1]**4),"ratio_bound":bound,"convergence_error":error})
diagnostics["cycle_transfer"]=cycle_rows
check("spatial_factor_omission_control",any(abs(q["ratio"]-q["kinetic_only_ratio"])>1e-5 for q in cycle_rows),
      "At least one actual finite-cycle ratio changes when the spatial plaquette factor is omitted.","negative_control")
wrong_character_ratio=float(2*iv(2,8.)/iv(1,8.))
check("representation_dimension_control",wrong_character_ratio>1,
      {"wrong_coefficient_ratio":wrong_character_ratio,
       "correct_convolution_ratio":float(iv(2,8.)/iv(1,8.))},"negative_control")
check("gauge_cycle_power_control",float(iv(2,1.)/iv(1,1.))!=float((iv(2,1.)/iv(1,1.))**4),
      "Four-edge gauge-invariant cycle transports each edge: r_1^4, not r_1.","negative_control")

# Ground-state transform identity with a nonconstant positive spatial factor.
r0=.4
base=np.array([[1.,r0],[r0,1.]])
K=np.kron(base,base)
A=np.array([2.,1.,3.,4.])
T=A[:,None]*K*A[None,:]
eig,vec=np.linalg.eigh(T)
psi=vec[:,-1]
if psi.sum()<0: psi=-psi
lam=eig[-1]
P=T*psi[None,:]/(lam*psi[:,None])
nu=A*psi/(A@psi)
pi=psi**2/(psi@psi)
P2=K*nu[None,:]/(K@nu)[:,None]
eps=float(K.min()/K.max())
check("Doob_stochastic_reversible",np.max(abs(P.sum(axis=1)-1))<1e-13 and
      np.max(abs(pi[:,None]*P-(pi[:,None]*P).T))<1e-13,
      {"row_error":float(np.max(abs(P.sum(axis=1)-1)))})
check("Doob_exact_denominator",np.max(abs(P-P2))<1e-13,
      "Perron equation removes A(U) only after the correct row denominator.")
check("Doob_minorization",float(np.min(P/nu[None,:]))>=eps-1e-13,
      {"minimum_density_ratio":float(np.min(P/nu[None,:])),"m_over_M":eps})
check("omitted_Perron_control",np.max(abs((T/lam).sum(axis=1)-1))>1e-2,
      "T/lambda_0 itself is not stochastic for this nonconstant multiplier.","negative_control")
for name,wrong_eps in (("factor_two",math.exp(-4.)),("link_count",math.exp(-2.))):
    x0=4.
    Q2=np.array([[math.exp(x0),math.exp(-x0)],[math.exp(-x0),math.exp(x0)]])
    Pq=Q2/Q2.sum(axis=1)[:,None]
    minimum=float(np.min(Pq/.5))
    check(name+"_minorization_control",minimum<wrong_eps,
          {"actual_minimum_density_ratio":minimum,"wrong_minorization":wrong_eps},"negative_control")

# Electric kinetic gap does not generally survive positive multiplication.
r=sp.Rational(1,2); a0=sp.Integer(3)
kin_ratio=(1-r)/(1+r)
top=(sp.Integer(25)+4*sp.sqrt(34))/4
nontrivial=sp.Rational(27,4)
ratio=nontrivial/top
check("electric_gap_inheritance_control",bool(ratio>kin_ratio),
      {"magnetic_ratio_exact":str(ratio),"magnetic_ratio":float(ratio),
       "kinetic_ratio":str(kin_ratio)},"negative_control")
base=np.array([[1.,.5],[.5,1.]])
mult=np.array([3.,1.,1.,3.])
T=mult[:,None]*np.kron(base,base)*mult[None,:]
e=np.linalg.eigvalsh(T)
check("electric_control_exact_vs_matrix",abs(e[-1]-float(top))<1e-12 and
      abs(e[-2]-float(nontrivial))<1e-12,
      "Independent matrix eigensolve matches the exact two-dimensional reduction.")

volume_rows=[{"n":n,"spatial_edges":3*n**3,"log_minorization":-6*n**3} for n in (4,8,16)]
check("finite_volume_bound_degradation",all(volume_rows[i+1]["log_minorization"]<volume_rows[i]["log_minorization"] for i in (0,1)),
      "Only the explicit lower-bound certificate degenerates; no physical-gap upper bound follows.")
diagnostics["volume_minorization"]=volume_rows

result={
 "scope":"Finite author checks; no continuum infrared bound and no independent review",
 "runtime":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"sympy":sp.__version__},
 "resolution_certificate":{
  "per_element":"Exact SU(2) Haar moments and normalization coefficients checked through the declared finite orders.",
  "per_site":"Single-link normalized moments and finite vertex gauge covariance checked; no infinite gauge fixing is used.",
  "per_mode":"Finite character-mode transfer diagnostics checked with two truncations; no complete continuum spectrum computed.",
  "per_block":"Disjoint and repeated-link loop controls and the finite spatial-cycle transfer checked at their written scopes.",
  "lattice_wide":"Checked and not executed — no cutoff/volume-uniform physical infrared estimate has been supplied or tested."},
 "summary":{"passed":sum(x["passed"] for x in checks),"failed":sum(not x["passed"] for x in checks),
            "negative_controls":sum(x["kind"]=="negative_control" for x in checks)},
 "checks":checks,"diagnostics":diagnostics}
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(bool(result["summary"]["failed"]))
