"""Independent exact square-source/removal-column threshold control."""
import os
for z in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[z]='1'
import resource,time,json,hashlib,datetime,itertools,gzip
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
t0=time.process_time();here=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not any((runtime/z).exists() for z in ('STOP_REQUESTED','STOP_REQUESTED.json'))
 assert datetime.datetime.now(datetime.timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
guard()
import numpy as np
axes=((1,0,0),(0,1,0),(0,0,1));dirs=axes+tuple(tuple(-x for x in v) for v in axes)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda a,s:tuple(s*x for x in a)
origin=(0,0,0)
G=tuple(sorted({add(u,v) for u in dirs for v in dirs}-{origin}));assert len(G)==18
Gs=set(G);mon=list(itertools.combinations_with_replacement(range(5),2));zero=np.zeros(15,dtype=np.int64)
def edge(a,b):return tuple(sorted((a,b)))
def canonical(S):
 S=tuple(sorted(S));return tuple(sub(v,S[0]) for v in S)
def wedges(x):
 ds=[edge(add(x,u),sub(x,u)) for u in axes]
 planes={}
 for i,j in itertools.combinations(range(3),2):
  planes[i,j]=[(edge(add(x,scale(axes[i],s)),add(x,scale(axes[j],t))),s*t) for s,t in itertools.product((-1,1),repeat=2)]
 return ds,planes
@lru_cache(None)
def weights_delta(d):
 out=[0]*5;non=[i for i,v in enumerate(d) if v]
 if len(non)==1 and abs(d[non[0]])==2:
  i=non[0]
  if i<2:out[i]=1
  else:out[0]=out[1]=-1
 elif len(non)==2 and all(abs(d[i])==1 for i in non):
  idx={(0,1):2,(0,2):3,(1,2):4}[tuple(non)];out[idx]=-d[non[0]]*d[non[1]]
 return tuple(out)
def weights(e):return weights_delta(sub(e[1],e[0]))
def mul(a,b):return np.array([a[i]*b[j]+(a[j]*b[i] if i!=j else 0) for i,j in mon],dtype=np.int64)
@lru_cache(None)
def matching(S):
 a,b,c,d=S
 ans=np.zeros(15,dtype=np.int64)
 for e,f in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):ans+=mul(weights(e),weights(f))
 return ans
@lru_cache(None)
def product_edges(e,f):return mul(weights(e),weights(f))
def defect(e,eta):
 S=set(e)|set(eta)
 val=matching(canonical(S)) if len(S)==4 else zero
 return val-product_edges(e,eta)
def candidates(edges):
 out=set()
 for a,b in edges:
  for v in (a,b):
   for d in G:out.add(edge(v,add(v,d)))
  for x in G:
   for y in G:
    c,d=add(a,x),add(b,y)
    if c!=d:out.add(edge(c,d))
 return out
rows=[];d0,p0=wedges(origin)
rows.append((8,[(e,1) for e in d0]))
for entries in p0.values():
 for (e,a),(f,b) in itertools.combinations(entries,2):rows.append((3,[(e,a),(f,-b)]))
for v in axes:
 d1,p1=wedges(v)
 differences=[[(e,1),(f,-1)] for e,f in zip(d1,d0)]
 rows.extend((12,row) for row in differences)
 rows.append((-4,[item for row in differences for item in row]))
 for ij in p0:rows.append((3,p1[ij]+[(e,-s) for e,s in p0[ij]]))
B12=np.zeros((15,15),dtype=np.int64);F12={};row_n=[]
def accum(dic,k,v):
 if k in dic:dic[k]+=v
 else:dic[k]=v.copy()
for nr,(w,row) in enumerate(rows):
 if nr%5==0:guard()
 res=candidates([e for e,_ in row]);non=0
 for eta in res:
  v=sum((c*defect(e,eta) for e,c in row),start=np.zeros(15,dtype=np.int64))
  if not np.any(v):continue
  non+=1;B12+=w*np.outer(v,v)
  for e,c in row:
   if set(e).isdisjoint(eta):accum(F12,canonical(e+eta),w*c*v)
 row_n.append((len(res),non))
