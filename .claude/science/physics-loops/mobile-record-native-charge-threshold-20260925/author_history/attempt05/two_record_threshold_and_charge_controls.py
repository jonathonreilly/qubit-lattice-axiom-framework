"""Personal exact primitive controls. No imported scientific runner or LP.

The rational trial was proposed in earlier saved explorations. This program
reconstructs its integer operator rows from primitive ordered star paths.
Only the Python standard library is used. Odd occupancy below is an auxiliary
algebraic kernel, not an added physical charge sector.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import argparse, hashlib, json, time

DEN=10**9
DEFICITS={(0,0,2):30355481,(0,0,4):0,(0,0,6):82543,
 (0,1,1):62454728,(0,1,3):592565,(0,1,5):257096,
 (0,2,2):1564788,(0,2,4):501938,(0,3,3):0,
 (1,1,2):2988879,(1,1,4):733404,(1,2,3):1227493,(2,2,2):0}

def neighbors(v,side=None):
    out=[]
    for axis in range(3):
        for step in (-1,1):
            w=list(v);w[axis]+=step
            if side:w[axis]%=side
            out.append(tuple(w))
    return sorted(set(out))

def active_pairs(b,side=None):
    return {tuple(sorted((a,c))) for a in neighbors(b,side)
            for shared in neighbors(a,side) for c in neighbors(shared,side) if c!=a}

def primitive_row(occupied,side=None):
    """Exact 2 S* S minus the local empty-occupancy scalar."""
    occupied=tuple(sorted(occupied));occ=set(occupied);answer=Counter();path_count=0
    pairs=set().union(*(active_pairs(b,side) for b in occupied))
    for a,c in sorted(pairs):
        paths=[(u,v) for u in neighbors(a,side) for v in neighbors(c,side) if u!=v]
        empty=Counter(tuple(sorted(path)) for path in paths)
        answer[occupied]-=2*sum(m*m for m in empty.values())
        intermediate=Counter(tuple(sorted((*occupied,u,v))) for u,v in paths if u not in occ and v not in occ)
        for word,forward in intermediate.items():
            wordset=set(word)
            for u,v in paths:
                if u in wordset and v in wordset:
                    target=tuple(b for b in word if b!=u and b!=v)
                    assert len(target)==len(occupied)
                    answer[target]+=2*forward
                    path_count+=forward
    answer={word:c for word,c in answer.items() if c}
    assert all(c>=0 for word,c in answer.items() if word!=occupied)
    return answer,len(pairs),path_count

def kind(x,side=None):
    d=[abs(b-a) for a,b in zip(*x)]
    if side:d=[min(v,side-v) for v in d]
    return tuple(sorted(d))

def trial_numerator(x,side=None):return DEN-DEFICITS.get(kind(x,side),0)

def classes(radius):
    return sorted({tuple(sorted(d)) for d in product(range(radius+1),repeat=3)
                   if 0<sum(d)<=radius and sum(d)%2==0})

def point_pair(d,side=None,origin=(1,0,0)):
    other=tuple(a+b for a,b in zip(origin,d))
    if side:other=tuple(v%side for v in other)
    return tuple(sorted((origin,other)))

def group(row,side=None):
    grouped=Counter()
    for y,c in row.items():grouped[kind(y,side)]+=c
    return dict(grouped)

def orbit_size(d):
    return len({tuple(s*v for s,v in zip(sign,p)) for p in set(permutations(d)) for sign in product((-1,1),repeat=3)})

def charge_controls(side):
    vertices=list(product(range(side),repeat=3));A=[v for v in vertices if sum(v)%2==0]
    n=len(A);m=n+2;counts=Counter();samples=[]
    for a in A:
        ns=neighbors(a,side)
        for b in ns:
            for sigma in (-1,1):
                norm=0;projected_times_m=0
                for c in ns:
                    if c==b:continue
                    x=tuple(sorted((b,c)));minus=b if sigma==1 else a
                    qexc={a:sigma-1,b:-sigma,c:1};qexc={v:q for v,q in qexc.items() if q}
                    div=Counter()
                    for (left,right),value in { (a,b):sigma,(a,c):-1 }.items():
                        div[left]+=value;div[right]-=value
                    assert {v:q for v,q in div.items() if q}==qexc and sum(qexc.values())==0
                    occupied=A+list(x)
                    assert minus in occupied and len(occupied)==m
                    # A single colored word has norm1 and sum of its amplitudes1.
                    amplitudes={minus:1};norm+=sum(v*v for v in amplitudes.values())
                    projected_times_m+=sum(amplitudes.values())**2
                    counts['resolved_primitive_outputs']+=1
                    counts['minus_on_B' if minus in x else 'minus_on_A']+=1
                assert Fraction(projected_times_m,m*norm)==Fraction(1,m)
                counts['resolved_edge_sign_marks']+=1
            # At a flat connection only: two orthogonal minus locations, equal amplitude.
            norm=2*(len(ns)-1);projected_times_m=4*(len(ns)-1)
            assert Fraction(projected_times_m,m*norm)==Fraction(2,m)
            counts['flat_coherent_edge_controls']+=1
    b=next(v for v in vertices if sum(v)%2==1)
    c=next(v for v in vertices if sum(v)%2==1 and v!=b)
    occupied=A+[b,c]
    for label,f in [('total',lambda v:1),('one_A',lambda v:int(v==A[0])),
                    ('one_B',lambda v:int(v==b)),('both_B',lambda v:int(v in (b,c))),
                    ('coordinate',lambda v:v[0]-2*v[1]+3*v[2])]:
        words=[f(b)+f(c)-2*f(minus) for minus in occupied]
        mean=Fraction(sum(words),m);variance=Fraction(sum(w*w for w in words),m)-mean*mean
        expected=Fraction(4*sum(f(v)**2 for v in occupied),m)-4*Fraction(sum(f(v) for v in occupied),m)**2
        assert variance==expected
        assert mean==f(b)+f(c)-2*Fraction(sum(f(v) for v in occupied),m)
        samples.append({'test':label,'charge_mean':str(mean),'charge_variance':str(variance)})
    return {'side':side,'A_sites':n,'occupied_sites_after_one_birth':m,
            'uniform_minus_mean_A_excitation':str(Fraction(-2,m)),
            'uniform_minus_mean_occupied_B_charge':str(1-Fraction(2,m)),
            'uniform_minus_probability_minus_on_B':str(Fraction(2,m)),
            'resolved_first_birth_color_line_weight':str(Fraction(1,m)),
            'flat_coherent_first_birth_color_line_weight':str(Fraction(2,m)),
            'counts':dict(counts),'test_charge_rows':samples}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();rows=[];raws={}
    for d in classes(10):
        x=point_pair(d);raw,npairs,npaths=primitive_row(x);raws[d]=raw
        g=group(raw);residual=sum(c*trial_numerator(y) for y,c in raw.items())-12096*trial_numerator(x)
        assert residual<=0
        rows.append({'type':d,'active_A_pairs':npairs,'ordered_out_return_paths':npaths,
          'row_sum':sum(raw.values()),'target_count':len(raw),'trial_residual_numerator':residual,
          'grouped_integer_row':[[list(k),v] for k,v in sorted(g.items())]})
    assert len(rows)==37 and len(DEFICITS)==13 and set(DEFICITS)==set(classes(6))
    near=[r for r in rows if sum(r['type'])<=4]
    defect=sum((r['row_sum']-12096)*orbit_size(tuple(r['type'])) for r in near)
    assert defect==-1548
    periodic=[]
    for side in (24,26):
        ds=classes(6)+[(0,0,8),(0,0,10),(0,0,side//2 if side%4==0 else side//2-1),(2,4,6)]
        for d in ds:
            for origin in ((1,0,0),(side-1,side-2,side-2)):
                x=point_pair(d,side,origin);raw,npairs,npaths=primitive_row(x,side)
                g=group(raw,side);residual=sum(c*trial_numerator(y,side) for y,c in raw.items())-12096*trial_numerator(x,side)
                assert residual<=0
                if sum(d)<=6:assert g==group(raws[d])
                if sum(d)>4:assert sum(raw.values())==12096
                periodic.append({'side':side,'type':d,'origin':origin,'row_sum':sum(raw.values()),
                                 'trial_residual_numerator':residual,'target_count':len(raw),
                                 'near_full_grouped_row_equal_unwrapped':sum(d)<=6})
    # Separate auxiliary one-occupancy contribution and exact Fourier curvature.
    origin=(1,0,0);single,_,singlepaths=primitive_row((origin,));kernel={tuple(b-a for a,b in zip(origin,y[0])):c for y,c in single.items()}
    assert sum(kernel.values())==6048
    assert all(kernel.get(tuple(-z for z in d))==c for d,c in kernel.items())
    second=[[sum(c*d[i]*d[j] for d,c in kernel.items()) for j in range(3)] for i in range(3)]
    assert all(second[i][j]==(second[0][0] if i==j else 0) for i in range(3) for j in range(3))
    far=(origin,(21,20,20));raw,_,_=primitive_row(far);expected=Counter()
    for i in (0,1):
        for d,c in kernel.items():
            moved=tuple(a+b for a,b in zip(far[i],d));target=tuple(sorted((moved,far[1-i])))
            expected[target]+=c
    assert raw=={y:c for y,c in expected.items() if c}
    # Exact off-diagonal reciprocity on representative changed occupancy targets.
    reciprocity=[]
    for d in classes(6):
        x=point_pair(d);raw=raws[d];targets=[(y,c) for y,c in sorted(raw.items()) if y!=x]
        for y,c in targets[::max(1,len(targets)//3)]:
            reverse,_,_=primitive_row(y);assert reverse.get(x)==c
            reciprocity.append({'input_type':d,'target':y,'both_coefficients':c})
    result={'scope':'Personal exact flat occupancy supersolution and charge/color controls. Not independent review, a finite-g binding theorem, a physical projector, charge calibration or particle identification.',
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'imported_scientific_helpers':[],'denominator':DEN,
      'deficits':[[list(k),v] for k,v in sorted(DEFICITS.items())],
      'unwrapped_rows':rows,'near_total_row_defect':defect,'periodic_controls':periodic,
      'reciprocity_controls':reciprocity,
      'auxiliary_one_occupancy_kernel':[[list(k),v] for k,v in sorted(kernel.items())],
      'auxiliary_kernel_row_sum':sum(kernel.values()),'auxiliary_kernel_second_moment':second,
      'auxiliary_ordered_paths':singlepaths,'far_pair_equals_two_auxiliary_contributions':True,
      'charge_controls':[charge_controls(side) for side in (2,4,6)],
      'elapsed_seconds':time.perf_counter()-start}
    with Path(args.output).open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('unwrapped_rows','periodic_controls','reciprocity_controls','auxiliary_one_occupancy_kernel')},indent=2))

if __name__=='__main__':main()
