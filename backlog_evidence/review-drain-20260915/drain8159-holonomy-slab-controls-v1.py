from pathlib import Path
import ast,json,math,hashlib,time
import numpy as np
r=Path('/private/tmp/review-drain-20260915');w=r/'review-draft-slot'
def load(p,names):
 t=ast.parse(p.read_text());ns={'np':np,'math':math,'G':np.array([1.,1.,.75])};ns['pref']=1/(math.pi**2*math.sqrt(np.prod(ns['G'])));exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(p),'exec'),ns);return ns
old=load(r/'drain8159-holonomy-before-slab-v1.py',{'band'});new=load(w/'scripts/holonomy_check_2026_09_15.py',{'band','_band_plane','fourier_cube'});rows=[];start=time.monotonic()
for L in [9,12]:
 for phi in [np.array([.61,1.12,2.29]),np.array([2.1,2.4,1.8]),np.full(3,math.pi)]:
  for sign in [1,-1]:
   a=old['band'](L,phi,sign,True);b=new['band'](L,phi,sign,True);errs=[float(np.max(abs(np.asarray(x)-np.asarray(y)))) for x,y in zip(a,b)]
   assert errs[0]<1e-9*max(1,abs(a[0])) and errs[1]<1e-12 and errs[2]<1e-10 and errs[3]<2e-12
   e0=new['band'](L,phi,sign,False);assert e0==(b[0],b[1]);rows.append({'L':L,'phi':phi.tolist(),'sign':sign,'errors_energy_min_gradient_hessian':errs})
fourier=[]
for M in [12,24,48]:
 mesh=np.indices((2*M+1,)*3,dtype=float).reshape(3,-1)-M;r2=np.sum(mesh*mesh/new['G'][:,None],axis=0);nz=r2>0;assert int((~nz).sum())==1
 for alpha in [np.full(3,math.pi),np.array([.7,1.3,2.2])]:
  expected=new['pref']*np.sum(np.cos(alpha@mesh[:,nz])/r2[nz]**2);actual=new['fourier_cube'](M,alpha);error=abs(actual-expected);assert error<2e-13;fourier.append({'M':M,'alpha':alpha.tolist(),'error':float(error),'points':(2*M+1)**3-1})
 del mesh,r2,nz
L=12;phi=np.array([2.1,2.4,1.8]);_,_,_,h=new['band'](L,phi,derivatives=True);eps=.004;fd=np.zeros((3,3));en=new['band'](L,phi)[0]
for i in range(3):
 ui=np.eye(3)[i]*eps;fd[i,i]=(new['band'](L,phi+ui)[0]-2*en+new['band'](L,phi-ui)[0])/eps**2
 for j in range(i):
  uj=np.eye(3)[j]*eps;fd[i,j]=fd[j,i]=(new['band'](L,phi+ui+uj)[0]-new['band'](L,phi+ui-uj)[0]-new['band'](L,phi-ui+uj)[0]+new['band'](L,phi-ui-uj)[0])/(4*eps**2)
error=float(np.max(abs(fd-h)));assert error<2e-6
out={'status':'BOUNDED AUTHOR COMPARISONS PASS; NOT FULL PRIMARY','band_cases':rows,'Fourier_cases':fourier,'original_L12_finite_difference_error':error,'unchanged_threshold':2e-6,'seconds':time.monotonic()-start,'no_primary_import_or_main':True}
(r/'drain8159-holonomy-slab-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],error,out['seconds'])
