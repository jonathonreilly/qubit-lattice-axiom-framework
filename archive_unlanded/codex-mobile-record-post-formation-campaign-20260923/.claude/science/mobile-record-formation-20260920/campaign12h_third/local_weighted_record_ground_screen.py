#!/usr/bin/env python3
"""Local weighted cooling algebra and exact finite variational minimization."""
from __future__ import annotations

from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
import random

import numpy as np
import scipy.linalg as la
import sympy as sp

import local_gauge_record_cooling_check as base

OUT=Path(__file__).resolve().parent


def exact_weighted_controls():
    r,z=sp.symbols('r z',positive=True)
    l=sp.Matrix([[r,-1],[r*r,-r]])/(1+r*r);pm=l.T*l
    assert (l*l).applyfunc(sp.factor)==sp.zeros(2)
    assert (pm*pm-pm).applyfunc(sp.factor)==sp.zeros(2)
    v=sp.Matrix([1,r*z]);g=r*(1-z)/(1+r*r*z)
    assert (pm*v-g*l.T*v).applyfunc(sp.factor)==sp.zeros(2,1)
    # Eight configurations with a local two-bit weight and a coherent spectator.
    dim=8;amps=sp.Matrix([2**int((c&1)>0 and (c&2)>0) for c in range(dim)])
    groups=defaultdict(list)
    for bit in range(3):
        for a in range(dim):
            if a>>bit&1:continue
            b=a^(1<<bit);ratio=amps[b]/amps[a]
            groups[(bit,ratio)].append((a,b))
    jumps=[];h=sp.zeros(dim);loss=sp.zeros(dim);eye=sp.eye(dim)
    for j,((bit,ratio),pairs) in enumerate(sorted(groups.items())):
        op=sp.zeros(dim)
        for a,b in pairs:
            op[a,a]=ratio/(1+ratio**2);op[a,b]=-1/(1+ratio**2)
            op[b,a]=ratio**2/(1+ratio**2);op[b,b]=-ratio/(1+ratio**2)
        assert op*amps==sp.zeros(dim,1) and op**2==sp.zeros(dim)
        pm=op.T*op;assert pm**2==pm
        h+=(j-2)*pm;loss+=(j+1)*pm;jumps.append((j+1,op))
        fv=sp.Matrix([amps[c]*2**sum(3**b for b in range(3) if c>>b&1) for c in range(dim)])
        zz=2**(3**bit);gg=ratio*(1-zz)/(1+ratio**2*zz)
        assert pm*fv==gg*op.T*fv
    assert sp.Matrix.vstack(*[op for rate,op in jumps]).rank()==dim-1
    target=amps*amps.T/(amps.T*amps)[0]
    gen=-sp.I*(sp.kronecker_product(eye,h)-sp.kronecker_product(h.T,eye))
    for rate,op in jumps:
        pm=op.T*op
        gen+=rate*(sp.kronecker_product(op,op)-(sp.kronecker_product(eye,pm)+sp.kronecker_product(pm.T,eye))/2)
    vec=sp.Matrix([target[i,j] for j in range(dim) for i in range(dim)])
    assert gen*vec==sp.zeros(dim*dim,1)
    prime=65537
    def residue(a):
        ar,ai=a.as_real_imag();rr=sp.Rational(ar);ii=sp.Rational(ai)
        return (int(rr.p)*pow(int(rr.q),-1,prime)+256*int(ii.p)*pow(int(ii.q),-1,prime))%prime
    arr=np.array([[residue(a) for a in row] for row in gen.tolist()],dtype=np.int64)
    rank=base.rank_mod(arr);assert rank==dim*dim-1
    return {'symbolic_pair_identity':'exact for arbitrary positive r,z',
            'eight_state_weight':'psi(c) proportional to 2^(bit0*bit1), with bit2 coherent spectator',
            'local_context_jump_count':len(jumps),'pair_counts':[len(x) for x in groups.values()],
            'common_dark_dimension':1,'exact_complex_Liouvillian_nullity':1,
            'modular_rank_certificate':{'prime':prime,'i_image':256,'rank':rank},
            'separating_vector_identity':'Each class checked exactly at exp(t)=2 with F=sum3^bit*bit.',
            'target_normalization_squared':str((amps.T*amps)[0])}


def local_support_controls():
    rng=random.Random(20260922);rows=[]
    for size in (2,3,4):
        vertices,edges,faces=base.geometry((size,)*3,True)
        p=faces[0];mask=p['r']|p['l'];overlap=[q for q in faces if (q['r']|q['l'])&mask]
        union=0
        for q in overlap:union|=q['r']|q['l']
        flip=lambda c,q:((c&q['r']==0 and c&q['l']==q['l']) or (c&q['r']==q['r'] and c&q['l']==0))
        diffs=[]
        for _ in range(128):
            a=(rng.getrandbits(len(edges))&~mask)|p['l'];b=a^mask
            assert flip(a,p) and flip(b,p)
            all_diff=sum(flip(b,q)-flip(a,q) for q in faces)
            local_diff=sum(flip(b,q)-flip(a,q) for q in overlap)
            assert all_diff==local_diff and abs(local_diff)<=12
            assert base.gauss(a,vertices,edges)==base.gauss(b,vertices,edges)
            diffs.append(all_diff)
        assert len(overlap)<=13 and union.bit_count()<=40
        rows.append({'side':size,'all_links':len(edges),'overlapping_plaquettes_including_self':len(overlap),
                     'support_links':union.bit_count(),'random_flippable_backgrounds':128,
                     'background_charge':'Arbitrary fixed charges; each flip preserves them exactly.',
                     'observed_delta_flippability_values':sorted(set(diffs)),
                     'locality_check':'All global changes equal changes in the bounded overlap neighborhood.'})
    return rows


