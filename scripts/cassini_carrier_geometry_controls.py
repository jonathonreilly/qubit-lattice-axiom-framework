"""Exact finite-voltage geometry and receiver-reference controls."""
AUDIT_TIMEOUT_SEC = 180
from fractions import Fraction as Q
import cmath,math
import numpy as np
import sympy as s
from cassini_carrier_estimator import amplitude_certificate
from cassini_receiver_reference import nco_increment

def controls():
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    # The completion of a complex square is checked over exact Gaussian rationals,
    # against direct residual vectors, including a zero correlation.
    for j,(z,u) in enumerate([
        ([1+2*s.I,4-3*s.I,-2+s.I],[1,s.I,-1]),
        ([1,-1,1,-1],[1,1,1,1]),
        ([s.Rational(2,3)+s.I,s.Rational(3,7)-2*s.I],[1,-s.I]),
    ]):
        n=len(z);norm=lambda v:sum(s.expand(x*s.conjugate(x)) for x in v)
        ah=sum(s.conjugate(v)*x for x,v in zip(z,u))/n
        E=s.simplify(norm(z)-n*ah*s.conjugate(ah))
        for k,c in enumerate([0,1+2*s.I,ah]):
            residual=norm([x-c*v for x,v in zip(z,u)])
            check(f'complex_projection_{j}_{k}',s.simplify(residual-E-n*(c-ah)*s.conjugate(c-ah))==0)
        check(f'orthogonal_residual_{j}',s.simplify(sum(s.conjugate(v)*(x-ah*v) for x,v in zip(z,u)))==0)
    # Same samples admit distinct nonzero carriers when discrepancy is unrestricted.
    z=np.array([1+2j,4-3j,-2+1j]);t=np.array([0.,.001,.002])
    for f in [-99.25,78.125]:
        c=2-3j;u=np.exp(2j*np.pi*f*t);eta=z-c*u
        check(f'unbounded_discrepancy_witness_{f}',np.allclose(c*u+eta,z,rtol=0,atol=1e-14))
    # Phase disk tangent construction, plus exact tangent-circle and full-circle domains.
    for r,rho in [(5.,3.),(13.,5.),(1.,.25)]:
        a=math.asin(rho/r);c=r*math.cos(a)*cmath.exp(1j*a)
        check(f'phase_disk_tangent_{r}_{rho}',abs(abs(c-r)-rho)<1e-12 and abs(cmath.phase(c)-a)<1e-12)
        check(f'opposite_phase_excluded_{r}_{rho}',abs(-r-r)>rho)
    check('tangent_origin_not_all_phases',abs((-1+0j)-1)>1 and abs(0-1)==1)
    chat=-1+0j;c=-1-.1j
    check('circular_phase_across_principal_cut',abs(c-chat)<.25 and abs(cmath.phase(c/chat))<math.asin(.25) and abs(cmath.phase(c)-cmath.phase(chat))>6)
    for angle in [0.,.7,2.,3.]:
        check(f'disk_strictly_contains_origin_{angle}',abs(.1*cmath.exp(1j*angle)-1)<1.2)
    # Quantizer cells: an exact within-cell constant-modulus family must survive.
    a=amplitude_certificate([3,-3,-3,3],[3,3,-3,-3])
    check('constant_modulus_cell_accepted',not a['quantization_only_rejected'] and not a['common_amplitude_intersection_empty'])
    a=amplitude_certificate([1,1001],[1,1])
    check('amplitude_variation_certificate',a['constant_amplitude_residual_lower_numerator']==995992 and a['quantization_only_rejected'])
    check('disjoint_radius_certificate',a['max_cell_radius_lower_squared']==1000000 and a['min_cell_radius_upper_squared']==8)
    # Midpoint frequency holds are not the same as a continuous cubic phase.
    F1,F2,F3,h,x=s.symbols('F1 F2 F3 h x', real=True)
    P=lambda v:F1*v+F2*v**2/2+F3*v**3/3
    F=lambda v:F1+F2*v+F3*v*v
    check('midpoint_hold_join_error',s.expand(P(x+h)-P(x)-h*F(x+h/2)-F3*h**3/12)==0)
    # Archived polynomial derivative and integrated phase use exact rational coefficients.
    row={'nco_F':[Q(12345,16),Q(-7,32),Q(3,128)],
         'nco_P':[Q(9,5),Q(12345,16),Q(-7,64),Q(1,128)]}
    for d in [Q(0),Q(1,2000),Q(-3,7)]:
        f1,f2,f3=row['nco_F'];p=lambda v:f1*v+f2*v*v/2+f3*v*v*v/3
        check(f'phase_increment_{d}',nco_increment(row,d)==p(1+d)-p(d))
    # Stored IEEE P and F need not be exactly rationally derivative-consistent.
    rounded={'nco_F':[1.,2.,.1],'nco_P':[0.,1.,1.,.1/3]}
    check('archived_phase_not_rounded_frequency',nco_increment(rounded,Q(0))==2+Q(.1/3) and nco_increment(rounded,Q(0))!=2+Q(.1)/3)
    ref=Q(2117064000);lo=Q(8430000000);N=Q(1192222525,1000)
    expected=Q(1863016320000,221)-Q(192222525,1000)
    check('S_exciter_X_downlink_factor',Q(880,221)==Q(11,3)*Q(240,221))
    check('pre_NSP_reference_minus_count',Q(880,221)*ref-(N-10**6)==expected)
    check('no_extra_96_multiplier',96*Q(880,221)*ref-(N-10**6)!=expected)
    check('counter_bias_units',Q(880,221)*ref-(N-1000)!=expected)
    check('counter_sign_matters',Q(880,221)*ref+(N-10**6)!=expected)
    # Analytic grid-cover bound on explicit deterministic examples, without pretending
    # that a floating FFT is a rigorous numerical interval enclosure.
    t=np.array([-.0015,-.0005,.0005,.0015]);z=np.array([1+2j,-4+3j,2-1j,3+4j])
    A=lambda f:np.dot(z,np.exp(-2j*np.pi*f*t))
    L=2*np.pi*sum(abs(t*z))
    for f,g in [(-31.,2.),(99.,99.001),(420.,-300.)]:
        check(f'correlation_Lipschitz_{f}_{g}',abs(A(f)-A(g))<=L*abs(f-g)+1e-12)
    return checks

if __name__=='__main__':
    import json
    print(json.dumps(controls(),indent=2))
