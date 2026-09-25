"""Independent exact certificates from own primitive kernel and physical charge paths.

Searched witnesses are disclosed: the supersolution comes from our preceding
LP search; finite eigenvectors only propose rational Collatz test vectors.
No author40 or earlier author runtime/result is read, run, or imported.
"""
from collections import Counter,deque
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from primitive_kernel import column,ordered_path_column,relative_type,neighbors

HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
O=(0,0,0);start=time.perf_counter()
search=json.loads((HERE/'SUPERSOLUTION_EXPLORATION.json').read_text())
chosen=next(r for r in search['runs'] if r.get('exact_feasible'))
DEN=10**9
c={tuple(k):round(Fraction(v)*DEN) for k,v in zip(chosen['support_types'],chosen['rational_corrections'])}
def height(typ):return DEN+c.get(tuple(typ),0)
assert min([DEN]+[DEN+x for x in c.values()])>0
single={k[0]:v for k,v in column((O,)).items()}
T=2*sum(single.values())
assert T==12096
single_groups={}
for point,value in single.items():
 typ=tuple(sorted(map(abs,point)))
 if typ not in single_groups:single_groups[typ]={'coefficient':value,'multiplicity':0}
 assert single_groups[typ]['coefficient']==value
 single_groups[typ]['multiplicity']+=1

def reps_unwrapped(radius):
 return sorted({tuple(sorted(x)) for x in product(range(radius+1),repeat=3) if 0<sum(x)<=radius and sum(x)%2==0})
raw_rows=[];cert_rows=[];ordered_checks=[]
for r in reps_unwrapped(10):
 col=column((O,r));agg=Counter()
 for points,value in col.items():agg[relative_type(*points)]+=value
 residual=sum(value*height(typ) for typ,value in agg.items())-T*height(r)
 assert residual<0
 if sum(r)>4:
  free=Counter()
  for jump,value in single.items():
   final1=tuple(sorted((jump,r)))
   final2=tuple(sorted((O,tuple(a+b for a,b in zip(r,jump)))))
   free[final1]+=value;free[final2]+=value
  free={k:v for k,v in sorted(free.items()) if v}
  assert col==free
 if sum(r)<=6:
  independent=ordered_path_column((O,r))
  assert col==independent
  ordered_checks.append({'separation':r,'all_complete_column_entries':len(col),'match':True})
 raw=[[list(map(list,key)),value] for key,value in col.items()]
 raw_rows.append({'separation':r,'complete_column':raw})
 cert_rows.append({'separation':r,'row_sum':sum(col.values()),'height_numerator':height(r),'residual_numerator':residual,'grouped_column':[[list(k),v] for k,v in sorted(agg.items()) if v],'raw_column_sha256':sha(json.dumps(raw,separators=(',',':')).encode())})
one_ordered=ordered_path_column((O,));assert one_ordered=={(k,):v for k,v in single.items()}

