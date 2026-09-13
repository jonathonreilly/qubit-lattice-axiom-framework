"""Author mutation challenges; this harness is not an independent audit."""
from pathlib import Path
import gzip,hashlib,json,os,subprocess,tempfile,time
AUDIT_TIMEOUT_SEC = 180
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'scripts/native_weyl_canonical_metric_constraints_2026_09_13.py'
MUTATIONS=[
 ('CAR_sign','(-1)**((bits&((1<<site)-1)).bit_count())','1'),
 ('path_phase','path=(1j)**(length-1)*ap','path=(-1j)**(length-1)*ap'),
 ('path_imaginary','-path@(np.eye(dim)-signs[0]@signs[length])/2,imag','path@(np.eye(dim)-signs[0]@signs[length])/2,imag'),
 ('path_range','if d==4:continue','if d==3:continue'),
 ('Koszul_variation','(jets[b][i,a]-jets[a][i,b])/2','(jets[b][i,a]+jets[a][i,b])/2'),
 ('half_density_variation','spinvar+s.I*sum((dtrace[i]*SP[i]/4','spinvar+s.I*sum((dtrace[i]*SP[i]/8'),
 ('Darboux_spinor','s.Matrix([-pb(aval[i],z) for z in psi])','s.Matrix([pb(aval[i],z) for z in psi])'),
 ('configuration_curvature','curv=deriv+aa[i]*aa[j]-aa[j]*aa[i]','curv=deriv-aa[i]*aa[j]+aa[j]*aa[i]'),
 ('Darboux_curvature',"(s.I*psid*srho(deriv)*psi)[0]+pb(aval[i],aval[j])","(s.I*psid*srho(deriv)*psi)[0]-pb(aval[i],aval[j])"),
 ('metric_curvature_scale','-(h*k-k*h)/4)','-(h*k-k*h)/2)'),
 ('scalar_connection','*inv[cidx,j]/4','*inv[cidx,j]/8'),
 ('covariant_principal','targetgam=-.5*np.einsum','targetgam=-.25*np.einsum'),
 ('covariant_zero','+.25j*np.einsum(\'i,imn->mn\',divh,gam)','+.5j*np.einsum(\'i,imn->mn\',divh,gam)'),
 ('polar_rotation','(ev[:,None]+ev[None,:])','(2*ev[:,None]+ev[None,:])'),
 ('polar_connection','Om+AP,K','Om-AP,K'),
 ('Kosmann_rotation','-.25j*sum((gam[i]@gam[j]*exterior[i,j]','-.5j*sum((gam[i]@gam[j]*exterior[i,j]'),
 ('normal_bracket','first.append(1j*fij)','first.append(-1j*fij)'),
 ('normal_bracket_connection','targetzero-=.25j*sum','targetzero-=.5j*sum'),
 ('ADM_temporal','A-E.T@exterior@E','A+E.T@exterior@E'),
 ('metric_trace_contraction','+(2*lam-1)*s.trace(mom)*s.trace(Hess)','+(3*lam-1)*s.trace(mom)*s.trace(Hess)'),
 ('torus_trace','trace_witness,s.pi)','trace_witness,2*s.pi)'),
 ('product_normal','cvar,s.Rational(1,6)','cvar,s.Rational(1,3)'),
 ('curvature_Euler','+gginv*hn*gginv-gginv*lap','-gginv*hn*gginv-gginv*lap'),
 ('Legendre_trace','gm*pp*gm-ptr*gm/2','gm*pp*gm-ptr*gm/3'),
 ('ADM_Lagrangian','-ktr**2+rr-alpha*cc0','-ktr**2+rr+alpha*cc0'),
 ('periodic_product','curvature=-s.I*srho(kk)*field','curvature=s.I*srho(kk)*field'),
 ('spatial_node_jet','s.sin(kz)*s.sin(ky)/v,(z-s.cos(kz))/v','s.sin(kz)*s.sin(ky)/v,(z-s.cos(kz))*v'),
 ('shift_node_jet','(z-s.cos(kz))*s.sin(kz)/v]);spin','(z-s.cos(kz))*s.sin(kz)*v]);spin'),
 ('spin_node','spin=s.Matrix([s.sin(kz)/v,s.sin(kz)/v,1])','spin=s.Matrix([s.sin(kz)/v,s.sin(kz)*v,1])'),
 ('shift_second_moment',',3*chir*z)',',2*chir*z)'),
 ('spin_first_moment',',z/v)',',2*z/v)'),
 ('finite_shift','zeta*sn(u,2)-sn(u,2,2)/2','zeta*sn(u,2)+sn(u,2,2)/2'),
 ('finite_time_spin','return aa(inv@V)+aa(inv@J@E)','return 2*aa(inv@V)+aa(inv@J@E)'),
 ('finite_leading_error','leading=.75*chir*zeta','leading=.5*chir*zeta'),
]

def main():
 started=time.monotonic();original=SOURCE.read_text();sha=hashlib.sha256(original.encode()).hexdigest()
 for name,old,new in MUTATIONS:
  assert original.count(old)==1,(name,'selector_count',original.count(old))
  compile(original.replace(old,new),'<mutation>','exec')
 rows=[];out=HERE/'mutation_evidence';out.mkdir(exist_ok=True)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
 for name,old,new in MUTATIONS:
  mutated=original.replace(old,new)
  with tempfile.TemporaryDirectory(prefix='toe-canonical-mutation-') as temp:
   root=Path(temp);(root/'scripts').mkdir();p=root/'scripts'/SOURCE.name;p.write_text(mutated)
   result=subprocess.run(['python3',str(p)],capture_output=True,env=env,timeout=60)
  folder=out/name;folder.mkdir(exist_ok=True)
  for fn,data in [('source.py',mutated.encode()),('stdout',result.stdout),('stderr',result.stderr)]:
   (folder/(fn+'.gz')).write_bytes(gzip.compress(data,mtime=0))
  effective=result.returncode!=0 and b'AssertionError' in result.stderr and b'duplicate check names' not in result.stderr
  row=dict(name=name,original_sha256=sha,mutated_sha256=hashlib.sha256(mutated.encode()).hexdigest(),old=old,new=new,returncode=result.returncode,effective=effective,stderr_tail=result.stderr.decode()[-1600:])
  (folder/'manifest.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
  if not effective:
   (HERE/'MUTATIONS_INCOMPLETE.json').write_text(json.dumps(rows,indent=2)+'\n')
   raise AssertionError((name,'no mathematical failure'))
 receipt=dict(source_sha256=sha,mutation_count=len(rows),all_effective=all(r['effective'] for r in rows),elapsed_seconds=time.monotonic()-started,mutations=rows)
 (HERE/'MUTATIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k!='mutations'}))
if __name__=='__main__':main()
