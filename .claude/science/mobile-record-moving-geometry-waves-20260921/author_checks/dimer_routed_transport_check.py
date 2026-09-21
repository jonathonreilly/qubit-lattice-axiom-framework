#!/usr/bin/env python3
"""Author controls for parity-independent whole-pair routing and quenched waves."""
from pathlib import Path
from collections import Counter, deque
import datetime, hashlib, itertools, json, math, sys
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
AXES = np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)], dtype=int)
EV = np.vstack((AXES, np.zeros((8,3),dtype=int)))
BV = np.vstack((np.zeros((6,3),dtype=int), np.array(list(itertools.product((-1,1),repeat=3)))))
S2 = np.stack([np.cross(EV[:,None,:],BV[None,:,:])[:,:,i] +
               np.cross(EV[None,:,:],BV[:,None,:])[:,:,i] for i in range(3)])
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def proper_rotations():
    out=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1,1),repeat=3):
            R=np.zeros((3,3),dtype=int)
            for j in range(3): R[perm[j],j]=signs[j]
            if round(np.linalg.det(R))==1: out.append(R)
    assert len(out)==24
    return out

def make_lattice(N):
    xyz=np.array(list(itertools.product(range(N),repeat=3)),dtype=int)
    index=lambda a: np.ravel_multi_index(tuple((np.asarray(a)%N).T),(N,N,N))
    neighbors=np.stack([index(xyz+d) for d in AXES])
    return xyz,index,neighbors

def matching(N,flips,seed,axis=0,sign=1,winding=False):
    xyz,index,nb=make_lattice(N); parity=xyz.sum(axis=1)%2
    black=np.flatnonzero(parity==0)
    directions=np.full(len(black),sign) if winding else sign*(1-2*(xyz[black,axis]%2))
    white=index(xyz[black]+directions[:,None]*np.eye(3,dtype=int)[axis])
    partner=np.full(N**3,-1,dtype=int); partner[black]=white;partner[white]=black
    rng=np.random.default_rng(seed);accepted=0
    for _ in range(flips):
        a=int(rng.integers(N**3));i,j=rng.choice(3,2,replace=False)
        b=int(nb[2*i,a]);d=int(nb[2*j,a]);c=int(nb[2*j,b])
        if partner[a]==b and partner[d]==c:
            partner[a]=d;partner[d]=a;partner[b]=c;partner[c]=b;accepted+=1
        elif partner[a]==d and partner[b]==c:
            partner[a]=b;partner[b]=a;partner[d]=c;partner[c]=d;accepted+=1
    assert np.all(partner[partner]==np.arange(N**3))
    assert np.all(np.any(nb==partner[None,:],axis=0))
    if flips and not winding: assert accepted>0
    return partner,accepted

def routing(N,partner,parity=0):
    xyz,index,nb=make_lattice(N);black=np.flatnonzero(xyz.sum(axis=1)%2==parity)
    white=partner[black];where=np.full(N**3,-1,dtype=int);where[black]=np.arange(len(black))
    q=np.stack([where[partner[nb[i,black]]] for i in range(6)])
    d=np.zeros((len(black),3),dtype=int)
    for i,delta in enumerate(AXES): d[white==nb[i,black]]=delta
    inv=np.argsort(q,axis=1)
    for z in q: assert np.array_equal(np.sort(z),np.arange(len(black)))
    assert np.all(np.sum(abs(d),axis=1)==1)
    return xyz,index,nb,black,white,d,q,inv

def drive2(delta,colors,l,a,b,r):
    axis=int(np.flatnonzero(delta)[0]);sgn=int(delta[axis]);S=S2[axis]*sgn
    return int(S[colors[l],colors[a]]+S[colors[a],colors[r]]-
               S[colors[l],colors[b]]-S[colors[b],colors[r]])

def events(N,partner,site_colors,parity=0):
    xyz,index,nb,black,white,d,q,inv=routing(N,partner,parity)
    colors=site_colors[black];out=Counter()
    for j,delta in enumerate(AXES):
        for u,v in enumerate(q[j]):
            if u==v: continue
            l=int(inv[j,u]);r=int(q[j,v])
            assert len({l,u,int(v),r})==4
            action=tuple(sorted((tuple(sorted((int(black[u]),int(black[v])))),
                                 tuple(sorted((int(white[u]),int(white[v])))))))
            out[action]+=8+drive2(delta,colors,l,u,int(v),r)
    return out  # actual event rate is numerator/8, with k0=2,gamma=1.

