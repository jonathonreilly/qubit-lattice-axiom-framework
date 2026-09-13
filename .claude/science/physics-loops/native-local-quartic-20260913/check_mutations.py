"""Author mutation challenges; this harness is not an independent audit."""
from pathlib import Path
import gzip,hashlib,json,os,subprocess,tempfile,time
AUDIT_TIMEOUT_SEC = 180
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'scripts/native_weyl_local_interaction_covariance_2026_09_13.py'
MUTATIONS=[('graded_bracket_sign', 'def pb(a,b):return scale(-s.I,', 'def pb(a,b):return scale(s.I,'), ('right_odd_derivative', '(-1)**(len(m)-1-k)*c', '(-1)**(len(m)-k)*c'), ('pair_conjugation_order', 'for i in reversed(m)', 'for i in m'), ('kinetic_lapse_coefficient', 'kinetic=scale(-s.I*N/2,', 'kinetic=scale(-s.I*N/4,'), ('Euler_integration_by_parts', 'scale(-1,total_x(left(kinetic,index+8)))', 'scale(1,total_x(left(kinetic,index+8)))'), ('native_Wilson_symbol', '2+zeta-s.cos(k1)-s.cos(k2)-s.cos(k3)', '2+zeta-s.cos(k1)-s.cos(k2)+s.cos(k3)'), ('left_Weyl_boost', 'boost=s.diag(sig/2,-sig/2)', 'boost=s.diag(sig/2,sig/2)'), ('cross_current_sign', '*(mul(a,b) for a,b in zip(jR,jL))', '*(scale(-1,mul(a,b)) for a,b in zip(jR,jL))'), ('native_relative_orbital_phase', 'scale(-1/z,q[3])', 'scale(1/z,q[3])'), ('density_forward_factor', 'scale(forward[i,j]/2,', 'scale(forward[i,j],'), ('density_intervalley_sign', 'scale(exchange[i,j],', 'scale(-exchange[i,j],'), ('density_mean_zero_choice', 'aq:1,bq:-1,cq:1', 'aq:1,bq:0,cq:1'), ('density_invariant_image', 'scale(bq/2,cross)', 'scale(bq,cross)'), ('CAR_anticommutation_sign', '(-1)**((k&((1<<j)-1)).bit_count())', '1'), ('filtered_CAR_overlap', 'Fplus=[1j/(4*v),.5,-1j/(4*v)]', 'Fplus=[1j/(4*v),.4,-1j/(4*v)]'), ('quartic_normal_order', '-(sites[i].conj().T@sites[k])@', '+(sites[i].conj().T@sites[k])@'), ('native_density_stencil', 'for disp,coef in [(1,.5),(2,-.5)]', 'for disp,coef in [(1,.25),(2,-.5)]'), ('native_valley_spinor', '*(np.array([1,-1])*vl)', '*(np.array([1,1])*vl)'), ('physical_spacing_power', 'scaled=vel0*W/spacing**3', 'scaled=vel0*W/spacing**2'), ('native_two_particle_exchange', '-vv[:,:,None]*ush[:,None,:]', '+vv[:,:,None]*ush[:,None,:]')]

def main():
 started=time.monotonic();original=SOURCE.read_text();sha=hashlib.sha256(original.encode()).hexdigest()
 for name,old,new in MUTATIONS:
  assert original.count(old)==1,(name,'selector_count',original.count(old))
  compile(original.replace(old,new),'<mutation>','exec')
 rows=[];out=HERE/'mutation_evidence';out.mkdir(exist_ok=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
 for name,old,new in MUTATIONS:
  mutated=original.replace(old,new)
  with tempfile.TemporaryDirectory(prefix='toe-quartic-mutation-') as temp:
   root=Path(temp);(root/'scripts').mkdir();p=root/'scripts'/SOURCE.name;p.write_text(mutated)
   result=subprocess.run(['python3',str(p)],capture_output=True,env=env,timeout=60)
  folder=out/name;folder.mkdir(exist_ok=True)
  for fn,data in [('source.py',mutated.encode()),('stdout',result.stdout),('stderr',result.stderr)]:
   (folder/(fn+'.gz')).write_bytes(gzip.compress(data,mtime=0))
  effective=result.returncode!=0 and b'AssertionError' in result.stderr and b'duplicate check names' not in result.stderr
  row=dict(name=name,original_sha256=sha,mutated_sha256=hashlib.sha256(mutated.encode()).hexdigest(),old=old,new=new,returncode=result.returncode,effective=effective,stderr_tail=result.stderr.decode()[-1600:])
  (folder/'manifest.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
  if not effective:
   (HERE/'MUTATIONS_INCOMPLETE.json').write_text(json.dumps(rows,indent=2)+'\n')
   raise AssertionError((name,'no mathematical failure'))
 receipt=dict(source_sha256=sha,mutation_count=len(rows),all_effective=all(r['effective'] for r in rows),elapsed_seconds=time.monotonic()-started,mutations=rows)
 (HERE/'MUTATIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k!='mutations'}))
if __name__=='__main__':main()
