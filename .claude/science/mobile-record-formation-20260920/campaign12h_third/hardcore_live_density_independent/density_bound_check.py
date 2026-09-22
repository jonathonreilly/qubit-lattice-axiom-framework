"""Exact clock normalization and symbolic bookkeeping for the density estimate."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('own_finite_sector',HERE/'finite_sector_check.py')
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
model=own.build(6,[(i,(i+1)%6) for i in range(6)],{0,2,4},0)
n=len(model['states']); zero=s.zeros(n)
hop=sum(model['hop'],zero); total=s.diag(*map(int,model['occ'].sum(axis=1)))
vector=s.zeros(n,1);vector[model['states'].index(0)]=vector[model['states'].index(63)]=1
rho=vector*vector.T/2
coupling=s.Rational(3,2); beta=s.Rational(2,5); delta=7
rows=[]
for potential,values in [('sublattice',model['b']),('field_squared',model['field'])]:
    h=delta*s.diag(*values)-coupling*hop
    for mode in ['coherent_plus','coherent_minus','resolved']:
        jumps=[]
        for v in model['births']:
            jumps.extend([v[1],v[-1]] if mode=='resolved' else [v[1]+(1 if mode=='coherent_plus' else -1)*v[-1]])
        def dual_generator(o):return s.I*(h*o-o*h)+beta*sum((own.dual(j,o) for j in jumps),zero)
        current=total; deriv=[]
        for k in range(4):
            deriv.append(s.simplify(s.trace(rho*current)/6))
            if k<3:current=dual_generator(current)
        assert deriv==[s.Rational(1,2),0,0,2*beta*coupling**2]
        rows.append({'potential':potential,'instrument':mode,'time_derivatives_orders_0_to_3_of_record_density':list(map(str,deriv)),'time_cubic_coefficient':str(deriv[3]/6)})
d,alph,kap,bet,C,lam,time=s.symbols('d alpha kappa beta C lambda time',positive=True)
c=(2*d-1)*bet; a=4*kap*d*bet/alph+c
bound=C*C*lam*lam/(alph*alph)*(s.exp(a*time)+c/a*(s.exp(a*time)-1))
assert s.simplify(s.diff(bound,time)-a*bound-c*C*C*lam*lam/(alph*alph))==0
assert s.simplify(bound.subs(time,0)-C*C*lam*lam/(alph*alph))==0
assert s.simplify(a.subs({alph:1,kap:1})-(6*d-1)*bet)==0
assert s.simplify(a.subs({alph:s.Rational(1,2),kap:2})-(18*d-1)*bet)==0
out={'created_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'own_operator_builder_sha256':sha256((HERE/'finite_sector_check.py').read_bytes()).hexdigest(),'exact_clock_controls':rows,'symbolic_scalar_bound_ODE':'Verified exactly for general positive alpha,kappa,C,lambda,beta,d; d is an integer >=1 in the theorem.','exponents':{'sublattice':'(6d-1) beta','field_squared':'(18d-1) beta'},'normalization':'One coherent sign per edge or two charge-resolved channels has total loss beta*Pvac. Both coherent signs at the displayed strength double beta.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'DENSITY_BOUND_RESULTS.json').write_text(text);print(text,end='')
