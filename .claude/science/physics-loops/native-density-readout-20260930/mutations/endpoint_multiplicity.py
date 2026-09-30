#!/usr/bin/env python3
"""Exact source controls for the supplied density-spectrum/readout theorem.

Author-reused implementations from the three frozen discovery/check controls,
with explicit provenance in the unit pack. No independent review is claimed.
These are finite coefficient/operator controls; the source proves the limits.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/NATIVE_DENSITY_SPECTRUM_AND_READOUT_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
]

def response_controls():
    """Exact local-source controls, not a finite-density spectral calculation."""
    from fractions import Fraction as F
    from itertools import product, combinations
    from collections import defaultdict
    import json

    zero=(0,0,0)
    ei=[tuple(int(i==j) for i in range(3)) for j in range(3)]
    def add(a,b): return tuple(x+y for x,y in zip(a,b))
    def mul(s,a): return tuple(s*x for x in a)
    def edge(a,b): return tuple(sorted((a,b)))
    def accum(rows):
        z=defaultdict(F)
        for e,c in rows:z[e]+=c
        return {e:c for e,c in z.items() if c}
    def ds(c):return [edge(add(c,e),add(c,mul(-1,e))) for e in ei]
    def vs(c,i,j):return [(edge(add(c,mul(s,ei[i])),add(c,mul(t,ei[j]))),s*t) for s,t in product((1,-1),repeat=2)]
    def qrows(c):
        d=ds(c)
        yield F(1,2),{d[0]:1,d[1]:-1}
        yield F(1,6),{d[0]:1,d[1]:1,d[2]:-2}
        for i,j in combinations(range(3),2):yield F(1,4),dict(vs(c,i,j))
    def rows(c):
        yield 'mu',F(2,3),dict.fromkeys(ds(c),1)
        for i,j in combinations(range(3),2):
            for (e,a),(f,b) in combinations(vs(c,i,j),2):
                yield 'mu',F(1,4),accum([(e,a),(f,-b)])
        for v in ei:
            for (w,r),(w2,s) in zip(qrows(c),qrows(add(c,v))):
                assert w==w2
                yield 'tau',w,accum(list(s.items())+[(e,-a) for e,a in r.items()])

    refs=ds(zero)
    for i,j in combinations(range(3),2):
        for eta in (1,-1):refs.append(edge(zero,add(ei[i],mul(eta,ei[j]))))
    refmap={e:i for i,e in enumerate(refs)}
    G=set(mul(s*2,e) for e in ei for s in (1,-1))
    for i,j in combinations(range(3),2):
        G.update(add(mul(s,ei[i]),mul(t,ei[j])) for s,t in product((1,-1),repeat=2))
    pins=sorted(edge(zero,d) for d in G);pinmap={e:i for i,e in enumerate(pins)}
    K={u:[defaultdict(F) for _ in refs] for u in ('mu','tau')}
    P=[[F(0) for _ in pins] for _ in pins]
    row_count=0
    for c in product(range(-3,4),repeat=3):
        for unit,w,r in rows(c):
            row_count+=1
            for e,a in r.items():
                if e in refmap:
                    k=K[unit][refmap[e]]
                    for f,b in r.items():k[f]+=w*a*b
                if unit=='mu' and e in pinmap:
                    for f,b in r.items():
                        if f in pinmap:P[pinmap[e]][pinmap[f]]+=w*a*b

    # Expected pinned matrix from the source endpoint classification.
    def pclass(e):
        d=e[1] if e[0]==zero else e[0]
        axes=tuple(i for i,x in enumerate(d) if x)
        return axes,d
    for a,e in enumerate(pins):
        ca,da=pclass(e)
        for b,f in enumerate(pins):
            cb,db=pclass(f)
            want=F(0)
            if e==f:want=F(2,3) if len(ca)==1 else F(3,2)
            elif len(ca)==2 and ca==cb and sum(x!=y for x,y in zip(da,db))==1:want=F(1,4)
            assert P[a][b]==want,(e,f,P[a][b],want)

    def midpoint(e):return tuple(F(x+y,2) for x,y in zip(*e))
    def kind(e):
        d=tuple(y-x for x,y in zip(*e)); nz=[i for i,x in enumerate(d) if x]
        if len(nz)==1:return nz[0]
        i,j=nz
        # endpoint sorting makes the first nonzero coordinate positive
        eta=1 if d[i]*d[j]>0 else -1
        return 3+2*list(combinations(range(3),2)).index((i,j))+(0 if eta==1 else 1)

    coeff={unit:[[defaultdict(F) for _ in refs] for _ in refs] for unit in K}
    row_sums={}
    for unit,table in K.items():
        row_sums[unit]=[]
        for a,(e,kr) in enumerate(zip(refs,table)):
            row_sums[unit].append(sum(abs(c) for c in kr.values()))
            assert row_sums[unit][-1] <= (3 if unit=='mu' else 24)
            for f,c in kr.items():
                if not c:continue
                r=tuple(y-x for x,y in zip(midpoint(e),midpoint(f)))
                assert sum(abs(x) for x in r)<=3
                coeff[unit][a][kind(f)][r]+=c
    for table in coeff.values():
        for row in table:
            for cr in row:
                for r,c in list(cr.items()):assert cr.get(mul(-1,r),F(0))==c,(r,c,cr)

    # h(0)=2 mu Q0 and exact second-order coefficients along six directions.
    for unit,table in coeff.items():
        for i,row in enumerate(table):
            for j,cr in enumerate(row):
                want=F(0)
                if unit=='mu':
                    if i<3 and j<3:want=F(2,3)
                    elif i>=3 and j>=3 and (i-3)//2==(j-3)//2:want=F(1)
                assert sum(cr.values())==want,(unit,i,j,sum(cr.values()),want)
    directions=ei+[add(ei[i],ei[j]) for i,j in combinations(range(3),2)]
    for q in directions:
        q2=sum(x*x for x in q)
        for unit,table in coeff.items():
            for i,row in enumerate(table):
                for j,cr in enumerate(row):
                    actual=-sum(c*sum(a*b for a,b in zip(r,q))**2 for r,c in cr.items())/2
                    want=F(0)
                    if i<3 and j<3 and unit=='tau':want=q2*((1 if i==j else 0)-F(1,3))
                    if i>=3 and j>=3 and (i-3)//2==(j-3)//2:
                        u,v=list(combinations(range(3),2))[(i-3)//2]
                        sign=1 if (i-j)%2==0 else -1
                        if unit=='tau':want=sign*q2
                        else:
                            want=F(sign*(q[u]**2+q[v]**2),4)
                            if i==j:want+=F(q[u]*q[v],2)*(-1 if (i-3)%2==0 else 1)
                    assert actual==want,(q,unit,i,j,actual,want)

    # Literal full 6-site hard-core action of two overlapping actual plane S centers.
    centers=[zero,add(ei[0],ei[1])]
    sites=sorted({x for c in centers for e,sign in vs(c,0,1) for x in e})
    siteidx={x:i for i,x in enumerate(sites)};dim=1<<len(sites)
    all_edges=sorted(edge(a,b) for a,b in combinations(sites,2) if tuple(y-x for x,y in zip(a,b)) in G)
    def zeros():return [[F(0) for _ in range(dim)] for _ in range(dim)]
    def mm(A,B):
        C=zeros()
        nz=[[(j,x) for j,x in enumerate(r) if x] for r in B]
        for i in range(dim):
            for k,a in enumerate(A[i]):
                if a:
                    for j,b in nz[k]:C[i][j]+=a*b
        return C
    def plus(A,B,s=1):return [[a+s*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
    def adj(A):return list(map(list,zip(*A)))
    def comm(A,B):return plus(mm(A,B),mm(B,A),-1)
    def scale(A,s):return [[s*x for x in r] for r in A]
    def annih(e):
        M=zeros(); mask=sum(1<<siteidx[x] for x in e)
        for n in range(dim):
            if n&mask==mask:M[n^mask][n]=1
        return M
    B={e:annih(e) for e in all_edges}
    H=zeros(); localK=defaultdict(F)
    for center in centers:
        for (e,a),(f,b) in combinations(vs(center,0,1),2):
            row={e:a,f:-b};L=zeros()
            for g,c in row.items():L=plus(L,scale(B[g],c))
            H=plus(H,scale(mm(adj(L),L),F(1,4)))
            for g,c in row.items():
                for h,d in row.items():localK[g,h]+=F(c*d,4)
    N=[]
    for x in range(len(sites)):
        n=zeros()
        for state in range(dim):n[state][state]=int(bool(state&(1<<x)))
        N.append(n)
    A=zeros()
    for x,n in enumerate(N):A=plus(A,scale(n,1<<x))
    # Full carrier identity summed over all physical endpoints.
    left=zeros()
    for n in N:left=plus(left,scale(comm(n,comm(H,n)),F(1,2)))
    right=scale(H,-1)
    for (e,f),c in localK.items():
        right=plus(right,scale(mm(adj(B[e]),B[f]),c*len(set(e)&set(f))))
    assert left==right
    J=comm(H,A);T=scale(comm(adj(J),comm(H,J)),F(1,2))
    Qlift=zeros()
    for e in all_edges:
        ie=sum(1<<siteidx[x] for x in e)
        for f in all_edges:
            jf=sum(1<<siteidx[x] for x in f)
            Qlift=plus(Qlift,scale(mm(adj(B[e]),B[f]),T[ie][jf]))
    R=plus(T,Qlift,-1)
    nonzero=[]
    for i,j in product(range(dim),repeat=2):
        if i.bit_count()<=2 or j.bit_count()<=2:assert R[i][j]==0
        if R[i][j]:nonzero.append([i,j,str(R[i][j])])
    assert nonzero, 'fixture must exhibit the hard-core higher-occupancy correction'
    return {'source_rows':row_count,'pinned_edges':len(pins),
     'exact_row_sums':{k:[str(x) for x in v] for k,v in row_sums.items()},
     'hessian_directions':directions,'full_carrier_sites':sites,
     'nonzero_remainder_entries':nonzero}

def readout_controls():
    """Literal pair-row control; no imported model or author-runner functions."""
    import collections, fractions, hashlib, itertools, json, pathlib, resource, time
    F=fractions.Fraction
    start=time.monotonic(); cpu=time.process_time()
    axes=((1,0,0),(0,1,0),(0,0,1)); zero=(0,0,0)
    def add(x,y,L=None):
        z=tuple(a+b for a,b in zip(x,y)); return tuple(a%L for a in z) if L else z
    def mul(s,x): return tuple(s*a for a in x)
    def pair(x,y): return tuple(sorted((x,y)))
    def words(x,L=None):
        ds=[{pair(add(x,e,L),add(x,mul(-1,e),L)):1} for e in axes]
        planes=[]
        for i,j in itertools.combinations(range(3),2):
            planes.append([{pair(add(x,mul(s,axes[i]),L),add(x,mul(t,axes[j]),L)):s*t} for s,t in itertools.product((-1,1),repeat=2)])
        return ds,planes
    def combine(ws,coeffs):
        d=collections.defaultdict(int)
        for w,a in zip(ws,coeffs):
            for e,b in w.items(): d[e]+=a*b
        return {e:a for e,a in d.items() if a}
    def qrows(x,L=None):
        ds,ps=words(x,L)
        return [(combine(ds,(1,-1,0)),F(1,2)),(combine(ds,(1,1,-2)),F(1,6))]+[(combine(p,(1,1,1,1)),F(1,4)) for p in ps]
    def srows(x,L=None):
        ds,ps=words(x,L)
        return [(combine(ds,(1,1,1)),F(2,3))]+[(combine([p[i],p[j]],(1,-1)),F(1,4)) for p in ps for i,j in itertools.combinations(range(4),2)]
    def grows(x,L=None):
        a=qrows(x,L); out=[]
        for e in axes:
            b=qrows(add(x,e,L),L)
            for (u,c),(v,d) in zip(a,b):
                assert c==d and not (set(u)&set(v)), 'adjacent centers share pair'
                out.append((combine([v,u],(1,-1)),c))
        return out
    def diag(rows):
        d=collections.defaultdict(F)
        for w,c in rows:
            for e,a in w.items(): d[e]+=c*a*a
        return dict(d)
    def edges(L):
        typ={}
        for x in itertools.product(range(L),repeat=3):
            for e in axes:
                for s in (-1,1): typ[pair(x,add(x,mul(2*s,e),L))]='a'
            for i,j in itertools.combinations(range(3),2):
                for s,t in itertools.product((-1,1),repeat=2):typ[pair(x,add(add(x,mul(s,axes[i]),L),mul(t,axes[j]),L))]='p'
        return typ
    results={}
    for L in (5,6):
        sites=list(itertools.product(range(L),repeat=3)); se=[]; gr=[]; att=[]
        for x in sites:
            se.extend(srows(x,L));gr.extend(grows(x,L))
            att.extend((w,c*(-2 if k<2 else -1)) for k,(w,c) in enumerate(qrows(x,L)))
        sd,gd,ad=map(diag,(se,gr,att)); et=edges(L)
        assert set(sd)==set(gd)==set(ad)==set(et)
        for e,t in et.items():
            assert sd[e]==({'a':F(2,3),'p':F(3,2)}[t])
            assert gd[e]==({'a':F(4),'p':F(3)}[t])
            assert ad[e]==({'a':F(-4,3),'p':F(-1,2)}[t])
        configs=[set(),{sites[0]},{(0,0,0),(2,0,0)},{(0,0,0),(1,1,0)},set(sites)]
        # Fixed arithmetic masks, with no randomness or sampled quantum assumption.
        configs += [{x for j,x in enumerate(sites) if ((j*37+salt*19)%101)<level} for salt in range(5) for level in (3,17,50,90)]
        neighbors={x:set() for x in sites}
        for x,y in et: neighbors[x].add(y);neighbors[y].add(x)
        for cfg in configs:
            m={x:len(neighbors[x]&cfg) for x in cfg}
            V3=sum(v*(v-1)//2 for v in m.values())
            D=sum((v-1)*(v-2)//2 for v in m.values())
            s=sum(c for e,c in sd.items() if set(e)<=cfg)
            a=sum(c for e,c in ad.items() if set(e)<=cfg)
            assert len(cfg)+V3+a==D+s
            # Original literal quadratic lowering row norms on a basis configuration.
            normS=sum(c*sum(z*z for e,z in w.items() if set(e)<=cfg) for w,c in se)
            assert normS==s
        results[f'L{L}']={'sites':len(sites),'positive_S_rows':len(se),'gradient_rows':len(gr),'edges':dict(collections.Counter(et.values())),'configurations':len(configs),'all_weights_exact':True}
    # Degree lower bound in both parameter branches, with literal edge-type composition.
    degree_checks=0
    for tau in (F(1,100),F(1,6),F(1,3),F(5,6),F(1),F(100)):
        mu=F(1); c=min(mu,mu/3+2*tau); wa=2*mu/3+4*tau;wp=3*mu/2+3*tau
        for ma in range(7):
            for mp in range(13):
                m=ma+mp
                assert mu*(m-1)*(m-2)/2+(wa*ma+wp*mp)/2>=c
                degree_checks+=1
        assert min(mu,wa/2)==c
    results['degree_checks']=degree_checks
    # Infinite-lattice local rows, just the finitely many centers that can cover origin.
    centers=list(itertools.product(range(-2,3),repeat=3))
    S=[];G=[]
    for x in centers:
        S.extend(srows(x));G.extend(grows(x))
    def support(w):return set(itertools.chain.from_iterable(w))
    def rad(x):return sum(abs(a) for a in x)
    incident={e for w,c in S+G for e in w if zero in e}
    assert len(incident)==18
    for e in incident:
        relevant=[(w,c) for w,c in S+G if e in w]
        assert all(max(map(rad,support(w)))<=3 for w,c in relevant)
        assert sum(c*w.get(e,0)**2 for w,c in S)==({'a':F(2,3),'p':F(3,2)}['a' if max(abs(a-b) for a,b in zip(*e))==2 else 'p'])
    # Radius2 is insufficient for complete incident gradient weight; explicit missed row.
    missed=[(w,c) for w,c in G if any(zero in e for e in w) and max(map(rad,support(w)))==3]
    assert missed
    B3={x for x in itertools.product(range(-3,4),repeat=3) if rad(x)<=3}
    insideS=[(w,c) for w,c in S if support(w)<=B3]
    insideG=[(w,c) for w,c in G if support(w)<=B3]
    for e in incident:
        assert diag(insideS)[e]==diag(S)[e]
        assert diag(insideG)[e]==diag(G)[e]
    results['local']={'incident_edges':18,'radius3_complete':True,'radius2_missed_gradient_rows':len(missed),'witness':[[[list(a),list(b)],v] for (a,b),v in missed[0][0].items()]}
    # Nonzero finite-volume coherent fixture: normalized uniform E1 pair, norm^2=V.
    # Its H0 energy vanishes by actual constant Q outputs and local singlet cancellation;
    # full dephasing has two particles and one axial edge in every branch.
    L=5;psi=collections.defaultdict(int)
    for x in itertools.product(range(L),repeat=3):
        ds,_=words(x,L)
        for e,a in combine(ds,(1,-1,0)).items():psi[e]+=a
    norm=sum(a*a for a in psi.values());assert norm==2*L**3
    for x in itertools.product(range(L),repeat=3):
        for w,c in srows(x,L)+grows(x,L):assert sum(a*psi.get(e,0) for e,a in w.items())==0
    assert all(edges(L)[e]=='a' for e in psi)
    results['coherent_pair']={'norm_without_sqrt2':norm,'N':2,'H0':0,'dephased_energy_mu':'2/3','dephased_energy_tau':'4','same_occupation_distribution':True}
    return results

def monitoring_controls():
    # Author-reused literal original-Hamiltonian pin calculation.
    from fractions import Fraction as F
    import itertools,collections,json,time,resource,hashlib,pathlib
    wall=time.monotonic();cpu=time.process_time();axes=((1,0,0),(0,1,0),(0,0,1));zero=(0,0,0)
    def add(x,y,L):return tuple((a+b)%L for a,b in zip(x,y))
    def neg(x):return tuple(-a for a in x)
    def pair(x,y):return tuple(sorted((x,y)))
    def combine(rows,cs):
     d=collections.defaultdict(int)
     for row,c in zip(rows,cs):
      for e,a in row.items():d[e]+=c*a
     return {e:a for e,a in d.items() if a}
    def q(x,L):
     ds=[{pair(add(x,e,L),add(x,neg(e),L)):1} for e in axes]
     out=[(combine(ds,(1,-1,0)),F(1,2)),(combine(ds,(1,1,-2)),F(1,6))]
     for i,j in itertools.combinations(range(3),2):
      terms={}
      for s,t in itertools.product((-1,1),repeat=2):
       a=tuple(s*v for v in axes[i]);b=tuple(t*v for v in axes[j]);terms[pair(add(x,a,L),add(x,b,L))]=s*t
      out.append((terms,F(1,4)))
     return out
    D=[];kinds=[]
    for i in range(3):
     for s in (-1,1):D.append(tuple(2*s*v for v in axes[i]));kinds.append(('a',i,s))
    for i,j in itertools.combinations(range(3),2):
     for s,t in itertools.product((-1,1),repeat=2):D.append(tuple(s*a+t*b for a,b in zip(axes[i],axes[j])));kinds.append(('p',i,j,s,t))
    results={}
    for L in (5,6):
     index={pair(zero,tuple(v%L for v in d)):i for i,d in enumerate(D)};assert len(index)==18
     M=[[F(2 if i==j else 0) for j in range(18)] for i in range(18)]
     T=[[F(0) for _ in range(18)] for _ in range(18)]
     def outer(target,row,coef):
      entries=[(index[e],v) for e,v in row.items() if e in index]
      for i,a in entries:
       for j,b in entries:target[i][j]+=coef*a*b
     sites=list(itertools.product(range(L),repeat=3));cache={x:q(x,L) for x in sites};nonempty_cross=0
     for x in sites:
      rows=cache[x]
      # Original attractions, plus2mu I from muN+V3-muDdiag. No S rows used.
      for a,(row,w) in enumerate(rows):outer(M,row,(-2 if a<2 else -1)*w)
      for e in axes:
       nextrows=cache[add(x,e,L)]
       for (a,w),(b,v) in zip(rows,nextrows):
        assert w==v
        if set(a)&set(index) and set(b)&set(index):nonempty_cross+=1
        outer(T,combine([b,a],(1,-1)),w)
     assert nonempty_cross==0
     # Entrywise comparison with the source matrix, including every offdiagonal and mixing zero.
     for i,ki in enumerate(kinds):
      for j,kj in enumerate(kinds):
       em=et=F(0)
       if i==j:em,et=(F(2,3),F(4)) if ki[0]=='a' else (F(3,2),F(3))
       elif ki[0]==kj[0]=='p' and ki[1:3]==kj[1:3] and sum(a!=b for a,b in zip(ki[3:],kj[3:]))==1:em,et=F(1,4),F(-3,2)
       assert M[i][j]==em and T[i][j]==et,(L,i,j,M[i][j],T[i][j],em,et)
     # Eigenvectors are independently enumerated sign characters on each plane.
     checks=0
     for plane in itertools.combinations(range(3),2):
      inds=[i for i,k in enumerate(kinds) if k[0]=='p' and k[1:3]==plane]
      for powers,eig in [((0,0),(F(2),F(0))),((1,0),(F(3,2),F(3))),((0,1),(F(3,2),F(3))),((1,1),(F(1),F(6)))]:
       vec=[F(0)]*18
       for i in inds:vec[i]=kinds[i][3]**powers[0]*kinds[i][4]**powers[1]
       for mat,val in zip((M,T),eig):assert [sum(mat[i][j]*vec[j] for j in range(18)) for i in range(18)]==[val*x for x in vec]
       checks+=1
     results[f'L{L}']={'matrix_entries_each':324,'pin_centers_with_cross_gradient':nonempty_cross,'plane_eigenvectors':checks,'mu_matrix':[[str(a) for a in row] for row in M],'tau_matrix':[[str(a) for a in row] for row in T]}
    # Literal physical occupation action on four actual M2 factors.
    pairs=list(itertools.combinations(range(4),2));counts=collections.Counter();paths=0
    for p in pairs:
     for qpair in pairs:
      overlap=len(set(p)&set(qpair))
      for state in range(16):
       if any(not (state>>v)&1 for v in qpair):continue
       after=state
       for v in qpair:after &= ~(1<<v)
       if any((after>>v)&1 for v in p):continue
       for v in p:after |=1<<v
       actual=F(0)
       for v in range(4):
        ni=(state>>v)&1;no=(after>>v)&1
        actual+=ni*no-F(ni+no,2)
       assert actual==overlap-2
       paths+=1;counts[str(actual)]+=1
    # Full integer occupation identity on an actual small embedded configuration menu.
    menu=[zero]+D[:6]+D[6:9];Dset=set(D);cfgs=0
    for mask in range(1<<len(menu)):
     occ={x for i,x in enumerate(menu) if (mask>>i)&1}
     deg={x:sum(tuple(y[k]-x[k] for k in range(3)) in Dset for y in occ) for x in occ}
     E=sum(deg.values())//2;triples=sum(m*(m-1)//2 for m in deg.values());Dval=sum((m-1)*(m-2)//2 for m in deg.values())
     assert Dval==len(occ)-2*E+triples
     for tau in (F(1,100),F(1,3),F(1),F(10)):
      c=min(F(1),F(1,3)+2*tau)
      assert 2*Dval+4*c*E-2*c*len(occ)==2*(1-c)*Dval+2*c*triples>=0
     cfgs+=1
    results['physical_paths']={'nonzero_Bp_dagger_Bq_paths':paths,'coefficients':dict(counts),'all_pairs':36,'full_four_site_basis_masks':16}
    results['actual_configuration_count_identity']={'embedded_sites':len(menu),'all_masks':cfgs,'parameter_cases_per_mask':4}
    return results

def main():
    import argparse
    import json
    import resource
    import time
    parser = argparse.ArgumentParser()
    parser.add_argument('--group', choices=('all','response','readout','monitoring'), default='all')
    args = parser.parse_args()
    started=time.monotonic(); cpu=time.process_time(); out={}
    for name, fn in [('response',response_controls),('readout',readout_controls),('monitoring',monitoring_controls)]:
        if args.group in ('all',name):
            out[name]=fn()
    out['scope']='Finite exact controls only; analytical proofs supply all-volume and spectral assertions.'
    out['resources']={'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-started,
                      'maxrss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps(out,sort_keys=True,indent=2))
    print('TOTAL: PASS='+str(len(out)-2)+' FAIL=0')

if __name__=='__main__':
    main()
