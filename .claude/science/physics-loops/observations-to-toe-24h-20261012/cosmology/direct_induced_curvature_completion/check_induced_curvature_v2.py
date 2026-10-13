#!/usr/local/bin/python3
"""Direct author checks for a supplied Jordan-Ricci completion, not a data fit."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import platform
import sys
import mpmath as mp
import sympy as sp

HERE=Path(__file__).resolve().parent
mp.mp.dps=90
CHECKS=[]

def number(x):
    if isinstance(x,str) and '/' in x:
        a,b=x.split('/');return mp.mpf(a)/mp.mpf(b)
    return mp.mpf(x)

def fmt(x):return mp.nstr(x,75)

def check(name,passed,**details):
    CHECKS.append(dict(name=name,passed=bool(passed),**details))

def close(name,actual,expected,tol='1e-55'):
    err=abs(actual-expected)/max(mp.mpf(1),abs(expected))
    check(name,err<=number(tol),actual=fmt(actual),expected=fmt(expected),
          normalized_error=fmt(err),tolerance=tol)

def exact(name,actual,expected=0):
    err=sp.factor(sp.simplify(actual-expected))
    check(name,err==0,remainder=str(err))

def symbolic_controls():
    a,q,z=sp.symbols('a q z',positive=True)
    F=q*(1+z);d=q*z;J=1+(1-3*a)*z
    metric=(q-3*a*d)/F+sp.Rational(3,4)*(2*sp.sqrt(a)*d/F)**2
    exact('weyl.kinetic',metric,J/(1+z)**2)
    exact('weyl.coupling', (sp.sqrt(a)/(1+z))**2/metric,a/J)
    Q,du,V,L,T,boxF=sp.symbols('Q du_squared V Lambda_tilde T boxF')
    QZ=q*Q-3*a*d*du
    R=(2*QZ+8*q*V+4*L*sp.Symbol('A4')-T+3*boxF)/F
    expected=(-q*d*Q/F-3*q*a*d*du/F+2*q*(q-d)*V/F+
              2*q*L*sp.Symbol('A4')/F-q*T/(2*F)+3*q*boxF/(2*F))
    exact('trace.full_L0',q*(R/2-Q-2*V),expected)
    # Vary the original q, Lambda action before changing conformal frame.
    lam,rho,delta,L0,A4vol,ff,fh,mu,MM,ricciJ,zeta=sp.symbols(
        'Lambda rho delta L0 A4vol F4 Fhat4 mu M RicciJ zeta')
    action=q*L0-(lam+rho)*A4vol+lam*ff/mu**4+q*q*fh/(2*MM**4)+zeta*ricciJ/2
    exact('forms.q_unchanged',sp.diff(action,q),L0+q*fh/MM**4)
    exact('forms.Lambda_unchanged',sp.diff(action,lam),-A4vol+ff/mu**4)
    exact('forms.constant_shift',action.subs({rho:rho+delta,lam:lam-delta},simultaneous=True)-action,-delta*ff/mu**4)
    t,c,s,ell=sp.symbols('t c s ell',real=True)
    zz=s*sp.exp(2*t);vv=sp.Rational(3,2)+ell*t*t/2
    cp=(zz*vv-ell*t*(1+zz)/4)*sp.exp(-4*t)
    f=(vv+c*sp.exp(4*t))/(1+zz)**2
    exact('stationary.Einstein_gradient',sp.diff(f,t).subs(c,cp))
    hg2=2*(vv+cp*sp.exp(4*t))/(3*(1+zz))
    hg_expected=1+ell*(t*t/3-t/6)
    exact('stationary.original_H_squared',hg2,hg_expected)
    b=(6*hg2-2*vv)*sp.exp(-4*t)
    b_expected=(3+ell*(t*t-t))*sp.exp(-4*t)
    exact('stationary.flux',b,b_expected)
    numerator=ell*(1-4*t)+zz*(ell*(1-6*t)+8*vv)
    exact('stationary.u_Hessian',sp.diff(f,t,2).subs(c,cp),numerator/(1+zz)**3)
    x,y=sp.symbols('x y',real=True)
    D=1+sp.Rational(2,3)*(1+a)*(x*x+y*y)
    full=(vv+(a/2-t+2*t*t/a)*x*x+a*y*y/3+c*sp.exp(4*t))/(1+zz)**2
    mx=(sp.diff(full,x,2)/(4*a/(9*D*(1+zz)))).subs({x:0,y:0})
    my=(sp.diff(full,y,2)/(a/(3*D*(1+zz)))).subs({x:0,y:0})
    exact('stationary.x_Hessian',mx,(sp.Rational(9,4)-9*t/(2*a)+9*t*t/(a*a))/(1+zz))
    exact('stationary.y_Hessian',my,2/(1+zz))
    te=-1/(ell+12)
    exact('response.t',1/sp.diff(b_expected,t).subs(t,0),te)
    exact('response.C',sp.diff(cp,t).subs(t,0)*te,(ell*(1+s)+12*s)/(4*(ell+12)))
    exact('response.HJ',sp.diff(hg_expected*sp.exp(-2*t),t).subs(t,0)*te/2,sp.Rational(1,12))
    gt=sp.exp(2*t)/(1+zz)
    exact('response.GT',sp.diff(gt,t).subs(t,0)*te,-2/((ell+12)*(1+s)**2))
    force0=ell*t*(1+zz)-4*zz*vv
    exact('fixed_C.implicit_slope',(-sp.diff(force0,s)/sp.diff(force0,t)).subs({t:0,s:0}),6/ell)
    exact('origin.residual',cp.subs(t,0),3*s/2)
    exact('origin.physical_u_mass',
          (a*numerator/(1+(1-3*a)*zz)).subs(t,0),
          a*(ell*(1+s)+12*s)/(1+(1-3*a)*s))
    # Positive-s end: substitute w=exp(-2t) and retain explicit log terms.
    w,ss=sp.symbols('w ss',positive=True)
    asym=(sp.Rational(3,2)+ell*sp.log(w)**2/8+c/w**2)/(1+ss/w)**2
    exact('asymptotic.potential',sp.limit(asym,w,0,dir='+'),c/ss**2)
    ku=(1+(1-3*a)*ss/w)/(1+ss/w)**2
    exact('asymptotic.kinetic_scaled',sp.limit(ku/w,w,0,dir='+'),(1-3*a)/ss)

def kinetic_controls(protocol):
    rows=[]
    for av in protocol['parameter_grid']['a']:
        aa=number(av)
        for sv in protocol['parameter_grid']['s']:
            ss=number(sv)
            for tv in protocol['parameter_grid']['t']:
                t=number(tv);z=ss*mp.exp(2*t);F=1+z;J=1+(1-3*aa)*z
                key=f'kinetic.a{av}.s{sv}.t{tv}'
                predicted=(F>0 and (z<0 or aa<=mp.mpf(1)/3 or z<1/(3*aa-1)))
                direct=(1-3*aa*z)/F+mp.mpf(3)/4*(2*mp.sqrt(aa)*z/F)**2
                close(key+'.transformed_u',direct,J/F**2)
                eig=[direct,4*aa/(9*F),aa/(3*F)]
                check(key+'.positive_domain',all(v>0 for v in eig)==predicted)
                # Differentiate the physical matter factor rather than its reduced slope.
                u=t/mp.sqrt(aa)
                def logB(uu):
                    return mp.sqrt(aa)*uu-mp.log(1+ss*mp.exp(2*mp.sqrt(aa)*uu))/2
                eff=None
                if predicted:
                    eff=mp.diff(logB,u)**2/direct
                    close(key+'.matter_coupling',eff,aa/J)
                rows.append(dict(a=av,s=sv,t=tv,F_over_q=fmt(F),J=fmt(J),
                                 positive_kinetic_domain=predicted,
                                 transformed_kinetic=[fmt(v) for v in eig],
                                 scalar_coupling_norm=fmt(eff) if eff is not None else None))
        if aa>mp.mpf(1)/3:
            boundary=1/(3*aa-1)
            close(f'kinetic.a{av}.degenerate_J',1+(1-3*aa)*boundary,mp.mpf(0),'1e-65')
    return rows

def bisect(fn,lo,hi):
    flo=fn(lo)
    if flo*fn(hi)>0:raise ValueError('root not bracketed')
    for _ in range(360):
        mid=(lo+hi)/2;fm=fn(mid)
        if fm*flo<=0:hi=mid
        else:lo=mid;flo=fm
    return (lo+hi)/2

def boundary_roots(ell,tcrit,ellcrit):
    if ell<ellcrit:return [mp.mpf(0)]
    if ell==ellcrit:raise ValueError('degenerate root outside supplied grid')
    ll=lambda t:3*mp.expm1(4*t)/(t*(t-1))
    small=bisect(lambda t:ll(t)-ell,mp.mpf(1)+mp.mpf('1e-40'),tcrit)
    hi=2*tcrit
    while ll(hi)<ell:hi*=2
    big=bisect(lambda t:ll(t)-ell,tcrit,hi)
    return [mp.mpf(0),small,big]

def vacuum_data(aa,nn,ss,t):
    ell=nn/aa;z=ss*mp.exp(2*t);F=1+z;J=1+(1-3*aa)*z
    bare=mp.mpf('1.5')+ell*t*t/2
    cc=(z*bare-ell*t*F/4)*mp.exp(-4*t)
    return z,F,J,bare,cc

def full_potential(aa,nn,ss,cc,u,x,y):
    A=mp.exp(mp.sqrt(aa)*u)
    bare=(mp.mpf('1.5')+(aa/2-mp.sqrt(aa)*u+2*u*u)*x*x+
          aa*y*y/3+nn*u*u/2)
    return (bare+cc*A**4)/(1+ss*A*A)**2

def hessian_class(av,nv,sv,t,u_mass):
    if t==0:
        # These supplied grid labels are rational. Preserve an exact zero;
        # numerical differentiation can leave a tiny signed roundoff residue.
        aa=sp.Rational(av);nn=sp.Rational(nv);ss=sp.Rational(sv)
        sign=int(sp.sign(nn*(1+ss)+12*aa*ss))
    else:
        sign=1 if u_mass>mp.mpf('1e-55') else -1 if u_mass<-mp.mpf('1e-55') else None
    return {1:'positive',-1:'negative_direction',0:'degenerate',None:'unresolved'}[sign]

def stationary_controls(protocol):
    vacua=[];census=[];sensitivity=[];fixed_C=[]
    g=lambda t:4*t*t-6*t+1+(2*t-1)*mp.exp(-4*t)
    tc=mp.findroot(g,(mp.mpf('1.2'),mp.mpf('1.4')))
    ec=3*mp.expm1(4*tc)/(tc*(tc-1))
    for av in protocol['parameter_grid']['a']:
        aa=number(av)
        for nv in protocol['parameter_grid']['nu']:
            nn=number(nv);ell=nn/aa
            roots=boundary_roots(ell,tc,ec)
            # Count separately using extrema of b(t).
            additional=False
            if ell>mp.mpf(48)/5:
                tm=(3+mp.sqrt(5-48/ell))/4
                additional=tm>1 and (3+ell*(tm*tm-tm))*mp.exp(-4*tm)>3
            check(f'census.a{av}.nu{nv}',len(roots)==(3 if additional else 1))
            census.append(dict(a=av,nu=nv,count=len(roots),t=[fmt(t) for t in roots]))
            for sv in protocol['parameter_grid']['s']:
                ss=number(sv)
                for k,t in enumerate(roots):
                    z,F,J,v,c=vacuum_data(aa,nn,ss,t);valid=F>0 and J>0
                    row=dict(a=av,nu=nv,s=sv,root=k,t=fmt(t),z=fmt(z),F_over_q=fmt(F),J=fmt(J),
                             C_over_Hv_squared=fmt(c),positive_kinetic_domain=valid)
                    key=f'vacuum.a{av}.nu{nv}.s{sv}.root{k}'
                    close(key+'.boundary',(3+ell*(t*t-t))*mp.exp(-4*t),mp.mpf(3),'1e-65')
                    if not valid:
                        row['disposition']='excluded by tensor/scalar kinetic domain'
                        vacua.append(row);continue
                    u=t/mp.sqrt(aa);A=mp.exp(t);B=A/mp.sqrt(F)
                    vh=full_potential(aa,nn,ss,c,u,0,0)
                    hh=mp.sqrt(2*vh/3);hj=hh/B
                    hg=hh*mp.sqrt(F)
                    close(key+'.metric_equation',12*hg*hg,8*(v+c*A**4)/F,'1e-65')
                    close(key+'.scalar_equation',ell*t+4*c*A**4-z*6*hg*hg,mp.mpf(0),'1e-65')
                    close(key+'.flux_from_metric',(6*hg*hg-2*v)/A**4,mp.mpf(3),'1e-65')
                    close(key+'.physical_H',hj,mp.sqrt(1+ell*(t*t/3-t/6))*mp.exp(-t),'1e-65')
                    close(key+'.tensor_G',B*B,A*A/F,'1e-65')
                    mass=[];kh=[J/F**2,4*aa/(9*F),aa/(3*F)]
                    expected=[(nn*(1-4*t)+z*(nn*(1-6*t)+8*aa*v))/(F*J),
                              (mp.mpf(9)/4-9*t/(2*aa)+9*t*t/(aa*aa))/F,2/F]
                    for j in range(3):
                        def potential_displaced(vv):
                            coords=[u,mp.mpf(0),mp.mpf(0)]
                            coords[j]+=vv/mp.sqrt(2*kh[j])
                            return 2*full_potential(aa,nn,ss,c,*coords)
                        force=mp.diff(potential_displaced,0)
                        mj=mp.diff(potential_displaced,0,2)
                        close(key+f'.gradient_{j}',force,mp.mpf(0),'1e-65')
                        close(key+f'.canonical_mass_{j}',mj,expected[j],'1e-65')
                        mass.append(mj)
                    classification=hessian_class(av,nv,sv,t,mass[0])
                    check(key+'.mass_classification_resolved',classification!='unresolved')
                    row.update(HJ_over_Hv=fmt(hj),Hhat_over_Hv=fmt(hh),tensor_G_ratio=fmt(B*B),
                               scalar_coupling_norm=fmt(aa/J),canonical_masses=[fmt(m) for m in mass],
                               physical_masses=[fmt(m/(B*B)) for m in mass],
                               local_Hessian_class=classification,
                               positive_local_Hessian=classification=='positive')
                    vacua.append(row)
            # Secant controls use a declared subset away from F=0, J=0.
            for sv in ['-0.1','0','0.1','1']:
                ss=number(sv)
                for ev in protocol['parameter_grid']['epsilon']:
                    ee=number(ev);bf=lambda t:(3+ell*(t*t-t))*mp.exp(-4*t)
                    t=bisect(lambda t:bf(t)-3-ee,-mp.mpf('.01'),mp.mpf('.01'))
                    z,F,J,v,c=vacuum_data(aa,nn,ss,t)
                    key=f'response.a{av}.nu{nv}.s{sv}.eps{ev}'
                    predicted=F>0 and (z<0 or aa<=mp.mpf(1)/3 or z<1/(3*aa-1))
                    check(key+'.domain_recorded',(F>0 and J>0)==predicted)
                    if F<=0 or J<=0:
                        sensitivity.append(dict(a=av,nu=nv,s=sv,epsilon=ev,
                                                disposition='outside kinetic domain'))
                        continue
                    H=mp.sqrt(1+ell*(t*t/3-t/6))*mp.exp(-t)
                    G=mp.exp(2*t)/F
                    observed=[t/ee,(c-3*ss/2)/ee,(H-1)/ee,(G-1/(1+ss))/ee]
                    expected=[-1/(ell+12),(ell*(1+ss)+12*ss)/(4*(ell+12)),
                              mp.mpf(1)/12,-2/((ell+12)*(1+ss)**2)]
                    for j in range(4):
                        close(key+f'.slope_{j}',observed[j],expected[j],str(2*abs(ee)))
                    sensitivity.append(dict(a=av,nu=nv,s=sv,epsilon=ev,t=fmt(t),C=fmt(c),
                                            HJ_over_Hv=fmt(H),tensor_G_ratio=fmt(G),
                                            secants=[fmt(x) for x in observed],
                                            zero_derivatives=[fmt(x) for x in expected]))
            for sv in ['-0.00000001','0.00000001']:
                ss=number(sv)
                f=lambda t:ell*t*(1+ss*mp.exp(2*t))-4*ss*mp.exp(2*t)*(mp.mpf('1.5')+ell*t*t/2)
                t=mp.findroot(f,6*ss/ell,tol=mp.mpf('1e-75'))
                key=f'fixed_C.a{av}.nu{nv}.s{sv}'
                close(key+'.stationary',f(t),mp.mpf(0),'1e-65')
                bound=200*(1+6/ell)**2*ss**2
                check(key+'.first_order_remainder',abs(t-6*ss/ell)<=bound,
                      error=fmt(abs(t-6*ss/ell)),bound=fmt(bound))
                check(key+'.origin_is_not_stationary',f(0)!=0)
                fixed_C.append(dict(a=av,nu=nv,s=sv,C='0',t=fmt(t),
                                    leading_t=fmt(6*ss/ell),remainder_bound=fmt(bound)))
    # Explicit witnesses are admitted grid rows, not hidden branch exclusions.
    changed=[r for r in vacua if r.get('positive_local_Hessian') and r['root']>0]
    negative=[r for r in vacua if r['positive_kinetic_domain'] and r.get('canonical_masses') and
              r.get('local_Hessian_class')=='negative_direction' and r['root']==0]
    zero=[r for r in vacua if r.get('local_Hessian_class')=='degenerate' and r['root']==0]
    check('witness.exists_second_positive_Hessian',bool(changed))
    check('witness.exists_positive_kinetic_negative_mass',bool(negative))
    return dict(root_census=census,vacua=vacua,flux_response=sensitivity,fixed_C=fixed_C,
                critical_t=fmt(tc),critical_ell=fmt(ec),second_positive_Hessian_count=len(changed),
                origin_negative_mass_count=len(negative),origin_zero_mass_count=len(zero))

def serialized_controls(protocol,stationary):
    rows=stationary['vacua'];expected_keys=set()
    for av in protocol['parameter_grid']['a']:
        for nv in protocol['parameter_grid']['nu']:
            ell=number(nv)/number(av);count=1
            if ell>mp.mpf(48)/5:
                tm=(3+mp.sqrt(5-48/ell))/4
                if tm>1 and (3+ell*(tm*tm-tm))*mp.exp(-4*tm)>3:count=3
            for sv in protocol['parameter_grid']['s']:
                for k in range(count):expected_keys.add((av,nv,sv,k))
                actual=[r for r in rows if (r['a'],r['nu'],r['s'])==(av,nv,sv)]
                check(f'serialized.census.a{av}.nu{nv}.s{sv}',len(actual)==count,
                      actual=len(actual),expected=count)
    keys=[(r['a'],r['nu'],r['s'],r['root']) for r in rows]
    check('serialized.census.all_including_excluded',set(keys)==expected_keys and len(keys)==len(expected_keys))
    negative=zero=positive_nonzero=0
    for i,r in enumerate(rows):
        aa=number(r['a']);nn=number(r['nu']);ss=number(r['s']);t=number(r['t'])
        z=ss*mp.exp(2*t);F=1+z;J=1+(1-3*aa)*z
        valid=F>0 and J>0;key=f'serialized.vacuum.{i}'
        close(key+'.z',number(r['z']),z,'1e-65')
        close(key+'.F',number(r['F_over_q']),F,'1e-65')
        close(key+'.J',number(r['J']),J,'1e-65')
        check(key+'.domain_flag',r['positive_kinetic_domain']==valid)
        if not valid:
            check(key+'.excluded_record',r.get('disposition')=='excluded by tensor/scalar kinetic domain' and
                  'canonical_masses' not in r and 'positive_local_Hessian' not in r)
            continue
        v=mp.mpf('1.5')+nn*t*t/(2*aa);cc=number(r['C_over_Hv_squared'])
        masses=[(nn*(1-4*t)+z*(nn*(1-6*t)+8*aa*v))/(F*J),
                (mp.mpf(9)/4-9*t/(2*aa)+9*t*t/(aa*aa))/F,2/F]
        expected_class=hessian_class(r['a'],r['nu'],r['s'],t,masses[0])
        check(key+'.class_resolved',expected_class!='unresolved')
        check(key+'.class_record',r['local_Hessian_class']==expected_class)
        check(key+'.Hessian_flag',r['positive_local_Hessian']==(expected_class=='positive'))
        if r['root']==0:
            negative+=expected_class=='negative_direction';zero+=expected_class=='degenerate'
            if expected_class=='degenerate':
                close(key+'.exact_zero_numeric_residue',number(r['canonical_masses'][0]),mp.mpf(0),'1e-65')
        else:positive_nonzero+=expected_class=='positive'
        factor=mp.exp(2*t)/F
        close(key+'.tensor_G',number(r['tensor_G_ratio']),factor,'1e-65')
        close(key+'.coupling',number(r['scalar_coupling_norm']),aa/J,'1e-65')
        close(key+'.C_from_scalar_equation',cc,(z*v-nn*t*F/(4*aa))*mp.exp(-4*t),'1e-65')
        for j in range(3):
            close(key+f'.canonical_mass_{j}',number(r['canonical_masses'][j]),masses[j],'1e-65')
            close(key+f'.physical_mass_{j}',number(r['physical_masses'][j]),masses[j]/factor,'1e-65')
        hhat=mp.sqrt(2*(v+cc*mp.exp(4*t))/(3*F**2))
        close(key+'.Hhat',number(r['Hhat_over_Hv']),hhat,'1e-65')
        close(key+'.physical_H',number(r['HJ_over_Hv']),hhat/mp.sqrt(factor),'1e-65')
    check('serialized.count.negative_origins',stationary['origin_negative_mass_count']==negative)
    check('serialized.count.zero_origins',stationary['origin_zero_mass_count']==zero)
    check('serialized.count.positive_nonzero',stationary['second_positive_Hessian_count']==positive_nonzero)

def main():
    p=argparse.ArgumentParser();p.add_argument('--freeze',required=True)
    p.add_argument('--output-json',required=True);args=p.parse_args()
    output=Path(args.output_json)
    if output.exists():raise FileExistsError(output)
    protocol=json.loads((HERE/'PROTOCOL_v1.json').read_text())
    frozen=json.loads(Path(args.freeze).read_text());identities={}
    for row in frozen['inputs']:
        path=Path(row['path']);actual=hashlib.sha256(path.read_bytes()).hexdigest()
        identities[str(path)]=actual
        check('source.'+str(path),actual==row['sha256'])
    symbolic_controls()
    kinetics=kinetic_controls(protocol)
    stationary=stationary_controls(protocol)
    serialized_controls(protocol,stationary)
    names=[r['name'] for r in CHECKS]
    check('metadata.unique_assertion_names',len(names)==len(set(names)))
    result=dict(schema='parent_induced_curvature_v2',created_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                interpretation='Supplied two-derivative candidate and synthetic controls; no measured Ricci coefficient, fit, independent observation test, or full constrained/global stability theorem.',
                counts=dict(passed=sum(r['passed'] for r in CHECKS),failed=sum(not r['passed'] for r in CHECKS),total=len(CHECKS)),
                checks=CHECKS,source_hashes=identities,kinetic_rows=kinetics,stationary=stationary,
                versions=dict(python=platform.python_version(),mpmath=mp.__version__,sympy=sp.__version__))
    with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result['counts']))
    return int(result['counts']['failed']>0)

if __name__=='__main__':sys.exit(main())
