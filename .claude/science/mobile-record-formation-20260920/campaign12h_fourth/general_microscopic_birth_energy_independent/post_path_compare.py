"""POST comparison using only the immutable PRE local primitives for paths.
Author data are read after independently forming each value; author code is
neither imported nor executed. Polynomial enumeration does not use radicals.
"""
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json, math, sympy as sp
from path_engine import Graph,cube,ring,circulation
HERE=Path(__file__).resolve().parent

def calc(kind,n,S,degree):
 g=cube() if kind=='cube' else ring(6) if kind=='ring' else Graph(degree+1,(0,),[(0,k) for k in range(1,degree+1)])
 x=g.initial(circulation(g,[0,1,3,2],n) if kind=='cube' else circulation(g,list(range(6)),n) if kind=='ring' else None)
 C=None if S is None else sp.Integer(S*(S+1))
 @lru_cache(None)
 def out(s,center=None):return tuple((q,float(w)) for q,w in g.outward(s,C,S,center))
 @lru_cache(None)
 def born(s,e,sign):return tuple((q,float(w)) for q,w in g.birth(s,e,sign,C,S))
 def apply(v,action):
  ans=defaultdict(float)
  for s,z in v.items():
   for t,w in action(s):ans[t]+=z*w
  return {s:z for s,z in ans.items() if z!=0}
 def add(v,w,cv=1,cw=1):return {s:cv*v.get(s,0)+cw*w.get(s,0) for s in v.keys()|w.keys()}
 norm=lambda v:sum(z*z for z in v.values())
 D=lambda s:float(g.electric_D(s))
 E2=lambda s:sum(v*v for v in s[1])
 F=lambda v:apply(v,out)
 fv=F({x:1.});f2=F(fv)
 instruments={}
 for instrument in ('resolved','coherent'):
  total={'total_dimensionless_rate':0.,'total_R_squared_norm':0.,'D_drift':0.,'E2_drift':0.,'max_local_identity_squared_residual':0.}
  selected=None
  for ei,e in enumerate(g.edges):
   a=next(v for v in e if v in g.A)
   for sign in ((1,-1) if instrument=='resolved' else (None,)):
    j=lambda v:apply(v,lambda s:born(s,ei,sign))
    bv=j(fv);rv=add(j(f2),F(bv),.5,-1);loc=apply(bv,lambda s:out(s,a))
    bn,rn=norm(bv),norm(rv)
    residual=norm(add(rv,loc));assert residual<1e-24,(kind,n,S,e,sign,residual)
    total['max_local_identity_squared_residual']=max(total['max_local_identity_squared_residual'],residual)
    total['total_dimensionless_rate']+=bn;total['total_R_squared_norm']+=rn
    total['D_drift']+=sum(z*z*(D(s)-D(x)) for s,z in bv.items())
    total['E2_drift']+=sum(z*z*(E2(s)-E2(x)) for s,z in bv.items())
    chosen=(0,5) if kind=='ring' else (0,1)
    if e==chosen and sign in (1,None):
     selected={'mark':[a,next(v for v in e if v!=a),0 if sign is None else sign], 'B_squared_norm':bn,'R_squared_norm':rn,'blocked':bn<1e-14,'high_band_moment_coefficient':rn/bn if bn>1e-14 else None,'conditional_D':sum(z*z*D(s) for s,z in bv.items())/bn if bn>1e-14 else None,'conditional_E2':sum(z*z*E2(s) for s,z in bv.items())/bn if bn>1e-14 else None}
  total['selected_first_edge']=selected;instruments[instrument]=total
 return {'graph':kind,'degree_for_star':degree if kind=='star' else None,'n':n,'S':S,'initial_D':D(x),'initial_E2':E2(x),'instruments':instruments}

