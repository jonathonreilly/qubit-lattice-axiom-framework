"""Personal finite scientific fault injection; source-bound, no audit verdict."""
import ast,hashlib,json,time,sys
from pathlib import Path
RUNNER=Path('/Users/jonreilly/Documents/Codex/toe-principal-flux-transfer-20260914/scripts/principal_flux_positive_gaussian_transfer_and_hamiltonian_limit_2026_09_14.py')
if len(sys.argv)>1:RUNNER=Path(sys.argv[1])
CASES=[
 ('principal_difference_orientation','single_square_checks','flux[:, None]-flux[None, :]','flux[:, None]+flux[None, :]','single_square_checks'),
 ('drop_periodic_integer_images','single_square_checks','minlength=n**e) for db','minlength=n**e) for db','unused'),
 ('wrong_penalty_scale','single_square_checks','(db-curl)**2/n**2','(db-curl)**2','single_square_checks'),
 ('row_normalize_penalized_kernel','single_square_checks','full=lookup[flux_delta+2,residue_delta]','full=lookup[flux_delta+2,residue_delta]\n            full=full/full.sum(axis=0)[None,:]','single_square_checks'),
 ('non_gaussian_integer_lift_power','theta','q**(j*j)','q**j','single_square_checks'),
 ('drop_original_link_multiplicity','square_generator_multiplicity_check','a[i,j]+=4*','a[i,j]+=1*','square_generator_multiplicity_check'),
 ('cube_incidence_orientation','cube_geometry','d[0,faces.index((axes,tuple(high)))]+=(-1)**axis','d[0,faces.index((axes,tuple(high)))]+=1','cube_checks'),
 ('fixed_diagonal_normalization','cube_checks','he=2*t*e*np.eye(size)','he=t*e*np.eye(size)','cube_checks'),
 ('logarithm_coefficient_sign','cube_checks','ck=matrices[2]-a@a/2+2*e*np.eye(size)','ck=matrices[2]+a@a/2+2*e*np.eye(size)','cube_checks'),
 ('delete_shared_face_interactions','cube_checks','if np.any((f[:,l]!=0)&(f[:,r]!=0)):','if False:','cube_checks'),
 ('logarithm_correction_inferred_sign','cube_checks','effective-h+eps*t*t*ck','effective-h-eps*t*t*ck','cube_checks'),
 ('spatial_half_factor_sign','cube_checks','s=np.exp(-eps*v/2)','s=np.exp(eps*v/2)','cube_checks'),
 ('product_time_mismatch','cube_checks','np.linalg.matrix_power(transfer,steps)','np.linalg.matrix_power(transfer,2*steps)','cube_checks'),
 ('strip_mismatch_power','exact_strip_checks','penalty=np.sum(mismatch*mismatch,axis=1)','penalty=np.sum(np.abs(mismatch),axis=1)','exact_strip_checks'),
 ('strip_laurent_incidence','exact_strip_checks','[(0,-1,1)]','[(0,1,1)]','exact_strip_checks'),
 ('wilson_time_scaling','elementary_scaling_checks','beta_w=2/3*math.log(1/q)','beta_w=3/2*math.log(1/q)','elementary_scaling_checks'),
]
# The image-deletion fault acts on the full-coordinate sum only, leaving the
# separate physical convolution as its challenger.
CASES[1]=('drop_periodic_integer_images','single_square_checks','q**energy*np.exp(-mu*(db-curl)**2/n**2)','q**energy*np.exp(-mu*(db-curl)**2/n**2)*np.all(np.abs(lifts)<=1,axis=1)','single_square_checks')
# Exact literal for the last internal strip-link factor.
CASES[14]=('strip_laurent_incidence','exact_strip_checks','[(-1,1,0),(0,-1,1)]','[(-1,1,0),(0,1,1)]','exact_strip_checks')

CASES += [('spatial_cosine_scale','cube_checks','v=1.5*kappa*','v=2*kappa*','cube_checks'), ('wrong_scale_control_collapses','cube_checks','hewrong[i,j]-=t*np.exp(-mu*(delta@delta))','hewrong[i,j]-=t*np.exp(-mu*(delta@delta)/9)','cube_checks')]

def main():
 source=RUNNER.read_text();tree=ast.parse(source)
 functions={node.name:ast.get_source_segment(source,node) for node in tree.body if isinstance(node,ast.FunctionDef)}
 records=[]
 for name,function,old,new,invoke in CASES:
  original=functions[function]
  assert old in original,(name,old)
  changed=original.replace(old,new)
  assert changed!=original and source.count(original)==1
  mutant=source.replace(original,changed)
  scope={'__name__':'personal_mutation','__file__':str(RUNNER)}
  exec(compile(mutant,str(RUNNER),'exec'),scope)
  start=time.monotonic()
  try:scope[invoke]()
  except AssertionError as error:
   record=dict(fault=name,changed_function=function,old=old,new=new,invoked=invoke,outcome='AssertionError',detail=str(error)[:250],seconds=time.monotonic()-start)
  else:raise AssertionError(('UNDETECTED',name))
  records.append(record);print(name,record['outcome'],flush=True)
 result=dict(runner=str(RUNNER),runner_sha256=hashlib.sha256(source.encode()).hexdigest(),mutations=records,qualification='Personal finite challenge by changed mathematical mechanisms, not independent review or a phase proof.')
 Path(__file__).with_name('BLOCK8_MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
