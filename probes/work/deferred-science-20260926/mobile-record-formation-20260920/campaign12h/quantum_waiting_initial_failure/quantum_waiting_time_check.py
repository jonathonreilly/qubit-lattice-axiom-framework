#!/usr/bin/env python3
"""Primary exact and matrix-exponential checks of no-event statistics."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

HERE=Path(__file__).resolve().parent
V=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
S=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
rho=[(np.eye(2)+sum(v[i]*S[i] for i in range(3)))/2 for v in V]


def main():
    epsilon,j,t,dot=sp.symbols('epsilon j t dot',real=True)
    rT=epsilon*(6+2*j*j);rS=epsilon*(6-6*j*j);w=(1-dot)/4
    mean=sp.expand((1-w)*rT+w*rS)
    assert mean==epsilon*(6+2*j*j*dot).expand()
    variance=sp.simplify((1-w)*rT*rT+w*rS*rS-mean*mean)
    assert sp.simplify(variance-64*epsilon**2*j**4*w*(1-w))==0
    mixture_gap=sp.exp(-6*epsilon*t)*(sp.cosh(2*epsilon*j*j*t)-1)
    assert sp.limit(mixture_gap/(2*t*t),t,0)==epsilon**2*j**4
    # The two physically equal mixed preparations agree for a single effect.
    exact_rhos=[]
    pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
    for v in V:
        exact_rhos.append((sp.eye(2)+sum((int(v[i])*pauli[i] for i in range(3)),sp.zeros(2)))/2)
    assert (exact_rhos[0]+exact_rhos[1])/2==(exact_rhos[2]+exact_rhos[3])/2==sp.eye(2)/2
    cases=[]; maximum=0.;maximum_mixture=0.
    for jj,ee,tt in product([-.8,-.5,0,.1,.5,.8],[.05,1.],[.01,.5,3.]):
        R=ee*(6*np.eye(4)+2*jj*jj*sum(np.kron(s,s) for s in S))
        no=expm(-tt*R/2);effect=no.conj().T@no
        assert np.linalg.eigvalsh(effect).min()>-1e-12 and np.linalg.eigvalsh(np.eye(4)-effect).min()>-1e-12
        numerical=np.zeros((6,6));classical=np.zeros((6,6));error=0.
        for a,c in product(range(6),repeat=2):
            dc=int(V[a]@V[c]);weight=(1-dc)/4
            value=np.trace(effect@np.kron(rho[a],rho[c])).real
            target=(1-weight)*np.exp(-ee*(6+2*jj*jj)*tt)+weight*np.exp(-ee*(6-6*jj*jj)*tt)
            error=max(error,abs(value-target));numerical[a,c]=value
            classical[a,c]=np.exp(-ee*(6+2*jj*jj*dc)*tt)
            assert value>=classical[a,c]-1e-13
        assert error<1e-12
        numerical_gap=(numerical[0,0]+numerical[1,0]-numerical[2,0]-numerical[3,0])/2
        requested_gap=(classical[0,0]+classical[1,0]-classical[2,0]-classical[3,0])/2
        formula=np.exp(-6*ee*tt)*(np.cosh(2*ee*jj*jj*tt)-1)
        assert abs(numerical_gap)<1e-12 and abs(requested_gap-formula)<1e-12
        maximum=max(maximum,error);maximum_mixture=max(maximum_mixture,abs(requested_gap-formula))
        cases.append({'j':jj,'epsilon':ee,'time':tt,'matrix_exponential_max_error':error,
                      'quantum_equal_preparation_gap':numerical_gap,'classical_equal_preparation_gap':requested_gap,
                      'universal_worst_row_probability_error_lower_bound':formula/2})
    result={'status':'All primary exact and matrix-exponential checks passed',
            'symbolic_mean_rate_identity':str(mean),'symbolic_rate_variance':str(variance),
            'universal_short_time_error_coefficient':'epsilon^2 j^4',
            'cases':cases,'max_matrix_exponential_error':maximum,'max_classical_mixture_formula_error':maximum_mixture,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies':{'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'scope':'Two unknown physical input qubits without preparation information; positive instantaneous quantum rates do not reproduce fixed-label classical exponential waiting histories.'}
    text=json.dumps(result,indent=2)+'\n';(HERE/'QUANTUM_WAITING_TIME_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__': main()