for triple in itertools.combinations(G,3):
 S=canonical((origin,)+triple);v=matching(S)
 if np.any(v):B12+=12*np.outer(v,v);accum(F12,S,12*v)
F12={s:v for s,v in F12.items() if np.any(v)}
oldpath=here.parent/'native-interaction-route/quartic.json'
old=json.loads(oldpath.read_text());oldB=np.array(old['energy_mu_matrix_numerator'],dtype=np.int64)+np.array(old['energy_tau_matrix_numerator'],dtype=np.int64)
assert np.array_equal(B12,oldB),'independent full bare matrix mismatch'
# Independent actual K2 columns in the physical unique-edge carrier.
@lru_cache(None)
def pair_template(delta):
 e=edge(origin,delta);out=defaultdict(int);out[e]+=24
 centers=set(add(e[0],v) for v in dirs)&set(add(e[1],v) for v in dirs)
 for c in centers:
  ds,ps=wedges(c)
  if e in ds:
   i=ds.index(e)
   for j,f in enumerate(ds):out[f]+=48*(i==j)-16
   for step in dirs:
    td,_=wedges(add(c,step))
    for j,f in enumerate(td):out[f]+=-12*(i==j)+4
  else:
   hits=[(ij,s) for ij,p in ps.items() for f,s in p if f==e];assert len(hits)==1
   ij,sgn=hits[0]
   for f,s in ps[ij]:out[f]+=15*sgn*s
   for step in dirs:
    _,tp=wedges(add(c,step))
    for f,s in tp[ij]:out[f]+=-3*sgn*s
 return tuple((f,c) for f,c in out.items() if c)
def pair_column(e):
 base=e[0]
 return [(tuple(add(base,v) for v in f),c) for f,c in pair_template(sub(e[1],base))]
def degreeD(S):
 deg=[sum(sub(v,u) in Gs for v in S if v!=u) for u in S]
 return sum((d-1)*(d-2)//2 for d in deg)
def Hcol(S):
 out=defaultdict(int);out[S]+=12*degreeD(S)
 for e in itertools.combinations(S,2):
  if sub(e[1],e[0]) not in Gs:continue
  eta=tuple(v for v in S if v not in e)
  for f,c in pair_column(e):
   if set(f).isdisjoint(eta):out[canonical(eta+f)]+=c
 return {s:c for s,c in out.items() if c}
def nmatch(S):
 a,b,c,d=S
 return sum(sub(y,x) in Gs and sub(v,u) in Gs for (x,y),(u,v) in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))))
# Complete connected core, by a graph-growth algorithm, not a box enumeration.
sets={(origin,)};counts=[]
for size in (2,3,4):
 nxt=set()
 for S in sets:
  for a in S:
   for d in G:
    v=add(a,d)
    if v not in S:nxt.add(canonical(S+(v,)))
 sets=nxt;counts.append(len(sets))
core=sorted(S for S in sets if nmatch(S));assert counts==[9,113,1647] and len(core)==1487
ci={s:i for i,s in enumerate(core)};Fc=np.array([F12.get(s,zero) for s in core],dtype=np.int64)
Dtrial=1920;Xnum=-Fc.copy();HX={};hc={};full_columns=[]
for j,S in enumerate(core):
 if j%100==0:guard()
 col=Hcol(S);full_columns.append(col)
 for out,c in col.items():
  if out in ci:hc[ci[out],j]=c
  if np.any(Xnum[j]):accum(HX,out,c*Xnum[j])
for (i,j),c in hc.items():assert hc.get((j,i),0)==c,'core fiber Hermiticity'
HXC=np.array([HX.get(s,zero) for s in core],dtype=np.int64)
upper_num=Dtrial**2*B12+Dtrial*(Fc.T@Xnum+Xnum.T@Fc)+Xnum.T@HXC
assert np.array_equal(upper_num,upper_num.T)
residual={}
for S in set(F12)|set(HX):
 v=Dtrial*F12.get(S,zero)+HX.get(S,zero)
 if np.any(v):residual[S]=v
