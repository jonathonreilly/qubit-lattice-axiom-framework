"""Independent calibration and finite-volume checks, frozen before author code.

No author runner is imported. Inputs are exposed development material.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_DERIVATION_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_INPUTS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LEE2020_CALIBRATION_PLAN_v1.json",
]
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
from numpy.polynomial.legendre import leggauss
import scipy
from scipy.integrate import quad
from scipy.special import jv
import sympy as s

ROOT = Path(__file__).resolve().parents[5]
EXPECTED = ["f4d4e11a139c3ffa18ead244778a9f14b5f4ddde0f2ebb283463578d65832b04",
            "d237e334664e5b97ee7759432e842e60ad14acff20c852d3148a47e75786d0ec",
            "f30d6f9cbcf76f8313333cd45092a3046ae31241cc858ecb5b714d98a99be9ba"]
def binding():
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
initial = binding()
inputs = json.loads((ROOT / AUDIT_INPUT_PATHS[1]).read_text())
rows = []
details = {}
def ck(name, passed, detail=None):
    rows.append({"name": name, "passed": bool(passed), "detail": detail})
    print(json.dumps({"progress": name, "passed": bool(passed)}), file=sys.stderr, flush=True)
def close(name, actual, expected, rtol=2e-10, atol=1e-14):
    actual, expected = float(actual), float(expected)
    error = abs(actual - expected)
    ck(name, error <= atol + rtol * abs(expected),
       {"actual": actual, "expected": expected, "absolute_error": error, "rtol": rtol, "atol": atol})
ck("initial_source_binding", list(initial.values()) == EXPECTED)

# Cartesian force and analytic energy, with independent complex-step rotations.
phases = 2 * np.pi * np.arange(3) / 3
def pair(m, M, r, R, z, dx, dy, phi, alpha=0):
    x = np.column_stack((r * np.cos(phases + alpha), r * np.sin(phases + alpha), np.zeros(3)))
    y = np.column_stack((dx + R * np.cos(phases + phi), dy + R * np.sin(phases + phi), np.full(3, z)))
    vector = y[None, :, :] - x[:, None, :]
    squared = np.sum(vector * vector, axis=2)  # analytic complex-step extension, no conjugate
    forces = m * M * vector / squared[:, :, None]**1.5
    energy = -m * M * np.sum(1 / np.sqrt(squared))
    torque = np.sum(x[:, None, 0] * forces[:, :, 1] - x[:, None, 1] * forces[:, :, 0])
    return energy, torque, np.sum(forces, axis=(0, 1))
def centered(phi, m, M, r, R, z=0):
    angles = np.asarray(phi)[..., None] + phases
    den = r*r + R*R + z*z - 2*r*R*np.cos(angles)
    return 3*m*M*r*R*np.sum(np.sin(angles) / den**1.5, axis=-1)
vals = inputs["si_metrology"]
m, M, r, R = [vals[key]["value"] for key in ("inner_mass", "outer_mass", "inner_radius", "outer_radius")]
radial, vertical = vals["radial_offset"]["value"], vals["vertical_offset"]["value"]
h = 1e-24
for phi in (.17, .51, 1.06):
    for dx, dy, z, label in ((0., 0., 0., "center"), (radial, radial/3, vertical, "offset")):
        E, T, F = pair(m, M, r, R, z, dx, dy, phi)
        dE_inner = np.imag(pair(m, M, r, R, z, dx, dy, phi, 1j*h)[0])/h
        dE_outer = np.imag(pair(m, M, r, R, z, dx, dy, phi+1j*h)[0])/h
        close(f"inner_energy_force_{label}_{phi}", T, -dE_inner)
        close(f"offset_torque_lever_identity_{label}_{phi}", T-dE_outer, dx*F[1]-dy*F[0])
        if label == "center":
            close(f"centered_pair_reduction_{phi}", T, centered(phi,m,M,r,R))
            close(f"centered_outer_phase_derivative_{phi}", T, dE_outer)
        else:
            ck(f"different_center_torques_not_opposites_{phi}", abs(T-dE_outer) > 1e-14,
               {"inner_torque": float(T), "outer_energy_derivative": float(dE_outer)})

phi_s = s.symbols("phi", real=True)
identity = s.expand_trig(s.legendre(3, s.cos(phi_s)) - (3*s.cos(phi_s)+5*s.cos(3*phi_s))/8)
ck("Legendre_third_harmonic_exact", s.simplify(identity) == 0)
ck("leading_coefficient_exact", 9*3*s.Rational(5,8) == s.Rational(135,8))
def coefficient(function, n=3):
    value, err = quad(lambda x: float(function(x))*np.sin(n*x)/np.pi, 0, 2*np.pi,
                      epsabs=1e-15, epsrel=5e-13, limit=200)
    return value, err
B, Berr = coefficient(lambda phi: centered(phi,m,M,r,R))
fft_rows = []
for count in (48,96,192):
    phi = 2*np.pi*np.arange(count)/count
    torque = centered(phi,m,M,r,R)
    c3 = np.mean(torque*np.exp(-3j*phi))
    close(f"real_Fourier_amplitude_{count}", 2*abs(c3), B)
    close(f"signed_sine_coefficient_{count}", -2*c3.imag, B)
    close(f"cosine_coefficient_zero_{count}", 2*c3.real, 0.)
    ck(f"missing_factor_two_detected_{count}", abs(abs(c3)/B-.5)<1e-10)
    for n in (1,2,4,5):
        close(f"forbidden_harmonic_n{n}_{count}", abs(np.mean(torque*np.exp(-1j*n*phi))), 0.)
    fft_rows.append({"count":count,"real_amplitude_per_G":float(2*abs(c3)),"complex_coefficient_real":float(c3.real),"complex_coefficient_imag":float(c3.imag)})
small = []
for ratio in (1/20,1/40,1/80):
    a3, err = coefficient(lambda phi: centered(phi,1.,1.,ratio,1.))
    normalized = a3/ratio**3
    small.append({"ratio":ratio,"A3_over_q3":normalized,"relative_remainder":normalized/(135/8)-1,"quad_error":err})
ck("small_radius_approaches_leading_coefficient", abs(small[-1]["relative_remainder"])<2e-4, small)
for i in (0,1):
    quotient=small[i]["relative_remainder"]/small[i+1]["relative_remainder"]
    ck(f"small_radius_quadratic_relative_remainder_{i}",3.9<quotient<4.1,{"quotient":quotient})
details["Fourier_controls"]={"adaptive_B":B,"adaptive_error_estimate":Berr,"FFTs":fft_rows,"small_radius":small}

# Published-model diagnostics: none of these discrepancies is an acceptance target.
published = inputs["published_summary_fNm"]
candidate_G = inputs["printed_G"]["mantissa"]*10.**(-11)
literal_G = inputs["printed_G"]["mantissa"]*10.**inputs["printed_G"]["exponent"]
base_fNm = candidate_G*B*1e15
def pair_amplitude(dx=0.,dy=0.,z=0.):
    # Same real harmonic definition, including any phase; independent adaptive integrals.
    fn=lambda ph: pair(m,M,r,R,z,dx,dy,ph)[1]
    sine, e1=coefficient(fn)
    cosine,e2=quad(lambda ph: fn(ph)*np.cos(3*ph)/np.pi,0,2*np.pi,epsabs=1e-15,epsrel=5e-13,limit=200)
    return float(np.hypot(sine,cosine)),float(e1+e2)
corrections={}
for label,dx,z in (("radial",radial,0.),("vertical",0.,vertical),("combined",radial,vertical)):
    amp,err=pair_amplitude(dx=dx,z=z)
    corrections[label]={"amplitude_per_G":amp,"correction_fNm":(amp-B)*candidate_G*1e15,"quad_error_per_G":err,"offset_direction":"dx=specified radial offset, dy=0"}
def derivative_integrand(phi, which):
    ang=phi+phases;co=np.cos(ang);si=np.sin(ang)
    den=r*r+R*R-2*r*R*co
    if which=="inner_radius":
        derivative=3*m*M*R*np.sum(si*(den**(-1.5)-3*r*(r-R*co)*den**(-2.5)))
    else:
        derivative=3*m*M*r*np.sum(si*(den**(-1.5)-3*R*(R-r*co)*den**(-2.5)))
    return derivative
derivatives={"inner_mass":B/m,"outer_mass":B/M}
for key in ("inner_radius","outer_radius"):
    derivatives[key]=coefficient(lambda ph:derivative_integrand(ph,key))[0]
    rr=r+1j*h if key=="inner_radius" else r
    RR=R+1j*h if key=="outer_radius" else R
    independent_d=coefficient(lambda ph:np.imag(centered(ph,m,M,rr,RR))/h)[0]
    close("analytic_sensitivity_"+key,derivatives[key],independent_d)
sensitivities={}
for key,deriv in derivatives.items():
    diagnostic=abs(deriv)*vals[key]["uncertainty"]*candidate_G*1e15
    target=published["sigma_by_parameter"][key]
    sensitivities[key]={"derivative_per_G":deriv,"single_parameter_sigma_fNm":diagnostic,"printed_sigma_fNm":target,"difference_fNm":diagnostic-target,"ratio_to_printed":diagnostic/target}
gamma=published["Nmeas"]/(published["Ncal_nominal"]+published["Ncal_correction_table"])
gamma_sigma=gamma*np.hypot(published["Nmeas_statistical_uncertainty"]/published["Nmeas"],published["Ncal_systematic_uncertainty"]/(published["Ncal_nominal"]+published["Ncal_correction_table"]))
details["published_model_diagnostics"]={
    "nominal_amplitude_fNm_negative_exponent_candidate":base_fNm,
    "published_nominal_fNm":published["Ncal_nominal"],"nominal_difference_fNm":base_fNm-published["Ncal_nominal"],
    "G_consistency_only":published["Ncal_nominal"]*1e-15/B,
    "G_negative_exponent_candidate":candidate_G,"G_literal_printed":literal_G,
    "nominal_amplitude_fNm_literal_exponent":literal_G*B*1e15,
    "literal_to_candidate_ratio":literal_G/candidate_G,
    "corrections":corrections,
    "published_radial_correction_table":published["radial_correction_table"],
    "published_radial_correction_prose":published["radial_correction_prose"],
    "published_vertical_correction":published["vertical_correction"],
    "single_parameter_sensitivities":sensitivities,
    "conditional_uncorrelated_four_parameter_sigma_fNm":float(np.sqrt(sum(x["single_parameter_sigma_fNm"]**2 for x in sensitivities.values()))),
    "gamma_arithmetic":gamma,"gamma_sigma_conditional_uncorrelated":float(gamma_sigma),
    "published_gamma":inputs["published_gamma"],
    "interpretation":"Published-model diagnostics only; no input retuned, covariance inferred or G measured."
}

# Cylindrical normalization and point harmonics, independently from angular space.
qq,zz=s.symbols("q z",positive=True)
ck("vertical_Green_derivative_jump",s.simplify(s.diff(s.exp(-qq*zz)/qq,zz).subs(zz,0)-s.diff(s.exp(qq*zz)/qq,zz).subs(zz,0)+2)==0)
ck("source_normalization_4pi",s.simplify((-2)*(2*s.pi)+4*s.pi)==0)
point=[]
for mass in (0.,.8,2.):
    axial,ae=quad(lambda kval: kval/np.hypot(kval,mass)*np.exp(-np.hypot(kval,mass)*.47),0,np.inf,epsabs=1e-13,epsrel=2e-10,limit=200)
    close(f"axial_point_Green_{mass}",axial,np.exp(-mass*.47)/.47,rtol=2e-8,atol=1e-13)
    for n in (0,1,3):
        def angular(theta):
            d=np.sqrt(.34**2+.61**2+.47**2-2*.34*.61*np.cos(theta))
            return np.exp(-mass*d)/d*np.cos(n*theta)/np.pi
        real,err1=quad(angular,0,np.pi,epsabs=1e-13,epsrel=2e-10,limit=200)
        def hankel(kval):
            qval=np.hypot(kval,mass)
            return kval/qval*jv(n,kval*.34)*jv(n,kval*.61)*np.exp(-qval*.47)
        bessel,err2=quad(hankel,0,np.inf,epsabs=1e-13,epsrel=2e-10,limit=200)
        close(f"point_angular_Bessel_mu{mass}_n{n}",bessel,real,rtol=2e-8,atol=1e-13)
        point.append({"mu":mass,"n":n,"angular_complex_order_coefficient":real,"Bessel_coefficient":bessel,"quadrature_error_estimates":[err1,err2]})
details["point_harmonics"]=point

# Explicit six-dimensional volume quadrature of all nine wedge pairs.
cfg={"N":3,"n":3,"betaA":.17,"betaB":.21,"rA":[.2,.6],"rB":[.25,.55],"tA":.12,"tB":.16,"d":.4,"rhoA":1.3,"rhoB":.8,"mu":.7,"G":1.}
def interval(order,a,b):
    node,weight=leggauss(order)
    return (a+b)/2+(b-a)*node/2,(b-a)*weight/2
def wedge_points(order,which):
    radius,wr=interval(order,*cfg["r"+which]);wr=wr*radius
    theta,wt=interval(order,-cfg["beta"+which],cfg["beta"+which])
    theta=np.concatenate([theta+2*np.pi*j/cfg["N"] for j in range(cfg["N"])])
    wt=np.tile(wt,cfg["N"])
    z,wz=interval(order,-cfg["tA"],0.) if which=="A" else interval(order,cfg["d"],cfg["d"]+cfg["tB"])
    rr,tt,zz=np.meshgrid(radius,theta,z,indexing="ij")
    coords=np.column_stack(((rr*np.cos(tt)).ravel(),(rr*np.sin(tt)).ravel(),zz.ravel()))
    weights=(wr[:,None,None]*wt[None,:,None]*wz[None,None,:]*cfg["rho"+which]).ravel()
    expected_mass=cfg["rho"+which]*cfg["N"]*cfg["beta"+which]*(cfg["r"+which][1]**2-cfg["r"+which][0]**2)*cfg["t"+which]
    close(f"volume_mass_{which}_order{order}",np.sum(weights),expected_mass)
    return coords,weights
def volume_coefficient(order,count):
    started=time.monotonic()
    aa,wa=wedge_points(order,"A");bb,wb=wedge_points(order,"B")
    energy=[];phase=2*np.pi*np.arange(count)/(cfg["N"]*count)
    for ph in phase:
        bx=bb[:,0]*np.cos(ph)-bb[:,1]*np.sin(ph)
        by=bb[:,0]*np.sin(ph)+bb[:,1]*np.cos(ph)
        total=0.
        for start in range(0,len(aa),256):
            block=aa[start:start+256]
            sq=(block[:,0,None]-bx[None,:])**2+(block[:,1,None]-by[None,:])**2+(block[:,2,None]-bb[None,:,2])**2
            dist=np.sqrt(sq)
            total+=np.sum(wa[start:start+256,None]*wb[None,:]*np.exp(-cfg["mu"]*dist)/dist)
        energy.append(-cfg["G"]*total)
    value=np.mean(np.array(energy)*np.exp(-1j*cfg["n"]*phase))
    return {"volume_order":order,"phase_count":count,"cosine_energy_coefficient":float(2*value.real),"sine_energy_coefficient":float(-2*value.imag),"complex_coefficient_magnitude":float(abs(value)),"seconds":time.monotonic()-started,"phase_energies":energy}
volumes=[volume_coefficient(order,32) for order in (4,6,8)]
phase_check=volume_coefficient(6,48)
def bessel_wedge(order):
    ra,wa=interval(order,*cfg["rA"]);rb,wb=interval(order,*cfg["rB"])
    def fn(kval):
        qval=np.hypot(kval,cfg["mu"])
        RA=np.dot(wa*ra,jv(cfg["n"],kval*ra));RB=np.dot(wb*rb,jv(cfg["n"],kval*rb))
        return kval*np.exp(-qval*cfg["d"])*(-np.expm1(-qval*cfg["tA"]))* (-np.expm1(-qval*cfg["tB"]))*RA*RB/qval**3
    integral,err=quad(fn,0,np.inf,epsabs=1e-14,epsrel=2e-10,limit=300)
    ell=cfg["n"]/cfg["N"]
    factor=-8*cfg["G"]*cfg["rhoA"]*cfg["rhoB"]*np.sin(cfg["n"]*cfg["betaA"])*np.sin(cfg["n"]*cfg["betaB"])/ell**2
    return {"radial_order":order,"integral":integral,"integral_error_estimate":err,"cosine_energy_coefficient":factor*integral}
bessels=[bessel_wedge(order) for order in (24,40)]
best=bessels[-1]["cosine_energy_coefficient"]
close("finite_wedge_Bessel_radial_convergence",bessels[0]["cosine_energy_coefficient"],best,rtol=2e-8,atol=1e-14)
close("finite_wedge_full_volume_vs_Bessel",volumes[-1]["cosine_energy_coefficient"],best,rtol=2e-6,atol=1e-14)
close("finite_wedge_phase_convergence",phase_check["cosine_energy_coefficient"],volumes[1]["cosine_energy_coefficient"],rtol=2e-8,atol=1e-14)
errors=[abs(row["cosine_energy_coefficient"]-best) for row in volumes]
ck("finite_wedge_volume_convergence",errors[2]<errors[1]<errors[0],{"absolute_errors":errors})
for row in volumes:
    close(f"finite_wedge_real_even_energy_order{row['volume_order']}",row["sine_energy_coefficient"],0.,atol=1e-14)
ck("spurious_4pi_energy_factor_detected",abs(volumes[-1]["cosine_energy_coefficient"]-best/(4*np.pi))>.8*abs(best))
ck("single_complex_order_energy_detected",abs(volumes[-1]["cosine_energy_coefficient"]-best/2)>.49*abs(best))
details["finite_wedge"]={"fixture":cfg,"complete_volume_quadratures":volumes,"phase_convergence_run":phase_check,"Bessel_radial_quadratures":bessels,"real_torque_amplitude":cfg["n"]*abs(best),"quadrature_class":"Floating diagnostics, not interval certified"}
final=binding();ck("final_sources_unchanged",final==initial)
out={"kind":"Focused independent calibration controls; no formal audit status","python":sys.version,"numpy":np.__version__,"scipy":scipy.__version__,"sympy":s.__version__,"source_binding":initial,"final_source_binding":final,"summary":{"passed":sum(x["passed"] for x in rows),"failed":sum(not x["passed"] for x in rows)},"checks":rows,"details":details,"empirical_validation":False,"author_runner_or_results_read":False}
print(json.dumps(out,indent=2))
assert out["summary"]["failed"]==0
