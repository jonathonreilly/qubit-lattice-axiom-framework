import sys, time
import t1_minflip as T
from t1b_boxstab import min_flip_fixed, bases_by_name
orb, reps = T.orbits(False); nor=len(reps)
name_of = {T.describe(reps[o]): o for o in range(nor)}
desc="c=1 f={}; c=1 f={+x}; c=0 f={+x,+y}; c=1 f={+x,+y}; c=0 f={+x,-x,+y,+z}; c=0 f={+x,-x,+y,-y,+z}; c=0 f={+x,-x,+y,-y,+z,-z}"
A={name_of[x.strip()] for x in desc.split(';')}
b=bases_by_name()['p2:01101001']
for box in map(int, sys.argv[1:]):
    t0=time.time(); m,S=min_flip_fixed(b,orb,nor,box,A,ub=150)
    ext=[max(s[i] for s in S)-min(s[i] for s in S)+1 for i in range(3)] if S else None
    print(f"neel box={box} minflip={m} extent={ext} t={time.time()-t0:.1f}s", flush=True)
