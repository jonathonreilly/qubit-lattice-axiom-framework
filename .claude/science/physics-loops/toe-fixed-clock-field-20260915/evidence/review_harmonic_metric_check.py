from pathlib import Path
import numpy as np,json
def check(L):
    xyz=list(np.ndindex(L,L,L));V=L**3;E=3*V
    def ix(x):return int(np.ravel_multi_index(tuple(np.asarray(x)%L),(L,L,L)))
    D=np.zeros((V,E),dtype=np.int64);U=np.tile(np.eye(3,dtype=np.int64),(V,1))
    for x in xyz:
        v=ix(x)
        for i in range(3):
            y=np.array(x);y[i]+=1
            D[v,3*v+i]+=1;D[ix(y),3*v+i]-=1
    tree=[];R=np.zeros((E,V),dtype=np.int64)
    for x in sorted(xyz,key=sum):
        v=ix(x)
        if v==0:continue
        i=next(i for i in range(3) if x[i]>0)
        parent=np.array(x);parent[i]-=1;p=ix(parent);edge=3*p+i
        R[:,v]=R[:,p];R[edge,v]-=1;tree.append(edge)
    target=np.eye(V,dtype=np.int64);target[0,:]-=1
    assert np.array_equal(D@R,target)
    chords=[e for e in range(E) if e not in set(tree)]
    C=np.eye(E,dtype=np.int64)[:,chords]-R@D[:,chords]
    assert not np.any(D@C)
    assert np.array_equal(C[chords,:],np.eye(len(chords),dtype=np.int64))
    F=np.zeros((E,3*V),dtype=np.int64)
    for x in xyz:
        v=ix(x)
        for f,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
            xi=np.array(x);xi[i]+=1;xj=np.array(x);xj[j]+=1
            F[3*v+i,3*v+f]+=1;F[3*ix(xi)+j,3*v+f]+=1
            F[3*ix(xj)+i,3*v+f]-=1;F[3*v+j,3*v+f]-=1
    Z=F[chords,:];assert np.array_equal(C@Z,F)
    raw=C.T@U;assert not np.any(raw%L);H=raw//L
    assert not np.any(Z.T@H)
    X0=U[chords,:];assert np.array_equal(C@X0,U)
    assert np.array_equal(H.T@X0,L*L*np.eye(3,dtype=np.int64))
    # Exact integer weighted identity, multiplied by L*prod(weights).
    weights=np.array([2,3,5],dtype=np.int64);scale=int(np.prod(weights))
    KK=C.T@((U@weights)[:,None]*C)
    XX=X0*(scale//weights)[None,:]
    assert np.array_equal(KK@XX,L*scale*H)
    assert np.array_equal(H.T@XX,L*L*np.diag(scale//weights))
    return {'L':L,'vertices':V,'links':E,'cycle_dimension':len(chords),
      'harmonic_dimension':3,'integer_identities':'exact','electric_weights':weights.tolist(),
      'tangent_metric':[f'{w}/{L}' for w in weights]}
d={'status':'exact_integer_normalization_checks','rows':[check(L) for L in [3,4,5]],
   'scope':'author cross-check; no independent audit'}
s=json.dumps(d,indent=2);Path(__file__).with_suffix('.json').write_text(s+'\n');print(s)
