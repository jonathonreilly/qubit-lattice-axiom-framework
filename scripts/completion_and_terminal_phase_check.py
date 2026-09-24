"""Root exact accessible-output checks for the electric-completion family.

Reuses the sealed root rotor path code and separately compares the marked
outputs with the older independent path implementation. This is author
evidence; a new independent review is a separate artifact.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/completion_and_terminal_phase_check.py', 'scripts/cube_high_flux_birth.py', 'scripts/full_rotor_energy_control.py', 'scripts/mobile_compensation_model_20260924.py')
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE
SOURCE = BASE / 'full_rotor_energy_control.py'
MODEL = BASE / 'mobile_compensation_model_20260924.py'
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod
r=load('completion_root_paths',SOURCE)
old=load('completion_older_paths',MODEL)
assert hashlib.sha256(MODEL.read_bytes()).hexdigest()=='eb53d8e60b7bbef8ccfb460fc64b25cab007edb87cd7af45151d76f52c95c23a'


def diag(v,lam):
    return r.add(r.scale(r.d(v),1-lam),r.scale(r.d(v,True),lam))


def older_birth(v,edge,sign):
    out={}
    for s,c in v.items():
        for t,a in old.effective_birth(s,old.CUBE_EDGES.index(edge),sign,
                                       old.CUBE_A,old.CUBE_EDGES).items():
            out[t]=out.get(t,0)+c*F(a)
    return out


def case(n):
    q,E=r.m.initial(n);omega={(tuple(q),tuple(E)):F(1)}
    first=r.birth(omega,(0,1),1)
    second=r.birth(first,(6,7),1)
    assert first==older_birth(omega,(0,1),1)
    assert second==older_birth(older_birth(omega,(0,1),1),(6,7),1)
    assert r.dot(first,first)==2 and r.dot(second,second)==2
    assert all(all(q) for q,E in second)
    assert r.h4(second)=={} and r.d(second)=={}
    terminal_energies=sorted(sum(e*e for e in E) for q,E in second)
    assert terminal_energies==sorted((4*n*n+4*n+4,4*n*n+2*n+4))
    states=list(second)
    difference=tuple(a-b for a,b in zip(states[0][1],states[1][1]))
    assert sum(e*e for e in difference)==4
    assert states[0][0]==states[1][0]
    # The difference is a divergence-free unit circulation of square0-2-6-4.
    expected={r.m.EDGE[e] for e in ((0,2),(2,6),(4,6),(0,4))}
    assert {i for i,e in enumerate(difference) if e}==expected
    div=[0]*8
    for (a,b),e in zip(r.m.EDGES,difference):div[a]+=e;div[b]-=e
    assert not any(div)
    lambdas=[]
    for lam in (F(0),F(1,3),F(1,2),F(1)):
        D=diag(first,lam);norm=r.dot(first,first)
        mean=r.dot(first,D)/norm
        variance=r.dot(D,D)/norm-mean**2
        expected_mean=(1+3*lam)*n*n+3*lam*n+2*lam
        expected_var=((1-lam)*n*n-lam*n)**2
        assert mean==expected_mean and variance==expected_var
        V=r.h4(first)
        cov=r.dot(D,V)/norm-mean*r.dot(first,V)/norm
        assert cov==0
        e0,e1=[lam*sum(e*e for e in E) for q,E in states]
        assert abs(e0-e1)==2*lam*abs(n)
        lambdas.append({'lambda':str(lam),'first_D_lambda_mean':str(mean),
                        'first_D_lambda_variance':str(variance),
                        'D_lambda_H4_covariance':str(cov),
                        'terminal_frequency_over_K_absolute':str(abs(e0-e1))})
    return {'n':n,'ordered_two_mark_norm_squared':2,
            'small_time_history_probability_over_kappa2_t2':1,
            'terminal_states':[{'q':q,'E':E} for q,E in states],
            'wilson_translation_difference':difference,
            'terminal_E2_eigenvalues':terminal_energies,'lambdas':lambdas}


rows=[case(n) for n in (-7,-2,-1,0,1,2,19)]
local_bounds=[]
for S in (1,2,3,4,8,16):
    C=S*(S+1);largest=F(0)
    for E in range(-S,S+1):
        for qa in (-1,0,1):
            for qb in (-1,0,1):
                for orientation in (-1,1):
                    d=int(qa!=0 and qb==0)*E*(E-orientation*qa)
                    R=F(E*E-d,C)
                    largest=max(largest,abs(R))
                    assert abs(R)<=1
                    if qa and not qb: assert 0<=d<=C
    assert largest==F(S,S+1)
    local_bounds.append({'S':S,'exact_largest_abs_local_R':str(largest)})
report={'scope':'root conditional completion and terminal interference control',
        'source_sha256':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (SOURCE,MODEL,BASE/'cube_high_flux_birth.py')},
        'rows':rows,'local_diagonal_bounds':local_bounds}
print(json.dumps(report,indent=2))
