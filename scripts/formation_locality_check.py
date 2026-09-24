"""Exact site-star decomposition of the finite formation generator."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/formation_locality_check.py', 'scripts/repeated_formation_check.py')
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import sympy as s
sys.dont_write_bytecode=True
from repeated_formation_check import tree_model

HERE=Path(__file__).resolve().parent
delta=s.Rational(13,10);kappa=s.Rational(7,10)
rows=[]
for model in [tree_model(2),tree_model(4),tree_model(None)]:
    dim=len(model['states']);T=s.Matrix(model['T']);p=list(map(int,model['p']));q1=list(map(int,model['q1']))
    all_eff_losses=[]
    for kind in ['coherent','resolved']:
        jumps=list(map(s.Matrix,model[kind]));loss=sum((j.T*j for j in jumps),s.zeros(dim))
        D=delta*s.eye(len(q1))-s.I*kappa*loss.extract(q1,q1)/2
        A=T.extract(q1,p);inv=D.inv();B=A.T*inv*A
        H=-delta**2*(B+B.conjugate().T)/2
        # Use unscaled jumps; their dissipators have coefficient kappa.
        eff=[delta*j.extract(p,q1)*inv*A for j in jumps]
        Hlocal=s.zeros(len(p));local_eff=[s.zeros(len(p)) for _ in jumps];sites=[]
        for a in model['A_sites']:
            qa=[i for i in q1 if model['states'][i][0][a]==0]
            others=[i for i in q1 if i not in qa]
            assert loss.extract(qa,others)==s.zeros(len(qa),len(others))
            Da=delta*s.eye(len(qa))-s.I*kappa*loss.extract(qa,qa)/2
            Aa=T.extract(qa,p);Ba=Aa.T*Da.inv()*Aa
            Ha=-delta**2*(Ba+Ba.conjugate().T)/2;Hlocal+=Ha
            localjs=[]
            for j,J in enumerate(jumps):
                L=delta*J.extract(p,qa)*Da.inv()*Aa
                local_eff[j]+=L
                if L!=s.zeros(len(p)):localjs.append(j)
            degree=sum(a in edge for edge in model['edges'])
            sites.append({'A_site':a,'degree':degree,'one_hole_dimension':len(qa),
                          'nonzero_effective_channel_indices':localjs})
        assert s.simplify(H-Hlocal)==s.zeros(len(p))
        assert all(s.simplify(a-b)==s.zeros(len(p)) for a,b in zip(eff,local_eff))
        Gamma=kappa*sum((j.conjugate().T*j for j in eff),s.zeros(len(p)))
        all_eff_losses.append(Gamma)
        diagonal_rates=[]
        if model['label'].startswith('star_'):
            for ii,idx in enumerate(p):
                q,E=model['states'][idx];vac=sum(v==0 for v in q[1:])
                expected=2*vac*(vac-1)*kappa*delta**2/(delta**2+kappa**2*(vac-1)**2) if vac else 0
                assert s.simplify(Gamma[ii,ii]-expected)==0
                diagonal_rates.append({'q':q,'empty_leaves':vac,'rate':str(s.factor(Gamma[ii,ii]))})
        rows.append({'model':model['label'],'instrument':kind,'sites':sites,
                     'global_resolvent_equals_sum_of_site_star_H_and_channels':True,
                     'basis_state_formation_rates':diagonal_rates})
    assert all_eff_losses[0]==all_eff_losses[1]
result={'created_utc':datetime.now(timezone.utc).isoformat(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'model_source_sha256':hashlib.sha256((HERE/'repeated_formation_check.py').read_bytes()).hexdigest(),
        'controls':rows,'coherent_and_resolved_effective_losses_equal_in_all_controls':True,
        'scope':'Exact finite operator decompositions and basis rates. General locality/norm bounds and rotor extension rest on the separately written proof.'}
p=HERE/'FORMATION_LOCALITY_RESULTS.json';assert not p.exists()
data=json.dumps(result,indent=2)+'\n';p.write_text(data);print(data,end='')
