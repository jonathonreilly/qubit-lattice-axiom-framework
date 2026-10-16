#!/usr/bin/env python3
"""Author controls for PHYSICAL_PORT_BRIDGE_v1; synthetic, not empirical."""
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 120
HERE = Path(__file__).resolve().parent
checks = []

def record(name, ok, detail=None):
    checks.append({"name": name, "passed": bool(ok), "detail": detail})
def eq(name, lhs, rhs):
    rem = sp.simplify(lhs-rhs)
    record(name, rem == 0, str(rem))
def near(name, value, reference, tol=1e-10):
    record(name, abs(value-reference) <= tol, {"value": float(value), "reference": float(reference), "tolerance": tol})

q, i, t = sp.symbols("q i t", real=True)
phi = q+q**3
k = sp.diff(phi,q)
L = 2+q**2
K = 1+q
H = sp.cos(q)
W0 = sp.cos(2*q)
W = W0+i*phi+L*i**2/2+K*i**3/3+H*i**4/4
flux = sp.diff(W,i)
corr = (sp.diff(L,q)*i**2/2+sp.diff(K,q)*i**3/3+sp.diff(H,q)*i**4/4)/k
eq("coenergy_force_in_flux_coordinate", sp.diff(W,q)/k-sp.diff(W0,q)/k, i+corr)
eq("coenergy_flux_derivative", flux, phi+L*i+K*i**2+H*i**3)
eq("mixed_derivative_reciprocity",sp.diff(sp.diff(W,q),i),sp.diff(flux,q))
q1,q2=sp.symbols("q1 q2",real=True)
work=(W-W0).subs(q,q2)-(W-W0).subs(q,q1)
eq("finite_bias_work_from_flux_differences",work,sp.integrate(flux.subs(q,q2)-flux.subs(q,q1),(i,0,i)))
eq("flux_origin_and_current_only_offset_cancel",sp.diff(flux+sp.sin(i)+7,q),sp.diff(flux,q))
lc=sp.diff(L,q)*i**2/(2*k)
eq("linear_inductance_even_force_term",((i+lc)-(-i+lc))/2,i)
record("nonlinear_odd_force_not_removed_by_current_reversal",sp.simplify(((i+corr)-(-i+corr.subs(i,-i)))/2-i) != 0)

b=phi
good_a=k
bad_a=sp.Integer(1)
eq("true_reciprocal_after_coordinate_change",good_a/k,sp.diff(b,q)/k)
eq("naive_sensor_relabel_false_pass",sp.Integer(1),sp.diff(b,q)/k)
record("proper_transform_rejects_false_pass",sp.diff((bad_a/k)/(sp.diff(b,q)/k),q) != 0)
record("naive_sensor_relabel_false_rejection",sp.diff(good_a/(sp.diff(b,q)/k),q) != 0)
gx,gj,lam=sp.symbols("gx gj lam",nonzero=True,real=True)
a0,b0=sp.symbols("a0 b0",nonzero=True,real=True)
eq("constant_gain_product_sets_reciprocity_factor",gj*lam*b0/(b0/gx),gx*gj*lam)

# Flux coordinate from integrating independently imposed motion voltage.
for alpha in [0.2,0.9]:
    def path(tt): return 0.1+alpha*tt**2
    def voltage(tt): return (1+3*path(tt)**2)*2*alpha*tt
    val=quad(voltage,0,1.3,epsabs=1e-13)[0]
    f=lambda z:z+z**3
    near("motion_voltage_integral_"+str(alpha),val,f(path(1.3))-f(path(0)))
near("voltage_offset_accumulation",quad(lambda tt:0.003,0,1.3)[0],0.003*1.3)

# An exact mechanical/actuator synthetic model with arbitrary initial states.
# Actuator flux is phi(q) + (2+0.02*q)*I, so J=I+0.01*I^2/k(q).
A=np.array([[0.,1.],[-2.3,-0.4]])
tau=1.4
Delta=0.35
T=expm(A*Delta)
s,p=np.trace(T),np.linalg.det(T)
weights=np.array([-p,s+p,-(1+s),(s+p)/p,-(1+s)/p,1/p])
def phi_f(z): return z+z**3
def k_f(z): return 1+3*z*z
def evolve(z0,dt,qheld):
    M=expm(A*dt)
    f=np.array([0.,-phi_f(qheld)/tau])
    return M@z0+np.linalg.solve(A,(M-np.eye(2))@f)
def current_from_J(J,qheld):
    c=0.01/k_f(qheld)
    return 2*J/(1+np.sqrt(1+4*c*J))
def force_reading(z,qheld): return 0.2*qheld+z[0]  # a_bar=1
def samples(qx,qy,z0):
    before=[force_reading(evolve(z0,n*Delta,qx),qx) for n in [-2,-1,0]]
    end=evolve(z0,Delta,qy)
    after=[force_reading(evolve(end,(n-1)*Delta,qx),qx) for n in [2,3,4]]
    J=np.array(before+after)
    I=np.array([current_from_J(v,qx) for v in J])
    corrected=I+0.01*I**2/k_f(qx)
    exact=force_reading(end,qx)-force_reading(evolve(z0,Delta,qx),qx)
    return J,I,corrected,exact
