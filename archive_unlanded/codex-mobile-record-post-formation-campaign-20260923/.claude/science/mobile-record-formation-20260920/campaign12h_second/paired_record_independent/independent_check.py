#!/usr/bin/env python3
"""Independent edge-mask enumeration, analytic lumping, and record controls.
No author runner/result imports. Output is confined to this directory.
"""
from pathlib import Path
from itertools import product,permutations
from collections import Counter,defaultdict
import hashlib,json
import sympy as s
import numpy as np
HERE=Path(__file__).resolve().parent;checks=[]
def done(name,details):checks.append({'name':name,'details':details})
V=list(product((0,1),repeat=3));vi={x:i for i,x in enumerate(V)}
E=[(i,j) for i in range(8) for j in range(i+1,8) if sum(abs(V[i][a]-V[j][a]) for a in range(3))==1]
ei={e:j for j,e in enumerate(E)};foot=[(1<<a)|(1<<b) for a,b in E]
axes=[next(i for i in range(3) if V[a][i]!=V[b][i]) for a,b in E]
def members(m):return [e for e in range(12) if m>>e&1]
def occ(m):return sum(foot[e] for e in members(m))
M=[]
for m in range(1<<12):
 seen=0
 for e in members(m):
  if seen&foot[e]:break
  seen|=foot[e]
 else:M.append(m)
mi={m:i for i,m in enumerate(M)};census=Counter(m.bit_count() for m in M)
assert len(M)==108 and [census[k] for k in range(5)]==[1,12,42,44,9]
unit=[tuple(sign*int(j==i) for j in range(3)) for i in range(3) for sign in (-1,1)]
def translated_edge(e,a):
 p,q=[tuple(V[v][j]+a[j] for j in range(3)) for v in E[e]]
 if p not in vi or q not in vi:return None
 return ei[tuple(sorted((vi[p],vi[q])))]
def cube_target(m,normal):
 if m.bit_count()!=4:return None
 face=[]
 for side in (0,1):
  edges=[e for e in members(m) if all(V[v][normal]==side for v in E[e])]
  if len(edges)!=2 or len({axes[e] for e in edges})!=1:return None
  face.append(axes[edges[0]])
 if face[0]==face[1]:return None
 target=0
 for e in members(m):
  vs=[]
  for v in E[e]:
   p=list(V[v]);p[normal]=1-p[normal];vs.append(vi[tuple(p)])
  target|=1<<ei[tuple(sorted(vs))]
 assert target!=m
 return target
rows=[[],[],[]]
channels=[]
for m in M:
 B=defaultdict(int);H=defaultdict(int);C=defaultdict(int);occupied=occ(m)
 for e in range(12):
  if not occupied&foot[e]:B[mi[m|1<<e]]+=1
 for e in members(m):
  for a in unit:
   f=translated_edge(e,a)
   if f is not None and not ((occupied^foot[e])&foot[f]):
    target=m^(1<<e)^(1<<f)
    assert target in mi and target!=m
    H[mi[target]]+=1
 for normal in range(3):
  target=cube_target(m,normal)
  if target is not None:C[mi[target]]+=1
 for family,row in zip(rows,[B,H,C]):family.append(dict(row))
 channels.append({'mask':m,'birth':sum(B.values()),'translation':sum(H.values()),'cube':sum(C.values())})
B,H,C=rows
for R in [H,C]:
 for i,row in enumerate(R):
  for j,w in row.items():assert R[j].get(i,0)==w
assert Counter(x['cube'] for x in channels)=={0:102,1:6}
for m,c in zip(M,channels):
 if m.bit_count()==0:assert c['birth']==12
 if m.bit_count()==1:assert (c['birth'],c['translation'])==(7,2)
done('reflecting_cube_states_and_channel_multiplicities',{'census':[census[k] for k in range(5)],'states':108,'cube_event_counts':{'zero':102,'one':6},'one_dimer_birth_translation_rates':[7,2]})
# Ten exact equitable classes; internal moves drop out of the lumped generator.
names=['empty','one','parallel_face','parallel_diagonal','skew','three_parallel','three_mixed','unfilled_trap','full_columnar','full_mixed']
def category(m,i):
 n=m.bit_count();ac=sorted(Counter(axes[e] for e in members(m)).values(),reverse=True)
 if n==0:return 0
 if n==1:return 1
 if n==2:
  if ac==[1,1]:return 4
  return 2 if sum(B[i].values())==4 else 3
 if n==3:
  if ac==[3]:return 5
  if ac==[2,1]:return 6
  assert ac==[1,1,1];return 7
 return 8 if ac==[4] else 9
