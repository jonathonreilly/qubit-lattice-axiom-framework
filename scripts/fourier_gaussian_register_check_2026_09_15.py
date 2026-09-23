"""Finite author challenges of the Fourier/feature-register derivation.

Fourier sums are numerical samples, not infinite-volume error certificates.
The Gaussian registers are constructed as actual finite tensor matrices.
Determinant polynomial jets share the earlier independently compared helper.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/CUBIC_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'scripts/cofactor_cyclic_check_2026_09_15.py', 'scripts/contact_register_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'cubic_fourier_energy_and_gaussian_registers_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/CUBIC_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/fourier_gaussian_register_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
import math
from pathlib import Path

import numpy as np
from contact_register_check_2026_09_15 import direct_jet, jet_product
from cofactor_cyclic_check_2026_09_15 import compositions


H = .25+math.pi**2/64


def exterior_symbol(z, degree):
    source = list(itertools.combinations(range(4), degree))
    target = list(itertools.combinations(range(4), degree+1))
    result = np.zeros((len(target), len(source)), dtype=complex)
    for col, subset in enumerate(source):
        for axis in range(4):
            if axis not in subset:
                ordered = tuple(sorted((axis,)+subset))
                result[target.index(ordered), col] = z[axis]*(-1)**sum(s < axis for s in subset)
    return result


def symbol_checks(rng):
    maximum = 0.
    for _ in range(80):
        p = rng.uniform(-math.pi, math.pi, 4)
        z = np.exp(1j*p)-1
        lam = np.vdot(z,z).real
        assert lam >= 4*np.dot(p,p)/math.pi**2-1e-13
        assert lam <= 16+1e-13
        for degree in [1,2,3]:
            before, after = exterior_symbol(z,degree-1), exterior_symbol(z,degree)
            lap = before@before.conj().T+after.conj().T@after
            maximum = max(maximum,float(np.linalg.norm(lap-lam*np.eye(len(lap)),2)))
    assert maximum < 2e-14
    return dict(momentum_degree_cases=240,maximum_hodge_symbol_error=maximum)


def fourier_samples():
    # One conserved unit plaquette boundary and its translated integer sum.
    loop = [(0,(0,0,0,0),1),(1,(1,0,0,0),1),
            (0,(0,1,0,0),-1),(1,(0,0,0,0),-1)]
    translated = loop+[(c,tuple(y+(3 if a==2 else 0) for a,y in enumerate(pos)),2*v)
                       for c,pos,v in loop]
    fixtures = {'one_edge':[(0,(0,0,0,0),1)],'plaquette_current':loop,
                'separated_integer_currents':translated}
    results=[]
    for name,entries in fixtures.items():
        samples=[]
        for size in [12,20,28]:
            current=np.zeros((4,)+(size,)*4)
            for component,position,value in entries:
                current[(component,)+position]+=value
            m=np.abs(current).sum(); r=np.linalg.norm(current.ravel())
            freq=2*np.pi*np.fft.fftfreq(size)
            lam=sum(4*np.sin(freq.reshape(tuple(size if i==axis else 1 for i in range(4)))/2)**2
                    for axis in range(4))
            inverse=np.zeros_like(lam);np.divide(1.,lam,out=inverse,where=lam>0)
            energy=0.
            for component in current:
                transform=np.fft.fftn(component)
                energy+=np.sum(abs(transform)**2*inverse)/size**4
            bound=H*m*r
            if name=="plaquette_current":
                assert abs(energy-(1-size**(-4))/2)<1e-13
            assert energy <= bound
            samples.append(dict(grid=size,energy=float(energy),analytic_infinite_bound=float(bound),
                                sampled_ratio=float(energy/bound)))
        results.append(dict(fixture=name,samples=samples))
    return results


def tensor_registers(vectors, edges, order):
    dimension=vectors.shape[1]+1
    vacuum=np.zeros(dimension**len(edges));vacuum[0]=1
    product=np.eye(len(vacuum))
    pos={v:i for i,v in enumerate(order)}
    norm_errors=[]
    for vertex in order:
        local=np.ones((1,1))
        expected=1.
        for edge in edges:
            factor=np.eye(dimension)
            if vertex in edge:
                factor=np.zeros((dimension,dimension))
                other=edge[1] if vertex==edge[0] else edge[0]
                if pos[vertex]<pos[other]:factor[0,1:]=vectors[vertex]
                else:factor[1:,0]=vectors[vertex]
                expected*=np.linalg.norm(vectors[vertex])
            local=np.kron(local,factor)
        norm_errors.append(abs(np.linalg.norm(local,2)-expected))
        product=product@local
    return float(vacuum@product@vacuum),max(norm_errors)


def register_checks(rng):
    cases=0;max_error=norm_error=0.
    graphs=[[(0,1)],[(0,1),(1,2)],[(0,1),(0,2),(0,3)],[(0,2),(1,3)]]
    for _ in range(6):
        vectors=rng.normal(size=(4,2))
        for graph in graphs:
            reference=math.prod(float(vectors[i]@vectors[j]) for i,j in graph)
            for order in itertools.permutations(range(4)):
                value,ne=tensor_registers(vectors,graph,order)
                max_error=max(max_error,abs(value-reference));norm_error=max(norm_error,ne)
                cases+=1
    assert max_error<2e-13 and norm_error<2e-13
    return dict(cases=cases,maximum_inner_product_error=max_error,maximum_local_norm_error=norm_error)


def gaussian_jet(s, features, edges):
    gram=features@features.T
    result=np.ones(2**len(edges))*math.exp(-np.sum(s*gram)/2)
    for mask in range(len(result)):
        for e,(i,j) in enumerate(edges):
            if mask & (1<<e):result[mask]*=-gram[i,j]
    return result


def determinant_jet(s, footprints, edges):
    # Coefficients of distinct-variable nilpotent increments, not finite differences.
    result=np.empty(2**len(edges))
    for mask in range(len(result)):
        result[mask]=direct_jet(s,footprints,[edge for e,edge in enumerate(edges) if mask & (1<<e)])
    return result


def source_checks(rng):
    count=4;length=4
    vec=rng.normal(size=(length,length));vec/=np.linalg.norm(vec,axis=0)
    s=vec.T@vec
    features=rng.normal(size=(count,2))*.4
    family=[set(),{0},{1},{0,1}]
    mass=np.array([1.,1.,1.,2.]);r=mass.copy();x=1.
    initial_feature_norms=np.linalg.norm(features,axis=1)
    # Supply synthetic features inside the declared energy hypothesis.
    features*=np.minimum(1.,.9*np.sqrt(H*x*mass*r)/initial_feature_norms)[:,None]
    assert np.all(np.sum(features**2,axis=1)<=H*x*mass*r)
    original=rng.normal(size=(count,count));j=(original+original.T)/7
    rho=np.linalg.norm(j,2)
    source=np.array([0.,-.5+.2j,.9,1.1-.3j])
    s4=float(np.trace(np.diag(abs(source)**4)@j@j))
    phases=np.exp(1j*rng.normal(size=(length,count)))
    configurations=np.array(list(itertools.product(range(count),repeat=length)))
    reserve=np.array([2.**len(a) for a in family])*np.exp(mass+x*r*r/512)
    graphs=[[(0,1)],[(0,1),(1,2)],[(0,1),(0,2),(0,3)],[(0,2),(1,3)]]
    c=max(math.sqrt(1.5),math.sqrt(H/2)*(128*x)**.25)
    results=[];mixed_identity=wrong_gap=0.
    for graph in graphs:
        degree=[sum(i in edge for edge in graph) for i in range(length)]
        constant=(2*c*c)**len(graph)*math.prod(math.factorial(d)**.75 for d in degree)
        sharp_constant=0.
        for mask in range(2**len(graph)):
            eg=[e for k,e in enumerate(graph) if mask & (1<<k)]
            eh=[e for k,e in enumerate(graph) if not mask & (1<<k)]
            local_constants=[]
            for i in range(length):
                hi=sum(i in e for e in eh);gi=sum(i in e for e in eg)
                local_constants.append(max(len(family[a])**(hi/2)*np.linalg.norm(features[a])**gi
                                           *math.exp(-mass[a]-x*r[a]**2/512) for a in range(count)))
            sharp_constant+=math.prod(local_constants)
        values=[]
        for conf in configurations:
            footprints=[family[a] for a in conf];psi=features[conf]
            dj=determinant_jet(s,footprints,graph);gj=gaussian_jet(s,psi,graph)
            derivative=jet_product(dj,gj)[-1]
            # Every Leibniz partition gets explicit feature-register contractions.
            direct=0.
            for mask in range(2**len(graph)):
                eg=[e for k,e in enumerate(graph) if mask & (1<<k)]
                eh=[e for k,e in enumerate(graph) if not mask & (1<<k)]
                inner=math.prod(float(psi[i]@psi[k]) for i,k in eg)
                direct+=direct_jet(s,footprints,eh)*(-1)**len(eg)*inner*gj[0]
            mixed_identity=max(mixed_identity,abs(direct-derivative))
            wrong_gap=max(wrong_gap,abs(derivative-dj[-1]*gj[-1]))
            coefficient=derivative/np.prod(reserve[conf])
            coefficient*=np.prod([j[conf[i],conf[(i+1)%length]]*phases[i,conf[i]] for i in range(length)])
            values.append(coefficient)
        values=np.array(values)
        actual=[]
        for powers in compositions(4,length):
            mark=np.prod(source[configurations]**np.array(powers)[None,:],axis=1)
            actual.append(abs(values@mark))
        bound=constant*rho**(length-2)*s4
        sharp_bound=sharp_constant*rho**(length-2)*s4
        assert max(actual)<=sharp_bound and sharp_bound<=bound
        results.append(dict(edges=graph,source_distributions=len(actual),maximum=float(max(actual)),
                            bound=float(bound),ratio=float(max(actual)/bound),
                            direct_vertex_norm_bound=float(sharp_bound),
                            direct_vertex_norm_ratio=float(max(actual)/sharp_bound)))
    assert mixed_identity<1e-12 and wrong_gap>.01
    return dict(source_checks=results,leibniz_identity_error=mixed_identity,
                rejected_product_of_derivatives_gap=wrong_gap)


def degree_reserve_checks():
    ratios=[]
    for d in range(41):
        for g in range(d+1):
            # Exact extrema in the two independent continuous reserve variables.
            first=0. if d==0 else d/2*(math.log(d/2)-1)
            second=0. if g==0 else g/4*(math.log(128*g)-1)
            bound=.5*math.lgamma(d+1)-d/2*math.log(2)+.25*math.lgamma(g+1)+g/4*math.log(128)
            ratio=math.exp(first+second-bound)
            assert ratio<=1+1e-13
            ratios.append(ratio)
    return dict(degree_pairs=len(ratios),maximum_ratio=max(ratios),H=H,
                old_H=math.pi**2/4+1/64,
                source_mass_reserve_at_32768=32768/512-(3*math.log(2)+1))


def main():
    rng=np.random.default_rng(928531)
    result=dict(status='finite_author_checks_passed',independent_review=False,
                symbol=symbol_checks(rng),fourier_samples=fourier_samples(),
                feature_registers=register_checks(rng),source=source_checks(rng),
                reserves=degree_reserve_checks(),
                limitations=['initial random-feature energy-premise failure is preserved under review/',
                             'Fourier grid sums are not infinite-volume error certificates',
                             'finite source tests use generic labels, x=1, and no physical convergence assertion',
                             'determinant jets and source compositions share earlier helpers',
                             'complete Gaussian/contact derivative of one prescribed graph only',
                             'no residual mixed-pair representation or physical graph sum'])
    _OUTPUT_JSON.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: cubic cochain symbols and Gaussian derivative registers')
    print('per_site: finite support/grid fixtures')
    print('per_mode: finite Fourier grids and finite register degrees; no infinite-lattice execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
