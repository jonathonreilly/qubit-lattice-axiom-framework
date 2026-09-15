from pathlib import Path
import json,hashlib,time
R=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915/scripts/quantized_current_poisson_identity_centered_gaussian_domination_and_clock_wilson_cosets_2026_09_15.py')
source=R.read_text()
faults=[
('lattice_covolume','abs(np.linalg.det(B))*math.sqrt(np.linalg.det(A))','math.sqrt(np.linalg.det(A))','nonsquare_lattice'),
('dual_lattice_transpose','k=grid(2,24)@np.linalg.inv(B)','k=grid(2,24)@np.linalg.inv(B).T','nonsquare_lattice'),
('generic_dual_damping','R=k-b;v=p*np.exp(-2*np.pi**2','R=k-b;v=p*np.exp(-np.pi**2','nonsquare_lattice'),
('generic_covariance_normalization','target=Ai-4*np.pi**2*Ai@(dcov/dualz)@Ai','target=Ai-2*np.pi**2*Ai@(dcov/dualz)@Ai','nonsquare_lattice'),
('generic_mgf_frequency','mgfs[i]+=v@np.cos(2*np.pi*R@Ai@h)','mgfs[i]+=v@np.cos(np.pi*R@Ai@h)','nonsquare_lattice'),
('generic_coset_shift','cosets[i]+=v@np.exp(2j*np.pi*k@s)','cosets[i]+=v@np.exp(2j*np.pi*R@s)','nonsquare_lattice'),
('electric_precision_beta','A=N*N/beta*Qi;Ai=beta/(N*N)*Q','A=N*N*beta*Qi;Ai=beta/(N*N)*Q','actual_current_cube'),
('magnetic_shift_N','b=N*M*mm;k=k0+np.rint(b)','b=M*mm;k=k0+np.rint(b)','actual_current_cube'),
('physical_Wilson_variable','wilson+=v@np.cos(2*np.pi*k@s)','wilson+=v@np.cos(2*np.pi*R@s)','actual_current_cube'),
('external_source_N','J=D[0].astype(float);s=J/N','J=D[0].astype(float);s=J','actual_current_cube'),
('clock_alias','alias=N*np.eye(r)[0]','alias=np.eye(r)[0]','actual_current_cube'),
('Fourier_current_rescale','aa=integer_div[mask]/N','aa=integer_div[mask]','actual_current_cube'),
('Fourier_source_modulus','np.rint(integer_div+J).astype(int)%N==0','np.rint(integer_div).astype(int)%N==0','actual_current_cube'),
('continuous_all_tilt_bound','vt>=.25-1e-15 and vt>1/alpha','vt<=1/alpha','discrete_controls'),
('signed_mixing_measure','chi=(1-p*np.cos(np.pi*n))/(1-p)','chi=(1+p*np.cos(np.pi*n))/(1+p)','discrete_controls'),
('positive_mixing_signed_lattice','signed=np.exp(-alpha*n*n/2)*np.cos(np.pi*n)','signed=np.exp(-alpha*n*n/2)*(1+np.cos(np.pi*n))/2','discrete_controls'),
('zero_coset_strict_positivity','assert np.max(abs(zeros))<1e-14','assert min(zeros)>0','discrete_controls'),
('Hodge_projected_metric','H*P==d1.T*d1','H*P==H','hodge_edge_bounds')]
results=[]
for name,old,new,target in faults:
 count=source.count(old);assert count==(2 if name=='generic_covariance_normalization' else 1),(name,count)
 ns={'__name__':'personal_mutation'};exec(compile(source.replace(old,new,1),'<mutation:'+name+'>','exec'),ns);start=time.monotonic()
 try:ns[target]()
 except AssertionError as e:row=dict(name=name,detected=True,target=target,failure=str(e)[:300],elapsed_sec=time.monotonic()-start)
 else:row=dict(name=name,detected=False,target=target,elapsed_sec=time.monotonic()-start)
 results.append(row);print(name,row['detected'],flush=True)
record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal targeted fault challenges, not independent review or an audit verdict.')
Path(__file__).with_name('BLOCK18_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n')
assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
