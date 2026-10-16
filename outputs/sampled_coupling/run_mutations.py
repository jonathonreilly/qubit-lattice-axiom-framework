"""Bounded scratch mutations of the integrated primary and its helper."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PRIMARY = 'scripts/sampled_coupling_inverse.py'
HELPER = 'scripts/sampled_coupling_math.py'
NOTE = 'docs/SAMPLED_COUPLING_RECONSTRUCTION_NOTE_2026-10-16.md'

MUTATIONS = [
    ('affine_characteristic', PRIMARY, '(z-1)*(z*z-s*z+p)', '(z+1)*(z*z-s*z+p)'),
    ('difference_recurrence', PRIMARY, 'F3 = (1+s)*F2-(s+p)*F1+p*F0', 'F3 = (1+s)*F2-(s+p)*F1-p*F0'),
    ('cramer_sign', PRIMARY, '(d1*d3-d2*d2)/H-p', '(d1*d3+d2*d2)/H-p'),
    ('energy_dissipation', PRIMARY, '-gamma*sp.diff(Z,t)-om2*Z', 'gamma*sp.diff(Z,t)-om2*Z'),
    ('calibration_matrix', HELPER, '[d[2], -d[1]]', '[d[2], d[1]]'),
    ('baseline_weight', HELPER, '[-p, s+p, -(1+s)', '[p, s+p, -(1+s)'),
    ('backward_weight', HELPER, '(s+p)/p, -(1+s)/p, 1/p', '(s+p), -(1+s), 1'),
    ('pulse_duration', PRIMARY, 'end = advance(before[-1],DELTA,y,om2,gamma)', 'end = advance(before[-1],2*DELTA,y,om2,gamma)'),
    ('green_normalization', PRIMARY, 'return expm(np.array([[0.,1.],[-om2,-gamma]])*t)[0,1]', 'return 2*expm(np.array([[0.,1.],[-om2,-gamma]])*t)[0,1]'),
    ('surface_centering', HELPER, 'E = D-D[:, [0]]', 'E = D+D[:, [0]]'),
    ('surface_anchor', HELPER, 'E[:, -1]/anchor, E[0, :]/anchor', 'E[:, -1], E[0, :]'),
    ('p_sensitivity', HELPER, 'f4-(1+s)*f3+s*f2', 'f4-(1+s)*f3'),
    ('coefficient_bound', HELPER, '(2+2*S)/p_min**2', '(2+S)/p_min**2'),
    ('calibration_bound', HELPER, 'norm/(1-eta)*(2*epsilon_force+4*epsilon_force*np.linalg.norm(theta_hat, np.inf))', '.5*norm/(1-eta)*(2*epsilon_force+4*epsilon_force*np.linalg.norm(theta_hat, np.inf))'),
    ('ratio_margin', HELPER, '/(abs(anchor)-epsilon_anchor)', '/(abs(anchor)+epsilon_anchor)'),
    ('shape_error_terms', HELPER, 'epsilon_B_x+epsilon_B_y+abs(kappa_hat)', 'abs(kappa_hat)'),
    ('potential_cross_force', PRIMARY, 'V=U+lam*C*w*w/2+lam*b*w', 'V=U+lam*C*w*w/2-lam*b*w'),
    ('interaction_sign', PRIMARY, 'anchor=-J*ar*d/tau', 'anchor=J*ar*d/tau'),
    ('nonpolynomial_shape', PRIMARY, 'k=2/(np.e-1)', 'k=1/(np.e-1)'),
    ('second_mode_control', PRIMARY, 'mixture=cal+.15*np.exp', 'mixture=cal+0*np.exp'),
    ('zero_anchor_guard', HELPER, 'if anchor == 0:', 'if False:'),
]


def main():
    bindings={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in [PRIMARY,HELPER,NOTE]}
    rows=[]
    for name,target,old,new in MUTATIONS:
        with tempfile.TemporaryDirectory(prefix='coupling-mutation-') as tmp:
            base=Path(tmp)
            for n in [PRIMARY,HELPER,NOTE]:
                (base/n).parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(ROOT/n,base/n)
            text=(base/target).read_text()
            if text.count(old)!=1:
                raise RuntimeError(f'mutation anchor count for {name}: {text.count(old)}')
            (base/target).write_text(text.replace(old,new,1))
            cmd=['/usr/local/bin/python3','-B',PRIMARY]
            started=time.monotonic()
            r=subprocess.run(cmd,cwd=base,capture_output=True,text=True,timeout=120,
                             env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
            (OUT/(name+'.stdout')).write_text(r.stdout)
            (OUT/(name+'.stderr')).write_text(r.stderr)
            failed=[]
            if r.stdout:
                data=json.loads(r.stdout)
                failed=[c['name'] for c in data['checks'] if not c['passed']]
            rows.append(dict(name=name,target=target,old=old,new=new,
                             returncode=r.returncode,detected=r.returncode!=0,
                             failed_checks=failed,elapsed_seconds=time.monotonic()-started,
                             timeout_seconds=120))
    unchanged=all(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==v for n,v in bindings.items())
    result=dict(source_hashes=bindings,unchanged=unchanged,mutations=rows,
                detected=sum(x['detected'] for x in rows),total=len(rows))
    (OUT/'mutation_controls_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(detected=result['detected'],total=len(rows),unchanged=unchanged,
                         missed=[r['name'] for r in rows if not r['detected']]),indent=2))
    return int(not unchanged or result['detected']!=len(rows))


if __name__=='__main__':
    raise SystemExit(main())
