from pathlib import Path
import hashlib,json,time
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915/scripts')
tasks=[
(15,'carrier_preserving_closed_integer_charge_gas_convexification_2026_09_15.py',[
 ('parallel_instead_of_transverse_carrier','cancellation','direction=p-1','direction=0'),
 ('exterior_incidence_sign','cancellation','out.get((x,J),0)-s*v','out.get((x,J),0)+s*v'),
 ('charge_cancellation_sign','cancellation','n2[k]=-1','n2[k]=1'),
 ('net_mass_for_total_mass','cancellation','assert s==4*R+4 and net==8','assert s==net and net==8'),
 ('Ursell_sign','trees_and_logarithm','result+=(-1)**len(chosen)','result+=1'),
 ('complete_graph_factorial','trees_and_logarithm','math.factorial(n-1) and T','math.factorial(n) and T'),
 ('Eulerian_recurrence','constants','+(n-k)*(a[k-1]','+(n-k+1)*(a[k-1]'),
 ('Gaussian_split_factor','constants','t=math.pi**2*beta/(4*d)','t=math.pi**2*beta/(8*d)'),
 ('theta_energy_factor','finite_theta_hessian','w=np.exp(-4*t*n*n)','w=np.exp(-2*t*n*n)'),
 ('Poisson_Hessian_sign','finite_theta_hessian','dual_hess=-np.pi**2/(2*t)+','dual_hess=np.pi**2/(2*t)+'),
 ('effective_action_sign','finite_theta_hessian','effective=precision-hess','effective=precision+hess'),
 ('residual_covariance_sign','gaussian_precision','residual=np.linalg.inv(G-c*np.eye(L))','residual=np.linalg.inv(G+c*np.eye(L))'),
 ('precision_geometric_sign','gaussian_precision','series=sum(c**k','series=sum((-c)**k'),
 ('source_variance_sign','source_curvature','combined=mean_curvature+variance_term','combined=mean_curvature-variance_term'),
 ('source_residual_covariance','source_curvature','variance=beta*(G-c)','variance=beta*c'),
 ('source_normalization','source_curvature','mu=weights*Z/normalization','mu=weights*Z'),
]),
(16,'finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.py',[
 ('discard_mutual_phase','comparisons','mag=phase@mag_w','mag=np.full(denom,mag_w.sum())'),
 ('electric_beta_inverse','comparisons','l,Qi,l)/(2*beta)','l,Qi,l)*beta/2'),
 ('electric_alias_spacing','comparisons','l=j[None,:]+N*a','l=j[None,:]+a'),
 ('omit_source_character','comparisons','l=j[None,:]+N*a','l=N*a'),
 ('magnetic_beta_inverse','comparisons','beta*B*b*b','B*b*b/beta'),
 ('magnetic_energy_half','comparisons','-2*np.pi**2*beta*B*b*b','-np.pi**2*beta*B*b*b'),
 ('Gaussian_prefactor','comparisons','c=(2*np.pi*beta)**(-r/2)','c=(np.pi*beta)**(-r/2)'),
 ('Gaussian_determinant','comparisons','/math.sqrt(float(C[\'Q\'].det()))','/float(C[\'Q\'].det())'),
 ('phase_character_frequency','comparisons','np.cos(2*np.pi*np.arange(denom)','np.cos(np.pi*np.arange(denom)'),
 ('magnetic_representative_shift','comparisons','k+C[\'D\']*n','k+2*C[\'D\']*n'),
 ('four_cube_clock_order','four_cube_witness','k=3*ep;N=3','k=3*ep;N=2'),
 ('four_cube_magnetic_charge','four_cube_witness','k=3*ep;N=3','k=ep;N=3'),
 ('four_cube_current','four_cube_witness','a=D.T*ep;k=3*ep','a=2*D.T*ep;k=3*ep'),
])]
for block,name,faults in tasks:
 R=ROOT/name;source=R.read_text();results=[]
 for title,fn,old,new in faults:
  count=source.count(old);assert count>=1,(title,count)
  if title!='magnetic_representative_shift':assert count==1,(title,count)
  ns={'__name__':'personal_mutation'};exec(compile(source.replace(old,new),'<mutation:'+title+'>','exec'),ns);start=time.monotonic()
  try:ns[fn]()
  except AssertionError as e:results.append(dict(name=title,function=fn,detected=True,failure=str(e)[:300],elapsed_sec=time.monotonic()-start))
  else:results.append(dict(name=title,function=fn,detected=False,elapsed_sec=time.monotonic()-start))
  print(block,title,results[-1]['detected'],flush=True)
 record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal deliberate-fault challenges only; not independent proof review or an audit verdict.')
 Path(__file__).with_name(f'BLOCK{block}_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n')
 assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
