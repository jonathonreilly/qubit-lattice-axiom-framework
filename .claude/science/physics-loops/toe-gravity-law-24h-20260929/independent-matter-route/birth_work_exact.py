"""Exact full-original-first-mark energy calculation on cubic integer rotors.
Independent implementation of q/E words and the supplied F and j moves.
No one-pair Hamiltonian projection or substituted birth observable is used.
All arithmetic integers or Fraction; infinite-lattice locality reduction.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

DIRS = tuple(tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (-1, 1))
ORIGIN = (0,0,0)
OMEGA = ((), ())
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def even(a): return sum(a)%2 == 0
def nb(a): return tuple(add(a,d) for d in DIRS)
def default(a): return int(even(a))
def canonical(q,e):
    return (tuple(sorted((v,x) for v,x in q.items() if x != default(v))),
            tuple(sorted((ab,x) for ab,x in e.items() if x)))
def unpack(s): return dict(s[0]), dict(s[1])
def charge(q,v): return q.get(v,default(v))
def F(s,a):
    q,e = unpack(s); v = charge(q,a)
    if not v: return []
    ans=[]
    for b in nb(a):
        if charge(q,b): continue
        q2,e2=q.copy(),e.copy(); q2[a]=0; q2[b]=v
        e2[a,b]=e2.get((a,b),0)-v
        ans.append(canonical(q2,e2))
    return ans

def J(s,a,b,sigma):
    q,e=unpack(s)
    if charge(q,a) or charge(q,b): return None
    q[a]=sigma; q[b]=-sigma; e[a,b]=e.get((a,b),0)+sigma
    return canonical(q,e)

def birth(a,b,sigmas):
    out=Counter()
    for sigma in sigmas:
        for t in F(OMEGA,a):
            y=J(t,a,b,sigma)
            if y is not None: out[y]+=1
    return out

def gauss(s):
    q,e=unpack(s); div=Counter()
    for (a,b),v in e.items(): div[a]+=v; div[b]-=v
    return all(div[v] == charge(q,v)-default(v) for v in set(q)|set(div))

def D(s):
    q,e=unpack(s)
    return sum(v*(v-charge(q,a)) for (a,b),v in e.items() if charge(q,b)==0)

def partners(a):
    return {c for b in nb(a) for c in nb(b)}-{a}

def candidate_pairs(vec,halo=0):
    vertices={v for s in vec for v,c in s[0]}|{v for s in vec for ab,c in s[1] for v in ab}
    active={a for v in vertices for a in ((v,) if even(v) else nb(v))}
    for _ in range(halo): active |= {c for a in active for c in partners(a)}
    return sorted({tuple(sorted((a,c))) for a in active for c in partners(a)})

def apply_pair(vec,a,c):
    out=Counter()
    for s,v in vec.items():
        for u in F(s,a):
            for t in F(u,c): out[t]+=v
    return out

def norm2(vec): return sum(v*v for v in vec.values())

def energy_change(vec,halo=0):
    norm=norm2(vec); total=0; rows=[]
    assert all(gauss(s) and D(s)==0 for s in vec)
    for a,c in candidate_pairs(vec,halo):
        out=apply_pair(vec,a,c)
        vacuum_count=36-len(set(nb(a))&set(nb(c)))
        excess=norm2(out)-norm*vacuum_count
        total-=2*excess
        if excess: rows.append({'a':a,'c':c,'S_norm2':norm2(out),'vacuum_count':vacuum_count,'norm_excess':excess})
    return Fraction(total,norm),rows

def main():
    edge=(1,0,0); modes={'minus':(-1,), 'plus':(1,), 'coherent':(-1,1)}
    result={}
    for name,sigmas in modes.items():
        vec=birth(ORIGIN,edge,sigmas)
        delta,rows=energy_change(vec)
        delta_halo,_=energy_change(vec,1)
        assert delta==delta_halo
        assert len(vec)==(10 if name=='coherent' else 5)
        assert all(c==1 for c in vec.values())
        # Opposite ordering is equal for every pair, by independent output words.
        for a,c in candidate_pairs(vec):
            assert apply_pair(vec,a,c)==apply_pair(vec,c,a)
        result[name]={'norm2':norm2(vec),'electric_energy':0,'delta_H4':str(delta),
                      'changed_pairs':len(rows),'candidate_pairs':len(candidate_pairs(vec)),
                      'halo_candidate_pairs':len(candidate_pairs(vec,1)), 'pair_rows':rows}
        print(name,'norm2',norm2(vec),'delta_D',0,'delta_H4',delta,'changed_pairs',len(rows),flush=True)
    # Covariance checks rotate the actual preparation and mark together.
    for edge in DIRS:
        for name,sigmas in modes.items():
            val,_=energy_change(birth(ORIGIN,edge,sigmas))
            assert str(val)==result[name]['delta_H4']
    # Resolve the exact off-diagonal energy contribution between original signs.
    vm=birth(ORIGIN,(1,0,0),(-1,));vp=birth(ORIGIN,(1,0,0),(1,))
    cross=0
    for a,c in candidate_pairs(vm+vp):
        ym,yp=apply_pair(vm,a,c),apply_pair(vp,a,c)
        cross-=2*sum(v*yp.get(s,0) for s,v in ym.items())
    coherent_from_parts=(5*Fraction(result['minus']['delta_H4'])+5*Fraction(result['plus']['delta_H4'])+2*cross)/10
    assert coherent_from_parts==Fraction(result['coherent']['delta_H4'])
    result['cross_unnormalized_H4']=cross
    # There are 6N edge channels, two resolved signs each.
    result['resolved_power_per_kappa_delta_N']=str(30*(Fraction(result['minus']['delta_H4'])+Fraction(result['plus']['delta_H4'])))
    result['coherent_power_per_kappa_delta_N']=str(60*Fraction(result['coherent']['delta_H4']))
    print('cross_unnormalized_H4',cross)
    print('resolved d<E>/dt /(kappa*delta*N)',result['resolved_power_per_kappa_delta_N'])
    print('coherent d<E>/dt /(kappa*delta*N)',result['coherent_power_per_kappa_delta_N'])
    print('TOTAL: PASS=6 FAIL=0 (first states; full energy; locality halo; F ordering; cubic preparation; coherent interference)')
    Path(__file__).with_name('birth_work_exact.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
