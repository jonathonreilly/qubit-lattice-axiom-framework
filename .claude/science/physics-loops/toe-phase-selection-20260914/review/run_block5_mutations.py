#!/usr/bin/env python3
"""Challenge a frozen public runner without modifying its source or inputs."""
import gzip
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

PACK=Path(__file__).resolve().parent.parent
OUT=PACK/'review/block5_mutations'
PUBLIC=Path('/Users/jonreilly/Documents/Codex/toe-causal-gaussian-likelihood-20260914/scripts/permanent_local_gaussian_likelihood_protocol_2026_09_14.py')

MUTATIONS=[
    ('axis_only_detour','causal_wire_checks',[
        ('add(before,(1,1,0))','add(before,(2,0,0))'),
        ('add(after,(1,1,0))','add(after,(2,0,0))')]),
    ('shared_terminal_direction','causal_wire_checks',[
        ('compiler.ports={key:2*p for key,p in compiler.ports.items()}','compiler.ports={key:p for key,p in compiler.ports.items()}')]),
    ('reused_edge_planes','causal_wire_checks',[
        ('+e_index*self.colors+self.color_id(n)','+self.color_id(n)')]),
    ('lost_complex_payload','local_rule_window_checks',[
        ('def decode(matrix):\n    z=np.trace(matrix)/2','def decode(matrix):\n    z=np.trace(matrix).real/2')]),
    ('transposed_star_rotation','local_rule_window_checks',[
        ('vector=rotation@components','vector=rotation.T@components')]),
    ('wrong_local_observation','local_rule_window_checks',[
        ('mean=0j if child<4 else values[1]-values[0]','mean=0j if child<4 else values[1]+values[0]')]),
    ('unnormalized_control_atoms','local_rule_window_checks',[
        ('default_weight=s.Rational(1,len(default_atoms))','default_weight=s.Rational(2,len(default_atoms))')]),
    ('real_complex_kl_factor','local_rule_window_checks',[
        ('complex_kl=(mean.dot(mean))/c','complex_kl=(mean.dot(mean))/(2*c)')]),
    ('likelihood_cross_sign','dk_likelihood_checks',[
        ('q.row_join(-b)','q.row_join(b)')]),
    ('arm_dependent_circuit_roster','dk_likelihood_checks',[
        ('if (i,j) in roster:','if linear[i,j]!=0:')]),
    ('wrong_antiperiodic_compression','source_coercivity_checks',[
        ('A[:half,:half]+A[half:,half:]-A[:half,half:]-A[half:,:half]',
         'A[:half,:half]+A[half:,half:]+A[:half,half:]+A[half:,:half]')]),
    ('overstrong_joint_precision_bound','source_coercivity_checks',[
        ('uniform_lower=mass*gamma/(1+mass*gamma)','uniform_lower=1+mass*gamma')]),
]


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    original=PUBLIC.read_text()
    original_sha=sha256(original.encode()).hexdigest()
    rows=[]
    for name,family,replacements in MUTATIONS:
        text=original
        for before,after in replacements:
            count=text.count(before)
            assert count>=1,(name,before)
            text=text.replace(before,after)
        code=OUT/(name+'.py.gz')
        code.write_bytes(gzip.compress(text.encode(),mtime=0))
        driver=("import gzip\nfrom pathlib import Path\n"
                f"ns={{'__name__':'mutation','__file__':{str(PUBLIC)!r}}}\n"
                f"code=gzip.decompress(Path({str(code)!r}).read_bytes()).decode()\n"
                f"exec(compile(code,{str(code)!r},'exec'),ns)\n"
                f"ns[{family!r}]()\n")
        start=time.monotonic()
        run=subprocess.run([sys.executable,'-c',driver],capture_output=True,text=True,timeout=180)
        elapsed=time.monotonic()-start
        detected=run.returncode!=0 and 'AssertionError' in run.stderr
        for kind,data in (('stdout',run.stdout),('stderr',run.stderr)):
            (OUT/f'{name}.{kind}.gz').write_bytes(gzip.compress(data.encode(),mtime=0))
        row=dict(name=name,family=family,detected=detected,exit_code=run.returncode,
                 elapsed_seconds=elapsed,mutated_source_sha256=sha256(text.encode()).hexdigest(),
                 stdout_sha256=sha256(run.stdout.encode()).hexdigest(),stderr_sha256=sha256(run.stderr.encode()).hexdigest(),
                 final_error=run.stderr.strip().splitlines()[-1] if run.stderr else '')
        rows.append(row)
        print(json.dumps(row),flush=True)
    assert sha256(PUBLIC.read_bytes()).hexdigest()==original_sha,'Public source changed during mutation run'
    summary=dict(primary_sha256=original_sha,mutations=rows,all_detected=all(r['detected'] for r in rows),
                 scope='Personal author fault injection; not independent mathematical review or audit')
    (OUT/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    assert summary['all_detected']


if __name__=='__main__':
    main()
