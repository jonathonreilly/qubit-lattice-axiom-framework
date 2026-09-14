"""Personal source-bound mathematical fault challenges; not an audit."""
import ast,hashlib,json,time,sys
from pathlib import Path
RUNNER=Path('/Users/jonreilly/Documents/Codex/toe-clock-penalty-normal-form-20260914/scripts/clock_penalty_local_normal_form_and_ground_state_limit_2026_09_14.py')
if len(sys.argv)>1:RUNNER=Path(sys.argv[1])
CASES=[
 ('face_orientation','geometry','((a,shift(x,b)),-1)','((a,shift(x,b)),1)','geometry_and_grade_locality'),
 ('cube_orientation','geometry','D[c,fi[aa,shift(x,a)]] += (-1)**a','D[c,fi[aa,shift(x,a)]] += 1','geometry_and_grade_locality'),
 ('lose_cube_edge_incidence','geometry_and_grade_locality','cube_edge=(cube_face@face_edge)>0','cube_edge=(cube_face@face_edge)>2','geometry_and_grade_locality'),
 ('linear_instead_of_squared_charge','cube_model','N=Q*Q','N=Q','matrix_normal_form'),
 ('wrong_mismatch_penalty_scale','cube_model','-mu*int(m@m)','-mu*int(m@m)/9','matrix_normal_form'),
 ('lost_original_link_multiplicity','cube_model','for l in range(len(edges)):','for l in range(len(edges)//2):','matrix_normal_form'),
 ('inverse_commutator_sign','matrix_normal_form','inverse=np.divide(off,grades,','inverse=-np.divide(off,grades,','matrix_normal_form'),
 ('absolute_energy_denominator','matrix_normal_form','inverse=np.divide(off,grades,','inverse=np.divide(off,abs(grades),','matrix_normal_form'),
 ('positive_second_effective_correction','matrix_normal_form','C=-B[np.ix_(p,q)]','C=B[np.ix_(p,q)]','matrix_normal_form'),
 ('delete_second_harmonic','matrix_normal_form','double=math.exp(-degree*.8)*(Z@Z+Z.T@Z.T)','double=0*(Z@Z+Z.T@Z.T)','matrix_normal_form'),
 ('reverse_iterated_rotation','matrix_normal_form','transform=expm(generator)','transform=expm(-generator)','matrix_normal_form'),
 ('wrong_prepared_dressing','matrix_normal_form','psi=uall.T@phi','psi=uall@phi','matrix_normal_form'),
 ('squared_penalty_equals_each_charge','equal_penalty_is_not_equal_charge','np.any(qp!=Q,axis=1)','np.all(qp==Q,axis=1)','equal_penalty_is_not_equal_charge'),
 ('delete_wall_energy','logical_controls','energy[old]+lam*(old!=s)-h*f*s','energy[old]-h*f*s','logical_controls'),
 ('ignore_global_rotation_accumulation','logical_controls','1_000_000*math.log1p(-p)','math.log1p(-p)','logical_controls'),
 ('missing_lie_schwinger_weight','local_algebra_checks','integral+=w/2*u*','integral+=w/2*','local_algebra_checks'),
 ('wrong_first_majorant','local_algebra_checks','Fraction(16,128-16)','Fraction(16,128+16)','local_algebra_checks'),
 ('wrong_iterated_majorant','local_algebra_checks','Fraction(4*(2+1),32-4)','Fraction(4*(2+1),32+4)','local_algebra_checks'),
]

def main():
 source=RUNNER.read_text();tree=ast.parse(source)
 functions={n.name:ast.get_source_segment(source,n) for n in tree.body if isinstance(n,ast.FunctionDef)}
 records=[]
 for name,function,old,new,invoke in CASES:
  original=functions[function];assert old in original,(name,old)
  mutant=source.replace(original,original.replace(old,new))
  scope={'__name__':'personal_mutation','__file__':str(RUNNER)}
  exec(compile(mutant,str(RUNNER),'exec'),scope)
  start=time.monotonic()
  try:scope[invoke]()
  except AssertionError as error:
   row=dict(fault=name,changed_function=function,old=old,new=new,invoked=invoke,outcome='AssertionError',detail=str(error)[:250],seconds=time.monotonic()-start)
  else:raise AssertionError(('UNDETECTED',name))
  records.append(row);print(name,row['outcome'],flush=True)
 result=dict(runner=str(RUNNER),runner_sha256=hashlib.sha256(source.encode()).hexdigest(),mutations=records,qualification='Personal finite mathematical fault challenges. Neither independent review nor arbitrary-volume proof execution.')
 Path(__file__).with_name('BLOCK9_MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