finite=[]
for L in [6,8,10,12,14,16,18,20]:
 all_rel=[x for x in product(range(L),repeat=3) if sum(x)%2==0 and x!=O]
 classes=Counter(relative_type(O,x,L) for x in all_rel);types=sorted(classes);indices={x:i for i,x in enumerate(types)}
 rows=[];residuals=[];n=L**3//2
 for r in types:
  col=column((O,r),L);agg=Counter()
  for points,value in col.items():agg[relative_type(*points,L)]+=value
  assert O not in agg or agg[O]==0
  row={indices[k]:v for k,v in sorted(agg.items()) if v};rows.append(row)
  residuals.append(sum(v*height(types[j]) for j,v in row.items())-T*height(r))
 for i,row in enumerate(rows):
  for j,value in row.items():assert classes[types[i]]*value==classes[types[j]]*rows[j].get(i,0)
 weights=np.array([classes[k] for k in types],dtype=float)
 matrix=np.zeros((len(types),len(types)))
 for i,row in enumerate(rows):
  for j,value in row.items():matrix[i,j]=value*math.sqrt(weights[i]/weights[j])
 assert np.max(abs(matrix-matrix.T))<1e-10
 values,vectors=np.linalg.eigh(matrix)
 vec=vectors[:,-1]/np.sqrt(weights)
 if sum(vec)<0:vec=-vec
 assert min(vec)>0
 v=[round(float(x/max(vec))*10**12) for x in vec]
 assert min(v)>0
 ratios=[Fraction(sum(a*v[j] for j,a in row.items()),v[i]) for i,row in enumerate(rows)]
 lo,hi=min(ratios),max(ratios);assert hi<T
 average=Fraction(sum(classes[types[i]]*sum(row.values()) for i,row in enumerate(rows)),n-1)
 assert average==T-Fraction(1548,n-1)
 finite.append({'L':L,'n':n,'types':types,'relative_class_weights':[classes[k] for k in types],
  'matrix_rows':[[[j,v] for j,v in sorted(row.items())] for row in rows],
  'supersolution_residual_numerators':residuals,'same_local_supersolution_valid':max(residuals)<=0,
  'positive_integer_test_vector':v,'nonnegative_shift':1-min(row.get(i,0) for i,row in enumerate(rows)),
  'exact_Perron_interval':[str(lo),str(hi)],'constant_trial_exact':str(average),
  'floating_top_diagnostic':float(values[-1]),'floating_residual':float(np.linalg.norm(matrix@vectors[:,-1]-values[-1]*vectors[:,-1]))})

# The physical charge check uses actual A-even/B-odd coordinates at L=6.
L=6;vertices=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(vertices)}
A=[x for x in vertices if sum(x)%2==0];B=[x for x in vertices if sum(x)%2==1]
edges=[(a,b) for a in A for b in neighbors(a,L)];edgeindex={e:i for i,e in enumerate(edges)}
a=(0,0,0);b=(L-1,0,0);partners=[x for x in neighbors(a,L) if x!=b]
background=[int(x in A) for x in vertices]
def divergence(flow):
 d=[0]*len(vertices)
 for e,value in flow.items():
  u,v=edges[e];d[index[u]]+=value;d[index[v]]-=value
 return d
def spanning_flow(charge):
 source=[q-p for q,p in zip(charge,background)];assert sum(source)==0
 parent={O:None};order=[O]
 for u in order:
  for v in neighbors(u,L):
   if v not in parent:parent[v]=u;order.append(v)
 f={}
 for u in reversed(order[1:]):
  p=parent[u];oriented=(u,p) if u in A else (p,u);value=source[index[u]]*(1 if u in A else -1)
  if value:f[edgeindex[oriented]]=value
  source[index[p]]+=source[index[u]]
 assert divergence(f)==[q-p for q,p in zip(charge,background)]
 return f
births=[]
for sign in [-1,1]:
 for moved in partners:
  # First F_a: move the original positive charge to a vacant neighbor.
  intermediate=background.copy();intermediate[index[a]]=0;intermediate[index[moved]]=1
  assert intermediate[index[a]]==intermediate[index[b]]==0
  q=intermediate.copy();q[index[a]]=sign;q[index[b]]=-sign
  flow={edgeindex[a,b]:sign,edgeindex[a,moved]:-1}
  assert divergence(flow)==[x-y for x,y in zip(q,background)]
  assert sum(x!=0 for x in q)==len(A)+2 and sum(x==-1 for x in q)==1 and sum(q)==len(A)
  qb=sum(q[index[x]] for x in B);qa=sum(q[index[x]]-1 for x in A)
  assert qb==1-sign and qa==sign-1
  births.append({'sigma':sign,'moved_neighbor':moved,'charge_word':q,'electric_shift':sorted(flow.items()),'total_B_charge':qb,'total_A_defect':qa})
fixed_c=partners[0];occupied=A+[b,fixed_c];M=len(occupied)
uniform=[]
for minus in occupied:
 q=[int(x in occupied) for x in vertices];q[index[minus]]=-1
 flow=spanning_flow(q);qb=sum(q[index[x]] for x in B);qa=sum(q[index[x]]-1 for x in A)
 uniform.append({'minus_site':minus,'charge_word':q,'one_integer_Gauss_flow':sorted(flow.items()),'total_B_charge':qb,'total_A_defect':qa})
