"""Personal fault injection against the exact delivered runner source."""
import ast
import hashlib
import json
from pathlib import Path
import sys
import time

RUNNER=Path('/Users/jonreilly/Documents/Codex/toe-periodic-clock-phase-20260914/scripts/periodic_finite_clock_villain_covariance_and_masslessness_2026_09_14.py')
if len(sys.argv)>1:
    RUNNER=Path(sys.argv[1])

CASES=[
 ('dual_covariance_sign','cube_duality','C/beta+D/bd','C/beta-D/bd','cube_duality',()),
 ('composite_annihilator_translate','composite_annihilator_test','(D@np.array(v))%N','(D@np.array(v)+1)%N','composite_annihilator_test',()),
 ('double_gaussian_damping','selected_link_integration','z=K*np.exp(-beta*cost/2)','z=K*np.exp(-beta*cost)','selected_link_integration',()),
 ('phase_second_derivative_sign','phase_curvature','z*np.cos(x)+z*z','z*np.cos(x)-z*z','phase_curvature',()),
 ('affine_source_curvature_sign','affine_source_test','beta+beta*beta*curvature','beta-beta*beta*curvature','affine_source_test',()),
 ('cosine_positive_mixture_weight','children','F(1,6)','F(1,3)','square_test',(1,)),
 ('retained_amplitude_ancestry','children','pa+1','pa+2','ancestry_test',()),
 ('hodge_dual_cell_translation','star_matrix','x[a]-(a in J)','x[a]-(a in I)','torus_checks',()),
 ('periodic_coloring_alias','torus_checks','(x[b]%2)*2**j','(x[b]%2)*0','torus_checks',()),
 ('chain_homotopy_orientation','edge_filling','result[(v,j,k)]=-1','result[(v,j,k)]=1','homotopy_checks',()),
 ('neighbor_distance_cutoff','constants_check','distance2<=1','distance2<=2','constants_check',()),
 ('sufficient_clock_order','constants_check','16384**2','8192**2','constants_check',()),
 ('circle_score_sign','cube_contact','off = float(','off = -float(','cube_contact',()),
 ('clock_score_sign','finite_clock_score_contact','\n        off=float(','\n        off=-float(','finite_clock_score_contact',()),
 ('slab_separation_exponent','covariance','separation - 1','separation','pf_checks',()),
 ('clock_transfer_link_count','finite_clock_transfer','coeff**4','coeff**3','finite_clock_transfer',()),
 ('directional_projector_component','spectral_and_hypothesis_checks','symbol[0]+symbol[1]','symbol[0]','spectral_and_hypothesis_checks',()),
 ('delete_winding_pair','torus_checks','if np.max(abs(winding))>1e-9:continue','if np.any(sig):continue','torus_checks',()),
]


def main():
    source=RUNNER.read_text();tree=ast.parse(source)
    functions={n.name:ast.get_source_segment(source,n) for n in tree.body if isinstance(n,ast.FunctionDef)}
    records=[]
    for name,function,old,new,invoke,args in CASES:
        original=functions[function]
        assert old in original,(name,old)
        changed=original.replace(old,new)
        assert changed!=original and source.count(original)==1
        mutant=source.replace(original,changed)
        scope={'__name__':'private_fault_injection'}
        exec(compile(mutant,str(RUNNER),'exec'),scope)
        start=time.monotonic()
        try:
            scope[invoke](*args)
        except AssertionError as error:
            record=dict(fault=name,changed_function=function,invoked=invoke,
                        outcome='AssertionError',detail=str(error)[:250],seconds=time.monotonic()-start)
        else:
            raise AssertionError(('undetected fault',name))
        records.append(record)
        print(name,record['outcome'],flush=True)
    result=dict(runner=str(RUNNER),runner_sha256=hashlib.sha256(source.encode()).hexdigest(),
                mutations=records,qualification='Personal finite fault injection, not an independent proof review or an audit verdict.')
    Path(__file__).with_name('BLOCK7_MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
