"""Exact three-scalar complex affine top-form and all oriented cube faces."""
import json,os,re,resource,subprocess,time
import sympy as S
START=time.monotonic();resources=[];checks=[]
def guard(where):
 p=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5);m=re.search(r'System-wide memory free percentage:\s*(\d+)%',p.stdout);assert p.returncode==0 and m
 r={'where':where,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'free':int(m.group(1)),'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'elapsed':time.monotonic()-START,'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}};resources.append(r);assert r['rss']<2e9 and r['free']>=50 and max(r['load'])<20 and r['nice']>=10 and r['elapsed']<60 and set(r['threads'].values())=={'1'}
def gate(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail});assert ok,name
def integral(expr,variables):
 poly=S.Poly(S.expand(expr),*variables,domain=S.QQ_I);out=S.S.Zero
 for powers,coef in poly.terms():
  for v,n in zip(variables,powers):
   lo,hi=(S.S.Zero,S.S.One) if v==s else (-p,p)
   coef*= (hi**(n+1)-lo**(n+1))/S.Integer(n+1)
  out+=coef
 return S.simplify(out)
guard('start');w=S.symbols('w0:3');s=S.symbols('s');W=S.Matrix(w);p=S.Rational(2,3);sigma=S.Rational(2,3);I=S.I
C0=S.Matrix([[1,S.Rational(1,10),0],[S.Rational(1,10),S.Rational(6,5),S.Rational(1,13)],[0,S.Rational(1,13),S.Rational(4,5)]])
E=S.Matrix([[I/21,S.Rational(1,31),-I/41],[S.Rational(1,31),-I/27,S.Rational(1,37)],[-I/41,S.Rational(1,37),I/33]])
b0=S.Matrix([S.Rational(1,7),-S.Rational(1,9),S.Rational(1,11)]);d=S.Matrix([(1+I)/17,-I/19,S.Rational(1,23)])
Cs=C0+s*E;a=b0+s*d+sigma*Cs*W;J=S.expand(sigma**3*Cs.det())
f=S.expand(1+a[0]/17+a[1]/19+(a[0]*a[1]+a[2]**2)/23+I*a[1]*a[2]/37+a[0]**2*a[1]*a[2]/101)
body=S.expand(J*f);gate('affine maps do not commute',C0*E!=E*C0)
volume_delta=integral(body.subs(s,1)-body.subs(s,0),w)
velocity_density=sigma**2*Cs.adjugate()*(d+sigma*E*W)
guard('polynomial built');faces=[];flux=0
for i in range(3):
 F=S.expand(f*velocity_density[i]);others=tuple(v for j,v in enumerate(w) if j!=i)+(s,)
 plus=integral(F.subs(w[i],p),others);minus=-integral(F.subs(w[i],-p),others)
 faces.extend([plus,minus]);flux+=plus+minus
 guard('face pair '+str(i))
gate('all oriented faces equal exact volume change',S.simplify(flux-volume_delta)==0)
gate('omitted face rejected',S.simplify(flux-faces[0]-volume_delta)!=0)
gate('wrong outward sign rejected',S.simplify(flux-2*faces[1]-volume_delta)!=0)
missing_j=integral(J*S.diff(f,s),w+(s,))
gate('Jacobian derivative omission rejected',S.simplify(missing_j-volume_delta)!=0)
center_only=sigma**2*Cs.adjugate()*d;wrong=0
for i in range(3):
 F=S.expand(f*center_only[i]);variables=tuple(v for j,v in enumerate(w) if j!=i)+(s,)
 wrong+=integral(F.subs(w[i],p)-F.subs(w[i],-p),variables)
gate('linear boundary velocity omission rejected',S.simplify(wrong-volume_delta)!=0)
# Full trace/minors enter the identity before integration, too.
div=sum(S.diff(f*velocity_density[i],w[i]) for i in range(3))
gate('pointwise top-form divergence identity',S.Poly(S.expand(S.diff(body,s)-div),*(w+(s,))).is_zero)
guard('completion')
print(json.dumps({'checks':checks,'volume_change_exact':str(volume_delta),'volume_change_numeric':str(S.N(volume_delta,18)),'face_count':len(faces),'omission_discrepancies':{'face':str(S.N(faces[0],18)),'Jacobian_derivative':str(S.N(volume_delta-missing_j,18)),'linear_velocity':str(S.N(volume_delta-wrong,18))},'resources':resources,'scope':'Mixed three-scalar polynomial top form; checks the exact contour/minor mechanism, not an interacting Yang-Mills integral.'},indent=2))
