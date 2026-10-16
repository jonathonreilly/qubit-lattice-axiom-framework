"""Focused alternate Hessian and split-transport controls; no author import."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_v1.md",
]
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import sympy as s

ROOT=Path(__file__).resolve().parents[5]
source=ROOT/AUDIT_INPUT_PATHS[0]
initial=hashlib.sha256(source.read_bytes()).hexdigest()
rows=[];details={}
def ck(name,passed,detail=None):
    rows.append({"name":name,"passed":bool(passed),"detail":detail})
    print(json.dumps({"progress":name,"passed":bool(passed)}),file=sys.stderr,flush=True)
def zero(name,expr):
    residual=s.simplify(expr);ck(name,residual==0,str(residual))
def near(name,actual,expected):
    error=float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)))
    scale=float(np.linalg.norm(expected))
    ck(name,error<=1e-12+2e-10*scale,{"absolute_error":error,"expected_norm":scale})
ck("initial_source_binding",initial=="ebecac4abf41d8757eeefc3c188498d4acfa3419a093b32f3bf19c49df885991")

# Radial Hessian proof, independent of direct triangle differentiation.
r=s.symbols("r",positive=True);mass=s.symbols("mass",nonnegative=True)
g=s.exp(-mass*r)/r
h=(1+mass*r)*s.exp(-mass*r)/r**3
lr=s.exp(-mass*r)*((mass*r)**2+2*mass*r+2)/r**3
lt=-(1+mass*r)*s.exp(-mass*r)/r**3
B=s.exp(-mass*r)*(mass*r+2)**2/r**3
zero("radial_Hessian_eigenvalue",s.diff(g,r,2)-lr)
zero("tangential_Hessian_eigenvalue",s.diff(g,r)/r-lt)
zero("kernel_gradient_relation",s.diff(g,r)+r*h)
zero("h_derivative",s.diff(h,r)+s.exp(-mass*r)*((mass*r)**2+3*mass*r+3)/r**4)
zero("printed_radial_factor",h-r*s.diff(h,r)-B)
zero("Hessian_norm_dominates_tangential",lr+lt-s.exp(-mass*r)*((mass*r)**2+mass*r+1)/r**3)
zero("printed_factor_dominates_Hessian_norm",B-lr-2*s.exp(-mass*r)*(mass*r+1)/r**3)
zero("rh_negative_derivative",s.diff(r*h,r)+s.exp(-mass*r)*((mass*r)**2+2*mass*r+2)/r**3)
zero("B_negative_derivative",s.diff(B,r)+s.exp(-mass*r)*((mass*r)**3+5*(mass*r)**2+12*mass*r+12)/r**4)
tt=s.symbols("t",nonnegative=True)
polys=[tt**2+tt+1,2*(tt+1),tt**2+2*tt+2,tt**3+5*tt**2+12*tt+12]
ck("sign_proofs_include_massless_endpoint",all(all(c>0 for c in s.Poly(poly,tt).all_coeffs()) and poly.subs(tt,0)>0 for poly in polys))

J=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
def kernel(x,y,m):
    v=y-x;rad=np.sqrt(np.dot(v,v))
    return np.dot(y,J@x)*(1+m*rad)*np.exp(-m*rad)/rad**3
def constants(d,L,m):
    base=np.exp(-m*d)
    cy=L*base*(m*d+2)**2/d**3
    return base*(1+m*d)/d**2+cy,cy
gradient_details=[]
for m in (0.,.9,4.):
    for index,(x,y) in enumerate(((np.zeros(3),np.array([1.,0.,0.])),
                                 (np.array([.3,-.2,.1]),np.array([-.4,.5,1.2])))):
        v=y-x;rad=np.linalg.norm(v);jx=J@x
        hh=(1+m*rad)*np.exp(-m*rad)/rad**3
        llr=np.exp(-m*rad)*((m*rad)**2+2*m*rad+2)/rad**3
        llt=-hh
        Hess=llt*np.eye(3)+(llr-llt)*np.outer(v,v)/rad**2
        gx=J@(-hh*v)+Hess@jx;gy=-Hess@jx
        step=1e-25;gxc=[];gyc=[]
        for axis in range(3):
            xx=x.astype(complex);xx[axis]+=1j*step
            yy=y.astype(complex);yy[axis]+=1j*step
            gxc.append(np.imag(kernel(xx,y,m))/step)
            gyc.append(np.imag(kernel(x,yy,m))/step)
        near(f"complex_step_gradient_x_{m}_{index}",gxc,gx)
        near(f"complex_step_gradient_y_{m}_{index}",gyc,gy)
        cx,cy=constants(rad,np.linalg.norm(jx),m)
        ck(f"printed_gradient_bounds_{m}_{index}",np.linalg.norm(gx)<=cx+1e-12 and np.linalg.norm(gy)<=cy+1e-12)
        if index==0:
            ck(f"extra_x_term_is_necessary_{m}",np.linalg.norm(gx)>0 and cy==0)
        gradient_details.append({"m":m,"pair":index,"gradient_x_norm":float(np.linalg.norm(gx)),"gradient_y_norm":float(np.linalg.norm(gy)),"Cx":cx,"Cy":cy})
details["gradient_checks"]=gradient_details

# Nontrivial split couplings: repeated original atoms go to different destinations.
A=np.array([[.3,.1,0.],[.3,.1,0.],[-.2,.25,-.1]])
da=np.array([[.04,-.01,.02],[-.02,.03,.01],[.01,.02,-.015]])
wa=np.array([.4,.5,1.5])
Bp=np.array([[.25,.15,1.5],[.25,.15,1.5],[-.35,.2,1.6]])
db=np.array([[-.03,.02,-.025],[.015,-.035,.01],[.02,.01,-.02]])
wb=np.array([.6,.4,.7])
MA=float(sum(wa));MB=float(sum(wb))
na=np.linalg.norm(da,axis=1);nb=np.linalg.norm(db,axis=1)
DA=float(wa@na);DB=float(wb@nb)
epsA=float(max(na));epsB=float(max(nb));d0=1.5;d=d0-epsA-epsB;L=.6
near("product_mass_factor_A",np.sum(wa[:,None]*wb[None,:]*na[:,None]),MB*DA)
near("product_mass_factor_B",np.sum(wa[:,None]*wb[None,:]*nb[None,:]),MA*DB)
ck("uniform_original_gap_certificate",float(np.min(Bp[:,2])-np.max(A[:,2]))>=d0)
ck("positive_interpolated_gap_certificate",d>0,{"d0":d0,"epsA":epsA,"epsB":epsB,"d":d})
endpoint_lever=max(np.linalg.norm(A[:,:2],axis=1).max(),np.linalg.norm((A+da)[:,:2],axis=1).max())
ck("lever_certificate_by_convexity",endpoint_lever<=L,{"maximum_endpoint_lever":float(endpoint_lever),"L":L})
transport=[]
phase=2*np.pi*np.arange(64)/64
for m in (0.,.9,4.):
    cx,cy=constants(d,L,m);envelope=MB*cx*DA+MA*cy*DB
    old=[];new=[];pair_excess=[];weighted_absolute=[]
    for phi in phase:
        co,si=np.cos(phi),np.sin(phi)
        rotation=np.array([[co,-si,0.],[si,co,0.],[0.,0.,1.]])
        BB=Bp@rotation.T;BBnew=(Bp+db)@rotation.T
        ko=np.array([[kernel(x,y,m) for y in BB] for x in A])
        kn=np.array([[kernel(x,y,m) for y in BBnew] for x in A+da])
        changes=np.abs(kn-ko)
        point_bound=cx*na[:,None]+cy*nb[None,:]
        pair_excess.append(float(np.max(changes-point_bound)))
        weighted_absolute.append(float(np.sum(wa[:,None]*wb[None,:]*changes)))
        old.append(float(np.sum(wa[:,None]*wb[None,:]*ko)))
        new.append(float(np.sum(wa[:,None]*wb[None,:]*kn)))
    old=np.array(old);new=np.array(new);delta=new-old
    ck(f"all_point_transport_bounds_{m}",max(pair_excess)<=1e-12,{"largest_excess":max(pair_excess)})
    ck(f"product_coupling_bound_{m}",max(weighted_absolute)<=envelope+1e-12,{"largest_integrated_absolute_change":max(weighted_absolute),"bound":envelope})
    ck(f"field_difference_bound_{m}",max(abs(delta))<=envelope+1e-12)
    harmonic=[]
    for n in (1,2,3):
        cn=np.mean(old*np.exp(-1j*n*phase));cp=np.mean(new*np.exp(-1j*n*phase))
        dc=abs(cp-cn)
        ampchange=abs(2*abs(cp)-2*abs(cn))
        sinechange=abs(-2*(cp-cn).imag);coschange=abs(2*(cp-cn).real)
        ck(f"complex_and_real_harmonic_bounds_{m}_{n}",dc<=envelope+1e-12 and max(ampchange,sinechange,coschange)<=2*envelope+1e-12 and ampchange<=2*dc+1e-12)
        harmonic.append({"n":n,"complex_coefficient_change":float(dc),"real_amplitude_change":float(ampchange),"sine_coefficient_change":float(sinechange),"cosine_coefficient_change":float(coschange)})
    transport.append({"m":m,"MA":MA,"MB":MB,"DA":DA,"DB":DB,"Cx":cx,"Cy":cy,"complex_envelope":envelope,"real_envelope":2*envelope,"maximum_field_change":float(max(abs(delta))),"harmonics":harmonic})
details["split_transport"]=transport

# Domain and signed-mass countercontrols do not evaluate a singular kernel.
endpoint1=np.array([1.,0.,0.]);endpoint2=-endpoint1
ck("endpoint_gaps_do_not_certify_straight_path",np.linalg.norm(endpoint1)==1 and np.linalg.norm(endpoint2)==1 and np.linalg.norm((endpoint1+endpoint2)/2)==0,
   {"endpoint_gaps":[1,1],"midpoint_gap":0,"unconstrained_atom_W1":2,"admitted_straight_transport_exists":False})
signed=kernel(np.array([.5,0.,0.]),np.array([0.,1.,1.]),0.)-kernel(np.array([-.5,0.,0.]),np.array([0.,1.,1.]),0.)
near("zero_net_mass_nonzero_torque",signed,8/27)
ck("net_mass_bound_rejected",signed!=0)
ph=s.symbols("ph",real=True)
sign_c=4*s.integrate(s.cos(ph),(ph,0,s.pi/2))/(2*s.pi)
zero("generic_complex_Fourier_sign_control",sign_c-2/s.pi)
ck("complex_envelope_is_not_real_envelope",float(sign_c)<1 and float(2*sign_c)>1,{"complex_coefficient":str(sign_c),"real_coefficient":str(2*sign_c),"uniform_pointwise_envelope":1,"scope":"Generic Fourier function, not apparatus realization"})

# Stipulated scale only, using exact SI conversions and rational parameters.
smallMA=s.Rational(65749,10**8);smallMB=s.Rational(119856,10**8)
lever=s.Rational(27,1000);eps=s.Rational(1,10**6);gap=s.Rational(50,10**6)-2*eps
G=s.Rational(66742,10**15)
scales=[]
for mm in (0,20000):
    ccY=lever*s.exp(-mm*gap)*(mm*gap+2)**2/gap**3
    ccX=s.exp(-mm*gap)*(1+mm*gap)/gap**2+ccY
    envelope=G*smallMA*smallMB*eps*(ccX+ccY)
    ck(f"stipulated_positive_envelope_{mm}",envelope>0)
    scales.append({"m_per_meter":mm,"complex_envelope_Nm":str(s.N(envelope,30)),"real_envelope_Nm":str(s.N(2*envelope,30)),"complex_envelope_fNm":str(s.N(envelope*10**15,30)),"real_envelope_fNm":str(s.N(2*envelope*10**15,30)),"displacements_are_stipulated_not_measured":True})
details["stipulated_scale"]={"mass_A_kg":str(smallMA),"mass_B_kg":str(smallMB),"d_meter":str(gap),"epsilon_each_meter":str(eps),"L_meter":str(lever),"reference_G_SI":str(G),"unit_scalar_strength":True,"cases":scales,"empirical_bound":False}
final=hashlib.sha256(source.read_bytes()).hexdigest()
ck("source_unchanged",initial==final)
out={"kind":"Focused independent geometry-transport controls; no formal audit status","python":sys.version,"numpy":np.__version__,"sympy":s.__version__,"source_sha256":initial,"final_source_sha256":final,"summary":{"passed":sum(x["passed"] for x in rows),"failed":sum(not x["passed"] for x in rows)},"checks":rows,"details":details,"author_runner_or_results_read":False,"empirical_validation":False}
print(json.dumps(out,indent=2))
assert out["summary"]["failed"]==0
