"""One-shot clean publication construction from the frozen personal40 proof."""
from pathlib import Path
import hashlib,json,re,subprocess

E=Path(__file__).resolve().parent
R=E/'native-charge-threshold-publication'
A=E/'native-charge-identification-personal'
base='d3dfdff92b6eb9e422da3691d13af4c249b7c4e9'
branch='codex/mobile-record-native-charge-and-separated-threshold-20260925'
packet='.claude/science/physics-loops/mobile-record-native-charge-threshold-20260925'
note='docs/NATIVE_BIRTH_CHARGE_AND_SEPARATED_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-25.md'
runner='scripts/native_birth_charge_and_separated_threshold_2026_09_25.py'
runtime=packet+'/runtime/two_record_threshold_and_charge_controls.py'
out='outputs/native_charge_threshold_20260925'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git',*a],cwd=R,text=True).strip()
assert git('rev-parse','HEAD')==base and git('branch','--show-current')==branch
assert git('status','--porcelain')==''
assert sha(A/'AUTHOR_SEAL.json')=='08dd5ec99ddeccfb7f70a50e216cd40e3cf8ab954cbda6fca27fbbfcaecad83a'
for row in json.loads((A/'AUTHOR_SEAL.json').read_text())['members']:
    p=A/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
assert json.loads((E/'FORTIETH_POST_ROOT_REVIEW.json').read_text())['required_mathematical_repair'] is None
parents=[]
for row in json.loads((A/'SOURCE_PINS.json').read_text())['sources'][:4]:
    p='docs/'+Path(row['path']).name;assert sha(R/p)==row['sha256'];parents.append(p)
source=A/'FIRST_BIRTH_CHARGE_AND_SEPARATED_THRESHOLD_ROOT.md'
assert sha(source)=='e31c8ec8ddbb7ef39ef5237afd94cd633d1637f7ab248d0de62fd61bcf2e73a5'
text=source.read_text()
replacements=[
 ('supplied model; not yet independently checked at this seal. No particle or',
  'supplied model; separate scoped PRE and POST checks are complete. No particle or'),
 ('This is the separated flat occupancy threshold. There is no state of this',
  'This is the global separated flat occupancy threshold. There is no state of this'),
 ('Start with the original all-A-plus, empty-B, zero-electric-flux basis input.',
  'Supply the immediately pre-mark all-A-plus, empty-B, zero-electric-flux basis input.')]
for old,new in replacements:
    assert text.count(old)==1;text=text.replace(old,new)
