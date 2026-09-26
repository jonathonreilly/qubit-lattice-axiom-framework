#!/usr/bin/env python3
"""Exact fresh-pair readout of a spin-half plaquette, with spectators.

Every claim is conditional on the supplied instrument and local roles.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

OUT=Path(__file__).resolve().parent
I=sp.I


def sparse_kron(*args):return sp.SparseMatrix(sp.kronecker_product(*args))


def zero(a):return all(sp.expand(v)==0 for v in a.values())


def edge_op(a,edge):
    return sparse_kron(*(a if j==edge else sp.eye(2) for j in range(4)))


def exact_all():
    plus=sp.SparseMatrix([[0,0],[1,0]])
    z=sp.diag(-1,1)
    ef=[edge_op(z,j)/2 for j in range(4)]
    # Oriented boundary 0->1->2->3->0; canonical edge2 runs3->2,
    # canonical edge3 runs0->3, hence two lowering factors.
    w=sparse_kron(plus,plus,plus.T,plus.T)
    x=w+w.T;y=-I*(w-w.T);p=w.T*w+w*w.T;ze=2*ef[0]
    i16=sp.SparseMatrix(sp.eye(16))
    assert zero(x*x-p) and zero(y*y-p)
    assert zero(x**3-x) and zero(y**3-y)
    assert zero(ze*w-w*ze-2*w)
    assert zero(ze*p-p*ze)
    incidence=sp.Matrix([[1,0,0,1],[-1,1,0,0],[0,-1,-1,0],[0,0,1,-1]])
    divergences=[sum((incidence[v,j]*ef[j] for j in range(4)),sp.zeros(16)) for v in range(4)]
    for div in divergences:
        for a in (w,x,y,p,ze):assert zero(div*a-a*div)

    q3=sp.diag(0,1,-1);n3=sp.diag(0,1,1);vac3=sp.diag(1,0,0)
    matter_charge=[sparse_kron(q3,sp.eye(3)),sparse_kron(sp.eye(3),q3)]
    nm=sparse_kron(n3,sp.eye(3))+sparse_kron(sp.eye(3),n3)
    pv_m=sparse_kron(vac3,vac3);pv=sparse_kron(pv_m,i16)
    n=sparse_kron(nm,i16);i144=sp.SparseMatrix(sp.eye(144))
    gs=[sparse_kron(sp.eye(9),div)-(sparse_kron(matter_charge[v],i16) if v<2 else sp.zeros(144))
        for v,div in enumerate(divergences)]
    vops={}
    for q in (1,-1):
        a=sp.zeros(3);a[1 if q==1 else 2,0]=1
        b=sp.zeros(3);b[2 if q==1 else 1,0]=1
        v=sparse_kron(a,b,edge_op(plus if q==1 else plus.T,0));vops[q]=v
        for g in gs:assert zero(g*v-v*g)
        assert zero(n*v-v*n-2*v)
        assert zero(v.T*v-sparse_kron(pv_m,(i16-q*ze)/2))
    assert zero(sum((v.T*v for v in vops.values()),sp.zeros(144))-pv)

    contexts=[]
    for axis,op in [('Y',y),('X',x)]:
        for s in (1,-1):
            pulse=i16+(sp.sqrt(2)/2-1)*p-I*s*sp.sqrt(2)*op/2
            assert zero(pulse.conjugate().T*pulse-i16)
            target=ze*(i16-p)+(-s*x if axis=='Y' else s*y)
            assert zero(pulse.conjugate().T*ze*pulse-target)
            gated=sparse_kron(pv_m,pulse)+sparse_kron(sp.eye(9)-pv_m,i16)
            birth={q:v*gated for q,v in vops.items()}
            assert zero(sum((b.conjugate().T*b for b in birth.values()),sp.zeros(144))-pv)
            mean=sum((q*b.conjugate().T*b for q,b in birth.items()),sp.zeros(144))
            assert zero(mean+sparse_kron(pv_m,target))
            for b in birth.values():
                for g in gs:assert zero(g*b-b*g)
            contexts.append({'axis':axis,'setting':s,'pulse_unitarity':'exact',
                             'Gauss_commutators':'all4 zero','total_birth_effect':'P_v',
                             'charge_mean_operator':'-Z(I-P)+sX' if axis=='Y' else '-Z(I-P)-sY'})
    d=sp.diag(*[sp.exp(-I*sp.pi*int(ze[j,j])/4) for j in range(16)])
    assert zero(d*x*d.conjugate().T-y)

    # Explicit physical doublet, found from the actual nonzero ring matrix.
    dest,src=next(iter(w.todok()))
    a=sp.zeros(16,1);a[src]=1;b=sp.zeros(16,1);b[dest]=1
    assert ze[dest,dest]==1 and ze[src,src]==-1
    for div in divergences:assert zero(div*a) and zero(div*b)
    states={'real_plus':(a+b)/sp.sqrt(2),'real_minus':(a-b)/sp.sqrt(2),
            'imag_plus':(a+I*b)/sp.sqrt(2)}
    probabilities=[]
    for label,psi in states.items():
        row={'state':label,'X':str(sp.expand((psi.conjugate().T*x*psi)[0])),
             'Y':str(sp.expand((psi.conjugate().T*y*psi)[0])),'outcomes':[]}
        for axis,op in [('Y',y),('X',x)]:
            for s in (1,-1):
                pulse=i16+(sp.sqrt(2)/2-1)*p-I*s*sp.sqrt(2)*op/2
                for q in (1,-1):
                    prob=sp.expand((psi.conjugate().T*pulse.conjugate().T*(i16-q*ze)*pulse*psi)[0]/2)
                    row['outcomes'].append({'axis':axis,'setting':s,'new_tail_charge':q,'probability':str(prob)})
        probabilities.append(row)
    assert [sp.expand(v*sp.conjugate(v)) for v in states['real_plus']]==[sp.expand(v*sp.conjugate(v)) for v in states['real_minus']]

    # Nonflippable basis states: one context alone is biased; contrasts cancel.
    nonflip=[]
    for j in range(16):
        if p[j,j]:continue
        first=-ze[j,j]
        assert x[j,j]==0 and y[j,j]==0
        nonflip.append({'basis':j,'m_plus':str(first),'m_minus':str(first),'contrast':0})

    # Orthogonal spent outcomes and an exact resource-conserving dilation.
    pf=sp.diag(1,0,0);c=sp.SparseMatrix(sp.zeros(432))
    for index,q in enumerate((1,-1),start=1):
        sf=sp.zeros(3);sf[index,0]=1
        c+=sparse_kron(vops[q],sf)+sparse_kron(vops[q].T,sf.T)
    assert zero(c.conjugate().T-c)
    assert zero(c**3-c)
    resource=sparse_kron(n,sp.eye(3))+2*sparse_kron(i144,pf)
    assert zero(c*resource-resource*c)
    for g in gs:assert zero(c*sparse_kron(g,sp.eye(3))-sparse_kron(g,sp.eye(3))*c)
    gate=sp.SparseMatrix(sp.eye(432))-c*c-I*c
    assert zero(gate.conjugate().T*gate-sp.eye(432))
    fuel_cols=[j*3 for j in range(144)]
    k0=gate.extract(fuel_cols,fuel_cols)
    assert zero(k0-(i144-pv))
    for index,q in enumerate((1,-1),start=1):
        rows=[j*3+index for j in range(144)]
        assert zero(gate.extract(rows,fuel_cols)+I*vops[q])
    # The probe is a quantum instrument, not a noninvasive correlator meter.
    # Without a pulse, phase is lost to the distinct q pointer outcomes.
    matter_vac=sp.zeros(9,1);matter_vac[0]=1
    psi=sparse_kron(matter_vac,states['real_plus'])
    rho=psi*psi.conjugate().T
    out=sum((v*rho*v.T for v in vops.values()),sp.zeros(144))
    purity=sp.simplify(sp.trace(out*out));assert purity==sp.Rational(1,2)
    assert sp.trace(n*out)==2
    return {'local_field_dimension':16,'matter_field_dimension':144,'dilated_dimension':432,
            'physical_flippable_doublet':{'source_basis':src,'target_basis':dest,'all_divergences':0},
            'exact_contexts':contexts,'phase_state_record_probabilities':probabilities,
            'electric_probabilities_real_plus_minus':'identical at all16 basis words',
            'nonflippable_bias_controls':nonflip,
            'diagonal_phase_synthesis':'D X Ddagger = Y exactly',
            'dilation':{'C_cubic':'C^3=C','Gauss_commutators':'all4 zero',
                        'resource_commutator':'zero','gate_unitarity':'exact',
                        'fuel_Kraus':'I-P_v','spent_Kraus':['-i V_+','-i V_-']},
            'backaction_control':{'input':'physical positive real cat, no pulse','output_purity':str(purity),
                                   'output_record_count':2,'interpretation':'Fresh charge pointer distinguishes branches and disturbs the field/matter state.'}}


def main():
    result={'status':'PASS','exact_results':exact_all(),'failed_attempts':[],
            'limits':'Supplied local gauge roles, controllable pulses and Born instrument. No microscopic native compiler, universal charge export, full energy accounting or unperturbed two-time correlator is established.'}
    (OUT/'FRESH_CHARGED_RECORD_LOOP_READOUT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
