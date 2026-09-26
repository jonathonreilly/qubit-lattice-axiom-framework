#!/usr/bin/env python3
"""Post-seal source authentication and independent arithmetic comparison.

Does not execute the author checker or modify any earlier artifact.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent
EXPECTED = {
    'DIMER_FIXED_ENCODING_QUANTUM_CONTRACTION.md': 'f8b7e30ac671f19c93e5c9456c1f4e892f221eaa7888435e7aec5155126455e7',
    'quantum_metric_exact_check.py': 'be629d6d9ef483bda8b246e19135b1cc5524bffc6075612ea36d0c53532749ce',
    'QUANTUM_METRIC_EXACT_RESULTS.json': '1a319d4d17b3ac9a18ce665e55087ea6aafb84d3baa0869529785e2a01b54da0',
    'QUANTUM_METRIC_AUTHOR_PRECOMPARISON_SEAL.json': 'a472ec115b47d6a923006820dff4f0b2cb1060838a6bf8e3aefe26c083fed4de',
}


def row(path):
    data = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    prepath = HERE/'PRE_COMPARISON_SEAL.json'
    assert row(prepath)['sha256'] == '72116be479051ed6e637d4a3b3c466c5f2016559a0c9cf0ae44e986a2e13d4b8'
    pre = json.loads(prepath.read_text())
    for bound in pre['sources']+pre['artifacts']:
        assert row(Path(bound['path'])) == bound
    source_rows = {}
    for name, digest in EXPECTED.items():
        r = row(AUTHOR/name)
        assert r['sha256'] == digest
        source_rows[r['path']] = r
    author_seal = json.loads((AUTHOR/'QUANTUM_METRIC_AUTHOR_PRECOMPARISON_SEAL.json').read_text())
    for name, digest in author_seal['artifacts_sha256'].items():
        r = row(AUTHOR/name)
        assert r['sha256'] == digest
        source_rows[r['path']] = r
    own = json.loads((HERE/'RESULTS.json').read_text())
    author = json.loads((AUTHOR/'QUANTUM_METRIC_EXACT_RESULTS.json').read_text())
    for path, digest in author['source_sha256'].items():
        r = row(AUTHOR.parent/path)
        assert r['sha256'] == digest
        source_rows[r['path']] = r
    assert author['script_sha256'] == EXPECTED['quantum_metric_exact_check.py']
    assert (AUTHOR/'QUANTUM_METRIC_EXACT_RUN.log').read_bytes() == (AUTHOR/'QUANTUM_METRIC_EXACT_RESULTS.json').read_bytes()
    assert (AUTHOR/'QUANTUM_METRIC_EXACT_RUN.stderr').read_bytes() == b''
    G = s.Matrix([[s.Rational(x) for x in r] for r in own['quantum']['metric']])
    assert s.Rational(author['metric']['u']) == G[0, 0]
    assert s.Rational(author['metric']['v']) == G[1, 1]
    assert s.Rational(author['metric']['cross']) == G[0, 1] == 0
    assert s.Rational(author['metric']['u_minus_4v']) == G[0, 0]-4*G[1, 1]
    checks = []
    for witness in author['witnesses']:
        n, orient = witness['N'], witness['orientation']
        # Independently derived finite triangle sums, frozen in DERIVATION.md.
        A = -64*s.Rational(11, 10)*(n-1)/n**3
        C = orient*s.Rational(8*(n*n-144), n**3)
        cu, cv = 2*A-C/14, 2*A+2*C/7
        value = s.factor(cu*G[0, 0]+cv*G[1, 1])
        assert s.Rational(witness['coefficient_u']) == cu
        assert s.Rational(witness['coefficient_v']) == cv
        assert s.Rational(witness['coefficient_cross']) == 0
        assert s.Rational(witness['chi_squared_derivative_per_pair']) == value
        assert witness['strictly_positive'] == bool(value > 0)
        assert witness['physical_pairs'] == n**3//2
        checks.append({'N': n, 'orientation': orient, 'coefficient_u': str(cu),
                       'coefficient_v': str(cv), 'derivative': str(value), 'positive': bool(value > 0)})
    assert len(checks) == 6
    assert [(r['N'], r['orientation']) for r in checks if r['positive']] == [(2048, 1)]
    # Independent symbolic check of the author's Fourier and contraction remark.
    z = s.symbols('z', nonzero=True)
    skew_laurent = z**4+z**-2-z**2-z**-4
    assert skew_laurent == (z**4-z**-4)-(z**2-z**-2)
    u, v, d, g = s.symbols('u v d g', real=True)
    M = s.diag(u, v)
    B = s.Matrix([[0, 1], [4, 0]])
    T = -d*s.eye(2)-s.I*g*B
    H = s.simplify(M*T+T.conjugate().T*M)
    assert H == s.Matrix([[-2*d*u, -s.I*g*(u-4*v)], [s.I*g*(u-4*v), -2*d*v]])
    assert s.expand(H.det()) == 4*d*d*u*v-g*g*(u-4*v)**2
    # d=O(k^2), g=k/7+O(k^3) at gamma=1. For fixed positive u,v and
    # u!=4v the determinant is negative at all sufficiently small nonzero k.
    result = {
        'independent_preseal_all_rows_unchanged': True,
        'preseal_source_rows': len(pre['sources']), 'preseal_artifact_rows': len(pre['artifacts']),
        'sources': sorted(source_rows.values(), key=lambda r: r['path']),
        'author_logs_authenticated': True,
        'author_start_time_independently_verified': False,
        'author_checker_reexecuted': False,
        'metric_entries_equal_exactly': True,
        'six_triangle_arithmetic_checks': checks,
        'long_wave_Hermitian_determinant': str(s.factor(H.det())),
        'long_wave_condition_scope': 'Fixed gamma=1 and k0, diagonal positive metric, same encoding for arbitrarily large even tori; necessary only.',
        'external_Temme_paper_read_or_imported': False,
        'findings': [],
    }
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
