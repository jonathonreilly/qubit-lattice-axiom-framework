from pathlib import Path
import sys,subprocess,time,json,hashlib
from concurrent.futures import ThreadPoolExecutor
S=Path(__file__).resolve().parent;W=S.parent/'walk_worktree';source=W/'scripts/excluded_walk_scattering_flux_transport_form_2026_10_11.py';raw=source.read_text();D=S/'flux_publication_mutations';D.mkdir(exist_ok=True)
cases=[
 ('bond_current_sign','return 2*(a[0].conj()*b[j+1]+a[j+1].conj()*b[0]).x','return -2*(a[0].conj()*b[j+1]+a[j+1].conj()*b[0]).x','assert div==rhs'),
 ('absorption_sign','else F(0))-2*z.y*sum','else F(0))+2*z.y*sum','assert div==rhs'),
 ('boundary_orientation','outflux-=bond(shift(x,j,-1),j)','outflux+=bond(shift(x,j,-1),j)','assert outflux==2*G.y'),
 ('corner_amplitude','shift_amp=(phase-1)/8','shift_amp=(phase-1)/4','assert sum(a.abs2() for a in out)==1'),
 ('parity_phase','(-1)**dot(C,p)*amp[i][j]','1*amp[i][j]','assert error<2e-13'),
 ('flux_density_factor','Factual=2*w/(pi*pi*speed*curv)','Factual=w/(pi*pi*speed*curv)','assert abs(norm(expected)-Factual)'),
 ('ellipsoid_flux_factor','flux=D*D*e/(8*pi*pi)','flux=D*D*e/(4*pi*pi)','assert abs(flux-D/(2*pi))'),
 ('form_pair_factor','for i in range(N) for j in range(N))/2','for i in range(N) for j in range(N))/4','assert qpi==phase2*covariance'),
 ('observable_adjoint','T=mm(mm(adj(S),M),S)','T=mm(mm(S,M),S)','assert Df3=='),
 ('fourth_moment_cross','3*B[i][j]**2-B[i][i]*B[j][j]','2*B[i][j]**2-B[i][i]*B[j][j]','assert exact==wanted'),
 ('ellipsoid_geometry','D*(i==j)+k[i]*k[j]','D*(i==j)+0*k[i]*k[j]','assert exact==wanted'),
 ('active_rank','if pivot is None:continue','if pivot is None:return len(a)','assert matrix_rank(exact)==len(active)'),
 ('tensor_upper_bound','e**4/F(30)*k[i]**2','e**4/F(3000)*k[i]**2','assert det([[mat[i][j]'),
]
def run(case):
 name,before,after,check=case;assert raw.count(before)==1,(name,raw.count(before));p=D/(name+'.py');p.write_text(raw.replace(before,after));start=time.monotonic();r=subprocess.run([sys.executable,str(p)],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180);log=D/(name+'.log');log.write_text(r.stdout);hit=r.returncode==1 and 'AssertionError' in r.stdout and check in r.stdout
 return dict(name=name,before=before,after=after,expected_check=check,source=str(p),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),log=str(log),log_sha256=hashlib.sha256(log.read_bytes()).hexdigest(),exit_code=r.returncode,elapsed_seconds=time.monotonic()-start,intended_failure=hit)
with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(run,cases))
(D/'manifest.json').write_text(json.dumps({'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'timeout_seconds':180,'command_prefix':[sys.executable],'mutations':rows},indent=2)+'\n')
for r in rows:print(r['name'],r['exit_code'],r['intended_failure'])
assert all(r['intended_failure'] for r in rows)
