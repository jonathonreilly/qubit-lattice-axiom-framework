"""Personal deliberate-fault challenges; no independent audit status."""
from pathlib import Path
import hashlib,json,time
P=Path(__file__).parents[1];R=Path('/Users/jonreilly/Documents/Codex/toe-direct-clock-wilson-20260914/scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py');source=R.read_text()
faults=[
('disjoint_cube_support','cochain_quantization','range(0,L,2)','range(0,L,1)'),
('harmonic_unit_norm','cochain_quantization','h[(0,1)][:]=L**-2','h[(0,1)][:]=L**-1'),
('lift_normalization','cochain_quantization','2*np.pi*np.sqrt(beta)*(curl[I]/N-k[I])','np.pi*np.sqrt(beta)*(curl[I]/N-k[I])'),
('cube_count','cochain_quantization','assert len(cubes)==V//16','assert len(cubes)==V//8'),
('atom_probability','image_atoms_and_cube_law','q=math.exp(-2*math.pi**2*beta);bound=','q=math.exp(-math.pi**2*beta);bound='),
('nearest_neighbor_direction','image_atoms_and_cube_law','toward=mode+(1 if t>=mode else -1)','toward=mode+(-1 if t>=mode else 1)'),
('clock_lift_variance','image_atoms_and_cube_law','sigma=N*N/(4*np.pi**2*beta)','sigma=N*N/(2*np.pi**2*beta)'),
('clock_gaussian_image','image_atoms_and_cube_law','-beta*(angles[:,None]-2*np.pi*image[None,:])**2/2','-beta*(angles[:,None]-2*np.pi*image[None,:])**2'),
('root_of_unity_normalizer','image_atoms_and_cube_law',"**6 for j in range(N))/N","**6 for j in range(N))/(N+1)"),
('operator_norm_constant','integer_current_map_and_theta','close(dot(a,a),16*dot(w,w))','close(dot(a,a),8*dot(w,w))'),
('inverse_current_potential','integer_current_map_and_theta','psi=green(ds(source,L,2),L)','psi=ds(source,L,2)'),
('potential_radius_constant','integer_current_map_and_theta','B=math.pi*math.sqrt(sigma)/32','B=math.pi*math.sqrt(sigma)/16'),
('real_poisson_source_sign','affine_source_relative','np.exp(2*np.pi*np.sqrt(sigma)*(W@he))','np.exp(-2*np.pi*np.sqrt(sigma)*(W@he))'),
('affine_phase_omitted','affine_source_relative','phase=np.exp(2j*np.pi*W@b)','phase=np.ones(len(W))'),
('imaginary_poisson_source','affine_source_relative','np.exp(2*np.pi*np.sqrt(sigma)*(W@he))','np.exp(2j*np.pi*np.sqrt(sigma)*(W@he))'),
('gaussian_characteristic_factor','affine_source_relative','G=math.exp(-he@he/2)','G=math.exp(-he@he/4)'),
('scalar_theta_two_signs','integer_current_map_and_theta','return 1+2*sum(math.exp(-u*n*n)','return 1+sum(math.exp(-u*n*n)'),
('scalar_theta_square','integer_current_map_and_theta','math.exp(-u*n*n) for n in range(1,cut+1)','math.exp(-u*n) for n in range(1,cut+1)'),
('scalar_laplacian_normalization','integer_current_map_and_theta','lam=sum(4*np.sin','lam=sum(2*np.sin'),
('green_zero_mode','loop_potential_refinement','out=np.zeros_like(lam),where=lam>1e-12','out=np.ones_like(lam),where=lam>1e-12'),
('logarithmic_family_coefficient','logarithmic_rates_and_moment_boundary','beta=math.ceil(4*math.log(2*V));N=8*beta;sigma=N*N','beta=math.ceil(2*math.log(2*V));N=8*beta;sigma=N*N'),
('clock_order_to_variance','logarithmic_rates_and_moment_boundary','N=8*beta;sigma=N*N/(4*math.pi**2*beta)','N=4*beta;sigma=N*N/(4*math.pi**2*beta)'),
('principal_moment_volume_exponent','logarithmic_rates_and_moment_boundary','(k+1)/2-math.pi**2','k/2-math.pi**2'),
('conditional_is_not_unconditional','conditional_defect_count','joint=(p0*p0+p1*p1)/2','joint=mean*mean'),
('charge_alias_scope','loop_potential_refinement','q=N;B=q/math.sqrt(beta)','q=1;B=q/math.sqrt(beta)'),
]
results=[]
for name,fn,old,new in faults:
 assert source.count(old)==1,(name,source.count(old));ns={'__name__':'personal_mutation'};mutated=source.replace(old,new)
 exec(compile(mutated,'<mutation:'+name+'>','exec'),ns)
 start=time.monotonic()
 try:ns[fn]()
 except AssertionError as e:results.append(dict(name=name,function=fn,detected=True,failure=str(e)[:350],elapsed_sec=time.monotonic()-start))
 else:results.append(dict(name=name,function=fn,detected=False,elapsed_sec=time.monotonic()-start))
 print(name,results[-1]['detected'],flush=True)
record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal selected-family deliberate-fault checks; not an independent review or proof of universal claims.')
Path(__file__).with_name('BLOCK12_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n')
assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
