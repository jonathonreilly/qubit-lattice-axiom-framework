from pathlib import Path
import json,hashlib,time
R=Path('/Users/jonreilly/Documents/Codex/toe-clock-image-noise-20260914/scripts/finite_clock_image_noise_current_sector_and_positive_time_os_equivalence_2026_09_14.py');source=R.read_text()
faults=[
('lift_sqrt_beta','conditional_moments_and_score','X=np.sqrt(beta)*(angle-2*np.pi*k)','X=beta*(angle-2*np.pi*k)'),
('gaussian_energy_half','conditional_moments_and_score','logs=-X*X/2','logs=-X*X'),
('missing_conditional_center','conditional_moments_and_score','xi=X-mean','xi=X'),
('raw_second_as_variance','conditional_moments_and_score','var=float(p@(xi*xi))','var=float(p@(X*X))'),
('score_derivative_sign','conditional_moments_and_score','score=2*np.sum(n*coeff*np.sin(n*angle))','score=-2*np.sum(n*coeff*np.sin(n*angle))'),
('variance_boltzmann_sign','conditional_moments_and_score','lower=4*math.pi**2*beta*math.exp(-c)','lower=4*math.pi**2*beta*math.exp(c)'),
('curvature_noise_sign','conditional_moments_and_score','close(v,1-curvature/beta,2e-7)','close(v,1+curvature/beta,2e-7)'),
('curvature_beta_normalization','conditional_moments_and_score','close(v,1-curvature/beta,2e-7)','close(v,1-curvature,2e-7)'),
('two_clock_angle','two_clock_score_alias','for u in [0,np.pi]]','for u in [0,np.pi/2]]'),
('clt_source_normalization','conditional_characteristic_clt','u=t/math.sqrt(count)','u=t/count'),
('clt_log_product','conditional_characteristic_clt','actual=count*np.log(chi)','actual=math.sqrt(count)*np.log(chi)'),
('third_signed_moment','conditional_characteristic_clt','third=float(p@abs(xi)**3)','third=float(p@xi**3)'),
('average_invariant_variance','conditional_stability_and_mixture','target=prob@(B*np.exp(-variances*t*t/2))','target=(prob@B)*math.exp(-float(prob@variances)*t*t/2)'),
('variance_mixture_fourth','conditional_stability_and_mixture','fourth=3*float(prob@(variances**2))','fourth=3*meanv**2'),
('os_noise_average_factor','white_noise_os_intertwiner','D=np.exp(-noise*charges**2/2)','D=np.exp(-noise*charges**2)'),
('white_cross_noise','white_noise_os_intertwiner','HX=gram(self_F+noise);D=','HX=gram(self_F+noise)*np.exp(noise*charges[:,None]*charges[None,:]);D='),
('hodge_projection_factor','current_sector_blindness','Pe=d1@d1.T/(p@p)','Pe=d1@d1.T/(2*(p@p))'),
('white_imposed_bianchi','current_sector_blindness','I=np.eye(6)','I=Pe'),
('magnetic_fourier_factor','current_sector_blindness','kernel=s2/(2*r)*math.exp(-r*tau)','kernel=s2/r*math.exp(-r*tau)'),
('magnetic_time_exponent','current_sector_blindness','kernel=s2/(2*r)*math.exp(-r*tau)','kernel=s2/(2*r)*math.exp(-2*r*tau)'),
('current_contact_derivative','current_sector_blindness','r*r+1/(2*eps)-tau*tau/(4*eps*eps)','r*r+1/(2*eps)+tau*tau/(4*eps*eps)'),
]
results=[]
for name,fn,old,new in faults:
 assert source.count(old)==1,(name,source.count(old));ns={'__name__':'personal_mutation'};exec(compile(source.replace(old,new),'<mutation:'+name+'>','exec'),ns);start=time.monotonic()
 try:ns[fn]()
 except AssertionError as e:results.append(dict(name=name,function=fn,detected=True,failure=str(e)[:350],elapsed_sec=time.monotonic()-start))
 else:results.append(dict(name=name,function=fn,detected=False,elapsed_sec=time.monotonic()-start))
 print(name,results[-1]['detected'],flush=True)
record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal selected-family deliberate-fault challenges only; not independent proof review or an audit verdict.')
Path(__file__).with_name('BLOCK13_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n');assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
