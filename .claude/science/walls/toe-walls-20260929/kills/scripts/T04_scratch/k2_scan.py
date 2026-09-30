#!/usr/bin/env python3
"""Kill-check T04, k2: scan the attacker's own model (its SW code) over the centre energy Dc
to test 'never to zero' and the quoted 0.2..40 percent range; also the J/eps^4 coefficient
across the two energy models."""
import sys, numpy as np
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T04_scratch')
import ring_flip_identity as R
for model in ('U', 'ice'):
    R.MODEL = model
    print('MODEL', model, ' (Dv=1, U=1); columns: Dc, a1, a2, |JF/JB|, 1-|JF/JB|')
    for Dc in (20, 4, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.001):
        r = R.run_case(1, Dc, 1, tED=1e-4 if Dc >= 0.05 else 1e-5)
        JB, JF = r['J_B'], r['J_F']
        print(f"  Dc={Dc:<7} a1={r['a1']:12.4f} a2={r['a2']:12.4f} |JF/JB|={abs(JF)/abs(JB):.5f}  fermion suppression={(1-abs(JF)/abs(JB))*100:.2f}%   ED check {r['ED_halfsplit_F']/1e-0:.3e}")
# centre-only limit: remove vertex route by Dv -> huge
print('Vertex route removed (Dv=1e6), Dc=1: ')
for model in ('U', 'ice'):
    R.MODEL = model
    r = R.run_case(1e6, 1, 1, tED=1e-4)
    print(' ', model, 'a1', r['a1'], 'a2', r['a2'], 'J_B', r['J_B'], 'J_F', r['J_F'])
# J / eps^4 coefficient, both models, at (1,1,1)
print('J/eps^4 (Delta=1): eps^2 = leak weight per t^2')
for model in ('U', 'ice'):
    R.MODEL = model
    r = R.run_case(1, 1, 1, tED=1e-3)
    e2 = r['leak_B'] / 1e-3 ** 2
    print(' ', model, 'eps2/t2=', e2, ' J_B/eps2^2=', abs(r['J_B']) / e2 ** 2)
