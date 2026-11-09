#!/usr/bin/env python3
"""Exact finite checks of local formation. This is not an axiom derivation.
Q arithmetic is adapted from the pinned previous joint-law diagnostic;
independence comes from the separate hand proof, not this shared arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import resource
import time

START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (50, 55))


def guard():
    assert time.monotonic()-START < 55, 'wall budget'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024*1024, 'RSS budget (macOS bytes)'


class Q:
    """Q(i,sqrt(2)), coefficients of 1,sqrt(2),i,i*sqrt(2)."""
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = (a.v if isinstance(a, Q) else tuple(map(F, (a,b,c,d))))

    def __add__(self, other):
        other = Q(other)
        return Q(*(x+y for x,y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return Q(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-Q(other))

    def __rsub__(self, other):
        return Q(other) - self

    def __mul__(self, other):
        other = Q(other)
        out = [F(0)]*4
        for j,x in enumerate(self.v):
            if not x:
                continue
            for k,y in enumerate(other.v):
                if not y:
                    continue
                ie, re = j//2+k//2, j%2+k%2
                out[(ie%2)*2+re%2] += x*y*((-1)**(ie//2))*(2**(re//2))
        return Q(*out)

    __rmul__ = __mul__

    def inverse(self):
        norm = self*self.conj()
        a,b,c,d = norm.v
        assert c == d == 0 and a*a-2*b*b != 0, 'nonzero field divisor'
        return self.conj()*Q(a/(a*a-2*b*b), -b/(a*a-2*b*b))

    def __truediv__(self, other):
        return self*Q(other).inverse()

    def __eq__(self, other):
        return self.v == Q(other).v

    def __hash__(self):
        return hash(self.v)

    def conj(self):
        a,b,c,d = self.v
        return Q(a,b,-c,-d)

    def nonnegative(self):
        a,b,c,d = self.v
        assert c == d == 0, 'expected real number'
        if a >= 0 and b >= 0:
            return True
        if a <= 0 and b <= 0:
            return a == b == 0
        return a*a >= 2*b*b if a >= 0 else 2*b*b >= a*a

    def serial(self):
        return [str(x) for x in self.v]



def clean(a):
    return {k:Q(v) for k,v in a.items() if v != 0}


def add(*matrices):
    out={}
    for a in matrices:
        for k,v in a.items(): out[k]=out.get(k,Q())+v
    return clean(out)


def scale(a,s):
    return clean({k:v*s for k,v in a.items()})


def mul(a,b):
    rows={}
    for (j,k),v in b.items(): rows.setdefault(j,[]).append((k,v))
    out={}
    for (i,j),v in a.items():
        for k,w in rows.get(j,[]): out[i,k]=out.get((i,k),Q())+v*w
    return clean(out)


def adj(a): return {(j,i):v.conj() for (i,j),v in a.items()}

def tr(a): return sum((v for (i,j),v in a.items() if i==j),Q())

def identity(d): return {(i,i):Q(1) for i in range(d)}

def outer(v): return clean({(i,j):a*b.conj() for i,a in v.items() for j,b in v.items()})

def sandwich(k,rho): return mul(mul(k,rho),adj(k))

def kron(a,b,db): return clean({(i*db+k,j*db+l):v*w for (i,j),v in a.items() for (k,l),w in b.items()})


I=identity(2)
X={(0,1):Q(1),(1,0):Q(1)}
Y={(0,1):Q(0,0,-1),(1,0):Q(0,0,1)}
Z={(0,0):Q(1),(1,1):Q(-1)}
PAULI=(X,Y,Z)
R=Q(0,F(1,2))
AXES=[(1,0,0),(0,1,0),(0,0,1),(R,0,R),(-R,0,R),(F(3,5),0,F(4,5)),(F(2,3),F(2,3),F(1,3))]
AXES=[tuple(Q(x) for x in n) for n in AXES]
SINGLET=outer({1:R,2:-R})
SITES={0:((1,0,0),(2,0,0)),1:((1,0,7),(2,0,7))}


def proj(n,a): return scale(add(I,*(scale(p,a*c) for p,c in zip(PAULI,n))),F(1,2))

def dot(n,m): return sum((a*b for a,b in zip(n,m)),Q())


def local_operators(n,sq,fault=None):
    d={}
    for i in range(8):
        ptr=i%4
        target=3-ptr if fault=='overwrite' and ptr in (1,2) else ptr
        d[4*(i//4)+target,i]=sq if ptr==0 else Q(1)
    js=[]
    for a,code in ((1,1),(-1,2)):
        js.append({(4*i+code,4*j):v for (i,j),v in proj(n,a).items()})
    return clean(d),js


def local_channel(rho,n,q,sq,fault=None):
    d,js=local_operators(n,sq,fault)
    return add(sandwich(d,rho),*(scale(sandwich(k,rho),1-q) for k in js))


def lift(k,wing): return kron(k,identity(8),8) if wing==0 else kron(identity(8),k,8)


def carrier_channel(rho,wing,n,q,sq):
    d,js=local_operators(n,sq)
    return add(sandwich(lift(d,wing),rho),*(scale(sandwich(lift(k,wing),rho),1-q) for k in js))


def pointer_code(records,wing):
    sites=SITES[wing]
    if all(s not in records for s in sites): return 0
    assert all(s in records for s in sites), 'complete local record block'
    code=2*records[sites[0]]+records[sites[1]]
    assert code in (1,2), 'legal filled pointer'
    return code


def encode(rho,records):
    pa,pb=pointer_code(records,0),pointer_code(records,1)
    def index(i): return (4*(i//2)+pa)*8+4*(i%2)+pb
    return {(index(i),index(j)):v for (i,j),v in rho.items()}


def branches(rho,records,wing,n,q,fault=None):
    if pointer_code(records,wing): return [(0,Q(1),rho,dict(records))]
    out=[]
    if q: out.append((0,Q(q),rho,dict(records)))
    for a,code in ((1,1),(-1,2)):
        k=kron(proj(n,a),I,2) if wing==0 else kron(I,proj(n,a),2)
        selected=sandwich(k,rho)
        probability=tr(selected)
        assert probability.nonnegative()
        weight=(1-q)*probability
        if weight==0: continue
        r=dict(records)
        r.update(zip(SITES[wing],(code//2,code%2)))
        assert all(r[s]==v for s,v in records.items()), 'append only records'
        state=scale(selected,probability.inverse())
        if fault=='frozen-condition' and wing==0: state=rho
        out.append((a,weight,state,r))
    assert sum((w for _,w,_,_ in out),Q())==1, 'normalized formation kernel'
    return out


def tree(rho,n,m,q,order,fault=None):
    reached=[(Q(1),rho,{})]
    for wing in order:
        expanded=[]
        for weight,state,records in reached:
            for _,w,new_state,new_records in branches(state,records,wing,(n,m)[wing],q,fault):
                expanded.append((weight*w,new_state,new_records))
        reached=expanded
    return reached


def ensemble(reached): return add(*(scale(encode(state,records),w) for w,state,records in reached))


def event_weight(reached,wing,outcome):
    code=1 if outcome==1 else 2
    return sum((w for w,_,r in reached if pointer_code(r,wing)==code),Q())


def serialized_map(a): return sorted((i,j,v.serial()) for (i,j),v in a.items())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fault',choices=['overwrite','frozen-condition','remote-setting'])
    fault=parser.parse_args().fault
    counts={'local_completeness':0,'matrix_unit_semigroup':0,'occupied_matrix_units_fixed':0,'local_trace_preservation':0,'setting_pairs':0,'record_histories':0,'permanent_reapplications':0}
    q=F(1,2)
    for n in AXES:
        d,js=local_operators(n,R,fault)
        total=add(mul(adj(d),d),*(scale(mul(adj(j),j),1-q) for j in js))
        assert total==identity(8), 'local completeness'
        counts['local_completeness']+=1
        for i,j in product(range(8),repeat=2):
            unit={(i,j):Q(1)}
            image=local_channel(unit,n,q,R,fault)
            if i%4 and j%4:
                assert image==unit, 'occupied pointer permanence'
                counts['occupied_matrix_units_fixed']+=1
            assert tr(image)==Q(int(i==j)), 'all-matrix-unit trace preservation'
            counts['local_trace_preservation']+=1
            composed=local_channel(image,n,q,R,fault)
            assert composed==local_channel(unit,n,F(1,4),Q(F(1,2)),fault), 'channel semigroup on coherences'
            counts['matrix_unit_semigroup']+=1
        guard()
    # A product input detects remote-setting dependence hidden by singlet marginals.
    product_zero={(0,0):Q(1)}
    marginals=[]
    for remote in (AXES[0],AXES[2]):
        local=remote if fault=='remote-setting' else AXES[2]
        first=branches(product_zero,{},0,local,q)
        marginals.append(sum((w for a,w,_,_ in first if a==1),Q()))
    assert marginals[0]==marginals[1], 'remote setting entered local formation'
    maximum_weights={}
    for n,m in product(AXES,repeat=2):
        initial=encode(SINGLET,{})
        direct_ab=carrier_channel(carrier_channel(initial,0,n,q,R),1,m,q,R)
        direct_ba=carrier_channel(carrier_channel(initial,1,m,q,R),0,n,q,R)
        assert direct_ab==direct_ba, 'disjoint local channels commute'
        ab=tree(SINGLET,n,m,q,(0,1),fault)
        ba=tree(SINGLET,n,m,q,(1,0),fault)
        assert ensemble(ab)==direct_ab==ensemble(ba), 'record-history conditional update'
        weights={}
        for w,state,records in ab:
            ca,cb=pointer_code(records,0),pointer_code(records,1)
            assert tr(state)==1 and w.nonnegative()
            if ca and cb:
                a=1 if ca==1 else -1; b=1 if cb==1 else -1
                expected=Q(F(1,16))*(1-a*b*dot(n,m))
                weights[a,b]=w/(Q(1-q)*Q(1-q))
            elif ca or cb: expected=Q(F(1,8))
            else: expected=Q(F(1,4))
            assert w==expected, 'clock and Born sector weights'
            for wing in (0,1):
                if pointer_code(records,wing):
                    again=branches(state,records,wing,AXES[1],q)
                    assert again==[(0,Q(1),state,records)], 'absorbing registered outcome'
                    counts['permanent_reapplications']+=1
            counts['record_histories']+=1
        assert event_weight(ab,0,1)==event_weight(ab,1,1)==Q(F(1,4)), 'no-signalling marginals'
        counts['setting_pairs']+=1
        maximum_weights[n,m]=weights
        guard()
    ns=[AXES[2],AXES[0]]; ms=[AXES[3],AXES[4]]
    chsh=Q()
    for x,y in product(range(2),repeat=2):
        correlation=sum((a*b*w for (a,b),w in maximum_weights[ns[x],ms[y]].items()),Q())
        chsh+=(1 if (x,y)!=(1,1) else -1)*correlation
    assert chsh==Q(0,-2), 'derived CHSH score'
    conditional=[]
    for a,w,state,records in branches(SINGLET,{},0,AXES[2],0):
        p=sum((v for b,v,_,_ in branches(state,records,1,AXES[2],0) if b==1),Q())
        conditional.append((a,p))
    assert conditional==[(1,Q(0)),(-1,Q(1))], 'full-history conditional collision'
    # The polynomial control agrees on z,x,y but fails the diagonal axis.
    t=R; h=(3*t-t*t*t)/2
    assert h!=t and -h==Q(0,F(-5,8)), 'conditional quantum effect inconsistency'
    # Positive but non-CP transposition fails on half of an entangled pair.
    partial_transpose={(2*(j//2)+i%2,2*(i//2)+j%2):v for (i,j),v in SINGLET.items()}
    phi_plus=outer({0:R,3:R})
    witness=tr(mul(phi_plus,partial_transpose))
    assert witness==Q(F(-1,2)), 'partial transpose negativity witness'
    # Complete record state needs preparation/operation order or an extra predictor.
    rho0={(0,0):Q(1)}
    history_zx=sandwich(proj(AXES[0],1),sandwich(proj(AXES[2],1),rho0))
    history_xz=sandwich(proj(AXES[2],1),sandwich(proj(AXES[0],1),rho0))
    normalized_zx=scale(history_zx,tr(history_zx).inverse())
    normalized_xz=scale(history_xz,tr(history_xz).inverse())
    z_probs=[tr(sandwich(proj(AXES[2],1),s)) for s in (normalized_zx,normalized_xz)]
    assert z_probs==[Q(F(1,2)),Q(1)], 'unordered history insufficiency'
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'exact finite formation diagnostics passed','counts':counts,'local_native_qubits':3,'two_wing_native_qubits':6,'carrier_dimension':64,'CHSH_signed_coefficients':chsh.serial(),'conditional_B_plus':[(a,p.serial()) for a,p in conditional],'polynomial_diagonal_expectation':(-h).serial(),'quantum_diagonal_expectation':(-t).serial(),'partial_transpose_witness':witness.serial(),'unordered_history_Z_plus':[p.serial() for p in z_probs],'no_event_q':'1/2','continuous_time_execution':False,'N5':{'element':'exact complex Kraus algebra','site':'two-site local pointer code and append-only R','mode':'no physical propagation mode simulated','block':'disjoint three-qubit detector channels with single-outcome intermediate sectors','lattice':'finite two-block embedding only'},'elapsed_seconds':time.monotonic()-START,'max_rss_host_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
