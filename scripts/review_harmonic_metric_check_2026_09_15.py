
# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/FLAT_HOLONOMY_MINIMIZATION_AND_PERIODIC_SPECTRAL_FLOOR_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/FREE_WEYL_HOLONOMY_MINIMIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'fixed_box_slow_spectrum_and_harmonic_metric_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/review_harmonic_metric_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
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
s=json.dumps(d,indent=2);_OUTPUT_JSON.write_text(s+'\n');print(s)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: Exact integer incidence, cycle-basis, plaquette and weighted harmonic-metric identities.')
    print('per_site: Periodic cubic coordinate fixtures L=3,4,5.')
    print('per_mode: Three harmonic directions and complete finite cycle-coordinate identities; no spectral solver or slow-spectrum/cutoff-refinement run.')
    print('per_block: Three exact integer normalization fixtures with electric weights2,3,5.')
    print('lattice_wide: Not executed: the all-L metric theorem relies on the written proof.')
