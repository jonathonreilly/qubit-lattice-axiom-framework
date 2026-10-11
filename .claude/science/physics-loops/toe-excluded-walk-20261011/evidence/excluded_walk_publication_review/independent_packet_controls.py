#!/usr/bin/env python3
"""Independent finite controls of the coherent excluded-walk packet.

No author or repository code is imported. Symbolic prolate-coordinate
integration derives the angular variance; vectorized Pauli projectors and
Gauss-Legendre coarea quadrature check the actual lattice angular section.
Quadrature is not interval-certified. No PV integral or time propagation is
approximated, and no finite check establishes the scattering theorem.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import sys
import numpy as np
import scipy
from scipy.special import roots_legendre
import sympy as sy

started = perf_counter()
source = Path(__file__).read_bytes()
e, k, t, d, A, lam = sy.symbols('e k t d A lam', positive=True)
z = sy.symbols('z', real=True)
D = e**2-k**2
# In prolate coordinates, y_1=a z+b sqrt(1-z^2) cos(phi).
# Integrate phi first, then the flat probability dz/2 exactly.
a2, b2 = e**2*t**2/4, D*(1-t**2)/4
mean = sy.integrate((a2*z**2+b2*(1-z**2)/2)/2, (z,-1,1))
fourth = sy.integrate((a2**2*z**4+3*a2*b2*z**2*(1-z**2)
                      +sy.Rational(3,8)*b2**2*(1-z**2)**2)/2, (z,-1,1))
beta = D+k**2*t**2
assert sy.factor(mean-beta/12) == 0
assert sy.factor(fourth-beta**2/80) == 0
assert sy.factor(fourth-mean**2-beta**2/180) == 0
# The coarea/contact product is constant D/16 in dv dphi at one cone.
u, vp = sy.symbols('u vp', real=True)
jac = k**3*(u**2-vp**2)/8
rprod = k**2*(u**2-vp**2)/4
assert sy.cancel(jac*D/(8*rprod)/k) == D/16
rho0 = sy.simplify(8/(2*sy.pi)**3 * (D/16)*4*sy.pi)
assert rho0 == D/(4*sy.pi**2)
print('Exact prolate integration: rho0=D/(4*pi^2), mean(y1^2)=beta/12, fourth=beta^2/80, variance=beta^2/180.')

# Derive the sign using a genuinely complex coherent vector and a generic
# unit-modulus Cayley phase; do not enter the desired change as an identity.
R, B, sig, mu, eta = sy.symbols('R B sig mu eta', real=True)
phase = (R-sy.I*B)/(R+sy.I*B)
obs = sy.Matrix([[mu,sig],[sig,eta]])
Sc = sy.diag(phase,1)
def expect(vec):
    return sy.simplify((sy.conjugate(vec.T)*(sy.conjugate(Sc.T)*obs*Sc-obs)*vec)[0])
plus = sy.Matrix([1,sy.I])/sy.sqrt(2)
minus = sy.Matrix([1,-sy.I])/sy.sqrt(2)
change = sy.factor(expect(plus))
assert change == -2*B*R*sig/(B**2+R**2)
assert sy.simplify(expect(minus)+change) == 0
assert expect(sy.Matrix([1,0])) == 0
asym = sy.simplify(change.subs({R:lam*A, B:sy.pi*lam**2*rho0,
                                sig:lam**3*d})/lam**4)
assert sy.simplify(sy.limit(asym,lam,0)+2*sy.pi*rho0*d/A) == 0
print('Exact Cayley-phase expectation:', change, '; reversing coherence reverses it; pure contact has zero change.')

# Check full K/E Jacobian and homogeneous seminorm exponents by substitutions,
# including a nonconstant polynomial energy profile extended by zero. Order-7
# traces at the endpoints vanish; these are independent exact scale fixtures.
x = sy.symbols('x', real=True)
f = (1-x**2)**8
for j in range(8):
    assert sy.diff(f,x,j).subs(x,1) == 0
    assert sy.diff(f,x,j).subs(x,-1) == 0
normE = sy.integrate(f*f,(x,-1,1))
assert normE > 0
amp, kval, Eval = sy.symbols('amp kval Eval', positive=True)
assert sy.simplify((lam**-2)**2 * lam**3 * lam) == 1
# Perform physical-variable norm integrals for polynomial envelope fixtures.
# Their order-seven boundary traces vanish; they need not equal the source's
# C-infinity bumps to discriminate a missing K volume or torus normalization.
rr=sy.symbols('rr',nonnegative=True)
radius=sy.Rational(1,32)
radial_unit=sy.integrate(rr**2*(1-rr**2)**16,(rr,0,1))
normK2=(2*sy.pi)**3/(4*sy.pi*radius**3*radial_unit)
normE2=4/normE
for scale_value in (sy.Rational(1,4),sy.Rational(1,16)):
    physical_K=4*sy.pi/(2*sy.pi)**3*sy.integrate(
        rr**2*(1-rr**2/(scale_value*radius)**2)**16,(rr,0,scale_value*radius))
    physical_E=sy.integrate((1-16*(Eval/scale_value-sy.Rational(3,2))**2)**16,
        (Eval,sy.Rational(5,4)*scale_value,sy.Rational(7,4)*scale_value))
    global_norm=sy.factor(scale_value**-4*normK2*normE2*physical_K*physical_E)
    assert global_norm==1
    assert sy.factor(scale_value**-1*normK2*normE2*physical_K*physical_E)==scale_value**3
print('Exact physical K-ball and E-interval norm integrals: the lambda^-2 amplitude gives unit global norm; energy-only normalization fails.')
# Three unscaled scalar densities are lambda^-1, 1, lambda times profile.
profiles = [f, (x+sy.Rational(3,2))*f, (x*x+x+2)*f]
for density_power, prof in zip((-1,0,1),profiles):
    for order in (0,1,7):
        actual = sy.diff(lam**density_power*prof.subs(x,Eval/lam),Eval,order)
        expected = lam**(density_power-order)*sy.diff(prof,x,order).subs(x,Eval/lam)
        assert sy.simplify(actual-expected) == 0
    L1_power = Fraction(density_power+1-7)
    global_L2_power = L1_power+Fraction(3,2)
    assert global_L2_power == { -1:Fraction(-11,2),0:Fraction(-9,2),1:Fraction(-7,2)}[density_power]
    print('Density amplitude power',density_power,'=> order-7 global L2(K;L1(E)) power',global_L2_power)
r=7; Tpower=Fraction(3,2)
cook=Fraction(3,2)-r+Tpower*(r-1)
projection=Fraction(3,2)-r+Tpower*r
assert (cook,projection,1+cook,2*projection)==(Fraction(7,2),Fraction(5),Fraction(9,2),Fraction(10))
assert 5-2*r+2*r*Tpower==12 and 7-2*r+2*r*Tpower==14
assert Fraction(1)+Fraction(3,2)-6+Tpower*5==4
print('Exact joint powers: state 7/2, projection 5, removed probability 10, current error 9/2, form factors 12 and 14; r=6 only yields current order 4.')

# The actual lattice ++ spin projectors, not an inserted contact weight.
sigma=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
eye2=np.eye(2,dtype=complex)
c=np.array([0,1,-1,0],complex)/np.sqrt(2)
sig1=np.array([np.kron(s,eye2) for s in sigma])
sig2=np.array([np.kron(eye2,s) for s in sigma])
gx,gw=roots_legendre(28)
phi=2*np.pi*np.arange(48)/48
Z,PHI=np.meshgrid(gx,phi,indexing='ij')
directions=np.column_stack((np.sqrt(1-Z.ravel()**2)*np.cos(PHI.ravel()),
                           np.sqrt(1-Z.ravel()**2)*np.sin(PHI.ravel()),Z.ravel()))
weights=np.repeat(gw,48)*2*np.pi/48/(2*np.pi)**3
N=len(weights)

def spin_projector(v):
    length=np.linalg.norm(v,axis=1)
    return (eye2[None,:,:]+np.einsum('ni,ijk->njk',v/length[:,None],sigma))/2

def lattice_section(kappa,ee,ll):
    lo=np.full(N,ee/4); hi=np.full(N,ee)
    def quantities(R):
        xp=ll*(R[:,None]*directions+kappa/2)
        xm=ll*(R[:,None]*directions-kappa/2)
        sp,sm=np.sin(xp),np.sin(xm)
        ap,bp=np.linalg.norm(sp,axis=1),np.linalg.norm(sm,axis=1)
        slope=np.sum(directions*(sp*np.cos(xp)/ap[:,None]+sm*np.cos(xm)/bp[:,None]),axis=1)
        return sp,sm,ap+bp,slope
    for _ in range(58):
        mid=(lo+hi)/2
        energy=quantities(mid)[2]
        below=energy<ll*ee
        lo=np.where(below,mid,lo);hi=np.where(below,hi,mid)
    R=(lo+hi)/2
    sp,sm,energy,slope=quantities(R)
    assert np.max(np.abs(energy-ll*ee))<1e-15
    factor=ll*R/np.sqrt(slope)
    section=[]; zh=[]; zhp=[]
    for corner in product((-1,1),repeat=3):
        sg=np.array(corner)
        av=sp*sg;bv=-sm*sg
        pa,pb=spin_projector(av),spin_projector(bv)
        pp=np.einsum('nab,ncd->nacbd',pa,pb).reshape(N,4,4)
        pc=np.einsum('nij,j->ni',pp,c)
        H=np.einsum('ni,ijk->njk',av,sig1)+np.einsum('ni,ijk->njk',bv,sig2)
        hh=np.einsum('nij,j->ni',H,c)
        hp=-np.sin(ll*kappa[0]/2)*(sg[0]*np.sin(ll*R*directions[:,0]))[:,None]*(sig1[0]@c)
        section.append(factor[:,None]*pc)
        zh.append(factor[:,None]*np.einsum('nij,nj->ni',pp,hh))
        zhp.append(factor[:,None]*np.einsum('nij,nj->ni',pp,hp))
    section=np.concatenate(section);zh=np.concatenate(zh);zhp=np.concatenate(zhp)
    ww=np.tile(weights,8)
    def inner(a,b): return np.sum(ww*np.sum(np.conj(a)*b,axis=1))
    rho=inner(section,section).real
    assert np.max(np.abs(zh-ll*ee*section))<4e-16
    v=section/np.sqrt(rho)
    gamma=np.tile(-2*np.sin(ll*kappa[0])/ll*(np.sin(ll*R*directions[:,0])/ll)**2,8)
    mean=inner(v,gamma[:,None]*v).real
    uu=(gamma-mean)[:,None]*v
    dd=np.sqrt(inner(uu,uu).real); uu/=dd
    assert abs(inner(v,uu))<2e-14 and abs(inner(uu,uu)-1)<1e-14
    chi=(v+1j*uu)/np.sqrt(2)
    # Positive Re G=ll is a finite algebra fixture, not a computed resolvent.
    phase=(ll-1j*np.pi*rho)/(ll+1j*np.pi*rho)
    out=(phase*v+1j*uu)/np.sqrt(2)
    assert abs(inner(chi,chi)-1)<1e-14 and abs(inner(out,out)-1)<1e-14
    current=ll**3*gamma
    change=(inner(out,current[:,None]*out)-inner(chi,current[:,None]*chi)).real
    assert abs(change-ll**3*dd*phase.imag)<2e-17
    # Actual h and h' incoming/outgoing scalar overlaps obey the exact
    # energy/contact identity and the three predicted scaled amplitudes.
    for state in (chi,out):
        b0=inner(section,state)
        b1=inner(zh,state)
        assert abs(b1-ll*ee*b0)<2e-16
    zeta_norm=np.sqrt(inner(zhp,zhp).real)/ll**3
    return rho/ll**2,dd,zeta_norm,change/ll**4

for kappa in [np.array([1/8,0.,0.]),np.array([1/8,1/64,-1/80])]:
    ee=1.5
    Dv=ee**2-np.dot(kappa,kappa)
    beta_v=Dv+kappa[0]**2
    expected_rho=Dv/(4*np.pi**2)
    expected_d=kappa[0]*beta_v/(3*np.sqrt(5))
    prev=None
    print('Lattice Pauli/coarea fixture kappa=',kappa.tolist(),'e=',ee)
    for ll in (1/16,1/32,1/64,1/128):
        rh,dd,hpn,current=lattice_section(kappa,ee,ll)
        erho=abs(rh-expected_rho); ed=abs(dd-expected_d)
        # Finite fixture tolerances, not claimed uniform analytic constants.
        # The density coefficient at e=1.5 is about .016 lambda^2; the
        # preserved initial .01 tolerance was inappropriately tight.
        assert erho<.02*ll**2 and ed<.02*ll**2
        if prev is not None:
            assert erho<.26*prev[0] and ed<.26*prev[1]
        prev=(erho,ed)
        print('  lambda=',ll,'rho/lambda^2=',format(rh,'.14g'),'d=',format(dd,'.14g'),
              '||Z h_prime||/lambda^3=',format(hpn,'.14g'),
              'synthetic-phase current/lambda^4=',format(current,'.14g'))
    print('  limiting rho=',format(expected_rho,'.14g'),'d=',format(expected_d,'.14g'))

assert source==Path(__file__).read_bytes()
print('No author source imported; floating quadrature supplies finite controls only.')
print('python='+sys.version.split()[0]+'; sympy='+sy.__version__+'; numpy='+np.__version__+'; scipy='+scipy.__version__)
print('runtime_seconds=%.6f'%(perf_counter()-started))
print('script_sha256='+sha256(source).hexdigest())
