#!/usr/bin/env python3
"""Root controls: exact graph words and harmonic/observational conversion.
No full evolution, telescope-data fit or independent reconstruction is claimed.
"""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from fractions import Fraction
import hashlib, json, time
import mpmath as mp


def graph(periods):
    vertices = list(product(*(range(L) for L in periods)))
    index = {p:i for i,p in enumerate(vertices)}
    A = tuple(i for i,p in enumerate(vertices) if sum(p)%2==0)
    edges = []
    for a in A:
        p = vertices[a]
        dest = set()
        for j,L in enumerate(periods):
            for sign in (-1,1):
                q = list(p); q[j] = (q[j]+sign)%L
                dest.add(index[tuple(q)])
        edges.extend((a,b) for b in sorted(dest))
    return vertices,A,tuple(edges)


def graph_control(periods):
    vertices,A,edges = graph(periods)
    nV,nE = len(vertices),len(edges)
    stars=defaultdict(list)
    for e,(a,b) in enumerate(edges): stars[a].append((e,b))
    degrees={len(v) for v in stars.values()}; assert len(degrees)==1
    z=degrees.pop()
    q0=tuple(1 if a in A else 0 for a in range(nV))
    drift=Counter(); second=Counter(); occupancy=Counter(); paths=[]
    mark_outputs=defaultdict(set)
    for a,star in stars.items():
        for eb,b in star:
            for ec,c in star:
                if b==c: continue
                for sigma in (-1,1):
                    q=list(q0);q[a]=sigma;q[b]=-sigma;q[c]=1
                    kick={eb:sigma,ec:-1}
                    div=Counter()
                    for e,d in kick.items():
                        src,dst=edges[e];div[src]+=d;div[dst]-=d
                    assert all(div[v]==q[v]-q0[v] for v in range(nV))
                    key=(a,b,sigma)
                    assert tuple(q) not in mark_outputs[key]
                    mark_outputs[key].add(tuple(q))
                    paths.append((a,b,c,sigma,kick))
                    occupancy[b]+=1;occupancy[c]+=1
                    drift.update(kick)
                    for e,de in kick.items():
                        for f,df in kick.items(): second[e,f]+=de*df
    assert len(paths)==2*len(A)*z*(z-1)
    assert set(drift.values())=={-2*(z-1)}
    assert all(second[e,f]==(4*(z-1) if e==f else 0)
               for e in range(nE) for f in range(nE))
    assert set(occupancy.values())=={4*z*(z-1)}
    # Coherent +/- marks still have orthogonal matter output words.
    for a,star in stars.items():
        for _,b in star:
            assert mark_outputs[a,b,-1].isdisjoint(mark_outputs[a,b,1])

    p0=(0,)*len(periods)
    def moved(p,j):
        q=list(p);q[j]=(q[j]+1)%periods[j];return tuple(q)
    p1=moved(p0,0);p2=moved(p1,1);p3=moved(p0,1)
    index={p:i for i,p in enumerate(vertices)}
    lookup={e:i for i,e in enumerate(edges)}
    loop=Counter()
    for p,q in zip((p0,p1,p2,p3),(p1,p2,p3,p0)):
        u,v=index[p],index[q]
        if (u,v) in lookup: loop[lookup[u,v]]+=1
        else: loop[lookup[v,u]]-=1
    assert sum(loop.values())==0
    divloop=Counter()
    for e,v in loop.items():
        a,b=edges[e];divloop[a]+=v;divloop[b]-=v
    assert not any(divloop.values())
    coefficients=Counter();constant=0;frozen_constant=0
    for a,b,c,sigma,kick in paths:
        for e,v in loop.items():
            ae,be=edges[e]
            active=int(be not in (b,c))
            qa=sigma if ae==a else 1
            coefficients[e]+=2*v*(active-1)
            constant+=active*(2*v*kick.get(e,0)+v*v-qa*v)-(v*v-v)
            frozen_constant+=2*v*kick.get(e,0)
    rB=4*z*(z-1)
    assert all(coefficients[e]==-rB*2*v for e,v in loop.items())
    assert constant==-rB*sum(v*v for v in loop.values())
    assert frozen_constant==0
    # Omitting new matter's vacancy gates would miss this nonzero operator.
    frozen_mutant_residual=abs(constant)+sum(abs(v) for v in coefficients.values())
    assert frozen_mutant_residual>0
    # A one-sign instrument is deliberately different: it has cross noise.
    one_sign_cross=Counter()
    for a,b,c,sigma,kick in paths:
        if sigma!=1: continue
        for e,de in kick.items():
            for f,df in kick.items():
                if e!=f:one_sign_cross[e,f]+=de*df
    assert any(one_sign_cross.values())
    return {'periods':periods,'vertices':nV,'edges':nE,'degree':z,
            'actual_unit_paths':len(paths),'resolved_marks':len(mark_outputs),
            'per_edge_drift_over_kappa':-2*(z-1),
            'per_edge_covariance_rate_over_kappa':4*(z-1),
            'off_diagonal_second_moment_sum_abs':sum(abs(v) for (e,f),v in second.items() if e!=f),
            'B_occupancy_rate_over_kappa':rB,
            'loop_acceleration_E_coefficients':dict(coefficients),
            'loop_acceleration_constant':constant,
            'field_only_postbirth_mutant_residual':frozen_mutant_residual,
            'one_sign_cross_noise_sum_abs':sum(abs(v) for v in one_sign_cross.values())}


