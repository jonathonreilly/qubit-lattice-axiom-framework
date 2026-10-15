#!/usr/bin/env python3
"""Direct author substitution for a regular scalar/dust reconstruction family.

Synthetic exact field equations; no observed density, metric or chosen real action.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

base=Path(__file__).resolve().parent
r,k,rho,C,f,Cnew=s.symbols('r k rho C f Cnew',positive=True)
B=1-k*r*r
F=(C-rho*r*r/2)/B
Z=3*k/(rho-2*k*f)
V=rho/2+3*(rho-2*k*f)**2/(2*(rho-2*k*C))
gt=(B-1)/r**2+s.diff(B,r)/r
gr=(B-1)/r**2
ga=s.diff(B,r)/(2*r)
checks=[];mutations=[]


def test(name,expr):
    v=s.factor(s.cancel(expr))
    checks.append({'name':name,'ok':v==0,'residual':str(v)})


def equations(profile,density):
    fp=s.diff(profile,r);fpp=s.diff(fp,r)
    box=B*fpp+(s.diff(B,r)/2+2*B/r)*fp
    kinetic=Z.subs(f,profile)*B*fp**2
    potential=V.subs(f,profile)
    et=profile*gt+density+kinetic/2+potential+box
    er=profile*gr-kinetic/2+potential-B*fpp-s.diff(B,r)*fp/2+box
    ea=profile*ga+kinetic/2+potential-B*fp/r+box
    scalar=-(gt+gr+2*ga)/2+Z.subs(f,profile)*box+s.diff(Z,f).subs(f,profile)*B*fp**2/2-s.diff(V,f).subs(f,profile)
    return [s.factor(s.cancel(x)) for x in (et,er,ea,scalar)]


test('metric temporal Einstein component',gt+3*k)
test('metric radial Einstein component',gr+k)
test('metric angular Einstein component',ga+k)
test('source affine transport equation',s.diff(F,r)-2*k*r/B*F+rho*r/B)
test('radial field derivative',s.diff(F,r)-(2*k*C-rho)*r/B**2)
for name,value in zip(('time','radial','angular','scalar'),equations(F,rho)):
    test('full '+name+' equation',value)
test('positive Einstein kinetic coefficient',2*f*Z+3-3*rho/(rho-2*k*f))
test('center field limit',s.limit(F,r,0)-C)
test('center field derivative',s.limit(s.diff(F,r),r,0))
test('center second derivative',s.limit(s.diff(F,r,2),r,0)-(2*k*C-rho))
test('center Z limit',s.limit(Z.subs(f,F),r,0)-3*k/(rho-2*k*C))
test('center V limit',s.limit(V.subs(f,F),r,0)-(2*rho-3*k*C))

# Derive the dust stress and multiplier equation from its actual Lagrangian.
# Keep arbitrary lapse, T_t and T_r until after variation.
N, lam, Tt, Tr = s.symbols('N lam Tt Tr', positive=True)
X=-Tt**2/N**2+B*Tr**2
Lm=-lam*(X+1)/2
selected={N:1,lam:rho,Tt:1,Tr:0}
test('dust multiplier equation from variation',s.diff(Lm,lam).subs(selected))
test('dust temporal stress from Lagrangian',(-lam*Tt**2/N**2+Lm).subs(selected)+rho)
test('dust radial stress from Lagrangian',(lam*B*Tr**2+Lm).subs(selected))
test('dust angular stress from Lagrangian',Lm.subs(selected))
t=s.symbols('t');rootg=N*r*r/s.sqrt(B)
# Substitute the chosen flow after constructing the canonical currents.
jt=(rootg*s.diff(Lm,Tt)).subs(selected)
jr=(rootg*s.diff(Lm,Tr)).subs(selected)
test('dust current continuity from its action',s.diff(jt,t)+s.diff(jr,r))
# A wrong clock normalization must fail the multiplier constraint.
wrong=s.factor(s.diff(Lm,lam).subs({N:1,lam:rho,Tt:2,Tr:0}))
mutations.append({'name':'wrong dust clock normalization','detected':wrong!=0,'residual':str(wrong)})

for name,expr in [
    ('change scalar C at fixed potential coefficient',equations(F.subs(C,Cnew),rho)[0]),
    ('change source density at fixed action/profile',equations(F,2*rho)[0]),
    ('delete potential at fixed profile',-V.subs(f,F)),
]:
    v=s.factor(s.cancel(expr));mutations.append({'name':name,'detected':v!=0,'residual':str(v)})

out={'kind':'author exact synthetic substitution; independent check pending',
     'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'source_sha256':hashlib.sha256((base/'BLOCK03_MATERIAL_CANDIDATE_v1.md').read_bytes()).hexdigest(),
     'sympy':s.__version__,'checks':checks,'mutations':mutations,
     'scope':'Local regular-center dust family only; no exterior matching, nonlinear stability or empirical validation.'}
out['pass']=all(x['ok'] for x in checks) and all(x['detected'] for x in mutations)
(base/'MATERIAL_CANDIDATE_CONTROLS_v2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'mutations':len(mutations),'pass':out['pass']},indent=2))
sys.exit(0 if out['pass'] else 1)
