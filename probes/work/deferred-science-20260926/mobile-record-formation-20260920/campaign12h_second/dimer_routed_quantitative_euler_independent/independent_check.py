#!/usr/bin/env python3
"""Independent controls for the quantitative block/phase/error estimates."""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
import math,json
import numpy as np
from scipy.linalg import expm

OUT=Path(__file__).resolve().parent


def monotone_path(x,y):
    x=list(x);out=[tuple(x)]
    for i in range(3):
        while x[i]!=y[i]:
            x[i]+=1 if x[i]<y[i] else -1
            out.append(tuple(x))
    return out


def physical_counts():
    rows=[]
    for L in [3,5,7]:
        sites=list(product(range(L),repeat=3));counts=Counter()
        for x in sites:
            for y in sites:
                path=monotone_path(x,y)
                es=[tuple(sorted(e)) for e in zip(path,path[1:])]
                assert len(es)==len(set(es))
                counts.update(es)
        assert len(counts)==3*(L-1)*L**2
        for (x,y),count in counts.items():
            axis=next(i for i in range(3) if x[i]!=y[i]);a=x[axis]+1
            assert count==2*a*(L-a)*L**2
            assert 2*count<=L**4
        rows.append(dict(L=L,ordered_pairs=L**6,physical_edges=len(counts),
                         maximum_load=max(counts.values()),claimed_bound=str(Fraction(L**4,2))))
    return rows


class Geometry:
    def __init__(self,N,kind,seed=420061):
        self.N=N;self.xyz=list(product(range(N),repeat=3));self.lookup={v:i for i,v in enumerate(self.xyz)}
        self.black=[x for x in self.xyz if sum(x)%2==0]
        self.bi={x:i for i,x in enumerate(self.black)}
        self.mate={}
        for x in self.xyz:
            if (sum(x)%2==0 if kind=='winding' else x[0]%2==0):
                y=self.move(x,0,1);self.mate[x]=y;self.mate[y]=x
        accepted=0
        if kind=='irregular':
            rng=np.random.default_rng(seed);planes=list(combinations(range(3),2))
            for _ in range(8*N**3):
                x=self.xyz[int(rng.integers(N**3))];i,j=planes[int(rng.integers(3))]
                b=self.move(x,i,1);d=self.move(x,j,1);c=self.move(b,j,1)
                if self.mate[x]==b and self.mate[d]==c:
                    self.mate[x]=d;self.mate[d]=x;self.mate[b]=c;self.mate[c]=b
                elif self.mate[x]==d and self.mate[b]==c:
                    self.mate[x]=b;self.mate[b]=x;self.mate[d]=c;self.mate[c]=d
                else:continue
                accepted+=1
        self.accepted=accepted
        self.owner={x:self.bi[x if sum(x)%2==0 else self.mate[x]] for x in self.xyz}
        assert all(self.mate[self.mate[x]]==x for x in self.xyz)

    def move(self,x,axis,sign):
        y=list(x);y[axis]=(y[axis]+sign)%self.N;return tuple(y)

    def local(self,l,center=(0,0,0)):
        offsets=list(product(range(-l,l+1),repeat=3))
        embedded={r:tuple((center[i]+r[i])%self.N for i in range(3)) for r in offsets}
        owners={r:self.owner[x] for r,x in embedded.items()}
        representatives={}
        for r in offsets:representatives.setdefault(owners[r],r)
        blackset={self.bi[x] for x in embedded.values() if sum(x)%2==0}
        multiplicity=Counter()
        for r in offsets:
            for i in range(3):
                s=list(r);s[i]+=1;s=tuple(s)
                if s in owners and owners[r]!=owners[s]:multiplicity[tuple(sorted((owners[r],owners[s])))]+=1
        assert max(multiplicity.values())<=2
        adjacency={v:set() for v in representatives}
        for a,b in multiplicity:adjacency[a].add(b);adjacency[b].add(a)
        visited={next(iter(adjacency))};todo=list(visited)
        while todo:
            for v in adjacency[todo.pop()]-visited:visited.add(v);todo.append(v)
        assert len(visited)==len(representatives)
        return owners,representatives,blackset,multiplicity


