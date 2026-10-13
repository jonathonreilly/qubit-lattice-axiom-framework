#!/usr/bin/env python3
"""Parent-authored matter-only vacuum response checks. No empirical fit.
The MS-bar free-electron finite part is a scheme-labelled diagnostic.
First-execution outputs are exclusive; frozen inputs are hash verified.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, sys, re, gzip
import sympy as sp
import mpmath as mp

HERE=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'evidence_v2'
INPUT=json.loads((HERE/'INPUTS_v1.json').read_text())
NIST=json.loads((HERE/'NIST_SELECTED_ROWS_v1.json').read_text())
FREEZE=json.loads((OUT/'FREEZE.json').read_text())
mp.mp.dps=80
CHECKS=[]
def number(s):
    parts=str(s).split('/')
    return mp.mpf(parts[0]) if len(parts)==1 else mp.mpf(parts[0])/mp.mpf(parts[1])
def stamp():return datetime.now(timezone.utc).isoformat()
def exact(name,expr):
    v=sp.simplify(sp.expand(expr))
    CHECKS.append({'name':name,'passed':bool(v==0),'symbolic_remainder':str(v)})
def near(name,got,expected,tol=mp.mpf('1e-60'),scale=None):
    got=mp.mpf(got);expected=mp.mpf(expected)
    scale=max(mp.mpf(1),abs(got),abs(expected)) if scale is None else mp.mpf(scale)
    err=abs(got-expected)/scale
    CHECKS.append({'name':name,'passed':bool(err<=tol),'got':str(got),'expected':str(expected),
                   'normalization':str(scale),'normalized_error':str(err),'tolerance':str(tol)})
def truth(name,condition,detail=None):
    CHECKS.append({'name':name,'passed':bool(condition),'detail':detail})
def source_check():
    rows=[]
    for row in FREEZE['inputs']:
        path=Path(row['path']);actual=hashlib.sha256(path.read_bytes()).hexdigest()
        truth('frozen input '+str(path),actual==row['sha256'])
        rows.append({'path':str(path),'sha256':actual})
    raw=gzip.decompress((HERE/'primary_recovery/NIST_CODATA_2022.txt.gz').read_bytes())
    truth('exact full NIST recovery hash',hashlib.sha256(raw).hexdigest()==NIST['table_sha256'])
    lines=raw.decode().splitlines(keepends=True)
    for name,row in NIST['selected_rows'].items():
        truth('exact NIST row '+name,lines[row['line_number']-1]==row['raw_line'])
        cells=re.split(r'\s{2,}',row['raw_line'].strip())
        truth('NIST parsed value '+name,cells[0]==name and cells[1].replace(' ','')==row['value']
              and cells[2].replace(' ','')==row['uncertainty'])
    rad=json.loads(Path(INPUT['radiation_result']['path']).read_text())
    near('inherited photon calibration',number(INPUT['Omega_gamma']),
         number(str(rad['thermal']['thermal_rows'][1]['Omega_gamma'])))
    return rows
def symbolic():
    a,nu,Hv,ME,C,w,m,mu=sp.symbols('a nu Hv ME C w m mu',positive=True)
    u,x,y=sp.symbols('u x y',real=True)
    A=sp.exp(sp.sqrt(a)*u)
    rho=-m**4*(sp.log(m**2/mu**2)-sp.Rational(3,2))/(16*sp.pi**2)
    eps,L=sp.symbols('eps L',real=True)
    # Dimensionally regulated determinant, divided by m^4/(16 pi^2).
    finite=sp.limit(2*sp.exp(eps*(sp.EulerGamma+2*L))*sp.gamma(eps-2)-1/eps,eps,0)
    exact('Dirac determinant MS-bar finite coefficient',finite-(sp.Rational(3,2)+2*L))
    exact('free Dirac beta',sp.diff(rho,mu)*mu-m**4/(8*sp.pi**2))
    t=sp.symbols('mass_squared',positive=True)
    rho_t=-t*t*(sp.log(t/mu**2)-sp.Rational(3,2))/(16*sp.pi**2)
    exact('mass-squared derivative',sp.diff(rho_t,t)+t*(sp.log(t/mu**2)-1)/(8*sp.pi**2))
    for n in range(7):
        exact('covariant vacuum derivative '+str(n),sp.diff(C*A**4,u,n)-(4*sp.sqrt(a))**n*C*A**4)
    # Expand logarithm only on positive real masses/scales/A.
    r_fixed=-A**4*m**4*(2*sp.sqrt(a)*u+sp.log(m**2/mu**2)-sp.Rational(3,2))/(16*sp.pi**2)
    exact('fixed versus matched scale finite term',r_fixed-A**4*rho+A**4*m**4*sp.sqrt(a)*u/(8*sp.pi**2))
    R=sp.symbols('R',nonnegative=True)
    deltaV=3*Hv**2*R*A**4/2
    exact('old-origin canonical mass 24aR',sp.diff(deltaV,u,2).subs(u,0)/Hv**2-24*a*R)
    phi=sp.symbols('phi',real=True)
    Uphys=2*ME**2*C*sp.exp(4*sp.sqrt(a)*phi/(sp.sqrt(2)*ME))
    exact('canonical rather than unnormalized mass',sp.diff(Uphys,phi,2).subs(phi,0)-16*a*C)
    for n in [1,2]:
        exact('constant subtraction leaves derivative '+str(n),sp.diff(C*(A**4-1),u,n).subs(u,0)-C*(4*sp.sqrt(a))**n)
    f=a/2-sp.sqrt(a)*u+2*u*u
    V=Hv**2*(sp.Rational(3,2)+f*x*x+a*y*y/3+nu*u*u/2)+C*A**4
    exact('coercive f square',f-(2*(u-sp.sqrt(a)/4)**2+3*a/8))
    uv=-w/(4*sp.sqrt(a));cv=nu*Hv**2*w*sp.exp(w)/(16*a)
    sub={u:uv,x:0,y:0,C:cv}
    exact('shifted vacuum stationary',sp.diff(V,u).subs(sub))
    vmin=sp.simplify(V.subs(sub)/Hv**2)
    exact('shifted vacuum value',vmin-sp.Rational(3,2)-nu*(w*w+2*w)/(32*a))
    exact('shifted Einstein Hubble',2*vmin/3-1-nu*(w*w+2*w)/(48*a))
    for name,var,k,expected in [('u',u,1,nu*(1+w)),('x',x,4*a/9,sp.Rational(9,4)+9*w/(8*a)+9*w*w/(16*a*a)),('y',y,a/3,2)]:
        exact('shifted canonical mass '+name,sp.diff(V,var,2).subs(sub)/(k*Hv**2)-expected)
    for qi,qj in [(u,x),(u,y),(x,y)]:exact('vacuum mixed mass '+str(qi)+str(qj),sp.diff(V,qi,qj).subs(sub))
    # Arbitrary Hamiltonian gradients cancel; no special orbit imposed.
    HH,sm,sr,alpha=sp.symbols('H sigma rad alpha')
    vel=sp.symbols('v0:3');mom=sp.symbols('p0:3');grad=sp.symbols('g0:3')
    edot=sum(grad[i]*vel[i]+vel[i]*(-3*HH*mom[i]-grad[i]-(alpha*sm if i==0 else 0)) for i in range(3))+(-3*HH+alpha*vel[0])*sm-4*HH*sr
    exact('general Hamiltonian energy exchange',edot+3*HH*(sum(mom[i]*vel[i]for i in range(3))+sm+sp.Rational(4,3)*sr))
    tt=sp.symbols('t',real=True);scale=sp.Function('b')(tt);ss=sp.Function('s')(tt);zeta=sp.symbols('zeta')
    hh=sp.diff(scale,tt)/scale;re=6*(sp.diff(hh,tt)+2*hh**2)
    weight=sp.exp(2*ss)*scale**3
    original=zeta*weight*(re+6*sp.diff(ss,tt,2)+18*hh*sp.diff(ss,tt)+6*sp.diff(ss,tt)**2)/2
    integrated=zeta*weight*re/2-3*zeta*weight*sp.diff(ss,tt)**2
    boundary=3*zeta*weight*sp.diff(ss,tt)
    exact('Jordan curvature explicit total derivative',original-integrated-sp.diff(boundary,tt))
    return {'determinant_finite_normalized':str(finite),'V_min_over_Hv2':str(vmin),
            'scope':'Symbolic identities for supplied action and prescription, not empirical confirmation.'}
def calibration():
    rows=NIST['selected_rows'];const={k:number(v['value'])for k,v in rows.items()}
    c=const['speed of light in vacuum'];h=const['Planck constant'];hb=h/(2*mp.pi)
    mass=const['electron mass'];dm=number(rows['electron mass']['uncertainty'])
    G=const['Newtonian constant of gravitation'];dG=number(rows['Newtonian constant of gravitation']['uncertainty'])
    hzero=number(INPUT['H0_km_per_s_Mpc'])*1000/number(INPUT['Mpc_m'])
    omega=number(INPUT['Omega_gamma']);matter=number(INPUT['matter_fraction'])
    hv=hzero*mp.sqrt(1-matter-omega)
    energy=mass*c*c
    # The second tabulated quantity is a correlated rounding cross-check.
    near('CODATA mass-energy rounding only',energy,const['electron mass energy equivalent'],tol=mp.mpf('5e-25'),scale=1)
    loop=lambda mm:3*(mm*c*c)**4/(32*mp.pi**2*(hb*c)**3)
    rho=loop(mass)
    near('loop relative mass uncertainty derivative',mp.diff(loop,mass)*dm/rho,4*dm/mass)
    scales=[]
    for astr in INPUT['a_values']:
        aa=number(astr)
        me2=(1+aa)*hb*c**5/(8*mp.pi*G)
        target=3*me2*(hb*hv)**2/(hb*c)**3
        si=3*(1+aa)*c*c*hv*hv/(8*mp.pi*G)
        near('SI target two forms a='+astr,target,si)
        RR=rho/target
        near('mass-ratio dimensionless conversion a='+astr,RR,
             3*(energy**4)/(32*mp.pi**2)/(3*me2*(hb*hv)**2))
        g_rows=[]
        for sg in [-1,1]:
            gg=G+sg*dG
            om=omega*gg/G  # photons kept fixed; critical density changes with G.
            hh=hzero*mp.sqrt(1-matter-om)
            rr=rho/(3*(1+aa)*c*c*hh*hh/(8*mp.pi*gg))
            g_rows.append({'sigma_shift':sg,'G_N':str(gg),'Omega_gamma_correlated':str(om),'R':str(rr)})
        scales.append({'a':astr,'M_E_energy_squared_J2':str(me2),'rho_target_J_per_m3':str(target),
                       'R_electron_mu_equals_m':str(RR),'old_origin_delta_mass_squared_over_Hv2':str(24*aa*RR),
                       'G_uncertainty_endpoints':g_rows})
        physical_U=lambda phi:rho*(hb*c)**3*mp.exp(4*mp.sqrt(aa)*phi/mp.sqrt(2*me2))
        mass_from_canonical_energy=mp.diff(physical_U,0,2)/(hb*hv)**2
        near('serialized calibrated canonical mass '+astr,
             number(scales[-1]['old_origin_delta_mass_squared_over_Hv2']),mass_from_canonical_energy)
    return {'hbar_Js':str(hb),'H0_s_inverse':str(hzero),'Hv_s_inverse':str(hv),
            'electron_energy_J':str(energy),'rho_electron_loop_J_per_m3':str(rho),
            'electron_mass_relative_sigma':str(dm/mass),'loop_mass_relative_linear_sigma':str(4*dm/mass),
            'loop_mass_endpoints':[{'sigma_shift':sg,'rho_J_per_m3':str(loop(mass+sg*dm))}for sg in [-1,1]],
            'G_uncertainty_scope':'Separate endpoints, with Omega_gamma rescaled by G/G0 at fixed photons. No combined Gaussian model or independent likelihood.',
            'a_rows':scales}
def scheme_and_operator():
    ans=[];mm=mp.mpf('1.7')
    beta=mm**4/(8*mp.pi**2)
    loop=lambda m,mu:-m**4*(mp.log(m*m/(mu*mu))-mp.mpf('1.5'))/(16*mp.pi**2)
    base=loop(mm,mm);ref=mp.mpf('0.002')
    for a0 in INPUT['a_values']:
        aa=number(a0);alpha=mp.sqrt(aa)
        for u0 in INPUT['u_values']:
            uu=number(u0);A=mp.exp(alpha*uu)
            for l0 in INPUT['log_mu_over_m']:
                ell=number(l0);mu=mm*mp.exp(ell)
                matched=loop(A*mm,A*mu);pulled=A**4*loop(mm,mu)
                fixed=loop(A*mm,mu);matchterm=A**4*mm**4*mp.log(A)/(8*mp.pi**2)
                near('matched scale '+a0+','+u0+','+l0,matched,pulled)
                near('fixed scale plus local match '+a0+','+u0+','+l0,fixed+matchterm,pulled)
                ct=ref-base-beta*ell
                near('running total '+a0+','+u0+','+l0,loop(mm,mu)+ct,ref)
                ans.append({'a':a0,'u':u0,'log_mu_over_m':l0,'loop_J':str(loop(mm,mu)),
                            'matched_E':str(matched),'fixed_E':str(fixed),'finite_matching_term':str(matchterm),
                            'total_J':str(loop(mm,mu)+ct)})
            C=mp.mpf('2.3')
            for n in range(7):
                actual=mp.diff(lambda zz:C*mp.exp(4*alpha*zz),uu,n)
                near('numeric operator derivative '+a0+','+u0+',n='+str(n),actual,C*A**4*(4*alpha)**n)
                near('whole-operator cancellation '+a0+','+u0+',n='+str(n),
                     mp.diff(lambda zz:C*mp.exp(4*alpha*zz)-C*mp.exp(4*alpha*zz),uu,n),0)
            for n in [1,2]:
                near('constant-only subtraction derivative '+a0+','+u0+',n='+str(n),
                     mp.diff(lambda zz:C*(mp.exp(4*alpha*zz)-1),uu,n),C*A**4*(4*alpha)**n)
    near('scheme with zero finite loop is not zero running',loop(mm,mm*mp.exp(mp.mpf('-.75'))),0)
    return ans
def positive_vacua(cal):
    rows=[];electrons={q['a']:number(q['R_electron_mu_equals_m'])for q in cal['a_rows']}
    for astr in INPUT['a_values']:
        aa=number(astr);alpha=mp.sqrt(aa)
        for nstr in INPUT['nu_values']:
            nn=number(nstr)
            for rstr in INPUT['residual_ratios']:
                rr=electrons[astr] if rstr.startswith('electron')else number(rstr)
                C=mp.mpf('1.5')*rr;z=24*aa*rr/nn
                ww=mp.lambertw(z).real
                if z==0:bis=mp.mpf(0)
                else:
                    lo=mp.mpf(0);hi=mp.log1p(z)
                    for _ in range(360):
                        mid=(lo+hi)/2
                        if mid*mp.exp(mid)>z:hi=mid
                        else:lo=mid
                    bis=(lo+hi)/2
                tag=astr+','+nstr+','+rstr
                near('W versus monotone bisection '+tag,ww,bis,tol=mp.mpf('1e-55'))
                uv=-ww/(4*alpha);av=mp.exp(-ww/4)
                def pot(u,x,y):
                    return mp.mpf('1.5')+(aa/2-alpha*u+2*u*u)*x*x+aa*y*y/3+nn*u*u/2+C*mp.exp(4*alpha*u)
                vv=pot(uv,0,0);mx=mp.diff(lambda x:pot(uv,x,0),0,2)/(4*aa/9)
                my=mp.diff(lambda y:pot(uv,0,y),0,2)/(aa/3)
                mu=mp.diff(lambda u:pot(u,0,0),uv,2)
                grad=mp.diff(lambda u:pot(u,0,0),uv)
                near('vacuum force '+tag,grad,0,scale=max(1,nn*abs(uv)))
                near('vacuum value '+tag,vv,mp.mpf('1.5')+nn*(ww*ww+2*ww)/(32*aa))
                near('vacuum u mass '+tag,mu,nn*(1+ww))
                near('vacuum x mass '+tag,mx,mp.mpf('2.25')+9*ww/(8*aa)+9*ww*ww/(16*aa*aa))
                near('vacuum y mass '+tag,my,2)
                hh=mp.sqrt(2*vv/3)
                near('vacuum Hubble '+tag,hh*hh,1+nn*(ww*ww+2*ww)/(48*aa))
                near('vacuum A '+tag,mp.exp(alpha*uv),av)
                truth('positive mass and floor '+tag,mu>0 and mx>0 and my>0 and vv>=mp.mpf('1.5'))
                # Derivative and value away from the stationary point, without solving a trajectory.
                for delta in [-1,1]:
                    shifted=uv+delta/alpha
                    truth('unique u minimum side '+tag+','+str(delta),
                          pot(shifted,0,0)>vv and delta*mp.diff(lambda u:pot(u,0,0),shifted)>0)
                rows.append({'a':astr,'nu':nstr,'residual_label':rstr,'R':str(rr),'w':str(ww),
                             'u_v':str(uv),'A_v':str(av),'V_min_over_Hv2':str(vv),
                             'H_E_over_Hv':str(hh),'H_J_over_Hv':str(hh/av),
                             'tensor_G_ratio':str(av*av),'Jordan_Ricci_coefficient_ratio':str(1/(av*av)),
                             'mass_squared_over_Hv2':[str(mu),str(mx),str(my)]})
                # Action coefficient from the solved scalar, independent of stored A_v.
                ricci_from_action=mp.exp(-2*alpha*uv)
                near('serialized tensor-G from inverse action '+tag,number(rows[-1]['tensor_G_ratio']),1/ricci_from_action)
                near('serialized Ricci coefficient from action '+tag,number(rows[-1]['Jordan_Ricci_coefficient_ratio']),ricci_from_action)
                near('serialized tensor/Ricci reciprocity '+tag,number(rows[-1]['tensor_G_ratio'])*number(rows[-1]['Jordan_Ricci_coefficient_ratio']),1)
    return rows
def curvature_control():
    # Explicit finite-domain check includes the surface term; zeta=1 here.
    s=lambda t:mp.mpf('.1')*t*t-mp.mpf('.03')*t**3
    sd=lambda t:mp.mpf('.2')*t-mp.mpf('.09')*t*t
    sdd=lambda t:mp.mpf('.2')-mp.mpf('.18')*t
    H=mp.mpf('.7');re=12*H*H
    weight=lambda t:mp.exp(2*s(t)+3*H*t)
    old=lambda t:weight(t)*(re+6*sdd(t)+18*H*sd(t)+6*sd(t)**2)/2
    new=lambda t:weight(t)*re/2-3*weight(t)*sd(t)**2
    boundary=lambda t:3*weight(t)*sd(t)
    diff=mp.quad(lambda t:old(t)-new(t),[0,1]);surface=boundary(1)-boundary(0)
    near('induced-curvature integral with boundary',diff,surface)
    return {'original_minus_integrated_bulk':str(diff),'surface_term':str(surface),'zeta_value':'1, dimensionless check only; no electron-induced zeta inferred'}
def main():
    result={'started_at':stamp(),'source_hashes':source_check(),
            'scope':'Free matter-only Jordan-covariant MS-bar diagnostic and classical positive-residual response. No independent observation test.'}
    result['symbolic']=symbolic();print('symbolic finished',flush=True)
    result['calibration']=calibration();print('calibration finished',flush=True)
    result['scheme_operator']=scheme_and_operator();print('scheme/operator finished',flush=True)
    result['positive_vacua']=positive_vacua(result['calibration']);print('positive vacua finished',flush=True)
    result['curvature']=curvature_control()
    names=[q['name']for q in CHECKS]
    truth('unique assertion names',len(names)==len(set(names)))
    result['checks']=CHECKS;result['checks_passed']=sum(q['passed']for q in CHECKS)
    result['checks_failed']=sum(not q['passed']for q in CHECKS)
    result['versions']={'python':sys.version,'sympy':sp.__version__,'mpmath':mp.__version__}
    result['ended_at']=stamp()
    with (OUT/'RESULTS.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'passed':result['checks_passed'],'failed':result['checks_failed'],
                      'failed_checks':[q for q in CHECKS if not q['passed']],
                      'electron_loop_J_per_m3':result['calibration']['rho_electron_loop_J_per_m3'],
                      'a_rows':result['calibration']['a_rows']},indent=2))
    return bool(result['checks_failed'])
if __name__=='__main__':sys.exit(main())