def charge_moments(rows):
 count=len(rows);mean=Fraction(sum(x['total_B_charge'] for x in rows),count)
 second=Fraction(sum(x['total_B_charge']**2 for x in rows),count)
 return {'normalization_squared_unscaled':count,'B_mean':str(mean),'B_second':str(second),'B_variance':str(second-mean*mean),'A_defect_mean':str(Fraction(sum(x['total_A_defect'] for x in rows),count))}
moments={'resolved_minus':charge_moments([x for x in births if x['sigma']==-1]),'resolved_plus':charge_moments([x for x in births if x['sigma']==1]),'unnormalized_coherent_then_normalized':charge_moments(births),'uniform_minus_fixed_occupation':charge_moments(uniform)}
for x in occupied:
 mean=Fraction(sum(row['charge_word'][index[x]] for row in uniform),M)
 assert mean==Fraction(len(A),M)
assert Fraction(moments['uniform_minus_fixed_occupation']['B_variance'])==Fraction(8*len(A),M*M)

result={'scope':__doc__,'source_sha256':sha(Path(__file__).read_bytes()),'helper_sha256':sha((HERE/'primitive_kernel.py').read_bytes()),'search_artifact_sha256':sha((HERE/'SUPERSOLUTION_EXPLORATION.json').read_bytes()),
 'Q_convention':'Q_I=-H4=2 sum unordered pair Grams; all threshold values use this convention.',
 'single_algebraic_kernel':{'complete_column':[[list(k),v] for k,v in single.items()],'cubic_groups':[[list(k),v] for k,v in sorted(single_groups.items())],'row_sum':sum(single.values()),'odd_occupancy_is_not_physical':True},
 'supersolution':{'denominator':DEN,'corrections_numerators':[[list(k),v] for k,v in sorted(c.items())],'positive_minimum_numerator':min([DEN]+[DEN+x for x in c.values()]),'threshold':T,'complete_unwrapped_type_rows':cert_rows,'raw_ordered_primitive_cross_checks':ordered_checks,'maximum_unwrapped_residual_numerator':max(x['residual_numerator'] for x in cert_rows)},
 'finite_tori':finite,'physical_charge_control':{'L':L,'n':len(A),'emitter':a,'marked_B':b,'partner_set':partners,'actual_birth_branches':births,'uniform_minus_fixed_B_occupation':[b,fixed_c],'uniform_minus_Gauss_rows':uniform,'normalized_charge_moments':moments,'flat_color_overlap_squared':{'resolved':'1/'+str(M),'coherent':'2/'+str(M)},'coherent_diag_equals_equal_resolved_mixture':True},
 'limits':'No g-dependent calculation, dynamics, physical charge calibration or author program. Charge diagonal equality does not dephase the coherent output. Flat color projection is not a physical energy spectral weight.',
 'elapsed_seconds':time.perf_counter()-start}
for filename,obj in [('DECISIVE_RESULTS.json',result),('UNWRAPPED_PRIMITIVE_COLUMNS.json',raw_rows)]:
 with (HERE/filename).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
summary={'source_sha256':result['source_sha256'],'helper_sha256':result['helper_sha256'],'kernel_groups':result['single_algebraic_kernel']['cubic_groups'],
 'supersolution':{k:v for k,v in result['supersolution'].items() if k not in ['complete_unwrapped_type_rows','raw_ordered_primitive_cross_checks']},
 'unwrapped_type_count':len(cert_rows),'ordered_primitive_cross_checks':len(ordered_checks),
 'finite_tori':[{k:v for k,v in row.items() if k not in ['types','relative_class_weights','matrix_rows','supersolution_residual_numerators','positive_integer_test_vector']} for row in finite],
 'charge_moments':moments,'elapsed_seconds':result['elapsed_seconds'],'complete_result_sha256':sha((HERE/'DECISIVE_RESULTS.json').read_bytes())}
print(json.dumps(summary,indent=2))
