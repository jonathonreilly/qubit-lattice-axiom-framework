"""One-time clean publication writer for the personally derived 46+47 unit."""
from pathlib import Path
import ast, hashlib, json, re, subprocess
E=Path(__file__).resolve().parent; R=E/'local-charge-observation-publication'
base='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
branch='codex/mobile-record-local-charge-observation-20260925'
packet='.claude/science/physics-loops/mobile-record-local-charge-observation-20260925'
note='docs/ORIGINAL_LOCAL_CHARGE_CURRENT_AND_FINITE_TIME_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-25.md'
runner='scripts/original_local_charge_current_and_finite_time_covariance_2026_09_25.py'
out='outputs/native_local_charge_covariance_20260925'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *args:subprocess.check_output(['git',*args],cwd=R,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch and git('status','--porcelain')==''
for directory,sealhash in [('native-charge-current-noise-personal','57208448fe5e06b459aaef80b7a044c848954d9ba386d7643baaba20787f604d'),('native-charge-finite-time-personal','1f2cb7ce4c8e8b5491a2e35aae215f7e0533d6119343074173ef13dc877d8ba8')]:
 d=E/directory;assert sha(d/'AUTHOR_SEAL.json')==sealhash
 for row in json.loads((d/'AUTHOR_SEAL.json').read_text())['members']:
  assert sha(d/row['path'])==row['sha256'] and (d/row['path']).stat().st_size==row['bytes']
sources=[E/'native-charge-current-noise-qualified/CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md',E/'native-charge-finite-time-personal/LOCAL_CHARGE_FINITE_TIME_COVARIANCE_ROOT.md']
assert [sha(p) for p in sources]==['e1447ae3d5a5cad6c756dc1b2079e0bee6e275c53bc8f9a9d926037168c9cba4','9a83191276a1a0380158ef88961c1d36b0d82c9cd645210739c999c4568f464a']
parent_stems=['LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS','LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT','FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES']
parents=['docs/'+s+'_BOUNDED_THEOREM_NOTE_2026-09-24.md' for s in parent_stems]
assert [sha(R/p) for p in parents]==['7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b','2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516']
changes=[[
 ('2026-09-25. Personal conditional theorem candidate; no independent check\nof this candidate is claimed at its author seal. No publication or audit status.',
  '2026-09-25. Personally derived conditional theorem with separate scoped PRE\nand POST checks. No retained audit status or empirical confirmation is claimed.'),
 ("The root's sealed42 static branch identities are an explicitly imported conditional parent,\nnow separately PRE/POST checked; their proof will be restated rather than\nsilently importing an additional instrument. No root45 result or checker is used.",
  'The branch identities were previously derived in the personal candidate42.\nTheir proof is restated below from the three common-model parents; it requires\nno additional instrument or physical premise. No root45 result or checker is used.')
 ],[
 ('Personal conditional theorem candidate47, 2026-09-25. No independent check\nis claimed at its author seal. It extends the personally sealed candidate46,\nwhose independent PRE is still pending. Candidate46 is an explicit provisional dependency. This is',
  'Personally derived conditional theorem47, 2026-09-25. Separate scoped PRE and\nPOST checks are complete. It extends the branch compression proved in Part I. This is'),
 ('theorem or code is used. No47 checker evidence has been seen.',
  'theorem or code is used. No47 checker evidence had been seen at the author seal.'),
 ('Work on the tensor product with A restricted to its two occupied signs, B to',
  'Throughout Part II assume a finite simple bipartite graph of maximum degree\nat most six. Work on the tensor product with A restricted to its two occupied signs, B to'),
 ('Candidate46 remains a declared\nprovisional dependency until its independent result is reviewed. No laboratory',
  'The candidate46 branch compression is proved in Part I and its separate\nindependent checks have been reviewed. No laboratory'),
 ('That improvement is an unproved route here, not part of\nthis result.',
  'That improvement was unproved in the sealed personal author record and is\nnot part of this personal result. PRE47 separately supplies a colored-series\nestimate with its own convergence window; the distinction is recorded above.')
 ]]
bodies=[]
for p,replacements in zip(sources,changes):
 s=p.read_text()
 for old,new in replacements:assert s.count(old)==1,(p,old);s=s.replace(old,new,1)
 bodies.append(re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',s,flags=re.M))
header='---\nclaim_id: '+Path(note).stem.lower()+'\nclaim_type: bounded_theorem\nclaim_scope: "Bounded original charge current, initial charge covariance and a fixed-local-support finite-time covariance remainder for the supplied common generator and minimum-number preparation; no measured charge or detector identification."\nupstream_dependencies:\n'
header+=''.join('  - '+Path(p).stem.lower()+'\n' for p in parents)
header+='runner: '+runner+'\n---\n\n'
front='''**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Original local charge current and finite-time covariance

For the supplied common matter/rotor law and the prescribed all-A-plus,
all-B-empty matter preparation, neighboring cubic-lattice charges obey

    Cov(a,b;t) / Var(b;t) -> -1/6 as t -> 0+, for kappa > 0.

This value is calculated before fitting data. The complete proof below gives
an explicit finite-time error bound, uniform in the electric coupling and
finite volume for fixed local support and fixed bounded-interaction strengths.
The initial field may be any compatible normal state; electric moments and a
selected zero-field input are unnecessary. All original later formation
channels and the common matter/field dynamics remain present.

This is a conditional model consequence. It does not yet identify a measurable
charge, justify the starting preparation, calibrate space or time, or derive a
detector coupling. The bound is conservative: at delta=kappa=1 in model rate
units, the displayed sufficient 1/60 ratio-tolerance window on sides16 and20
is only 5/12223805590224 model time units. This is neither physical seconds
nor the time when the actual model departs from its initial behavior. No
experimental agreement or exclusion is inferred.

Part I derives a bounded current from existing operators, exact charge
continuity, and the original charge covariance slope. Its cubic Fourier slope
is 40 kappa sum_i(1-cos(k_i)) per site. Part II controls finite-time local
covariance without differentiating unbounded electric observables. Its volume
uniformity is for fixed local supports; it does not extend the full Fourier
observable uniformly in volume or construct infinite-volume dynamics.

Both resolved original signs and the stipulated unnormalized coherent sum on
each separately recorded edge are covered. Their diagonal initial charge
statistics agree; their states and later recycling maps need not. The full
vacancy gates, integer Gauss fields and unsigned matter algebra are retained.
No field-only postbirth limit or truncation after a first birth is introduced.

The primary agent personally derived both proofs and decisive controls. Two
separate checkers sealed PRE reconstructions before the respective author
release, followed by POST comparisons. Earlier source exposure is disclosed
in each history; these are scoped checks, not universal claims of blindness.
Root reviewed the complete arguments, new checking code, compact results and
failure records and freshly replayed read-only correspondence. POST46 found
one wording error: zero electric field is sufficient, but not necessary, for
vanishing Hamiltonian-current expectation. That exclusivity was removed in a
separately sealed qualified copy; the original note remains unchanged. POST47
found no required mathematical repair within the stated hypotheses.

Additional PRE results retain their own authorship and scope. PRE46 gives
integrated continuity and other charge/current checks. PRE47 gives a local
colored-series remainder containing a formation factor, with a stated
convergence window; it is not the personally proved all-finite-time estimate
in Part II. Its Pearson coefficient uses sqrt(Var(a) Var(b)), whereas the
quotient above uses Var(b). Their equal initial limits do not equate the two
finite-time observables. In PRE47, charge-diagonal in the relevant integral
proof means a bounded function of matter charges, hence an operator commuting
with D. It does not admit arbitrary field-off-diagonal operators.

The PRE47 finite-dimensional control uses a six-vertex tree with two A and
four B sites, which allows two births. It is different from the historical
three-A/three-B six-site fixture that cannot form a second pair. Neither is
a numerical cubic-torus evolution or a physical preparation.

## Part I: current and initial charge statistics

'''
footer='''
## Reproduction and next observation obligation

The canonical runner executes exact copies of the two personally sealed
standard-library programs. The first reconstructs 8480 primitive Gauss-law
births and 180 covariance entries on five graphs. The second checks18 local
support sets and exact rational error arithmetic on six cubic sizes. These
are finite exact controls, not numerical finite-time propagation or proofs
of the analytic integral identities. The sealed PRE/POST packets and their
fresh root replay receipts preserve the distinct evidence coverage.

The next bridge requires physical preparation, spatial charge/readout
identification and calibrated time, then a measurement interval with justified
errors. No laboratory data have been fitted or compared in this unit. No
finite-frequency noise, photon absorption, heat, measured mass, natural vacuum,
microscopic joint time transfer or TOE completion follows. This publication
requests review; it requests no merge or audit disposition.

Direct conditional parents:

'''+''.join('- ['+Path(p).stem+']('+Path(p).name+').\n' for p in parents)
(R/note).write_text(header+front+bodies[0]+'\n## Part II: local finite-time covariance\n\n'+bodies[1]+footer)
runtime=[]
for directory,name in [('native-charge-current-noise-personal','current_noise_controls.py'),('native-charge-finite-time-personal','local_support_controls.py')]:
 p=packet+'/runtime/'+name;(R/p).parent.mkdir(parents=True,exist_ok=True);(R/p).write_bytes((E/directory/name).read_bytes());runtime.append(p)
wrapper='#!/usr/bin/env python3\n"""Exact-source original local charge and covariance controls."""\n'
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
    with tempfile.TemporaryDirectory(prefix='local-charge-covariance-') as tmp:
        for rel in RUNTIMES:(Path(tmp)/Path(rel).name).write_bytes((root/rel).read_bytes())
        for rel,label in zip(RUNTIMES,('current','finite_time')):
            program=Path(tmp)/Path(rel).name
            run=subprocess.run([sys.executable,'-B',str(program)],cwd=tmp,capture_output=True,env=env)
            (out/(label+'.stdout.json')).write_bytes(run.stdout)
            (out/(label+'.stderr.txt')).write_bytes(run.stderr)
            if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
            data=json.loads(run.stdout)
            if label=='current':
                assert data['source_sha256']==sha(program.read_bytes())
                assert data['all_assertions_passed'] and data['primitive_count']==8480 and data['real_polarized_covariance_entries']==180
            else:
                assert data['program_sha256']==sha(program.read_bytes())
                assert data['status']=='all exact assertions passed' and [g['L'] for g in data['graphs']]==[4,6,8,12,16,20]
            artifacts.append(dict(label=label,path=OUTPUT_DIRECTORY+'/'+label+'.stdout.json',
                sha256=sha(run.stdout),bytes=len(run.stdout),exit_code=0,stderr_bytes=0,
                runtime_source_sha256=sha(program.read_bytes())))
    result=dict(scope='Conditional original local charge current and covariance; no time propagation, measured readout or empirical claim.',
        source_sha256=sha(Path(__file__).read_bytes()),artifacts=artifacts,
        runtime_sha256={rel:sha((root/rel).read_bytes()) for rel in RUNTIMES},
        elapsed_seconds=time.perf_counter()-tick,all_assertions_passed=True)
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'LOCAL_CHARGE_OBSERVATION_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
'''
ast.parse(wrapper);(R/runner).write_text(wrapper)
manifest=dict(base_revision=base,base_branch='main',branch=branch,packet=packet,note=note,runner=runner,runtime=runtime,
 output_directory=out,parent_paths=parents,source_notes=list(map(str,sources)),
 cache='logs/runner-cache/original_local_charge_current_and_finite_time_covariance_2026_09_25.txt',
 result=out+'/LOCAL_CHARGE_OBSERVATION_PUBLIC_RESULTS.json',
 presentation_replacements=[[dict(old=a,new=b) for a,b in rr] for rr in changes],heading_level_increment=2,
 source_files_sha256={p:sha(R/p) for p in [note,runner,*runtime,*parents]})
with (E/'LOCAL_CHARGE_OBSERVATION_PUBLICATION_WORKING_SOURCES.json').open('x') as f:json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps(dict(note=note,runner=runner,sources_sha256=manifest['source_files_sha256']),indent=2))