errs=[];raw_errors=[]
for qx,qy,z0 in [(0.1,0.8,np.array([0.3,-0.7])),(0.6,0.2,np.array([1.5,0.9])),(0.2,0.9,np.array([-1.1,0.4]))]:
    J,I,corrJ,expected=samples(qx,qy,z0)
    errs.append(abs(weights@corrJ-expected))
    raw_errors.append(abs(weights@I-expected))
record("corrected_port_restores_six_sample_inverse",max(errs)<2e-12,{"maximum_absolute_error":max(errs)})
record("uncorrected_current_biases_same_inverse",max(raw_errors)>1e-5,{"errors":raw_errors})
record("six_sample_error_weight_bound",abs(weights@np.sign(weights)) <= np.linalg.norm(weights,1)+1e-14,{"weight_l1":float(np.linalg.norm(weights,1))})

# C1 interval bound: independent complex perturbations; no Gaussian claims.
def force(V,I,Z,v,m,a,X): return (V*I-Z*I**2)/v-m*a-X
def bound(V,I,Z,v,m,a,eV,eI,eZ,ev,em,ea,eX):
    if abs(v)<=ev: raise ValueError("velocity margin absent")
    MI,MV,MZ,MN=abs(I),abs(V),abs(Z),abs(V*I-Z*I**2)
    eN=MI*eV+MV*eI+eV*eI+MI**2*eZ+MZ*(2*MI*eI+eI**2)+eZ*(2*MI*eI+eI**2)
    return eN/(abs(v)-ev)+MN*ev/(abs(v)*(abs(v)-ev))+abs(m)*ea+abs(a)*em+em*ea+eX
rng=np.random.default_rng(20261016)
worst=0.
for n in range(600):
    vals=rng.normal(size=7)+1j*rng.normal(size=7)
    vals[3]+=3
    vals[4]=abs(vals[4]);vals[5]=vals[5].real;vals[6]=vals[6].real
    eps=np.array([0.02,0.01,0.03,0.01,0.005,0.02,0.01])
    errors=eps*np.exp(2j*np.pi*rng.random(7))*rng.random(7)
    errors[4:]=eps[4:]*rng.uniform(-1,1,3)
    V,I,Z,v,m,a,X=vals
    B=bound(V,I,Z,v,m,a,*eps)
    error=abs(force(*(vals+errors))-force(*vals))
    worst=max(worst,float(error/B))
record("complex_force_interval_bound_600_draws",worst<=1+1e-12,{"max_error_over_bound":worst})
guard=False
try: bound(1,1,1,0,1,1,.1,.1,.1,.1,.1,.1,.1)
except ValueError: guard=True
record("zero_velocity_guard",guard)
near("published_design_impedance_budget_arithmetic",8*0.0005,0.004)
near("published_design_uncorrected_drift_arithmetic",8*0.01,0.08)

# Green energy bound and physical edge controls.
edge_max=0.
for Omega,Gamma in [(0.4,0),(3.,0),(8.,0),(2.,0.5),(1.,3.)]:
    M=np.array([[0.,1.],[-Omega**2,-Gamma]])
    for zt in np.linspace(0,2,150):
        g,gp=expm(M*zt)@np.array([0.,1.])
        E=(gp**2+Omega**2*g**2)/2
        edge_max=max(edge_max,float(E))
        assert abs(g)<=zt+1e-12
record("passive_green_energy_and_time_envelope",edge_max<=0.5+1e-12,{"maximum_energy":edge_max})
Om=2*np.pi;r=.25
g=lambda z:np.sin(Om*z)/Om
ideal=quad(lambda z:g(1-z),0,1,epsabs=1e-13)[0]
sym=lambda z:min(z/r,1.,(1-z)/r)
first=lambda z:min(z/r,1.)
symmetric=quad(lambda z:g(1-z)*sym(z),0,1,points=[r,1-r],epsabs=1e-13)[0]
asym=quad(lambda z:g(1-z)*first(z),0,1,points=[r],epsabs=1e-13)[0]
expected=1/(4*np.pi**2)-1/(2*np.pi**3)
near("ideal_full_period_pulse_endpoint_zero",ideal,0.)
near("symmetric_ramp_can_share_zero_endpoint",symmetric,0.)
near("asymmetric_ramp_endpoint_exact",asym,expected)
record("asymmetric_ramp_breaks_ideal_endpoint",abs(asym)>0.009,{"actual_endpoint_integral":asym})
record("edge_error_envelope",abs(asym-ideal)<=1.*1.*r,{"absolute_error":abs(asym-ideal),"bound":r})

result={"source_note":"PHYSICAL_PORT_BRIDGE_v1.md","source_sha256":hashlib.sha256((HERE/"PHYSICAL_PORT_BRIDGE_v1.md").read_bytes()).hexdigest(),"runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"claims":"Author symbolic/numeric controls; standard calibration physics remains adopted. Published design arithmetic is not observed performance.","empirical_validation":False,"checks":checks,"summary":{"passed":sum(c["passed"] for c in checks),"failed":sum(not c["passed"] for c in checks)}}
print(json.dumps(result,indent=2))
sys.exit(bool(result["summary"]["failed"]))

