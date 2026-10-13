#!/usr/bin/env python3
"""Direct radiation consistency and a separately reconstructed candidate.

All observations here are exposed calibration/development information.
This script does not run a raw CMB likelihood or certify a negative packet.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import sys

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
import sympy as sp

HERE = Path(__file__).resolve().parent
FIX = json.loads((HERE / 'NUMERICAL_FIXTURES_v1.json').read_text())
CHECKS = []


def check(name, passed, **evidence):
    CHECKS.append({'name': name, 'passed': bool(passed), **evidence})


def close(name, actual, expected, atol=2e-11, rtol=2e-11):
    actual, expected = float(actual), float(expected)
    err = abs(actual-expected)
    tol = atol + rtol*max(abs(actual), abs(expected))
    check(name, np.isfinite(actual) and err <= tol, actual=actual,
          expected=expected, error=err, tolerance=tol)


def exact(name, expression):
    r = sp.factor(sp.cancel(expression))
    check(name, r == 0, reduced_expression=str(r))
    return str(r)


def symbolic_identities():
    a, s, r, l = sp.symbols('a S R L', positive=True)
    d = lambda z: sp.diff(z, s)+4*r/(3*s)*sp.diff(z, r)
    hb2 = sp.Rational(2, 3)*((1+a)*s+l)
    bden = (2+a)*s+2*l
    hf2 = hb2*(1+2*r/bden)
    derivative = -sp.Rational(3, 2)*s*sp.diff(hf2, s)-2*r*sp.diff(hf2, r)
    ray = -s-sp.Rational(4, 3)*r-a*s*hf2/hb2
    residual = 2*a*r*s*((2+a)*s-l)/(3*bden**2)
    answer = {'old_residual': str(residual)}
    exact('old Friedmann versus Raychaudhuri residual', derivative-ray-residual)
    exact('old dust-only limit', residual.subs(r, 0))
    exact('old isolated residual root', residual.subs(s, l/(2+a)))
    w = s+sp.Rational(4, 3)*r
    c = (1+a)*(s+r)+l
    h2 = sp.Rational(2, 3)*c
    u = l+a*s/2+a*r/3
    v2 = a*w
    exact('new Friedmann', 3*h2-2*(s+r)-v2-2*u)
    exact('new Raychaudhuri', -sp.Rational(3, 2)*s*d(h2)+w+v2)
    # Divide the chi equation by a H/v, an everywhere nonzero factor.
    exact('new chi Klein Gordon', -(3*s+sp.Rational(16, 3)*r)/2
          +3*w-3*s*d(u)/a)
    exact('new u Klein Gordon', -sp.sqrt(a)*s+sp.sqrt(a)*s)
    f = 9*h2*s*s/(a*w)
    usc = d(u)
    ussc = d(usc)
    hchi = f*ussc+d(f)*usc/2
    exact('U first derivative', usc-a*(sp.Rational(1, 2)+4*r/(9*s)))
    exact('U second derivative', ussc-4*a*r/(27*s*s))
    rr = r/s
    df_positive = (18/a)*(((1+a)*(1+4*rr/3)*s*(3+4*rr)
                          +c*(3+8*rr/3))/(3+4*rr)**2)
    exact('positive coordinate derivative decomposition', d(f)-df_positive)
    m = a*f/hchi+a*s*s/u
    exact('bare Hessian determinant', m*hchi-a*f-a*s*s*hchi/u)
    uu = sp.symbols('u', real=True)
    v = u-sp.sqrt(a)*s*uu+m*uu*uu/2
    exact('global transverse complete square', v-
          (m*(uu-sp.sqrt(a)*s/m)**2/2+u-a*s*s/(2*m)))
    g = a*w/(9*h2)
    gamma = s*d(g)/(2*g)
    vq = s*d(u)
    uq2 = s*d(vq)
    exact('canonical and coordinate Hessian', hchi-(uq2-gamma*vq)/g)
    hh = -(1+a)*w/h2
    exact('coordinate Friedmann denominator',
          2*(s+r+u)/(3-9*g)-h2)
    exact('coordinate p acceleration on exact solution',
          3*(3+hh)-9*gamma-vq/(g*h2))
    answer['positive_U_chichi'] = str(sp.factor(hchi))
    answer['coordinate_gamma'] = str(sp.factor(gamma))
    answer['dust_field_speed_squared_over_a'] = str(sp.Rational(3, 2)/(1+a))
    answer['radiation_field_speed_squared_over_a'] = str(2/(1+a))
    return answer


def thermal_calibration():
    p = FIX['constants']
    h, k, c, gn = (p[x] for x in ['h_Js', 'k_J_per_K', 'c_m_per_s', 'G_N_SI'])
    i3, e3 = quad(lambda x: x**3*np.exp(-x)/(-np.expm1(-x)), 0, np.inf,
                  epsabs=2e-12, epsrel=2e-12)
    i2, e2 = quad(lambda x: x**2*np.exp(-x)/(-np.expm1(-x)), 0, np.inf,
                  epsabs=2e-12, epsrel=2e-12)
    close('Bose energy integral', i3, np.pi**4/15)
    close('Bose number integral', i2, 2*float(mp.zeta(3)))
    hzero = FIX['H0_km_per_s_Mpc']*1000/p['Mpc_m']
    rows = []
    for shift in [-1, 0, 1]:
        t = FIX['temperature_K']+shift*FIX['temperature_sigma_K']
        energy = 8*np.pi*(k*t)**4/(h**3*c**3)*i3
        rho = energy/c**2
        number = 8*np.pi*(k*t)**3/(h**3*c**3)*i2
        omega = 8*np.pi*gn*rho/(3*hzero**2)
        close('photon pressure relation '+str(shift), energy/3, rho*c*c/3,
              atol=1e-30, rtol=2e-12)
        rows.append({'temperature_K': t, 'sigma_shift': shift,
                     'energy_J_per_m3': energy, 'mass_density_kg_per_m3': rho,
                     'number_per_m3': number, 'Omega_gamma': omega})
    data = HERE/'data/FIRAS_monopole.txt'
    check('FIRAS data hash', hashlib.sha256(data.read_bytes()).hexdigest()==FIX['data_sha256'])
    table = np.loadtxt(data)
    check('FIRAS43 rows5 columns', table.shape==(43, 5), shape=list(table.shape))
    baseline = FIX['baseline_temperature_K']
    def intensity(wn):
        nu = wn*100*c
        return 2*h*nu**3/c**2/np.expm1(h*nu/(k*baseline))/1e-20
    xpeak = brentq(lambda x: 3*(-np.expm1(-x))-x, 2., 4.)
    wnpeak = xpeak*k*baseline/(h*c*100)
    evidence = []
    for j, (wn, absolute, resid, sigma, galaxy) in enumerate(table):
        width = FIX['spectrum_controls']['frequency_rounding_halfwidth_cm_inverse']
        sites = [wn-width, wn+width]
        if sites[0] <= wnpeak <= sites[1]:
            sites.append(wnpeak)
        vals = [intensity(x) for x in sites]
        rounding = FIX['spectrum_controls']['intensity_rounding_halfwidth_MJy_per_sr']
        rounding += FIX['spectrum_controls']['residual_rounding_halfwidth_kJy_per_sr']/1000
        lo, hi = min(vals)+resid/1000-rounding, max(vals)+resid/1000+rounding
        check('FIRAS stated baseline/rounding '+str(j), lo<=absolute<=hi,
              published_MJy_per_sr=absolute, lower=lo, upper=hi)
        check('FIRAS positive published error '+str(j), sigma>0, error_kJy_per_sr=sigma)
        evidence.append({'wavenumber_cm_inverse': wn, 'absolute_MJy_per_sr': absolute,
                         'residual_kJy_per_sr': resid, 'sigma_kJy_per_sr': sigma,
                         'galaxy_kJy_per_sr': galaxy, 'rounded_baseline_interval':[lo, hi]})
    r, err = table[:, 2], table[:, 3]
    return {'thermal_rows': rows, 'H0_s_inverse': hzero,
            'Bose_integrals':[i2, i3], 'quadrature_error_estimates':[e2, e3],
            'FIRAS_rows': evidence,
            'FIRAS_diagonal_residual_sum_only': float(np.sum((r/err)**2)),
            'FIRAS_weighted_RMS_kJy_per_sr': float(np.sqrt(np.sum((r/err)**2)/np.sum(1/err**2))),
            'roles':'T is exposed calibration; H0=70 and m=.3 supplied. Published baseline identity is a data-description control. No independent spectral likelihood or fit.'}


def local_functions(x, a, b, l):
    s = np.exp(x)
    r = b*np.exp(4*x/3)
    w = s+4*r/3
    wq = s+16*r/9
    c = (1+a)*(s+r)+l
    cq = (1+a)*w
    h2 = 2*c/3
    g = a*w/(6*c)
    gamma = (wq/w-cq/c)/2
    u = l+a*s/2+a*r/3
    uq = a*s/2+4*a*r/9
    uqq = a*s/2+16*a*r/27
    curvature_numerator = uqq-gamma*uq
    uchi2 = curvature_numerator/g
    m = a*s*s/curvature_numerator+a*s*s/u
    return {'S':s,'R':r,'W':w,'C':c,'H2':h2,'g':g,'Gamma':gamma,
            'U':u,'Uq':uq,'Uqq':uqq,'Uchichi':uchi2,'M':m}


def potential(u, x, a, b, l):
    z = local_functions(x, a, b, l)
    mq = np.imag(local_functions(x+1e-25j, a, b, l)['M'])/1e-25
    v = z['U']-np.sqrt(a)*z['S']*u+z['M']*u*u/2
    vu = -np.sqrt(a)*z['S']+z['M']*u
    vx = z['Uq']-np.sqrt(a)*z['S']*u+mq*u*u/2
    return v, vu, vx, z


def rhs(n, y, a, b, l):
    u, x, wu, px, lm, lr = y
    sm, sr = np.exp(lm), np.exp(lr)
    v, vu, vx, z = potential(u, x, a, b, l)
    denom = 3-wu*wu-z['g']*px*px
    if denom <= 0 or sm+sr+v <= 0:
        raise ValueError(('nonpositive Friedmann data', n, denom, sm+sr+v))
    h2 = 2*(sm+sr+v)/denom
    hh = -(sm+4*sr/3)/h2-wu*wu-z['g']*px*px
    return np.array([wu, px, -(3+hh)*wu-(vu+np.sqrt(a)*sm)/h2,
                     0.,
                     -3+np.sqrt(a)*wu, -4.])


def algebra_grid():
    rows = []
    for a in FIX['couplings']:
        for r in FIX['radiation_to_matter']:
            for l in FIX['vacuum_to_matter']:
                z = local_functions(0., a, r, l)
                # An independent numerical derivative of U_q/g coordinate formula.
                uq_derivative = np.imag(local_functions(1e-25j, a, r, l)['Uq'])/1e-25
                gq = np.imag(local_functions(1e-25j, a, r, l)['g'])/1e-25
                close('grid Uqq', uq_derivative, z['Uqq'])
                close('grid connection', gq/(2*z['g']), z['Gamma'])
                f = 1/z['g']
                hess = np.array([[z['M'], np.sqrt(a/z['g'])],
                                 [np.sqrt(a/z['g']), z['Uchichi']]])
                # Scale eigenvalues before checking to avoid a large unit setting.
                ev = np.linalg.eigvalsh(hess/z['H2'])
                check('grid positive bare Hessian', np.min(ev)>0, a=a, r=r, l=l,
                      eigenvalues_over_H2=ev.tolist())
                close('grid Hessian determinant', np.linalg.det(hess)/z['H2']**2,
                      (a/z['U'])*z['Uchichi']/z['H2']**2)
                for uval in [-10, -1, -np.sqrt(a), 0, np.sqrt(a), 1, 10]:
                    v, vu, vx, zz = potential(uval, 0., a, r, l)
                    check('grid global transverse lower bound', v>=z['U']/2,
                          value=float(v), bound=float(z['U']/2), u=uval)
                if r>0:
                    yy=np.array([0.,0.,0.,-3.,0.,np.log(r)])
                    deriv=rhs(0., yy, a, r, l)
                    close('grid u acceleration', deriv[2], 0.)
                    close('grid x acceleration', deriv[3], 0.)
                    close('grid dust conservation', deriv[4], -3.)
                    close('grid radiation conservation', deriv[5], -4.)
                rows.append({'a':a,'R_over_S':r,'L_over_S':l,
                             'local':{k:float(v)for k,v in z.items()},
                             'eigenvalues_over_H2':ev.tolist()})
    return rows


def old_potential_responses(omega):
    rows=[]
    for a in FIX['couplings']:
        s0=1.5*FIX['matter_fraction']/(1+a)
        r0=1.5*omega/(1+a)
        l=FIX['old_potential_L']
        for zred in FIX['redshifts']:
            s=s0*(1+zred)**3
            r=r0*(1+zred)**4
            hb2=2*((1+a)*s+l)/3
            den=(2+a)*s+2*l
            hf2=hb2*(1+2*r/den)
            # Analytic partials of the original Friedmann solution.
            hs=2*(1+a)/3*(1+2*r/den)-2*hb2*r*(2+a)/den**2
            hr=2*hb2/den
            differentiated=-1.5*s*hs-2*r*hr
            ray=-s-4*r/3-a*s*hf2/hb2
            delta=2*a*r*s*((2+a)*s-l)/(3*den**2)
            close('old potential radiation residual', (differentiated-ray)/hf2,
                  delta/hf2, atol=3e-14, rtol=2e-10)
            rows.append({'a':a,'z':zred,'S':s,'R':r,'H2_forced':hf2,
                         'residual_over_H2':delta/hf2,
                         'derivative_residual_over_H2':(differentiated-ray)/hf2})
    return rows


def exact_background_integrations(omega):
    rows=[]
    n0=-math.log(1000001)
    sites=sorted(set([-math.log1p(z)for z in FIX['redshifts']]+FIX['future_N_sites']))
    cfg=FIX['integration']
    for a in FIX['couplings']:
        s0=1.5*FIX['matter_fraction']/(1+a)
        r0=1.5*omega/(1+a)
        b=r0/s0**(4/3)
        l=1.5*(1-FIX['matter_fraction']-omega)
        initial=np.array([0.,math.log(s0)-3*n0,0.,-3.,math.log(s0)-3*n0,math.log(r0)-4*n0])
        runs=[]
        target=np.array([[0.,math.log(s0)-3*n,0.,-3.,math.log(s0)-3*n,math.log(r0)-4*n]for n in sites])
        for j in range(2):
            sol=solve_ivp(lambda n,y:rhs(n,y,a,b,l),(n0,6.),initial,
                          method='DOP853',rtol=cfg['rtol'][j],atol=cfg['atol'][j],
                          max_step=cfg['max_step'][j],dense_output=True)
            check('background solver success', sol.success, a=a, refinement=j,
                  message=sol.message, nfev=sol.nfev)
            values=sol.sol(sites).T
            tol=cfg['comparison_atol']+cfg['comparison_rtol']*np.maximum(np.abs(values),np.abs(target))
            scaled=np.abs(values-target)/tol
            check('background full-state exact trajectory', np.max(scaled)<1,
                  a=a,refinement=j,max_tolerance_units=float(np.max(scaled)))
            runs.append({'refinement':j,'nfev':sol.nfev,'states':values.tolist(),
                         'max_tolerance_units':float(np.max(scaled))})
        r0v=np.array(runs[0]['states']);r1v=np.array(runs[1]['states'])
        tol=cfg['comparison_atol']+cfg['comparison_rtol']*np.maximum(np.abs(r0v),np.abs(r1v))
        check('background step refinement', np.max(np.abs(r0v-r1v)/tol)<1,
              a=a,max_tolerance_units=float(np.max(np.abs(r0v-r1v)/tol)))
        chis=[]
        for n in sites:
            chi,err=quad(lambda q:-math.sqrt(local_functions(q,a,b,l)['g']),
                         math.log(s0),math.log(s0)-3*n,epsabs=2e-12,epsrel=2e-12)
            zz=local_functions(math.log(s0)-3*n,a,b,l)
            chis.append({'N':n,'chi_minus_chi_present':chi,'quadrature_error':err,
                         'field_speed_over_sqrt_a':math.sqrt(zz['W']/zz['H2']),
                         'potential_slope_minus_dlogU_dchi':zz['Uq']/(zz['U']*math.sqrt(zz['g']))})
        rows.append({'a':a,'b':b,'L':l,'S0':s0,'R0':r0,'sites_N':sites,
                     'target_states':target.tolist(),'runs':runs,'canonical_coordinates':chis})
    return rows


def endpoint_controls():
    cfg=FIX['endpoint_series'];mp.mp.dps=cfg['digits'];rows=[]
    for aa in cfg['a']:
        for bb in cfg['b']:
            a,b,l=map(mp.mpf,map(str,[aa,bb,cfg['L']]))
            hv=mp.sqrt(2*l/3);cc=2*mp.sqrt(a)/(3*hv)
            def parts(s):
                r=b*s**(mp.mpf(4)/3);w=s+4*r/3;c=(1+a)*(s+r)+l
                g=a*w/(6*c);ga=((s+16*r/9)/w-(1+a)*w/c)/2
                u=l+a*s/2+a*r/3;uq=a*s/2+4*a*r/9;uqq=a*s/2+16*a*r/27
                hchi=(uqq-ga*uq)/g
                return g,u,hchi
            series=[]
            for sval in cfg['S']:
                s=mp.mpf(str(sval))
                # t=sqrt(S), so the endpoint quadrature has no sqrt singularity.
                delta=mp.quad(lambda t:2*mp.sqrt(parts(t*t)[0])/t,[0,mp.sqrt(s)])
                q=delta/cc
                g,u,hchi=parts(s)
                sc=(s-q*q)/(b*q**(mp.mpf(8)/3))
                uc=(u-l-a*q*q/2)/(a*b*q**(mp.mpf(8)/3))
                third=-s/mp.sqrt(g)*mp.diff(lambda ss:parts(ss)[2],s)
                third_scaled=third*delta**(mp.mpf(1)/3)
                third_limit=16*a*b/(81*cc**(mp.mpf(8)/3))
                series.append({'S':str(s),'delta_chi':str(delta),'S_series_coefficient':str(sc),
                               'U_series_coefficient':str(uc),'U_chichi':str(hchi),
                               'scaled_third_derivative':str(third_scaled),'third_derivative_limit':str(third_limit)})
            last=series[-1]
            for label,key,value in [('S','S_series_coefficient',-.8),('U','U_series_coefficient',-1/15)]:
                close('future fractional series '+label,float(last[key]),value,
                      atol=cfg['last_coefficient_relative_tolerance']*abs(value),rtol=0)
            close('future scaled third derivative',float(last['scaled_third_derivative'])/float(last['third_derivative_limit']),1.,
                  atol=cfg['last_coefficient_relative_tolerance'],rtol=0)
            close('future finite second derivative',float(last['U_chichi']),float(a/cc**2),
                  atol=2e-8,rtol=2e-8)
            rows.append({'a':aa,'b':bb,'L':float(l),'canonical_endpoint_scale':str(cc),'series':series})
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-json',required=True);args=ap.parse_args()
    destination=Path(args.output_json)
    if destination.exists():raise FileExistsError(destination)
    result={'started_at':datetime.now(timezone.utc).isoformat(),
            'roles':'Exposed observations calibrate candidate construction; no independent empirical test.'}
    result['symbolic']=symbolic_identities()
    result['thermal']=thermal_calibration()
    omega=result['thermal']['thermal_rows'][1]['Omega_gamma']
    result['local_grid']=algebra_grid()
    result['old_potential']=old_potential_responses(omega)
    result['new_background']=exact_background_integrations(omega)
    result['endpoint']=endpoint_controls()
    result['checks']=CHECKS
    result['checks_passed']=sum(x['passed']for x in CHECKS)
    result['checks_failed']=sum(not x['passed']for x in CHECKS)
    result['ended_at']=datetime.now(timezone.utc).isoformat()
    result['versions']={'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,'mpmath':mp.__version__}
    result['source_hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in
        [Path(__file__),HERE/'HAND_DERIVATION_v2.md',HERE/'PROTOCOL_v1.json',HERE/'NUMERICAL_FIXTURES_v1.json',HERE/'SOURCE_LEDGER_v1.json',HERE/'data/FIRAS_monopole.txt']}
    with destination.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({'checks_passed':result['checks_passed'],'checks_failed':result['checks_failed'],
                      'Omega_gamma':omega,'failures':[x for x in CHECKS if not x['passed']]},indent=2))
    return 0 if result['checks_failed']==0 else 1


if __name__=='__main__':
    sys.exit(main())
