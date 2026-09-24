#!/usr/bin/env python3
"""Disclosed root finite-matter and SI arithmetic controls; no empirical fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md')
ROOT_CONTROL_SOURCES = [('prepared-probe-dynamics-personal/flat_matter_controls.py', 'ce3c7aa5e31bfb78231b4cd4ae746a97878fa39da6ae08fc24ab63d14db3c7d9'), ('prepared-probe-output-energy-personal/output_energy_controls.py', '8d70c1821496c04cf98b066e0186fc6aa544c5f3f06bc97b312dabcc1e9a0eee'), ('observation-unit-bridge-personal/unit_conversions.py', 'cad001b23a6fd9c896ee978a34e7320f6cb0e3ae98d8f46f6ad61652a1af5fb7')]
RESULT_PATH = 'outputs/prepared_probe_physical_limits_20260924/PROBE_PHYSICAL_LIMITS_RESULTS.json'
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json,time
import mpmath as mp

def input_control(side):
    vertices=list(product(range(side),repeat=3));index={v:i for i,v in enumerate(vertices)}
    bits=[1<<i for i in range(len(vertices))]
    A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    def near(i):
        v=vertices[i];out=[]
        for k in range(3):
            for s in (-1,1):
                w=list(v);w[k]=(w[k]+s)%side;out.append(index[tuple(w)])
        return out
    adj={i:near(i) for i in range(len(vertices))}
    mask=sum(bits[i] for i in A)
    def location(v):return index[tuple(x%side for x in v)]
    a,d,h,c,e,b=map(location,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0),(-1,0,0)])
    fixed=list(map(location,[(0,-1,0),(0,0,1),(0,0,-1)]))
    minus=bits[d]|bits[h]
    common_plus=(mask^minus)|sum(bits[i] for i in fixed)
    initial=[(common_plus|bits[v],minus) for v in (c,e)]
    pairs=set()
    for x in A:
        for y in adj[x]:
            for z in adj[y]:
                if x<z:pairs.add((x,z))
    pairs=sorted(pairs)
    def hop(state,src,dst):
        p,n=state
        if not ((p|n)&bits[src]) or (p|n)&bits[dst]:return None
        if p&bits[src]:return p^bits[src]^bits[dst],n
        return p,n^bits[src]^bits[dst]
    def step(vector,src,dests,inward=False):
        out=defaultdict(int)
        for q,w in vector.items():
            for v in dests:
                r=hop(q,v,src) if inward else hop(q,src,v)
                if r is not None:out[r]+=w
        return dict(out)
    def pair_action(q,x,z):
        first=step({q:1},x,adj[x]);forward=step(first,z,adj[z])
        back=step(forward,z,adj[z],True);out=step(back,x,adj[x],True)
        assert out.get(q,0)==sum(w*w for w in forward.values())
        return out
    base_scalar=0
    for x,z in pairs:
        r=len(set(adj[x])&set(adj[z]));base_scalar-=2*(36+r*(r-2))
    actions=[];active_counts=[]
    for q in initial:
        result=defaultdict(int);active=0
        for x,z in pairs:
            neighborhood=set(adj[x])|set(adj[z])
            if not any((q[0]|q[1])&bits[v] for v in neighborhood) and not (q[1]&(bits[x]|bits[z])):
                r=len(set(adj[x])&set(adj[z]));result[q]+=-2*(36+r*(r-2))
            else:
                active+=1
                for f,value in pair_action(q,x,z).items():result[f]+=-2*value
        actions.append(dict(result));active_counts.append(active)
    assert actions[0].get(initial[1],0)==actions[1].get(initial[0],0)
    w=defaultdict(int)
    for sign,out in zip((1,-1),actions):
        for q,c0 in out.items():w[q]+=sign*c0
    w={q:c0 for q,c0 in w.items() if c0}
    mean=Fraction(w.get(initial[0],0)-w.get(initial[1],0),2)
    square=Fraction(sum(c0*c0 for c0 in w.values()),2)
    variance=square-mean*mean
    def mark(vector,sigma):
        moved=step(vector,a,adj[a]);out=defaultdict(int)
        for (p,n),value in moved.items():
            if (p|n)&(bits[a]|bits[b]):continue
            if sigma==1:r=(p|bits[a],n|bits[b])
            else:r=(p|bits[b],n|bits[a])
            out[r]+=value
        return {q:c0 for q,c0 in out.items() if c0}
    assert not mark({initial[0]:1,initial[1]:-1},1)
    leak={}
    for sigma in (-1,1):
        bw=mark(w,sigma)
        leak[str(sigma)]={'norm_squared':str(Fraction(sum(x*x for x in bw.values()),2)),
                          'output_words':len(bw)}
    shifted=dict(w)
    shifted[initial[0]]=shifted.get(initial[0],0)-base_scalar
    shifted[initial[1]]=shifted.get(initial[1],0)+base_scalar
    shifted={q:c0 for q,c0 in shifted.items() if c0}
    def describe(q):
        p,n=q
        return {'A_minus':[vertices[i] for i in A if n&bits[i]],
                'B_occupied':[[vertices[i],1 if p&bits[i] else -1]
                              for i in range(len(vertices)) if not mask&bits[i] and (p|n)&bits[i]]}
    certificate=[dict(describe(q),amplitude=c0) for q,c0 in sorted(shifted.items())]
    path=Path(__file__).resolve().parents[1]/'outputs/prepared_probe_physical_limits_20260924'/f'FLAT_ACTION_SIDE_{side}.json'
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    return {'side':side,'vertices':len(vertices),'overlap_pairs':len(pairs),
            'active_pair_counts':active_counts,'all_B_empty_flat_scalar':base_scalar,
            'mean_H4':str(mean),'mean_minus_background':str(mean-base_scalar),
            'variance_H4':str(variance),'selected_mark_leakage':leak,
            'shifted_action_words':len(shifted),'action_certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

def output_control(side):
    vertices=list(product(range(side),repeat=3));index={v:i for i,v in enumerate(vertices)}
    bits=[1<<i for i in range(len(vertices))]
    A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    def near(i):
        v=vertices[i];out=[]
        for k in range(3):
            for s in (-1,1):
                w=list(v);w[k]=(w[k]+s)%side;out.append(index[tuple(w)])
        return out
    adj={i:near(i) for i in range(len(vertices))}
    mask=sum(bits[i] for i in A)
    def location(v):return index[tuple(x%side for x in v)]
    a,d,h,c,e,b=map(location,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0),(-1,0,0)])
    fixed=list(map(location,[(0,-1,0),(0,0,1),(0,0,-1)]))
    minus=bits[d]|bits[h]
    common_plus=(mask^minus)|sum(bits[i] for i in fixed)
    initial_before=[(common_plus|bits[v],minus) for v in (c,e)]
    # Actual selected output of the first branch: old plus at a hops to e,
    # then the original pair has sign sigma at a and -sigma at b.
    initial=[]
    for sigma in (-1,1):
        p,n=initial_before[0]
        p=(p^bits[a])|bits[e]
        if sigma==1:p|=bits[a];n|=bits[b]
        else:n|=bits[a];p|=bits[b]
        assert (p|n).bit_count()==len(A)+6 and p.bit_count()-n.bit_count()==len(A)
        initial.append((p,n))
    pairs=set()
    for x in A:
        for y in adj[x]:
            for z in adj[y]:
                if x<z:pairs.add((x,z))
    pairs=sorted(pairs)
    def hop(state,src,dst):
        p,n=state
        if not ((p|n)&bits[src]) or (p|n)&bits[dst]:return None
        if p&bits[src]:return p^bits[src]^bits[dst],n
        return p,n^bits[src]^bits[dst]
    def step(vector,src,dests,inward=False):
        out=defaultdict(int)
        for q,w in vector.items():
            for v in dests:
                r=hop(q,v,src) if inward else hop(q,src,v)
                if r is not None:out[r]+=w
        return dict(out)
    def pair_action(q,x,z):
        first=step({q:1},x,adj[x]);forward=step(first,z,adj[z])
        back=step(forward,z,adj[z],True);out=step(back,x,adj[x],True)
        assert out.get(q,0)==sum(w*w for w in forward.values())
        return out
    base_scalar=0
    for x,z in pairs:
        r=len(set(adj[x])&set(adj[z]));base_scalar-=2*(36+r*(r-2))
    actions=[];active_counts=[]
    for q in initial:
        result=defaultdict(int);active=0
        for x,z in pairs:
            neighborhood=set(adj[x])|set(adj[z])
            if not any((q[0]|q[1])&bits[v] for v in neighborhood) and not (q[1]&(bits[x]|bits[z])):
                r=len(set(adj[x])&set(adj[z]));result[q]+=-2*(36+r*(r-2))
            else:
                active+=1
                for f,value in pair_action(q,x,z).items():result[f]+=-2*value
        actions.append(dict(result));active_counts.append(active)
    rows=[]
    for sigma,q,out,count in zip((-1,1),initial,actions,active_counts):
        mean=out.get(q,0);second=sum(v*v for v in out.values())
        rows.append({'sigma':sigma,'mean_H4':mean,'mean_minus_empty':mean-base_scalar,
                     'variance_H4':second-mean*mean,'nonzero_output_words':sum(v!=0 for v in out.values()),
                     'active_pair_count':count,'record_number':(q[0]|q[1]).bit_count()})
    return {'side':side,'vertices':len(vertices),'overlap_pairs':len(pairs),
            'all_B_empty_flat_scalar':base_scalar,'selected_output_matter_rows':rows}
def unit_control():
    mp.mp.dps=70
    h=mp.mpf('6.62607015e-34');e=mp.mpf('1.602176634e-19');c=mp.mpf('299792458')
    hbar_GeV_s=h/(2*mp.pi*e*10**9)
    rows=[]
    for label,limit in [('MAGIC2017','5.9e10'),('LHAASO2024_v2_ML_MINOS','6.9e11')]:
        tau=6*hbar_GeV_s/mp.mpf(limit)
        rows.append({'benchmark':label,'E_QG2_lower_GeV':limit,
          'orientation_independent_necessary_a_upper_m':str(c*tau),
          'necessary_tau_upper_seconds':str(tau),
          'status':'Conditional published timing conversion; no selected scale or new fit.'})
    return rows

def main():
    start=time.perf_counter();root=Path(__file__).resolve().parents[1]
    path=root/RESULT_PATH;path.parent.mkdir(parents=True,exist_ok=True)
    result={'scope':'Exact disclosed root coefficients and conditional SI arithmetic; no full rotor propagation.',
            'input_rows':[input_control(s) for s in (6,16)],
            'output_rows':[output_control(16)],'unit_rows':unit_control(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.perf_counter()-start,'all_assertions_passed':True}
    data=json.dumps(result,indent=2,allow_nan=False)+'\n';path.write_text(data);print(data,end='')
    print('TOTAL_PASS: 3')

if __name__=='__main__':main()
