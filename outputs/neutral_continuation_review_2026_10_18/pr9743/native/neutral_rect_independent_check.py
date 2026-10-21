import sys,numpy as np,json
from collections import defaultdict
sys.path.insert(0,'/private/tmp')
from neutral_rect_model import sector
from neutral_translation_model import translation_tables,transform
D=sector((3,3,4));T,R,C=translation_tables(D);rng=np.random.default_rng(365)
def act(s,o):
 x,z,p=o;return s^x,p*(-1)**((s&z).bit_count())
def W(j):
 v={D['solve'](j):1.}
 for g in D['all_generators']:
  out=dict(v)
  for s,c in v.items():b,p=act(s,g);out[b]=out.get(b,0)+c*p
  v={s:c for s,c in out.items() if c}
 norm=sum(c*c for c in v.values())**.5
 return {s:c/norm for s,c in v.items()}
def tr(j,k):return tuple(int(v) for v in transform(j,T,R,C,k))
shifts=[(x,y,z) for x in range(3) for y in range(3) for z in range(4)]
def phys(s,k):
 dx,dy,dz=shifts[k];v=0
 for x in range(3):
  for y in range(3):
   for z in range(4):
    i=x*12+y*4+z;b=((x+dx)%3)*12+((y+dy)%3)*4+(z+dz)%4
    v|=((s>>i)&1)<<b
 return v
maxmap=maxtrans=0.
terms=sum(D['H'],[])
for _ in range(6):
 j=int(rng.integers(D['dim']));w=W(j);assert len(w)==32
 left=defaultdict(float);right=defaultdict(float)
 for s,c in w.items():
  for o in sum(D['physical_H'],[]):b,p=act(s,o);left[b]+=c*p
 for o in terms:
  b,p=act(j,o)
  for s,c in W(b).items():right[s]+=c*p
 maxmap=max(maxmap,max(abs(left[s]-right[s]) for s in left.keys()|right.keys()))
 for k in [1,4,12,35]:
  b,p=tr(j,k);a={phys(s,k):c for s,c in w.items()};b={s:p*c for s,c in W(b).items()}
  maxtrans=max(maxtrans,max(abs(a.get(s,0)-b.get(s,0)) for s in a.keys()|b.keys()))
for _ in range(100):
 j=int(rng.integers(D['dim']));k,l=rng.integers(36,size=2);a,p=tr(j,int(l));b,q=tr(a,int(k));s=tuple((shifts[k][i]+shifts[l][i])%[3,3,4][i] for i in range(3));c,r=tr(j,shifts.index(s));assert (b,p*q)==(c,r)
 # H T equals T H as sparse raw logical vectors.
 left=defaultdict(float);right=defaultdict(float);b,p=tr(j,int(k))
 for o in terms:
  a,q=act(b,o);left[a]+=p*q
  a,q=act(j,o);c,r=tr(a,int(k));right[c]+=q*r
 assert dict(left)==dict(right)
P='/private/tmp/neutral_rect_data/'
labels=np.load(P+'labels.npy',mmap_mode='r');signs=np.load(P+'signs.npy',mmap_mode='r');reps=np.load(P+'reps.npy',mmap_mode='r');sizes=np.load(P+'sizes.npy',mmap_mode='r')
maxorbit=0.
for _ in range(5):
 j=int(rng.integers(len(reps)));r=int(reps[j]);members={tr(r,k)[0]:tr(r,k)[1] for k in range(36)}
 assert len(members)==sizes[j]
 assert all(labels[s]==j and signs[s]==p for s,p in members.items())
 full=defaultdict(float)
 for s,p in members.items():
  for o in terms:a,c=act(s,o);full[a]+=p*c/np.sqrt(sizes[j])
 compressed=defaultdict(float)
 for s,c in full.items():compressed[int(labels[s])]+=signs[s]*c/np.sqrt(sizes[int(labels[s])])
 for i,c in compressed.items():
  expected=0.;ri=int(reps[i])
  for x,z,p in terms:
   s=ri^x
   if labels[s]==j:expected+=p*(-1)**((s&z).bit_count())*signs[s]*np.sqrt(sizes[i]/sizes[j])
  maxorbit=max(maxorbit,abs(c-expected))
print(json.dumps({'n':D['n'],'physical_orbit_size':32,'H_map_error':maxmap,'translation_map_error':maxtrans,'group_and_commutator_controls':100,'orbit_matvec_error':maxorbit},indent=2))
def gauss_sum(vars,linear,pairs,const=0):
 if not pairs:return 0 if linear else (-1)**const*(1<<len(vars))
 i,j=next(iter(pairs));a=int(i in linear);b=int(j in linear)
 u={next(iter(p-{i})) for p in pairs if i in p and j not in p}
 v={next(iter(p-{j})) for p in pairs if j in p and i not in p}
 newpairs={p for p in pairs if i not in p and j not in p};newlinear=linear-{i,j}
 if b:newlinear^=u
 if a:newlinear^=v
 for x in u:
  for y in v:
   if x==y:newlinear.symmetric_difference_update({x})
   else:newpairs.symmetric_difference_update({frozenset([x,y])})
 return 2*gauss_sum(vars-{i,j},newlinear,newpairs,const^(a*b))
traces=[]
for k in range(36):
 off,p0=tr(0,k);cols=[tr(1<<i,k)[0]^off for i in range(D['n'])];rr={};bad=False
 for row in range(D['n']):
  mask=sum((((cols[i]>>row)&1)^int(i==row))<<i for i in range(D['n']));rhs=(off>>row)&1
  while mask:
   b=mask.bit_length()-1
   if b in rr:mask^=rr[b][0];rhs^=rr[b][1]
   else:rr[b]=(mask,rhs);break
  else:
   if rhs:bad=True;break
 if bad:traces.append(0);continue
 free=[i for i in range(D['n']) if i not in rr]
 def sol(v):
  s=sum(((v>>i)&1)<<b for i,b in enumerate(free))
  for b in sorted(rr):
   mask,rhs=rr[b]
   if ((s&mask).bit_count()%2)^rhs:s^=1<<b
  return s
 base=sol(0);vs=[sol(1<<i)^base for i in range(len(free))];c=int(tr(base,k)[1]<0);linear=set();pairs=set()
 for i,v in enumerate(vs):
  if int(tr(base^v,k)[1]<0)^c:linear.add(i)
 for i in range(len(vs)):
  for j in range(i):
   if int(tr(base^vs[i]^vs[j],k)[1]<0)^c^int(i in linear)^int(j in linear):pairs.add(frozenset([i,j]))
 traces.append(gauss_sum(set(range(len(free))),linear,pairs,c))
assert sum(traces)%36==0
print('independent signed Burnside dimension',sum(traces)//36,'saved',len(reps))
assert sum(traces)//36==len(reps)
