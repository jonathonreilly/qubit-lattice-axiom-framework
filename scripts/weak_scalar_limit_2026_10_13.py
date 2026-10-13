#!/usr/bin/env python3
"""Conditional coefficient/constraint theorem; no history integration or data fit."""
from pathlib import Path
import argparse
import hashlib
import json
import mpmath as mp
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'outputs/weak_scalar_limit_2026_10_13'
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=[
    'docs/WEAK_SCALAR_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-13.md',
    'outputs/weak_scalar_limit_2026_10_13/FIXTURES_v1.json',
    'outputs/weak_scalar_limit_2026_10_13/imports.json',
]
CHECKS=[]

def check(name,passed,**details):
    CHECKS.append(dict(name=name,passed=bool(passed),**details))

def fmt(x):
    return mp.nstr(x,80)

def near(name,actual,expected,tolerance):
    error=abs(actual-expected)/max(1,abs(expected))
    check(name,error<=tolerance,error=fmt(error),tolerance=fmt(tolerance))

def exact(name,expr):
    residue=sp.factor(sp.cancel(expr))
    check(name,residue==0,residue=str(residue))

def symbolic():
    k=sp.symbols('k',positive=True)
    u,x,y,px,py,sg,nu,al,E=sp.symbols('u x y px py sigma nu alpha E',real=True)
    a=(1-k)*(1+3*k)/4;d=k*(1-3*k);s=(1+k)/d
    F=1+s*E;f=d+(1+k)*E;D=1+sp.Rational(2,3)*(1+k)*(x*x+y*y)
    D0=D.subs(k,0);Vbar=x*x/2+y*y/3
    V0=sp.Rational(3,2)+(k/2-al*u+2*a*u*u/k)*x*x+k*y*y/3+nu*u*u/2
    V1=(k/2+al*k*u+2*a*u*u/k)*x*x+k*y*y/3
    raw=(1+s)*(V0+s*V1+sp.Rational(3,2)*s*E*E)/F**2
    S=sp.Rational(3,2)*(d+(1+k)*E*E)+2*a*k*x*x+4*al*k*k*u*x*x+8*a*a*u*u*x*x/k+4*a*k*y*y/3+nu*d*u*u/2
    exact('algebra.compact_potential',raw-4*a*S/f**2)
    exact('algebra.compact_kinetic_u',(1+(1-3*a)*s*E)/F**2-d*(d+(1-3*a)*(1+k)*E)/f**2)
    exact('algebra.compact_CB',(1+s)*E/F-4*a*E/f)
    exact('algebra.zero_potential',raw.subs({u:0,E:1})-sp.Rational(3,2)-k*Vbar)
    Ku=((1+(1-3*a)*s)/((1+s)**2))
    Kx=4*k/(9*D);Ky=k/(3*D)
    for name,expr,want in [('Ku',Ku/k,sp.Rational(1,4)),('Kx',Kx/k,4/(9*D0)),('Ky',Ky/k,1/(3*D0)),('ab',sp.sqrt(a)/(1+s)/k,sp.Rational(1,2))]:
        exact('limit.'+name,sp.limit(expr,k,0,dir='+')-want)
    # First-order physical constraint at u=pu=0. The note proves the
    # scaled u,pu terms alter this only at order k^2 or higher.
    H0=1+2*sg/3;Tbar=4*px*px/(9*D0)+py*py/(3*D0)
    H2=(3+2*k*Vbar+2*sg/(1+k))/(3-Kx*px*px-Ky*py*py)
    C1=2*(Vbar-sg)/(3*H0)+Tbar/3
    got=sp.diff(H2,k).subs(k,0)/H0
    exact('constraint.first_correction',got-C1)
    exact('constraint.ideal_cancellation',C1.subs({sg:x*x+y*y,px:-sp.Rational(3,2)*x,py:-2*y}))
    gx=4/(9*D0);gy=1/(3*D0);positions=[x,y];mom=[px,py];metric=[gx,gy]
    formulas=[(-2*x*px*px-4*y*px*py+sp.Rational(3,2)*x*py*py)/(3*D0),
              (-4*x*px*py-2*y*py*py+sp.Rational(8,3)*y*px*px)/(3*D0)]
    for i in range(2):
        lowered=mom[i]*sum(sp.diff(metric[i],positions[j])*mom[j] for j in range(2))-sum(sp.diff(metric[j],positions[i])*mom[j]**2 for j in range(2))/2
        exact('connection.'+str(i),lowered/metric[i]-formulas[i])
    return dict(first_correction=str(C1),constraint_at_zero=str(H2),connection=[str(z) for z in formulas])

