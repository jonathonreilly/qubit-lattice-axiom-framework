"""Working temporal force/energy norm and adjacent-average controls.
Synthetic only; no actual radio-to-force or physical energy calibration.
"""
from pathlib import Path
import json,hashlib,time
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
import mpmath as mp
import sympy as sp

AUDIT_TIMEOUT_SEC=120
mp.mp.dps=40

def transform(omega,T):
    return np.sinc(omega*T/(2*np.pi))**2

def partial_norm2(mu,T,cutoff):
    fun=lambda om:(max(om*om-mu*mu,0.)**1.5/om)*transform(om,T)**2 if om else 0.
    pts=np.arange(2*np.pi/T,cutoff,2*np.pi/T)
    val,err=quad(fun,mu,cutoff,points=pts[pts>mu],epsabs=1e-10,epsrel=2e-10,limit=500)
    return val/(6*np.pi**2),err/(6*np.pi**2)

def run_checks():
    checks=[];norms=[];gauss=[];readouts=[]
    def check(label,cond):
        assert bool(cond),label
        checks.append(label)
    x,T=sp.symbols('x T',positive=True,real=True)
    derivative_norm=2*sp.integrate(1/T**4,(x,0,T))
    check('triangular_derivative_norm',sp.simplify(derivative_norm-2/T**3)==0)
    w=sp.symbols('w',nonzero=True,real=True)
    W=2*sp.integrate((T-x)*sp.cos(w*x)/T**2,(x,0,T))
    check('triangle_transform',sp.trigsimp(W-(sp.sin(w*T/2)/(w*T/2))**2)==0)
    check('angular_isotropy_factor',sp.integrate(2*sp.pi*x*x,(x,-1,1))==4*sp.pi/3)
    # Finite numerical integrals plus a rigorous analytic bound on the omitted
    # positive integrand. Quadrature errors themselves are not interval-certified.
    for tt in [.4,1.,2.3]:
        cutoff=300/tt
        exact=1/(3*np.pi*tt**3)
        values=[]
        for mm in [0.,.3/tt,1/tt,3/tt,10/tt]:
            val,err=partial_norm2(mm,tt,cutoff)
            tail=8/(3*np.pi**2*tt**4*cutoff)
            check(f'norm_positive_{tt}_{mm}',val>0)
            check(f'mass_enclosure_{tt}_{mm}',val<=exact+1e-10)
            if mm==0:
                check(f'massless_tail_enclosure_{tt}',val+tail>=exact-1e-10)
            values.append(val)
            norms.append(dict(mu=mm,T=tt,cutoff=cutoff,partial_norm_squared=val,
                              omitted_tail_upper_bound=tail,quadrature_error_estimate=err,
                              massless_exact_norm_squared=exact))
        check(f'mass_monotonicity_{tt}',all(b<a for a,b in zip(values,values[1:])))
    # Frequency versus direct time filtering for a smooth Gaussian initial field.
    # qhat=-i A ell^4 k1 exp(-ell^2 k^2/2), p=0. Its energy is known by integration.
    tx,tw=leggauss(72);kx,kw=leggauss(240)
    for mm,ell,tt,A in [(0.,.7,.8,.2),(.8,.9,1.3,.3),(2.,.6,.4,.1)]:
        kmax=14/ell;k=(kx+1)*kmax/2;wk=kw*kmax/2
        om=np.sqrt(k*k+mm*mm)
        coef=A*ell**4*(4*np.pi/3)/(2*np.pi)**1.5
        spec=coef*k**4*np.exp(-ell*ell*k*k/2)
        freq=np.sum(wk*spec*transform(om,tt))
        # Split at the triangle cusp; this is actual time quadrature of the
        # unfiltered time-domain Fourier evolution, not the transform formula.
        direct=0.
        for sign in [-1,1]:
            ts=sign*(tx+1)*tt/2
            weight=(tt-np.abs(ts))/tt**2
            fieldgrad=np.cos(np.outer(ts,om))@(wk*spec)
            direct+=np.sum(tw*tt/2*weight*fieldgrad)
        E=A*A*np.pi**1.5*ell*(5/8+mm*mm*ell*ell/4)
        upper=np.sqrt(2*E/(3*np.pi*tt**3))
        check(f'time_frequency_filter_{mm}',abs(direct-freq)<3e-12)
        check(f'Gaussian_energy_filter_{mm}',abs(freq)<=upper)
        gauss.append(dict(mu=mm,ell=ell,T=tt,A=A,frequency_average=float(freq),
                          direct_time_average=float(direct),energy=E,energy_upper_bound=upper,
                          discrepancy=float(abs(direct-freq))))
    # Check the Gaussian weight's Parseval normalization separately.
    for tt in [mp.mpf('.4'),mp.mpf('1.2')]:
        spectral=mp.quad(lambda om:om*om*mp.exp(-tt*tt*om*om),[0,mp.inf])/(6*mp.pi**2)
        derivative=mp.quad(lambda s:(-s/(tt**3*mp.sqrt(2*mp.pi))*mp.exp(-s*s/(2*tt*tt)))**2,[-mp.inf,0,mp.inf])
        check(f'Gaussian_Parseval_{tt}',abs(spectral-derivative/(6*mp.pi))<mp.mpf('1e-30'))
    # Rectangular weight cutoff norm and a finite-energy witness against
    # incorrectly applying the triangular norm to a rectangular force average.
    boxes=[]
    for tt in [.5,1.,2.]:
        for factor in [10.,40.,160.]:
            lam=factor/tt
            val=quad(lambda om:np.sin(om*tt)**2,0,lam,epsabs=1e-10)[0]/(6*np.pi**2*tt*tt)
            exact=(lam/2-np.sin(2*lam*tt)/(4*tt))/(6*np.pi**2*tt*tt)
            check(f'box_cutoff_formula_{tt}_{factor}',abs(val-exact)<2e-12)
            boxes.append(dict(T=tt,cutoff=lam,norm_squared=exact))
        check(f'box_not_triangle_witness_{tt}',boxes[-2]['norm_squared']>1/(3*np.pi*tt**3))
    # Direct polynomial identities, including arbitrary constants, then nonlinear
    # readouts with explicit count-average errors and a negative Doppler factor.
    z=sp.symbols('z',real=True)
    for n in range(7):
        v=z**n
        left=(sp.integrate(v,(z,0,T))-sp.integrate(v,(z,-T,0)))/T**2
        right=(sp.integrate((T+z)*sp.diff(v,z),(z,-T,0))+sp.integrate((T-z)*sp.diff(v,z),(z,0,T)))/T**2
        check(f'adjacent_velocity_identity_degree{n}',sp.simplify(left-right)==0)
    for tt,center in [(mp.mpf('.5'),mp.mpf('.3')),(mp.mpf('1.2'),mp.mpf('-.4'))]:
        v=lambda s:17+mp.exp(mp.mpf('.3')*s)+mp.sin(2*s)
        a=lambda s:mp.mpf('.3')*mp.exp(mp.mpf('.3')*s)+2*mp.cos(2*s)
        vm=mp.quad(v,[center-tt,center])/tt
        vp=mp.quad(v,[center,center+tt])/tt
        av=mp.quad(lambda u:(tt+u)/tt**2*a(center+u),[-tt,0])+mp.quad(lambda u:(tt-u)/tt**2*a(center+u),[0,tt])
        check(f'nonlinear_adjacent_identity_{tt}',abs((vp-vm)/tt-av)<mp.mpf('1e-30'))
        kap=mp.mpf(-2);f0=mp.mpf(7)
        dnp=mp.mpf('.02');dnm=-mp.mpf('.03')
        yp=kap*vp+123+dnp/(f0*tt)
        ym=kap*vm+123+dnm/(f0*tt)
        estimate=(yp-ym)/(kap*tt)
        eb=(abs(dnp)+abs(dnm))/(abs(kap*f0)*tt*tt)
        check(f'count_error_bound_{tt}',abs(estimate-av)<=eb+mp.mpf('1e-30'))
        readouts.append({'T':str(tt),'center':str(center),'triangular_acceleration':str(av),
                         'adjacent_velocity_difference':str((vp-vm)/tt),'count_readout':str(estimate),
                         'count_error_bound':str(eb)})
    result={'checks_passed':len(checks),'checks':checks,'mass_norms':norms,
            'Gaussian_initial_data_controls':gauss,'box_cutoff_controls':boxes,'adjacent_readouts':readouts,
            'scope':'Fixed-point temporal field functional and conditional leading velocity/count readout. No actual radio-force calibration, physical energy budget, localized state selection or observational test.'}
    return result
