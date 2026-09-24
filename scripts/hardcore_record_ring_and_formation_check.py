#!/usr/bin/env python3
"""Hard occupancy exclusion, fourth-order gauge loops, and live formation.

All assertions are finite controls. The general coefficient and fixed-volume
limit arguments are in HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/hardcore_record_ring_and_formation_check.py', 'scripts/local_gauge_record_cooling_check.py')

from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import random
import time

import numpy as np
import scipy.linalg as la
import sympy as sp

import local_gauge_record_cooling_check as geometry_source

OUT=Path(__file__).resolve().parent


def square_model(reference, allow_birth=False, fermionic=False):
    count=sum(reference);basis=[]
    for matter in itertools.product((0,1,-1) if allow_birth else (0,1),repeat=4):
        if sum(matter)!=count:continue
        if not allow_birth and sum(v!=0 for v in matter)!=count:continue
        for bits in itertools.product((0,1),repeat=4):
            if all(bits[x]-bits[(x-1)%4]+reference[x]-matter[x]==0 for x in range(4)):
                basis.append((matter,bits))
    ix={s:i for i,s in enumerate(basis)};dim=len(basis)
    hop=sp.zeros(dim);penalty=[];jumps=[sp.zeros(dim) for _ in range(4)]
    n=[];gauss_hops=0
    for i,(matter,bits) in enumerate(basis):
        n.append(sum(v!=0 for v in matter))
        penalty.append(sum(matter[x]!=0 for x in range(4) if not reference[x]))
        for edge in range(4):
            x,y=edge,(edge+1)%4
            for u,v,orientation in ((x,y,1),(y,x,-1)):
                charge=matter[u]
                if charge==0 or matter[v]!=0:continue
                step=-orientation*charge
                if not 0<=bits[edge]+step<=1:continue
                m=list(matter);b=list(bits);m[u]=0;m[v]=charge;b[edge]+=step
                target=(tuple(m),tuple(b));assert target in ix
                sign=(-1)**sum(matter[a]!=0 for a in range(min(u,v)+1,max(u,v))) if fermionic else 1
                hop[ix[target],i]-=sign;gauss_hops+=1
            if allow_birth and matter[x]==matter[y]==0:
                charge=1 if bits[edge]==0 else -1
                m=list(matter);b=list(bits);m[x]=charge;m[y]=-charge;b[edge]+=charge
                target=(tuple(m),tuple(b));assert target in ix
                jumps[edge][ix[target],i]=1
    assert hop==hop.T
    num=sp.diag(*n);assert num*hop==hop*num
    for j in jumps:assert num*j-j*num==2*j
    return basis,hop,penalty,n,jumps,gauss_hops


def square_controls():
    rows=[];eps=sp.symbols('epsilon',real=True);energy=sp.symbols('energy')
    for reference in [(1,0,0,0),(1,0,1,0)]:
        basis,hop,penalty,n,jumps,gh=square_model(reference)
        p=[i for i,e in enumerate(penalty) if e==0];q=[i for i,e in enumerate(penalty) if e]
        b=hop.extract(p,q);tq=hop.extract(q,q)
        den=sp.diag(*[sp.Rational(1,penalty[i]) for i in q])
        h2=-b*den*b.T;f4=-b*den*tq*den*tq*den*b.T;k2=b*den**2*b.T
        h4=f4-(k2*h2+h2*k2)/2
        want2=-sum(reference)*sp.eye(2)
        want4=sp.Matrix([[0,-1],[-1,0]]) if sum(reference)==1 else sp.Matrix([[2,-2],[-2,2]])
        assert h2==want2 and h4==want4
        # An independent exact characteristic-polynomial series check, without
        # substituting the Schur coefficient into the polynomial calculation.
        char=sp.factor((energy*sp.eye(len(basis))-sp.diag(*penalty)-eps*hop).det())
        factors=sp.factor_list(char,energy)[1];series=[]
        for factor,multiplicity in factors:
            if factor.subs({energy:0,eps:0})!=0:continue
            a2,a4,a6=sp.symbols('a2 a4 a6')
            expr=sp.series(factor.subs(energy,a2*eps**2+a4*eps**4+a6*eps**6),eps,0,8).removeO().expand()
            sol=sp.solve([expr.coeff(eps,j) for j in (2,4,6)],(a2,a4,a6),dict=True)
            assert len(sol)==1
            series.append({str(k):str(v) for k,v in sol[0].items()})
        assert len(series)==2 and sorted(sp.Rational(x['a4']) for x in series)==sorted(h4.eigenvals())
        numerical=[]
        for ratio in (.02,.04,.08):
            mat=np.diag(penalty)+ratio*np.array(hop,dtype=float)
            eig=la.eigvalsh(mat)[:2]
            approx=la.eigvalsh(ratio**2*np.array(h2,dtype=float)+ratio**4*np.array(h4,dtype=float))
            error=float(max(abs(eig-approx)))
            assert error<100*ratio**6
            numerical.append({'t_over_Delta':ratio,'exact_low_energies_over_Delta':eig.tolist(),
                              'fourth_order_energies_over_Delta':approx.tolist(),
                              'error_divided_by_ratio6':error/ratio**6})
        rows.append({'reference_occupancy':reference,'physical_sector_dimension':len(basis),
                     'low_indices':p,'basis':basis,'penalties_over_Delta':penalty,
                     'hop_matrix_over_t':hop.tolist(),'directed_Gauss_preserving_hops':gh,
                     'second_coefficient':h2.tolist(),'zero_energy_Schur_fourth':f4.tolist(),
                     'normalized_effective_fourth':h4.tolist(),
                     'characteristic_polynomial':str(char),'exact_low_series':series,'numerical_controls':numerical})
    # Identical fermions exchange sign on the two-record loop. Statistics are
    # an explicit premise, not determined by permanence of recorded contents.
    basis,h,pen,n,jumps,gh=square_model((1,0,1,0),fermionic=True)
    p=[i for i,v in enumerate(pen) if v==0];q=[i for i,v in enumerate(pen) if v]
    b=h.extract(p,q);den=sp.diag(*[sp.Rational(1,pen[i]) for i in q]);tq=h.extract(q,q)
    f4=-b*den*tq*den*tq*den*b.T;h2=-b*den*b.T;k2=b*den**2*b.T
    h4=f4-(k2*h2+h2*k2)/2;assert h4==sp.Matrix([[2,2],[2,2]])
    return {'bosonic_cases':rows,'fermionic_two_record_fourth':h4.tolist()}


def lattice_paths(shape,c):
    vertices,edges,faces=geometry_source.geometry(shape,True)
    d=len(shape);vindex={v:i for i,v in enumerate(vertices)}
    assert all(n>=6 and n%2==0 for n in shape)
    assert geometry_source.gauss(c,vertices,edges)==(0,)*len(vertices)
    a_set={i for i,v in enumerate(vertices) if sum(v)%2==0}
    adjacency=defaultdict(dict);eligible=[]
    for e,(v,axis,w) in enumerate(edges):
        x,y=vindex[v],vindex[w];a,b=(x,y) if x in a_set else (y,x)
        # Positive charge A->B lowers E if the stored edge is A->B.
        bit_required=int(x==a)
        adjacency[a][b]=(e,bit_required)
        if (c>>e)&1==bit_required:eligible.append((a,b,e,bit_required))
    degrees=Counter(x for a,b,e,sgn in eligible for x in (a,b))
    assert set(degrees)==set(range(len(vertices))) and set(degrees.values())=={d}
    m=len(eligible);assert m==d*len(vertices)//2
    # Enumerate complete four-hop Q paths by two distinct outgoing moves and
    # every allowed pair of return moves. No four-step path is guessed from a
    # desired plaquette. The two outgoing time orders have total weight 2;
    # the middle energy denominator 2 cancels this factor exactly.
    schur=Counter();midstates=0;return_ordered_paths=0
    for (a,b,e,sgn),(aa,bb,ee,ss) in itertools.combinations(eligible,2):
        if a==aa or b==bb:continue
        midstates+=1;field2=c^(1<<e)^(1<<ee)
        for dest,other_dest in ((b,bb),(bb,b)):
            for hole,other_hole in ((a,aa),(aa,a)):
                if dest not in adjacency[hole] or other_dest not in adjacency[other_hole]:continue
                f,required=adjacency[hole][dest];ff,rr=adjacency[other_hole][other_dest]
                # A B->A return is allowed in the complement of the outgoing domain.
                if (field2>>f)&1==required:continue
                field3=field2^(1<<f)
                if (field3>>ff)&1==rr:continue
                final=field3^(1<<ff);schur[final]-=1;return_ordered_paths+=2
    h4=dict(schur);h4[c]=h4.get(c,0)+m*m
    diagonal=len(vertices)*d*(2*d-1)//2
    expected={c:diagonal};flippable=[]
    for face in faces:
        r,l=face['r'],face['l']
        if (c&r==0 and c&l==l) or (c&r==r and c&l==0):
            target=c^r^l;expected[target]=expected.get(target,0)-2;flippable.append(target)
    assert h4==expected
    shared=len(vertices)*d*(d-1)//2
    assert midstates==m*(m-1)//2-shared
    # The first excursion has one A vacancy and one occupied B site. Its
    # remaining empty neighbors number 2d-1, independent of electric state.
    assert all(len(adjacency[a])-1==2*d-1 for a,b,e,sgn in eligible)
    return {'shape':shape,'vertices':len(vertices),'links':len(edges),
            'field_configuration_hex':hex(c),'eligible_first_hops':m,
            'eligible_degree_at_every_vertex':d,'distinct_Q_two_excursions':midstates,
            'four_hop_paths_including_time_orders':return_ordered_paths,
            'fourth_order_diagonal':diagonal,'offdiagonal_targets':len(flippable),
            'every_offdiagonal_coefficient':-2,'all_coefficients_exact':True,
            'vacant_edges_after_each_first_hop':2*d-1,
            'leading_birth_loss_over_beta_t2_over_Delta2':m*(2*d-1),
            'column_sha256':hashlib.sha256(json.dumps(sorted(h4.items())).encode()).hexdigest()}


def lattice_controls():
    rng=random.Random(2026092219);rows=[]
    for shape in ((6,6),(6,6,6)):
        vertices,edges,faces=geometry_source.geometry(shape,True)
        c=sum(1<<e for e,(v,a,w) in enumerate(edges) if sum(v[b] for b in range(len(shape)) if b!=a)%2==0)
        for trial in range(3):
            if trial:
                for _ in range(10*len(faces)):
                    face=rng.choice(faces);r,l=face['r'],face['l']
                    if (c&r==0 and c&l==l) or (c&r==r and c&l==0):c^=r^l
            rows.append(lattice_paths(shape,c))
    return rows


def live_birth_controls():
    basis,hop,penalty,n,jumps,gh=square_model((1,0,1,0),allow_birth=True)
    num=sp.diag(*n);loss=sum((j.T*j for j in jumps),sp.zeros(len(basis)))
    assert loss.is_diagonal()
    before=[i for i,k in enumerate(n) if k==2];after=[i for i,k in enumerate(n) if k==4]
    assert len(before)==7 and after
    for j in jumps:
        assert j.extract(before,range(len(basis)))==sp.zeros(len(before),len(basis))
    h=np.array(hop.extract(before,before),dtype=float)
    diagonal=np.array([penalty[i] for i in before],float)
    gamma=np.array([float(loss[i,i]) for i in before])
    assert np.array_equal(gamma,(diagonal==1).astype(float))
    low=[i for i,v in enumerate(diagonal) if v==0];assert len(low)==2
    psi=np.zeros(7,dtype=complex);psi[low[0]]=1
    result=[]
    # Fix the effective ring scale J=2 t^4/Delta^3, then increase both bare
    # scales with t/Delta shrinking. Birth is kept live with beta=1.
    for delta in (256.,1024.,4096.,16384.,65536.):
        ring=1.;t=(ring*delta**3/2)**.25;beta=1.;tau=np.pi/(2*ring)
        cond=delta*np.diag(diagonal)+t*h-.5j*beta*np.diag(gamma)
        final=la.expm(-1j*tau*cond)@psi
        survival=float(np.vdot(final,final).real)
        target=float(abs(final[low[1]])**2)
        vals=la.eigvals(cond);slow=sorted(vals,key=lambda x:abs(x))[:2]
        # Slow eigenvalues have common leading shift -2 t^2/Delta; use real
        # order to avoid a sort by imaginary magnitude hiding a branch.
        slow=sorted(slow,key=lambda x:x.real)
        widths=[float(-2*z.imag) for z in slow]
        predicted_loss=2*beta*t*t/(delta*delta+(beta/2)**2)
        assert 0<=target<=survival+1e-9<=1+1e-9
        assert max(abs(w/predicted_loss-1) for w in widths)<.35
        result.append({'Delta':delta,'hopping_t':t,'t_over_Delta':t/delta,
                       'beta':beta,'effective_ring_J':ring,'test_time':tau,
                       'no_birth_probability':survival,'unconditional_target_low_state_probability':target,
                       'exact_slow_decay_rates':widths,'leading_decay_rate':predicted_loss,
                       'exact_slow_coherent_ring':float((slow[1].real-slow[0].real)/2)})
    assert result[-1]['no_birth_probability']>.98 and result[-1]['unconditional_target_low_state_probability']>.96
    # Exact symbolic leading complex energies of the even/odd reflection blocks.
    t,a,D,E=sp.symbols('t a D E',nonzero=True)
    even=sp.Matrix([[0,-sp.sqrt(2)*t,0],[-sp.sqrt(2)*t,a,-2*t],[0,-2*t,2*D]])
    odd=sp.Matrix([[0,-sp.sqrt(2)*t],[-sp.sqrt(2)*t,a]])
    series={}
    for label,mat in [('even',even),('odd',odd)]:
        c2,c4=sp.symbols('c2 c4');char=(E*sp.eye(mat.rows)-mat).det()
        expr=sp.series(char.subs(E,c2*t*t+c4*t**4),t,0,6).removeO().expand()
        sol=sp.solve([expr.coeff(t,k) for k in (2,4)],(c2,c4),dict=True)
        assert len(sol)==1;series[label]={str(k):str(sp.factor(v)) for k,v in sol[0].items()}
    assert sp.simplify(sp.sympify(series['odd']['c4'],locals={'a':a,'D':D})-
                       sp.sympify(series['even']['c4'],locals={'a':a,'D':D})-4/(a*a*D))==0
    return {'full_physical_dimension':len(basis),'two_record_dimension':len(before),
            'four_record_dimension':len(after),'Gauss_and_permanent_count_checked':True,
            'two_record_basis':[basis[i] for i in before],
            'loss_diagonal_over_beta':gamma.tolist(),
            'reflection_block_low_series':series,'complex_first_excursion_energy':'a=Delta-i beta/2',
            'fixed_ring_live_birth_cases':result,
            'scope':'Exact finite first-birth survival; after one birth all four sites are occupied. No infinite-lattice phase or indefinite survival conclusion.'}


def main():
    started=time.monotonic()
    dep=hashlib.sha256((OUT/'local_gauge_record_cooling_check.py').read_bytes()).hexdigest()
    assert dep=='1dfd370af4b92bcff307a91314e610750e7b7961184a547f2f33d094027a8282'
    result={'status':'PASS','geometry_dependency_sha256':dep,'square':square_controls(),
            'periodic_lattice_path_columns':lattice_controls(),'live_formation':live_birth_controls(),
            'runtime_seconds':time.monotonic()-started}
    text=json.dumps(result,indent=2,default=str)+'\n'
    (OUT/'HARDCORE_RECORD_RING_AND_FORMATION_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':main()
