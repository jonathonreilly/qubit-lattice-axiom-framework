from pathlib import Path
import json,sys
import sympy as s
p=Path(__file__).resolve().parent
r=s.symbols('r',positive=True);x,y=s.symbols('x y',real=True);u=s.symbols('u',real=True);nu=s.symbols('nu',positive=True)
D=1+s.Rational(2,3)*(x*x+y*y)
h=s.diag(4/(9*D),1/(3*D));g=s.diag(1,4*r*r/(9*D),r*r/(3*D));gu=s.exp(-u)*s.diag(s.Rational(1,4),4/(9*D),1/(3*D))
checks=[]
def eq(name,a,b):
 z=s.simplify(a-b); checks.append(dict(name=name,actual=str(a),expected=str(b),residual=str(z),passed=z==0))
def ricci(metric,coords):
 n=len(coords);iv=metric.inv();G=[[[s.simplify(sum(iv[k,l]*(s.diff(metric[l,j],coords[i])+s.diff(metric[l,i],coords[j])-s.diff(metric[i,j],coords[l])) for l in range(n))/2) for j in range(n)] for i in range(n)] for k in range(n)]
 R=s.zeros(n)
 for i in range(n):
  for j in range(n):
   R[i,j]=sum(s.diff(G[k][i][j],coords[k])-s.diff(G[k][i][k],coords[j])+sum(G[k][i][j]*G[l][k][l]-G[l][i][k]*G[k][j][l] for l in range(n)) for k in range(n))
 return R,G
J=s.diag(-2/r,1,1);changed=s.simplify(J.T*gu.subs(u,-2*s.log(r))*J)
for i in range(3): eq('coordinate_metric_'+str(i),changed[i,i],g[i,i])
R2,G2=ricci(h,[x,y]);R3,G3=ricci(g,[r,x,y]);origin={x:0,y:0}
Kh=s.simplify(sum(h.inv()[i,j]*R2[i,j] for i in range(2) for j in range(2)).subs(origin)/2)
Rscalar=s.simplify(sum(g.inv()[i,j]*R3[i,j] for i in range(3) for j in range(3)).subs(origin))
eq('base_Gaussian_curvature_at_origin',Kh,s.Rational(7,2));eq('three_dimensional_scalar_at_origin',Rscalar,5/r**2)
for i in range(3):eq('radial_geodesic_connection_'+str(i),G3[i][0][0],0)
eq('radial_length',s.integrate(s.exp(-u/2)/2,(u,0,s.oo)),1)
t=s.exp(-u);W=s.Rational(3,2)*(1-t)**2+t**2*(x*x/2+y*y/3+nu*u*u/2);Wr=s.Rational(3,2)*(1-r*r)**2+r**4*(x*x/2+y*y/3+2*nu*s.log(r)**2)
eq('potential_coordinate_identity',W.subs(u,-2*s.log(r)),Wr);eq('fixed_transverse_potential_endpoint',s.limit(Wr,r,0,dir='+'),s.Rational(3,2))
res=dict(scope='Exact normalized target geometry and pointwise potential endpoint; not a claim of actual cosmological escape or quantum cutoff.',checks=checks,counts=dict(passed=sum(q['passed'] for q in checks),failed=sum(not q['passed'] for q in checks)))
(p/'BOUNDARY_GEOMETRY_RESULTS_v1.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res['counts']));sys.exit(bool(res['counts']['failed']))
