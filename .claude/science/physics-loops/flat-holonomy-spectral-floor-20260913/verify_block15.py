from pathlib import Path
import sys,json,gzip,hashlib,subprocess,time,os
root=Path.cwd();sys.path[:0]=[str(root/'scripts'),str(root/'docs/audit/scripts')]
import runner_cache
import forensic_evidence_readiness as readiness
p=root/'.claude/science/physics-loops/flat-holonomy-spectral-floor-20260913'
runner='scripts/flat_holonomy_minimization_and_periodic_spectral_floor_2026_09_13.py'
note='docs/FLAT_HOLONOMY_MINIMIZATION_AND_PERIODIC_SPECTRAL_FLOOR_BOUNDED_THEOREM_NOTE_2026-09-13.md'
result,cache=runner_cache.execute_and_write_cache(runner,timeout_sec=90)
(p/'CANONICAL_EXECUTION.json').write_text(json.dumps(result,indent=2)+'\n')
(p/'CANONICAL_CACHE.txt.gz').write_bytes(gzip.compress(Path(cache).read_bytes(),mtime=0))
assert result['status']=='ok',result
row=dict(claim_id=Path(note).stem.lower(),claim_type='bounded_theorem',runner_path=runner,note_path=note)
receipt=dict(note_sha256=hashlib.sha256(Path(note).read_bytes()).hexdigest(),runner_sha256=hashlib.sha256(Path(runner).read_bytes()).hexdigest(),runner_source_issue=readiness._runner_source_issue(runner,root),cached_row_readiness_issue=readiness.cached_row_readiness_issue(row,{},repo_root=root),cache_status=runner_cache.cache_status(runner))
(p/'SOURCE_READINESS.json').write_text(json.dumps(receipt,indent=2)+'\n')
assert receipt['runner_source_issue'] is None and receipt['cached_row_readiness_issue'] is None and receipt['cache_status']=='fresh',receipt
print(json.dumps(dict(canonical=result,readiness=receipt)),flush=True)
source=Path(runner).read_text();mutations=[
('ring_chord_shift','n+(edge==3)','n-(edge==3)'),
('ring_electric_factor','.5*g*g*np.dot(offsets[f]+n,offsets[f]+n)','g*g*np.dot(offsets[f]+n,offsets[f]+n)'),
('ring_car_sign','sign*=(-1)**((v&((1<<x)-1)).bit_count())','sign*=1'),
('twist_removed','antiperiodic if twist_y else periodic','periodic'),
('radical_sine_square','S=3*sy*sy','S=sy*sy'),
('radical_inner_coefficient','S+2*ulo','S+ulo'),
('root_lower_shift','lo,hi=Q(k,scale),Q(k+1,scale)','lo,hi=Q(k+1,scale),Q(k+2,scale)'),
('root_upper_shift','lo,hi=Q(k,scale),Q(k+1,scale)','lo,hi=Q(k-1,scale),Q(k,scale)'),
('bloch_twist_factor','+np.array(phi))/L','+2*np.array(phi))/L'),
('site_twist_factor','np.exp(1j*phi[axis]/L)','np.exp(2j*phi[axis]/L)'),
('clifford_cross_sign','+2*(b*n-d*m)*syy*ty0','-2*(b*n-d*m)*syy*ty0'),
('normal_metric','K=sy.Matrix([[4,4],[4,8]])','K=sy.Matrix([[2,4],[4,8]])'),
('filled_ring_formula','2*(np.cos(theta/4)+np.sin(theta/4))','2*(np.cos(theta/4)-np.sin(theta/4))'),
('slow_gap_normalization','2**(-1/4))<.001','2**(1/4))<.001')]
out=p/'mutations';out.mkdir(exist_ok=True);records=[];start=time.monotonic()
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for name,old,new in mutations:
 assert old in source,(name,old)
 wrong=source.replace(old,new,1);path=out/(name+'.py');path.write_text(wrong)
 run=subprocess.run([sys.executable,str(path)],capture_output=True,timeout=90,env=env)
 record=dict(name=name,effective_mathematical_failure=run.returncode!=0 and b'AssertionError' in run.stderr,returncode=run.returncode,source_sha256=hashlib.sha256(wrong.encode()).hexdigest(),failure_tail=run.stderr.decode()[-1200:])
 for suffix,data in [('py',wrong.encode()),('stdout',run.stdout),('stderr',run.stderr)]:
  (out/(name+'.'+suffix+'.gz')).write_bytes(gzip.compress(data,mtime=0))
 path.unlink();records.append(record);print(json.dumps(record),flush=True)
receipt=dict(base_sha256=hashlib.sha256(source.encode()).hexdigest(),elapsed_seconds=time.monotonic()-start,mutations=records)
(p/'MUTATIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
assert all(r['effective_mathematical_failure'] for r in records),records
