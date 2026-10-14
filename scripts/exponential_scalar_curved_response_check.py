#!/usr/bin/env python3
"""Conditional curved-response and exterior-energy controls. No observed data."""
from fractions import Fraction as F
import hashlib
import json
import math
import sys
import sympy as s
import mpmath as mp
from scipy.integrate import solve_ivp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_CURVED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-14.md",
)

def check_response():
    mp.mp.dps = 100
    checks = []
    details = {}

    def record(name, ok, value=None):
        checks.append({'name': name, 'pass': bool(ok), 'value': value})

    def exact(name, expr):
        z = s.simplify(expr)
        record(name, z == 0, str(z))

    def mpr(q):
        q = F(q)
        return mp.mpf(q.numerator) / q.denominator

    def fmt(q):
        return mp.nstr(q, 45)

    def fraction_pair(q):
        return [str(q.numerator), str(q.denominator)]

    x, B = s.symbols('x B', positive=True)
    psi = s.Function('psi')(x)
    y = psi/x
    leg = (1-x*x)*s.diff(psi,x,2)-2*x*s.diff(psi,x)+(2-B)*psi
    rad = s.diff(x*x*(1-x*x)*s.diff(y,x),x)/(x*x)-B*y
    exact('radial_operator_to_Legendre', x*rad-leg)
    exact('B2_elementary_solution', leg.subs({s.diff(psi,x,2):0,s.diff(psi,x):0,psi:1,B:2}))
    y0 = 1/x-s.atanh(x)
    exact('massless_Coulomb_flux', x*x*(1-x*x)*s.diff(y0,x)+1)
    record('massless_Coulomb_is_horizon_singular', s.limit(y0,x,1,dir='-') == -s.oo)
    record('massless_regular_solution_has_zero_source', s.diff(x,x)==1 and (x).subs(x,0)==0)

    n, N, A, v = s.symbols('n N A v', positive=True)
    an, an1 = s.symbols('an an1')
    # Coefficients from 2v P_vv-v^2 P_vv+2P_v-2vP_v-A P=0.
    exact('horizon_recurrence', (2*(n+1)**2*an1-(n*(n+1)+A)*an).subs(an1,(n*(n+1)+A)*an/(2*(n+1)**2)))
    b1 = s.symbols('b1')
    poly = 1+b1*x+(B-2)*x*x/2+B*b1*x**3/6+(B+4)*(B-2)*x**4/24
    lp = (1-x*x)*s.diff(poly,x,2)-2*x*s.diff(poly,x)+(2-B)*poly
    for power in range(3):
        exact('center_recurrence_power_'+str(power),s.expand(lp).coeff(x,power))
    Dpoly = 1-(B-2)*x*x/2-B*b1*x**3/3-(B+4)*(B-2)*x**4/8
    exact('scalar_gradient_series', poly-x*s.diff(poly,x)-Dpoly)
    exact('center_regular_V_series', s.expand((1-x*x)*s.diff(1+B*x*x/6+B*(B+10)*x**4/120,x,2)+(2/x-4*x)*s.diff(1+B*x*x/6+B*(B+10)*x**4/120,x)-B*(1+B*x*x/6+B*(B+10)*x**4/120)).coeff(x,2))

    # Derive the physical-radius metric without importing the target acceleration.
    R,H,m,k,eps,a0,a1 = s.symbols('R H m k eps a0 a1', positive=True)
    f=1-H*H*R*R
    r=R*(1-eps*a0)
    hin=s.series(1-H*H*r*r-2*eps*m/r,eps,0,2).removeO()
    FJ=s.series((1+2*eps*a0)*hin,eps,0,2).removeO()
    GJ=s.series(hin*(1+2*eps*R*a1),eps,0,2).removeO()
    exact('physical_areal_lapse', FJ-(f+eps*(-2*m/R+2*a0)))
    exact('physical_areal_radial_metric', GJ-(f+eps*(-2*m/R+2*H*H*R*R*a0+2*f*R*a1)))
    dF=-2*H*H*R+eps*(2*m/(R*R)+2*a1)
    # Algebraic derivative at eps=0 avoids a branch expansion of sqrt(f).
    dacc = s.diff(s.sqrt(GJ)*dF/(2*FJ),eps).subs(eps,0)
    P,D=s.symbols('P D', real=True)
    dacc=s.simplify(dacc.subs({a0:-k*m*P/R,a1:k*m*D/R**2}))
    target=m/R**2*((1-2*H*H*R*R)+k*(f*f*D-H*H*R*R*(1+f)*P))/f**s.Rational(3,2)
    exact('proper_holding_acceleration_same_physical_R', dacc-target)
    exact('circular_frequency', s.expand(R*dF/2).subs({eps:1,a1:k*m*D/R**2})-(-H*H*R*R+m/R*(1+k*D)))
    fc=1-x*x
    Enorm=(fc*fc*Dpoly-x*x*(1+fc)*poly)/(1-2*x*x)
    exact('holding_excess_center_series', s.series(Enorm,x,0,3).removeO()-(1-(B/2+1)*x*x))
    gfun=1-H*H*R*R-2*m/R
    exact('Einstein_tt_vacuum', (R*s.diff(gfun,R)+gfun-1)/R**2+3*H*H)
    exact('Einstein_angular_vacuum', s.diff(gfun,R)/R+s.diff(gfun,R,2)/2+3*H*H)

    uu=s.Function('u')(x); ww=s.Function('w')(x)
    p=x*x*(1-x*x)
    Wr=p*(uu*s.diff(ww,x)-s.diff(uu,x)*ww)
    Wdiff=s.diff(Wr,x).subs({s.diff(uu,x,2):(B*x*x*uu-s.diff(p,x)*s.diff(uu,x))/p,
                              s.diff(ww,x,2):(B*x*x*ww-s.diff(p,x)*s.diff(ww,x))/p})
    exact('weighted_Wronskian_constant', Wdiff)

    # Nonvacuous damaged-expression probes.
    bad_leg=(1-x*x)*s.diff(psi,x,2)-2*x*s.diff(psi,x)-B*psi
    record('damage_missing_curvature_2_detected', s.simplify(x*rad-bad_leg)==2*psi)
    record('damage_holding_equals_scalar_gradient_detected', s.simplify(s.series(Enorm-Dpoly,x,0,3).removeO())==-2*x*x)
    wrongF=s.series((1+2*eps*a0)*(f-2*eps*m/R),eps,0,2).removeO()
    record('damage_missing_areal_radius_shift_detected', s.simplify((FJ-wrongF).coeff(eps))==2*H*H*R*R*a0)
    flatV=s.sinh(s.sqrt(B)*x)/(s.sqrt(B)*x)
    flatVres=(1-x*x)*s.diff(flatV,x,2)+(2/x-4*x)*s.diff(flatV,x)-B*flatV
    record('damage_flat_body_kernel_detected', s.simplify(s.series(flatVres,x,0,3).removeO())==-s.Rational(5,3)*B*x*x)

    def coefficients(bb, count):
        out=[F(1)]
        for j in range(count):
            out.append(out[-1]*(j*(j+1)+bb-2)/F(2*(j+1)**2))
        return out

    def P_interval(bb, vv, terms=256):
        aa=coefficients(bb,terms+1)
        val=sum((aa[j]*vv**j for j in range(terms+1)),F(0))
        der=sum((j*aa[j]*vv**(j-1) for j in range(1,terms+1)),F(0))
        r0=vv/F(2)*(1+(bb-2)/F((terms+2)**2))
        r1=vv/F(2)*(1+(bb-2)/F((terms+1)*(terms+2)))
        if not (0<=r0<1 and 0<=r1<1):
            raise ValueError('tail ratios must be below one')
        tv=aa[terms+1]*vv**(terms+1)/(1-r0)
        td=(terms+1)*aa[terms+1]*vv**terms/(1-r1)
        return (val,val+tv),(der,der+td)

    def kernels_interval(bb,xx):
        pp,pd=P_interval(bb,1-xx)
        zz,_=P_interval(bb,F(1))
        ps=(pp[0]/zz[1],pp[1]/zz[0])
        dd=((pp[0]+xx*pd[0])/zz[1],(pp[1]+xx*pd[1])/zz[0])
        ff=1-xx*xx
        ee=((ff*ff*dd[0]-xx*xx*(1+ff)*ps[1])/(1-2*xx*xx),
            (ff*ff*dd[1]-xx*xx*(1+ff)*ps[0])/(1-2*xx*xx))
        return ps,dd,ee

    def sqrt_interval(bb,bits=96):
        ni=math.isqrt(bb.numerator); di=math.isqrt(bb.denominator)
        if ni*ni==bb.numerator and di*di==bb.denominator:
            return F(ni,di),F(ni,di)
        den=2**bits
        lo=math.isqrt(bb.numerator*den*den//bb.denominator)
        assert F(lo,den)**2<=bb<F(lo+1,den)**2
        return F(lo,den),F(lo+1,den)

    def exp_minus_interval(tt,terms=128):
        term=F(1); val=term
        for j in range(1,terms+1):
            term*=tt/F(j); val+=term
        nxt=term*tt/F(terms+1); ratio=tt/F(terms+2)
        assert 0<=ratio<1
        return 1/(val+nxt/(1-ratio)),1/val

    def flat_interval(bb,xx):
        bl,bh=sqrt_interval(bb)
        tl,th=bl*xx,bh*xx
        # F(t) is decreasing for t>=0; use endpoint exponential enclosures.
        el=exp_minus_interval(th)[0]; eh=exp_minus_interval(tl)[1]
        return (1+th)*el,(1+tl)*eh

    def psi_mp(bb,xx):
        ll=-mp.mpf('.5')+mp.sqrt(mp.mpf('2.25')-bb)
        return mp.re(mp.legenp(ll,0,xx)/mp.legenp(ll,0,0))

    def V_mp(bb,xx):
        rad=mp.sqrt(9-4*bb)
        return mp.re(mp.hyp2f1((3+rad)/4,(3-rad)/4,mp.mpf('1.5'),xx*xx))

    fixed=[(F(16),F(1,100)),(F(16),F(1,10)),(F(16),F(1,4)),(F(16),F(1,2)),
           (F(64),F(1,8)),(F(256),F(1,16)),(F(1600),F(1,40)),
           (4*(4+3*F(1,100000))/(1-3*F(1,100000)),F(1,4))]
    certificates=[]; comparisons=[]
    for i,(bb,xx) in enumerate(fixed):
        ps,dd,ee=kernels_interval(bb,xx); ff=flat_interval(bb,xx)
        db=(dd[0]/ff[1]-1,dd[1]/ff[0]-1)
        eb=(ee[0]/ff[1]-1,ee[1]/ff[0]-1)
        cert={'B':str(bb),'x':str(xx),'terms':256,'sqrt_bits':96,'exp_terms':128}
        for key,iv in [('psi',ps),('D',dd),('holding_relative_tensor',ee),('flat',ff),('D_relative_flat',db),('holding_relative_flat',eb)]:
            cert[key]=[fraction_pair(q) for q in iv]
            record(f'exact_interval_order_{i}_{key}',iv[0]<=iv[1])
            record(f'exact_interval_width_{i}_{key}',iv[1]-iv[0]<F(1,10**25))
        mm,zz=mpr(bb),mpr(xx)
        pp=psi_mp(mm,zz); dp=mp.diff(lambda t:psi_mp(mm,t),zz)
        dv=pp-zz*dp; fv=(1+mp.sqrt(mm)*zz)*mp.exp(-mp.sqrt(mm)*zz)
        ef=((1-zz*zz)**2*dv-zz*zz*(2-zz*zz)*pp)/(1-2*zz*zz)
        for key,actual,iv in [('psi',pp,ps),('D',dv,dd),('holding',ef,ee),('flat',fv,ff)]:
            if key == 'flat':
                # Exact exponential enclosures are as narrow as 1e-398. A 100-digit
                # floating value cannot test membership; recompute only this comparison.
                with mp.workdps(500):
                    tt = mp.sqrt(mpr(bb))*mpr(xx)
                    flat_precise = (1+tt)*mp.exp(-tt)
                    inside = mpr(iv[0]) <= flat_precise <= mpr(iv[1])
            else:
                inside = mpr(iv[0]) <= actual <= mpr(iv[1])
            record(f'special_function_inside_rational_certificate_{i}_{key}',inside)
        comparisons.append({'B':str(bb),'x':str(xx),'psi':fmt(pp),'D':fmt(dv),'flat':fmt(fv),'holding_relative_tensor':fmt(ef),'D_relative_flat':fmt(dv/fv-1),'holding_relative_flat':fmt(ef/fv-1)})
        certificates.append(cert)
    details['comparison_points']=comparisons
    certificate_bytes=(json.dumps(certificates,indent=2)+'\n').encode()

    # Distinct ODE integration; not a claim of independent authorship.
    ode_records=[]
    for bb in [16,64,256,1600]:
        hh=1e-6; aa=coefficients(F(bb),9)
        init=[sum(float(aa[j])*hh**j for j in range(9)),
              -sum(j*float(aa[j])*hh**(j-1) for j in range(1,9))]
        sol=solve_ivp(lambda zz,yy:[yy[1],(2*zz*yy[1]+(bb-2)*yy[0])/(1-zz*zz)],
                      (1-hh,0),init,method='DOP853',rtol=5e-12,atol=1e-13,dense_output=True)
        norm=sol.y[0,-1]; errs=[]
        for xx in [.02,.1,.25,.5,.8]:
            val,der=sol.sol(xx)/norm
            expected=psi_mp(mp.mpf(bb),mp.mpf(str(xx)))
            dex=expected-mp.mpf(str(xx))*mp.diff(lambda t:psi_mp(mp.mpf(bb),t),mp.mpf(str(xx)))
            errs += [float(abs(mp.mpf(val)/expected-1)),float(abs(mp.mpf(val-xx*der)/dex-1))]
        record(f'ODE_horizon_to_center_{bb}',sol.success and max(errs)<2e-9,{'max_relative_error':max(errs),'nfev':sol.nfev})
        ode_records.append({'B':bb,'success':bool(sol.success),'nfev':sol.nfev,'max_relative_error':max(errs),'message':sol.message})
    details['ODE']=ode_records

    flux=[]; wr=[]; bodies=[]
    for bb in [mp.mpf(2),mp.mpf(16),mp.mpf(64)]:
        pfun=lambda tt:psi_mp(bb,tt)
        fi=bb*mp.quad(lambda tt:tt*pfun(tt),[0,mp.mpf('.2'),mp.mpf('.6'),1])
        record('flux_normalization_'+str(bb),abs(fi-1)<mp.mpf('1e-80'),fmt(fi-1))
        flux.append({'B':str(bb),'residual':fmt(fi-1)})
        for xx in [mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.7')]:
            vf=lambda zz:V_mp(bb,zz); yf=lambda zz:pfun(zz)/zz
            wv=xx*xx*(1-xx*xx)*(vf(xx)*mp.diff(yf,xx)-mp.diff(vf,xx)*yf(xx))
            record('Wronskian_'+str(bb)+'_'+str(xx),abs(wv+1)<mp.mpf('1e-80'),fmt(wv+1))
            wr.append({'B':str(bb),'x':str(xx),'residual':fmt(wv+1)})
        rs=mp.mpf('.2')
        body=3/rs**3*mp.quad(lambda tt:tt*tt*V_mp(bb,tt),[0,rs])
        record('body_charge_bounds_'+str(bb),1<=body<=V_mp(bb,rs))
        bodies.append({'B':str(bb),'radius_x':str(rs),'uniform_charge':fmt(body),'upper_bound':fmt(V_mp(bb,rs))})
    details.update({'flux':flux,'Wronskian':wr,'body':bodies})

    # Compare the full conformal-coordinate acceleration with its analytic linear coefficient.
    # Solve R=(1+a(r))r; use exact A=1+a here as a mathematical first-order control.
    acc_records=[]
    for xx in [mp.mpf('.1'),mp.mpf('.25'),mp.mpf('.5')]:
        kk=mp.mpf('.02'); bb=mp.mpf(16); RR=xx
        pp=psi_mp(bb,xx); DD=pp-xx*mp.diff(lambda t:psi_mp(bb,t),xx); ff=1-xx*xx
        expect=((1-2*xx*xx)+kk*(ff*ff*DD-xx*xx*(1+ff)*pp))/(RR*RR*ff**mp.mpf('1.5'))
        errs=[]
        for mass in [mp.mpf('1e-10'),mp.mpf('1e-12'),mp.mpf('1e-14')]:
            af=lambda rr:-kk*mass*psi_mp(bb,rr)/rr
            rr=mp.findroot(lambda rr:(1+af(rr))*rr-RR,(RR,RR+mass))
            h=1-rr*rr-2*mass/rr; hp=-2*rr+2*mass/rr**2
            hold=mp.sqrt(h)/(1+af(rr))*(hp/(2*h)+mp.diff(af,rr)/(1+af(rr)))
            bg=-RR/mp.sqrt(1-RR*RR)
            err=abs((hold-bg)/mass-expect)/max(1,abs(expect)); errs.append(err)
        record('full_metric_linear_coefficient_'+str(xx),errs[2]<mp.mpf('1e-11') and errs[1]<errs[0]/50 and errs[2]<errs[1]/50,[fmt(q) for q in errs])
        acc_records.append({'x':str(xx),'relative_errors':[fmt(q) for q in errs]})
    details['full_metric_linear_checks']=acc_records

    # Direct differentiation of the supplied action at its vacuum.
    kk,nu,uu,EE=s.symbols('kk nu uu EE',positive=True)
    aa=(1-kk)*(1+3*kk)/4;ss=(1+kk)/(kk*(1-3*kk));alpha=s.sqrt(aa)
    Ef=s.exp(2*alpha*uu);Ff=1+ss*Ef;Jf=1+(1-3*aa)*ss*Ef
    Cf=(1+ss)*Ef/Ff;Kf=Jf/Ff**2
    Uf=s.Rational(3,2)+s.Rational(3,2)*ss*(Ef-1)**2/Ff**2+nu*(1+ss)*uu**2/(2*Ff**2)
    exact('action_vacuum_stationary',s.diff(Uf,uu).subs(uu,0))
    exact('action_vacuum_coupling',(s.diff(s.log(Cf)/2,uu)**2/Kf).subs(uu,0)-kk)
    exact('action_vacuum_mass',(s.diff(Uf,uu,2)/Kf).subs(uu,0)-4*(3*(1+kk)+nu)/(1-3*kk))
    exact('action_mass_above_twelve',4*(3*(1+kk)+nu)/(1-3*kk)-12-4*(12*kk+nu)/(1-3*kk))
    return {'checks':checks,'details':details,'rational_certificates_sha256':hashlib.sha256(certificate_bytes).hexdigest(),'rational_certificates_bytes':len(certificate_bytes)}


def check_energy():
    mp.mp.dps=80
    checks=[]; detail={}
    def rec(name,ok,value=None): checks.append({'name':name,'pass':bool(ok),'value':value})
    def exact(name,expr):
        zz=s.simplify(expr);rec(name,zz==0,str(zz))
    def fmt(q):return mp.nstr(q,40)

    x,t,B,J=s.symbols('x t B J',positive=True)
    f=1-x*x
    P=s.Function('P')(x,t)
    phi=P/x
    kg=-s.diff(phi,t,2)/f+s.diff(x*x*f*s.diff(phi,x),x)/(x*x)-B*phi-J*phi/(x*x)
    wave=-s.diff(P,t,2)+f*f*s.diff(P,x,2)+f*s.diff(f,x)*s.diff(P,x)-f*(B-2+J/(x*x))*P
    exact('full_radial_KG_to_tortoise_wave',x*f*kg-wave)
    rho=s.symbols('rho',positive=True)
    exact('tortoise_coordinate',s.diff(s.atanh(x),x)-1/f)
    V=(1-x*x)*(B-2+J/x**2)
    exact('potential_positive_factorization',V-(1-x)*(1+x)*(B-2+J/x**2))

    # Covariant stress/slice calculation, leaving all factors visible.
    qdot,qgrad,massfield=s.symbols('qdot qgrad massfield',real=True)
    Ttt=qdot*qdot-s.Rational(1,2)*(-f)*(-qdot*qdot/f+f*qgrad*qgrad+B*massfield*massfield)
    # n^t=1/sqrt(f), slice volume=x^2/sqrt(f) dx dOmega.
    E_density=s.simplify(Ttt*x*x/f)
    exact('Killing_energy_density_from_stress',E_density-x*x*(qdot*qdot/f+f*qgrad*qgrad+B*massfield*massfield)/2)

    P1=s.Function('P1')(x)
    ephi=(x*x*f*s.diff(P1/x,x)**2+B*P1**2)/2
    epsi=(f*s.diff(P1,x)**2+(B-2)*P1**2)/2
    exact('energy_boundary_term',ephi-epsi+s.diff(f*P1**2/(2*x),x))

    W=s.Function('W')(rho,t); VV=s.Function('V')(rho)
    ed=(s.diff(W,t)**2+s.diff(W,rho)**2+VV*W**2)/2
    flux=s.diff(W,t)*s.diff(W,rho)
    cons=s.diff(ed,t)-s.diff(flux,rho)
    exact('wave_local_energy_identity',cons.subs(s.diff(W,t,2),s.diff(W,rho,2)-VV*W))

    y=s.Function('y')(x); I=s.Function('I')(x); p=x*x*f
    q=s.simplify(y*I)
    qprime=s.diff(q,x).subs(s.diff(I,x),1/(p*y*y))
    Lq=s.diff(p*qprime,x)-B*x*x*q
    Lq=Lq.subs(s.diff(I,x),1/(p*y*y)).subs(s.diff(y,x,2),(B*x*x*y-s.diff(p,x)*s.diff(y,x))/p)
    exact('reduction_of_order_solution',Lq)
    exact('static_energy_as_boundary_term',(s.diff(p*y*s.diff(y,x),x)-(p*s.diff(y,x)**2+B*x*x*y*y)).subs(s.diff(y,x,2),(B*x*x*y-s.diff(p,x)*s.diff(y,x))/p))

    eps,qh=s.symbols('eps qh',positive=True)
    leading_gradient=1/(2*qh*eps)
    leading_energy=s.Rational(1,2)*(1-eps)**2*(1-(1-eps)**2)*leading_gradient**2
    exact('log_branch_energy_coefficient',s.limit(eps*leading_energy,eps,0)-1/(4*qh*qh))
    bad_energy=s.Rational(1,2)*(1-eps)**2*(1-(1-eps)**2)**2*leading_gradient**2
    rec('damage_extra_lapse_factor_detected',s.limit(eps*bad_energy,eps,0)==0)

    # A true counterexample outside positivity: B=-4, j=0 has a growing mode.
    w=s.tanh(rho)/s.cosh(rho)
    badV=-6/s.cosh(rho)**2
    exact('negative_potential_growing_mode',-s.diff(w,rho,2)+badV*w+w)
    rec('negative_potential_mode_regular_and_decaying',s.limit(w,rho,0)==0 and s.limit(w,rho,s.oo)==0)
    # Finite energy does not imply a static state, even at a positive candidate mass.
    pulse=rho*s.exp(-rho*rho)
    pulse_acc=s.diff(pulse,rho,2)-14/s.cosh(rho)**2*pulse
    rec('finite_energy_pulse_nonstatic',s.simplify(pulse_acc.subs(rho,1))!=0,str(s.simplify(pulse_acc.subs(rho,1))))
    rec('finite_energy_pulse_regular_decay',s.limit(pulse,rho,0)==0 and s.limit(pulse,rho,s.oo)==0)

    ll=-mp.mpf('.5')+mp.sqrt(mp.mpf('2.25')-16)
    Pmp=lambda xx:mp.re(mp.legenp(ll,0,xx)) # Horizon normalization P(1)=1.
    Y=lambda xx:Pmp(xx)/xx
    x0=mp.mpf('.5')
    regular_limit=-mp.mpf('.5')*x0*x0*(1-x0*x0)*Y(x0)*mp.diff(Y,x0)
    rows=[];previous=None
    for ee in [mp.mpf('1e-2'),mp.mpf('1e-4'),mp.mpf('1e-6'),mp.mpf('1e-8'),mp.mpf('1e-10'),mp.mpf('1e-12')]:
        xx=1-ee; pp=xx*xx*(1-xx*xx)
        integ=mp.quad(lambda zz:1/((1-zz*zz)*Pmp(zz)**2),[x0,xx])
        qval=Y(xx)*integ; qder=mp.diff(Y,xx)*integ+1/(pp*Y(xx))
        eq=pp*qval*qder/2
        er=pp*Y(xx)*mp.diff(Y,xx)/2+regular_limit
        coeff=ee*pp*qder*qder/2
        row={'epsilon':str(ee),'log_branch_energy':fmt(eq),'regular_energy':fmt(er),'regular_limit':fmt(regular_limit),'log_gradient_coefficient':fmt(coeff)}
        if previous:
            slope=(eq-previous[1])/mp.log(previous[0]/ee);row['energy_log_slope']=fmt(slope)
        rows.append(row); previous=(ee,eq)
    rec('logarithmic_divergence_coefficient_numeric',abs(coeff-mp.mpf('.25'))<mp.mpf('1e-8'),fmt(coeff))
    rec('logarithmic_integrated_slope_numeric',abs(slope-mp.mpf('.25'))<mp.mpf('1e-7'),fmt(slope))
    rec('regular_branch_finite_energy_numeric',abs(er/regular_limit-1)<mp.mpf('1e-9'),fmt(er/regular_limit-1))
    detail['cutoff_energy']=rows
    pf=lambda rr:rr*mp.exp(-rr*rr)
    PE=mp.quad(lambda rr:(mp.diff(pf,rr)**2+14/mp.cosh(rr)**2*pf(rr)**2)/2,[0,1,3,mp.inf])
    rec('finite_energy_nonstatic_pulse_numeric',mp.isfinite(PE) and PE>0,fmt(PE))
    detail['pulse_energy']=fmt(PE)
    return {'checks':checks,'details':detail}


def run_checks():
    if hasattr(sys,'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    response=check_response()
    energy=check_energy()
    checks=response['checks']+energy['checks']
    return {'scope':'Conditional static vacuum and exterior-energy mathematics; no observed data, fitted parameters or cosmological state selection.',
            'response':response,'energy':energy,
            'counts':{'passed':sum(q['pass'] for q in checks),'failed':sum(not q['pass'] for q in checks)}}

if __name__=='__main__':
    result=run_checks()
    print(json.dumps(result,indent=2))
    sys.exit(bool(result['counts']['failed']))
