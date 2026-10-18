import sys, time
import t1_minflip as T
from t1b_boxstab import min_flip_fixed, bases_by_name
orb, reps = T.orbits(False); nor=len(reps)
name_of = {T.describe(reps[o]): o for o in range(nor)}
desc="c=0 f={}; c=1 f={}; c=1 f={+x}; c=0 f={+x,-x}; c=1 f={+x,+y}; c=0 f={+x,-x,+y}; c=0 f={+x,-x,+y,-y}; c=0 f={+x,+y,+z}; c=0 f={+x,-x,+y,+z}; c=1 f={+x,-x,+y,-y,+z}; c=1 f={+x,-x,+y,-y,+z,-z}"
A={name_of[x.strip()] for x in desc.split(';')}
# faithfulness check: every face orbit has a centre value
ok = all((orb[f<<1] in A) or (orb[(f<<1)|1] in A) for f in range(64))
print("faithful (a centre value allowed for every neighbour condition):", ok, " |A|=",len(A))
b=bases_by_name()['p2:00000001']
for box in map(int, sys.argv[1:]):
    t0=time.time(); m,S=min_flip_fixed(b,orb,nor,box,A,ub=60)
    print(f"faithful-18 rule box={box} minflip={m} t={time.time()-t0:.1f}s", flush=True)