body=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',text,flags=re.M)
claim=Path(note).stem.lower()
header='---\nclaim_id: '+claim+'\nclaim_type: bounded_theorem\nclaim_scope: "Conditional global flat separated threshold, ordered weak-coupling energy limit, and actual-birth charge/comparison-projector distinctions; no physical mass, finite-coupling binding exclusion or selected particle."\nupstream_dependencies:\n'
header+=''.join('  - '+Path(p).stem.lower()+'\n' for p in parents)
header+='runner: '+runner+'\n---\n\n'
front='''**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Native birth charge and the separated threshold

The leading magnetic energy edge in the supplied model does not by itself
identify a charged particle. The global two-record comparison has exactly the
separated upper edge 12096, proved by an explicit positive rational comparison
function and separated trial states. Its ordered finite-volume weak-coupling
energy consequence is -3024 in the supplied scaled units. Meanwhile the actual
birth charge words differ from the uniform-minus color vector used in that
spectral comparison, and charge observables generally leave its color line.
The energy edge, the birth charge distribution and that comparison vector are
distinct mathematical objects.

The full proof below preserves every matter color, the vacancy-gated electric
term, Gauss law, and the original resolved signs or the stipulated unnormalized
coherent edge instrument. No field-only postbirth law is assumed. The flat
connection is a spectral comparison; zero electric flux is not a flat-angle
preparation. The actual birth example specifies the immediately pre-mark input.
It does not establish the field state at a randomly timed first event after
autonomous waiting from that input.

The threshold is global over the whole flat comparison operator. It does not
exclude a branch above a smaller separated edge in a fixed-total-momentum
fiber, finite-g binding, collective particles, or another physical preparation.
The auxiliary one-record kernel is algebraic: the corresponding odd-number
sector is not physical on this closed Gauss graph. Its curvature is not a
measured mass. The ordered limit takes g to zero at fixed L before L tends to
infinity; no joint-limit error bound is supplied.

This publication is stacked on the open native-ground PR #9199 at
d3dfdff92b6eb9e422da3691d13af4c249b7c4e9. Its finite-volume spectral comparison
is an explicitly imported conditional parent, not an assumed result on main.
The root personally derived the proof and controls. A separate checker sealed
a PRE before author disclosure and a released-source POST afterward. Root
read both arguments and ran the read-only evidence checks at unchanged source
identities. Those checks found no required mathematical repair within the
author's stated scope. The final publication correspondence is a separate
presentation/source check, not an additional blind reconstruction.

The independent PRE's stronger finite-volume coverage and strictness, full
auxiliary band, wrapped small-volume certificates and charge trace-distance
bounds remain attributed to that report. The POST's explicit fourth-order
Fourier remainder also remains separately attributed. The root theorem below
retains its own rational witness and conservative L>=24 periodic domain.
Earlier failed bounded-ansatz searches and the missing exploratory attempt04
script/receipt remain disclosed; the final standalone program independently
of those personal helpers verifies every decisive rational residual.

The comparison-projector weights below are not low-energy probabilities. The
Gauss-fiber convention must be fixed, and coherent equality holds at the
specified flat connection; the general statement is an upper bound. No
experimental detector, stable packet, charge unit, force law or measured
particle mass is identified by this result.

## Complete personal argument

'''
footer='''
## Reproduction and observation boundary

The primary runner executes an exact copy of the sealed standalone personal
program in a temporary directory, keeping full result JSON and both streams.
It checks the primitive grouped rows, the rational witness, modular controls,
reciprocity, the auxiliary kernel and actual birth charge moments. Fresh reuse
is not new independence. Finite controls support the displayed analytic tail
and periodic lifting proofs; they do not prove finite-g binding or dynamics.

The next required bridge is an actual prepared or selected full-state charged
packet, its persistent transport and current/force response, and justified
physical scale and readout. There is no data fit or empirical confirmation in
this unit. No new axiom, audit verdict or merge is requested.

The direct conditional parents are:

'''+''.join('- ['+Path(p).stem+']('+Path(p).name+').\n' for p in parents)
assert not (R/note).exists();(R/note).write_text(header+front+body+footer)
(R/runtime).parent.mkdir(parents=True)
(R/runtime).write_bytes((A/'two_record_threshold_and_charge_controls.py').read_bytes())
assert sha(R/runtime)=='710428b3f5785b50bad193615c8adfbf163743d7eaca90cf81e4695b677ce447'
wrapper='#!/usr/bin/env python3\n"""Exact-source native charge and global threshold controls."""\n'
wrapper+='AUDIT_TIMEOUT_SEC = 120\nAUDIT_INPUT_PATHS = '+repr(tuple([note,*parents,runtime]))+'\n'
wrapper+='OUTPUT_DIRECTORY = '+repr(out)+'\nRUNTIME = '+repr(runtime)+'\n'
wrapper+=r'''
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

def main():
    root=Path(__file__).resolve().parents[1];out=root/OUTPUT_DIRECTORY
    out.mkdir(parents=True,exist_ok=True);tick=time.perf_counter()
    sha=lambda data:hashlib.sha256(data).hexdigest()
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='native-charge-threshold-') as tmp:
        source=Path(tmp)/Path(RUNTIME).name;source.write_bytes((root/RUNTIME).read_bytes())
        artifact=Path(tmp)/'CHARGE_THRESHOLD_RESULTS.json'
        run=subprocess.run([sys.executable,'-B',str(source),'--output',str(artifact)],cwd=tmp,capture_output=True,env=env)
        for label,data in [('stdout',run.stdout),('stderr',run.stderr)]:
            (out/('charge_control.'+label+'.txt')).write_bytes(data)
        if run.returncode or run.stderr:raise RuntimeError(run.stderr.decode())
        data=artifact.read_bytes();full=json.loads(data);summary=json.loads(run.stdout)
        omitted={'unwrapped_rows','periodic_controls','reciprocity_controls','auxiliary_one_occupancy_kernel'}
        assert summary=={k:v for k,v in full.items() if k not in omitted}
        assert full['source_sha256']==sha(source.read_bytes())
        (out/artifact.name).write_bytes(data)
    result={'scope':'Fresh exact-source primitive controls of conditional global flat threshold and native birth charges; no new independence, finite-g dynamics or physical calibration.',
      'source_sha256':sha(Path(__file__).read_bytes()),'runtime_source_sha256':sha((root/RUNTIME).read_bytes()),
      'elapsed_seconds':time.perf_counter()-tick,'exit_code':run.returncode,'stderr_bytes':len(run.stderr),
      'stdout_bytes':len(run.stdout),'stdout_sha256':sha(run.stdout),
      'complete_scientific_artifact':{'path':OUTPUT_DIRECTORY+'/'+artifact.name,'sha256':sha(data),'bytes':len(data)},
      'all_assertions_passed':True}
    output=json.dumps(result,indent=2,allow_nan=False)+'\n'
    (out/'NATIVE_CHARGE_THRESHOLD_PUBLIC_RESULTS.json').write_text(output)
    print(output,end='');print('TOTAL_PASS: 1')

if __name__=='__main__':main()
'''
# In this raw source template, the two visible backslashes above would produce
# a literal escape after JSON. Publish an actual newline escape in Python code.
wrapper=wrapper.replace("+'\\\\n'","+'\\n'")
(R/runner).write_text(wrapper)
manifest={'base_revision':base,'base_branch':'codex/mobile-record-native-ground-energy-and-formation-20260925',
 'branch':branch,'packet':packet,'note':note,'runner':runner,'runtime':[runtime],
 'output_directory':out,'parent_paths':parents,'source_note':str(source),
 'cache':'logs/runner-cache/native_birth_charge_and_separated_threshold_2026_09_25.txt',
 'result':out+'/NATIVE_CHARGE_THRESHOLD_PUBLIC_RESULTS.json',
 'presentation_replacements':[{'old':a,'new':b} for a,b in replacements],
 'heading_level_increment':2,'source_files_sha256':{p:sha(R/p) for p in [note,runner,runtime,*parents]}}
with (E/'NATIVE_CHARGE_THRESHOLD_PUBLICATION_WORKING_SOURCES.json').open('x') as f:
    json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps(manifest,indent=2))