cat=[category(m,i) for i,m in enumerate(M)];sizes=Counter(cat)
expected_sizes=[1,12,12,6,24,12,24,8,3,6]
assert [sizes[c] for c in range(10)]==expected_sizes
lumped=[]
for family in rows:
 rates=[]
 for c in range(10):
  forms=[]
  for i in range(108):
   if cat[i]!=c:continue
   row=[0]*10
   for j,w in family[i].items():
    if cat[j]!=c:row[cat[j]]+=w
   row[c]=-sum(row)
   forms.append(row)
  assert all(x==forms[0] for x in forms)
  rates.append(forms[0])
 lumped.append(s.Matrix(rates))
G=sum(lumped,s.zeros(10));trans=list(range(7));absorb=[7,8,9]
P=-G.extract(trans,trans).inv()*G.extract(trans,absorb)
assert P[0,:]==s.Matrix([[s.Rational(4,21),s.Rational(13,49),s.Rational(80,147)]])
assert all(x>=0 for x in P) and P*s.ones(3,1)==s.ones(7,1)
# A simpler exact harmonic certificate needs no rate-sensitive matrix inverse.
hcat=s.Matrix([s.Rational(4,21),s.Rational(4,21),0,0,s.Rational(1,3),0,0,1,0,0])
for A in lumped:assert A*hcat==s.zeros(10,1)
h=[hcat[c] for c in cat]
for family in rows:
 for i,row in enumerate(family):assert sum(w*(h[j]-h[i]) for j,w in row.items())==0
assert all(sum(B[i].values())>=1 for i in range(108) if cat[i]<7)
# Closed SCCs are found independently by direct reachability on the 108-state graph.
adj=[set(B[i])|set(H[i])|set(C[i]) for i in range(108)]
reach=[]
for i in range(108):
 seen={i};todo=[i]
 while todo:
  v=todo.pop()
  for j in adj[v]-seen:seen.add(j);todo.append(j)
 reach.append(seen)
components=[];assigned=set()
for i in range(108):
 if i in assigned:continue
 comp={j for j in reach[i] if i in reach[j]};assigned|=comp;components.append(comp)
closed=[comp for comp in components if all(adj[i]<=comp for i in comp)]
assert sorted(map(len,closed))==[1]*11+[2]*3
assert sum(map(len,closed))==17 and 108-sum(map(len,closed))==91
traps=[i for comp in closed for i in comp if M[i].bit_count()==3]
assert len(traps)==8
for i in traps:
 vacant=[v for v in range(8) if not occ(M[i])>>v&1]
 assert len(vacant)==2 and all(V[vacant[0]][a]+V[vacant[1]][a]==1 for a in range(3))
 assert len(adj[i])==0
done('exact_ten_class_absorption_and_harmonic_certificate',{'classes':dict(zip(names,expected_sizes)),'birth_lump':lumped[0].tolist(),'translation_lump':lumped[1].tolist(),'cube_lump':lumped[2].tolist(),'empty_hitting_unfilled_columnar_mixed':[str(x) for x in P[0,:]],'harmonic_function':[str(x) for x in hcat],'transient_states':91,'closed_component_sizes':sorted(map(len,closed)),'unfilled_traps':8,'opposite_corner_vacancies':True})
# Actual matching event graph covariance on the reflecting cube.
groups=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
  R=np.zeros((3,3),dtype=int)
  for a in range(3):R[a,perm[a]]=signs[a]
  t=np.array([int(v<0) for v in signs]);destv=[vi[tuple(R@np.array(v)+t)] for v in V]
  deste=[ei[tuple(sorted((destv[a],destv[b])))] for a,b in E]
  destm=[mi[sum(1<<deste[e] for e in members(m))] for m in M]
  for family in rows:
   for i,row in enumerate(family):
    transformed={destm[j]:w for j,w in row.items()}
    assert transformed==family[destm[i]]
  groups.append((R,t,int(round(np.linalg.det(R)))))
