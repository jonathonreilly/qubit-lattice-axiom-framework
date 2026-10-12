#!/usr/bin/env python3
"""Spherical source profiles for a positive gamma(s=1) mediator measure.

Read-only source use, single process, arbitrary precision for tiny rank effects.
Output is conditional theoretical response, not an experimental exclusion.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib,json,sys
from pathlib import Path

sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import joint_scalar as old
import mpmath as mp


def m(x):
    return mp.mpf(str(x))


def full(symbol):
    return mp.matrix([1,*map(m,old.charge(symbol))])


def compound(counts):
    return mp.matrix([1,*map(m,old.compound(counts))])


def dot(a,b):
    return (a.T*b)[0]


def kernel(ell,r,a):
    total=ell+r
    z=a/total
    p=ell/total if a==0 else ell/total*mp.atanh(z)/z
    f=p+ell*r/(total*total-a*a)
    return p,f


def layer(ell,r,R,lo,hi,fraction):
    return [fraction*mp.quad(lambda y:3*y*y*kernel(ell,r,R*y)[k], [lo,hi])/(hi**3-lo**3)
            for k in [0,1]]


def earth_rows(ell,r,freeze):
    R=m(freeze['Earth_radius_m']); c=m(freeze['Earth_core_radius_fraction'])
    weights_core=layer(ell,r,R,m(0),c,m('.32'))
    weights_mantle=layer(ell,r,R,c,m(1),m('.68'))
    fe=full('Fe'); mantle=compound({'Si':1,'O':2})
    rows=[weights_core[k]*fe+weights_mantle[k]*mantle for k in [0,1]]
    return rows,{'core_potential_weight':weights_core[0],
                 'mantle_potential_weight':weights_mantle[0],
                 'core_force_weight':weights_core[1],
                 'mantle_force_weight':weights_mantle[1],
                 'effective_force_core_fraction':weights_core[1]/(weights_core[1]+weights_mantle[1])}


def solar_nodes(path,R,residual):
    rows=[]
    for line in path.read_text().splitlines():
        words=line.split()
        if len(words)!=12:
            continue
        try:
            row=list(map(mp.mpf,words))
        except ValueError:
            continue
        rows.append(row)
    assert len(rows)>1000
    names=['H','He4','He3','C12','N14','O16']
    nodes=[]
    for row in rows:
        fractions=row[6:]
        q=mp.zeros(3,1)
        for name,fraction in zip(names,fractions):
            q+=fraction*full(name)
        remainder=1-sum(fractions)
        assert remainder>=0
        q+=remainder*full(residual)
        nodes.append((row[0],row[1]*R,q))
    # Same constant-composition missing end shells as the massless block;
    # source radii are anchored at 0 and the supplied full solar radius.
    nodes=[(m(0),m(0),nodes[0][2]),*nodes,(m(1),R,nodes[-1][2])]
    assert all(nodes[i+1][0]>=nodes[i][0] for i in range(len(nodes)-1))
    return nodes


def integrate_nodes(nodes,ell=None,r=None):
    rows=[mp.zeros(3,1),mp.zeros(3,1)]
    prev=None
    for mass,radius,q in nodes:
        factors=[m(1),m(1)] if ell is None else kernel(ell,r,radius)
        cur=[f*q for f in factors]
        if prev is not None:
            delta=mass-prev[0]
            for k in [0,1]:
                rows[k]+=delta*(prev[1][k]+cur[k])/2
        prev=(mass,cur)
    return rows


def normal(row):
    return row/row[0]


def cross(a,b):
    return mp.matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])


def null_x_one(a,b):
    out=cross(a,b)
    return out/out[1]


def serial(value):
    if isinstance(value,mp.matrix):
        if value.cols==1:
            return [mp.nstr(x,45) for x in value]
        return [[mp.nstr(value[i,j],45) for j in range(value.cols)] for i in range(value.rows)]
    if isinstance(value,mp.mpf):
        return mp.nstr(value,45)
    if isinstance(value,dict):
        return {key:serial(v) for key,v in value.items()}
    if isinstance(value,list):
        return list(map(serial,value))
    return value


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-dir',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--dps',type=int,default=80)
    args=p.parse_args()
    mp.mp.dps=args.dps
    runtime=args.source_dir.parent
    deadline=json.loads((runtime/'DEADLINE.json').read_text())
    assert datetime.now(timezone.utc).timestamp()<deadline['deadline_epoch']
    assert not any((runtime/s).exists() for s in ['STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED'])
    freeze_path=Path(__file__).with_name('MODEL_FREEZE.json')
    freeze=json.loads(freeze_path.read_text())
    old.checked_sources(args.source_dir)
    solar={}
    for file in freeze['Sun_profiles']:
        for remainder in freeze['Sun_residual_metals']:
            solar[file+'_'+remainder]=solar_nodes(args.source_dir/file,m(freeze['Sun_radius_m']),remainder)
    baseline='bs05op.dat_Fe'
    E0=m('.32')*full('Fe')+m('.68')*compound({'Si':1,'O':2})
    S0=integrate_nodes(solar[baseline])[1]
    old_results=json.loads((Path(__file__).resolve().parent.parent/'source_null_results.json').read_text())
    frozen_vector=m('.1')*mp.matrix(list(map(m,old_results['source_null_direction_x1'])))
    exact_massless=m('.1')*null_x_one(E0,S0)
    electron_vector=mp.matrix([-m('.1')*E0[1],m('.1'),0])
    delta_test=mp.matrix([0,*map(m,old.mix({'Ti':.90,'Al':.06,'V':.04})-old.mix({'Pt':.90,'Rh':.10}))])
    rs,ra=map(m,freeze['Earth_field_radii_m'])
    rSun=m(freeze['Sun_field_radius_m'])
    results=[]
    for ell_value in freeze['ell_m']:
        ell=m(ell_value)
        earth_surface,core_surface=earth_rows(ell,rs,freeze)
        earth_altitude,core_altitude=earth_rows(ell,ra,freeze)
        sun_rows={name:integrate_nodes(nodes,ell,rSun) for name,nodes in solar.items()}
        WF=[earth_surface[1],earth_altitude[1],sun_rows[baseline][1]]
        WP=[earth_surface[0],earth_altitude[0],sun_rows[baseline][0]]
        names=['Earth_surface','Earth_710km','Sun_1AU']
        fixed=[]
        for label,d in [('frozen_massless_double_null',frozen_vector),
                        ('precision_control_massless_double_null',exact_massless),
                        ('massless_Earth_null_electron',electron_vector)]:
            force={name:dot(row,d) for name,row in zip(names,WF)}
            potential={name:dot(row,d) for name,row in zip(names,WP)}
            fixed.append({'vector_label':label,'d_g_x_e':d,'force_source_contraction':force,
                          'potential_source_contraction':potential,
                          'Earth_710km_TiPt_scalar_product':force['Earth_710km']*dot(delta_test,d),
                          'Sun_annual_Yb_k_bare_GM':m('6.95')*d[2]*force['Sun_1AU']})
        retunes=[]
        for chosen,other in [(1,0),(0,1)]:
            v=null_x_one(WF[chosen],WF[2])
            d=m('.1')*v
            residuals={name:dot(row,d) for name,row in zip(names,WF)}
            assert abs(residuals[names[chosen]])<mp.power(10,-args.dps+10)
            assert abs(residuals['Sun_1AU'])<mp.power(10,-args.dps+10)
            retunes.append({'nulled_rows':[names[chosen],'Sun_1AU'],'tested_row':names[other],
                            'd_g_x_e':d,'force_source_contraction':residuals,
                            'third_row_TiPt_scalar_product':residuals[names[other]]*dot(delta_test,d),
                            'held_source_potential_contractions':{name:dot(row,d) for name,row in zip(names,WP)}})
        mat=mp.matrix([list(normal(row)) for row in WF])
        determinant=mp.det(mat)
        # Scaling columns by the frozen coupling-box half widths makes the
        # numerical conditioning convention explicit; no empirical errors used.
        scaled=mat*mp.diag([m('.001'),m('.1'),m('.1')])
        singular=mp.svd(scaled,compute_uv=False)
        assert abs(determinant)>mp.power(10,-args.dps+10)
        results.append({'ell_m':ell,'force_rows':dict(zip(names,WF)),
                        'potential_rows':dict(zip(names,WP)),
                        'normalized_force_rows':dict(zip(names,map(normal,WF))),
                        'Earth_core_weights':{'surface':core_surface,'altitude':core_altitude},
                        'fixed_vectors':fixed,'two_row_retunes':retunes,
                        'three_normalized_force_rows_determinant':determinant,
                        'box_scaled_singular_values':singular,
                        'box_scaled_condition_number':singular[0]/singular[2],
                        'solar_stress_force_rows':{name:rows[1] for name,rows in sun_rows.items()}})
        print('ell',ell_value,'det',mp.nstr(determinant,8),'third',mp.nstr(retunes[0]['third_row_TiPt_scalar_product'],9),flush=True)

    # Independent analytic/numerical checks of the kernel itself.
    ell=m('1e7'); r=ra; a=m('.6')*rs
    P,F=kernel(ell,r,a)
    grad=-r*r*mp.diff(lambda rr:kernel(ell,rr,a)[0]/rr,r)
    assert abs(grad-F)<mp.power(10,-args.dps+10)
    mu=1/ell
    angular=mp.quad(lambda z:mp.exp(-mu*mp.sqrt(r*r+a*a-2*r*a*z))/mp.sqrt(r*r+a*a-2*r*a*z),[-1,1])/2
    shell=mp.exp(-mu*r)/r*mp.sinh(mu*a)/(mu*a)
    assert abs(angular-shell)<mp.power(10,-args.dps+10)
    total=ell+r
    def integrand(t):
        z=a/total
        sinhc=mp.sinh(t*z)/(t*z) if t else m(1)
        return ell/total*mp.exp(-t)*sinhc*(1+t*r/total)
    gamma_force=mp.quad(integrand,[0,1,mp.inf])
    assert abs(gamma_force-F)<mp.power(10,-args.dps+10)
    pointP,pointF=kernel(ell,r,m(0))
    assert abs(pointF-ell*(ell+2*r)/(ell+r)**2)<mp.power(10,-args.dps+10)
    out={'status':'conditional source-profile calculation; no empirical exclusion',
         'created_at':datetime.now(timezone.utc).isoformat(),'mpmath_version':mp.__version__,'precision_decimal_digits':args.dps,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'model_freeze_sha256':hashlib.sha256(freeze_path.read_bytes()).hexdigest(),
         'charge_code_sha256':hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest(),
         'source_hashes':{name:hashlib.sha256((args.source_dir/name).read_bytes()).hexdigest() for name in freeze['Sun_profiles']},
         'massless_profile_rows':{'Earth':E0,'Sun':S0},
         'frozen_vector_massless_roundoff_contractions':{'Earth':dot(E0,frozen_vector),'Sun':dot(S0,frozen_vector)},
         'precision_control_vector':exact_massless,
         'results':results,
         'kernel_checks':{'radial_derivative_abs_error':abs(grad-F),'direct_angular_abs_error':abs(angular-shell),
                          'gamma_integral_abs_error':abs(gamma_force-F),'point_limit':'passed'},
         'limits':['Spherical source profiles; Earth core fraction/radius and density layering supplied, no geological posterior.',
                   'Solar integral uses the tabulated radial/mass mesh without a continuum resolution error estimate.',
                   'Atomic/nuclear charge approximations inherited unchanged from massless block.',
                   'Fixed stored vector and precision-controlled massless representative are separately printed.',
                   'Retuned vector is a different vector for each ell and chosen pair; no universal cross-ell cancellation claimed.',
                   'Force products use point test bodies and bare metric GM normalization; no actual orbit/instrument exclusion.',
                   'Rank is an arbitrary-precision statement for supplied models, not a sensitivity or practical identification claim.']}
    args.output.write_text(json.dumps(serial(out),indent=2)+'\n')
    print('Kernel quadrature/gradient/point checks PASS; results',args.output,flush=True)


if __name__=='__main__':
    main()
