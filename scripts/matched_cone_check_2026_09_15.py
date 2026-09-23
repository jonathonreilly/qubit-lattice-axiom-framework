#!/usr/bin/env python3
"""Finite algebra checks; no interacting or thermodynamic phase computation."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SUPPLIED_MATCHED_FREE_CONE_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/FREE_WEYL_HOLONOMY_MINIMIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/ITERATED_LOCAL_MAXWELL_MATTER_STATE_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'supplied_matched_free_cone_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SUPPLIED_MATCHED_FREE_CONE_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/matched_cone_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
import hashlib
import itertools
import json
import numpy as np
import sympy as sp


def symbolic_check():
    sx, sy, sz, dx, dy, dz, c, lam = sp.symbols('sx sy sz dx dy dz c lam')
    X = sp.Matrix([[0, -sz, sy], [sz, 0, -sx], [-sy, sx, 0]])
    D = sp.diag(dx, dy, dz)
    # Similar to the symmetric normal matrix, avoiding formal square roots.
    A = c * D * X.T * D * X
    target = c * (dy*dz*sx**2 + dx*dz*sy**2 + dx*dy*sz**2)
    residual = sp.expand((lam*sp.eye(3)-A).det()-lam*(lam-target)**2)
    assert residual == 0
    return {'characteristic_polynomial_residual': str(residual)}


def literal_curl(L):
    sites = list(itertools.product(range(L), repeat=3))
    lookup = {x:i for i,x in enumerate(sites)}
    def shift(x,j):
        y=list(x); y[j]=(y[j]+1)%L
        return tuple(y)
    C=np.zeros((3*L**3,3*L**3))
    # Plaquette row direction labels its normal, independently of Block22.
    for x in sites:
        for normal,(i,j) in enumerate(((1,2),(2,0),(0,1))):
            r=3*lookup[x]+normal
            C[r,3*lookup[shift(x,i)]+j]+=1
            C[r,3*lookup[x]+j]-=1
            C[r,3*lookup[shift(x,j)]+i]-=1
            C[r,3*lookup[x]+i]+=1
    return C


def spectral_check(L,G,eta):
    E=eta*np.sqrt(np.prod(G))/G
    B=np.sqrt(np.prod(G))/eta/G
    C=literal_curl(L)
    RE=np.sqrt(np.tile(E,L**3))
    RB=np.tile(B,L**3)
    A=(RE[:,None]*C.T) @ (RB[:,None]*C*RE[None,:])
    measured=np.linalg.eigvalsh(A)
    positive=measured[measured>1e-9]
    predicted=[]
    for n in itertools.product(range(L),repeat=3):
        if n==(0,0,0): continue
        val=float(np.dot(4*np.sin(np.pi*np.array(n)/L)**2,G))
        predicted.extend([val,val])
    assert len(positive)==2*(L**3-1)
    error=float(np.max(np.abs(positive-np.sort(predicted))))
    zero_error=float(np.max(np.abs(measured[:L**3+2])))
    assert error<2e-11 and zero_error<2e-11
    return {'L':L,'G':G.tolist(),'eta':eta,'positive_count':len(positive),
            'spectral_error':error,'kernel_error':zero_error}


def h0_vector(k):
    return np.array([np.sin(k[0]),np.sin(k[1]),
                     2.5-np.cos(k[0])-np.cos(k[1])-np.cos(k[2])])


def bloch_vector(k,charge):
    b=np.array([np.pi/3,0,0])
    if charge==1: return h0_vector(k-b)
    # h_-(k)=h_+(-k)^*, complex conjugation reverses sigma2.
    return h0_vector(-k-b)*np.array([1,-1,1])


def matter_check():
    rows=[]
    eps=2e-5
    target=np.diag([1,1,.75])
    for charge in [1,-1]:
        for sign in [-1,1]:
            node=np.array([charge*np.pi/3,0,sign*np.pi/3])
            J=np.column_stack([(bloch_vector(node+eps*np.eye(3)[j],charge)
                               -bloch_vector(node-eps*np.eye(3)[j],charge))/(2*eps)
                               for j in range(3)])
            error=float(np.max(np.abs(J.T@J-target)))
            node_error=float(np.linalg.norm(bloch_vector(node,charge)))
            assert error<2e-8 and node_error<2e-14
            rows.append({'charge':charge,'node':node.tolist(),
                         'metric_error':error,'node_residual':node_error})
    return rows


def negative_example():
    E=np.diag([1.,2.,3.]); B=np.eye(3)
    X=np.array([[0.,-1,0],[1,0,0],[0,0,0]])
    root=np.diag(np.sqrt(np.diag(E)))
    measured=np.linalg.eigvalsh(root@X.T@B@X@root)
    assert np.allclose(measured,[0,1,2],atol=1e-14,rtol=0)
    return {'positive_but_birefringent_axis_squared_frequencies':measured.tolist()}


def main():
    result={'status':'PASS','scope':'finite algebra only, personal checks',
            'symbolic':symbolic_check(),
            'literal_curl_spectra':[spectral_check(L,np.array(G),eta)
                 for L,G,eta in [(3,[1.,1.,.75],1.),(4,[1.,1.,.75],1.),
                                (4,[1.,1.,.75],.37),(3,[.4,1.3,2.1],2.)]],
            'wilson_nodes':matter_check(),'necessity_counterexample':negative_example()}
    result['runner_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output=json.dumps(result,indent=2)
    _OUTPUT_JSON.write_text(output+'\n')
    print(output)


if __name__=='__main__': main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: positive-weight cone identities')
    print('per_site: finite periodic curl fixtures')
    print('per_mode: finite Bloch derivatives and weighted polarization checks')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