def footprint_words():
    rows=[]
    # l=2 exhaustively tests the same geometric gap sublemma (no current is
    # inserted). l=6,N=36 is in the theorem's application range and stresses
    # a wrapping physical boundary; endpoint pairs there are preselected.
    for l,N in [(2,16),(6,36)]:
        L=2*l+1
        for kind in ['columnar','irregular']:
            g=Geometry(N,kind,420061+N);owners,reps,ordinary,mult=g.local(l)
            m=len(reps);assert 2*m>=L**3 and ordinary<=set(reps)
            allpairs=list(combinations(sorted(reps),2))
            full=l==2
            selected=allpairs if full else [allpairs[i] for i in np.linspace(0,len(allpairs)-1,6000,dtype=int)]
            load=Counter();wordload=Counter();weighted=Counter();maxlen=0
            for a,b in selected:
                route=monotone_path(reps[a],reps[b]);raw=[owners[x] for x in route]
                stack=[];position={}
                for v in raw:
                    if v in position:
                        for removed in stack[position[v]+1:]:del position[removed]
                        stack=stack[:position[v]+1]
                    else:position[v]=len(stack);stack.append(v)
                assert stack[0]==a and stack[-1]==b and len(stack)==len(set(stack))
                edges=[tuple(sorted(e)) for e in zip(stack,stack[1:])]
                assert all(e in mult for e in edges)
                assert set(edges)<={tuple(sorted(e)) for e in zip(raw,raw[1:]) if e[0]!=e[1]}
                ell=len(edges);assert ell<=3*(L-1)
                word=edges+edges[-2::-1];assert len(word)==2*ell-1<=6*L
                tokens={v:v for v in stack}
                for x,y in word:tokens[x],tokens[y]=tokens[y],tokens[x]
                assert tokens[a]==b and tokens[b]==a and all(tokens[v]==v for v in stack[1:-1])
                load.update(edges);wordload.update(word)
                for e in word:weighted[e]+=len(word)
                maxlen=max(maxlen,ell)
            assert max(load.values())<=L**4 and max(wordload.values())<=2*L**4
            assert max(weighted.values())<=12*L**5
            # Boundary normalization coefficients, evaluated exactly.
            mb=len(ordinary);extra=m-mb
            coefficient_squared=Fraction(extra,m*m)+mb*(Fraction(1,m)-Fraction(1,mb))**2
            assert mb==(L**3+(-1)**l)//2
            assert extra<=6*L**2
            rows.append(dict(radius=l,N=N,kind=kind,pairs=m,black_sites=mb,
                boundary_extra_pairs=extra,largest_edge_multiplicity=max(mult.values()),
                accepted_matching_construction_flips=g.accepted,reference_pairs_checked=len(selected),
                exhaustive_endpoint_inventory=full,maximum_word_path_length=maxlen,
                maximum_weighted_congestion=max(weighted.values()),claimed_congestion=12*L**5,
                exact_unit_form_Poincare_constant=48*L**2,
                exact_boundary_coefficient_squared=str(coefficient_squared),
                scaled_boundary_coefficient_l4=float(coefficient_squared*l**4)))
    return rows


def smoothing_phase():
    # Exact membership and independent convolution controls for the phase lemma.
    # A small radius suffices here; this control does not insert a four-site
    # current or stand in for the theorem's l>=6 application.
    N,l=16,2;g=Geometry(N,'irregular',620211);K=len(g.black);L=2*l+1
    offsets=list(product(range(-l,l+1),repeat=3));black_offsets=[r for r in offsets if sum(r)%2==0]
    mb=len(black_offsets);assert mb==(L**3+1)//2
    ordinary=[];geometric=[]
    for u in g.black:
        ordinary.append([g.bi[tuple((u[i]+r[i])%N for i in range(3))] for r in black_offsets])
        geometric.append(sorted({g.owner[tuple((u[i]+r[i])%N for i in range(3))] for r in offsets}))
    membership=np.bincount(np.concatenate(ordinary),minlength=K)
    cmembership=np.bincount(np.concatenate(geometric),minlength=K)
    assert np.all(membership==mb)
    assert min(map(len,geometric))>=L**3/2 and max(cmembership)<=L**3
    Q=2*np.pi*np.array([1,2,-1]);coords=np.array(g.black);phi=np.exp(-1j*coords@Q/N)
    def coefficients(blocks,b):
        c=np.zeros(K,dtype=complex)
        for u,block in enumerate(blocks):np.add.at(c,block,b[u]/len(block))
        return c
    simple=coefficients(ordinary,phi);irregular=coefficients(geometric,phi)
    assert max(abs(simple))<=1+1e-13 and max(abs(irregular))<=2+1e-13
    multiplier=np.mean(np.exp(1j*np.array(black_offsets)@Q/N))
    assert max(abs(simple-multiplier*phi))<3e-14
    assert abs(multiplier-1)<=np.sqrt(3)*np.linalg.norm(Q)*l/N
    phase_rows=[]
    for axis,sign in product(range(3),[-1,1]):
        delta=np.eye(3,dtype=int)[axis]*sign
        q=np.array([g.owner[g.move(u,axis,sign)] for u in g.black])
        dv=[]
        for v in q:
            u=g.black[v];w=g.mate[u];step=np.zeros(3,dtype=int)
            for ax in range(3):
                z=(w[ax]-u[ax])%N
                if z:step[ax]=1 if z==1 else -1
            dv.append(step)
        displacement=delta-np.array(dv)
        a=N*(phi[q]-phi)
        linear=-1j*phi*(displacement@Q)
        rem=a-linear
        bound=2*float(Q@Q)/N
        assert max(abs(rem))<=bound+1e-12
        c=coefficients(ordinary,rem)
        cc=coefficients(geometric,rem)
        assert max(abs(c))<=max(abs(rem))+1e-12
        assert max(abs(cc))<=2*max(abs(rem))+1e-12
        phase_rows.append(dict(axis=axis,sign=sign,maximum_phase_remainder=float(max(abs(rem))),
              Taylor_bound=bound,ordinary_coefficient_max=float(max(abs(c))),
              geometric_coefficient_max=float(max(abs(cc))),
              ordinary_Bernoulli_variance=float(np.vdot(c,c).real/(4*K))))
    return dict(N=N,radius=l,ordinary_membership_count=mb,geometric_maximum_membership=int(max(cmembership)),
        ordinary_Fourier_multiplier=[multiplier.real,multiplier.imag],phase_rows=phase_rows)