def dispersion_controls():
    mp.mp.dps=70
    rows=[]
    for direction in ((1,0,0),(1,1,0),(1,1,1),(1,2,3),(-2,3,5)):
        norm=mp.sqrt(sum(i*i for i in direction));n=[mp.mpf(i)/norm for i in direction]
        A4=sum(i**4 for i in n)
        for sx in ('0.00001','.001','.03','.2','.7','1'):
            x=mp.mpf(sx);D=4*sum(mp.sin(x*i/2)**2 for i in n)
            vel=[mp.sin(x*i)/mp.sqrt(D) for i in n]
            radial=sum(u*v for u,v in zip(n,vel));speed=mp.sqrt(sum(v*v for v in vel))
            assert speed<=1
            re=abs(radial-(1-A4*x*x/8))/x**4
            se=abs(speed-(1-A4*x*x/8))/x**4
            assert re<=mp.mpf(1)/40 and se<=mp.mpf(1)/20
            phase=mp.sqrt(D)/x
            rows.append({'direction':direction,'x':sx,'A4':str(A4),
                         'radial_speed_over_c':str(radial),'speed_over_c':str(speed),
                         'radial_remainder_over_x4':str(re),'speed_remainder_over_x4':str(se),
                         'phase_as_group_mutant_error_over_x2':str(abs(phase-radial)/x**2)})
    # The radial coefficient and phase coefficient differ by a factor of three.
    assert max(mp.mpf(r['phase_as_group_mutant_error_over_x2']) for r in rows)>mp.mpf('.08')
    # Exact SI defining constants: h, c, elementary charge; hbar=h/(2pi).
    h=mp.mpf('6.62607015e-34');c=mp.mpf('299792458');e=mp.mpf('1.602176634e-19')
    hc_GeV_m=h*c/(2*mp.pi*e*mp.mpf(10)**9)
    bounds=[]
    for label,energy in [('MAGIC2017_table6_including_systematics','5.9e10'),
                         ('LHAASO2024_table1_ML_MINOS','6.9e11')]:
        aq=mp.sqrt(12)*hc_GeV_m/mp.mpf(energy)
        bounds.append({'published_analysis':label,'E_QG_2_GeV':energy,
                       'a_sqrt_A4_upper_m':str(aq),
                       'a_orientation_independent_necessary_upper_m':str(mp.sqrt(3)*aq),
                       'status':'conditional conversion, not a new fit or framework prediction'})
    return {'rows':rows,'hbar_c_GeV_m':str(hc_GeV_m),'conditional_bounds':bounds}


def main():
    started=time.monotonic()
    out={'scope':'Root exact finite graph words; harmonic dispersion; conditional conversion only',
         'graphs':[graph_control(p) for p in ((2,2,2),(6,6),(6,6,6))],
         'dispersion':dispersion_controls(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out['elapsed_seconds']=time.monotonic()-started
    path=Path(__file__).with_name('PHOTON_BIRTH_CONTROL_RESULTS.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
