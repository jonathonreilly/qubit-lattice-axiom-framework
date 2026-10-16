"""Scratch-only mutation validation of the frozen canonical runner."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[2]
HELPER = ROOT / 'scripts/ringdown_action_math.py'
SOURCE = HELPER.read_text()
MUTATIONS = [
 ('held_force_variation_sign','dt(sy.diff(T,xd))-sy.diff(T-V,x)','dt(sy.diff(T,xd))+sy.diff(T-V,x)'),
 ('linear_response_residue_sign','Z=pol-Ns**2/','Z=pol+Ns**2/'),
 ('ringdown_inertia_sign','(cp-tp*O)*cc*cb','(cp+tp*O)*cc*cb'),
 ('numeric_inertia_gradient','+n0*vv-tp0*vv**2/2','+n0*vv+tp0*vv**2/2'),
 ('extractor_residue_factor','np.polyval(coeff[2:],pole)/(2*pole+Gamma)','np.polyval(coeff[2:],pole)/(pole+Gamma)'),
 ('fundamental_coefficient_factor','f=(rc[1]-1j*rc[2])/2','f=(rc[1]-1j*rc[2])'),
 ('quadratic_rejection_witness','epsilon=.08','epsilon=0'),
 ('cubic_closure_witness','cubic=.8','cubic=0'),
 ('zero_decay_basis','np.exp(0*zero_decay_times)','np.exp(-.3*zero_decay_times)'),
 ('quotient_error_radius','budget=eN/','budget=0*eN/'),
 ('residue_error_radius','ekbound=(2*abs(la)+abs(ga0))*er+abs(rh)*(2*el+eg)+(2*el+eg)*er','ekbound=0.'),
 ('midpoint_certificate','Lq*sum(widths**2)/4','0*Lq*sum(widths**2)/4'),
 ('hidden_chart_sign','.subs(Fp,-k/tau)','.subs(Fp,k/tau)'),
 ('fixed_hidden_curvature_sign','s.diff(E,x,2)+Gcan**2/cc','s.diff(E,x,2)-Gcan**2/cc'),
 ('complex_harmonic_sign',"fit['S']=-2*(2*la+ga)","fit['S']=2*(2*la+ga)"),
 ('relative_inertia_integration','np.exp(cumulative_simpson(rr.real,x=grid,initial=0))','np.exp(-cumulative_simpson(rr.real,x=grid,initial=0))'),
 ('root_continuity','last=n\n        nu_i=', 'n=n*(-1 if i%2 else 1)\n        last=n\n        nu_i='),
 ('response_polynomial','corrected=zv+(G_i+nu_i*sv)**2/','corrected=zv-(G_i+nu_i*sv)**2/'),
 ('static_force_curve',"static_res=arr('P0')-arr('G')**2", "static_res=arr('P0')+arr('G')**2"),
 ('equilibrium_integration',"cumulative_simpson(-arr('G')/arr('C')", "cumulative_simpson(arr('G')/arr('C')"),
 ('later_history_prediction','Cprime*z*z/2-tprime*zd*zd/2','Cprime*z*z/2+tprime*zd*zd/2'),
 ('force_covector_chain','s.diff(force_curve/s.diff(jj,xx),xx)','s.diff(force_curve*s.diff(jj,xx),xx)'),
 ('complex_S_error_budget','eS=eN/(Dmin-eD)+2*abs(a)*abs(rh)*abs(g0)*eD/(Dmin*(Dmin-eD))','eS=0.'),
 ('complex_r_error_budget','bound=(eS+eQ)/(abs(L0)-eL)+abs(S0-Q0)*eL/(abs(L0)*(abs(L0)-eL))','bound=0.'),
]


def run_case(case):
    name, old, new = case
    assert old in SOURCE, (name, 'missing mutation target')
    with tempfile.TemporaryDirectory(prefix='ringdown-mutation-') as tmp:
        dest = Path(tmp)
        for path in ['scripts/ringdown_action_inverse.py', 'docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md']:
            (dest/path).parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/path,dest/path)
        altered=SOURCE.replace(old,new)
        (dest/'scripts/ringdown_action_math.py').write_text(altered)
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        r=subprocess.run([sys.executable,'-B','scripts/ringdown_action_inverse.py'],cwd=dest,env=env,text=True,capture_output=True,timeout=120)
        failures=[line for line in r.stdout.splitlines() if line.startswith('FAIL:')]
        return {'name':name,'old':old,'new':new,'occurrences':SOURCE.count(old),'mutant_sha256':hashlib.sha256(altered.encode()).hexdigest(),'exit_code':r.returncode,'failed_checks':failures,'stderr':r.stderr,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'detected':r.returncode!=0 and len(failures)>0}


if __name__ == '__main__':
    before=hashlib.sha256(HELPER.read_bytes()).hexdigest()
    with ThreadPoolExecutor(max_workers=2) as pool:
        results=list(pool.map(run_case,MUTATIONS))
    unchanged=before==hashlib.sha256(HELPER.read_bytes()).hexdigest()
    report={'source_sha256':before,'canonical_source_unchanged':unchanged,'mutations':results,'summary':{'detected':sum(r['detected'] for r in results),'undetected':sum(not r['detected'] for r in results)}}
    (ROOT/'outputs/ringdown_action_inverse/mutations.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'summary':report['summary'],'source_unchanged':unchanged,'undetected':[r for r in results if not r['detected']]},indent=2))
    raise SystemExit(0 if unchanged and all(r['detected'] for r in results) else 1)
