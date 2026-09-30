#!/usr/bin/env python3
"""Exact finite controls; analytic CP/thermodynamic/energy proof is in the note.

No campaign helper or outside scientific dataset is imported. Symbolic rotor
shifts and full original mark outputs are retained. These are author controls,
not an independent review, infinite-volume computation or audit verdict.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[_key]='1'
import collections
import hashlib
import itertools
import json
import math
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/ORIGINAL_RECORD_THERMODYNAMIC_DYNAMICS_AND_ENERGY_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-30.md',
    'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/ORIGINAL_FIRST_BIRTH_SYSTEM_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-29.md',
]

def gram(rows):
    out=collections.Counter()
    for columns in rows.values():
        for i,si in columns:
            for j,sj in columns:
                out[i,j,tuple(b-a for a,b in zip(si,sj))]+=1
    return out


def star_controls():
    words=list(itertools.product((0,1,-1),repeat=6))
    inputs=[(q,w) for q in (1,-1) for w in words]
    frows=collections.defaultdict(list)
    channels={(b,s):collections.defaultdict(list) for b in range(6) for s in (1,-1)}
    paths=0; gauss=0; frelations=0
    fsector=collections.Counter();bsector=collections.Counter()
    for i,(q,w) in enumerate(inputs):
        o=sum(x!=0 for x in w)
        for d in range(6):
            if w[d]:continue
            wf=list(w);wf[d]=q
            sf=[0]*6;sf[d]=-q
            frows[tuple(wf)].append((i,tuple(sf)));frelations+=1;fsector[o]+=1
            for b in range(6):
                if b==d or w[b]:continue
                for sigma in (1,-1):
                    wb=wf.copy();wb[b]=-sigma
                    shift=sf.copy();shift[b]+=sigma
                    channels[b,sigma][(sigma,tuple(wb))].append((i,tuple(shift)))
                    # Actual oriented Gauss increments at A and all six B sites.
                    assert sum(shift)==sigma-q
                    for j in range(6):assert -shift[j]==wb[j]-w[j]
                    assert sum(x!=0 for x in wb)-o==2
                    paths+=1;gauss+=7;bsector[o]+=1
    fg=gram(frows);resolved=collections.Counter()
    for rows in channels.values():resolved.update(gram(rows))
    coherent=collections.Counter()
    for b in range(6):
        joined=collections.defaultdict(list)
        for s in (1,-1):
            for row,columns in channels[b,s].items():joined[row].extend(columns)
        coherent.update(gram(joined))
    assert resolved==coherent
    loss_half=F(1,1)
    remote={key:(1-2*loss_half)*value for key,value in resolved.items() if (1-2*loss_half)*value}
    assert not remote, 'remote full-generator identity action must cancel gain and both losses'
    assert max(resolved.values())>=60  # The cancellation is not a zero-jump fixture.
    expected=collections.Counter()
    for key,value in fg.items():
        i,j,shift=key;o=sum(x!=0 for x in inputs[j][1])
        assert o==sum(x!=0 for x in inputs[i][1])
        v=2*(5-o)*value
        if v:expected[key]=v
    assert resolved==expected, 'full Laurent loss identity, including off-diagonal input words'
    # Exact biregular row/column incidence, not a floating eigensolver.
    fdegrees=[];bdegrees=[]
    for o in range(6):
        col=[i for i,(_,w) in enumerate(inputs) if sum(x!=0 for x in w)==o]
        deg=collections.Counter(i for rows in frows.values() for i,_ in rows if i in set(col))
        rows=[v for w,v in frows.items() if sum(x!=0 for x in w)==o+1]
        assert all(deg[i]==6-o for i in col)
        assert all(len(r)==o+1 for r in rows)
        fdegrees.append((6-o)*(o+1))
        if o<=4:
            rows=channels[0,1]
            relevant={i for i,(q,w) in enumerate(inputs) if w[0]==0 and sum(x!=0 for x in w)==o}
            counts=collections.Counter(i for r in rows.values() for i,_ in r if i in relevant)
            assert all(counts[i]==5-o for i in relevant)
            assert all(len(r)==o+1 for (_,w),r in rows.items() if sum(x!=0 for x in w)==o+2)
            bdegrees.append((5-o)*(o+1))
    gamma=[2*(5-o)*(6-o)*(o+1) for o in range(6)]+[0]
    assert max(fdegrees)==12 and max(bdegrees)==9 and max(gamma)==80
    assert gamma==[60,80,72,48,20,0,0]
    assert (frelations,paths)==(2916,9720)
    return {'input_charge_words':len(inputs),'F_primitive_words':frelations,'birth_primitive_words':paths,
            'Gauss_vertex_equalities':gauss,'F_Gram_Laurent_entries':len(fg),'complete_loss_Laurent_entries':len(resolved),
            'Gamma_sector_bounds':gamma,'scope':'all star matter words and symbolic integer-link shifts; not a full torus evolution'}


def geometry_controls():
    e=[(1,0,0),(0,1,0),(0,0,1)];zero=(0,0,0)
    def add(a,b):return tuple(x+y for x,y in zip(a,b))
    def scale(s,a):return tuple(s*x for x in a)
    def norm(a):return sum(map(abs,a))
    units=e+[scale(-1,x) for x in e]
    ds={scale(2*s,v) for v in e for s in (-1,1)}
    ds|={add(scale(s,e[i]),scale(t,e[j])) for i,j in itertools.combinations(range(3),2) for s,t in itertools.product((-1,1),repeat=2)}
    star=lambda a:{a}|{add(a,v) for v in units}
    root=star(zero);active={zero}|ds
    pairs={tuple(sorted((a,add(a,d)))) for a in active for d in ds if star(a)&root or star(add(a,d))&root}
    pairs={p for p in pairs if (star(p[0])|star(p[1]))&root}
    electric={(add(b,scale(-1,d)),b) for b in units for d in units}
    support=set().union(*(star(a)|star(b) for a,b in pairs))
    balls={r:sum(sum(map(abs,x))<=r for x in itertools.product(range(-r,r+1),repeat=3)) for r in (2,3,4,5,6)}
    even6=sum(sum(map(abs,x))<=6 and sum(x)%2==0 and x!=zero for x in itertools.product(range(-6,7),repeat=3))
    assert len(ds)==18 and len(pairs)==264 and len(electric)==36
    assert max(map(norm,support))==5
    assert balls[4]==129 and balls[6]==377 and balls[2]==25 and even6==230
    assert (max(map(norm,support))+1)==6  # Electric halo cannot be omitted.
    return {'distance_two_partners':18,'current_pair_terms':len(pairs),'current_electric_terms':len(electric),
            'current_support_radius':5,'electric_picture_radius':6,'balls':balls,'other_even_centers_radius6':even6}


def series_controls():
    checked=0;tails=[]
    for x in [1,7,25,129,130,377,800,1600]:
        q=max(1,(x+128)//129)
        c=1
        for n in range(1,21):
            c*=129*(x+129*(n-1))
            assert c<=16641**n*math.factorial(n+q-1)//math.factorial(q-1)
            checked+=1
        for z in (F(1,4),F(1,2),F(3,4)):
            m=max(20,4*q);n=m+1;r=z*F(n+q,n+1)
            assert r<1
            bound=F(math.comb(n+q-1,n))*z**n/(1-r)
            partial=sum((F(math.comb(k+q-1,k))*z**k for k in range(n,n+160)),F(0))
            assert partial<=bound
            tails.append({'x':x,'q':q,'z':str(z),'m':m,'bound':str(bound),'partial':str(partial)})
    # Exponential generating functions for time segments, by exact convolution.
    simplex=0
    for segments in range(1,8):
        coeff=[F(1)]+[F(0)]*10
        for _ in range(segments):
            coeff=[sum((coeff[j]/math.factorial(n-j) for j in range(n+1)),F(0)) for n in range(11)]
        for n in range(11):
            assert coeff[n]==F(segments**n,math.factorial(n));simplex+=1
    for z in (F(1,10),F(1,4),F(1,2)):
        exact=3*z*(1+3*z)/(1-z)**5
        partial=sum((math.comb(n+2,2)*n*n*z**n for n in range(1,200)),F(0))
        assert partial<=exact<=240*z
    p0=123744  # Imported INITIAL theorem value at K=delta=kappa=1.
    aa=16641*(5184+160);cstar=241920+12165120
    t0=min(F(1,2*aa),F(p0,480*cstar*aa))
    assert 240*cstar*aa*t0<=F(p0,2)
    return {'connected_inequalities':checked,'timestamp_simplex_coefficients':simplex,'localization_tails':tails,
            'unit_parameter_t0':str(t0),'imported_initial_power':p0,'scope':'scalar majorants only, no operator CP theorem from these samples'}


def domain_controls():
    b=lambda u,s:(2*s+1)*(1+s)**u
    assert (b(2,2),b(2,4),b(4,2),b(4,4))==(45,225,405,5625)
    assert 2*b(2,2)+1+b(2,4)==316
    assert 2*2*(1+b(2,4))==904
    phases=[]
    for j in [1,2,7,32,1000]:
        before=4*j*j;after=4*(j+1)**2
        assert after-before==8*j+4
        phases.append({'j':j,'electric_energy_increment_over_K':after-before,'time_times_K_over_pi':str(F(1,8*j+4)),'operator_norm_defect':2})
    # Exact boundary counterexample: unitary circulation jump U_M of norm1.
    # With mean jump count r=gamma*t, Poisson E[count²]=r+r².
    boundary=[]
    for length in [8,16,32]:
        M=length;r=F(1,3)
        energy_one=4*M*M*(r+r*r)
        loops=length*length//16;volume=length**3
        pervolume=F(loops,volume)*energy_one
        boundary.append({'L':length,'M':M,'loop_energy_over_K':str(energy_one),'density_over_K':str(pervolume)})
    assert F(boundary[-1]['density_over_K'])==4*F(boundary[0]['density_over_K'])
    return {'weighted_band_constants':[45,225,405,5625],'current_electric_coefficient':316,
            'transport_electric_magnetic_coefficient':904,'physical_circulation_controls':phases,
            'boundary_variants_require_weighted_bounds':boundary,
            'scope':'analytic counterexample controls; no modified boundary law is adopted'}


def main():
    signal.alarm(AUDIT_TIMEOUT_SEC)
    resource.setrlimit(resource.RLIMIT_CPU,(30,31))
    start=time.monotonic();cpu=time.process_time();root=Path(__file__).resolve().parents[1]
    identities={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    results={};failures={}
    for name,fn in [('original_star',star_controls),('local_geometry',geometry_controls),('connected_series',series_controls),('energy_domains',domain_controls)]:
        print('BEGIN',name,flush=True)
        try:results[name]=fn();print('PASS',name,flush=True)
        except Exception as exc:failures[name]=repr(exc);print('FAIL',name,repr(exc),flush=True)
    print(json.dumps({'results':results,'failures':failures,'input_sha256':identities,'cpu_seconds':time.process_time()-cpu,
                      'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
    print('per_element: exact source charge and symbolic rotor-word controls in completed groups.')
    print('per_site: exact one-star and local current geometry, not sampled thermal states.')
    print('per_mode: no mode or continuum spectrum is claimed.')
    print('per_block: finite algebra/series/domain controls; all-time CP and weighted limits are analytic arguments.')
    print('lattice_wide: not executed; all-volume quantifiers are proved in the note, not inferred from this runner.')
    print(f'TOTAL: PASS={len(results)} FAIL={len(failures)}')
    if failures:raise SystemExit(1)
# Main suppressed: invoke the named actual finite control below.

star_controls()
