from pathlib import Path
import json,hashlib,time
R=Path('/Users/jonreilly/Documents/Codex/toe-clock-ward-quadrature-20260914/scripts/finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_2026_09_14.py')
source=R.read_text()
faults=[
('gaussian_half','w=np.exp(-b*v*v/2)','w=np.exp(-b*v*v)'),
('image_period','v=u[...,None]-2*PI*k','v=u[...,None]-PI*k'),
('image_derivative_sign','(-b*v*w).sum(-1)','(b*v*w).sum(-1)'),
('incident_precision','r=len(bs);G=bs.sum()','r=len(bs);G=bs.mean()'),
('weighted_center','bar=(d*bs).sum(1)/G','bar=d.mean(1)'),
('relative_image_weight','A=np.exp(-.5*((d-bar[:,None])**2*bs).sum(1))','A=np.exp(-.5*(d**2*bs).sum(1))'),
('fourier_phase','np.sum(A*np.exp(1j*m*bar))','np.sum(A*np.exp(-1j*m*bar))'),
('fourier_precision','expected=np.exp(-m*m/(2*G))','expected=np.exp(-m*m*G/2)'),
('quadrature_no_pair','eps=float(2*e.sum())','eps=float(e.sum())'),
('conditional_force_sign','ward=np.sum(pn*(fp+lpn*f))/pn.sum()','ward=np.sum(pn*(fp-lpn*f))/pn.sum()'),
('ward_normalization','ward=np.sum(pn*(fp+lpn*f))/pn.sum()','ward=np.sum(pn*(fp+lpn*f))/pn.mean()'),
('alias_zero_mode','alias=sum(spectrum[(q*N)%len(grid)]','alias=sum(spectrum[(q*N+1)%len(grid)]'),
('continuous_partition','p0=1/math.sqrt(2*PI*G)','p0=1/math.sqrt(PI*G)'),
('charge_N_not_constant','assert abs(clock-1)<1e-12','assert abs(clock-haar)<1e-12'),
('wilson_Haar_energy','haar=np.exp(-sum(mi*mi/(2*b)','haar=np.exp(-sum(mi*mi/b'),
('growing_order_sqrt_log','math.sqrt(2*G*(1+delta)*math.log(2*E))','math.sqrt(2*G*(1+delta))'),
]
results=[]
for name,old,new in faults:
 assert source.count(old)==1,(name,source.count(old));ns={'__name__':'personal_mutation'};exec(compile(source.replace(old,new),'<mutation:'+name+'>','exec'),ns);start=time.monotonic()
 try:ns['run']()
 except AssertionError as e:results.append(dict(name=name,detected=True,failure=str(e)[:350],elapsed_sec=time.monotonic()-start))
 else:results.append(dict(name=name,detected=False,elapsed_sec=time.monotonic()-start))
 print(name,results[-1]['detected'],flush=True)
record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal deliberate-fault challenges; not independent proof review or an audit verdict.')
Path(__file__).with_name('BLOCK14_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n');assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