assert sum(det==1 for _,_,det in groups)==24
done('actual_channel_covariance',{'proper_rotations':24,'additional_reflections_checked':24,'families':['birth','translation','cube'],'no_physical_reflection_assignment_inferred':True})
# Labeled whole-record implementation with simultaneous overlap-safe transport.
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def valid(records):
 assert len({v[0] for v in records.values()})==len(records)
 for x,(identity,d) in records.items():assert add(x,d) in records and records[add(x,d)][1]==neg(d)
def birth(records,x,d,start):
 y=add(x,d);assert x not in records and y not in records
 out=records.copy();out[x]=(start,d);out[y]=(start+1,neg(d));valid(out);return out

def move(records,x,a):
 d=records[x][1];y=add(x,d);old={x,y};targets={add(x,a),add(y,a)}
 assert not (targets-old)&records.keys()
 values={x:records[x],y:records[y]};out={p:v for p,v in records.items() if p not in old}
 for p,v in values.items():out[add(p,a)]=v
 valid(out);assert sorted(out.values())==sorted(records.values());assert out!=records
 return out
origin=(0,0,0);ex=(1,0,0);initial=birth({},origin,ex,1)
for a in unit:
 after=move(initial,origin,a);back=move(after,add(origin,a),neg(a));assert back==initial
history=move(initial,origin,(0,1,0));history=birth(history,origin,ex,3)
assert len(history)==4 and history[(0,1,0)]==initial[origin] and history[(1,1,0)]==initial[(1,0,0)]
# All 64 nearest-neighbor vacancy patterns are feasible via outward radial mates.
patterns=[]
for bits in product((0,1),repeat=6):
 records={};ident=1
 for d,vacant in zip(unit,bits):
  if not vacant:records=birth(records,d,d,ident);ident+=2
 valid(records);allowed=[d for d in unit if d not in records]
 assert len(allowed)==sum(bits)
 for d in allowed:valid(birth(records,origin,d,100))
 patterns.append({'vacancies':sum(bits),'hazard_over_beta':len(allowed)})
assert sum(r['vacancies']==0 for r in patterns)==1
# Outside all vacant: the only admissible one-site completion is vacant.
for d in unit:
 try:valid({origin:(1,d)})
 except AssertionError:pass
 else:raise AssertionError('isolated single record should be inadmissible')
done('record_identity_overlap_renewal_and_formation_law',{'translations_tested':6,'renewal_records':4,'feasible_neighbor_patterns':64,'conditional_probability':'1/(number of vacant neighbors) for each vacant neighbor; undefined at zero hazard','DLR_empty_exterior':'Only the vacant one-site completion is admissible.'})
# Staggered link Gauss formula on an even torus, including wrapped dimers.
def gauss_check(edges,N=4):
 n=np.zeros((N,N,N,3),dtype=int);occupied=np.zeros((N,N,N),dtype=int)
 for base,axis in edges:
  end=list(base);end[axis]=(end[axis]+1)%N;end=tuple(end)
  assert not occupied[base] and not occupied[end]
  occupied[base]=occupied[end]=1;n[base+(axis,)]=1
 parity=np.fromfunction(lambda x,y,z:1-2*((x+y+z)%2),(N,N,N),dtype=int)
 # Six times B uses integer arithmetic.
 field=parity[...,None]*(6*n-1)
 div=sum(field[...,a]-np.roll(field[...,a],1,axis=a) for a in range(3))
 assert np.array_equal(div,6*parity*(occupied-1))
 assert int(np.sum(parity*(1-occupied)))==0
 return field,n,parity
for m in M:
 edges=[(V[E[e][0]],axes[e]) for e in members(m)]
 gauss_check(edges)
gauss_check([((3,0,0),0),((0,3,1),1),((2,2,3),2)])
# Actual dense cube readout and its exact polynomial increment.
before=next(m for m in M if m.bit_count()==4 and all((V[E[e][0]][2]==0 and axes[e]==0) or (V[E[e][0]][2]==1 and axes[e]==1) for e in members(m)))
after=cube_target(before,2);assert after is not None and cube_target(after,2)==before
records={}
for j,e in enumerate(members(before)):
 a,b=E[e];d=tuple(V[b][i]-V[a][i] for i in range(3));records=birth(records,V[a],d,2*j+1)
