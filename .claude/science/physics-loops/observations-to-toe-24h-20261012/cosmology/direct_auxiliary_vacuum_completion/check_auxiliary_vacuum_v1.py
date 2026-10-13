#!/usr/local/bin/python3
"""Parent-authored controls for the explicit auxiliary action; no data fit."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import platform
import sys

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
mp.mp.dps = 90
ROWS = []


def check(name, passed, **details):
    ROWS.append(dict(name=name, passed=bool(passed), **details))


def exact(name, lhs, rhs=0):
    remainder = sp.simplify(lhs-rhs)
    check(name, remainder == 0, remainder=str(remainder))


def number(value):
    if isinstance(value, str) and '/' in value:
        n, d = value.split('/')
        return mp.mpf(n)/mp.mpf(d)
    return mp.mpf(value)


def fmt(value):
    return mp.nstr(value, 75)


def close(name, actual, expected, tol='1e-55'):
    error = abs(actual-expected)/max(mp.mpf(1), abs(expected))
    check(name, error <= mp.mpf(tol), actual=fmt(actual),
          expected=fmt(expected), normalized_error=fmt(error), tolerance=tol)


def symbolic_controls():
    q, lam, rho, delta, L0, avol, ff, fh, mu, MM = sp.symbols(
        'q Lambda rho delta L0 A4volume F Fhat mu M', real=True)
    lag = q*L0-(lam+rho)*avol+lam*ff/mu**4+q*q*fh/(2*MM**4)
    exact('action.Lambda_variation', sp.diff(lag, lam), -avol+ff/mu**4)
    exact('action.q_variation', sp.diff(lag, q), L0+q*fh/MM**4)
    exact('action.constant_translation',
          lag.subs({rho:rho+delta, lam:lam-delta}, simultaneous=True)-lag,
          -delta*ff/mu**4)
    exact('action.form_multiplier_Lambda_derivative', sp.diff(lam/mu**4,lam), 1/mu**4)
    exact('action.form_multiplier_q_derivative', sp.diff(q*q/(2*MM**4),q), q/MM**4)
    tau=sp.symbols('tau', real=True)
    exact('action.nonconstant_shift_obstruction',
          sp.diff(lam-sp.sin(tau),tau),-sp.cos(tau))
    Q,V,Tex,A4,R,lt,B,bV,bT = sp.symbols('Q V Tex A4 R Lambda_tilde B barV barT')
    trace_R = 2*Q+8*V-Tex/q+4*lt*A4/q
    exact('trace.L0_elimination', q*(R/2-Q-2*V).subs(R,trace_R),
          2*q*V-Tex/2+2*lt*A4)
    exact('trace.integrated_flux_solution',
          (q*B-2*q*bV+bT/2)/2, q*B/2-q*bV+bT/4)
    a,s,r,Hv = sp.symbols('a sigma radiation Hv', positive=True)
    hs=Hv**2+sp.Rational(2,3)*(1+a)*(s+r)
    hd=-(1+a)*(s+sp.Rational(4,3)*r)
    T=a*(s+sp.Rational(4,3)*r)
    vv=sp.Rational(3,2)*Hv**2+a*s/2+a*r/3
    Ltrack=3*(hd+2*hs)+T-2*vv
    exact('tracking.curvature_L0',Ltrack,3*Hv**2+(1+a)*s+2*a*r/3)
    exact('tracking.trace_L0',2*vv+s,Ltrack)
    # The stationary equations are derived from the full three-field potential.
    nu,u,x,y,C,t=sp.symbols('nu u x y C t', real=True)
    D=1+sp.Rational(2,3)*(1+a)*(x*x+y*y)
    KK=sp.diag(1,4*a/(9*D),a/(3*D))
    pot=Hv**2*(sp.Rational(3,2)+(a/2-sp.sqrt(a)*u+2*u*u)*x*x+
               a*y*y/3+nu*u*u/2)+C*sp.exp(4*sp.sqrt(a)*u)
    Cv=-nu*Hv**2*t*sp.exp(-4*t)/(4*a)
    vac={u:t/sp.sqrt(a),x:0,y:0,C:Cv}
    for field in (u,x,y):
        exact('vacuum.full_gradient_'+str(field),sp.diff(pot,field).subs(vac))
    mass=KK.inv()*sp.hessian(pot,(u,x,y))
    wanted=[nu*(1-4*t),sp.Rational(9,4)-9*t/(2*a)+9*t*t/(a*a),sp.Integer(2)]
    for i in range(3):
        exact('vacuum.canonical_mass_'+str(i),mass[i,i].subs(vac)/Hv**2,wanted[i])
    he2=2*pot.subs(vac)/(3*Hv**2)
    exact('vacuum.HE_squared',he2,1+(nu/a)*(t*t/3-t/6))
    bare=pot.subs(C,0).subs({u:t/sp.sqrt(a),x:0,y:0})
    bfun=(2*bare*sp.exp(-4*t)+4*Cv)/Hv**2
    exact('vacuum.flux_elimination',bfun,(3+(nu/a)*(t*t-t))*sp.exp(-4*t))
    tp=-a/(nu+12*a)
    exact('flux_response.implicit_t_slope',1/sp.diff(bfun,t).subs(t,0),tp)
    exact('flux_response.C_slope',sp.diff(Cv/Hv**2,t).subs(t,0)*tp,
          nu/(4*(nu+12*a)))
    # Differentiate H_J squared first to avoid symbolic square-root branches.
    hj2=he2*sp.exp(-2*t)
    exact('flux_response.physical_H_slope',sp.diff(hj2,t).subs(t,0)*tp/2,sp.Rational(1,12))
    exact('flux_response.tensor_G_slope',sp.diff(sp.exp(2*t),t).subs(t,0)*tp,
          -2*a/(nu+12*a))
    exact('vacuum.extrema_polynomial',sp.diff(bfun,t)*sp.exp(4*t),
          (nu/a)*(-4*t*t+6*t-1)-12)


def constant_shift_controls(protocol):
    out=[]
    # Exact rational coefficients plus a nonpolynomial A test cancellations
    # beyond a mere equality of the potential at the old field origin.
    rho=mp.mpf(7)/13; lam=-rho+mp.mpf(2)/9; q=mp.mpf(7)
    for av in protocol['parameter_grid']['a']:
        aa=number(av)
        for uv in ['-2','0','3']:
            u=number(uv); A4=mp.exp(4*mp.sqrt(aa)*u)
            for dv in protocol['parameter_grid']['vacuum_shifts']:
                delta=number(dv)
                before=lam+rho
                after=(lam-delta)+(rho+delta)
                key=f'shift.a{av}.u{uv}.delta{dv}'
                close(key+'.local_residual',after,before,'1e-48')
                for n in range(3):
                    close(key+f'.operator_derivative_{n}',
                          after*A4*(4*mp.sqrt(aa))**n/(2*q),
                          before*A4*(4*mp.sqrt(aa))**n/(2*q),'1e-48')
                if delta:
                    fixed_lambda=(lam+rho+delta)*A4/(2*q)
                    close(key+'.fixed_Lambda_contrast',
                          fixed_lambda-before*A4/(2*q),delta*A4/(2*q),'1e-48')
                out.append(dict(a=av,u=uv,delta=dv,local_residual_before=fmt(before),
                                local_residual_after=fmt(after)))
    return out


def flux_integrals(protocol, inputs):
    m=number(inputs['matter_fraction']); om=number(inputs['Omega_gamma'])
    vacuum=1-m-om; Bm=m/vacuum; Br=om/vacuum
    N0=-mp.log(number(inputs['initial_scale_inverse']))
    base=[]
    # Dimensionless H_v=1. Scale out exp(3 N_end), preserving ratios.
    for end in protocol['parameter_grid']['future_N']:
        nn=number(end)
        breaks=[N0]
        while breaks[-1]+2<nn:breaks.append(breaks[-1]+2)
        breaks.append(nn)
        H=lambda n:mp.sqrt(1+Bm*mp.exp(-3*n)+Br*mp.exp(-4*n))
        denN=mp.quadgl(lambda n:mp.exp(3*(n-nn))/H(n),breaks)
        dustN=mp.quadgl(lambda n:mp.exp(-3*nn)/H(n),breaks)
        radN=mp.quadgl(lambda n:mp.exp(-n-3*nn)/H(n),breaks)
        bscaled=Bm*mp.exp(-3*nn); rscaled=Br*mp.exp(-4*nn)
        zbreaks=[mp.exp(n-nn) for n in breaks]
        root=lambda z:mp.sqrt(z**4+bscaled*z+rscaled)
        denZ=mp.quadts(lambda z:z**4/root(z),zbreaks)
        dustZ=mp.quadts(lambda z:mp.exp(-3*nn)*z/root(z),zbreaks)
        radZ=mp.quadts(lambda z:mp.exp(-4*nn)/root(z),zbreaks)
        # Compare ratios to retain sensitivity to very small scaled integrals.
        close(f'volume.N{end}.den_quadrature_ratio',denN/denZ,mp.mpf(1),'1e-60')
        close(f'volume.N{end}.dust_quadrature_ratio',dustN/dustZ,mp.mpf(1),'1e-60')
        close(f'volume.N{end}.radiation_quadrature_ratio',radN/radZ,mp.mpf(1),'1e-60')
        base.append((end,denN,dustN,radN,denZ,dustZ,radZ))
    out=[]
    for av in protocol['parameter_grid']['a']:
        aa=number(av); s0=3*m/(2*(1+aa)*vacuum); r0=3*om/(2*(1+aa)*vacuum)
        previous=None
        for end,den,di,ri,den2,di2,ri2 in base:
            I_L=3*den+(1+aa)*s0*di+2*aa*r0*ri/3
            B=I_L/den
            B2=3+((1+aa)*s0*di2+2*aa*r0*ri2/3)/den2
            key=f'flux.a{av}.N{end}'
            close(key+'.independent_ratio',B,B2,'1e-60')
            check(key+'.finite_boundary_exceeds_future',B>3,
                  finite_minus_future=fmt(B-3))
            if previous is not None:
                check(key+'.approaches_future',B-3<previous-3)
            previous=B
            q=mp.mpf(7); mu=mp.mpf(3); MM=mp.mpf(5)
            cF=mu**4*den; chat=-MM**4*I_L/q
            close(key+'.signed_flux_relation',-q*mu**4/MM**4*chat/cF,B)
            # Reconstruct the integrated trace from separately weighted V/T.
            barV=(mp.mpf('1.5')*den+aa*s0*di/2+aa*r0*ri/3)/den
            barT=-2*q*s0*di/den
            close(key+'.zero_residual_trace',q*B/2-q*barV+barT/4,mp.mpf(0))
            if end==20:check(key+'.late_limit',0<B-3<mp.mpf('1e-22'))
            out.append(dict(a=av,N_end=end,B_over_Hv_squared=fmt(B),
                            finite_minus_future=fmt(B-3),scaled_volume=fmt(den),
                            scaled_dust_integral=fmt(di),scaled_radiation_integral=fmt(ri),
                            weighted_V=fmt(barV),weighted_T_over_q=fmt(barT/q)))
    return out


def bisect(fun,lo,hi,steps=360):
    flo=fun(lo); fhi=fun(hi)
    if flo==0:return lo
    if fhi==0:return hi
    if flo*fhi>0:raise ValueError('unbracketed root')
    for _ in range(steps):
        mid=(lo+hi)/2; fm=fun(mid)
        if flo*fm<=0:hi=mid
        else:lo=mid; flo=fm
    return (lo+hi)/2


def stationary_data(aa,nn,t):
    cc=-nn*t*mp.exp(-4*t)/(4*aa)
    u=t/mp.sqrt(aa)
    def pot(uu,xx,yy):
        return (mp.mpf('1.5')+(aa/2-mp.sqrt(aa)*uu+2*uu**2)*xx**2+
                aa*yy**2/3+nn*uu**2/2+cc*mp.exp(4*mp.sqrt(aa)*uu))
    vp=pot(u,0,0); HE=mp.sqrt(2*vp/3); A=mp.exp(t)
    mass=[]
    for j,k in enumerate([mp.mpf(1),4*aa/9,aa/3]):
        def displaced(z):
            p=[u,mp.mpf(0),mp.mpf(0)];p[j]+=z/mp.sqrt(2*k)
            return 2*pot(*p)
        mass.append(mp.diff(displaced,0,2))
    return dict(u=u,C=cc,V=vp,HE=HE,A=A,HJ=HE/A,GT=A*A,masses=mass,
                scalar_force=mp.diff(lambda z:pot(z,0,0),u),
                direct_flux=(6*HE**2-2*(mp.mpf('1.5')+nn*u*u/2))/A**4)


def vacuum_controls(protocol):
    vacua=[]; sensitivity=[]
    for av in protocol['parameter_grid']['a']:
        aa=number(av)
        for nv in protocol['parameter_grid']['nu']:
            nn=number(nv); ell=nn/aa
            b=lambda t:(3+ell*(t*t-t))*mp.exp(-4*t)
            roots=[mp.mpf(0)]
            # Independent monotonic intervals classify all additional t>1 roots.
            if ell>mp.mpf(48)/5:
                tmax=(3+mp.sqrt(5-48/ell))/4
                if tmax>1 and b(tmax)>3:
                    roots.append(bisect(lambda t:b(t)-3,mp.mpf(1),tmax))
                    hi=2*tmax
                    while b(hi)>3:hi*=2
                    roots.append(bisect(lambda t:b(t)-3,tmax,hi))
            for k,t in enumerate(roots):
                d=stationary_data(aa,nn,t);key=f'vacuum.a{av}.nu{nv}.root{k}'
                close(key+'.flux_constraint',b(t),mp.mpf(3),'1e-65')
                close(key+'.flux_from_curvature',d['direct_flux'],mp.mpf(3),'1e-65')
                close(key+'.stationary_force',d['scalar_force'],mp.mpf(0),'1e-65')
                expected=[nn*(1-4*t),mp.mpf(9)/4-9*t/(2*aa)+9*t*t/(aa*aa),mp.mpf(2)]
                for j in range(3):close(key+f'.canonical_mass_{j}',d['masses'][j],expected[j],'1e-65')
                close(key+'.physical_H',d['HJ'],mp.sqrt(1+ell*(t*t/3-t/6))*mp.exp(-t),'1e-65')
                close(key+'.tensor_G',d['GT'],mp.exp(2*t),'1e-65')
                check(key+'.specified_Hessian_class',
                      all(z>0 for z in d['masses']) if k==0 else t>1 and d['masses'][0]<0)
                vacua.append(dict(a=av,nu=nv,t=fmt(t),C_over_Hv_squared=fmt(d['C']),
                                  HJ_over_Hv=fmt(d['HJ']),tensor_G_ratio=fmt(d['GT']),
                                  canonical_masses=[fmt(z) for z in d['masses']]))
            # Sampled signs supplement, but do not replace, the analytic interval proof.
            for t in map(number,['-5','-1','-0.0001','0.0001','0.2','0.8','1']):
                check(f'vacuum.interval_sign.a{av}.nu{nv}.t{t}', b(t)>3 if t<0 else b(t)<3)
            for ev in protocol['parameter_grid']['epsilon']:
                ee=number(ev); target=3+ee
                tb=bisect(lambda t:b(t)-target,-mp.mpf('.01'),mp.mpf('.01'))
                # Solve u and C directly from the scalar equation and curvature flux,
                # not through the eliminated b(t), to compare the solution.
                def equations(uu,cc):
                    A4=mp.exp(4*mp.sqrt(aa)*uu)
                    Vbare=mp.mpf('1.5')+nn*uu*uu/2
                    return nn*uu+4*mp.sqrt(aa)*cc*A4,2*Vbare/A4+4*cc-target
                ud,cd=mp.findroot(equations,(mp.mpf(0),mp.mpf(0)),tol=mp.mpf('1e-75'))
                d=stationary_data(aa,nn,tb);key=f'sensitivity.a{av}.nu{nv}.eps{ev}'
                close(key+'.direct_two_equation_root',mp.sqrt(aa)*ud,tb,'1e-65')
                close(key+'.direct_C',cd,d['C'],'1e-65')
                close(key+'.direct_flux',d['direct_flux'],target,'1e-65')
                # Freeze a conservative finite-epsilon O(epsilon) slope tolerance.
                slopes=[tb/ee,d['C']/ee,(d['HJ']-1)/ee,(d['GT']-1)/ee]
                expected=[-aa/(nn+12*aa),nn/(4*(nn+12*aa)),mp.mpf(1)/12,-2*aa/(nn+12*aa)]
                for j in range(4):
                    close(key+f'.linear_slope_{j}',slopes[j],expected[j],str(2*abs(ee)))
                sensitivity.append(dict(a=av,nu=nv,epsilon=ev,t=fmt(tb),C=fmt(d['C']),
                                        HJ_over_Hv=fmt(d['HJ']),tensor_G_ratio=fmt(d['GT']),
                                        measured_secant_slopes=[fmt(z) for z in slopes],
                                        derivative_at_zero=[fmt(z) for z in expected]))
            # A derivative control at zero is distinct from finite-epsilon secants.
            bp=mp.diff(b,0)
            close(f'sensitivity.a{av}.nu{nv}.implicit_slope',1/bp,-aa/(nn+12*aa),'1e-65')
    return vacua,sensitivity


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-json',required=True)
    parser.add_argument('--freeze',required=True);args=parser.parse_args()
    output=Path(args.output_json)
    if output.exists():raise FileExistsError(output)
    protocol=json.loads((HERE/'PROTOCOL_v1.json').read_text())
    inputs=json.loads((HERE/'NUMERICAL_INPUTS_v1.json').read_text())
    frozen=json.loads(Path(args.freeze).read_text());source_hashes={}
    for item in frozen['inputs']:
        path=Path(item['path']);actual=hashlib.sha256(path.read_bytes()).hexdigest()
        source_hashes[str(path)]=actual
        check('source.'+str(path),actual==item['sha256'])
    symbolic_controls()
    shifts=constant_shift_controls(protocol)
    fluxes=flux_integrals(protocol,inputs)
    vacua,sensitivity=vacuum_controls(protocol)
    names=[r['name'] for r in ROWS]
    check('metadata.unique_assertion_names',len(names)==len(set(names)))
    result=dict(schema='parent_auxiliary_vacuum_controls_v1',created_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                interpretation='Internal checks of an explicit candidate action with supplied scales and flux boundary conditions; no data fit or independent observation test.',
                counts=dict(passed=sum(r['passed'] for r in ROWS),failed=sum(not r['passed'] for r in ROWS),total=len(ROWS)),
                source_hashes=source_hashes,checks=ROWS,constant_shifts=shifts,finite_fluxes=fluxes,
                constrained_vacua=vacua,flux_sensitivity=sensitivity,
                versions=dict(python=platform.python_version(),mpmath=mp.__version__,sympy=sp.__version__),mpmath_digits=mp.mp.dps)
    with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result['counts']))
    return 0 if not result['counts']['failed'] else 1


if __name__=='__main__':sys.exit(main())
