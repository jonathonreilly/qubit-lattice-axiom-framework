"""T166 - the response profile, with a perturbation that is NOT a symmetry.

T165 saturated: |v_A - v_B| = 1.000000 at every distance.  The cause is that the
rule is LINEAR AND ODD and the pure-state projection commutes with negation, so
flipping the seed flips the WHOLE grown configuration exactly.  That is a genuine
symmetry of the construction, not propagation, and it makes an antipodal seed
useless as a probe.  (The control was right: zero channel gave exactly zero.)

Redo with a SMALL ROTATION of the seed, which is not a symmetry of the rule, and
measure the response |v_A - v_B| against distance.  Two things can then show up:
   * a profile that falls with distance  -> a correlation length;
   * a profile that is flat inside the record front and zero outside -> the front
     itself is the causal boundary and influence is total within it.
Both are informative; they say different things about what 'propagation' means here.

Stated assumptions, neither of them axiom content: all boundary sites record each
step, and a record locks the nearest pure state deterministically (sampling from
the distribution would be more faithful but its noise would swamp the response)."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t165 import grow, DIRS
L=25; STEPS=9
def rotz(v,th):
    c,s=np.cos(th),np.sin(th)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1], v[2]])
print("T166  response profile to a SMALL seed perturbation")
print(f"      L={L}, {STEPS} steps, alpha=1/3, delta=1/sqrt(3)")
print()
base=np.array([0.3,0.0,0.4]); base=0.5*base/np.linalg.norm(base)
for eps in (0.4,0.1,0.02):
    A=grow(L,base,1/3,1/np.sqrt(3),STEPS,rng_seed=11)
    B=grow(L,rotz(base,eps),1/3,1/np.sqrt(3),STEPS,rng_seed=11)
    c=L//2
    print(f"   seed rotated by {eps} rad")
    print(f"      {'dist':>5} {'sites':>6} {'mean |v_A-v_B|':>16} {'/eps':>10} {'max':>10}")
    for r in range(1,STEPS+1):
        ds=[np.linalg.norm(A[x]-B[x]) for x in A if max(abs(np.array(x)-c))==r and x in B]
        if ds: print(f"      {r:5d} {len(ds):6d} {np.mean(ds):16.8f} {np.mean(ds)/eps:10.4f} {max(ds):10.6f}")
    print()
print("   flat in r and proportional to eps  => linear response, total inside the front")
print("   falling in r                       => a genuine correlation length")
