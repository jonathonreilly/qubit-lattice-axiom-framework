#!/usr/bin/env python3
"""Exact development controls; no observations or independent empirical test."""
import hashlib,json,platform
from pathlib import Path
import sympy as s
r,th,t,ph=s.symbols('r theta t phi', real=True)
b,c,C=s.symbols('b c C',positive=True)
x=[t,r,th,ph]
g=s.diag(-1,1/b,r*r,r*r*s.sin(th)**2); gi=g.inv()
simp=lambda z:s.factor(s.trigsimp(s.simplify(z)))
Gamma=[[[simp(sum(gi[a,d]*(s.diff(g[d,j],x[i])+s.diff(g[d,i],x[j])-s.diff(g[i,j],x[d])) for d in range(4))/2) for j in range(4)] for i in range(4)] for a in range(4)]
Ric=s.zeros(4)
for i in range(4):
 for j in range(4):
  Ric[i,j]=simp(sum(s.diff(Gamma[a][i][j],x[a])-s.diff(Gamma[a][i][a],x[j])+sum(Gamma[a][a][d]*Gamma[d][i][j]-Gamma[a][j][d]*Gamma[d][i][a] for d in range(4)) for a in range(4)))
R=simp(s.trace(gi*Ric)); G=s.simplify(gi*Ric-s.eye(4)*R/2)
rows=[]
def zero(name,z):
 z=simp(z); rows.append({'name':name,'pass':z==0,'residual':str(z)}); return z
zero('Ricci scalar from full connection',R-2*(1-b)/r**2)
zero('temporal Einstein component',G[0,0]-(b-1)/r**2)
zero('radial Einstein component',G[1,1]-(b-1)/r**2)
zero('angular Einstein component',G[2,2])
zero('second angular Einstein component',G[3,3])
for i in range(4):
 for j in range(4):
  if i!=j:zero(f'off-diagonal Einstein {i}{j}',G[i,j])
# A general continuum of exact synthetic geometries, rather than fitted cases.
# The positive radial variable is used after constructing the connection.
f=C*r**c; fp=s.diff(f,r); fpp=s.diff(fp,r)
Hess=s.zeros(4)
for i in range(4):
 for j in range(4):
  Hess[i,j]=simp(s.diff(f,x[i],x[j])-sum(Gamma[k][i][j]*s.diff(f,x[k]) for k in range(4)))
box=simp(s.trace(gi*Hess)); grad=simp((s.Matrix([s.diff(f,y) for y in x]).T*gi*s.Matrix([s.diff(f,y) for y in x]))[0])
w=(1-c)/c; Z=w/f; V=-c*C*r**(c-2)/2
kin=s.zeros(4);kin[1,1]=b*fp**2
rhs=Z*(kin-s.eye(4)*grad/2)-s.eye(4)*V+gi*Hess-s.eye(4)*box
residual=s.simplify((f*G-rhs).subs(b,1/(c+1)))
for i in range(4):zero(f'family metric equation {i}',residual[i,i])
scalar=simp((R/2+Z*box-s.Rational(1,2)*w*grad/f**2-s.diff(V,r)/fp).subs(b,1/(c+1)))
zero('family scalar Euler equation',scalar)
# Independent algebraic reconstruction from the connection-derived Einstein entries.
d=b/r; u=simp((G[2,2]-G[0,0])/d)
H=simp(G[1,1]-G[0,0]-b*(s.diff(u,r)+u*u))
W=simp(-G[0,0]-H/2-b*(s.diff(u,r)+u*u)-2*b*u/r)
zero('inverse logarithmic field slope',u.subs(b,1/(c+1))-c/r)
zero('inverse kinetic function',(H/(b*u*u)).subs(b,1/(c+1))-w)
zero('inverse potential per F',W.subs(b,1/(c+1))-V/f)
zero('healthy Einstein kinetic identity',2*w+3-(1+2/c))
# Off-shell alternatives are required to produce nonzero equations.
mutants=[]
for name,newZ,newV,newf in [('kinetic_plus_half',Z+s.Rational(1,2)/f,V,f),('potential_twice',Z,2*V,f)]:
 nrhs=newZ*(kin-s.eye(4)*grad/2)-s.eye(4)*newV+gi*Hess-s.eye(4)*box
 rr=s.simplify((f*G-nrhs).subs({b:s.Rational(1,2),c:1,C:1}))
 mutants.append({'name':name,'detected':any(simp(v)!=0 for v in rr),'residuals':[str(simp(rr[i,i])) for i in range(4)]})
# Perturb the profile exponent holding the actual action omega=0,V=-1/(2F).
fm=r**2; hm=s.diag(0,s.diff(fm,r,2),r*b*s.diff(fm,r),r*b*s.sin(th)**2*s.diff(fm,r))
bm=s.trace(gi*hm); rm=s.simplify((fm*G-s.eye(4)/(2*fm)-gi*hm+s.eye(4)*bm).subs(b,s.Rational(1,2)))
mutants.append({'name':'wrong_profile_same_action','detected':any(simp(v)!=0 for v in rm),'residuals':[str(simp(rm[i,i])) for i in range(4)]})
# Explicit common-action restrictions, in one F coordinate, no data fit.
F=s.symbols('F',positive=True)
zero('patch A reconstructed potential',(V/f*f).subs({c:1,C:1,r:F})+1/(2*F))
zero('patch B reconstructed potential',V.subs({c:2,C:4})+4)
# There is no equality to assert for an imposed overlap; preserve its mismatch.
overlap={'omega_A':'0','omega_B':'-1/2','difference':str(s.Rational(1,2)),'compatible_under_same_F_overlap':False,'common_disjoint_ranges':{'A':['1','2'],'B':['4','16']},'interpretation':'Exact constructed counterexample to inferring field-range registration from these two metrics; not a global spacetime result.'}
root=Path(__file__).resolve().parent
out={'kind':'exact synthetic author controls','python':platform.python_version(),'sympy':s.__version__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'derivation_sha256':hashlib.sha256((root/'BLOCK01_DERIVATION_v1.md').read_bytes()).hexdigest(),'checks':rows,'mutations':mutants,'overlap':overlap,'pass':all(q['pass'] for q in rows) and all(q['detected'] for q in mutants),'no_empirical_data':True}
(root/'BLOCK01_CONTROLS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(('PASS ' if row['pass'] else 'FAIL ')+row['name']+': '+row['residual'])
for row in mutants:print(('DETECTED ' if row['detected'] else 'MISSED ')+row['name']+': '+str(row['residuals']))
print('OVERLAP:',json.dumps(overlap))
print('TOTAL: PASS=%d FAIL=%d; DETECTED_MUTATIONS=%d/%d'%(sum(q['pass'] for q in rows),sum(not q['pass'] for q in rows),sum(q['detected'] for q in mutants),len(mutants)))
raise SystemExit(0 if out['pass'] else 1)