# Selected direct-row source tests, including Q source, use Hcol and M, not
# the square-source construction. Selection is deterministic, no results read.
selected=sorted(F12)[::max(1,len(F12)//12)][:12]
word=canonical(((0,0,0),(3,-1,1),(3,1,1),(6,0,0)));selected+=[word,core[0],core[-1]]
for S in selected:
 row=sum((c*matching(T) for T,c in Hcol(S).items()),start=np.zeros(15,dtype=np.int64))
 assert np.array_equal(row,F12.get(S,zero)),('source row disagreement',S,row,F12.get(S))
rawE=np.array([1,-1,0,0,0],dtype=np.int64);mE=np.array([rawE[i]*rawE[j] for i,j in mon],dtype=np.int64)
assert Hcol(word)[word]==80 and int(F12[word]@mE)==4
assert int(mE@B12@mE)==8256 # old checked bare E result, not author new matrix.
# Raw symmetric metric: duplicate offdiagonals exactly; no bosonic assumption.
G1=np.diag([2]*5);G1[0,1]=G1[1,0]=1
basis=[]
for i,j in mon:
 A=np.zeros((5,5),dtype=np.int64);A[i,j]=A[j,i]=1;basis.append(A)
G2=np.array([[np.trace(A.T@G1@B@G1) for B in basis] for A in basis],dtype=np.int64)
assert int(mE@G2@mE)==4
# Save full exact data for later author comparison; new author code unread.
allstates=sorted(set(F12)|set(residual)|{s for col in full_columns for s in col});ai={s:i for i,s in enumerate(allstates)}
rowsA=[];colsA=[];valsA=[]
for j,col in enumerate(full_columns):
 for S,c in col.items():rowsA.append(ai[S]);colsA.append(j);valsA.append(c)
np.savez_compressed(here/'PRE_ARRAYS.npz',states=np.array(allstates,dtype=np.int16),core=np.array(core,dtype=np.int16),F12=np.array([F12.get(s,zero) for s in allstates],dtype=np.int64),A_rows=np.array(rowsA,dtype=np.int32),A_cols=np.array(colsA,dtype=np.int32),A12=np.array(valsA,dtype=np.int32),B12=B12,G2=G2,Xnum=Xnum,upper_num=upper_num,residual_num=np.array([residual.get(s,zero) for s in allstates],dtype=np.int64))
result={'scope':'Independent pre-exposure exact source and trial evaluation; no new author proof/code/output read.','coordinates':old['coordinates'],'monomials':mon,'H_scale':12,'source_scale':12,'connected_growth_counts':counts,'core_dimension':len(core),'row_candidate_and_nonzero_counts':row_n,'complete_source_orbits':len(F12),'source_P_orbits':sum(nmatch(s)>0 for s in F12),'source_Q_orbits':sum(nmatch(s)==0 for s in F12),'core_to_all_nonzero_entries':len(valsA),'all_boundary_source_orbits':len(allstates),'residual_orbits':len(residual),'residual_P_orbits':sum(nmatch(s)>0 for s in residual),'residual_Q_orbits':sum(nmatch(s)==0 for s in residual),'bare_matrix_225_entries_match':True,'source_direct_rows_checked':len(selected),'selected_word_H_diagonal_numerator_over12':80,'selected_word_rawE_source_numerator_over12':4,'raw_metric':G2.tolist(),'trial_denominator':Dtrial,'raw_upper_matrix_denominator':12*Dtrial**2,'raw_upper_matrix_numerator':upper_num.tolist(),'normalized_E_threshold_upper_fraction':[int(mE@upper_num@mE),2*12*Dtrial**2],'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'pre_sha256':hashlib.sha256((here/'PRE.md').read_bytes()).hexdigest(),'old_bare_input_sha256':hashlib.sha256(oldpath.read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2,(result['cpu_seconds'],result['peak_rss_bytes'])
(here/'PRE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['complete_source_orbits','source_P_orbits','source_Q_orbits','core_to_all_nonzero_entries','residual_orbits','normalized_E_threshold_upper_fraction','cpu_seconds','peak_rss_bytes']},indent=2))
