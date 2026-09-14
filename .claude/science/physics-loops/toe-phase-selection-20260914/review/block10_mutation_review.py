"""Personal finite fault challenges; neither independent review nor audit."""
import ast
import hashlib
import json
import sys
import time
from pathlib import Path

RUNNER=Path(__file__).parents[1]/'block10_gaussian_maxwell_check.py'
if len(sys.argv)>1:RUNNER=Path(sys.argv[1])

CASES=[
 ('clock_curl_orientation','clock_lift_and_score','[[1,-1,0],[0,1,-1],[-1,0,1]]','[[1,1,0],[0,1,-1],[-1,0,1]]','clock_lift_and_score'),
 ('dual_temperature_factor','clock_lift_and_score','N*N/(4*np.pi*np.pi*beta)','N*N/(2*np.pi*np.pi*beta)','clock_lift_and_score'),
 ('lose_clock_fiber','clock_lift_and_score','N*math.exp(logZ)','math.exp(logZ)','clock_lift_and_score'),
 ('score_sign','clock_lift_and_score','Y=-score/math.sqrt(beta)','Y=score/math.sqrt(beta)','clock_lift_and_score'),
 ('noise_l1_accumulation','clock_lift_and_score','var@(h*h)','var@np.full(3,h.sum()**2)','clock_lift_and_score'),
 ('drop_conditional_variance','clock_lift_and_score','+np.diag(config@var)','+0*np.diag(config@var)','clock_lift_and_score'),
 ('dual_covariance_sign','clock_lift_and_score','cn/beta+CX,np.eye(3)','cn/beta-CX,np.eye(3)','clock_lift_and_score'),
 ('completed_square_source_scale','centered_theta_and_affine_control','z-math.sqrt(sigma)*h','z-sigma*h','centered_theta_and_affine_control'),
 ('affine_shift_removed','centered_theta_and_affine_control','2*np.arange(-10,11)+1','2*np.arange(-10,11)','centered_theta_and_affine_control'),
 ('gaussian_source_normalization','exact_plane_gaussian_approach','source=z@h/math.sqrt(sigma)','source=z@h/sigma','exact_plane_gaussian_approach'),
 ('drop_between_coset_covariance','tilted_coset_total_covariance','between=mean_second-np.outer(mean,mean)','between=0*(mean_second-np.outer(mean,mean))','tilted_coset_total_covariance'),
 ('tilted_hessian_source_sign','tilted_coset_total_covariance','exponent=base+tilt*source','exponent=base-tilt*source','tilted_coset_total_covariance'),
 ('wrong_exterior_orientation','exterior_one','matrix[row,mu]=-p[nu]','matrix[row,mu]=p[nu]','bianchi_and_contact'),
 ('wrong_projector_normalization','twoform_projection','float(np.vdot(p,p).real)','float(np.vdot(p,p).real)**2','os_electric_magnetic_reconstruction'),
 ('missing_midpoint_phase','midpoint_and_cell_average','edge_phase=np.diag(np.exp(1j*k/2))','edge_phase=np.eye(4)','midpoint_and_cell_average'),
 ('drop_cell_average_factor','midpoint_and_cell_average','sinc=float(np.prod(np.sinc(k/(2*np.pi))))','sinc=1.0','midpoint_and_cell_average'),
 ('wrong_cell_field_scaling','midpoint_and_cell_average','a*a/(ell*ell)','a/(ell*ell)','midpoint_and_cell_average'),
 ('wrong_B_orientation','os_electric_magnetic_reconstruction','change[4,4]=-1','change[4,4]=1','os_electric_magnetic_reconstruction'),
 ('electric_reflection_even','os_electric_magnetic_reconstruction','np.diag([-1,-1,-1,1,1,1])','np.eye(6)','os_electric_magnetic_reconstruction'),
 ('cross_residue_sign','os_electric_magnetic_reconstruction','M=-1j*C/r','M=1j*C/r','os_electric_magnetic_reconstruction'),
 ('drop_electric_magnetic_cross','os_electric_magnetic_reconstruction','gram=np.block([[PT,M],[M,PT]])','gram=np.block([[PT,0*M],[0*M,PT]])','os_electric_magnetic_reconstruction'),
 ('keep_wrong_EE_noncontact_sign','os_electric_magnetic_reconstruction','[[-r*r*PT*i0,-C*i1]','[[r*r*PT*i0,-C*i1]','os_electric_magnetic_reconstruction'),
 ('quadratic_dispersion','os_electric_magnetic_reconstruction','spectral=math.exp(-t*r)','spectral=math.exp(-t*r*r)','os_electric_magnetic_reconstruction'),
 ('euclidean_divergence_set_zero','bianchi_and_contact','contact=D.conj().T@P@D','contact=0*(D.conj().T@P@D)','bianchi_and_contact'),
 ('tail_factor_four_missing','tail_constants_and_scaling','integrated=4*(','integrated=1*(','tail_constants_and_scaling'),
 ('supplied_clock_order_halved','tail_constants_and_scaling','N=8*beta','N=4*beta','tail_constants_and_scaling'),
]


def main():
    source=RUNNER.read_text();tree=ast.parse(source)
    functions={node.name:ast.get_source_segment(source,node) for node in tree.body if isinstance(node,ast.FunctionDef)}
    records=[]
    for name,function,old,new,invoke in CASES:
        original=functions[function];assert original.count(old)==1,(name,original.count(old))
        mutant=source.replace(original,original.replace(old,new))
        namespace={'__name__':'personal_mutation','__file__':str(RUNNER)}
        exec(compile(mutant,str(RUNNER),'exec'),namespace)
        start=time.monotonic()
        try:namespace[invoke]()
        except AssertionError as error:
            records.append(dict(fault=name,function=function,invoked=invoke,old=old,new=new,
                                outcome='AssertionError',detail=str(error)[:220],seconds=time.monotonic()-start))
        else:raise AssertionError(('UNDETECTED',name))
        print(name,'detected',flush=True)
    result=dict(runner=str(RUNNER),runner_sha256=hashlib.sha256(source.encode()).hexdigest(),
                qualification='Personal finite mathematical challenges, not independent proof review or universal proof execution.',
                faults=records)
    Path(__file__).with_name('BLOCK10_MUTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
