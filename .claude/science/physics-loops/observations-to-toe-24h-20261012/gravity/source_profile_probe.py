#!/usr/bin/env python3
"""High precision source-profile inversion under frozen supplied geometry."""
import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80
R=mp.mpf('6371000'); RC=mp.mpf('.55')*R
FC=mp.mpf('.32'); FM=1-FC
ELLS=[mp.mpf(x) for x in ['1e7','1e9','1e11','1e13']]
RADII=[R,R+mp.mpf('710000'),2*R]


def shell_force(ell,r,u):
    L=ell+r; z=u/L
    atanh_over_z=1 if not z else mp.atanh(z)/z
    return ell/L*(atanh_over_z+(r/L)/(1-z*z))


def ball_series(ell,r,radius):
    L=ell+r; q=(radius/L)**2
    result=mp.mpf(0); power=mp.mpf(1)
    for n in range(10000):
        term=power*(1/mp.mpf(2*n+1)+r/L)*3/(2*n+3)
        result+=term
        # All omitted factors decrease, so geometric remainder is a bound.
        remainder=term*q/(1-q)
        if remainder<mp.mpf('1e-72'):
            return ell/L*result,ell/L*remainder,n+1
        power*=q
    raise ArithmeticError('Series did not reach declared remainder')


def kernels(ell,r):
    core=ball_series(ell,r,RC)[0]
    outer=ball_series(ell,r,R)[0]
    mantle=(R**3*outer-RC**3*core)/(R**3-RC**3)
    return core,mantle


def condition_2x2(matrix):
    # Product of singular values equals |det|; avoid subtracting near-equal roots.
    determinant=mp.det(matrix)
    norm2=sum(x*x for x in matrix)
    largest2=(norm2+mp.sqrt(norm2*norm2-4*determinant*determinant))/2
    return largest2/abs(determinant)


def run():
    checks=[];rows=[]
    def check(name,passed,**data): checks.append(dict(name=name,passed=bool(passed),**data))
    for ell in ELLS:
        values=[kernels(ell,r) for r in RADII]
        ratios=[c/m for c,m in values]
        check('strict_ratio_increase',ratios[0]<ratios[1]<ratios[2],ell=str(ell))
        for radius in [RC,R]:
            series,error,n=ball_series(ell,RADII[1],radius)
            direct=3*mp.quad(lambda u:u*u*shell_force(ell,RADII[1],u),[0,radius])/radius**3
            check('series_vs_direct_shell_integral',abs(series-direct)<mp.mpf('1e-65'),
                  ell=str(ell),source_radius=str(radius),terms=n,remainder=str(error))
        # Three separately frozen charge pairs check the actual inverse map.
        pairrows=[]
        for j in [1,2]:
            c1,m1=values[0];c2,m2=values[j]
            matrix=mp.matrix([[FC*c1,FM*m1],[FC*c2,FM*m2]])
            for a,b in [('1','0'),('0','1'),('1','-.4705882352941176470588235294117647058824')]:
                charge=mp.matrix([mp.mpf(a),mp.mpf(b)])
                signal=matrix*charge
                recovered=mp.lu_solve(matrix,signal)
                check('two_radius_reconstruction',max(abs(recovered[k]-charge[k]) for k in range(2))<mp.mpf('1e-40'),
                      ell=str(ell),second_radius=str(RADII[j]),charges=[a,b])
            pairrows.append(dict(r2=str(RADII[j]),determinant=str(mp.det(matrix)),
                                 condition_number_2=str(condition_2x2(matrix))))
        rows.append(dict(ell=str(ell),radii=list(map(str,RADII)),
                         core_force=list(map(lambda v:str(v[0]),values)),
                         mantle_force=list(map(lambda v:str(v[1]),values)),
                         ratios=list(map(str,ratios)),inversion=pairrows))
    # A single pole has proportional rows regardless of component profiles.
    mu=mp.mpf('1e-7')
    ff=lambda radius:3*mp.quad(lambda u:u*u*(mp.sinh(mu*u)/(mu*u) if u else 1),[0,radius])/radius**3
    core=ff(RC); mantle=(R**3*ff(R)-RC**3*core)/(R**3-RC**3)
    k=lambda r:(1+mu*r)*mp.exp(-mu*r)
    determinant=(core*k(RADII[0]))*(mantle*k(RADII[1]))-(core*k(RADII[1]))*(mantle*k(RADII[0]))
    check('single_mass_rank_one_control',abs(determinant)<mp.mpf('1e-75'))
    return dict(status='conditional-support',observations_fitted=False,mpmath_digits=mp.mp.dps,
                passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks),
                checks=checks,rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    results=run();Path(args.output).write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:results[k] for k in ['passed','failed','source_sha256']}))
    raise SystemExit(bool(results['failed']))
