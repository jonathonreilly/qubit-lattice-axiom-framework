"""New checks required for the proposed normalizable second-clock theorem.

Uses the author's independently built physical matrix generator, not an
independent review. Quadrature convergence is reported, not substituted for
the analytic dominated-convergence argument.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import importlib.util
import json
import numpy as np
from scipy.linalg import expm

D=Path(__file__).resolve().parent
p=D/'second_event_probe.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='4827171a51e018b306302b0fac315c000c63bb7311e69fcab18ad666916f1f25'
spec=importlib.util.spec_from_file_location('probe',p)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def first_sector():
    edges, aset=m.graph('ring8')
    words=m.charges(4)
    ix={q:i for i,q in enumerate(words)}
    W=np.array([sum(not q[a] for a in aset) for q in words])
    blocks=[np.flatnonzero(W==w) for w in range(5)]
    results=[]
    for angle in [0.,.37,1.19]:
        theta=np.zeros(8);theta[-1]=angle
        T=np.zeros((len(words),len(words)),complex)
        for col,q in enumerate(words):
            for out,shift in m.legal_hops(q,edges):
                T[ix[out],col]-=np.exp(1j*np.dot(theta,shift))
        A=T[np.ix_(blocks[1],blocks[0])]
        Z=T[np.ix_(blocks[2],blocks[1])]@A
        M=A.conj().T@A
        H2=-M
        H4=M@M-Z.conj().T@Z/2
        q=words[blocks[0][0]]
        norms=[]
        for edge in range(8):
            for sign in [-1,1]:
                poly=m.squared_norm_polynomial(m.effective_paths(q,edges,aset,edge,[sign]))
                assert poly=={(0,)*8:1}
                norms.append(1)
        assert abs(H2[0,0]+8)<1e-12 and abs(H4[0,0]-24)<1e-12
        results.append({'theta':angle,'H2':float(H2[0,0].real),'H4':float(H4[0,0].real),
                        'resolved_first_total_loss_over_kappa':sum(norms)})
    return results


def quadratures():
    kappa,delta=.7,1.3
    rows=[]
    for grid in [64,128,256]:
        # Midpoints avoid the four exceptional circulation phases.
        acc=np.zeros((2,3,2,3))
        for q in range(grid):
            theta=2*np.pi*(q+.5)/grid
            angles=np.zeros(8);angles[-1]=theta
            words,H,H4,jumps,G=m.target_matrices('ring8',angles)
            states=np.column_stack([m.first_output('ring8',angles,words,coh)[0]
                                    for coh in [False,True]])
            densities=np.array([1.,1+np.cos(theta),1-np.cos(theta)])
            for ei,eta in enumerate([20,80,320]):
                K=eta*H+delta*H4-.5j*kappa*G
                for ti,t in enumerate([.2,.7]):
                    evolved=expm(-1j*t*K)@states
                    survival=np.sum(abs(evolved)**2,axis=0)
                    acc[:,ei,ti,:]+=survival[:,None]*densities[None,:]/grid
        for coh in [False,True]:
            for ei,eta in enumerate([20,80,320]):
                for ti,t in enumerate([.2,.7]):
                    expected=.5*(np.exp(-2*kappa*t)+np.exp(-4*kappa*t))
                    for fi,label in enumerate(['integer_flux_0','plus_adjacent_flux','minus_adjacent_flux']):
                        value=float(acc[int(coh),ei,ti,fi])
                        rows.append({'grid':grid,'coherent_first':coh,'eta':eta,'t':t,
                                     'normalizable_field':label,'survival':value,
                                     'limiting_survival':float(expected),'error':abs(value-expected)})
    return rows


probe=json.loads((D/'SECOND_EVENT_PROBE_RESULTS.json').read_text())
generic=[];exceptional=[]
for r in probe['ring_controls']:
    if r['flat_dimension']==12:
        assert r['secular_Gamma_proposed_error']<1e-10
        for out in r['outputs']:
            assert abs(out['flat_weight']-.5)<1e-12
            assert max(abs(x['averaged_survival']-x['proposed_survival']) for x in out['rows'])<1e-12
        generic.append(r['theta'])
    else:
        assert r['flat_dimension']==14 and r['secular_Gamma_proposed_error']>3.9
        exceptional.append(r['theta'])
for r in probe['cube_exact_composition']['rows']:
    assert r['predicted_polynomial_equal']
for r in probe['cube_controls']:
    for out in r['outputs']:
        assert abs(out['hazard']-out['proposed_hazard'])<1e-12

out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'first_sector':first_sector(),'generic_ring_angles':generic,
     'exceptional_ring_angles_preserved':exceptional,'quadrature_rows':quadratures(),
     'status':'author controls, not an independent reconstruction'}
target=D/'SECOND_EVENT_VALIDATION_RESULTS.json'
assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