def original(k,u,x,y,nu):
    a=(1-k)*(1+3*k)/4;al=mp.sqrt(a);s=(1+k)/(k*(1-3*k));E=mp.exp(2*al*u)
    F=1+s*E;D=1+mp.mpf(2)/3*(1+k)*(x*x+y*y)
    # Original Weyl kinetic combination deliberately retained as an oracle.
    ku=(1-3*a*s*E)/F+mp.mpf(3)/4*(2*al*s*E/F)**2
    K=[ku,(1+s)*4*k/(9*F*D),(1+s)*k/(3*F*D)]
    V0=mp.mpf('1.5')+(k/2-al*u+2*a*u*u/k)*x*x+k*y*y/3+nu*u*u/2
    V1=(k/2+al*k*u+2*a*u*u/k)*x*x+k*y*y/3
    U=(1+s)*(V0+s*V1+mp.mpf('1.5')*s*E*E)/F**2
    return K,U,al/F,(1+s)*E/F

def compact(k,u,x,y,nu):
    a=(1-k)*(1+3*k)/4;al=mp.sqrt(a);d=k*(1-3*k);E=mp.exp(2*al*u)
    f=d+(1+k)*E;D=1+mp.mpf(2)/3*(1+k)*(x*x+y*y)
    K=[d*(d+(1-3*a)*(1+k)*E)/f**2,16*a*k/(9*f*D),4*a*k/(3*f*D)]
    S=mp.mpf('1.5')*(d+(1+k)*E*E)+2*a*k*x*x+4*al*k*k*u*x*x+8*a*a*u*u*x*x/k+4*a*k*y*y/3+nu*d*u*u/2
    return K,4*a*S/f**2,al*d/f,4*a*E/f

