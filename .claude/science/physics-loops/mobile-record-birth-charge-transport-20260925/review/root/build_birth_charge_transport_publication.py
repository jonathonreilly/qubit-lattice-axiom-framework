"""One-time clean publication writer for the personally derived 42+43 unit."""
from pathlib import Path
import ast, hashlib, json, re, subprocess
E=Path(__file__).resolve().parent; R=E/'birth-charge-transport-publication'
base='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
branch='codex/mobile-record-birth-charge-and-grouping-dynamics-20260925'
packet='.claude/science/physics-loops/mobile-record-birth-charge-transport-20260925'
note='docs/ORIGINAL_BIRTH_CHARGE_AND_GROUPING_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-25.md'
runner='scripts/original_birth_charge_and_grouping_dynamics_2026_09_25.py'
out='outputs/native_birth_charge_transport_20260925'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *args:subprocess.check_output(['git',*args],cwd=R,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch and git('status','--porcelain')==''
specs=[('native-birth-charge-cluster-personal','ORIGINAL_BIRTH_CHARGE_CLUSTERS_ROOT.md','061b603af09865b1f8673d2332816849f799f504dbadfe54b205e53be9077186'),
 ('native-birth-cluster-transport-personal','ORIGINAL_BIRTH_CLUSTER_TRANSPORT_ROOT.md','897ee094e3766f845645260bc7d6f121ed98053d585fd6db04993db81efbeae6')]
for directory,source,h in specs:
 d=E/directory;assert sha(d/'AUTHOR_SEAL.json')==h
 for row in json.loads((d/'AUTHOR_SEAL.json').read_text())['members']:
  assert sha(d/row['path'])==row['sha256'] and (d/row['path']).stat().st_size==row['bytes']
parents=[]
for row in json.loads((E/specs[0][0]/'SOURCE_PINS.json').read_text())['sources']:
 p=row['git_path'];assert sha(R/p)==row['sha256'];parents.append(p)
replacements=[[
 ('No independent check\nof this candidate is claimed.', 'Separate scoped PRE and POST checks are complete; no retained audit status\nis claimed.'),
 ('h=KD-2delta Q, the original', 'h=KD-2delta Q, where Q is the sum of S_xy^* S_xy over unordered\nOVERLAPPING A-star pairs, S_xy=F_y F_x P, the original'),
 ('On the full output span define', 'On the closed span of all individual branch images define'),
 ('On the output span let Z be q_a restricted to\nthat span', 'On that individual-branch span let Z be q_a restricted to\nthat span (not necessarily the range of the coherent output isometry)'),
 ('Consequently the first time is exponential with that rate when kappa>0;', 'Consequently the first time is exponential when its total rate Gamma_0>0;'),
 ('If kappa=0 there is no event to condition on.', 'If Gamma_0=0 there is no event to condition on.'),
 ('There is no independent\ncandidate42 result yet, and no result from independent40/41 was read for this\ncandidate.', 'This historical author seal preceded the separate candidate42 checks.\nNo result from independent40/41 was read for this candidate.')
 ],[
 ('This author packet is not independently\nchecked at its creation and is not an audit disposition or an observed particle\nprediction.', 'This author packet was not independently checked at its creation. Separate\nscoped PRE and POST checks are now complete; they confer no retained audit\nstatus or observed particle prediction.'),
 ('The denominators follow from the five distinct outgoing matter words for each', 'An actually occurring conditioned mark requires kappa>0. At kappa=0 these\nnormalized bare-B vectors still define supplied states, but no such event occurs.\nThe denominators follow from the five distinct outgoing matter words for each')
 ]]
bodies=[]
for (directory,source,h),changes in zip(specs,replacements):
 t=(E/directory/source).read_text()
 for old,new in changes: assert t.count(old)==1,(source,old);t=t.replace(old,new)
 bodies.append(re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',t,flags=re.M))
header='---\nclaim_id: '+Path(note).stem.lower()+'\nclaim_type: bounded_theorem\nclaim_scope: "Original first-birth static charge law and supplied-input failure of exact nearest-neighbor grouping invariance under the full generator; no selected particle, measured structure factor or lifetime."\nupstream_dependencies:\n'
header+=''.join('  - '+Path(p).stem.lower()+'\n' for p in parents)
header+='runner: '+runner+'\n---\n\n'
front='''**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Original birth charge and subsequent grouping dynamics

The original formation instrument makes two regional Gauss-charge sums of
exactly -1 and +1. This result holds for every normal incoming field in the
specified minimum-number matter sector. It gives an explicit static charge
distribution, including a cubic orientation-averaged structure factor
S(k)=(4/3) sum_i (1-cos(k_i)). The original first-event clock is scalar on that
sector, so the same charge law holds at the actual randomly timed first birth.
These statements precede any fit to data and still require a physical
preparation, units and measurement coupling before an observational comparison.

The smallest nearest-neighbor charge grouping does not then remain exactly
closed under the full law. For an original birth from a supplied immediately
pre-mark zero-electric input, a complete matter/field target outside every
such grouping has probabilities (16/5) delta^2 t^2+O(t^3) for the resolved
minus sign and (8/5) delta^2 t^2+O(t^3) for the coherent edge instrument.
The finite remainder is explicit in ||G^2 psi||. This rules out exact closure
of that particular grouping, while leaving larger dressings and approximate
collective particles open.

The two preparation statements differ. The static charge law is independent
of the incoming field and therefore applies at the actual first event after
waiting. The displayed transport coefficients require zero electric field
immediately before the mark. This publication does not derive that field
preparation at a randomly timed event and does not silently substitute it.
Nor does a small-time expansion establish a lifetime of order delta^-1.

The full matter/field Hamiltonian, vacancy-gated electric term, integer Gauss
fields and original formation instrument remain present throughout. Resolved
sign channels and the stipulated unnormalized coherent sum on each separate
edge have the same loss operator but different recycling maps. No field-only
postbirth limit or coherent sum over distinct recorded edges is used.

The root personally derived both arguments and their decisive controls.
Each separate checker sealed a PRE before the corresponding author release
and a POST afterward. Root read the proofs, new programs, compact results and
failure records and freshly replayed the read-only evidence checks. No required
mathematical repair was found within these claims. Presentation qualifications
make the positive total first-event rate, overlapping-star sum, branch-span
domain of the sign operator, and zero-rate event endpoint explicit.
Publication correspondence is a released-source check, not another blind proof.

The charge PRE's additional irregular-graph laws, resolved-sign Fourier cases,
sixth-order error and coherence counterexamples remain separately attributed.
The dynamics PRE supplies another positive-sign target, full outside-grouping
quadratic coefficients on L=4,6,8, loss means and a coarse finite-time bound.
Its positive-sign quadratic escape concerns a different target or the whole
outside projector; it does not contradict the quartic upper order for the one
target in the personal argument. Those PRE additions are not retroactive root
claims. The POST comparisons and full immutable histories accompany this unit.

## Complete charge argument

'''
footer='''
## Reproduction and observation boundary

The primary runner copies the exact two personally sealed programs and the
declared shared geometry helper into a temporary directory, executes them,
and preserves both complete result streams. Exact integer and rational
controls corroborate the displayed analytic proofs. Finite graphs do not
replace the all-field isometry argument or the all-L target/domain proof.
The helper reuse is explicit and gives no additional independence.

No finite-spin stopping-time or derivative transfer, selected vacuum, physical
charge unit, measured structure factor, mass, force, detector response or
empirical agreement is claimed. The next observation obligation is a prepared
or selected full-state packet with controlled transport and interaction,
followed by justified units and readout. No axiom, audit verdict or merge is
requested. The original failed shortcuts and receipt qualifications remain
available without rewriting their historical records.

Direct conditional parents:

'''+''.join('- ['+Path(p).stem+']('+Path(p).name+').\n' for p in parents)
(R/note).write_text(header+front+bodies[0]+'\n## Complete subsequent-dynamics argument\n\n'+bodies[1]+footer)
runtime=[]
for directory,name in [(specs[0][0],'charge_cluster_controls.py'),(specs[1][0],'cluster_escape_controls.py'),(specs[1][0],'birth_geometry.py')]:
 p=packet+'/runtime/'+name; (R/p).parent.mkdir(parents=True,exist_ok=True);(R/p).write_bytes((E/directory/name).read_bytes());runtime.append(p)
assert sha(R/runtime[0])==sha(R/runtime[2])=='4b1b273bb5046fab5e4f6dc307c650d9be9cba8df25b584020fcaadaa0d5ce6e'
wrapper='#!/usr/bin/env python3\n"""Exact-source original birth charge and grouping dynamics controls."""\n'
wrapper+='AUDIT_TIMEOUT_SEC = 120\nAUDIT_INPUT_PATHS = '+repr(tuple([note,*parents,*runtime]))+'\n'
wrapper+='OUTPUT_DIRECTORY = '+repr(out)+'\nRUNTIMES = '+repr(tuple(runtime))+'\n'
wrapper+=r'''
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter();artifacts=[]
    sha=lambda raw:hashlib.sha256(raw).hexdigest()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='birth-charge-transport-') as tmp:
        for rel in RUNTIMES:(Path(tmp)/Path(rel).name).write_bytes((root/rel).read_bytes())
        for rel,label in zip(RUNTIMES[:2],('charge','transport')):
            program=Path(tmp)/Path(rel).name
            run=subprocess.run([sys.executable,'-B',str(program)],cwd=tmp,capture_output=True,env=env)
            (out/(label+'.stdout.json')).write_bytes(run.stdout)
            (out/(label+'.stderr.txt')).write_bytes(run.stderr)
            if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
            data=json.loads(run.stdout)
            assert data['source_sha256']==sha(program.read_bytes())
            if label=='charge':assert data['all_assertions_passed'] and data['counts']['primitive_paths']==8448
            else:
                assert data['personal42_helper_sha256']==sha((Path(tmp)/'birth_geometry.py').read_bytes())
                assert len(data['results'])==2 and all(r['all_integer_Gauss_and_coefficient_assertions'] for r in data['results'])
            artifacts.append(dict(label=label,path=OUTPUT_DIRECTORY+'/'+label+'.stdout.json',
                sha256=sha(run.stdout),bytes=len(run.stdout),exit_code=0,stderr_bytes=0,
                runtime_source_sha256=sha(program.read_bytes())))
    result=dict(scope='Conditional original-birth charge and supplied-input grouping dynamics; no new independence, particle lifetime, units or empirical claim.',
        source_sha256=sha(Path(__file__).read_bytes()),artifacts=artifacts,
        runtime_sha256={rel:sha((root/rel).read_bytes()) for rel in RUNTIMES},
        elapsed_seconds=time.perf_counter()-tick,all_assertions_passed=True)
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'BIRTH_CHARGE_TRANSPORT_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
'''
ast.parse(wrapper);(R/runner).write_text(wrapper)
manifest=dict(base_revision=base,base_branch='main',branch=branch,packet=packet,note=note,runner=runner,runtime=runtime,
 output_directory=out,parent_paths=parents,source_notes=[str(E/d/n) for d,n,h in specs],
 cache='logs/runner-cache/original_birth_charge_and_grouping_dynamics_2026_09_25.txt',
 result=out+'/BIRTH_CHARGE_TRANSPORT_PUBLIC_RESULTS.json',
 presentation_replacements=[[dict(old=a,new=b) for a,b in rr] for rr in replacements],heading_level_increment=2,
 source_files_sha256={p:sha(R/p) for p in [note,runner,*runtime,*parents]})
with (E/'BIRTH_CHARGE_TRANSPORT_PUBLICATION_WORKING_SOURCES.json').open('x') as f:json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps(manifest,indent=2))
