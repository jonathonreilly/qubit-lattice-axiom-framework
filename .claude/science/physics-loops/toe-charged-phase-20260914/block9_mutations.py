from pathlib import Path
import json,hashlib,gzip,subprocess,tempfile,time,os
root=Path('/Users/jonreilly/Documents/Codex/toe-ice-winding-response-20260914')
primary=root/'scripts/cubic_ice_relaxed_magnetic_response_graph_flows_and_sheet_winding_2026_09_14.py'
packet=root/'.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block9'
source=primary.read_text();evidence=packet/'mutation_evidence';evidence.mkdir(exist_ok=True)
mutations=[
('cartesian_epsilon','exact_rk_certificate','y=index[dest];a=(-1)**sum(r)*(2*bits[0]-1)','y=index[dest];a=(2*bits[0]-1)'),
('Perron_edge_weight','spectral_graph_match','w=psi[x]*psi[y];Lw=','w=psi[x]*psi[x];Lw='),
('relaxation_factor','spectral_graph_match','variational=2*np.dot(w,residual*residual)','variational=np.dot(w,residual*residual)'),
('exact_Krylov_relation','exact_rk_certificate','coeff=[235008,-204608,69072','coeff=[235008,-204608,69073'),
('Doob_jump_rate','reversible_toy_transport','one[xx,yy]+=j*psi[yy]/psi[xx]*a','one[xx,yy]+=j*psi[xx]/psi[yy]*a'),
('current_bias_sign','reversible_toy_transport','bias=2/t*np.dot(bb*bb','bias=-2/t*np.dot(bb*bb'),
('frozen_field_dependence','frozen_cubic_states','(-1)**r[2]/2,(-1)**r[0]/2','(-1)**r[2]/2,(-1)**r[2]/2'),
('membrane_height_order','explicit_membrane_cycles','key=lambda f:-levels[f]','key=lambda f:levels[f]'),
('thermal_beta_normalization','positive_history_and_sector_limits','response=moment/(beta*Z)','response=moment/Z'),
('frozen_sector_multiplicity','positive_history_and_sector_limits','full=C/8*Z/(Z+16)','full=C/8*Z/(Z+15)'),
('comparison_congestion','comparison_and_contractible_moves','original+1e-12>=auxiliary/congestion','original+1e-12>=auxiliary*congestion')]
results=[]
for name,family,old,new in mutations:
 count=source.count(old);assert count==1,(name,count)
 mutant=source.replace(old,new);filename=Path(tempfile.gettempdir())/f'toe_block9_mutant_{name}.py'
 filename.write_text(mutant)
 # Invoke only the affected scientific family, preserving the entire mutated
 # source file. This avoids repeating unrelated checks and does not alter it.
 invoke='import runpy; runpy.run_path('+repr(str(filename))+')['+repr(family)+']()'
 started=time.monotonic();r=subprocess.run(['python3','-c',invoke],capture_output=True,text=True,timeout=90,cwd=root,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
 elapsed=time.monotonic()-started
 for suffix,data in [('py',mutant),('stdout',r.stdout),('stderr',r.stderr)]:
  with gzip.open(evidence/f'{name}.{suffix}.gz','wb') as f:f.write(data.encode())
 entry={'name':name,'family':family,'old':old,'new':new,'replacements':count,'mutant_sha256':hashlib.sha256(mutant.encode()).hexdigest(),'exit_code':r.returncode,'elapsed_sec':elapsed,'assertion_detected':r.returncode!=0 and 'AssertionError' in r.stderr,'stderr_tail':r.stderr[-1800:]}
 results.append(entry);print({k:entry[k] for k in ['name','exit_code','assertion_detected']},flush=True)
 filename.unlink()
(packet/'MUTATION_RESULTS.json').write_text(json.dumps({'primary_sha256':hashlib.sha256(source.encode()).hexdigest(),'execution':'Affected scientific family invoked from entire preserved mutated source; no unrelated families rerun.','results':results},indent=2)+'\n')
assert all(r['assertion_detected'] for r in results)