def numerics(fix):
    rows=[];connections=[]
    mp.mp.dps=fix['decimal_precision']
    for j,point in enumerate(fix['points']):
        v,w,x,y,px,py,sg,nu=map(mp.mpf,point)
        D0=1+mp.mpf(2)/3*(x*x+y*y);Hg=1+2*sg/3
        Vbar=x*x/2+y*y/3;Tbar=(4*px*px/9+py*py/3)/D0
        C1=2*(Vbar-sg)/(3*Hg)+Tbar/3
        target=[mp.mpf('.25'),4/(9*D0),1/(3*D0),Vbar,mp.mpf('.5'),mp.mpf(1),v*x*x-x*x-2*y*y/3,x*x]
        for power in fix['k_powers']:
            k=mp.mpf(10)**(-power);u=k*k*v;pu=k*w
            K,U,ab,cb=compact(k,u,x,y,nu);Kr,Ur,abr,cbr=original(k,u,x,y,nu)
            for c,(z,expected) in enumerate(zip([*K,U,ab,cb],[*Kr,Ur,abr,cbr])):
                near(f'compact.{j}.{power}.{c}',z,expected,mp.mpf(fix['raw_compact_tolerance']))
            Uu=mp.diff(lambda t:compact(k,t,x,y,nu)[1],u)
            Uuu=mp.diff(lambda t:compact(k,t,x,y,nu)[1],u,2)
            values=[*[z/k for z in K],(U-mp.mpf('1.5'))/k,ab/k,cb,Uu/k,k*Uuu]
            for c,(z,expected) in enumerate(zip(values,target)):
                near(f'limit.{j}.{power}.{c}',z,expected,mp.mpf(fix['coefficient_error_bound_per_k'])*k)
            for derivative,z in [(1,Uu),(2,Uuu)]:
                expected=mp.diff(lambda t:original(k,t,x,y,nu)[1],u,derivative)
                near(f'derivative.{j}.{power}.{derivative}',z,expected,mp.mpf(fix['raw_compact_tolerance']))
            T=K[0]*pu*pu+K[1]*px*px+K[2]*py*py
            nh=1+ab*pu;Hhat=2*(U+cb*cb*sg/(1+k))/(3-T);HJ=Hhat*nh*nh/cb
            check(f'domain.{j}.{power}',all(z>0 for z in K) and T<3 and nh>0)
            observed=(HJ/Hg-1)/k
            near(f'first_correction.{j}.{power}',observed,C1,mp.mpf(fix['first_correction_error_bound_per_k'])*k)
            near(f'Newton_limit.{j}.{power}',cb*(1+ab*ab/K[0])/(1+k),mp.mpf(1),200*k)
            if x:
                near(f'fast_curvature.{j}.{power}',k*k*Uuu/(K[0]*Hhat),4*x*x/Hg,200*k)
            rows.append(dict(point=j,k=fmt(k),coefficients=[fmt(z) for z in values],targets=[fmt(z) for z in target],
                             physical_H_squared=fmt(HJ),H_GR_squared=fmt(Hg),first_correction=fmt(C1),
                             finite_difference_correction=fmt(observed),potential_curvature=fmt(Uuu)))
        def metric(xx,yy):
            D=1+mp.mpf(2)/3*(xx*xx+yy*yy)
            return [4/(9*D),1/(3*D)]
        coords=[x,y];vel=[px,py];gg=metric(x,y)
        explicit=[(-2*x*px*px-4*y*px*py+mp.mpf('1.5')*x*py*py)/(3*D0),
                  (-4*x*px*py-2*y*py*py+mp.mpf(8)/3*y*px*px)/(3*D0)]
        for i in range(2):
            def deriv(entry,coordinate):
                return mp.diff(lambda t:metric(*(coords[:coordinate]+[t]+coords[coordinate+1:]))[entry],coords[coordinate])
            lowered=vel[i]*sum(deriv(i,r)*vel[r] for r in range(2))-sum(deriv(r,i)*vel[r]**2 for r in range(2))/2
            wanted=lowered/gg[i]
            near(f'lowered_momentum.{j}.{i}',explicit[i],wanted,mp.mpf(fix['connection_tolerance']))
            connections.append(dict(point=j,component=i,explicit=fmt(explicit[i]),lowered=fmt(wanted)))
            if abs(wanted)>mp.mpf('1e-10'):
                check(f'connection_omission_control.{j}.{i}',abs(wanted)>mp.mpf('1e-10'),omitted_error=fmt(abs(wanted)))
    return rows,connections

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--out',type=Path,default=HERE/'RESULTS.json');args=pa.parse_args()
    inputs=[dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()) for p in AUDIT_INPUT_PATHS]
    fix=json.loads((HERE/'FIXTURES_v1.json').read_text());sym=symbolic();rows,connections=numerics(fix)
    check('census.points',len(rows)==len(fix['points'])*len(fix['k_powers']))
    check('unique_names',len({c['name'] for c in CHECKS})==len(CHECKS))
    for item in inputs:
        check('input_unchanged.'+item['path'],hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'])
    result=dict(scope='Conditional fixed-compact coefficient and physical-constraint expansion; no ODE convergence or empirical test.',
                inputs=inputs,symbolic=sym,rows=rows,connections=connections,checks=CHECKS,
                counts=dict(passed=sum(c['passed'] for c in CHECKS),failed=sum(not c['passed'] for c in CHECKS),total=len(CHECKS)))
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print('Weighted action limits, first physical Hubble correction, curved connection and supplied local Newton limit.')
    print('TOTAL: PASS='+str(result['counts']['passed'])+' FAIL='+str(result['counts']['failed']))
    return int(result['counts']['failed']!=0)

if __name__=='__main__':
    raise SystemExit(main())