def symbolic():
 n,C=sp.symbols('n C',real=True,nonzero=True);g=cube();x=g.initial(circulation(g,[0,1,3,2],n));D0=g.electric_D(x);E0=sum(e*e for e in x[1])
 totalw=totalD=totalE=totalR=0
 selected={}
 for a in g.A:
  leaves=g.adj[a]
  def link(a,b):
   ei=g.edge_index[tuple(sorted((a,b)))];return x[1][ei] if a<b else -x[1][ei]
  wm={b:1-link(a,b)*(link(a,b)-1)/C for b in leaves}
  wp={b:1-link(a,b)*(link(a,b)+1)/C for b in leaves}
  for b in leaves:
   ei=g.edge_index[tuple(sorted((a,b)))];others=[c for c in leaves if c!=b]
   for sign in (1,-1):
    rate=dd=ee=0
    for old in others:
     s=g.hop(x,a,old)[0][0];y=g.birth(s,ei,sign)[0][0]
     p=wm[old]*(wp[b] if sign==1 else wm[b])
     rate+=p;dd+=p*(g.electric_D(y)-D0);ee+=p*(sum(v*v for v in y[1])-E0)
    if sign==1:
     r=4*wp[b]*sum(wm[o]*wm[t] for i,o in enumerate(others) for t in others[i+1:])
    else:
     r=wm[b]*sum(wm[o]*wp[t] for o in others for t in others if o!=t)
    totalw+=rate;totalD+=dd;totalE+=ee;totalR+=r
    if (a,b,sign)==(0,1,1):
     selected={'b':sp.factor(rate),'r':sp.factor(r),'conditional_D':sp.factor(dd/rate+D0),'conditional_E2':sp.factor(ee/rate+E0)}
 u=n*n/C;lam=sp.symbols('lambda',real=True)
 expected={'rate':48-32*u+8*u*u,'r':72-72*u+36*u*u+12*u/C,'D_drift':-32*n*n*(3-3*u+u*u)-16*n*n/C,'E2_drift':96-128*u+48*u*u}
 got={'rate':sp.factor(totalw),'r':sp.factor(totalR),'D_drift':sp.factor(totalD),'E2_drift':sp.factor(totalE)}
 for k in got:assert sp.simplify(got[k]-expected[k])==0,(k,got[k])
 a=1-n*(n+1)/C
 for k,target in {'b':a*(1+a),'r':4*a*a,'conditional_D':2*n*n/(1+a),'conditional_E2':4*n*n+2+2*n*(2*a+1)/(1+a)}.items():assert sp.simplify(selected[k]-target)==0
 # Derive the lambda expression by retaining both independently enumerated drifts.
 power=sp.expand(totalR+((1-lam)*totalD+lam*totalE)/C)
 target=72-72*u+36*u*u-32*(1-lam)*u*(3-3*u+u*u)+(-4*u+lam*(96-112*u+48*u*u))/C
 assert sp.simplify(power-target)==0
 t=sp.symbols('t',real=True)
 F0=72-168*t+132*t*t-32*t**3
 assert sp.expand(sp.diff(F0,t)+24*(t-1)*(4*t-7))==0
 return {'direct_polynomial_sums':{k:str(v) for k,v in got.items()},'selected':{k:str(v) for k,v in selected.items()},'finite_leading_power':str(sp.factor(power)),'F0_derivative':str(sp.factor(sp.diff(F0,t))),'method':'Enumerate actual old destination, marked edge and sign; evaluate diagonal observables on independently updated physical words. R cross histories counted by final charge location.'}

def differences(x,y,path=''):
 if isinstance(x,dict):
  assert set(x)==set(y),(path,set(x),set(y))
  return [z for k in x for z in differences(x[k],y[k],path+'/'+k)]
 if isinstance(x,list):
  assert x==y,(path,x,y);return []
 if isinstance(x,bool) or x is None or isinstance(x,str):assert x==y,(path,x,y);return []
 diff=abs(x-y);scaled=diff/max(1,abs(x),abs(y));assert scaled<2e-12,(path,x,y,scaled)
 return [{'field':path,'absolute_difference':diff,'relative_difference':scaled}]

if __name__=='__main__':
 source=json.loads((HERE/'post_sources/author__LOCAL_LEAKAGE_RESULTS.json').read_text());rows=[];diffs=[]
 for row in source['rows']:
  result=calc(row['graph'],row['n'],row['S'],row['degree_for_star']);d=differences(result,row)
  rows.append(result);diffs.extend(d)
 result={'independent_path_engine':'Frozen PRE path_engine.py; author Python not imported or run','author_case_count':len(source['rows']),'independent_rows':rows,'numeric_fields_compared':len(diffs),'largest_absolute_difference':max(x['absolute_difference'] for x in diffs),'largest_relative_difference':max(x['relative_difference'] for x in diffs),'all_numeric_comparisons':diffs,'symbolic':symbolic(),'all_assertions_passed':True}
 (HERE/'POST_PATH_COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('independent_rows','all_numeric_comparisons')},indent=2))
