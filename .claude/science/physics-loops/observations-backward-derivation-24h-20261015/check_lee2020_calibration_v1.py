"""Pinned published-model consistency and synthetic Green normalization checks.

No fit to the 95 torque records. No new measurement of G or scalar exclusion.
Printed calibration discrepancies remain diagnostics, not adjustable inputs.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import jv

HERE = Path(__file__).resolve().parent
INPUT = json.loads((HERE / "LEE2020_CALIBRATION_INPUTS_v1.json").read_text())
checks = []
details = {}


def check(name, condition, **data):
    checks.append({"name": name, "passed": bool(condition), **data})


def exact(name, expression):
    residual = sp.simplify(expression)
    check(name, residual == 0, residual=str(residual))


def ring_force(phi, r, R, m=1., M=1., G=1., dx=0., dy=0., z=0., beta=0.):
    """Torque on inner pattern, independently summed over all nine pairs."""
    theta = 2 * np.pi * np.arange(3) / 3
    x = np.column_stack((r * np.cos(theta + beta), r * np.sin(theta + beta),
                         np.zeros(3)))
    y = np.column_stack((dx + R * np.cos(theta + phi),
                         dy + R * np.sin(theta + phi), np.full(3, z)))
    displacement = y[None, :, :] - x[:, None, :]
    distance = np.linalg.norm(displacement, axis=-1)
    energy = -G * m * M * np.sum(1 / distance)
    torque = G * m * M * np.sum(np.cross(x[:, None, :], y[None, :, :])[..., 2]
                               / distance**3)
    return float(energy), float(torque)


def ring_reduced(phi, r, R, m=1., M=1., G=1., z=0.):
    angle = phi + 2 * np.pi * np.arange(3) / 3
    distance2 = r*r + R*R + z*z - 2*r*R*np.cos(angle)
    return 3*G*m*M*r*R*np.sum(np.sin(angle)/distance2**1.5)


def real_harmonic(function, n=3, grid=256):
    angles = 2*np.pi*np.arange(grid)/grid
    values = np.array([function(phi) for phi in angles])
    coefficient = np.mean(values*np.exp(-1j*n*angles))
    return 2*abs(coefficient), coefficient


u, q, radius = sp.symbols("u q radius", positive=True)
exact("P3 third harmonic coefficient", sp.legendre(3, sp.cos(u))
      - sp.Rational(3, 8)*sp.cos(u)-sp.Rational(5, 8)*sp.cos(3*u))
g = sp.exp(-q*radius)/radius
exact("Helmholtz outside source", sp.diff(radius**2*sp.diff(g, radius), radius)
      / radius**2-q**2*g)
exact("source flux normalization", sp.limit(radius**2*sp.diff(g, radius), radius, 0)+1)

# Independent force, reduction, and potential differentiation controls.
for rr, RR, zz in [(0.2, 1.0, 0.), (0.31, 1.2, 0.17)]:
    for phi in [.13, .49, 1.12]:
        energy, torque = ring_force(phi, rr, RR, z=zz)
        reduced = ring_reduced(phi, rr, RR, z=zz)
        check(f"nine pairs to reduced {rr,RR,zz,phi}", abs(torque-reduced)<2e-14)
        h = 1e-4
        derivative = (ring_force(phi-2*h,rr,RR,z=zz)[0]
                      -8*ring_force(phi-h,rr,RR,z=zz)[0]
                      +8*ring_force(phi+h,rr,RR,z=zz)[0]
                      -ring_force(phi+2*h,rr,RR,z=zz)[0])/(12*h)
        check(f"centered energy sign {rr,RR,zz,phi}", abs(torque-derivative)<2e-10,
              error=abs(torque-derivative))
        _, off_torque = ring_force(phi,rr,RR,dx=.07,dy=-.03,z=zz)
        inner = lambda b: ring_force(phi,rr,RR,dx=.07,dy=-.03,z=zz,beta=b)[0]
        derivative = (inner(-2*h)-8*inner(-h)+8*inner(h)-inner(2*h))/(12*h)
        check(f"offaxis inner energy sign {rr,RR,zz,phi}", abs(off_torque+derivative)<2e-10,
              error=abs(off_torque+derivative))
for rr in [.01,.005,.0025]:
    amplitude,_ = real_harmonic(lambda phi:ring_reduced(phi,rr,1.))
    leading = 135/8*rr**3
    relative = amplitude/leading-1
    check(f"small radius third harmonic {rr}", abs(relative)<2*rr*rr,
          relative_to_leading=relative)

# Published parameters: reference calculations only, not experimental fits.
pars = INPUT['si_metrology']
base = {short: pars[long]['value'] for short,long in
        [('r','inner_radius'),('R','outer_radius'),('m','inner_mass'),('M','outer_mass')]}
geometric_amplitude, geometric_c = real_harmonic(lambda phi:ring_reduced(phi,**base))
integral, integration_error = quad(lambda phi:ring_reduced(phi,**base)*math.sin(3*phi),
                                   0,2*math.pi,epsabs=1e-18,epsrel=1e-12,limit=300)
adaptive_amplitude = abs(integral/math.pi)
check("calibration quadrature vs Fourier", abs(adaptive_amplitude/geometric_amplitude-1)<1e-12,
      relative=abs(adaptive_amplitude/geometric_amplitude-1),reported_quad_error=integration_error)
for grid in [64,128,512]:
    value,_=real_harmonic(lambda phi:ring_force(phi,**base)[1],grid=grid)
    check(f"independent pair FFT grid {grid}", abs(value/geometric_amplitude-1)<2e-12,
          relative=abs(value/geometric_amplitude-1))
target=INPUT['published_summary_fNm']['Ncal_nominal']*1e-15
implied_G=target/geometric_amplitude
candidate_G=INPUT['printed_G']['mantissa']*1e-11
literal_G=INPUT['printed_G']['mantissa']*10.**INPUT['printed_G']['exponent']
nominal=geometric_amplitude*candidate_G/1e-15
check("unit factor separates printed exponent candidates", math.isclose(literal_G/candidate_G,1e22,rel_tol=1e-15))
check("complex-to-real factor mutation detected", abs(abs(geometric_c)/geometric_amplitude-.5)<1e-14)
details['calibration']={'geometric_A3_over_G_SI':geometric_amplitude,
    'published_Ncal_nominal_fNm':target/1e-15,'G_implied_by_published_computed_Ncal':implied_G,
    'literal_printed_G':literal_G,'labeled_negative_exponent_candidate':candidate_G,
    'candidate_predicted_nominal_fNm':nominal,'literal_predicted_nominal_fNm':geometric_amplitude*literal_G/1e-15,
    'candidate_minus_published_fNm':nominal-target/1e-15,
    'status':'Published-model consistency only. Ncal is calculated, so implied G is not a measurement.'}

def model_amplitude(parameters):
    value,_=real_harmonic(lambda phi:ring_reduced(phi,**parameters,G=candidate_G))
    return value/1e-15

sensitivities=[]
for short,long in [('m','inner_mass'),('M','outer_mass'),('r','inner_radius'),('R','outer_radius')]:
    value=base[short];step=1e-5*value
    def at(offset):
        parameters=base.copy();parameters[short]+=offset;return model_amplitude(parameters)
    derivative=(at(-2*step)-8*at(-step)+8*at(step)-at(2*step))/(12*step)
    derivative_coarse=(at(-4*step)-8*at(-2*step)+8*at(2*step)-at(4*step))/(24*step)
    check(f"metrology derivative step {long}",abs(derivative/derivative_coarse-1)<2e-8)
    sigma=abs(derivative)*pars[long]['uncertainty']
    reported=INPUT['published_summary_fNm']['sigma_by_parameter'][long]
    sensitivities.append({'parameter':long,'derivative_fNm_per_SI_unit':derivative,
                         'coherent_parameter_sigma_fNm':sigma,'printed_sigma_fNm':reported,
                         'difference_fNm':sigma-reported,'ratio':sigma/reported,
                         'interpretation':'All three equal sphere parameters varied together; source covariance/averaging convention not assumed.'})
details['metrology_sensitivity_diagnostics']=sensitivities
centering=[]
for offset in [0.,math.pi/6]:
    delta=pars['radial_offset']['value']
    radial,_=real_harmonic(lambda phi:ring_force(phi,**base,G=candidate_G,
              dx=delta*math.cos(offset),dy=delta*math.sin(offset))[1])
    centering.append({'displacement_orientation_rad':offset,'radial_delta_fNm':radial/1e-15-nominal})
vertical,_=real_harmonic(lambda phi:ring_reduced(phi,**base,G=candidate_G,z=pars['vertical_offset']['value']))
details['centering_diagnostics']={'radial':centering,'vertical_delta_fNm':vertical/1e-15-nominal,
    'published_radial_table_fNm':INPUT['published_summary_fNm']['radial_correction_table'],
    'published_radial_prose_fNm':INPUT['published_summary_fNm']['radial_correction_prose'],
    'published_vertical_fNm':INPUT['published_summary_fNm']['vertical_correction'],
    'scope':'Ideal six-sphere model, not a complete reproduction of apparatus uncertainty or null corrections.'}
pub=INPUT['published_summary_fNm']
details['reported_scale_arithmetic']={'gamma_from_reported_torques':pub['Nmeas']/(pub['Ncal_nominal']+pub['Ncal_correction_table']),
    'gamma_sigma_if_independent_reported_errors':math.hypot(pub['Nmeas_statistical_uncertainty']/(pub['Ncal_nominal']+pub['Ncal_correction_table']),pub['Nmeas']*pub['Ncal_systematic_uncertainty']/(pub['Ncal_nominal']+pub['Ncal_correction_table'])**2),
    'independence_status':'Arithmetic diagnostic conditional on independent supplied error summaries; covariance not derived.'}

# Independent real-space angular coefficients and cylindrical Bessel integrals.
point_rows=[]
for a,b,d,n,mu in [(0.,0.,.7,0,0.),(0.,0.,1.1,0,1.3),(.3,.7,.8,1,0.),(.4,.8,1.,2,.9),(1.,.5,.6,3,2.)]:
    def space(theta):
        distance=math.sqrt(a*a+b*b+d*d-2*a*b*math.cos(theta))
        return math.exp(-mu*distance)/distance*math.cos(n*theta)
    angular=quad(space,0,2*math.pi,epsabs=1e-12,epsrel=1e-12)[0]/(2*math.pi)
    def bessel(k):
        q=math.hypot(k,mu)
        return (k/q if q else 1.)*jv(n,k*a)*jv(n,k*b)*math.exp(-q*d)
    spectral,error=quad(bessel,0,np.inf,epsabs=1e-11,epsrel=1e-11,limit=300)
    check(f"Green angular vs spectral {a,b,d,n,mu}",abs(angular-spectral)<2e-10,
          absolute_error=abs(angular-spectral),quad_error=error)
    if a==b==0:
        check(f"axial point normalization {d,mu}",abs(spectral-math.exp(-mu*d)/d)<1e-12)
    check(f"wrong 4pi normalization detected {a,b,d,n,mu}",abs(angular-spectral/(4*math.pi))>1e-6)
    point_rows.append({'rA':a,'rB':b,'gap':d,'n':n,'mu':mu,'angular':angular,'bessel':spectral})
details['point_green']=point_rows


def interval_nodes(a,b,n):
    x,w=leggauss(n)
    return (a+b)/2+(b-a)*x/2,(b-a)*w/2


def wedge_nodes(N,beta,a,b,z0,z1,mass,orders):
    rr,rw=interval_nodes(a,b,orders[0]);zz,zw=interval_nodes(z0,z1,orders[1])
    th,tw=interval_nodes(-beta,beta,orders[2]);points=[];weights=[]
    density=mass/(N*beta*(b*b-a*a)*(z1-z0))
    for j in range(N):
        for r,wr in zip(rr,rw):
            for z,wz in zip(zz,zw):
                for t,wt in zip(th,tw):
                    angle=t+2*math.pi*j/N
                    points.append([r*math.cos(angle),r*math.sin(angle),z])
                    weights.append(density*wr*r*wz*wt)
    return np.array(points),np.array(weights),density


def wedge_direct(mu,n,orders,grid):
    A,wa,rhoA=wedge_nodes(2,.35,.25,.65,-.2,0.,1.1,orders)
    B,wb,rhoB=wedge_nodes(2,.22,.7,1.,.8,.95,.9,orders)
    energies=[];angles=2*np.pi*np.arange(grid)/grid
    for phi in angles:
        c,s=math.cos(phi),math.sin(phi)
        rotation=np.array([[c,-s,0.],[s,c,0.],[0.,0.,1.]])
        dist=np.linalg.norm(A[:,None,:]-(B@rotation.T)[None,:,:],axis=-1)
        energies.append(-np.sum(wa[:,None]*wb[None,:]*np.exp(-mu*dist)/dist))
    coefficient=2*np.mean(np.array(energies)*np.cos(n*angles))
    return float(coefficient),rhoA,rhoB,float(sum(wa)),float(sum(wb))


def wedge_spectral(mu,n,rhoA,rhoB):
    ra,wa=interval_nodes(.25,.65,32);rb,wb=interval_nodes(.7,1.,32)
    def integrand(k):
        q=math.hypot(k,mu)
        if q==0:return 0.
        RA=np.sum(wa*ra*jv(n,k*ra));RB=np.sum(wb*rb*jv(n,k*rb))
        return k*math.exp(-q*.8)*(-math.expm1(-q*.2))*(-math.expm1(-q*.15))*RA*RB/q**3
    integral,error=quad(integrand,0,np.inf,epsabs=1e-12,epsrel=1e-11,limit=300)
    prefactor=-8*rhoA*rhoB*math.sin(n*.35)*math.sin(n*.22)/(n/2)**2
    return prefactor*integral,abs(prefactor)*error


wedge_rows=[]
for mu in [0.,.7]:
    for n in [2,4]:
        coarse,rhoA,rhoB,ma,mb=wedge_direct(mu,n,(3,2,4),64)
        fine,_,_,_,_=wedge_direct(mu,n,(5,4,8),128)
        spectral,error=wedge_spectral(mu,n,rhoA,rhoB)
        check(f"volume mass normalization {mu,n}",abs(ma-1.1)<1e-13 and abs(mb-.9)<1e-13)
        check(f"complete wedge spatial vs spectral {mu,n}",abs(fine-spectral)<2e-9,
              absolute_error=abs(fine-spectral),coarse_error=abs(coarse-spectral),quad_error=error)
        check(f"wedge grid refinement {mu,n}",abs(fine-spectral)<abs(coarse-spectral))
        check(f"wedge 4pi mutation {mu,n}",abs(fine-spectral/(4*math.pi))>1e-6)
        wedge_rows.append({'mu':mu,'n':n,'coarse_spatial':coarse,'fine_spatial':fine,
                           'spectral':spectral,'absolute_error':abs(fine-spectral),
                           'torque_amplitude':n*abs(spectral)})
details['finite_wedge']=wedge_rows
names=['LEE2020_CALIBRATION_DERIVATION_v1.md','LEE2020_CALIBRATION_INPUTS_v1.json',
       'LEE2020_CALIBRATION_PLAN_v1.json',Path(__file__).name]
result={'source_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
        'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),
        'checks':checks,'details':details,
        'data_role':'Pinned exposed published metrology/model summaries and synthetic kernel controls; no torque-data fit or empirical holdout',
        'precision':'Floating quadrature/FFT checks, not certified enclosures',
        'empirical_validation':False}
print(json.dumps(result,indent=2))
raise SystemExit(bool(result['failed']))
