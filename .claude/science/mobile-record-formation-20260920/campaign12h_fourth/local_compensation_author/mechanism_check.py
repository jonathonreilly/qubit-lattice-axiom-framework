"""Exact rational sum-of-squares and all-mark rotor rate controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import importlib.util,hashlib,json
D=Path(__file__).resolve().parent;p=D/'local_compensation_check.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='6c8abe653492d44369ab94e9aa07af2d7215eb13f0d96a8c7e97ba446fb8485a'
spec=importlib.util.spec_from_file_location('local_controls',p);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
m=c.m

def clean(v):return {s:a for s,a in v.items() if a}
def add(v,w,scale=Fraction(1)):
    r=defaultdict(Fraction,v)
    for s,a in w.items():r[s]+=scale*a
    return clean(r)

def F(v,a,outward,resource):
    result=defaultdict(Fraction)
    for (q,E),amp in v.items():
        for qq,shift in m.paths.legal_hops(q,m.edges):
            if outward and not (q[a]!=0 and qq[a]==0):continue
            if not outward and not (q[a]==0 and qq[a]!=0):continue
            field=m.paths.add(E,shift)
            if resource=='spin1' and max(map(abs,field))>1:continue
            # Every allowed normalized spin-one shift has exact amplitude1.
            result[qq,field]+=amp
    return clean(result)

def square_controls():
    rows=[];epsilon=Fraction(1,7)
    seeds={'initial_four':{(c.q0,c.zero):Fraction(1)},
           'resolved_first':{s:Fraction(int(v)) for s,v in c.first_vector().items()}}
    for resource in ['rotor','spin1']:
        for name,seed in seeds.items():
            psi=seed
            for a in m.aset:psi=add(psi,F(psi,a,True,resource),epsilon)
            ppart={s:v for s,v in psi.items() if m.grade(s[0])==0}
            assert ppart==seed
            row={'resource':resource,'seed':name,'epsilon':str(epsilon),'dressed_support':len(psi)}
            for a in m.aset:
                vacancy={s:v for s,v in psi.items() if s[0][a]==0}
                assert not add(vacancy,F(psi,a,True,resource),-epsilon)
                assert not F(F(psi,a,True,resource),a,True,resource)
                for b in m.aset:
                    if a==b:continue
                    left=F(F(psi,a,True,resource),b,True,resource)
                    right=F(F(psi,b,True,resource),a,True,resource)
                    assert left==right
            h={s:Fraction(m.grade(s[0]))*v for s,v in psi.items()}
            for a in m.aset:
                h=add(h,F(psi,a,True,resource),-epsilon)
                h=add(h,F(psi,a,False,resource),-epsilon)
                h=add(h,F(F(psi,a,True,resource),a,False,resource),epsilon**2)
            assert not clean(h)
            row.update(all_four_local_constraints_exact_zero=True,
                       direct_full_H_action_exact_zero=True,
                       outward_nilpotence_and_pair_commutation_verified=True)
            rows.append(row)
    return rows

def polynomial(v):
    groups=defaultdict(list);out=defaultdict(int)
    for (q,E),a in v.items():
        assert a==int(a);groups[q].append((E,int(a)))
    for terms in groups.values():
        for x,n in terms:
            for y,k in terms:out[tuple(b-a for a,b in zip(x,y))]+=n*k
    return dict(out)

def rate_controls():
    rows=[]
    for coherent in [False,True]:
        for edge in range(12):
            for signs in ([[-1,1]] if coherent else [[-1],[1]]):
                first=c.first_vector(edge,signs);norm2=4 if coherent else 2
                assert polynomial(first)=={c.zero:norm2}
                total=defaultdict(int)
                for e2 in range(12):
                    for sigma in [-1,1]:
                        v=defaultdict(int)
                        for (q,E),a in first.items():
                            for qq,de in m.paths.effective_paths(q,m.edges,m.aset,e2,[sigma]):
                                v[qq,m.paths.add(E,de)]+=int(a)
                        for shift,a in polynomial(v).items():total[shift]+=a
                total={s:a for s,a in total.items() if a}
                assert total[c.zero]==8*norm2 and len(total)==3
                loops=[s for s in total if s!=c.zero]
                assert loops[1]==tuple(-x for x in loops[0])
                assert all(total[s]==norm2 and sum(abs(x) for x in s)==4 for s in loops)
                for loop in loops:assert m.paths.gauss_difference(c.q0,c.q0,loop,m.edges)
                rows.append({'coherent_first':coherent,'first_edge':list(m.edges[edge]),
                             'first_signs':signs,'first_Gram':norm2,
                             'normalized_second_rate_over_kappa':{'identity':8,'loop':list(loops[0]),'loop_coefficient':1,'adjoint_coefficient':1},
                             'all_normalizable_fields_rate_bounds_over_kappa':[6,10]})
    return rows

def main():
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'exact_rational_sum_of_squares':square_controls(),
            'all_first_mark_exact_rotor_rate_polynomials':rate_controls(),
            'scope':'Exact finite rational/path identities. General operator and convergence statements use the accompanying proofs, not extrapolation of these controls.'}
    p=D/'MECHANISM_CONTROLS.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