new={tuple((1-p[i]) if i==2 else p[i] for i in range(3)):v for p,v in records.items()}
valid(new);assert sorted(new.values())==sorted(records.values()) and len(new)==8
assert all(sum(abs(p[i]-next(q for q,w in new.items() if w[0]==v[0])[i]) for i in range(3))==1 for p,v in records.items())
X,Y,Z=s.symbols('X Y Z');phase=[X,Y,Z];delta=[0,0,0]
for e in set(members(before))|set(members(after)):
 p=V[E[e][0]];axis=axes[e];dn=int(e in members(after))-int(e in members(before))
 delta[axis]+=(-1)**sum(p)*dn*s.prod(phase[i]**p[i] for i in range(3))
assert all(s.expand(v-w)==0 for v,w in zip(delta,[(Y-1)*(Z+1),-(X-1)*(Z+1),0]))
assert s.expand(sum((1-phase[i])*delta[i] for i in range(3)))==0
assert all(v.subs({X:1,Y:1,Z:1})==0 if hasattr(v,'subs') else v==0 for v in delta)
kx,ky,kz,t=s.symbols('kx ky kz t',real=True)
linear=[s.expand(s.sympify(v).subs({X:1-s.I*kx*t,Y:1-s.I*ky*t,Z:1-s.I*kz*t})).coeff(t,1) for v in delta]
assert linear==[-2*s.I*ky,2*s.I*kx,0]
f0,_,_=gauss_check([(V[E[e][0]],axes[e]) for e in members(before)])
f1,_,_=gauss_check([(V[E[e][0]],axes[e]) for e in members(after)])
for axis in range(3):
 for cut in range(4):assert np.take((f1-f0)[...,axis],cut,axis=axis).sum()==0
done('staggered_Gauss_and_actual_cube_Fourier_increment',{'even_torus_side':4,'matching_states_tested':108,'wrapped_dimer_test':True,'integer_six_B_identity':True,'dense_records':8,'polynomial_increment':[str(s.factor(v)) for v in delta],'first_order':[str(v) for v in linear],'all_cut_flux_increments_zero':True})
# The staggered readout has an orientation sign and an origin-parity sign.
base_edges=[(V[E[e][0]],axes[e]) for e in members(before)]
for R,tvec,det in groups:
 transformed=[]
 for p,axis in base_edges:
  destaxis=next(j for j in range(3) if R[j,axis]);sign=R[destaxis,axis]
  base=(R@np.array(p)+tvec)%4
  if sign<0:base[destaxis]=(base[destaxis]-1)%4
  transformed.append((tuple(base),destaxis))
 actual,_,_=gauss_check(transformed)
 expected=np.zeros_like(actual);chi=(-1)**int(sum(tvec))
 for p in product(range(4),repeat=3):
  for axis in range(3):
   destaxis=next(j for j in range(3) if R[j,axis]);sign=R[destaxis,axis]
   base=(R@np.array(p)+tvec)%4
   if sign<0:base[destaxis]=(base[destaxis]-1)%4
   expected[tuple(base)+(destaxis,)]=chi*sign*f0[p+(axis,)]
 assert np.array_equal(actual,expected)
for displacement in unit:
 translated=[(tuple((p[j]+displacement[j])%4 for j in range(3)),axis) for p,axis in base_edges]
 actual,_,_=gauss_check(translated)
 axis=next(j for j in range(3) if displacement[j])
 assert np.array_equal(actual,-np.roll(f0,displacement[axis],axis=axis))
def pair_ids(record_map):
 return {tuple(sorted((value[0],record_map[add(pos,value[1])][0]))) for pos,value in record_map.items()}
assert pair_ids(records)==pair_ids(new)
done('readout_covariance_and_persistent_pair_identity',{'signed_cube_actions':48,'unit_translation_sign_checks':6,'new_edge_base_orientation_handled':True,'dense_move_preserves_birth_partner_pairs':True})

# Archive compact graph for transparent post-seal state-by-state comparison.
graph={'vertices':V,'edges':E,'matching_masks':M,'classes':cat,'class_names':names,'birth_rows':B,'translation_rows':H,'cube_rows':C,'hitting_unfilled':[str(v) for v in h]}
(HERE/'CUBE_GRAPH.json').write_text(json.dumps(graph,indent=2)+'\n')
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'all assertions passed','checks':checks,'scope':'Independent finite matching, event, Fourier, and reflecting-cube controls. No periodic accessibility, phase, wave or quantum assertion.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2,default=str)+'\n');print(json.dumps(result,indent=2,default=str))
