"""Exact colored-record controls for the supplied bosonic gauge model.

The complete square hopping matrices are constructed directly. No previous
author/checker module or stored numerical target is imported.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from itertools import product, permutations
import json
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent


def identity(path):
    p=Path(path).resolve();b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':sha256(b).hexdigest()}


def square():
    # Binary link fields are oriented cyclically around C4.
    states=[]
    for word in range(16):
        q=tuple(((word>>x)&1)-((word>>((x-1)%4))&1)+int(x%2==0) for x in range(4))
        if all(z in (0,1) for z in q):
            states.append((word,q))
    assert len(states)==7
    fields={word:i for i,(word,q) in enumerate(states)}
    colors=list(product(range(2),repeat=2))
    nc=len(colors);n=len(states)
    basis=[(word,q,c) for word,q in states for c in colors]
    lookup={(word,c):i for i,(word,q,c) in enumerate(basis)}
    t0=sp.zeros(n);t=sp.zeros(n*nc)
    for col,(word,q,c) in enumerate(basis):
        occupied=[x for x,z in enumerate(q) if z]
        colored=dict(zip(occupied,c))
        for e in range(4):
            x,y=e,(e+1)%4
            target_word=word^(1<<e)
            if target_word not in fields:continue
            target_q=states[fields[target_word]][1]
            source=next((z for z in (x,y) if q[z]==1 and target_q[z]==0),None)
            dest=next((z for z in (x,y) if q[z]==0 and target_q[z]==1),None)
            if source is None or dest is None:continue
            after=dict(colored);after[dest]=after.pop(source)
            target_colors=tuple(after[z] for z in sorted(after))
            row=lookup[(target_word,target_colors)]
            t[row,col]=-1
            t0[fields[target_word],fields[word]]=-1
    assert t==t.T and t0==t0.T
    penalty0=sp.diag(*[q[1]+q[3] for word,q in states])
    penalty=sp.kronecker_product(penalty0,sp.eye(nc))
    low0=[i for i in range(n) if penalty0[i,i]==0]
    low=[i for i in range(n*nc) if penalty[i,i]==0]
    assert len(low0)==2 and len(low)==8
    inv=sp.diag(*[1/penalty[i,i] if penalty[i,i] else 0 for i in range(n*nc)])
    h2=(-t*inv*t).extract(low,low)
    k2=(t*inv**2*t).extract(low,low)
    f4=(-t*inv*t*inv*t*inv*t).extract(low,low)
    h4=sp.simplify(f4-(k2*h2+h2*k2)/2)
    swap=sp.zeros(nc)
    for col,c in enumerate(colors):swap[colors.index(c[::-1]),col]=1
    x=sp.Matrix([[0,1],[1,0]])
    assert h2==-2*sp.eye(8)
    assert h4==2*sp.eye(8)-2*sp.kronecker_product(x,swap)
    symmetric=sp.eye(nc)+swap
    assert (swap-sp.eye(nc))*symmetric==sp.zeros(nc)
    embedding=sp.kronecker_product(sp.eye(n),symmetric)
    assert t*embedding==embedding*sp.kronecker_product(t0,sp.eye(nc))
    assert penalty*embedding==embedding*sp.kronecker_product(penalty0,sp.eye(nc))
    # Full (not merely effective) finite Hamiltonian spectra and exact embedding.
    numerical=[]
    for epsilon in (.04,.15,.4):
        scalar=np.array(penalty0+sp.Rational(str(epsilon))*t0,float)
        colored=np.array(penalty+sp.Rational(str(epsilon))*t,float)
        e0=float(np.linalg.eigvalsh(scalar)[0])
        ec=float(np.linalg.eigvalsh(colored)[0])
        assert abs(e0-ec)<1e-12
        numerical.append({'epsilon':epsilon,'scalar_ground_energy':e0,'colored_ground_energy':ec,
                          'difference':abs(e0-ec)})
    return {'base_dimension':n,'colored_dimension':n*nc,'low_dimension':len(low),
            'colors':colors,'h2':[[str(z) for z in row] for row in h2.tolist()],
            'h4':[[str(z) for z in row] for row in h4.tolist()],
            'full_hopping_intertwines_symmetric_color_embedding_exactly':True,
            'full_penalty_intertwines_symmetric_color_embedding_exactly':True,
            'ground_energy_controls':numerical}


def partial_trace_color(rho,nfield,ncolor):
    a=rho.reshape(nfield,ncolor,nfield,ncolor)
    return np.einsum('aibi->ab',a)


def reduced_dynamics():
    colors=list(product(range(2),repeat=2))
    swap=np.zeros((4,4),complex)
    for i,c in enumerate(colors):swap[colors.index(c[::-1]),i]=1
    x=np.array([[0,1],[1,0]],complex)
    h=-np.kron(x,swap)
    e=np.eye(4)
    dicke=(e[:,1]+e[:,2])/math.sqrt(2)
    anti=(e[:,1]-e[:,2])/math.sqrt(2)
    tau=np.diag([.7,.3])
    cases={'distinct_definite_colors':np.outer(e[:,1],e[:,1]),
           'symmetric_fixed_counts':np.outer(dicke,dicke),
           'antisymmetric_fixed_counts':np.outer(anti,anti),
           'invariant_mixture_fixed_counts':np.diag([0,.5,.5,0]),
           'iid_mixed_colors':np.kron(tau,tau),
           'identical_definite_colors':np.outer(e[:,0],e[:,0])}
    output=[]
    for name,rho in cases.items():
        eta=float(np.trace(swap@rho).real)
        comm=float(np.linalg.norm(swap@rho-rho@swap))
        support=float(np.linalg.norm((np.eye(4)-swap)@rho))
        rows=[]
        for time in (.2,math.pi/4,1.1):
            unit=expm(-1j*time*h)
            initial=np.kron(np.diag([1.,0.]),rho)
            field=partial_trace_color(unit@initial@unit.conj().T,2,4)
            co,si=math.cos(time),math.sin(time)
            predicted=np.array([[co*co,-1j*co*si*eta],[1j*co*si*eta,si*si]])
            error=float(np.linalg.norm(field-predicted))
            purity=float(np.trace(field@field).real)
            predicted_purity=1-.5*math.sin(2*time)**2*(1-eta**2)
            assert error<1e-12 and abs(purity-predicted_purity)<1e-12
            rows.append({'time':time,'field_purity':purity,'formula_matrix_error':error,
                         'imaginary_01_coherence':float(field[0,1].imag)})
        output.append({'color_state':name,'swap_expectation':eta,'commutator_norm':comm,
                       'symmetric_support_defect':support,'dynamics':rows})
    assert abs(float(np.trace(swap@np.kron(tau,tau)).real)-float(np.trace(tau@tau)))<1e-14
    return output


def graph_lift():
    # A finite graph with noncommuting permutation labels. Equality of ground
    # energies follows from the analytic vector-norm comparison, not this sample.
    words=list(permutations(range(3)))
    nc=len(words);vertices=5
    scalar=np.diag([0.,.3,-.2,.7,.1])
    full=np.kron(scalar,np.eye(nc))
    edges=[(0,1,.7,(0,1)),(1,2,1.1,(1,2)),(2,3,.4,(0,2)),
           (3,0,.8,(0,1)),(1,4,.6,(0,2)),(4,3,.9,(1,2))]
    swaps=[]
    for a,b,w,(i,j) in edges:
        perm=np.zeros((nc,nc))
        for col,word in enumerate(words):
            v=list(word);v[i],v[j]=v[j],v[i]
            perm[words.index(tuple(v)),col]=1
        scalar[a,b]-=w;scalar[b,a]-=w
        full[a*nc:(a+1)*nc,b*nc:(b+1)*nc]-=w*perm
        full[b*nc:(b+1)*nc,a*nc:(a+1)*nc]-=w*perm.T
        swaps.append(perm)
    embedding=np.kron(np.eye(vertices),np.ones((nc,1))/math.sqrt(nc))
    error=float(np.linalg.norm(full@embedding-embedding@scalar))
    e0=float(np.linalg.eigvalsh(scalar)[0]);ec=float(np.linalg.eigvalsh(full)[0])
    assert error<1e-12 and abs(e0-ec)<1e-12
    return {'vertices':vertices,'fiber_dimension':nc,'full_dimension':vertices*nc,
            'noncommuting_labels':bool(np.linalg.norm(swaps[0]@swaps[1]-swaps[1]@swaps[0])>1),
            'intertwiner_error':error,'scalar_ground_energy':e0,'lifted_ground_energy':ec,
            'scope':'Ground energy equality and a symmetric invariant sector, not uniqueness or autonomous preparation.'}


def main():
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'script':identity(__file__),
         'full_colored_square':square(),'reduced_field_controls':reduced_dynamics(),
         'permutation_labeled_graph':graph_lift(),
         'status':'Author controls for a supplied color-blind bosonic extension; no native selection or autonomous symmetrization claim.'}
    data=json.dumps(out,indent=2)+'\n';(HERE/'RECORD_CONTENT_PERMUTATION_RESULTS.json').write_text(data);print(data,end='')


if __name__=='__main__':
    main()
