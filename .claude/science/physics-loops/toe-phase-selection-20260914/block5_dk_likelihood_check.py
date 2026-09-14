#!/usr/bin/env python3
"""Finite released DK likelihood protocol; conditional, with proper-prior cost.

The source coefficients and action are supplied. No formation law or Born
probability is selected by this calculation. Exact low-dimensional Schur
algebra is challenged by independent full covariance/precision calculations.
"""
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as source


def clean(matrix):
    return matrix.applyfunc(s.cancel)


def array(matrix):
    return np.array(matrix.evalf(),dtype=complex)


def arithmetic_circuit(linear,roster):
    """Independent roots, binary copy trees, unary scale, binary sum, noise.

    Every edge points to a later node. All scalar degrees are at most three.
    This is a logical circuit; its physical embedding is a separate obligation.
    """
    nodes=[]
    outputs=defaultdict(list)
    forms=[]
    def node(kind, parents=(), coefficients=(), root=None):
        i=len(nodes)
        form=defaultdict(lambda:s.Integer(0))
        if root is not None:
            form[root]=s.Integer(1)
        for p,c in zip(parents,coefficients):
            assert p<i
            outputs[p].append(i)
            for k,v in forms[p].items():
                form[k]+=c*v
        forms.append({k:s.expand(v) for k,v in form.items() if s.expand(v)!=0})
        nodes.append(dict(kind=kind,parents=list(parents),coefficients=list(map(str,coefficients)),
                          stage=0 if not parents else 1+max(nodes[p]['stage'] for p in parents)))
        return i
    roots=[node('root',root=j) for j in range(linear.cols)]
    usages=defaultdict(list)
    for i in range(linear.rows):
        for j in range(linear.cols):
            if (i,j) in roster:
                usages[j].append((i,linear[i,j]))
    row_terms=defaultdict(list)
    def split(parent,items):
        if len(items)==1:
            row,coefficient=items[0]
            row_terms[row].append(node('scale',(parent,),(coefficient,)))
            return
        middle=len(items)//2
        for part in (items[:middle],items[middle:]):
            child=node('copy',(parent,),(s.Integer(1),))
            split(child,part)
    for j,items in usages.items():
        split(roots[j],items)
    observations=[]
    for row in range(linear.rows):
        layer=row_terms[row]
        assert layer
        while len(layer)>1:
            next_layer=[]
            for start in range(0,len(layer),2):
                pair=layer[start:start+2]
                next_layer.append(pair[0] if len(pair)==1 else node('sum',pair,(s.Integer(1),)*2))
            layer=next_layer
        observed=node('observation',layer,(s.Integer(1),))
        expected={j:linear[row,j] for j in range(linear.cols) if linear[row,j]!=0}
        assert forms[observed]==expected
        observations.append(observed)
    degree=[len(n['parents'])+len(outputs[i]) for i,n in enumerate(nodes)]
    assert max(degree)<=3
    assert all(nodes[i]['stage']>nodes[p]['stage'] for i,n in enumerate(nodes) for p in n['parents'])
    topology=[(n['kind'],n['parents'],n['stage']) for n in nodes]
    return dict(nodes=len(nodes),edges=sum(map(len,outputs.values())),
                kinds=dict(Counter(n['kind'] for n in nodes)),maximum_degree=max(degree),
                maximum_stage=max(n['stage'] for n in nodes),
                exact_observation_linear_forms=True,
                topology_sha256=sha256(json.dumps(topology,sort_keys=True).encode()).hexdigest(),
                circuit_sha256=sha256(json.dumps(nodes,sort_keys=True).encode()).hexdigest())


