"""Root comparison with an older independent path implementation.

The implementation predates this energy claim. This script is author-written
and is not a fresh independent reconstruction of the claim.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/finite_spin_path_comparison.py', 'scripts/cube_high_flux_birth.py', 'scripts/mobile_compensation_model_20260924.py')
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE
SOURCES = {
    'mobile_compensation_model_20260924.py': 'eb53d8e60b7bbef8ccfb460fc64b25cab007edb87cd7af45151d76f52c95c23a',
    'cube_high_flux_birth.py': 'd3f0a282d6a8ad0024c0794bd507fa3e25a3a500b420f7d77b39cc84eeb8cfab',
}
modules = []
for i, (path, expected) in enumerate(SOURCES.items()):
    p = BASE / path
    assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location('energy_comparison_' + str(i), p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    modules.append(mod)
model, root = modules


def case(S, n):
    q, E = root.initial(n)
    state = tuple(q), tuple(E)
    C = S * (S + 1)
    u = Fraction(n*n, C)
    expected_rate = 48 - 32*u + 8*u*u
    expected_D = 96*n*n - Fraction(32*n**4 + 16*n*n, C)
    expected_E2_drift = 16*(6-8*u+3*u*u)
    instruments = {}
    for coherent in (False, True):
        total = post_d = post_e2 = 0.
        paths = 0
        for edge in range(12):
            for sign in (None,) if coherent else (-1, 1):
                vec = model.effective_birth(state, edge, sign, model.CUBE_A,
                                            model.CUBE_EDGES, S)
                for (qq, ff), amp in vec.items():
                    assert model.gauss(qq, ff, model.CUBE_A, model.CUBE_EDGES)
                    assert max(abs(e) for e in ff) <= S
                    p = abs(amp)**2
                    total += p
                    post_d += p * root.electric(qq, ff)
                    post_e2 += p * sum(e*e for e in ff)
                    paths += 1
        assert math.isclose(total, float(expected_rate), rel_tol=1e-12, abs_tol=1e-11)
        assert math.isclose(post_d, float(expected_D), rel_tol=1e-12, abs_tol=1e-10)
        got_e2_drift = post_e2 - 4*n*n*total
        assert math.isclose(got_e2_drift, float(expected_E2_drift), rel_tol=1e-8, abs_tol=1e-7)
        instruments['coherent' if coherent else 'resolved'] = {
            'nonzero_paths': paths, 'rate':total, 'post_D_weighted':post_d,
            'E2_drift_over_kappa':got_e2_drift}
    selected = model.effective_birth(state, 0, 1, model.CUBE_A, model.CUBE_EDGES, S)
    a = Fraction(C-n*(n+1), C)
    expected_selected = a*(1+a)
    norm = sum(abs(amp)**2 for amp in selected.values())
    assert math.isclose(norm, float(expected_selected), rel_tol=1e-12, abs_tol=1e-12)
    if norm:
        mean = sum(abs(amp)**2*root.electric(*s) for s,amp in selected.items())/norm
        second = sum(abs(amp)**2*root.electric(*s)**2 for s,amp in selected.items())/norm
        variance = second-mean*mean
        expected_mean = 2*n*n/(1+a)
        expected_var = 4*n**4*a/(1+a)**2
        assert math.isclose(mean,float(expected_mean),rel_tol=1e-12,abs_tol=1e-10)
        assert math.isclose(variance,float(expected_var),rel_tol=1e-11,abs_tol=1e-8)
    else:
        assert n == S
    return {'S':S,'n':n,'exact_rate':str(expected_rate),
            'exact_post_D_weighted':str(expected_D),
            'exact_E2_drift_over_kappa':str(expected_E2_drift),
            'selected_norm_squared':norm,'instruments':instruments}


rows = [case(S,n) for S in (1,2,4,8,16,32,64,128)
        for n in sorted(set((-S,-S//2,0,S//3,S//2,3*S//4,S-1,S)))]
print(json.dumps({'source_bindings':SOURCES,'scope':'root comparison, not independent review',
                  'cases':len(rows),'rows':rows},indent=2))
