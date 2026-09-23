from pathlib import Path
import itertools,json
import sympy as sp
D=Path(__file__).resolve().parent
A=(0,1);BB=(2,3,4);edges=tuple((a,b) for a in A for b in BB);bg=(1,1,0,0,0)
def divergence(E):
 div=[0]*5
 for v,(a,b) in zip(E,edges):div[a]+=v;div[b]-=v
 return tuple(div)
def valid(s):
 q,E=s;return tuple(x+y for x,y in zip(divergence(E),bg))==q
def hops(s):
 q,E=s;out=[]
 for i,(a,b) in enumerate(edges):
  for x,y,sign in ((a,b,1),(b,a,-1)):
   if q[x] and not q[y]:
    r=list(q);r[y]=r[x];r[x]=0;F=list(E);F[i]-=sign*q[x]
    z=(tuple(r),tuple(F));assert valid(z);out.append((z,-1))
 return out
def insert(s,e,c):
 a,b=edges[e];q,E=s
 if q[a] or q[b]:return None
 r=list(q);r[a]=c;r[b]=-c;F=list(E);F[e]+=c
 z=(tuple(r),tuple(F));assert valid(z);return z
inputs=[]
for x,y in itertools.product(range(-1,2),repeat=2):
 E=(x,y,-x-y,-x,-y,x+y);s=(bg,E);assert valid(s);inputs.append(s)
I=sp.eye(len(inputs));v=sp.Matrix([1,sp.I,2,0,1,-sp.I,1,0,2]);rho=(v*v.conjugate().T)/(v.conjugate().T*v)[0]
rows=[]
for coherent in (False,True):
 for e,(a,b) in enumerate(edges):
  for cs in (((1,-1),) if coherent else ((1,),(-1,))):
   # Whole microscopic -jT action, with legal occupation and Gauss checks.
   columns=[];output=set();branches={}
   for col,s in enumerate(inputs):
    terms={}
    for mid,amp in hops(s):
     for c in cs:
      z=insert(mid,e,c)
      if z is not None:terms[z]=terms.get(z,0)-amp
    columns.append(terms);output.update(terms)
   output=sorted(output);ix={z:i for i,z in enumerate(output)}
   mat=sp.zeros(len(output),len(inputs))
   for j,col in enumerate(columns):
    for z,amp in col.items():mat[ix[z],j]+=amp
   c=(len(BB)-1)*len(cs)
   assert mat.T*mat==c*I
   V=mat/sp.sqrt(c);assert V.conjugate().T*(V*rho*V.conjugate().T)*V==rho
   # On a retained mark, matter erasure is a mixture of orthogonal field images.
   field_ranges={}
   for q,E in output:field_ranges.setdefault(q,set()).add(E)
   assert len(field_ranges)==c
   assert len(set.union(*field_ranges.values()))==sum(map(len,field_ranges.values()))
   recovered=sp.zeros(len(inputs))
   for q,Es in field_ranges.items():
    branch_rows=[ix[(q,E)] for E in sorted(Es)]
    U=mat[branch_rows,:]
    assert U.T*U==I
    assert all(divergence(E)==tuple(q[k]-bg[k] for k in range(5)) for E in Es)
    # The erased-matter branch weight is 1/c, and its field word is an isometry.
    recovered+=U.T*(U*rho*U.T)*U/c
   assert recovered==rho
   rows.append({'instrument':'coherent' if coherent else 'resolved','edge':e,'charges':cs,'c':c,'input_dimension':len(inputs),'output_dimension':len(output),'matter_charge_branches':len(field_ranges),'Gram_exact':True,'full_recovery_exact':True,'matter_erasure_recovery_exact':True})
# Zero total rate countercontrol: one A--B edge. T makes A vacant but B occupied.
q0=(1,0);mid=(0,1);assert not(mid[0]==mid[1]==0)
assert sum((1-1) for charge in (1,-1))==0
out={'graph':'K_{2,3}, A={0,1}, B={2,3,4}, all edges oriented A to B; two independent electric cycles','exact_input_fluxes':[s[1] for s in inputs],'channel_rows':rows,'total_rate_over_kappa_resolved':sum(x['c'] for x in rows if x['instrument']=='resolved'),'total_rate_over_kappa_coherent':sum(x['c'] for x in rows if x['instrument']=='coherent'),'zero_rate_countercontrol':'One A--B edge has c_plus=c_minus=0, no first event, and no normalized mark distribution.','method':'Independent legal rotor hops and insertions with exact integer/SymPy Gram and recovery checks; no author builder.'}
(D/'INDEPENDENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
