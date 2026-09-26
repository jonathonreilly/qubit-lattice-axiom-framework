#!/usr/bin/env python3
"""Exact local matrix entry after a depolarized classical pointer encoding.

Uses the full four-position swap rate on the two stencils selected by a
three-position output difference in the actual three-dimensional generator.
Does not construct an exponentially large torus matrix.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,itertools,json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent


def main():
    labels=[(0,np.eye(3,dtype=np.int64)[i]*s) for i in range(3) for s in (1,-1)]
    labels += [(1,np.array(b,dtype=np.int64)) for b in itertools.product((-1,1),repeat=3)]
    e=np.array([z if o==0 else np.zeros(3,dtype=np.int64) for o,z in labels])
    b=np.array([z if o==1 else np.zeros(3,dtype=np.int64) for o,z in labels])
    directions=[np.eye(3,dtype=np.int64)[i]*s for i in range(3) for s in (1,-1)]
    C={tuple(d):np.array([[int(d@(np.cross(e[a],b[c])+np.cross(e[c],b[a]))) for c in range(14)] for a in range(14)],dtype=np.int64) for d in directions}
    assert all(np.array_equal(c,c.T) and np.all(c.sum(axis=0)==0) and np.all(np.diag(c)==0) for c in C.values())
    N=12
    def add(x,y,k=1): return tuple((np.array(x)+k*np.array(y))%N)
    step=(-2,0,0)
    changed=[(0,0,0),add((0,0,0),step),add((0,0,0),step,2)]
    # B(-,-,-), B(+,-,-), A(+e2), all distinct.
    ycolors=[6,10,2]
    xcolors=[2,6,10]
    y=dict(zip(changed,ycolors));x=dict(zip(changed,xcolors))
    candidates=[]
    for u in itertools.product(range(N),repeat=3):
        if sum(u)%2: continue
        for d in directions:
            a=tuple(d-np.array([1,0,0]))
            if a==(0,0,0):continue
            positions=[add(u,a,-1),u,add(u,a),add(u,a,2)]
            assert len(set(positions))==4
            if set(changed)<=set(positions):
                candidates.append((tuple(d),positions))
    assert len(candidates)==2 and all(d==(-1,0,0) for d,p in candidates)
    # eta=1/2: B=(14I+ones)/28, B^-1=(28I-ones)/14.
    BN=14*np.eye(14,dtype=np.int64)+np.ones((14,14),dtype=np.int64)
    IN=28*np.eye(14,dtype=np.int64)-np.ones((14,14),dtype=np.int64)
    assert np.array_equal(BN@IN,392*np.eye(14,dtype=np.int64))
    states=np.array(list(itertools.product(range(14),repeat=4)),dtype=np.int64)
    swapped=states[:,[0,2,1,3]]
    terms=[]
    for d,positions in candidates:
        xx=[x.get(p,0) for p in positions]; yy=[y.get(p,0) for p in positions]
        inverse_weight=np.prod(np.stack([IN[states[:,j],yy[j]] for j in range(4)]),axis=0,dtype=np.int64)
        out_swapped=np.prod(np.stack([BN[xx[j],swapped[:,j]] for j in range(4)]),axis=0,dtype=np.int64)
        out_original=np.prod(np.stack([BN[xx[j],states[:,j]] for j in range(4)]),axis=0,dtype=np.int64)
        c=C[d];l,a,bb,rr=states.T
        hnum=c[l,a]+c[a,rr]-c[l,bb]-c[bb,rr]
        rate_num=22+5*hnum  # r=(11/20)+hnum/8, denominator40.
        assert int(rate_num.min())>0
        weights=inverse_weight*(out_swapped-out_original)
        baseline=Fraction(int((weights*22).sum()),40*392**4)
        bias=Fraction(int((weights*5*hnum).sum()),40*392**4)
        total=Fraction(int((weights*rate_num).sum()),40*392**4)
        assert baseline==0 and total==bias
        terms.append(dict(direction=d,positions=positions,input_colors=yy,output_colors=xx,
                          enumerated_stencil_states=len(states),baseline=str(baseline),bias=str(bias),total=str(total),
                          minimum_rate=str(Fraction(int(rate_num.min()),40))))
    entry=sum((Fraction(t['total']) for t in terms),Fraction(0))
    assert entry==Fraction(-5,3136)
    # A separate pair contraction verifies the symbolic all-noise expression.
    eta=sp.Symbol('eta',positive=True)
    r=1-eta; q=eta/14
    w_ab=lambda a,bb:sp.Matrix([q/r*(int(i==bb)-r*int(i==a)-q) for i in range(14)])
    cs=sp.Matrix(C[(-1,0,0)].tolist())/2
    symbolic_terms=[]
    for a,bb in [(2,6),(2,10)]:
        value=sp.factor((w_ab(a,bb).T*cs*w_ab(bb,a))[0])
        expected=sp.factor(q*q*(1+r*r)/(r*r)*cs[a,bb])
        assert sp.factor(value-expected)==0
        symbolic_terms.append(value)
    general=sp.factor(-sum(symbolic_terms)/4)
    assert general.subs(eta,sp.Rational(1,2))==sp.Rational(-5,3136)
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                status='author_exact_scoped_certificate_independent_check_pending',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                torus_N=N,black_sites=N**3//2,rate_parameters=dict(k0='11/10',gamma='1'),
                noise_eta='1/2',pointer_basis_size=14,changed_positions=changed,
                input_colors=ycolors,output_colors=xcolors,candidate_stencils=terms,
                full_generator_offdiagonal_entry=str(entry),all_eta_entry=str(general),
                all_eta_domain='0 < eta < 1; sign negative; gamma=1. At gamma=0 bias vanishes; at eta=0 the orthogonal code is recovered. eta=1 loses faithfulness and the inverse does not exist.',
                one_factor_wave_metric=dict(u='7*(1-eta)^2',v='7*(1-eta)^2/4',cross='0',matching='u=4v exactly'),
                scope='The product depolarized fourteen-pointer code cannot intertwine this full classical generator with a positive trace-preserving quantum evolution: linear inversion forces a negative initial output probability from a pure pointer configuration. Other encodings, generators and approximate realizations are not tested.')
    encoded=json.dumps(result,indent=2)+'\n';(HERE/'NOISY_POINTER_GENERATOR_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()
