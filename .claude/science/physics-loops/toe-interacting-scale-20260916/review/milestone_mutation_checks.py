#!/usr/bin/env python3
"""Run declared consequential mutations on temporary copies of author checks.

Nonzero mutated-run exits are retained explicitly, with their assertion
tracebacks. This script does not turn them into successful scientific runs.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


AUDIT_TIMEOUT_SEC=120
PACK=Path(__file__).resolve().parents[1]
EVIDENCE=PACK/'evidence'
STEMS=[
    'block01_uniform_response_check',
    'block02_integer_gaussian_square_check',
    'block02_tree_slater_check',
    'block03_characteristic_check',
    'block04_weyl_zero_mode_check',
    'block05_generator_propagation_check',
    'block06_rooted_matter_check',
]
AUDIT_INPUT_PATHS=[
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block01_uniform_response_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block02_integer_gaussian_square_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block02_tree_slater_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block03_characteristic_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block04_weyl_zero_mode_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block05_generator_propagation_check.py',
    '.claude/science/physics-loops/toe-interacting-scale-20260916/evidence/block06_rooted_matter_check.py',
]
# Scientific inputs are the seven package-local check programs. The self-hash
# and input hashes below are integrity reads; no external scientific data.


def case(stem,name,old,new,assertion):
    return dict(stem=stem,name=name,old=old,new=new,expected_assertion=assertion)


CASES=[
    case(STEMS[0],'Poisson derivative sign','moment_poisson = 1 / t - math.pi**2','moment_poisson = 1 / t + math.pi**2','Poisson derivative sign'),
    case(STEMS[0],'Fock nuclear norm versus operator norm','nuclear = np.linalg.svd(T, compute_uv=False).sum()','nuclear = np.linalg.norm(T, 2)','Wilson nuclear norm'),
    case(STEMS[0],'wavepacket normalization','math.sqrt(8/(3*R))','math.sqrt(7/(3*R))','literal compact wavepacket geometry'),
    case(STEMS[0],'plane-wave curl orientation','v[3*n] = -math.sqrt(2/V)','v[3*n] = math.sqrt(2/V)','plane-wave curl phase'),
    case(STEMS[0],'compact cosine-translation term','e_x*(s*s*gamma_z+difference_z)+e_z*difference_x','e_x*(s*s*gamma_z-difference_z)+e_z*difference_x','compact magnetic translation identity'),
    case(STEMS[0],'spectral moment normalization','mF = float((np.trace(rho@comm(F, comm(H, F)))/2).real)','mF = float((np.trace(rho@comm(F, comm(H, F)))).real)','spectral first moments'),
    case(STEMS[1],'integer boundary orientation','B[link[(step(x, j), i)], n] -= 1','B[link[(step(x, j), i)], n] += 1','boundary squared'),
    case(STEMS[1],'weighted optimized metric','A = omega/np.sqrt(e)[:, None]/np.sqrt(e)[None, :]','A = omega*np.sqrt(e)[:, None]*np.sqrt(e)[None, :]','weighted optimized metric'),
    case(STEMS[1],'positive-square divergence sign','rhs += sum(omega_p[p, p]*cosines[p]/2 for p in range(2))','rhs -= sum(omega_p[p, p]*cosines[p]/2 for p in range(2))','positive-square identity on padded Fourier core'),
    case(STEMS[1],'dual overlap exponent','math.exp(-g*g*metric[p, p]/4)','math.exp(-g*g*metric[p, p]/2)','exact parity-inserted dual overlap'),
    case(STEMS[2],'tree strip orientation','filling[face[((x[0], y, 0), 0, 1)]] -= 1','filling[face[((x[0], y, 0), 0, 1)]] += 1','literal strip fills fundamental loop'),
    case(STEMS[2],'charged dressing sign','-paths[:, a]+paths[:, b]','paths[:, a]-paths[:, b]','exact integer charged Gauss sector'),
    case(STEMS[2],'paired charge variance factor','variance_formula = 2*subtree_probabilities','variance_formula = 3*subtree_probabilities','paired tree-charge variance'),
    case(STEMS[2],'many-fermion determinant curvature','exact_variance = float(2*np.trace','exact_variance = float(3*np.trace','determinant fidelity curvature convergence'),
    case(STEMS[3],'perpendicular commutator sign','-1j*(S@u)*v_perp','+1j*(S@u)*v_perp','directional derivative converges to weighted commutator'),
    case(STEMS[3],'Fourier covariance normalization','hat.conj(), blocks, hat).real/L','hat.conj(), blocks, hat).real','position/Fourier covariance normalization'),
    case(STEMS[3],'annihilator complex smear','B = (u+1j*v)*Q','B = (u-1j*v)*Q','single rotor commutator including finite shift boundary'),
    case(STEMS[3],'Duhamel boundary coefficient','boundary = 0.5j*','boundary = 1j*','direct derivative versus Duhamel/annihilator decomposition'),
    case(STEMS[4],'Weyl symplectic phase','right = np.exp(0.5j*sigma)','right = np.exp(-0.5j*sigma)','Weyl ground-vector bound'),
    case(STEMS[4],'zero-mode half filling','first[j, 0, 0], second[j, 1, 1] = 1, 1','first[j, 0, 0], second[j, 1, 1] = .5, 1','half filling first zero-mode choice'),
    case(STEMS[4],'nonprojection higher-moment discriminator','independent = np.eye(4)/4','independent = correlated.copy()','higher correlations differ without the projection premise'),
    case(STEMS[5],'matter current sign','currents.append(-(derivative_half+derivative_half.getH()))','currents.append(derivative_half+derivative_half.getH())','exact charged electric equation'),
    case(STEMS[5],'generator annihilator residual sign','decomposition = -Q_omega@psi-1j*g*current@psi','decomposition = Q_omega@psi-1j*g*current@psi','ground-vector norm residual decomposition'),
    case(STEMS[5],'square-root null projection','A+math.sqrt(p)*Pi','A+math.sqrt(p)*np.eye(3)','rank-two square-root formula'),
    case(STEMS[5],'remove toy hidden-mode coupling','c,t=.6,1.','c,t=0.,1.','fixed first moment does not fix propagation'),
    case(STEMS[6],'root electric quadratic path term','coefficient=g*g*(E@(e*delta_E))+.5*g*g*np.sum(e*delta_E**2)','coefficient=g*g*(E@(e*delta_E))','rooted electric commutator including quadratic path term'),
    case(STEMS[6],'closing-link charged orientation','flux_shift=inn if l!=3 else (shift if charge==1 else shift.getH())','flux_shift=inn if l!=3 else (shift.getH() if charge==1 else shift)','actual closing hop equals rooted free hop plus compact loop'),
    case(STEMS[6],'free matter time direction','free_unitary=expm(-1j*t*H0dense)','free_unitary=expm(1j*t*H0dense)','free-time sign discriminator'),
]


def main():
    sources={stem:(EVIDENCE/f'{stem}.py').read_text() for stem in STEMS}
    records=[]
    env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1'
    with tempfile.TemporaryDirectory(prefix='toe-mutation-20260916-') as temporary:
        root=Path(temporary)
        for number,item in enumerate(CASES,1):
            directory=root/f'{number:02d}'
            directory.mkdir()
            for stem,source in sources.items():
                (directory/f'{stem}.py').write_text(source)
            source=sources[item['stem']]
            matches=source.count(item['old'])
            # The weighted metric line appears in both periodic and ladder
            # fixtures. Mutate its first, periodic occurrence deliberately.
            expected_matches=2 if item['name']=='weighted optimized metric' else 1
            if matches!=expected_matches:
                raise AssertionError(f"Mutation anchor count {item['name']}: {matches}")
            mutated=source.replace(item['old'],item['new'],1)
            path=directory/f"{item['stem']}.py"
            path.write_text(mutated)
            result=subprocess.run([sys.executable,str(path)],cwd=directory,env=env,
                                  text=True,capture_output=True,timeout=120)
            rejected=(result.returncode!=0 and
                      f"AssertionError: {item['expected_assertion']}" in result.stderr)
            row=dict(item,observed_returncode=result.returncode,
                     expected_assertion_observed=rejected,
                     stdout=result.stdout,stderr=result.stderr,
                     original_sha256=hashlib.sha256(source.encode()).hexdigest(),
                     mutated_sha256=hashlib.sha256(mutated.encode()).hexdigest())
            records.append(row)
            if not rejected:
                print(json.dumps(row,indent=2),flush=True)
                raise AssertionError(f"Mutation did not fail at its intended mathematical assertion: {item['name']}")
    output={'scope':'Expected failures of temporary mutated check programs; no scientific status conferred.',
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_hashes':{s:hashlib.sha256(t.encode()).hexdigest() for s,t in sources.items()},
            'mutations':records}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print(f"{len(records)} declared mutations returned nonzero at their intended mathematical assertions.")
    print(f"TOTAL: PASS={len(records)} FAIL=0")


if __name__=='__main__':
    main()
