"""Exact dark weights and two-refill law on the complete four-leaf record star."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,math
import sympy as s
sys.dont_write_bytecode=True
from repeated_formation_check import tree_model

HERE=Path(__file__).resolve().parent
m=tree_model(4);T=s.Matrix(m['T']);N=list(map(int,m['N'].diagonal()));W=list(map(int,m['W'].diagonal()))
p1=[i for i,n in enumerate(N) if n==1 and W[i]==0]
q1=[i for i,n in enumerate(N) if n==1 and W[i]==1]
p3=[i for i,n in enumerate(N) if n==3 and W[i]==0]
q3=[i for i,n in enumerate(N) if n==3 and W[i]==1]
assert len(p1)==1 and len(q1)==4 and len(p3)==18 and len(q3)==12
A3=T.extract(q3,p3);M=A3.T*A3
eigs=M.eigenvals()
assert all(k.is_Rational for k in eigs)
eigvalues=sorted(eigs)
projectors={}
for lam in eigvalues:
    P=s.eye(len(p3))
    for mu in eigvalues:
        if mu!=lam:P=P*(M-mu*s.eye(len(p3)))/(lam-mu)
    assert P*P==P and M*P==lam*P and P==P.T
    projectors[lam]=P
assert sum(projectors.values(),s.zeros(len(p3)))==s.eye(len(p3))
outrows={}
for kind in ('coherent','resolved'):
    vs=[s.Matrix(j).extract(p3,q1)*T.extract(q1,p1) for j in m[kind]]
    unnormalized=sum((v*v.T for v in vs),s.zeros(len(p3)))
    norm=s.trace(unnormalized);assert norm==24
    sigma=unnormalized/norm
    weights={str(lam):s.trace(P*sigma) for lam,P in projectors.items()}
    assert sum(weights.values())==1 and all(w>=0 for w in weights.values())
    # All decay channels vanish exactly on the P3 dark subspace in the bare
    # microscopic model too: hopping is A3 there, and births require a hole.
    assert A3*projectors[0]==s.zeros(len(q3),len(p3))
    for j in m[kind]:assert s.Matrix(j).extract(range(len(N)),p3)*projectors[0]==s.zeros(len(N),len(p3))
    outrows[kind]={'spectral_weights':{k:str(v) for k,v in weights.items()},
                  'eventual_second_birth_probability':str(1-weights['0']),
                  'post_first_birth_normalization':str(norm)}
recorded=json.loads((HERE/'REPEATED_FORMATION_RESULTS.json').read_text())
errors=[]
for row in recorded['full_dynamics_checks']:
    if row['model']!='star_4':continue
    delta=row['delta'];kappa=row['kappa'];r0=24*kappa*delta**2/(delta**2+9*kappa**2)
    b=2*kappa*delta**2/(delta**2+kappa**2)
    weights={int(k):float(s.Rational(v)) for k,v in outrows[row['instrument']]['spectral_weights'].items()}
    for old in row['rows']:
        t=old['time'];p0=math.exp(-r0*t)
        p1t=weights[0]*(1-p0)
        for lam,w in weights.items():
            if lam==0 or w==0:continue
            r=b*lam
            p1t+=w*(r0*t*math.exp(-r0*t) if abs(r-r0)<1e-12 else r0*(p0-math.exp(-r*t))/(r-r0))
        expected={'0':p0,'1':p1t,'2':1-p0-p1t}
        error=max(abs(expected[k]-old['effective_event_count_probabilities'][k]) for k in expected)
        assert error<2e-12
        errors.append(error)
result={'created_utc':datetime.now(timezone.utc).isoformat(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'model_source_sha256':hashlib.sha256((HERE/'repeated_formation_check.py').read_bytes()).hexdigest(),
        'recorded_results_sha256':hashlib.sha256((HERE/'REPEATED_FORMATION_RESULTS.json').read_bytes()).hexdigest(),
        'M_eigenvalue_multiplicities':{str(k):int(v) for k,v in eigs.items()},
        'instruments':outrows,'exact_projector_and_dark_identities':True,
        'effective_count_rows_compared':len(errors),'max_recorded_count_error':max(errors),
        'scope':'Exact finite four-leaf-star dark weights, microscopic eventual absorption and effective two-event law. Finite-time full dynamics checked in the separately bound runner.'}
target=HERE/'REPEATED_FORMATION_DARK_RESULTS.json';assert not target.exists()
data=json.dumps(result,indent=2)+'\n';target.write_text(data);print(data,end='')
