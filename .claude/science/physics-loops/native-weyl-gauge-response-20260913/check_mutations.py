"""Author wrong-value challenges, not independent review."""
from pathlib import Path
import gzip,hashlib,json,os,subprocess,tempfile,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'scripts/native_weyl_gauge_hall_and_cone_flow_2026_09_13.py'
MUTATIONS=[
('parameter_determinant','np.sqrt(np.prod(A,axis=1))','np.prod(A,axis=1)'),
('parameter_vertex_contraction','(2*square-np.sum(square))','(3*square-np.sum(square))'),
('angular_radial_power','w/q2**2,n,n','w/q2,n,n'),
('angular_numerator','inside=E*np.sum(w/q2)-2*E@avg@metric','inside=E*np.sum(w/q2)-E@avg@metric'),
('coframe_linear_coefficient','derivative=-5*C/3+2*np.trace(C)*np.eye(4)/3','derivative=-4*C/3+2*np.trace(C)*np.eye(4)/3'),
('scalar_space_integral','Is-2*(2+r)/(3*r*(1+r)**2)','Is-2*(2+r)/(3*(1+r)**2)'),
('scalar_photon_speed_sign','cd=(r-1/r)/12','cd=(1/r-r)/12'),
('polarization_loop_factor','8*s.integrate(x*(1-x),(x,0,1))/8','4*s.integrate(x*(1-x),(x,0,1))/8'),
('four_component_trace','trace,4*(np.outer(q,q+p)','trace,2*(np.outer(q,q+p)'),
('longitudinal_Ward_sign','qs@deriv@qs,-slash(E[:,j])','qs@deriv@qs,slash(E[:,j])'),
('metric_medium_volume','return M/det,det*np.linalg.inv(M)','return M*det,det*np.linalg.inv(M)'),
('birefringent_magnetic_kernel','n[0]**2*W+C.T@W@C','n[0]**2*W-C.T@W@C'),
('birefringent_time_kernel','out[0,0]=k@W@k','out[0,0]=k@W@k/2'),
('birefringent_self_insertion','actual,2*slash(K[j])','actual,slash(K[j])'),
('relative_metric_running_power','R=z**-3;W=','R=z**-2;W='),
('quadratic_memory_factor','W=s.Rational(2,5)*(z**-1-z**-6)','W=s.Rational(1,5)*(z**-1-z**-6)'),
('accumulated_metric','f=(1+2*tt**-3)/3','f=(1+3*tt**-3)/3'),
('native_incidence_symbol','(2*D[i]/a*np.sin(qmom[i]/2))','(D[i]/a*np.sin(qmom[i]/2))'),
('Peierls_second_contact','val=(1j*delta)**j*hop[axis]','val=(1j*delta)**j*hop[axis]*(.5 if j==2 else 1)'),
('gauge_curvature_bubble_factor','bubble=2*np.sum(abs(pert','bubble=np.sum(abs(pert'),
('native_current_derivative','out[...,axis]=np.cos(k[...,axis])','out[...,axis]=-np.cos(k[...,axis])'),
('native_shell_time_sign','V@G@(1j*G)@V','V@G@(-1j*G)@V'),
('native_photon_node_count',' for chir in [-1,1]:\n  node=np.array([0,0,chir*np.arccos(zeta)])',' for chir in [1]:\n  node=np.array([0,0,chir*np.arccos(zeta)])'),
('native_photon_electric_sign','(-np.trace(Vi@G@Vi@G@G@G','(np.trace(Vi@G@Vi@G@G@G'),
('common_coframe_opposite_node','value=np.sin(k[2])*np.sin(k[j])/vel','value=np.sin(k[j])/vel'),
('Chern_corner_orientation','orientation=np.array([1,-1,-1,1])','orientation=np.array([-1,-1,-1,1])'),
('Chern_occupied_band','u=U[...,0]','u=U[...,1]'),
('Chern_projector_curvature','/(2*np.linalg.norm(d,axis=-1)**3)','/(np.linalg.norm(d,axis=-1)**3)'),
('Kubo_energy_denominator','/(energy[1]-energy[0])**2','/(energy[1]-energy[0])**3'),
('Hall_physical_measure','H=charge2*kappa*vel/(2*np.pi**2*spacing)','H=charge2*kappa*vel/(np.pi**2*spacing)'),
('Hall_wave_contact_factor','+s.I*om*H*Cz','+s.I*om*H*Cz/2'),
('Hall_Gauss_reduction','matrix=(om**2-k2)*s.eye(3)+kk*kk.T','matrix=(om**2-k2)*s.eye(3)-kk*kk.T'),
('opposite_Hall_copy','reversed_copy=curvature(native_h(-k).conj(),-first(-k,0).conj(),-first(-k,1).conj())','reversed_copy=curvature(native_h(k),first(k,0),first(k,1))'),
]
def main():
 start=time.monotonic();original=SOURCE.read_text();sha=hashlib.sha256(original.encode()).hexdigest();out=HERE/'mutation_evidence';out.mkdir(exist_ok=True);rows=[]
 for name,old,new in MUTATIONS:
  assert original.count(old)==1,(name,'selector_count',original.count(old));compile(original.replace(old,new),'<mutation>','exec')
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
 for name,old,new in MUTATIONS:
  mutated=original.replace(old,new)
  with tempfile.TemporaryDirectory(prefix='toe-gauge-mutation-') as temp:
   p=Path(temp)/'primary.py';p.write_text(mutated);r=subprocess.run(['python3',str(p)],capture_output=True,env=env,timeout=60)
  folder=out/name;folder.mkdir(exist_ok=True)
  for fn,data in [('source.py',mutated.encode()),('stdout',r.stdout),('stderr',r.stderr)]:(folder/(fn+'.gz')).write_bytes(gzip.compress(data,mtime=0))
  effective=r.returncode!=0 and b'AssertionError' in r.stderr
  row=dict(name=name,source_sha256=sha,mutated_sha256=hashlib.sha256(mutated.encode()).hexdigest(),old=old,new=new,returncode=r.returncode,effective=effective,stderr_tail=r.stderr.decode()[-1800:]);rows.append(row)
  (folder/'manifest.json').write_text(json.dumps(row,indent=2)+'\n')
  if not effective:
   (HERE/'MUTATIONS_INCOMPLETE.json').write_text(json.dumps(rows,indent=2)+'\n');raise AssertionError((name,'no mathematical failure'))
 result=dict(source_sha256=sha,count=len(rows),all_effective=all(r['effective'] for r in rows),elapsed_seconds=time.monotonic()-start,mutations=rows)
 (HERE/'MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='mutations'}))
if __name__=='__main__':main()
