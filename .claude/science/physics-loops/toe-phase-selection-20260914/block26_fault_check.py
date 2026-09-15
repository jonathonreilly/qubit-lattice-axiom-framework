#!/usr/bin/env python3
"""Targeted author fault injections; no independent-review claim."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, tempfile
PACK=Path(__file__).resolve().parent
SOURCE=PACK/'block26_spectral_check.py'
FAULTS=[
 ('positive_probe_coefficient','F(1,4)-F(4,3)*x/(x+1)+F(25,12)*x/(x+4)','F(1,4)-F(1,3)*x/(x+1)+F(25,12)*x/(x+4)','check_positive_probe'),
 ('physical_score_sign','score=-derivative/(mp.sqrt(beta)*weight)','score=derivative/(mp.sqrt(beta)*weight)','check_physical_score_contact'),
 ('physical_score_normalization','score=-derivative/(mp.sqrt(beta)*weight)','score=-derivative/(beta*weight)','check_physical_score_contact'),
 ('physical_contact_removed','predicted=1-vbar-Cn/beta','predicted=1-Cn/beta','check_physical_score_contact'),
 ('time_zero_displaced','np.linalg.matrix_power(T,t)@obs','np.linalg.matrix_power(T,t+1)@obs','check_finite_markov_transfer'),
 ('poisson_numerator','(1-lam*lam)/(1-2*lam*np.cos(omega)+lam*lam)','(1-lam)/(1-2*lam*np.cos(omega)+lam*lam)','check_finite_markov_transfer'),
 ('susceptibility_reciprocal','return (1+lam)/(1-lam)','return (1-lam)/(1+lam)','check_finite_markov_transfer'),
 ('midpoint_phase','np.exp(-.5j*(k[i]+k[j]))','np.exp(.5j*(k[i]+k[j]))','check_midpoint_magnetic_symbol'),
 ('magnetic_orientation','BB[1,pairs.index((1,3))]=-1','BB[1,pairs.index((1,3))]=1','check_midpoint_magnetic_symbol'),
 ('matrix_probe_coefficient','return total/4-(4/3)*Sa+(25/12)*S4a','return total/4-(4/3)*Sa+(25/6)*S4a','check_matrix_band_projection'),
 ('energy_half','return 2*np.arcsinh(np.sqrt(u)/2)','return np.arcsinh(np.sqrt(u)/2)','check_parameter_certificate'),
 ('ordinary_weight_reciprocal','nu_atoms=[np.tanh(E/2)*W','nu_atoms=[W/np.tanh(E/2)','check_matrix_band_projection'),
 ('band_complement','np.diag((EE>=lower_E)&(EE<=upper_E))','np.diag((EE<lower_E)|(EE>upper_E))','check_matrix_band_projection'),
 ('contact_atom_deleted','nu_contact=chi_contact','nu_contact=0','check_contacts_and_invariant_atoms'),
 ('continuous_density_normalization','return 1-z/(2*a*width)*mp.log','return 1-z/(a*width)*mp.log','check_continuous_spectrum_and_nongaussianity'),
 ('loose_error_percentage','eps=F(1,10000000)','eps=F(1,1000)','check_parameter_certificate'),
]


def main():
 body=SOURCE.read_text();rows=[]
 with tempfile.TemporaryDirectory(prefix='toe-block26-fault-') as tmp:
  for name,old,new,fn in FAULTS:
   assert body.count(old)==1,(name,body.count(old))
   candidate=body.replace(old,new,1);p=Path(tmp)/(name+'.py');p.write_text(candidate)
   command='import runpy; r=runpy.run_path('+repr(str(p))+'); r['+repr(fn)+']()'
   r=subprocess.run([sys.executable,'-c',command],text=True,capture_output=True,timeout=60)
   row={'name':name,'family':fn,'original':old,'replacement':new,'source_sha256':hashlib.sha256(candidate.encode()).hexdigest(),
        'exit_code':r.returncode,'stderr':r.stderr,'stdout':r.stdout,'caught':r.returncode!=0 and 'AssertionError' in r.stderr}
   rows.append(row);print(json.dumps({'fault':name,'caught':row['caught'],'stderr_end':r.stderr.splitlines()[-1:]}),flush=True)
 receipt={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':SOURCE.name,
          'source_sha256':hashlib.sha256(body.encode()).hexdigest(),'faults':rows,'all_caught':all(r['caught'] for r in rows)}
 (PACK/'BLOCK26_FAULT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
 assert receipt['all_caught']


if __name__=='__main__':main()
