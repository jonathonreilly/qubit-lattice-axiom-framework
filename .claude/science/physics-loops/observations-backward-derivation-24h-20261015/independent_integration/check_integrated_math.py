#!/usr/bin/env python3
"""Independent geometry, action residuals and bound invariants for integration."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/SCALAR_OBSERVATION_INVERSE_AND_INPUT_BOUNDS_NOTE_2026-10-16.md",
    "scripts/scalar_observation_inverse.py",
    "scripts/scalar_observation_inverse_math.py",
)

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "scripts"))
import scalar_observation_inverse_math as author

EXPECTED = {
    AUDIT_INPUT_PATHS[0]: "23185fcfd16a9f762a9d810efb843ed178e5a749e7dba73dfcfa9726c745f768",
    AUDIT_INPUT_PATHS[1]: "d4cda09d0fd70b58d998783b8951c6f7596a2bc44909b0003c3679f7ae5d8405",
    AUDIT_INPUT_PATHS[2]: "6c363eb9087e84f932c5ec12964257cb92470daaa51b107f4f0c0d35a2b30c44",
}
checks = []


def red(x):
    return s.factor(s.cancel(s.together(x)))


def check(name, expressions):
    if not isinstance(expressions, (tuple, list)):
        expressions = [expressions]
    residuals = [red(x) for x in expressions]
    result = {"name": name, "ok": all(x == 0 for x in residuals), "residuals": [str(x) for x in residuals]}
    checks.append(result)
    print(("PASS: " if result["ok"] else "FAIL: ") + name, flush=True)


start_hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
checks.append({"name": "frozen current source identities at start", "ok": start_hashes == EXPECTED, "actual": start_hashes})

# Full four-dimensional connection/curvature from the metric, without calling
# the author's geometry helper until after the tensor is computed.
t, r, th, ph = s.symbols("t r theta phi", real=True)
N, B = s.Function("N")(r), s.Function("B")(r)
coords = (t, r, th, ph)
metric = s.diag(-N**2, 1 / B, r**2, r**2 * s.sin(th)**2)
inverse = s.diag(-1 / N**2, B, 1 / r**2, 1 / (r**2 * s.sin(th)**2))
gamma = [[[s.simplify(sum(inverse[a, l] * (s.diff(metric[l, j], coords[i]) + s.diff(metric[l, i], coords[j]) - s.diff(metric[i, j], coords[l])) / 2 for l in range(4))) for j in range(4)] for i in range(4)] for a in range(4)]
ricci = s.Matrix(4, 4, lambda i, j: s.simplify(sum(
    s.diff(gamma[a][i][j], coords[a]) - s.diff(gamma[a][i][a], coords[j])
    + sum(gamma[a][i][j] * gamma[b][a][b] - gamma[b][i][a] * gamma[a][j][b] for b in range(4))
    for a in range(4))))
scalar_curvature = s.simplify(sum(inverse[i, j] * ricci[i, j] for i in range(4) for j in range(4)))
einstein = [s.simplify(inverse[i, i] * ricci[i, i] - scalar_curvature / 2) for i in range(4)]
gt, gr, ga, d = author.spherical_geometry(r, N, B)
check("helper Einstein tensor compared with full four-dimensional curvature", [gt-einstein[0], gr-einstein[1], ga-einstein[2], ga-einstein[3]])
field = s.Function("field")(r)
hessian = [s.simplify(inverse[i, i] * (s.diff(field, coords[i], coords[i])-gamma[1][i][i]*s.diff(field, r))) for i in range(4)]
check("transport denominator is the actual angular-temporal Hessian difference", hessian[2]-hessian[0]-d*s.diff(field,r))

# A non-power metric supplies a different exact inverse family. The positive
# interval 1<=r<=2 has d>0 and the listed u has a positive numerator.
lapse = s.exp(r**2/16)
radial = 1/(1+r**2/5)
subs = {N:lapse, B:radial}
G = [red(x.subs(subs).doit()) for x in einstein]
curvature = red(scalar_curvature.subs(subs).doit())
u, omega, W = [red(x) for x in author.vacuum_inverse(r,lapse,radial)]
fval=s.symbols("fval",positive=True)
derivatives = {field:fval,s.diff(field,r):fval*u,s.diff(field,r,2):fval*(s.diff(u,r)+u**2)}
Hess = [red(x.subs(subs).doit().subs(derivatives)) for x in hessian]
box=sum(Hess)
norm=radial*fval**2*u**2
Z=omega/fval
potential=fval*W
residuals=[]
for i in range(4):
    directed=radial*(fval*u)**2 if i==1 else 0
    residuals.append(fval*G[i]-Z*(directed-norm/2)+potential-Hess[i]+box)
check("all metric equations for independent non-power reconstruction",residuals)
ZF=(s.diff(omega,r)/u-omega)/fval**2
VF=W+s.diff(W,r)/u
check("direct scalar equation for independent non-power reconstruction",curvature/2+Z*box+ZF*norm/2-VF)
check("non-power transport from independently computed curvature",u-(G[2]-G[0])/(radial*(1/r-s.diff(lapse,r)/lapse)))

# Exact primitive relation at arbitrary light speed, not only the runner's c=1.
rad,q,R,P,c,v=s.symbols("rad q R P c v",positive=True)
E,J=author.observation_parts(rad,q,R,P,c*R*v/rad,c)
check("primitive density with arbitrary light speed",J-R**2*P**2/(q*rad*(1-v**2)))
scale=s.symbols("scale",positive=True)
E2,J2=author.observation_parts(rad,q,R,P,scale*c*R*v/rad,scale*c)
check("simultaneous orbit-rate/light-speed unit conversion",[E2-E,J2-J])
log_arguments=[P,q,rad,R**2*(1-v**2),R]
endpoint_ratio=P*R**2/(q*rad*(R**2*(1-v**2)))
check("endpoint multiplicative ratio",endpoint_ratio-P/(q*rad*(1-v**2)))

# The helper's bound is linear in supplied error radii. Differentiate that
# implementation and compare with an independently differentiated rational J.
# Concrete rational envelopes avoid trying to order symbolic lower bounds.
lo={"r":s.Rational(2),"R":s.Rational(3),"q":s.Rational(5),"P":s.Rational(7),"D":s.Rational(11)}
hi={"r":s.Rational(13),"R":s.Rational(17),"O":s.Rational(19),"P":s.Rational(23)}
length=s.Rational(29)
light=s.Rational(31)
args=s.symbols("ar aR aO aq aP",nonnegative=True)
errors=dict(zip(("r","R","O","q","P"),args))
# Use concrete error basis vectors so helper domain guards are exercised without
# imposing an artificial total order on independent symbolic numbers.
RR,PP,QQ,radial_arg,DD=s.symbols("RR PP QQ radial_arg DD",positive=True)
func=RR**4*PP**2/(QQ*radial_arg*DD)
rect={RR:hi['R'],PP:hi['P'],QQ:lo['q'],radial_arg:lo['r'],DD:lo['D']}
deriv={key:s.Abs(s.diff(func,var)).subs(rect) for key,var in [('R',RR),('P',PP),('q',QQ),('r',radial_arg),('D',DD)]}
D_deriv={'r':2*hi['r']*hi['O']**2/light**2,'R':2*hi['R'],'O':2*hi['r']**2*hi['O']/light**2,'q':0,'P':0}
endpoint={'r':2/lo['r'],'R':4/lo['R'],'O':0,'q':2/lo['q'],'P':2/lo['P']}
for key in errors:
    basis={name:s.Integer(name==key) for name in errors}
    bound,eD=author.primitive_bound(lo,hi,basis,length,light)
    expected=endpoint[key]+2*D_deriv[key]/lo['D']+length*(deriv.get(key,0)+deriv['D']*D_deriv[key])
    check("independent derivative envelope coefficient: "+key,[bound-expected,eD-D_deriv[key]])

# Weighted Cauchy is a completed square: no selected numerical profiles needed.
S,weight,inc,H=s.symbols("S weight inc H",positive=True)
square=weight*(S-inc/(H*weight))**2
check("pointwise completed-square identity for radar bins",square-(weight*S**2-2*inc*S/H+inc**2/(H**2*weight)))
aa,width,scaleS=s.symbols("aa width scaleS",positive=True)
upper=aa+width
weighted=s.integrate(scaleS**2*r,(r,aa,upper))
increment=s.integrate(scaleS*r,(r,aa,upper))
inverse_weight=s.integrate(r,(r,aa,upper))
check("bin helper reaches equality for actual integrated profile",weighted-author.bin_lower_bound([increment],[inverse_weight]))

# Dust family re-established directly from full curvature and the full Hessian.
f,k,rho,C=s.symbols("f k rho C",positive=True)
Bd,Fd,Zd,Vd=author.dust_family(r,f,k,rho,C)
dust_sub={N:s.Integer(1),B:Bd}
dustG=[red(x.subs(dust_sub).doit()) for x in einstein]
dustR=red(scalar_curvature.subs(dust_sub).doit())
dustH=[red(x.subs(dust_sub).doit().subs(field,Fd).doit()) for x in hessian]
dustBox=sum(dustH)
dustNorm=Bd*s.diff(Fd,r)**2
matter=[-rho,0,0,0]
dust_res=[]
for i in range(4):
    directed=dustNorm if i==1 else 0
    dust_res.append(Fd*dustG[i]-matter[i]-Zd.subs(f,Fd)*(directed-dustNorm/2)+Vd.subs(f,Fd)-dustH[i]+dustBox)
check("dust metric equations from independently computed full curvature",dust_res)
check("dust scalar equation from independent curvature and Hessian",dustR/2+Zd.subs(f,Fd)*dustBox+s.diff(Zd,f).subs(f,Fd)*dustNorm/2-s.diff(Vd,f).subs(f,Fd))
check("constant branch scalar slope uses independently computed curvature",dustR/2-3*k)

# Restore the stipulated reference length instead of silently setting it to 1.
reference_length, positive_radius, power = s.symbols("reference_length positive_radius power",positive=True)
power_profile=C*(positive_radius/reference_length)**power
restored_factor=s.powdenest((C/power_profile)**(2/power)/reference_length**2,force=True)
check("restored reference length in power-family potential ratio",restored_factor-1/positive_radius**2)
for bb,exponent in [(s.Rational(1,2),s.Integer(1)),(s.Rational(1,3),s.Integer(2))]:
    profile=C*(r/reference_length)**exponent
    omega=(1-exponent)/exponent
    kinetic_function=omega/f
    potential=-bb*exponent*(exponent+1)*C**(2/exponent)*f**(1-2/exponent)/(2*reference_length**2)
    background={N:s.Integer(1),B:bb}
    gpower=[red(x.subs(background).doit()) for x in einstein]
    rpower=red(scalar_curvature.subs(background).doit())
    hpower=[red(x.subs(background).doit().subs(field,profile).doit()) for x in hessian]
    boxpower=sum(hpower)
    normpower=bb*s.diff(profile,r)**2
    metric_res=[]
    for i in range(4):
        directed=normpower if i==1 else 0
        metric_res.append(profile*gpower[i]-kinetic_function.subs(f,profile)*(directed-normpower/2)+potential.subs(f,profile)-hpower[i]+boxpower)
    scalar_res=rpower/2+kinetic_function.subs(f,profile)*boxpower+s.diff(kinetic_function,f).subs(f,profile)*normpower/2-s.diff(potential,f).subs(f,profile)
    check("all power-family equations with reference length restored: exponent "+str(exponent),metric_res+[scalar_res])

# Endpoint/guard controls appropriate to the actual helper contract.
for title,call in [
    ("zero D guard",lambda:author.primitive_bound({**lo,'D':0},hi,{name:0 for name in errors},1)),
    ("negative error guard",lambda:author.primitive_bound(lo,hi,{**{name:0 for name in errors},'R':-1},1)),
    ("zero light-speed guard",lambda:author.primitive_bound(lo,hi,{name:0 for name in errors},1,0)),
    ("empty bins guard",lambda:author.bin_lower_bound([],[])),
    ("zero H guard",lambda:author.bin_lower_bound([1],[0])),
    ("uncertified symbolic H guard",lambda:author.bin_lower_bound([1],[s.Symbol("unknown_H",real=True)])),
]:
    try:
        call(); rejected=False
    except ValueError:
        rejected=True
    checks.append({'name':title,'ok':rejected})

final_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
checks.append({'name':'source identities unchanged during independent calculation','ok':final_hashes==start_hashes,'actual':final_hashes})
result={'kind':'focused independent mathematical check, not audit or empirical test','utc_time':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'source_hashes':final_hashes,'checks':checks,'nonpower_transport':str(u),'nonpower_interval':'1 <= r <= 2; d>0 and u>0','pass':sum(bool(x['ok']) for x in checks),'fail':sum(not x['ok'] for x in checks)}
(HERE/'independent_math_evidence.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pass':result['pass'],'fail':result['fail'],'source_moved':final_hashes!=start_hashes}))
sys.exit(0 if result['fail']==0 else 1)