def main():
    fixture=source.Fixture(4,pattern=None,tag='block5-likelihood')
    qs=[fixture.q({source.RECORD_CELL:value}) for value in source.MENU]
    ss=[clean((q+q.H)/2) for q in qs]
    edges=source.edge_union(tuple(ss))
    bundles={fraction:[source.arm_bundle(fixture,value,edges,fraction=fraction)
                       for value in source.MENU]
             for fraction in (s.Rational(1,2),s.Rational(1,3))}
    roster=set()
    for arms in bundles.values():
        for arm in arms:
            q,b=arm['q'],arm['B']
            n,k=q.rows,b.cols
            linear=q.row_join(-b).col_join(s.zeros(k,n).row_join(s.eye(k)))
            roster.update((i,j) for i in range(n+k) for j in range(n+k) if linear[i,j]!=0)
    rows=[]
    for fraction in (s.Rational(1,2),s.Rational(1,3)):
        arm_rows=[]
        for value,arm in zip(source.MENU,bundles[fraction]):
            q,b,S,c=arm['q'],arm['B'],arm['S'],arm['variance']
            n,k=q.rows,b.cols
            d=n+k
            assert all(r>=0 for r in arm['residuals'])
            assert clean(b*b.H+c*s.eye(n)-S)==s.zeros(n)
            linear=q.row_join(-b).col_join(s.zeros(k,n).row_join(s.eye(k)))
            noise=s.diag(c*s.eye(n),s.eye(k))
            qinv=arm['q_inv']
            c0=arm['W'].row_join(qinv*b).col_join((b.H*qinv.H).row_join(s.eye(k)))
            Q0=clean(linear.H*noise.inv()*linear)
            # Exact right inverse, including radical cross-block entries.
            assert clean(Q0*c0)==s.eye(d)
            trace=s.cancel(s.trace(c0))
            lower=1/trace
            det0=s.cancel(source.norm2(arm['det_q'])/c**n)
            assert s.cancel(1/det0-arm['raw_mass'])==0
            naive_phi_block=clean(q.H*q/c)
            phi_off=sum(1 for i in range(n) for j in range(i+1,n) if naive_phi_block[i,j]!=0)
            unconditional=array(s.eye(d))
            ln=array(linear)
            nn=array(noise)
            cn=array(c0)
            qn=array(Q0)
            assert np.linalg.norm(qn@cn-np.eye(d),ord=2)<1e-10
            assert np.linalg.eigvalsh(qn)[0]>float(lower)
            variants=[]
            for alpha in (s.Rational(1,10),s.Rational(1,100)):
                # Integrate the zeta block using Sylvester's determinant identity.
                sa=S+alpha*c*s.eye(n)
                pphi=clean(alpha*s.eye(n)+(1+alpha)*q.H*source.exact_inv(sa)*q)
                ddet=(1+alpha)**(k-n)*source.dm_det(sa)/c**n
                deta=s.cancel(ddet*source.dm_det(pphi))
                exact_phi=source.exact_inv(pphi)
                numeric_q=qn+float(alpha)*np.eye(d)
                numeric_c=np.linalg.inv(numeric_q)
                assert np.linalg.norm(numeric_c[:n,:n]-array(exact_phi),ord=2)<1e-10
                sign,logdet=np.linalg.slogdet(numeric_q)
                assert abs(sign-1)<1e-10
                assert abs(logdet-float(s.log(deta)))<1e-9
                # Independently condition the full generative joint covariance.
                prior=unconditional/float(alpha)
                ycov=ln@prior@ln.conj().T+nn
                conditioned=prior-prior@ln.conj().T@np.linalg.solve(ycov,ln@prior)
                assert np.linalg.norm(conditioned-numeric_c,ord=2)<1e-8
                density_log=-d*np.log(np.pi)-np.linalg.slogdet(ycov)[1]
                expected=d*np.log(float(alpha))-d*np.log(np.pi)-n*np.log(float(c))-logdet
                assert abs(density_log-expected)<1e-9
                ratio=s.cancel(deta/det0)
                assert ratio>=1 and ratio<=(1+alpha/lower)**d
                # Complex Gaussian KL, independently from trace/log determinants.
                kl=float(np.trace(qn@numeric_c).real-d+logdet-float(s.log(det0)))
                kl_bound=d*float(alpha/lower)**2/2
                assert -1e-10<=kl<=kl_bound
                covariance_error=float(np.linalg.norm(numeric_c-cn,ord=2))
                assert covariance_error<=float(alpha/lower**2)
                # Store pi^d p(Y=0)/alpha^d; its limit differs from raw mass
                # by det(noise), which is constant only within the arm menu.
                scaled_density=s.cancel(1/(c**n*deta))
                variants.append(dict(alpha=str(alpha),determinant_ratio=str(ratio),
                                     scaled_observation_density=str(scaled_density),
                                     gaussian_kl=kl,kl_upper_bound=kl_bound,
                                     covariance_error=covariance_error,
                                     covariance_error_bound=float(alpha/lower**2)))
            arm_rows.append(dict(value=str(value),phi_dimension=n,zeta_dimension=k,
                                 complex_dimension=d,trace_target_covariance=str(trace),
                                 precision_lower_bound=str(lower),target_raw_mass=str(arm['raw_mass']),
                                 phi_block_nonzero_upper_offdiagonals=phi_off,
                                 naive_two_layer_phi_block_diagonal=(phi_off==0),
                                 logical_likelihood_circuit=arithmetic_circuit(linear,roster),variants=variants))
            print(f'checked supplied c={fraction}, arm={value}, complex dimension={d}',flush=True)
        masses=[s.Rational(r['target_raw_mass']) for r in arm_rows]
        target=[v/sum(masses) for v in masses]
        lower=min(s.Rational(r['precision_lower_bound']) for r in arm_rows)
        weights=[]
        for j,alpha in enumerate((s.Rational(1,10),s.Rational(1,100))):
            densities=[s.Rational(r['variants'][j]['scaled_observation_density']) for r in arm_rows]
            actual=[v/sum(densities) for v in densities]
            tv=s.cancel(sum(abs(a-b) for a,b in zip(actual,target))/2)
            bound=1-(1+alpha/lower)**(-arm_rows[0]['complex_dimension'])
            assert tv<=bound
            tilts=[1/s.Rational(a['variants'][j]['determinant_ratio']) for a in arm_rows]
            low,high=min(tilts),max(tilts)
            sharp=(s.sqrt(high)-s.sqrt(low))/(s.sqrt(high)+s.sqrt(low))
            assert float(tv)<=float(sharp)+1e-14
            weights.append(dict(alpha=str(alpha),normalized=[str(v) for v in actual],
                                target=[str(v) for v in target],tv=float(tv),
                                tv_upper_bound=float(bound),
                                exact_extremal_tilt_upper_bound=float(sharp)))
        rows.append(dict(fraction=str(fraction),arms=arm_rows,menu_weights=weights))
    topologies={a['logical_likelihood_circuit']['topology_sha256'] for row in rows for a in row['arms']}
    assert len(topologies)==1
    result=dict(source_path=str(Path(source.__file__).relative_to(ROOT)),
                source_sha256=sha256(Path(source.__file__).read_bytes()).hexdigest(),
                supplier_certificate=source.supplier_certificate(),
                common_circuit_topology_sha256=next(iter(topologies)),
                common_linear_coefficient_roster=len(roster),
                source_condition='T_cover=12, width=4, xgraded, mass=1, four supplied Record values',
                rows=rows,
                scope='Proper independent prior and supplied noisy linear circuit; source law is recovered only by conditioning and an alpha-to-zero limit. Physical wire embedding is separate. No selected native or Born law.')
    assert result['supplier_certificate']
    Path(__file__).with_name('BLOCK5_DK_LIKELIHOOD_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__':
    main()
