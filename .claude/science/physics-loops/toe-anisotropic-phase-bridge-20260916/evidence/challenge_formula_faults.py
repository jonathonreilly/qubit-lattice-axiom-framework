#!/usr/bin/env python3
"""Personal formula-fault challenges, not an audit verdict or phase test.

Each selected formula is changed in a preserved scratch source; its check
family executes in a fresh subprocess. A syntax/import error is not a kill.
The original source path is retained as __file__ so the phase checker can
read its explicitly pinned sibling. No external scientific data are read.
"""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
from hashlib import sha256
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
# name, source prefix, selected function, exact original, exact fault
FAULTS = [
 ('conditional_missing_half', 'block01_', 'weighted_curl',
  'expected=np.exp(-rho*rho/(2*a)+1j*rho*u)',
  'expected=np.exp(-rho*rho/a+1j*rho*u)'),
 ('anisotropic_wrong_dual_type', 'block01_', 'weighted_curl',
  '1/bs if a==0 else 1/bt', '1/bt if a==0 else 1/bs'),
 ('poisson_wrong_rate', 'block01_', 'integer_blocking',
  'reference=ive(abs(labels),T/g**2)', 'reference=ive(abs(labels),2*T/g**2)'),
 ('transfer_missing_endpoints', 'block02_', 'transfer_checks',
  'v=sqrtB[:,zero]', 'v=np.eye(N)[:,zero]'),
 ('sum_rule_missing_half', 'block02_', 'response_checks',
  'comm=float(np.dot(s*s,cosmeans)/(2*g*g))',
  'comm=float(np.dot(s*s,cosmeans)/(g*g))'),
 ('offset_wrong_response_sign', 'block02_', 'response_checks',
  'target=g*g*norm2-g**4*chi', 'target=g*g*norm2+g**4*chi'),
 ('tail_wrong_factorial_power', 'block02_', 'factorial_tail_check',
  '-2*mp.loggamma(n+1)', '-mp.loggamma(n+1)'),
 ('phase_wrong_harmonic_mean', 'block03_', 'one_plaquette',
  'harmonic.append(1/np.mean(1/p))', 'harmonic.append(np.mean(p))'),
 ('character_missing_pair_factor', 'block03_', 'one_plaquette',
  '2*k*l*(overlap(k+l)+overlap(k-l))',
  'k*l*(overlap(k+l)+overlap(k-l))'),
 ('cube_linearizes_cosine', 'block03_', 'cube_check',
  'grad=C.T@(z*np.cos(F))', 'grad=C.T@z'),
 ('kernel_drops_lower_weight', 'block04_', 'heat_comparison',
  'lower=math.exp(-4*t/(g*g))*base', 'lower=base'),
 ('haar_wrong_pair_normalization', 'block04_', 'local_geometry_and_orthogonality',
  'cosine_gram[p,q]=(int(plus)+int(minus))/2',
  'cosine_gram[p,q]=(int(plus)+int(minus))'),
 ('principal_charge_uses_raw_curl', 'block04_', 'principal_cube_event',
  'principal=(raw+math.pi)%(2*math.pi)-math.pi', 'principal=raw'),
 ('quantum_derivative_missing_two', 'block05_', 'connected_check',
  'deriv = 2 * excit.T @ (excit / gaps[:, None])',
  'deriv = excit.T @ (excit / gaps[:, None])'),
 ('quantum_electric_wrong_sign', 'block05_', 'connected_check',
  'e_deriv = 2 * cross @ (excit / gaps[:, None])',
  'e_deriv = -2 * cross @ (excit / gaps[:, None])'),
 ('cover_trace_drops_parity', 'block05_', 'covering_trace_check',
  'physical = float(weights[((m-k) % 2) == 0].sum())',
  'physical = float(weights.sum())'),
 ('raw_curl_replaced_by_principal', 'block06_', 'main',
  'raw_curl = {x: curl(theta, x) for x in faces}',
  'raw_curl = {x: (curl(theta, x)+1)%2-1 for x in faces}'),
 ('radial_killing_missing_half', 'block07_', 'heat_checks',
  '- nu * nu / (2 * r * r)', '- nu * nu / (r * r)'),
 ('mixture_inverted_partition_tilt', 'block07_', 'mixture_checks',
  'posterior = prior * partitions / (prior @ partitions)',
  'posterior = (prior / partitions) / np.sum(prior / partitions)'),
 ('circle_wrong_convolution_power', 'block07_', 'convolution_checks',
  'analytic = (ive(abs(frequency), beta) / i0e(beta)) ** steps',
  'analytic = (ive(abs(frequency), beta) / i0e(beta)) ** (steps/2)'),
 ('cusp_wrong_laplace_order', 'block07_', 'cusp_checks',
  'mp.besseli(mp.sqrt(2 * lam), a)', 'mp.besseli(mp.sqrt(lam), a)'),
 ('bridge_wrong_covariance_sign', 'block08_', 'actual_cosine_checks',
  'hessian = direct_hessian - covariance / (self.g * self.g)',
  'hessian = direct_hessian + covariance / (self.g * self.g)'),
 ('bridge_wrong_kinetic_metric', 'block08_', 'time_limit_check',
  'h = np.diag(2 * g * g * n * n + 1 / (g * g))',
  'h = np.diag(g * g * n * n + 1 / (g * g))'),
]


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    start = time.monotonic()
    root = HERE / 'formula_faults'
    root.mkdir(exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
    rows = []
    driver = ("from pathlib import Path; import sys; "
              "p=Path(sys.argv[1]); original=Path(sys.argv[2]); "
              "scope={'__name__':'formula_challenge','__file__':str(original)}; "
              "exec(compile(p.read_text(),str(p),'exec'),scope); scope[sys.argv[3]]()")
    for name, prefix, function, old, new in FAULTS:
        candidates = [p for p in HERE.glob(prefix+'*.py') if '.' not in p.stem
                      and 'diagnostic' not in p.stem]
        assert len(candidates) == 1, (prefix, candidates)
        original = candidates[0]
        code = original.read_text()
        assert code.count(old) == 1, (name, code.count(old))
        changed = code.replace(old, new)
        compile(changed, name, 'exec')
        fault = root / (name+'.py')
        fault.write_text(changed)
        completed = subprocess.run([sys.executable, '-c', driver, str(fault),
                                    str(original), function], env=env,
                                   capture_output=True, text=True, timeout=180)
        stdout = root / (name+'.stdout.txt')
        stderr = root / (name+'.stderr.txt')
        stdout.write_text(completed.stdout)
        stderr.write_text(completed.stderr)
        assertion_rejected = completed.returncode != 0 and 'AssertionError' in completed.stderr
        row = dict(fault=name, source=original.name, function=function,
                   original_sha256=digest(original), mutated_sha256=digest(fault),
                   exit_code=completed.returncode, assertion_rejected=assertion_rejected,
                   source_path=str(fault.relative_to(HERE)),
                   stdout_sha256=digest(stdout), stderr_sha256=digest(stderr))
        rows.append(row)
    report = dict(harness_sha256=digest(Path(__file__)), formula_faults=rows,
                  seconds=time.monotonic()-start,
                  scope='formula-fault checks on finite implementations; no phase or independent audit')
    print(json.dumps(report, indent=2))
    assert all(r['assertion_rejected'] for r in rows), 'a formula fault survived or failed for another reason'


if __name__ == '__main__':
    main()
