"""Author wrong-formula challenges; not an independent review."""
from pathlib import Path
import gzip,hashlib,json,os,subprocess,tempfile,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'scripts/local_hall_free_mixed_weyl_quartet_and_common_metric_2026_09_13.py'
MUTATIONS=[
('mixing_spin_direction','m1*XX+m3*ZX','m1*ZX+m3*XX'),
('onsite_hopping_phase','[(c-1j*a)/2 for c,a in zip(C,A)]','[(c+1j*a)/2 for c,a in zip(C,A)]'),
('squared_spectral_split','split=2*np.sqrt((a*b1+c*d)**2','split=np.sqrt((a*b1+c*d)**2'),
('noncommuting_H_squared_sign','+2*(b1*m3-d*m1)*np.kron(SIG[1],SIG[1])','-2*(b1*m3-d*m1)*np.kron(SIG[1],SIG[1])'),
('node_R_sign','R2=1-mu*mu*np.sin(2*theta-b)/np.sin(b)','R2=1+mu*mu*np.sin(2*theta-b)/np.sin(b)'),
('node_X_half_factor','mu*mu*np.sin(2*theta)/(2*np.sin(b))','mu*mu*np.sin(2*theta)/np.sin(b)'),
('missing_second_ky_plane','for y in [0,np.pi]:','for y in [0]:'),
('spectator_gap_factor','gap2=4*(np.sin(b)**2+mu*mu*np.cos(theta)**2)','gap2=2*(np.sin(b)**2+mu*mu*np.cos(theta)**2)'),
('determinant_metric_phase','qz=2*(c-1j*t*np.sin(b))*np.sin(z)','qz=2*(c+1j*t*np.sin(b))*np.sin(z)'),
('metric_y_normalization','G[1,1]=1','G[1,1]=.5'),
('occupied_Weyl_orientation','detJ=-np.cos(y)*np.imag(qx.conjugate()*qz)/gap2','detJ=np.cos(y)*np.imag(qx.conjugate()*qz)/gap2'),
('second_plane_chirality','detJ=-np.cos(y)*np.imag','detJ=-np.imag'),
('aligned_common_metric_speed','common=np.diag([R*R,1,','common=np.diag([R**4,1,'),
('Kubo_factor_two','return float(2*np.imag(np.sum(A[:2,2:]','return float(np.imag(np.sum(A[:2,2:]'),
('Kubo_occupied_band_count','A[:2,2:]*B[2:,:2].T/(e[:2,None]-e[None,2:])**2','A[:1,2:]*B[2:,:1].T/(e[:1,None]-e[None,2:])**2'),
('Kubo_gap_power','/(e[:2,None]-e[None,2:])**2','/(e[:2,None]-e[None,2:])**3'),
('wrong_occupied_projector','np.linalg.eigh(h(k,*parameters))[1][:,:2]','np.linalg.eigh(h(k,*parameters))[1][:,2:]'),
('Chern_link_orientation','return d/abs(d)','return d.conjugate()/abs(d)'),
('commutant_ignores_onsite_mixing','coeffs=[onsite,','coeffs=[0*onsite,'),
('Peierls_Ward_incidence','2*np.sin(qmom[j]/2)*derivative(mid,b,j)','np.sin(qmom[j]/2)*derivative(mid,b,j)'),
('Peierls_contact_half','val=(1j*dc)**power*hop[axis]','val=(1j*dc)**power*hop[axis]*(.5 if power==2 else 1)'),
('gauge_hessian_bubble_factor','bubble=2*np.sum(abs(A[np.ix_(occ,~occ)])','bubble=np.sum(abs(A[np.ix_(occ,~occ)])'),
('gauge_charge_normalization','np.repeat(np.exp(-.37j*chi.ravel()),4)','np.repeat(np.exp(-.74j*chi.ravel()),4)'),
('perturbation_breaks_T','p=np.kron(SIG[1],SIG[2])+.31','p=np.kron(SIG[1],SIG[1])+.31'),
('silently_fixed_node_energy','return np.array([np.trace(A@s).real/2 for s in SIG]),np.trace(A).real/2','return np.array([np.trace(A@s).real/2 for s in SIG]),0.'),
('spinless_TRIM_real_linear_terms','np.max(abs(s.conj()+s))<1e-12','np.max(abs(s.conj()-s))<1e-12'),
]
def main():
 start=time.monotonic();original=SOURCE.read_text();sha=hashlib.sha256(original.encode()).hexdigest();out=HERE/'mutation_evidence';out.mkdir(exist_ok=True);rows=[]
 for name,old,new in MUTATIONS:
  assert original.count(old)==1,(name,'selector_count',original.count(old));compile(original.replace(old,new),'<mutation>','exec')
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
 for name,old,new in MUTATIONS:
  mutated=original.replace(old,new)
  with tempfile.TemporaryDirectory(prefix='toe-quartet-mutation-') as temp:
   p=Path(temp)/'primary.py';p.write_text(mutated);r=subprocess.run(['python3',str(p)],capture_output=True,env=env,timeout=60)
  folder=out/name;folder.mkdir(exist_ok=True)
  for filename,data in [('source.py',mutated.encode()),('stdout',r.stdout),('stderr',r.stderr)]:(folder/(filename+'.gz')).write_bytes(gzip.compress(data,mtime=0))
  effective=r.returncode!=0 and b'AssertionError' in r.stderr
  row=dict(name=name,source_sha256=sha,mutated_sha256=hashlib.sha256(mutated.encode()).hexdigest(),old=old,new=new,returncode=r.returncode,effective=effective,stderr_tail=r.stderr.decode()[-1800:]);rows.append(row)
  (folder/'manifest.json').write_text(json.dumps(row,indent=2)+'\n')
  if not effective:
   (HERE/'MUTATIONS_INCOMPLETE.json').write_text(json.dumps(rows,indent=2)+'\n');raise AssertionError((name,'no mathematical failure'))
 result=dict(source_sha256=sha,count=len(rows),all_effective=all(r['effective'] for r in rows),elapsed_seconds=time.monotonic()-start,mutations=rows)
 (HERE/'MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='mutations'}))
if __name__=='__main__':main()
