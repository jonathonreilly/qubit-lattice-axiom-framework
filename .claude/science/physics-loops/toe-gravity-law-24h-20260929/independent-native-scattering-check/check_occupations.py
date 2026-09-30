#!/usr/bin/env python3
"""Independent physical-occupation action; coefficients are integers times 1/12."""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction
import json, os, resource, time

t0=time.monotonic()
out=Path(__file__).parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    assert os.environ.get(name)=='1'
resource.setrlimit(resource.RLIMIT_CPU,(30,35))
e=((1,0,0),(0,1,0),(0,0,1)); zero=(0,0,0)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda n,a:tuple(n*x for x in a)
steps=tuple(scale(s,v) for v in e for s in (-1,1))
G=set(scale(s*2,v) for v in e for s in (-1,1))
for i,j in combinations(range(3),2):
    for s,t in product((-1,1),repeat=2): G.add(add(scale(s,e[i]),scale(t,e[j])))
def canon(S):
    S=tuple(sorted(S)); a=S[0]
    return tuple(sub(v,a) for v in S)
def matching(S):
    return any(sub(S[b],S[0]) in G and sub(S[d],S[c]) in G
               for b,c,d in ((1,2,3),(2,1,3),(3,1,2)))
def degree(S): return [sum(sub(y,x) in G for y in S if x!=y) for x in S]
def plusentry(result,S,mu,ta):
    if not (mu or ta): return
    a,b=result.get(S,(0,0)); result[S]=(a+mu,b+ta)