def finite_component():
    vertices,edges,faces=base.geometry((2,2,2),True)
    seed=sum(1<<j for j,(v,a,w) in enumerate(edges) if sum(v[b] for b in range(3) if b!=a)%2==0)
    states,tree=base.component(seed,faces);pairs=base.pairs_from_component(states,faces);d=len(states)
    nf=np.zeros(d,dtype=int);h=np.zeros((d,d))
    for ps in pairs:
        for a,b in ps:nf[a]+=1;nf[b]+=1;h[a,b]-=1;h[b,a]-=1
    h+=np.diag(nf);assert not np.any(nf%2)
    x=sp.symbols('x');counts=Counter(map(int,nf));cross=Counter()
    for ps in pairs:
        for a,b in ps:cross[int(nf[a]+nf[b])//2]+=1
    z=sum(int(count)*x**n for n,count in counts.items())
    edgepoly=sum(int(count)*x**n for n,count in cross.items())
    rows=[]
    for delta in [sp.Rational(1,20),sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1)]:
        n=(1-delta)*sum(int(count)*nn*x**nn for nn,count in counts.items())-2*edgepoly
        ratio=sp.cancel(n/z)
        dn=sp.together(sp.diff(ratio,x)).as_numer_denom()[0]
        poly=sp.Poly(dn,x);power=min(m[0] for m in poly.monoms());poly=sp.Poly(poly.as_expr()/x**power,x)
        intervals=sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**13))
        candidates=[];all_positive=[]
        for (lo,hi),multiplicity in intervals:
            if hi<=0:continue
            assert lo>0
            xx=float((lo+hi)/2);energy=float(ratio.subs(x,xx))
            item={'lower':str(lo),'upper':str(hi),'multiplicity':multiplicity,'midpoint':xx,'energy':energy}
            candidates.append(item);all_positive.append(item)
        endpoints={'x_to_zero':str(sp.limit(ratio,x,0,dir='+')),'x_to_infinity':str(sp.limit(ratio,x,sp.oo))}
        best=min(candidates,key=lambda q:q['energy'])
        assert best['energy']<min(float(sp.sympify(q)) for q in endpoints.values())
        xx=best['midpoint'];theta=float(np.log(xx))
        trial=np.exp(theta*(nf-nf.max())/2);trial/=la.norm(trial)
        ham=h-float(delta)*np.diag(nf);ev,vec=la.eigh(ham);ground=vec[:,0]
        if ground.sum()<0:ground=-ground
        measured=float(trial@ham@trial);assert abs(measured-best['energy'])<1e-11
        gap=float(ev[1]-ev[0]);infidelity=float(1-(ground@trial)**2)
        bound=float((measured-ev[0])/gap)
        assert infidelity<=bound+1e-12 and infidelity>=-1e-12
        classes=[];all_residuals=[]
        for p,ps in enumerate(pairs):
            bym=defaultdict(list)
            for a,b in ps:bym[int(nf[b]-nf[a])].append((a,b))
            for m,group in sorted(bym.items()):
                rr=np.exp(theta*m/2)
                # Every full configuration in a context has the same locally
                # supplied amplitude ratio; verify the complete jump action.
                residual=np.zeros(d)
                for a,b in group:
                    val=(rr*trial[a]-trial[b])/(1+rr*rr)
                    residual[a]+=val;residual[b]+=rr*val
                all_residuals.append(float(np.max(abs(residual))))
            classes.append({'plaquette':p,'contexts':{str(m):len(group) for m,group in sorted(bym.items())}})
        assert max(all_residuals)<1e-12
        baseline=float(np.ones(d)@ham@np.ones(d)/d)
        row={'delta':str(delta),'normalization_polynomial':str(sp.expand(z)),
             'energy_numerator_polynomial':str(sp.expand(n)),
             'critical_polynomial_without_zero_root':str(poly.as_expr()),
             'all_positive_critical_root_intervals':all_positive,'endpoint_energies':endpoints,
             'x_optimum':xx,'theta_optimum':theta,'variational_energy':measured,'uniform_RK_trial_energy':baseline,
             'ground_energy':float(ev[0]),'finite_ground_gap':gap,'ground_infidelity':infidelity,
             'energy_gap_infidelity_upper_bound':bound,'all_later_time_trace_error_upper_bound':2*np.sqrt(max(bound,0)),
             'all_local_jump_target_residual_max':max(all_residuals),'local_jump_count':sum(len(c['contexts']) for c in classes),
             'plaquette_contexts':classes,
             'claim_limit':'Optimum of this one-parameter family on this one finite component; no thermodynamic fidelity or physical-law selection.'}
        rows.append(row)
    return {'dimension':d,'component_states_sha256':hashlib.sha256(json.dumps(states).encode()).hexdigest(),
            'flippability_counts':dict(counts),'edge_middegree_counts':dict(cross),'cases':rows}


def main():
    dep=hashlib.sha256((OUT/'local_gauge_record_cooling_check.py').read_bytes()).hexdigest()
    assert dep=='9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552'
    result={'status':'PASS','geometry_dependency_sha256':dep,'weighted_algebra':exact_weighted_controls(),
            'bounded_local_support':local_support_controls(),'finite_variational':finite_component(),
            'scope':'Local supplied many-qubit cooling and finite variational energy/overlap; no native nearest-neighbor compiler or thermodynamic photon claim.'}
    (OUT/'LOCAL_WEIGHTED_RECORD_GROUND_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
