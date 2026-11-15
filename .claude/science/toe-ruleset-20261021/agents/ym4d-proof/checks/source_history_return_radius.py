#!/usr/bin/env python3
"""Exact arithmetic diagnostics for the fixed-relative-source corollary.

Pre-stated criteria: retain both source factors, require a_eff>0, recover the
old external-source bound at rho=0, and pay the revised entropy threshold.
This checks the algebra in H20c-H21a; it does not integrate the sea or prove
coarse holomorphy, the full return, existence, or a physical mass gap.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import time

started = time.perf_counter()
checks = {
    'fixed_relative_radius_positive_and_u_independent': True,
    'stated_radius_leaves_exactly_half_the_decay': True,
    'mixed_source_exponent_identity': True,
    'rho_zero_recovers_original_external_source_bound': True,
    'revised_u_threshold_pays_polynomial_and_constant': True,
    'revised_entropy_threshold_gives_rooted_bound': True,
}
controls = {
    'reusing_original_decay_at_positive_rho_rejected': True,
    'critical_rho_has_no_positive_decay_budget': True,
}
geometry_cases = 0
exponent_cases = 0
examples = []
for N in range(2, 6):
    for L in (3, 5):
        for eps1 in (F(1, 2), F(1, 3)):
            geometry_cases += 1
            D = N*N-1
            nl = 4*L**3*(L-1)
            np = 6*nl
            a = eps1**2/(4*N)
            P = D*(F(nl, 2)+8)
            rho0 = a/(8*np)
            ae = a-4*rho0*np
            checks['fixed_relative_radius_positive_and_u_independent'] &= rho0 > 0
            checks['stated_radius_leaves_exactly_half_the_decay'] &= ae == a/2
            for u in (F(1), F(17, 3), F(10**6)):
                for lam in (F(0), F(2, 7)):
                    exponent_cases += 1
                    direct = -a*u + 4*(u*rho0+lam)*np
                    collected = -ae*u + 4*lam*np
                    checks['mixed_source_exponent_identity'] &= direct == collected
                    checks['rho_zero_recovers_original_external_source_bound'] &= (
                        -a*u+4*(u*0+lam)*np == -a*u+4*lam*np)
                    controls['reusing_original_decay_at_positive_rho_rejected'] &= (
                        direct > -a*u+4*lam*np)
            critical_rho = a/(4*np)
            controls['critical_rho_has_no_positive_decay_budget'] &= (
                a-4*critical_rho*np == 0 and P > 0)
            for B in (F(19, 7), F(-11, 5)):
                threshold = max(F(1), (2*P/ae)**2, 2*max(B, 0)/ae)
                # log u <= sqrt u for u>=1. The first exact inequality pays
                # P sqrt u; the second pays the remaining constant B.
                checks['revised_u_threshold_pays_polynomial_and_constant'] &= (
                    P**2*threshold <= (ae*threshold/2)**2
                    and B-ae*threshold/2 <= 0)
            if N == 2 and L == 3 and eps1 == F(1, 2):
                examples.append({'N':N,'L':L,'epsilon_1':str(eps1),
                                 'n_P':np,'a':str(a),'rho_0':str(rho0),
                                 'a_eff':str(ae),'P_0':str(P)})

s0 = 81
A0 = (5**4-1)**2
rq = F(1, 2*A0+8*s0)
dq = s0*rq/(1-A0*rq)
checks['revised_entropy_threshold_gives_rooted_bound'] &= A0*rq < 1 and dq <= F(1, 4)
assert all(checks.values()), checks
assert all(controls.values()), controls
print(json.dumps({
    'schema':'source-history-author-fixed-radius-v1',
    'scope':'Exact source-cost and sufficient-threshold arithmetic only; full raw sea/history return remains open',
    'checks':checks,'negative_controls':controls,
    'counts':{'checks':len(checks),'negative_controls':len(controls)},
    'geometry_cases':geometry_cases,'exponent_cases':exponent_cases,
    'examples':examples,'rooted_entropy_bound':str(dq),
    'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'elapsed_seconds':time.perf_counter()-started,'all_pass':True,
},indent=2))
