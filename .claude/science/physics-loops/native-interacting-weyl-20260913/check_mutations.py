"""Reproduce deliberately corrupted copies; no source or verdict mutation."""
from pathlib import Path
import hashlib, json, subprocess, sys, tempfile

AUDIT_TIMEOUT_SEC = 60
ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT/'scripts/native_interacting_weyl_2026_09_13.py'

# Each expected failure is reached by an actual mathematical/geometry check.
MUTATIONS = [
    ('Wilson_imaginary_sign','model','W = [(-Z+s.I*X)/2,','W = [(-Z-s.I*X)/2,','complete_Laurent_Wilson_symbol'),
    ('candidate_path_shortcut','model','return [v, add(v, detour), add(w, detour), w]','return [v,w]','AssertionError'),
    ('path_phase','model','s.I**(len(vs)-2)*out','s.I**(len(vs)-1)*out','path_involution'),
    ('real_hopping_sign','model','T = s.I*ap*(bv[v]-bv[w])/2','T = -s.I*ap*(bv[v]-bv[w])/2','real_hopping_sign'),
    ('quartic_coefficient','model','hn_density = bv[0]*bv[1]/4','hn_density = bv[0]*bv[1]/2','quartic_density_interaction_dictionary'),
    ('counterterm_sign','model','hnative += lam*hn_density-nu*','hnative += lam*hn_density+nu*','full_complex_interacting_native_CAR_H'),
    ('cycle_pulse_order','model','pulse = u*ident+v*ze[1,3]*cycle','pulse = u*ident+v*cycle*ze[1,3]','scalar_branch_full_reference_identity'),
    ('spectator_parity','boundary','p = b.bit_count()%2','p = 0','extended_state_total_parity_even'),
    ('single_unsupported_seed','boundary','records = {seeds[0]:1,seeds[1]:1}','records = {seeds[0]:1}','AssertionError'),
    ('kernel_weight','boundary','s.Rational(3,4) if a==1 else','s.Rational(1,2) if a==1 else','AssertionError'),
    ('boundary_omitted','boundary','Hlarge = Hsmall+bonds[1]','Hlarge = Hsmall','boundary_difference_really_starts_at_distance_two'),
    ('bond_chain_count','boundary','count == 6*11**(length-1)','count == 6*12**(length-1)','AssertionError'),
    ('Poisson_orientation','boundary','-2*s.pi*s.I*s.residue','2*s.pi*s.I*s.residue','Poisson_positive_energy_contour_residue'),
    ('clock_transform','boundary','gamma*s.exp(-12*gamma*wait)','gamma*s.exp(-11*gamma*wait)','actual_clock_Laplace_transform'),
]


def run():
    source = SOURCE.read_text()
    rows = []
    with tempfile.TemporaryDirectory(prefix='native-weyl-mutations-') as directory:
        for name,family,old,new,needle in MUTATIONS:
            assert source.count(old)==1,(name,source.count(old))
            changed = source.replace(old,new)
            path = Path(directory)/(name+'.py')
            path.write_text(changed)
            code = ("import importlib.util; "
                    "spec=importlib.util.spec_from_file_location('candidate',"+repr(str(path))+"); "
                    "mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); "
                    "mod.run_"+family+"()")
            result = subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,timeout=20)
            row = {'name':name,'family':family,'old':old,'new':new,
                   'mutated_sha256':hashlib.sha256(changed.encode()).hexdigest(),
                   'exit_code':result.returncode,'stderr':result.stderr,
                   'expected_failure_text':needle}
            rows.append(row)
            assert result.returncode!=0 and needle in result.stderr.splitlines()[-1],row
    out = {'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
           'effective_mutations':len(rows),'mutations':rows}
    (Path(__file__).resolve().parent/'MUTATIONS.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Deliberate mutations detected:',len(rows))


if __name__=='__main__':
    run()
