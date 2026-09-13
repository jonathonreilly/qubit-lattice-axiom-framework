from pathlib import Path
import sys,json,gzip,hashlib,subprocess,time,os
root=Path.cwd();sys.path[:0]=[str(root/'scripts'),str(root/'docs/audit/scripts')]
import runner_cache
import forensic_evidence_readiness as readiness
p=root/'.claude/science/physics-loops/gauss-reduced-weak-coupling-spectrum-20260913'
runner='scripts/exact_gauss_reduction_and_fixed_volume_weak_coupling_spectrum_2026_09_13.py'
note='docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md'
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
('root_flow_sign','R[edge, x] = D[v, edge]','R[edge, x] = -D[v, edge]'),
('cycle_sign','- R @ D[:, chords]','+ R @ D[:, chords]'),
('plaquette_orientation','((v, j), -1)','((v, j), 1)'),
('weighted_coulomb','@ rho))/we','@ rho))*we'),
('charged_chord_translation','n+(edge == 3)','n-(edge == 3)'),
('charged_domain_product','range(-S-int(min(E0[f])), S-int(max(E0[f]))+1)','range(-S, S+1)'),
('charged_electric_factor','.5*g*g*np.dot(E0[f]+n, E0[f]+n)','g*g*np.dot(E0[f]+n, E0[f]+n)'),
('charged_magnetic_factor','H[row, col] += -1/(2*g*g)','H[row, col] += -1/(g*g)'),
('car_annihilation_sign','(-1)**sum((f >> k) & 1 for k in range(j))','1'),
('pure_magnetic_factor','off = -np.ones(len(n)-step)/(2*g*g)','off = -np.ones(len(n)-step)/(g*g)'),
('harmonic_rank','D.shape[1]-D.shape[0]+1-3','D.shape[1]-D.shape[0]+1'),
('cube_frequency','[4, 4, 4, 6, 6]','[4, 4, 4, 4, 4]'),
('box_ode_coefficient','coeff*(4*n-(energy-1))','coeff*(2*n-(energy-1))'),
('box_hypergeom_parameter','hyp1f1((1-E)/4','hyp1f1((1-E)/2'),
('boundary_form_factor','np.sum(np.diff(np.r_[0., v, 0.])**2)/(2*g*g)','np.sum(np.diff(np.r_[0., v, 0.])**2)/(g*g)'),
('double_copy_erasure','step=2)','step=1)')]
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
