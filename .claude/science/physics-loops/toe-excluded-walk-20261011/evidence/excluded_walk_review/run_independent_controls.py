"""Run the independently designed baseline and actual source-copy discriminators."""
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,time
out=Path(__file__).resolve().parent
source=out/'cook_independent_check.py';text=source.read_text()
changes=[
 ('rank_two_term','V_expected=-h*c.H-c*h.H','V_expected=-h*c.H','rank-two perturbation identity'),
 ('torus_measure','/(2*s.pi)','/(s.pi)','normalized torus spectral-coupling norm'),
 ('projection_normalization','prepared=P2*chi/s.sqrt((chi.H*P2*chi)[0])','prepared=P2*chi','normalized projected-state distance identity'),
 ('cook_sign','predicted=1j*expm','predicted=-1j*expm','Cook comparison derivative sign'),
 ('fourier_normalization','amplitude=constant*fourier_polynomial','amplitude=constant*fourier_polynomial/(2*s.pi)','Fourier-density normalization'),
 ('tail_denominator','claimed=1/((order-1)*T**(order-1))','claimed=1/(T**(order-1))','Cook-tail integrated power and denominator'),
 ('scattering_adjoint','claimed_change=(phase-1)*w*v.H+(s.conjugate(phase)-1)*v*w.H','claimed_change=(s.conjugate(phase)-1)*w*v.H+(phase-1)*v*w.H','rank-one scattering-current identity with adjoints'),
 ('unchanged_K_law','reported_new=[(old_probs[j]-losses[j])/(1-loss) for j in range(2)]','reported_new=old_probs','global projection reweights total-momentum fibers'),
]
executions=[]
def run(path,name,expected=None):
    log=out/(name+'.log');start=time.monotonic()
    with log.open('w') as f:p=subprocess.run([sys.executable,str(path)],stdout=f,stderr=subprocess.STDOUT,timeout=90)
    output=log.read_text()
    okay=p.returncode==0 if expected is None else p.returncode==1 and 'AssertionError:' in output and expected in output
    row={'name':name,'source':path.name,'sha256':sha256(path.read_bytes()).hexdigest(),'command':[sys.executable,str(path)],'exit_code':p.returncode,'intended_result':okay,'expected_assertion':expected,'seconds':time.monotonic()-start,'log':log.name}
    executions.append(row);print(json.dumps(row),flush=True)
    assert okay,row
run(source,'baseline')
for name,before,after,expected in changes:
    assert text.count(before)==1,(name,text.count(before))
    mutant=out/('mutant_'+name+'.py');mutant.write_text(text.replace(before,after,1));run(mutant,name,expected)
(out/'control_manifest.json').write_text(json.dumps({'baseline_sha256':sha256(source.read_bytes()).hexdigest(),'mutations':[{'name':n,'before':b,'after':a,'expected':e} for n,b,a,e in changes],'executions':executions},indent=2)+'\n')
print('Independent baseline and',len(changes),'actual source mutants completed.')