def canonical_and_propagation():
    p=Fraction(1,3);rows=[]
    for m in [4,7,13,31,64]:
        ew=ew2=fourth=Fraction(0)
        for n in range(m+1):
            probability=math.comb(m,n)*p**n*(1-p)**(m-n)
            q=Fraction(n,m);hat=Fraction(n*(n-1),m*(m-1))
            w=hat-p*p-2*p*(q-p)
            ew+=probability*w;ew2+=probability*w*w;fourth+=probability*(q-p)**4
        target=2*p*p*(1-p)**2/Fraction(m*(m-1))
        expectedfourth=3*p*p*(1-p)**2/m**2+p*(1-p)*(1-6*p*(1-p))/m**3
        assert ew==0 and ew2==target and fourth==expectedfourth
        rows.append(dict(m=m,centered_U_statistic_mean=str(ew),exact_W_variance=str(ew2),
                         scaled_m2_W_variance=str(m*m*ew2),empirical_fourth=str(fourth)))
    A=np.array([[1.,3.],[0.,-2.]]);norm=float(np.linalg.norm(A,2));T=.4
    controls=[]
    for omega in [1.,17.,203.]:
        eta=.01;v=np.array([1.,1.])/np.sqrt(2);G=np.zeros((6,6),complex)
        G[:2,:2]=-1j*A;G[:2,5]=eta*omega*v;G[2:4,:2]=np.eye(2)
        G[4,5]=omega;G[5,4]=-omega
        initial=np.zeros(6,complex);initial[5]=1
        maximum=0.;residual=0.
        for t in np.linspace(0,T,41):
            z=expm(t*G)@initial;R=eta*math.sin(omega*t)*v
            residual=max(residual,float(np.linalg.norm(z[:2]-R+1j*A@z[2:4])))
            maximum=max(maximum,float(np.vdot(z[:2],z[:2]).real))
        bound=2*eta**2*math.exp(2*norm**2*T*T)
        assert residual<1e-12 and maximum<=bound
        controls.append(dict(forcing_frequency=omega,maximum_squared_error=maximum,
                             Gronwall_upper_bound=bound,integral_equation_residual=residual))
    return dict(exact_canonical_controls=rows,nonnormal_propagation_controls=controls,
                interpretation='Canonical controls are a scalar sampling/moment sublemma, not an alternative color model. Propagation control uses a nonnormal fixed matrix and bounded integrated forcing.')


if __name__=='__main__':
    result={}
    result['open_cube_paths']=physical_counts();print('open cube loads done',flush=True)
    result['contracted_footprints']=footprint_words();print('boundary footprints and immutable words done',flush=True)
    result['smoothing_and_phase']=smoothing_phase();print('phase and membership done',flush=True)
    result['canonical_and_propagation']=canonical_and_propagation();print('moment and propagation controls done',flush=True)
    result['scope']='Independent before author quantitative checker/results. Exact integer/Fraction sublemma controls separated from floating phase and matrix calculations.'
    (OUT/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','matched_footprints':len(result['contracted_footprints'])}))
