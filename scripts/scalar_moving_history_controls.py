"""Synthetic controls for temporal KG gradients on moving observation paths.
No observational samples or physical energy/readout calibrations are used.
"""
from pathlib import Path
import json, hashlib, time
import numpy as np
import sympy as sp
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC=120

def cq(fun,a,b):
    real=quad(lambda s: float(np.real(fun(s))),a,b,epsabs=3e-12,epsrel=3e-12,limit=400)[0]
    imag=quad(lambda s: float(np.imag(fun(s))),a,b,epsabs=3e-12,epsrel=3e-12,limit=400)[0]
    return real+1j*imag

def run_checks():
    checks=[];modes=[];straight=[];geometry=[]
    def check(name,condition):
        assert bool(condition),name
        checks.append(name)
    s=sp.symbols('s',real=True);w=sp.Function('w')(s);d=sp.Function('d')(s)
    expanded=sp.diff(sp.diff(w/d,s)/d,s)
    claimed=sp.diff(w,s,2)/d**2-3*sp.diff(w,s)*sp.diff(d,s)/d**3-w*sp.diff(d,s,2)/d**3+3*w*sp.diff(d,s)**2/d**4
    check('twice_IBP_coefficients',sp.simplify(expanded-claimed)==0)
    B,W0,k=sp.symbols('B W0 k',positive=True)
    cut=sp.sqrt(B/W0)
    radial=sp.integrate(k*k*W0**2,(k,0,cut))+sp.integrate(B*B/k**2,(k,cut,sp.oo))
    check('radial_envelope_integral',sp.simplify(radial-sp.Rational(4,3)*B**sp.Rational(3,2)*sp.sqrt(W0))==0)
    check('fixed_projection_constant',sp.simplify(radial/(6*sp.pi**2)-2*B**sp.Rational(3,2)*sp.sqrt(W0)/(9*sp.pi**2))==0)
    check('rotating_projection_constant',sp.simplify(radial/(2*sp.pi**2)-2*B**sp.Rational(3,2)*sp.sqrt(W0)/(3*sp.pi**2))==0)
    T=1.2;u=.18;amp=.04;omx=1.7;b=.025;rho=.43
    def path(t): return np.array([u*t,amp*np.sin(omx*t),b*t*t/2])
    def vel(t): return np.array([u,amp*omx*np.cos(omx*t),b*t])
    def acc(t): return np.array([0.,-amp*omx**2*np.sin(omx*t),b])
    def jerk(t): return np.array([0.,-amp*omx**3*np.cos(omx*t),0.])
    def nvec(t): return np.array([np.cos(rho*t),np.sin(rho*t),0.])
    def ndot(t): return rho*np.array([-np.sin(rho*t),np.cos(rho*t),0.])
    def nddot(t): return -rho*rho*nvec(t)
    vmax=np.sqrt(u*u+(amp*omx)**2+(b*T)**2)
    accel=np.sqrt((amp*omx**2)**2+b*b);jmax=abs(amp*omx**3);delta=1-vmax
    W0n=1.;W1=2/T;W2=4/T**2
    Bfixed=W2/delta**2+3*accel*W1/delta**3+jmax/delta**3+3*accel**2/delta**4
    Brot=(W2+2*abs(rho)*W1+rho**2)/delta**2+3*accel*(W1+abs(rho))/delta**3+jmax/delta**3+3*accel**2/delta**4
    check('subluminal_path',0<vmax<1)
    grid=np.linspace(-T,T,301)
    check('velocity_fixture_bound',max(np.linalg.norm(vel(t)) for t in grid)<=vmax)
    check('acceleration_fixture_bound',max(np.linalg.norm(acc(t)) for t in grid)<=accel)
    check('jerk_fixture_bound',max(np.linalg.norm(jerk(t)) for t in grid)<=jmax+1e-15)
    maxerr=0.;no_jump_witnesses=[];wrong_sign_witnesses=[]
    for mu in [0.,.8]:
      for kv in [np.array([.3,.4,.2]),np.array([2.,-1.,.7]),np.array([-7.,3.,5.]),np.array([40.,-20.,10.])]:
       omega=np.sqrt(kv@kv+mu*mu);r=kv/omega
       for sign in [-1.,1.]:
        def phase(t): return np.exp(-1j*(sign*omega*t-kv@path(t)))
        def den(t): return sign-r@vel(t)
        def dp(t): return -r@acc(t)
        def dpp(t): return -r@jerk(t)
        for rotating in [False,True]:
         def f(t): return r@nvec(t) if rotating else 1.
         def fp(t): return r@ndot(t) if rotating else 0.
         def fpp(t): return r@nddot(t) if rotating else 0.
         def weight(t): return (T-abs(t))/T**2
         direct=cq(lambda t: weight(t)*f(t)*phase(t),-T,0)+cq(lambda t:weight(t)*f(t)*phase(t),0,T)
         regular=0j
         for lo,hi,wp in [(-T,0,1/T**2),(0,T,-1/T**2)]:
          def transformed(t):
           ww=weight(t);aa=ww*f(t);ap=wp*f(t)+ww*fp(t)
           app=2*wp*fp(t)+ww*fpp(t)
           dd=den(t)
           return phase(t)*(app/dd**2-3*ap*dp(t)/dd**3-aa*dpp(t)/dd**3+3*aa*dp(t)**2/dd**4)
          regular+=cq(transformed,lo,hi)
         jump=sum(coeff*f(t)*phase(t)/den(t)**2 for t,coeff in [(-T,1/T**2),(0,-2/T**2),(T,1/T**2)])
         recovered=-(regular+jump)/omega**2
         envelope=min(W0n,(Brot if rotating else Bfixed)/omega**2)
         error=abs(direct-recovered);maxerr=max(maxerr,error)
         label=f'{mu}_{tuple(kv)}_{sign}_{rotating}'
         check('IBP_with_measure_'+label,error<2e-10)
         check('nonstationary_envelope_'+label,abs(direct)<=envelope+1e-11)
         check('frequency_nonstationarity_'+label,min(abs(den(t)) for t in grid)>=delta-1e-14)
         no_jump_witnesses.append(abs(direct+regular/omega**2))
         wrong_sign_witnesses.append(abs(direct+recovered))
         modes.append(dict(mu=mu,k=kv.tolist(),frequency_sign=sign,rotating=rotating,
                          direct=[direct.real,direct.imag],integrated_by_parts=[recovered.real,recovered.imag],
                          discrepancy=error,envelope=envelope,omitted_jump_error=no_jump_witnesses[-1]))
    check('omitted_distribution_jumps_rejected',max(no_jump_witnesses)>.1)
    check('wrong_global_IBP_sign_rejected',max(wrong_sign_witnesses)>1.)
    # Exact massless constant-velocity norms obtained by radial change of variable,
    # with angular quadrature independent of the coarse nonstationary envelope.
    for tt in [.5,1.,2.]:
     stationary=1/(3*np.pi*tt**3)
     for speed in [0.,.2,.65,.9]:
      para=quad(lambda z:z*z/(1-speed*z)**3,-1,1,epsabs=1e-12)[0]/(2*np.pi*tt**3)
      perp=quad(lambda z:(1-z*z)/(1-speed*z)**3,-1,1,epsabs=1e-12)[0]/(4*np.pi*tt**3)
      coarse=2/(9*np.pi**2)*(4/((1-speed)**2*tt**2))**1.5
      check(f'straight_envelope_{tt}_{speed}',max(para,perp)<=coarse+1e-12)
      if speed==0:
       check(f'stationary_limit_{tt}',max(abs(para-stationary),abs(perp-stationary))<1e-12)
      else:
       check(f'stationary_norm_not_reused_{tt}_{speed}',para>stationary and perp>stationary)
      straight.append(dict(T=tt,speed=speed,parallel_norm_squared=para,perpendicular_norm_squared=perp,
                           coarse_norm_squared=coarse,stationary_norm_squared=stationary))
    # Adjacent averages of the actual rotating readout, not of a different component.
    lhs=(cq(lambda t:nvec(t)@vel(t),0,T)-cq(lambda t:nvec(t)@vel(t),-T,0)).real/T**2
    term_force=(cq(lambda t:(T-abs(t))/T**2*(nvec(t)@acc(t)),-T,0)+cq(lambda t:(T-abs(t))/T**2*(nvec(t)@acc(t)),0,T)).real
    term_geometry=(cq(lambda t:(T-abs(t))/T**2*(ndot(t)@vel(t)),-T,0)+cq(lambda t:(T-abs(t))/T**2*(ndot(t)@vel(t)),0,T)).real
    check('rotating_velocity_readout_identity',abs(lhs-term_force-term_geometry)<2e-12)
    check('geometric_term_bound',abs(term_geometry)<=abs(rho)*vmax)
    check('dropped_geometric_term_rejected',abs(lhs-term_force)>1e-4)
    geometry=dict(adjacent_average_difference=lhs,triangular_projected_acceleration=term_force,
                  triangular_geometry_term=term_geometry,geometry_upper_bound=abs(rho)*vmax)
    result=dict(checks_passed=len(checks),checks=checks,modes=modes,straight_path_norms=straight,
                rotating_velocity_readout=geometry,max_IBP_discrepancy=maxerr,
                fixture_bounds=dict(T=T,vmax=vmax,A=accel,J=jmax,delta=delta,Bfixed=Bfixed,Brot=Brot),
                scope='Conditional moving-path energy functional under a frozen stable flat KG operator. No measured energy, path calibration, fitted data or independent observation.')
    return result
