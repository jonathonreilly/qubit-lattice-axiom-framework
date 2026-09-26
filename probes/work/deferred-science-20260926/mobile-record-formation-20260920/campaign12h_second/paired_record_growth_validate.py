"""Author cross-implementation channel checks. Not an independent review."""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,random,subprocess,sys
HERE=Path(__file__).resolve().parent
OUT=HERE/'growth_validation';OUT.mkdir(exist_ok=True)
BINARY=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/paired_record_growth')
N=4;SITES=tuple(product(range(N),repeat=3));ID={x:i for i,x in enumerate(SITES)}
D=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (1,-1));BITS=tuple(product((0,1),repeat=3))
def add(x,d):return tuple((a+b)%N for a,b in zip(x,d))
def valid(s):return all(v<0 or s[ID[add(x,D[v])]]==(v^1) for x,v in zip(SITES,s))
def word(s):return ''.join(str(x+1) for x in s)
def born(s,x,j):
 y=add(x,D[2*j]);assert s[ID[x]]<0 and s[ID[y]]<0
 new=s.copy();new[ID[x]]=2*j;new[ID[y]]=2*j+1;return new

def python_channels(s):
 assert valid(s);channels={}
 def keep(family,x,a,mask,new):
  if new==s or not valid(new):return
  if family!='B':assert Counter(new)==Counter(s)
  channels[(family,ID[x],a,mask)]=word(new)
 for x in SITES:
  for j in range(3):
   y=add(x,D[2*j])
   if s[ID[x]]<0 and s[ID[y]]<0:keep('B',x,j,0,born(s,x,j))
  if s[ID[x]]>=0:
   y=add(x,D[s[ID[x]]]);old={x,y}
   for a,d in enumerate(D):
    targets={add(p,d) for p in old}
    if any(s[ID[p]]>=0 for p in targets-old):continue
    new=s.copy()
    for p in old:new[ID[p]]=-1
    for p in old:new[ID[add(p,d)]]=s[ID[p]]
    keep('T',x,a,0,new)
  corners={b:add(x,b) for b in BITS}
  for j in range(3):
   axes=[a for a in range(3) if a!=j]
   def aligned(f,a):return all(s[ID[p]]==2*a+b[a] for b,p in corners.items() if b[j]==f)
   is_original=(aligned(0,axes[0]) and aligned(1,axes[1])) or (aligned(0,axes[1]) and aligned(1,axes[0]))
   if is_original:
    new=s.copy()
    for b,p in corners.items():dest=list(b);dest[j]=1-dest[j];new[ID[corners[tuple(dest)]]]=s[ID[p]]
    keep('C',x,j,0,new)
   edges=[]
   for b in BITS:
    if b[j]==0:
     dest=list(b);dest[j]=1;edges.append((corners[b],corners[tuple(dest)]))
   for mask in range(1,16):
    new=s.copy()
    for i,(p,q) in enumerate(edges):
     if mask&(1<<i):new[ID[p]],new[ID[q]]=s[ID[q]],s[ID[p]]
    keep('P',x,j,mask,new)
 return channels

def fixtures():
 out={'empty':[-1]*len(SITES)}
 for j in range(3):
  out[f'single_{j}']=born(out['empty'],(1,1,1),j)
  out[f'wrap_single_{j}']=born(out['empty'],(3,3,3),j)
 for base in ((0,0,0),(3,3,3)):
  r=out['empty'].copy()
  for y in (0,1):r=born(r,add(base,(0,y,0)),0)
  for x in (0,1):r=born(r,add(base,(x,0,1)),1)
  out[f'full_cube_{base}']=r
 jam=out['empty'].copy()
 for base in product((0,2),repeat=3):
  for x,j in [((1,0,0),1),((0,1,0),2),((0,0,1),0)]:jam=born(jam,add(base,x),j)
 out['jam']=jam
 for seed in range(8):
  rng=random.Random(seed);r=out['empty'].copy();edges=[(x,j) for x in SITES for j in range(3)];rng.shuffle(edges)
  for x,j in edges:
   if r[ID[x]]<0 and r[ID[add(x,D[2*j])]]<0:r=born(r,x,j)
  out[f'greedy_{seed}']=r
 return out

def main():
 rows=[]
 for name,s in fixtures().items():
  stem=name.replace(' ','').replace('(','').replace(')','').replace(',','_')
  inp=OUT/(stem+'.state.txt');inp.write_text(' '.join(map(str,s))+'\n');output=OUT/(stem+'.channels.txt')
  result=subprocess.run([str(BINARY),'--enumerate',str(N),str(inp),str(output)],capture_output=True,text=True)
  (OUT/(stem+'.stderr')).write_text(result.stderr);assert result.returncode==0,(name,result.stderr)
  actual={}
  for line in output.read_text().splitlines():
   f,x,a,mask,w=line.split();key=(f,int(x),int(a),int(mask));assert key not in actual;actual[key]=w
  expected=python_channels(s)
  if actual!=expected:
   missing=[k for k in expected if k not in actual];extra=[k for k in actual if k not in expected];wrong=[k for k in expected if k in actual and expected[k]!=actual[k]]
   (OUT/'FAILURE.json').write_text(json.dumps({'fixture':name,'missing':missing,'extra':extra,'wrong':wrong},indent=2));raise AssertionError('channel mismatch '+name)
  counts=dict(Counter(k[0] for k in actual));row={'fixture':name,'channels':len(actual),'by_family':counts,'exact_match':True};rows.append(row);print(json.dumps(row))
  if name=='empty':assert counts=={'B':3*N**3}
  if name.startswith('single_') or name.startswith('wrap_single_'):
   assert counts['T']==12 # Two endpoint channels per six dimer displacements.
  if name=='jam':assert not any(k in counts for k in ('B','T','C')) and counts.get('P',0)>0
  # Each conservative target has a same-rate reverse channel. T uses shifted anchor.
  for (family,x,a,mask),w in actual.items():
   if family=='B':continue
   target=[int(v)-1 for v in w];assert valid(target)
   if family=='T':
    newx=add(SITES[x],D[a]);newy=add(newx,D[target[ID[newx]]]);back=target.copy()
    for p in (newx,newy):back[ID[p]]=-1
    for p in (newx,newy):back[ID[add(p,D[a^1])]]=target[ID[p]]
   else:
    back=target.copy();axis=a;selected=15 if family=='C' else mask;channel=0
    for b in BITS:
     if b[axis]:continue
     c=list(b);c[axis]=1;p=add(SITES[x],b);q=add(SITES[x],tuple(c))
     if selected&(1<<channel):back[ID[p]],back[ID[q]]=target[ID[q]],target[ID[p]]
     channel+=1
   assert back==s,(name,family,x,a,mask)
 source={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'paired_record_growth.cpp',HERE/'PAIRED_RECORD_GROWTH_SCREEN_PROTOCOL.md',BINARY]}
 final={'status':'author cross-implementation, not independent review','sources_sha256':source,'rows':rows,'empty_density_derivative_per_beta':6,'translation_rate_accounting':'12 endpoint channels at kappa/2 = six dimer displacements at kappa','all_match':True}
 (OUT/'VALIDATION_RESULTS.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps({'all_match':True,'fixtures':len(rows),'total_channels':sum(r['channels'] for r in rows),'sources_sha256':source}))
if __name__=='__main__':main()
