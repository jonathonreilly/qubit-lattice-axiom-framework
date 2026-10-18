from pathlib import Path
import sys,json,numpy as np
from neutral_four_layer_spatial import geometry,diagonal
P=Path('/tmp/neutral_four_layer_spatial')
for R in map(int,sys.argv[1:] or [4,5]):
 d=np.load(P/f'R{R}.npz');u=d['u'];g=u[:,0];g*=np.sign(g.sum());reps=d['reps'];diag=d['diag'];ev=d['ev'];edgecoords=[]
 for x in range(R):
  for y in range(R):
   if x+1<R:edgecoords.append(((x,y),(x+1,y)))
   if y+1<R:edgecoords.append(((x,y),(x,y+1)))
 _,_,masks,_=geometry(R)
 def maps(pt):
  x,y=pt
  return [(x,y),(y,R-1-x),(R-1-x,R-1-y),(R-1-y,x),(x,R-1-y),(R-1-y,R-1-x),(R-1-x,y),(y,x)]
 def canonical(e):
  a,b=e;ma,mb=maps(a),maps(b)
  return min(tuple(sorted((ma[k],mb[k]))) for k in range(8))
 groups={}
 for i,e in enumerate(edgecoords):groups.setdefault(canonical(e),[]).append(i)
 rows=[]
 for key,inds in groups.items():
  E=-diagonal(reps,masks[inds])/5
  amplitudes=[float(u[:,j]@(E*g))/len(inds) for j in range(1,len(ev))]
  rows.append(dict(representative=key,edges=len(inds),amplitude_per_edge=amplitudes))
 modes=[]
 for j in range(len(ev)-1):
  total=sum(r['edges']*r['amplitude_per_edge'][j] for r in rows)
  square=sum(r['edges']*r['amplitude_per_edge'][j]**2 for r in rows)
  fourth=sum(r['edges']*r['amplitude_per_edge'][j]**4 for r in rows)
  corner=0.
  for row in rows:
   # Entire bond lies inside a 2x2 block at a geometric corner.
   pts=row['representative']
   if any(all((x<=1 if cx==0 else x>=R-2) and(y<=1 if cy==0 else y>=R-2) for x,y in pts) for cx,cy in [(0,0),(0,1),(1,0),(1,1)]):corner+=row['edges']*row['amplitude_per_edge'][j]**2
  modes.append(dict(gap=float(ev[j+1]-ev[0]),source_weight=9*total**2,transition_edge_participation=square*square/fourth if fourth else 0,corner_edge_fraction=corner/square if square else 0))
 out=dict(R=R,modes=modes,edge_orbits=rows,scope='Transition-density profile of D4-invariant coefficient eigenvectors; not particle wavefunction or bulk limit')
 (P/f'R{R}_profile.json').write_text(json.dumps(out,indent=2)+'\n');print(R,modes,flush=True)
