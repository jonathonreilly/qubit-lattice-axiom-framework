#!/usr/bin/env python3
"""Actual completed scalar backgrounds, fixed imported weak-body bridge."""
from pathlib import Path
import argparse, hashlib, json
import mpmath as mp

HERE=Path(__file__).resolve().parent
IC=HERE.parent/'direct_thermal_matter_bridge'
WF=HERE.parent/'direct_weak_field_inverse'
CHECKS=[]


def check(name, good, **detail):
    CHECKS.append(dict(name=name,passed=bool(good),**detail))


def compare(name, got, expected, relative='1e-55', absolute='1e-65'):
    error=abs(got-expected); bound=max(mp.mpf(absolute),mp.mpf(relative)*abs(expected))
    check(name,error<=bound,error=mp.nstr(error,24),allowed=mp.nstr(bound,24))


def supplied_formula(u,a,s,k0):
    al=mp.sqrt(a);E=mp.exp(2*al*u);z=s*E;F=1+z;J=1+(1-3*a)*z
    kap=a/J;beta=-a*(1-3*a)*z*F/J**2
    dg=-2*kap/(1+kap);db=beta*kap/(2*(1+kap)**2)
    cb=(1+s)*E/F
    return dict(kappa=kap,beta_c=beta,delta_gamma=dg,delta_beta=db,
                eta=4*db-dg,GNratio=cb*(1+kap)/(1+k0),
                dlogG_du=2*al/F*(1+beta/(1+kap)),CB=cb,
                alpha_B=al/F,K_u=J/F**2)


def original_metric_oracle(u,a,s,k0):
    def raw(t):
        A=mp.exp(mp.sqrt(a)*t);F=1+s*A*A
        Fu=mp.diff(lambda r:1+s*mp.exp(2*mp.sqrt(a)*r),t)
        K=(1-3*a*s*A*A)/F+mp.mpf(3)/4*(Fu/F)**2
        return A/mp.sqrt(F),K
    def canonical(t):
        return mp.diff(lambda r:mp.log(raw(r)[0]),t)/mp.sqrt(raw(t)[1])
    alpha=canonical(u);kappa=alpha**2
    beta=mp.diff(canonical,u)/mp.sqrt(raw(u)[1])
    def grav(t):
        return (1+s)*raw(t)[0]**2*(1+canonical(t)**2)/(1+k0)
    dg=-2*alpha**2/(1+alpha**2)
    db=alpha**2*beta/(2*(1+alpha**2)**2)
    return dict(kappa=kappa,beta_c=beta,delta_gamma=dg,delta_beta=db,eta=4*db-dg,
                GNratio=grav(u),dlogG_du=mp.diff(lambda t:mp.log(grav(t)),u),
                CB=(1+s)*raw(u)[0]**2,alpha_B=mp.diff(lambda t:mp.log(raw(t)[0]),u),K_u=raw(u)[1])


def main(freeze,out):
    mp.mp.dps=80
    for x in json.loads(freeze.read_text())['inputs']:
        check('source.'+x['path'],hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
    observations=json.loads((WF/'OBSERVATION_INPUTS_v1.json').read_text())
    collection=json.loads((IC/'evidence_v3/histories/RESULTS.json').read_text())['histories']
    rows=[];ids=['split_k0.01','equal_k0.01','split_k1e-05','equal_k1e-05','split_k1e-06','equal_k1e-06']
    cv=lambda v:mp.mpf(str(v))
    for label in ['.01','1e-5','1e-6']:
        k=mp.mpf(label);a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k))
        form=supplied_formula(mp.mpf(0),a,s,k)
        compare('exact_family.'+label+'.kappa',form['kappa'],k)
        compare('exact_family.'+label+'.eta',form['eta'],mp.mpf(0))
        compare('exact_family.'+label+'.stationary_G',form['dlogG_du'],mp.mpf(0))
    for name in ids:
        item=next(x for x in collection if x['case']['id']==name)
        check(name+'.complete',item['success'] and len(item['rows'])==241)
        cfg=item['configuration'];a,s,k0=map(cv,[cfg['a'],cfg['s'],cfg['k']])
        end=item['rows'][-1];u,pu=map(cv,[end['state'][0],end['state'][3]])
        form=supplied_formula(u,a,s,k0);oracle=original_metric_oracle(u,a,s,k0)
        for key in form:compare(name+'.raw.'+key,form[key],oracle[key])
        compare(name+'.stored.GNratio',form['GNratio'],cv(end['GNratio']),'3e-12','3e-12')
        hv=mp.sqrt(cv(cfg['Hv2']));hj=hv*mp.sqrt(cv(end['HJ2']))
        nh=1+form['alpha_B']*pu
        compare(name+'.stored.NJprime',nh,cv(end['NJprime']),'3e-12','3e-12')
        compare(name+'.stored.Hratio',mp.sqrt(cv(end['HJ2'])/cv(end['HGR2'])),cv(end['Hratio']),'3e-12','3e-12')
        du_time=hj*pu/nh
        raw_time=pu*hv*mp.sqrt(cv(end['H2']))/mp.sqrt(form['CB'])
        compare(name+'.clock.du_dt',du_time,raw_time,'3e-12','1e-48')
        drift=form['dlogG_du']*du_time*mp.mpf('365.25')*86400
        direct_drift=oracle['dlogG_du']*raw_time*mp.mpf('365.25')*86400
        compare(name+'.clock.dotG_year',drift,direct_drift,'3e-12','1e-48')
        initial=supplied_formula(mp.mpf(0),a,s,k0)
        bands=[]
        for n in [1,2]:
            band={}
            for label,key in [('Cassini','delta_gamma'),('LLR','eta')]:
                center=cv(observations[label]['mean']);error=cv(observations[label]['reported_uncertainty'])
                lower=center-n*error;upper=center+n*error;inside=lower<=form[key]<=upper
                # A second interval-membership expression tests the output boundary.
                check(name+f'.band.{label}.{n}',inside==(abs(form[key]-center)<=n*error))
                band[label]=dict(inside=bool(inside),lower=mp.nstr(lower,25),upper=mp.nstr(upper,25),
                                 prediction=mp.nstr(form[key],25))
            bands.append(dict(reported_error_multiple=n,separate_intervals=band))
        rows.append(dict(case=name,endpoint_u=mp.nstr(u,25),endpoint_pu=mp.nstr(pu,25),
                         input_k=mp.nstr(k0,25),actual={k:mp.nstr(v,30) for k,v in form.items()},
                         frozen_zero_background_shortcut={k:mp.nstr(initial[k],30) for k in ['kappa','delta_gamma','eta','GNratio']},
                         physical_H_per_second=mp.nstr(hj,25),dotG_over_G_per_Julian_year=mp.nstr(drift,25),
                         separate_working_rectangles=bands,full_history_limit='Only equal_k0.01 independently reproduced; weak full-history refinements/reproductions remain incomplete.'))
    result=dict(scope='Conditional weak-body/long-range response on actual completed cosmological endpoints; exposed separate summaries, not joint likelihood or new holdout.',
                supplied_bridge=observations,rows=rows,checks=CHECKS,
                counts=dict(passed=sum(x['passed'] for x in CHECKS),failed=sum(not x['passed'] for x in CHECKS),total=len(CHECKS)))
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(counts=result['counts'],rows=rows)),flush=True)
    raise SystemExit(bool(result['counts']['failed']))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    main(args.freeze,args.out)
