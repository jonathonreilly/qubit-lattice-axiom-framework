"""Explore all content-preserving matching rearrangements in each unit cube.
This strictly enlarges the proposed move support; it is not its dynamics.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
HERE=Path(__file__).resolve().parent
BITS=tuple(product((0,1),repeat=3));INDEX={x:i for i,x in enumerate(BITS)}
D=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (1,-1))
def local_patterns():
 out=[]
 def rec(free,words):
  if not free:out.append(tuple(words));return
  x=min(free);rec(free-{x},words)
  for y in free-{x}:
   delta=tuple(b-a for a,b in zip(BITS[x],BITS[y]))
   if delta not in D:continue
   new=words.copy();d=D.index(delta);new[x]=d;new[y]=d^1;rec(free-{x,y},new)
 rec(set(range(8)),[-1]*8);assert len(out)==108;return out
PATTERNS=local_patterns()
def analyze(path,N):
 s=list(map(int,path.read_text().split()));assert len(s)==N**3
 sites=tuple(product(range(N),repeat=3));idx={x:i for i,x in enumerate(sites)}
 def add(x,d):return tuple((a+b)%N for a,b in zip(x,d))
 def valid(words):return all(d<0 or words[idx[add(x,D[d])]]==(d^1) for x,d in zip(sites,words))
 assert valid(s);all_cubes=[];alternative_total=0;nearest_total=0
 for base in sites:
  corners=[add(base,b) for b in BITS];inside=set(corners);old=[s[idx[x]] for x in corners]
  pinned={i:d for i,(x,d) in enumerate(zip(corners,old)) if d>=0 and add(x,D[d]) not in inside}
  alternatives=[]
  for pattern in PATTERNS:
   if any(pattern[i]>=0 for i in pinned):continue
   target=list(pattern)
   for i,d in pinned.items():target[i]=d
   if Counter(target)!=Counter(old) or target==old:continue
   words=s.copy()
   for x,d in zip(corners,target):words[idx[x]]=d
   assert valid(words)
   # Existence of a one-step-or-stay assignment for every immutable content.
   def assign(a,b):
    if not a:return True
    x=a[0]
    return any((corners[y]==corners[x] or corners[y] in [add(corners[x],d) for d in D]) and assign(a[1:],b[:j]+b[j+1:]) for j,y in enumerate(b))
   nearest=all(assign([i for i,d in enumerate(old) if d==a],[i for i,d in enumerate(target) if d==a]) for a in range(6))
   alternatives.append({'target':target,'all_records_move_at_most_one_step':nearest});nearest_total+=int(nearest)
  alternative_total+=len(alternatives)
  all_cubes.append({'base':base,'pinned_corners':pinned,'source':old,'alternatives':alternatives})
 return {'state_path':str(path),'state_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'N':N,'vacancies':s.count(-1),'direction_counts':[s.count(2*i) for i in range(3)],'cubes':len(sites),'alternative_total':alternative_total,'nearest_record_alternatives':nearest_total,'census':all_cubes}

def main():
 output=HERE/'maximal_cube_support';output.mkdir(exist_ok=True);results=[]
 for phase,name,N in [('pilot','N4_jam_extended_s21092102',4),('screen','N4_jam_extended_s21092204',4),('pilot','N4_empty_extended_s21092101',4)]:
  path=HERE/('paired_growth_'+phase)/(name+'.final.txt');result=analyze(path,N)
  (output/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n');brief={k:v for k,v in result.items() if k!='census'};results.append(brief);print(json.dumps(brief))
 (output/'SUMMARY.json').write_text(json.dumps({'status':'author maximal unit-cube support census; not independent review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'results':results},indent=2)+'\n')
if __name__=='__main__':main()
