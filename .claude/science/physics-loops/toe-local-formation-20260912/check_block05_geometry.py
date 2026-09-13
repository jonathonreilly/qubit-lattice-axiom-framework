"""Literal small-torus incidence controls, not an all-volume proof or physics solve."""
from itertools import combinations, permutations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import hashlib, json, time

started=time.perf_counter()
L=8
v=(0,0,0)
def neighbor(x,a,sgn):
    y=list(x); y[a]=(y[a]+sgn)%L; return tuple(y)
def edge(x,y): return tuple(sorted((x,y)))
def star(x): return frozenset(edge(x,neighbor(x,a,s)) for a in range(3) for s in (-1,1))
def faces_of_edge(e):
    x,y=e
    a=next(i for i in range(3) if x[i]!=y[i])
    out=[]
    for b in range(3):
        if b==a: continue
        for s in (-1,1):
            xb,yb=neighbor(x,b,s),neighbor(y,b,s)
            out.append(tuple(sorted((e,edge(x,xb),edge(y,yb),edge(xb,yb)))))
    assert len(set(out))==4
    return out
checks=[]
def require(name,p):
    if not p: raise AssertionError(name)
    checks.append(name)

def incidence_pairings(occ):
    # Repeated occurrences stay literal here; dedup only equivalent pair sets.
    if not occ:
        yield (); return
    first=occ[0]
    for j in range(1,len(occ)):
        other=occ[j]
        if first==other or not set(first).intersection(other): continue
        pair=tuple(sorted((first,other)))
        rest=occ[1:j]+occ[j+1:]
        for tail in incidence_pairings(rest):
            yield tuple(sorted((pair,)+tail))

def analyse(name,w):
    sv,sw=star(v),star(w)
    target=sv^sw
    adjacent=edge(v,w) in sv
    boundary=tuple(sorted(target))
    families=[]
    if not adjacent:
        pairsets=set(incidence_pairings(boundary))
        require(name+'_far_pairsets',len(pairsets)==225)
        families=[('boundary',pairsets)]
        bridges=[]
    else:
        left=set().union(*[set(e) for e in sv if e not in sw])
        right=set().union(*[set(e) for e in sw if e not in sv])
        bridges=sorted({edge(x,y) for x in left for y in right
                        if any(y==neighbor(x,a,s) for a in range(3) for s in (-1,1))
                        and edge(x,y) not in target})
        require(name+'_five_literal_bridges',len(bridges)==5)
        for b in bridges:
            pairsets=set(incidence_pairings(tuple(sorted(boundary+(b,b)))))
            expected=225 if b==edge(v,w) else 9
            require(name+'_bridge_pairsets_'+str(b),len(pairsets)==expected)
            families.append((str(b),pairsets))
        for b in boundary:
            require(name+'_triple_boundary_impossible_'+str(b),
                    not set(incidence_pairings(tuple(sorted(boundary+(b,b))))))
    all_edges=sorted(set(boundary).union(bridges))
    index={e:i for i,e in enumerate(all_edges)}
    face_list=sorted(set(f for e in all_edges for f in faces_of_edge(e)))
    fi={f:i for i,f in enumerate(face_list)}
    edge_flux={e:sum(1<<fi[f] for f in faces_of_edge(e)) for e in all_edges}
    def mask_of(edges): return sum(1<<index[e] for e in edges)
    mv,mw,mt=mask_of(sv),mask_of(sw),mask_of(target)
    @lru_cache(None)
    def flux(mask):
        z=0
        for e,i in index.items():
            if mask>>i&1: z^=edge_flux[e]
        return z
    census=Counter(); proper=set(); noncut_counts=Counter(); by_family=[]
    for label,pairsets in families:
        local=Counter()
        for ps in sorted(pairsets):
            pm=[mask_of(p) for p in ps]
            require_distinct=len(set(pm))==6
            if not require_distinct: raise AssertionError(('pair labels repeated',name,label,ps))
            for order in permutations(pm):
                mask=0; cuts=[]
                for j,p in enumerate(order,1):
                    mask^=p
                    if j==6: continue
                    proper.add(mask)
                    if flux(mask)==0:
                        if mask not in (mv,mw) or j!=3:
                            raise AssertionError(('unexpected proper cut',name,mask,j))
                        cuts.append(j)
                    else:
                        noncut_counts[flux(mask).bit_count()]+=1
                if mask!=mt: raise AssertionError('wrong target')
                kind='singleton' if cuts else 'mixed'
                local[kind]+=1
        census.update(local)
        by_family.append({'label':label,'pair_sets':len(pairsets),**local})
    require(name+'_singleton_count',census['singleton']==16200)
    require(name+'_word_count',sum(census.values())==(187920 if adjacent else 162000))
    require(name+'_mixed_count',census['mixed']==(171720 if adjacent else 145800))
    require(name+'_every_mixed_prefix_has_bad_face',min(noncut_counts)>0)
    if not adjacent: require(name+'_proper_subset_count',len(proper)==1022)
    # A geometry-only missed-history mutation has a concrete nonempty complement.
    require(name+'_dropping_mixed_loses_actual_words',census['mixed']>census['singleton'])
    return {'centers':[v,w],'boundary_size':len(boundary),'families':by_family,
            'word_counts':dict(census),'proper_masks':len(proper),
            'proper_masks_sha256':hashlib.sha256(','.join(map(str,sorted(proper))).encode()).hexdigest(),
            'noncut_prefix_bad_face_counts':dict(sorted(noncut_counts.items()))}

out={'scope':'same-agent exact L8 incidence support; no native resolvent or infinite-volume enumeration',
     'L':L,'far':analyse('far',(3,0,0)), 'adjacent':analyse('adjacent',(1,0,0))}
# The small-cut lemma's algebra is separately checked on integer projections.
for p in range(7):
    for q in range(7-p):
        for r in range(7-p-q):
            if p*q*r>8: raise AssertionError('projection product')
require('integer_projection_product_max8',True)
out.update(check_groups=len(checks),checks=checks,seconds=time.perf_counter()-started)
Path(__file__).with_name('BLOCK05_GEOMETRY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('scope','check_groups','seconds')},indent=2))
print(json.dumps({k:{j:out[k][j] for j in ('word_counts','proper_masks')} for k in ('far','adjacent')},indent=2))
