"""Personal finite mathematical fault checks; not independent review."""
import ast
import hashlib
import json
import sys
import time
from pathlib import Path

RUNNER=Path(__file__).parents[1]/'block11_direct_wilson_check.py'
if len(sys.argv)>1:RUNNER=Path(sys.argv[1])
CASES=[
 ('forward_coboundary_direction','coboundary','np.roll(field[J],-1,axis=axis)','np.roll(field[J],1,axis=axis)','integral_cochain_and_short_vectors'),
 ('adjoint_difference_sign','adjoint','np.roll(values,1,axis=axis)-values','values-np.roll(values,1,axis=axis)','integral_cochain_and_short_vectors'),
 ('circle_anchor','circle_projection','np.take(values,[0],axis=axis)','np.take(values,[1],axis=axis)','integral_cochain_and_short_vectors'),
 ('period_cocycle_location','circle_projection','slice(L-1,L)','slice(0,1)','integral_cochain_and_short_vectors'),
 ('contraction_endpoint','contraction','np.cumsum(values,axis=axis)-values','np.cumsum(values,axis=axis)+values','integral_cochain_and_short_vectors'),
 ('tensor_koszul_sign','contraction','(-1)**position*shifted','shifted','integral_cochain_and_short_vectors'),
 ('harmonic_volume_factor','integral_cochain_and_short_vectors','L**4*float(values.mean())**2','L**2*float(values.mean())**2','integral_cochain_and_short_vectors'),
 ('short_vector_operator_bound','integral_cochain_and_short_vectors','integernorm/4-1e-12','integernorm/2-1e-12','integral_cochain_and_short_vectors'),
 ('packing_dimension_dropped','packing_and_parameters','rank*math.log(2*k+3)','math.log(2*k+3)','packing_and_parameters'),
 ('theta_tail_exponent','packing_and_parameters','bound=2*math.exp(-t/2)','bound=2*math.exp(-2*t)','packing_and_parameters'),
 ('dual_temperature_scale','packing_and_parameters','N*N/(4*np.pi*np.pi*beta)','N*N/(2*np.pi*np.pi*beta)','packing_and_parameters'),
 ('perpendicular_coset_energy','lattice_source_and_coset_mixture','zero_log-N*N*k*k/(6*sigma)','zero_log-N*N*k*k/(3*sigma)','lattice_source_and_coset_mixture'),
 ('poisson_character_source_factor','lattice_source_and_coset_mixture','+2*np.pi*math.sqrt(sigma)*(dualpoints@he)','+4*np.pi*math.sqrt(sigma)*(dualpoints@he)','lattice_source_and_coset_mixture'),
 ('affine_poisson_phase_sign','shifted_theta_relative_sources','np.exp(2j*np.pi*(dualz@b))','np.exp(-2j*np.pi*(dualz@b))','shifted_theta_relative_sources'),
 ('omit_affine_theta_denominator','shifted_theta_relative_sources','gaussian*numerator/denominator','gaussian*numerator','shifted_theta_relative_sources'),
 ('fractional_wilson_charge','clock_wilson_characters','q1=round(.8*math.sqrt(beta))','q1=.8*math.sqrt(beta)','clock_wilson_characters'),
 ('clock_charge_alias','clock_wilson_characters','np.exp(1j*N*angles[i])','np.exp(1j*N/2*angles[i])','clock_wilson_characters'),
 ('green_jump_rate','infinite_green','ive(abs(n),2*t)','ive(abs(n),t)','green_and_disjoint_loops'),
 ('periodic_zero_mode','periodic_green','out=np.zeros_like(symbol)','out=np.ones_like(symbol)','green_and_disjoint_loops'),
 ('heat_zero_mode_subtraction','green_and_disjoint_loops','np.prod(terms)-1/4**4','np.prod(terms)','green_and_disjoint_loops'),
 ('loop_edge_orientation','rectangle_current','tuple(x),direction','tuple(x),abs(direction)','green_and_disjoint_loops'),
 ('current_component_contraction','green_and_disjoint_loops','if mu==nu:cross+=','if mu!=nu:cross+=','green_and_disjoint_loops'),
 ('coulomb_kernel_normalization','time_integral','/(2*np.pi*np.pi)','/(4*np.pi*np.pi)','coulomb_time_and_charge_signs'),
 ('closing_paths_omitted','coulomb_time_and_charge_signs','loop_formula+=2*time_integral(A,R)-2*time_integral(A,math.sqrt(T*T+R*R))','loop_formula+=0','coulomb_time_and_charge_signs'),
 ('charge_interaction_sign','coulomb_time_and_charge_signs','-math.log(joint/separate)','math.log(joint/separate)','coulomb_time_and_charge_signs'),
 ('physical_score_sign','clock_lift_and_score','Y=-score/math.sqrt(beta)','Y=score/math.sqrt(beta)','clock_lift_and_score'),
 ('cell_average_factor','midpoint_and_cell_average','sinc=float(np.prod(np.sinc(k/(2*np.pi))))','sinc=1.0','midpoint_and_cell_average'),
 ('electric_reflection_sign','os_electric_magnetic_reconstruction','np.diag([-1,-1,-1,1,1,1])','np.eye(6)','os_electric_magnetic_reconstruction'),
 ('electric_magnetic_cross_sign','os_electric_magnetic_reconstruction','M=-1j*C/r','M=1j*C/r','os_electric_magnetic_reconstruction'),
 ('quadratic_physical_dispersion','os_electric_magnetic_reconstruction','spectral=math.exp(-t*r)','spectral=math.exp(-t*r*r)','os_electric_magnetic_reconstruction'),
]


def main():
    source=RUNNER.read_text();tree=ast.parse(source)
    functions={n.name:ast.get_source_segment(source,n) for n in tree.body if isinstance(n,ast.FunctionDef)}
    records=[]
    for name,function,old,new,invoke in CASES:
        original=functions[function];assert original.count(old)==1,(name,original.count(old))
        mutant=source.replace(original,original.replace(old,new))
        namespace={'__name__':'personal_mutation','__file__':str(RUNNER)}
        exec(compile(mutant,str(RUNNER),'exec'),namespace);start=time.monotonic()
        try:namespace[invoke]()
        except AssertionError as error:
            records.append(dict(fault=name,function=function,invoked=invoke,old=old,new=new,outcome='AssertionError',detail=str(error)[:240],seconds=time.monotonic()-start))
        else:raise AssertionError(('UNDETECTED',name))
        print(name,'detected',flush=True)
    result=dict(runner=str(RUNNER),runner_sha256=hashlib.sha256(source.encode()).hexdigest(),faults=records,qualification='Personal finite fault challenges. Not independent review or execution of the arbitrary-volume proof.')
    Path(__file__).with_name('BLOCK11_MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