# Enumerate local Q representations of one annihilated physical pair.
def reps(a,b):
    d=sub(b,a); nonzero=[j for j in range(3) if d[j]]
    if len(nonzero)==1 and abs(d[nonzero[0]])==2:
        yield ('E',tuple((x+y)//2 for x,y in zip(a,b)),nonzero[0],1)
    elif len(nonzero)==2 and all(abs(d[j])==1 for j in nonzero):
        i,j=nonzero
        for axis in (i,j):
            center=add(a,scale(d[axis],e[axis]))
            aa=sub(a,center); bb=sub(b,center)
            sign=next(v for v in aa if v)*next(v for v in bb if v)
            yield ('T',center,(i,j),sign)

def action(S):
    S=tuple(sorted(S)); result={}
    deg=degree(S)
    plusentry(result,S,12*(len(S)+sum(d*(d-1)//2 for d in deg)),0)
    for aa,bb in combinations(S,2):
        residual=tuple(x for x in S if x!=aa and x!=bb)
        residualset=set(residual)
        for kind,center,old,signold in reps(aa,bb):
            for shift in (zero,)+steps:
                cc=add(center,shift); onsite=(shift==zero)
                if kind=='E':
                    for new in range(3):
                        pair=(sub(cc,e[new]),add(cc,e[new]))
                        if residualset.intersection(pair): continue
                        pe=2 if new==old else -1
                        mu=-8*pe if onsite else 0
                        ta=24*pe if onsite else -4*pe
                        plusentry(result,tuple(sorted(residual+pair)),mu,ta)
                else:
                    i,j=old
                    for s,t in product((-1,1),repeat=2):
                        pair=(add(cc,scale(s,e[i])),add(cc,scale(t,e[j])))
                        if residualset.intersection(pair): continue
                        sg=s*t*signold
                        plusentry(result,tuple(sorted(residual+pair)),
                                  -3*sg if onsite else 0,18*sg if onsite else -3*sg)
    return {S:c for S,c in result.items() if c!=(0,0)}

# All labeled four-vertex graphs, independent of geometric realizability.
edges=tuple(combinations(range(4),2)); histogram={}; nonmatching=0
for bits in range(64):
    E={edges[j] for j in range(6) if bits>>j&1}
    deg=[sum(i in edge for edge in E) for i in range(4)]
    pm=any(tuple(sorted((0,b))) in E and tuple(sorted((c,d))) in E
           for b,c,d in ((1,2,3),(2,1,3),(3,1,2)))
    D=sum((d-1)*(d-2)//2 for d in deg)
    if not pm:
        assert D>=1; nonmatching+=1; histogram[D]=histogram.get(D,0)+1

# Connected shapes by growing an arbitrary spanning tree; no rotation quotient.
shapes={(zero,)}; counts=[1]
for n in range(2,5):
    newer=set()
    for S in shapes:
        occupied=set(S)
        for x in S:
            for d in G:
                y=add(x,d)
                if y not in occupied: newer.add(canon(S+(y,)))
    shapes=newer; counts.append(len(shapes))
core={S for S in shapes if matching(S)}

# Nine actual bond species, with exactly the anchor convention stated in the proof.
bondtypes=[('E',i) for i in range(3)]+[('T',(i,j,eta)) for i,j in combinations(range(3),2) for eta in (1,-1)]
def bond(a,x):
    kind,dat=bondtypes[a]
    if kind=='E': return tuple(sorted((sub(x,e[dat]),add(x,e[dat]))))
    i,j,eta=dat;return tuple(sorted((x,add(x,add(e[i],scale(eta,e[j]))))))
def identify(S):
    a,b=sorted(S);d=sub(b,a);axes=[j for j in range(3) if d[j]]
    if len(axes)==1:
        axis=axes[0];assert abs(d[axis])==2
        return axis,tuple((u+v)//2 for u,v in zip(a,b))
    assert len(axes)==2 and all(abs(d[j])==1 for j in axes)
    i,j=axes
    if d[i]<0: a,b=b,a;d=scale(-1,d)
    return bondtypes.index(('T',(i,j,d[j]))),a

holes=[]; image=set(); fixed=0; overlapping=0
for a,b in product(range(9),repeat=2):
    one=bond(a,zero)
    for r in product(range(-4,5),repeat=3):
        two=bond(b,r);overlap=bool(set(one)&set(two))
        cross=any(sub(v,u) in G for u in one for v in two)
        if overlap or cross:
            holes.append((r,a,b))
            fixed+=r==zero and a==b
            if overlap: overlapping+=1
            else: image.add(canon(one+two))
assert image==core

# Exact Gaussian-integer symbol check. All matrix entries below are scaled by 12.
roots=((1,0),(0,1),(-1,0),(0,-1))
def gadd(a,b): return a[0]+b[0],a[1]+b[1]
def gscale(n,a): return n*a[0],n*a[1]
def gmul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0],-a[1]
pairactions=[action(bond(b,zero)) for b in range(9)]
symbol_checks=0
for q in product(range(4),repeat=3):
    ell=2*sum(1-roots[k][0] for k in q)
    v=[(0,0)]*9
    for a,(kind,dat) in enumerate(bondtypes):
        if kind=='T':
            i,j,eta=dat
            v[a]=gscale(-eta,gadd(roots[(eta*q[j])%4],roots[q[i]]))
    for b in range(9):
        actual={}
        for S,(mu,ta) in pairactions[b].items():
            a,x=identify(S)
            phase=roots[(-sum(k*y for k,y in zip(q,x)))%4]
            oldmu,oldta=actual.get(a,((0,0),(0,0)))
            actual[a]=(gadd(oldmu,gscale(mu,phase)),gadd(oldta,gscale(ta,phase)))
        for a in range(9):
            pe=4*((3 if a==b else 0)-1) if a<3 and b<3 else 0
            outer=(0,0)
            if a>=3 and b>=3 and bondtypes[a][1][:2]==bondtypes[b][1][:2]:
                outer=gscale(3,gmul(v[a],conj(v[b])))
            predicted=(gadd((24*(a==b)-2*pe,0),gscale(-1,outer)),
                       gadd((ell*pe,0),gscale(ell,outer)))
            assert actual.get(a,((0,0),(0,0)))==predicted,(q,a,b,actual.get(a),predicted)
            symbol_checks+=1

# Literal source and incoming-channel witness, not a quotient norm.
S=((0,0,0),(2,0,0),(4,0,0),(6,0,0))
T=tuple(sorted(((0,0,0),(3,-1,1),(3,1,1),(6,0,0))))
U=tuple(sorted(((0,0,0),(3,-1,0),(3,1,0),(6,0,0))))
HS=action(S);HT=action(T)
assert HS[T]==(0,4) and HT[S]==(0,4)
assert HS[U]==(8,-24)
def edgeu(a,b):
    d=sub(a,b)
    return 1 if d in (scale(2,e[0]),scale(-2,e[0])) else -1 if d in (scale(2,e[1]),scale(-2,e[1])) else 0
def phi(S):
    return sum(edgeu(S[0],S[b])*edgeu(S[c],S[d]) for b,c,d in ((1,2,3),(2,1,3),(3,1,2)))
incoming=(sum(mu*phi(X) for X,(mu,ta) in HT.items()),sum(ta*phi(X) for X,(mu,ta) in HT.items()))
assert incoming==(0,4)
closed={X:c for X,c in HS.items() if not matching(X) and sum(c)!=0}
for X,c in closed.items(): assert action(X).get(S,(0,0))==c
closednorm=sum((Fraction(mu+ta,12))**2 for mu,ta in closed.values())
assert closednorm==Fraction(68,9)

# Full physical core, reconstructed from this independent action implementation.
entries=0; boundaryQ=set();boundaryE=set();maxspan=0
for j,S in enumerate(sorted(core)):
    column={}
    for X,(mu,ta) in action(S).items(): plusentry(column,canon(X),mu,ta)
    column={X:c for X,c in column.items() if c!=(0,0)}
    entries+=len(column)
    for X,c in column.items():
        maxspan=max(maxspan,max(max(v[k] for v in X)-min(v[k] for v in X) for k in range(3)))
        if X not in core:
            (boundaryE if matching(X) else boundaryQ).add(X)
    if j%64==0:
        assert time.monotonic()-t0<115
        assert not (runtime/'STOP_REQUESTED.json').exists()

result={'independence':'No author implementation read, imported or executed; expected printed counts were known only after frozen precomparison.',
 'graphs':{'nonmatching':nonmatching,'D_histogram':histogram,'connected_growth_counts':counts,'physical_core':len(core)},
 'free_hole':{'ordered':len(holes),'exchange_fixed':fixed,'symmetric':(len(holes)+fixed)//2,'ordered_overlaps':overlapping,'disjoint_hole_image_equals_core':True},
 'symbol':{'momenta':64,'Gaussian_integer_matrix_entries':symbol_checks,'all_equal':True},
 'witness':{'literal_shifted_mu_tau_over_12':HS[T],'literal_unshifted_mu_tau_over_12':HS[U],
            'H_CE_squared_at_T_mu_tau_over_12':incoming,'closed_nonzero_words_mu_tau_1':len(closed),
            'literal_closed_squared_norm':str(closednorm),'Hermiticity_columns':len(closed)},
 'core_action':{'nonzero_coefficient_pairs':entries,'Q_boundary_shapes':len(boundaryQ),'exterior_boundary_shapes':len(boundaryE),'maximum_coordinate_span':maxspan},
 'resources':{'wall_seconds':time.monotonic()-t0,'cpu_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
