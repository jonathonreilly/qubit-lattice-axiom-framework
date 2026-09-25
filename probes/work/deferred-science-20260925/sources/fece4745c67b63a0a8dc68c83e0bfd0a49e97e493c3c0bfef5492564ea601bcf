"""Own bounded combinatorial/domain controls. No author or parent code is imported.

This does not simulate full rotor evolution or independently reproduce the old
two-mark path check. It checks support bookkeeping, the exact commuting-D
cancellation on integer configurations, and the geometric sum used in PRE.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import cmath, hashlib, json, math, random

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition,**data):
    assert condition,(name,data)
    row=dict(name=name,passed=True,**data)
    checks.append(row)
    print(json.dumps(row,sort_keys=True))
def graph(periods):
    vertices=list(product(*(range(n) for n in periods)))
    def move(x,axis,sgn):
        y=list(x); y[axis]=(y[axis]+sgn)%periods[axis]; return tuple(y)
    neighbors={x:set(move(x,i,s) for i in range(3) for s in (-1,1)) for x in vertices}
    def dist(x,y): return sum(min(abs(a-b),n-abs(a-b)) for a,b,n in zip(x,y,periods))
    A={x for x in vertices if sum(x)%2==0}
    stars={a:{a}|neighbors[a] for a in A}
    pairs=set()
    for a in A:
        for b in neighbors[a]:
            for c in neighbors[b]-{a}:
                pairs.add(tuple(sorted((a,c))))
    return vertices,neighbors,dist,A,stars,sorted(pairs),move

geometry=[]
for periods in [(6,6,6),(6,8,10),(8,8,8),(10,10,10)]:
    vertices,neigh,dist,A,stars,pairs,move=graph(periods)
    orig=Counter(); enlarged=Counter(); sizes=Counter(); dsizes=Counter()
    representative={}
    for a,c in pairs:
        X=stars[a]|stars[c]
        Xplus=X|set().union(*(neigh[x] for x in X))
        orig.update(X); enlarged.update(Xplus)
        sizes[len(X)]+=1; dsizes[len(Xplus)]+=1
        # Diameter is translation invariant; check one instance per relative displacement.
        displacement=tuple((ci-ai)%n for ai,ci,n in zip(a,c,periods))
        representative.setdefault(displacement,Xplus)
    maxdiam=max(max(dist(x,y) for x in X for y in X) for X in representative.values())
    shell=Counter(dist((0,0,0),x) for x in vertices)
    jump_weights=Counter()
    for a in A:
        for x in stars[a]: jump_weights[x]+=2*6*5**2
    a=(0,0,0); d=(1,1,0)
    probe=stars[a]|stars[d]
    probeplus=probe|set().union(*(neigh[x] for x in probe))
    row=dict(periods=periods,volume=len(vertices),A_sites=len(A),distance_two_pairs=len(pairs),
             original_support_sizes=dict(sorted(sizes.items())),enlarged_support_sizes=dict(sorted(dsizes.items())),
             max_original_incidence=max(orig.values()),max_enlarged_incidence=max(enlarged.values()),
             max_enlarged_diameter=maxdiam,max_mark_squared_norm_budget=max(jump_weights.values()),
             shell_counts=dict(sorted(shell.items())),probe_support=len(probe),probe_enlarged_support=len(probeplus))
    geometry.append(row)
    check('cubic_support_'+str(periods),max(sizes)<=14 and max(dsizes)<=98 and maxdiam<=6
          and max(orig.values())<=6**2*5 and max(enlarged.values())<=7*6**2*5
          and max(jump_weights.values())<=2*6**2*5**2
          and all(count<=(1 if r==0 else 4*r*r+2) for r,count in shell.items()),**row)

# Exact integer-shell identity; finite enumeration is diagnostic, not its general proof.
shell_exact=[]
for r in range(1,16):
    count=sum(1 for x in product(range(-r,r+1),repeat=3) if sum(map(abs,x))==r)
    shell_exact.append([r,count])
check('integer_shell_counts',all(count==4*r*r+2 for r,count in shell_exact),rows=shell_exact)
q=Fraction(3,8)
S2=q*(4-3*q+q*q)/(1-q)**3
check('rigorous_radial_tail_constant',S2<5 and 8+6*S2<40,
      q_upper_bound=str(q),sum_n_plus_one_squared_at_q=str(S2),radial_constant_upper_bound=str(8+6*S2))

radial=[]
for geom in geometry:
    shell={int(k):v for k,v in geom['shell_counts'].items()}
    for support in [1,7,12,84]:
        for a_t in [0.,.1,1.,10.,100.]:
            s=a_t+1+math.log(support)
            val=sum(count*min(1.,math.exp(min(0.,s-r))) for r,count in shell.items())
            upper=40*(s+2)**3
            radial.append(dict(periods=geom['periods'],support=support,a_t=a_t,value=val,upper=upper))
check('finite_torus_radial_sum_screen',all(r['value']<=r['upper'] for r in radial),rows=radial)

# Full D(q,E) on a torus, including arbitrary B occupancy and A signs.
vertices,neigh,dist,A,stars,pairs,move=graph((6,6,6))
edges=[(x,move(x,axis,1)) for x in vertices for axis in range(3)]
def diagonal(q,E):
    total=0
    for e,m in zip(edges,E):
        x,y=e
        a,b,s=(x,y,1) if x in A else (y,x,-1)
        if q[b]==0: total+=m*(m-s*q[a])
    return total
rng=random.Random(9231704)
origin=(0,0,0); target=(1,0,0); ei=edges.index((origin,target))
Xplus={origin}|neigh[origin]
gap_rows=[]
for sample in range(100):
    qword={x:rng.choice([-1,1] if x in A else [-1,0,1]) for x in vertices}
    E=[rng.randrange(-30,31) for _ in edges]
    E1=E.copy(); E1[ei]+=1
    gap=diagonal(qword,E1)-diagonal(qword,E)
    expected=(qword[target]==0)*(2*E[ei]+1-qword[origin])
    # Alter every unit-cell variable outside Xplus. D itself changes extensively.
    qfar={x:(qword[x] if x in Xplus else rng.choice([-1,1] if x in A else [-1,0,1])) for x in vertices}
    Efar=[m if e[0] in Xplus else rng.randrange(-300,301) for e,m in zip(edges,E)]
    Efar1=Efar.copy(); Efar1[ei]+=1
    gapfar=diagonal(qfar,Efar1)-diagonal(qfar,Efar)
    gap_rows.append(dict(sample=sample,q_a=qword[origin],q_b=qword[target],electric=E[ei],
                         full_gap=gap,local_formula=expected,far_modified_gap=gapfar,
                         full_D_before=diagonal(qword,E),far_D_before=diagonal(qfar,Efar)))
check('full_gated_D_integer_cancellation',all(x['full_gap']==x['local_formula']==x['far_modified_gap'] for x in gap_rows),rows=gap_rows,
      scope='Ambient full-P configuration screen; Gauss need not hold for these cancellation tests.')
check('occupancy_gate_is_material',len({x['q_b'] for x in gap_rows})==3
      and any(x['q_b']==0 and x['full_gap']!=0 for x in gap_rows)
      and all(x['full_gap']==0 for x in gap_rows if x['q_b']!=0))

# Physical divergence-free flux states around a contractible elementary square.
# A = W+W*: <A>_initial=1, <A>_electric(t_m)=cos(pi)=-1.
phase_rows=[]
for m in [1,10,100,1000,10000]:
    K=.7; gap=4*K*(2*m+1); t=math.pi/gap
    phase_rows.append(dict(m=m,energy_gap=gap,time=t,initial_expectation=1.,
                           evolved_expectation=math.cos(gap*t),absolute_change=abs(math.cos(gap*t)-1.)))
check('physical_high_flux_no_uniform_lag_modulus',all(abs(x['absolute_change']-2.)<1e-14 for x in phase_rows)
      and all(y['time']<x['time'] for x,y in zip(phase_rows,phase_rows[1:])),rows=phase_rows,
      scope='Exact diagonal model formula; bounded full-H/dissipative perturbations vanish at this sequence in fixed volume by the analytic bound in PRE.')

out=dict(scope='Own bounded geometry and diagonal-domain diagnostics, not a full evolution simulation.',
         script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),check_count=len(checks),checks=checks)
(ROOT/'CONTROL_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',len(checks),'checks completed')