def geometric_controls():
    rows=[];rng=np.random.default_rng(91521)
    for N in [8,10,12]:
        for sample in range(4):
            partner,accepted=matching(N,0 if sample==0 else 8*N**3,1000+N+sample,
                                     axis=sample%3,sign=-1 if sample==3 else 1,winding=sample==0)
            xyz,index,nb,black,white,d,q,inv=routing(N,partner)
            K=len(black);cycle_lengths=[];winding=[];edges=set()
            for j,delta in enumerate(AXES):
                displacement=delta-d[q[j]]
                assert np.array_equal(index(xyz[black]+displacement),black[q[j]])
                assert np.array_equal(displacement.sum(axis=0),K*delta-d.sum(axis=0))
                assert np.all(np.sum(abs(displacement),axis=1)<=2)
                seen=set()
                for u in range(K):
                    if u in seen:continue
                    cycle=[];v=u
                    while v not in seen:seen.add(v);cycle.append(v);v=int(q[j,v])
                    assert v==u
                    if len(cycle)==1:
                        assert np.array_equal(d[u],delta);continue
                    assert len(cycle)>=N//2
                    steps=displacement[cycle];progress=steps@delta
                    assert np.all((progress>=1)&(progress<=2))
                    total=steps.sum(axis=0);assert np.all(total%N==0)
                    cycle_lengths.append(len(cycle));winding.append((total//N).tolist())
                for u,v in enumerate(q[j]):
                    if u!=v:edges.add(tuple(sorted((u,int(v)))))
            adj=[set() for _ in range(K)]
            for u,v in edges:adj[u].add(v);adj[v].add(u)
            reached={0};todo=[0]
            for u in todo:
                for v in adj[u]-reached:reached.add(v);todo.append(v)
            assert len(reached)==K
            ids=np.empty(N**3,dtype=int);ids[black]=2*np.arange(K);ids[white]=2*np.arange(K)+1
            selected=[]
            for j in range(6):
                candidates=np.flatnonzero(q[j]!=np.arange(K))
                if not len(candidates):continue
                for u in rng.choice(candidates,min(8,len(candidates)),replace=False):
                    v=q[j,u];new=ids.copy()
                    new[[black[u],black[v]]]=new[[black[v],black[u]]]
                    new[[white[u],white[v]]]=new[[white[v],white[u]]]
                    assert np.array_equal(np.sort(new),np.arange(N**3))
                    assert np.all((new^new[partner])==1)
                    positions=np.argsort(new);dist=(xyz[positions]-xyz[np.argsort(ids)]+N//2)%N-N//2
                    assert np.all(np.sum(abs(dist),axis=1)<=2)
                    selected.append([j,int(u),int(v)])
            colors=rng.integers(14,size=K);site_colors=np.empty(N**3,dtype=int)
            site_colors[black]=colors;site_colors[white]=colors
            forward=events(N,partner,site_colors,0);reverse=events(N,partner,site_colors,1)
            assert forward==reverse
            rows.append(dict(N=N,sample=sample,accepted_geometry_flips=accepted,pairs=K,
                             directed_nonfixed_channels=int(np.sum(q!=np.arange(K))),
                             nontrivial_cycles=len(cycle_lengths),minimum_cycle=min(cycle_lengths),
                             largest_cycle=max(cycle_lengths),distinct_pair_edges=len(edges),
                             immutable_replays=len(selected),parity_independent_aggregated_rates=True))
    # N=4 really has two-cycles; it cannot use the distinct-four-position proof.
    p,_=matching(4,0,1);q=routing(4,p)[6];lengths=[]
    for perm in q:
        for u in range(len(perm)):
            if perm[u]!=u and perm[perm[u]]==u:lengths.append(2)
    assert lengths
    return dict(rows=rows,short_torus_countercontrol='N=4 columnar routing contains nontrivial 2-cycles')

def local_controls():
    words=np.array(list(itertools.product(range(14),repeat=4)),dtype=np.int64)
    l,a,b,r=words.T;out=[]
    for i in range(3):
        S=S2[i];h=S[l,a]+S[a,r]-S[l,b]-S[b,r]
        assert h.min()==-4 and h.max()==4
        hs=S[l,b]+S[b,r]-S[l,a]-S[a,r];assert np.array_equal(hs,-h)
        total=np.zeros(len(words),dtype=int)
        for j in range(4):
            ll,aa,bb,rr=words[:,np.array([j-1,j,j+1,j+2])%4].T
            total+=S[ll,aa]+S[aa,rr]-S[ll,bb]-S[bb,rr]
        assert np.all(total==0)
        reversed_words=words[:,::-1];ll,aa,bb,rr=reversed_words.T
        assert np.array_equal(-(S[ll,aa]+S[aa,rr]-S[ll,bb]-S[bb,rr]),h)
        for weights in [np.ones(14,dtype=np.int64),np.arange(1,15,dtype=np.int64),
                        np.array([2]*6+[3]*8,dtype=np.int64)]:
            den=int(weights.sum());X=weights@EV;Y=weights@BV;mass=np.prod(weights[words],axis=1)
            numerator=weights[:,None]*(den*(np.cross(EV,Y)+np.cross(X,BV))-2*np.cross(X,Y))
            direct=np.array([np.sum(mass*(8+h)*((a==c).astype(int)-(b==c).astype(int))) for c in range(14)])
            assert np.array_equal(direct,4*den*numerator[:,i])
        out.append(dict(axis=i,words=len(words),drive2_range=[int(h.min()),int(h.max())],
                        all_cycle_balance=True,three_exact_rational_currents=True))
    return dict(rows=out,total_six_direction_words=6*len(words),actual_rate_range=['1/2','3/2'])

def symmetry_and_code():
    x,y,z=sp.symbols('x y z',real=True)
    f=sp.Matrix([y*z*(y*y-z*z),z*x*(z*z-x*x),x*y*(x*x-y*y)])
    n=sp.Matrix([x,y,z]);label_lookup={tuple(np.r_[EV[a],BV[a]]):a for a in range(14)}
    def raw_f(v):
        a,b,c=map(int,v);return np.array([b*c*(b*b-c*c),c*a*(c*c-a*a),a*b*(a*a-b*b)],dtype=np.int64)
    def label(v):
        fv=raw_f(v)
        if not np.all(fv):return None
        if 100*max(abs(fv))**2>81*int(fv@fv):
            e=np.zeros(3,dtype=int);i=int(np.argmax(abs(fv)));e[i]=int(np.sign(fv[i]));b=np.zeros(3,dtype=int)
        else:e=np.zeros(3,dtype=int);b=np.sign(fv)
        return label_lookup[tuple(np.r_[e,b])]
    rotations=proper_rotations();tested=0;counts=Counter()
    for R in rotations:
        transformed=sp.Matrix(R)*n
        g=f.subs(dict(zip((x,y,z),transformed)),simultaneous=True)-sp.Matrix(R)*f
        assert all(sp.expand(a)==0 for a in g)
        assert all(sp.expand(a)==0 for a in f.subs({x:-x,y:-y,z:-z},simultaneous=True)-f)
    vectors=set(itertools.product(range(-4,5),repeat=3))
    for R in rotations:
        for sign in [-1,1]: vectors.add(tuple(sign*(R@np.array([1,4,8]))))
    for v in sorted(vectors):
        a=label(v)
        if a is None:continue
        assert label(tuple(-np.array(v)))==a;counts[a]+=1
        for R in rotations:
            target=label_lookup[tuple(np.r_[R@EV[a],R@BV[a]])]
            assert label(R@v)==target;tested+=1
    assert set(counts)==set(range(14))
    assert len(set(counts[a] for a in range(6)))==1
    assert len(set(counts[a] for a in range(6,14)))==1
    # Conjugate all physical actions, using several rotations and all unit
    # translations. Aggregated rate comparison includes duplicate channels.
    N=8;partner,_=matching(N,8*N**3,662);xyz,index,nb,black,white,d,q,inv=routing(N,partner)
    colors=np.random.default_rng(102).integers(14,size=len(black));site=np.empty(N**3,dtype=int)
    site[black]=colors;site[white]=colors;base=events(N,partner,site)
    cases=[]
    for R,shift in [(R,np.zeros(3,dtype=int)) for R in rotations]+[(np.eye(3,dtype=int),d) for d in AXES]:
        perm=index(xyz@R.T+shift);newpartner=np.empty_like(partner);newpartner[perm]=perm[partner]
        color_perm=np.array([label_lookup[tuple(np.r_[R@EV[a],R@BV[a]])] for a in range(14)])
        newsite=np.empty_like(site);newsite[perm]=color_perm[site]
        expected=Counter()
        for action,value in base.items():
            transformed=tuple(sorted(tuple(sorted((int(perm[u]),int(perm[v])))) for u,v in action))
            expected[transformed]+=value
        assert events(N,newpartner,newsite)==expected
        cases.append(dict(rotation=R.tolist(),translation=shift.tolist()))
    return dict(exact_quartic_covariance_rotations=24,integer_content_tests=tested,
                sampled_label_counts=dict(counts),physical_rate_conjugacies=len(cases),
                formation_even_region_first_moments='Exactly zero by n -> -n; no numerical quadrature assumed.')

def wave_and_current_matrix():
    E=sp.Matrix(EV.T.tolist());B=sp.Matrix(BV.T.tolist())
    p=sp.Matrix([sp.Rational(1,14)]*14);C=sp.diag(*p)-p*p.T
    k=sp.Matrix([1,2,-1]);cross=lambda v:sp.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
    As=[]
    for i in range(3):
        v=sp.eye(3)[:,i];H=E.T*(-cross(v))*B+B.T*cross(v)*E
        A=C*H;assert A*C==C*A.T;As.append(A)
    A=sum((k[i]*As[i] for i in range(3)),sp.zeros(14));speed2=sp.Rational(4,49)*(k.dot(k))
    assert A**3==speed2*A
    assert A.rank()==4
    tangent=sp.eye(14)[:,:13]-sp.ones(14,1)*sp.zeros(1,13)
    tangent[13,:]=-sp.ones(1,13)
    reduced=(A*tangent)[:13,:]
    lam=sp.symbols('lambda');poly=reduced.charpoly(lam).as_expr()
    assert sp.factor(poly-lam**9*(lam**2-speed2)**2)==0
    expected_x=-sp.Rational(1,7)*cross(k)*B
    expected_y=sp.Rational(4,7)*cross(k)*E
    assert E*A==expected_x and B*A==expected_y
    assert E*C*E.T==sp.eye(3)/7 and B*C*B.T==4*sp.eye(3)/7
    # Exact unwrapped total product-current cancellation for anisotropic colors.
    w=sp.Matrix(list(range(1,15)));p2=w/sum(w);X=E*p2;Y=B*p2
    J=sp.Matrix.hstack(*[p2[a]*(E[:,a].cross(Y)+X.cross(B[:,a])-2*X.cross(Y)) for a in range(14)])
    rows=[]
    for N in [8,10]:
        partner,_=matching(N,9*N**3,317+N);d=routing(N,partner)[5]
        D=sp.Matrix(d.sum(axis=0).tolist());K=N**3//2;total=sp.zeros(3,14)
        for delta in AXES:
            dv=sp.Matrix(delta.tolist());total+=(K*dv-D)*(dv.T*J)/2
        assert total==K*J
        rows.append(dict(N=N,dimer_direction_sum=list(map(int,D)),exact_current_cancellation=True))
    return dict(speed_squared_at_equal_colors=str(speed2),tangent_characteristic_polynomial=str(sp.factor(poly)),
                propagating_rank=4,zero_speed_tangent_dimensions=9,geometry_current_controls=rows)

def block_geometry_and_smoothing():
    rows=[];N=32;partner,accepted=matching(N,10*N**3,9813)
    xyz,index,nb,black,white,d,q,inv=routing(N,partner);K=len(black)
    pairid=np.empty(N**3,dtype=int);pairid[black]=np.arange(K);pairid[white]=np.arange(K)
    for anchor in [0,K//7,K//3,K-1]:
        center=xyz[black[anchor]]
        dist=(xyz-center+N//2)%N-N//2
        for ell in [2,4,6]:
            sites=np.flatnonzero(np.max(abs(dist),axis=1)<=ell);C=set(map(int,pairid[sites]))
            Bset=set(map(int,pairid[sites[xyz[sites].sum(axis=1)%2==0]]))
            assert Bset<=C and len(C)-len(Bset)<=6*(2*ell+3)**2
            adj={u:set() for u in C}
            mask=np.zeros(N**3,dtype=bool);mask[sites]=True
            for x in sites:
                for z in nb[:,x]:
                    if mask[z]:adj[int(pairid[x])].add(int(pairid[z]))
            seen={next(iter(C))};todo=list(seen)
            for u in todo:
                for v in adj[u]-seen:seen.add(v);todo.append(v)
            assert seen==C
            if ell>=6:
                for j in range(6):
                    footprint={anchor,int(inv[j,anchor]),int(q[j,anchor]),int(q[j,q[j,anchor]])}
                    assert footprint<=C
            # Exact coefficient squared norm for the two conditional averages.
            variance=sum((sp.Rational(int(u in C),len(C))-sp.Rational(int(u in Bset),len(Bset)))**2 for u in C)
            assert variance==sp.Rational(1,len(Bset))-sp.Rational(1,len(C))
            rows.append(dict(anchor=anchor,ell=ell,black_cube=len(Bset),touching_pairs=len(C),
                             internal_contraction_connected=True,average_difference_variance=str(variance)))
    # Conditional on this geometry, iid scalar variance one makes the squared
    # coefficient norm exactly the variance of the smoothed direction term.
    coeff=np.zeros((3,N**3),dtype=float);Q=np.array([1.,2.,-1.])
    for j,delta in enumerate(AXES):
        coeff[:,black]+=.5*delta[:,None]*(d[q[j]]@Q)[None,:]
    assert np.max(abs(coeff.sum(axis=1)))==0
    bare=float(np.sum(coeff**2)/K);assert bare>0
    smooth=[]
    transforms=np.fft.fftn(coeff.reshape(3,N,N,N),axes=(1,2,3))
    for ell in [1,2,4,6,8]:
        kernel=np.zeros((N,N,N),dtype=float);count=0
        for off in itertools.product(range(-ell,ell+1),repeat=3):
            if sum(off)%2==0:kernel[tuple(np.array(off)%N)]=1;count+=1
        kernel/=count
        filtered=np.fft.ifftn(transforms*np.fft.fftn(kernel),axes=(1,2,3)).real.reshape(3,-1)
        var=float(np.sum(filtered[:,black]**2)/K)
        smooth.append(dict(ell=ell,exact_linear_variance_numerically_evaluated=var,black_block_size=count))
    assert smooth[-1]['exact_linear_variance_numerically_evaluated']<bare/10
    return dict(N=N,accepted_geometry_flips=accepted,connected_block_controls=rows,
                unsmoothed_direction_variance=bare,smoothing=smooth,
                scope='Finite geometric/canonical coefficient controls; no numerical proof of the limit or mixing constants.')

def main():
    out=HERE/'dimer_routed_transport_checks';out.mkdir(exist_ok=False)
    groups=[]
    for name,fn in [('geometry',geometric_controls),('local',local_controls),
                    ('symmetry_and_code',symmetry_and_code),('wave',wave_and_current_matrix),
                    ('blocks',block_geometry_and_smoothing)]:
        value=fn();(out/(name+'.json')).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
        groups.append(dict(group=name,passed=True,detail=value))
        print(json.dumps(dict(group=name,passed=True)),flush=True)
    result=dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                sources_sha256={Path(__file__).name:sha(__file__),'DIMER_ROUTED_RECORD_TRANSPORT.md':sha(HERE/'DIMER_ROUTED_RECORD_TRANSPORT.md')},
                groups=groups,scope='Author controls. The continuum limit relies on the explicit finite-block proof, not these finite examples.')
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print('PASS: five complete dimer-routed transport groups',flush=True)

if __name__=='__main__':main()
