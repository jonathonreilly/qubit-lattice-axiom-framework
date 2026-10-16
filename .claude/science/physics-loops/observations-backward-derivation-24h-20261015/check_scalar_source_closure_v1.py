"""Leading scalar source closure, exact and synthetic controls only."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
P=Path(__file__).resolve().parent
plan=json.loads((P/'SCALAR_SOURCE_PLAN_v1.json').read_text())
assert hashlib.sha256((P/plan['source']).read_bytes()).hexdigest()==plan['source_sha256']
rows=[];details={}
def ck(name,passed,detail=None):rows.append({'name':name,'passed':bool(passed),'detail':detail})
f,fs,D,m=s.symbols('F Fstar D m',positive=True)
me=m*s.sqrt(fs/f);phif=s.sqrt(fs*D/(2*f*f));beta=s.diff(s.log(me),f)/phif
ck('weak_charge_from_conformal_mass',s.simplify(2*fs*beta**2-1/D)==0)
GT=s.symbols('GT',positive=True)
ck('scalar_exchange_normalization',s.simplify((1/s.sqrt(2*fs))**2/(4*s.pi)-1/(8*s.pi*fs))==0)

# Direct integration over a sphere and direct binary moments.
z,az=s.symbols('z az',real=True);n=s.Matrix([s.sqrt(1-z*z)*s.cos(az),s.sqrt(1-z*z)*s.sin(az),z])
def sphere(expr):return s.simplify(s.integrate(s.integrate(s.expand_trig(expr),(az,0,2*s.pi)),(z,-1,1)))
ck('dipole_sphere_integral',s.simplify(sphere(n[0]**2)-4*s.pi/3)==0)
ck('quadrupole_sphere_integral',s.simplify(sphere(n[0]**2*n[1]**2)-4*s.pi/15)==0)
mu,r,om,t,al=s.symbols('mu r Om t alpha',positive=True)
rv=s.Matrix([r*s.cos(om*t),r*s.sin(om*t),0]);Iq=mu*(rv*rv.T-s.eye(3)*r*r/3)
I3=Iq.diff(t,3).subs(t,0);q3=s.sqrt(4*s.pi*GT)*al*I3
scalar_quad=s.simplify(sphere((n.dot(q3*n)/2)**2)/(16*s.pi**2))
tensor=s.simplify(GT*sum(v*v for v in I3)/5)
ck('equal_charge_scalar_quadrupole_fraction',s.simplify(scalar_quad/tensor-al**2/6)==0)
da=s.symbols('delta_alpha',real=True)
Ddd=s.sqrt(4*s.pi*GT)*mu*da*rv.diff(t,2).subs(t,0)
scalar_dip=s.simplify(sphere(n.dot(Ddd)**2)/(16*s.pi**2))
ck('dipole_flux_fraction',s.simplify(scalar_dip/tensor-s.Rational(5,96)*da**2/(r*r*om*om))==0)
ck('dipole_zero_does_not_remove_quadrupole',scalar_dip.subs(da,0)==0 and scalar_quad!=0)
m1,m2,a1,a2=s.symbols('m1 m2 a1 a2',positive=True);M=m1+m2;mu12=m1*m2/M
charge_dip=a1*m1*m2/M-a2*m2*m1/M
charge_quad=a1*m1*(m2/M)**2+a2*m2*(m1/M)**2
ck('mass_weighted_scalar_dipole',s.simplify(charge_dip-mu12*(a1-a2))==0)
ck('mass_weighted_scalar_quadrupole',s.simplify(charge_quad-mu12*(a1*m2+a2*m1)/M)==0)

# Independent canonical-potential and Jordan-trace mass calculations.
V=s.Function('V')(f);ww=s.Function('omega')(f);DD=2*ww+3
VE=fs**2*V/f**2;phiF=s.sqrt(fs*DD/(2*f*f))
massE=s.diff(s.diff(VE,f)/phiF,f)/phiF
massJ=s.simplify(f/fs*massE)
equil={s.diff(V,f):2*V/f}
target=2*(f*s.diff(V,f,2)-s.diff(V,f))/DD
ck('canonical_and_Jordan_scalar_mass',s.simplify(massJ.subs(equil)-target.subs(equil))==0)
xx,C=s.symbols('x C',real=True);FF=C*s.exp(xx);W=s.Function('W')(xx)
v=FF*W;vF=s.diff(v,xx)/FF;vFF=s.diff(vF,xx)/FF
ck('inverse_vacuum_criterion',s.simplify(FF*vF-2*v-FF*(s.diff(W,xx)-W))==0)
ck('inverse_mass_without_normalization',s.simplify(2*(FF*vFF-vF)-2*(s.diff(W,xx,2)-W))==0)
ck('normalization_absent_from_mass',C not in s.simplify(2*(FF*vFF-vF)).free_symbols)

# The outgoing massive-field energy current, not a massless dt(phi)^2 shortcut.
psi,k,nu,amp=s.symbols('psi k nu amp',positive=True)
for ell in [1,2]:
    av=s.integrate(nu*k*amp**2*k**(2*ell)*s.sin(psi)**2,(psi,0,2*s.pi))/(2*s.pi)
    zero_mass=av.subs(k,nu)
    ck('massive_flux_power_'+str(ell),s.simplify(av/zero_mass-(k/nu)**(2*ell+1))==0)
    wrong=s.integrate(nu**2*amp**2*k**(2*ell)*s.sin(psi)**2,(psi,0,2*s.pi))/(2*s.pi)
    ck('massless_flux_shortcut_detected_'+str(ell),s.simplify(wrong/zero_mass-(k/nu)**(2*ell+1))!=0)
ck('evanescent_time_averaged_radial_flux',s.integrate(s.sin(psi)*s.cos(psi),(psi,0,2*s.pi))==0)

cfg=plan['synthetic'];threshold_rows=[];mass_rows=[];charge_rows=[]
def chi(ell,nu,mass):return 0. if nu<=mass else (1-(mass/nu)**2)**((2*ell+1)/2)
rho=cfg['endpoint_ratio']
for omega in cfg['omega_values']:
    DD=2*omega+3;alpha2=1/DD;gamma=(1-alpha2)/(1+alpha2)
    ck('weak_PPN_charge_'+str(omega),abs((1-gamma)/(1+gamma)-alpha2)<1e-12)
    for mr in cfg['scalar_mass_over_omega']:
        c1=chi(1,1.,mr);c2=chi(2,2.,mr);eta=alpha2*c2/6
        q=np.sqrt(rho)/(1+eta);recovered=(q*(1+eta))**2
        ck('weak_source_siren_closure_'+str((omega,mr)),abs(recovered-rho)<1e-12)
        ck('threshold_range_'+str((omega,mr)),0<=c1<=c2<=1)
        if 1<=mr<2:ck('dipole_closed_quadrupole_open_'+str((omega,mr)),c1==0 and c2>0)
        threshold_rows.append({'omega':omega,'mass_over_orbital_frequency':mr,'dipole_factor':c1,'quadrupole_factor':c2,'extra_flux_fraction_weak_equal_charge':eta,'rho_recovered':float(recovered)})
    for scale in cfg['field_scales']:
        for av in [-.04,.01,.1]:
            # Direct potential in physical F, with all C choices retained.
            ff=s.symbols('ff',positive=True);f0=scale*np.exp(.3);potential=ff*(.02*ff/f0+av*s.log(ff/f0)**2)
            vf=s.diff(potential,ff);vff=s.diff(vf,ff)
            eq=float((ff*vf-2*potential).subs(ff,f0));mass2=float((2*(ff*vff-vf)/DD).subs(ff,f0))
            expected=4*av/DD
            ck('physical_F_potential_mass_'+str((omega,scale,av)),abs(eq)<1e-12 and abs(mass2-expected)<1e-12)
            ck('tachyonic_boundary_'+str((omega,scale,av)),(mass2<0)==(av<0))
            mass_rows.append({'omega':omega,'C':scale,'quadratic_W_coefficient':av,'mass_squared':mass2,'stable_mass_sign':mass2>=0})

for mass_ratio in cfg['mass_ratios']:
    for pp in cfg['charge_products']:
        values=[]
        for aa in cfg['charge1_values']:
            bb=pp/aa;aq=(aa+bb*mass_ratio)/(mass_ratio+1)
            eta_d=5*(aa-bb)**2/(96*cfg['orbital_speed']**2);eta_q=aq**2/6
            values.append(eta_d+eta_q)
            ck('fixed_conservative_product_'+str((mass_ratio,pp,aa)),abs(aa*bb-pp)<1e-15)
            charge_rows.append({'mass_ratio':mass_ratio,'product':pp,'alpha1':aa,'alpha2':bb,'dipole_fraction':eta_d,'quadrupole_fraction':eta_q,'total_leading_fraction':eta_d+eta_q})
        ck('same_product_different_radiation_'+str((mass_ratio,pp)),max(values)-min(values)>.1)
details.update(threshold_controls=threshold_rows,normalization_and_mass_controls=mass_rows,compact_charge_counterexamples=charge_rows)
out={'source_sha256':plan['source_sha256'],'plan_sha256':hashlib.sha256((P/'SCALAR_SOURCE_PLAN_v1.json').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows,'details':details,'empirical_validation':False,'scope':'Weak-source leading closure only; no compact-body charge, physical action or actual dataset validated.'}
print(json.dumps(out,indent=2));assert out['summary']['failed']==0
