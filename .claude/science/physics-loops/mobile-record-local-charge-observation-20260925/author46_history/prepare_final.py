"""One-time personal46 note/source writer, before independent disclosure."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
D=Path(__file__).resolve().parent;E=D.parent;R=E/'campaign-working'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md';assert not p.exists()
s=(D/'WORKING_DERIVATION.md').read_text()
s=s.replace('# Personal46 working derivation: original charge current and initial covariance growth','# Original charge current and initial charge-covariance growth')
s=s.replace('2026-09-25. Unsealed personal frontier, not independently checked or published.','2026-09-25. Personal conditional theorem candidate; no independent check\nof this candidate is claimed at its author seal. No publication or audit status.')
s=s.replace('The root\'s sealed42 static branch identities are a direct provisional parent,','The root\'s sealed42 static branch identities are an explicitly imported conditional parent,')
s=s.replace('Thus the displayed expression extends to a bounded, finite-support operator;','Thus the displayed expression extends to a bounded operator. Its action on P\nuses only the original finite local terms involving that link;')
s=s.replace('## 4. Observation obligations and next checks','## 4. Observation obligations')
start=s.index('Next: check the current sign/adjoint identity')
s=s[:start]+'''The next observation task is a controlled local finite-time or finite-lag
charge readout under the full law, with justified physical preparation and
calibration. No experimental exclusion or agreement can be drawn from the
unidentified initial slope alone.

## 5. Exact controls, chronology and limits

current_noise_controls.py is a new standard-library program. It imports no
earlier author or checker code. It executes the original outward F move and
then j for every primitive mark/destination/sign on the cube, equal L=4,6
cubic tori, a seven-site path and K2,3. The irregular graph bipartition is
specified combinatorially, not inferred from the displayed coordinate labels.
The degree-three cube is never assigned the degree-six Fourier coefficient.
No six-site second-birth calculation is used.

Every complete charge deviation and electric shift is retained sparsely, with
all six integer charge-test values. All 8480 primitive rows satisfy original
Gauss and hard-core constraints. Each fixed edge's primitive matter words are
distinct, so the same diagonal-charge sums apply to the stipulated coherent
edge mark. This verifies a diagonal statistic; it does not equate recycling
maps or quantum states. Field-independence for arbitrary normal input is proved
by the branch-isometry argument, not inferred from testing zero input flux.

The controls check 180 real polarized covariance entries, including the
real/imaginary components of allowed complex Fourier modes, all charge means,
all link formation currents, their divergence and the actual mark norm/rate
factors. The path has degree-one A sites with no formation, which tests the
zero-rate endpoint. On L4 at k=(pi/2,0,0) the full covariance slope is 2560
in units of kappa and the per-site slope is40. On L6 at k=(pi,0,0) the
corresponding values are17280 and80. Constant tests have exactly zero mean
and covariance slope on every graph.

The primary ran once at09:10:37UTC, exit0, empty stderr, elapsed1.856014958s
externally and1.781567500s internally. A separately written root_readonly_check.py
reconstructed every stored geometry, primitive field/charge row, coverage set,
mark norm, current, mean and covariance without importing or executing the
primary. Its fresh run took.462467417s, exit0 and empty stderr; all seven
observed input files were byte/stat unchanged. All five compact result groups
were read completely. Long raw vectors were checked mechanically, not all
manually read. This is personal verification, not independent evidence.

The current/core argument, arbitrary-normal-state first derivative and all
volume/measurement qualifications are analytic proof obligations not replaced
by the finite controls. No second time derivative, finite-frequency spectrum,
finite-spin stopping/derivative transfer, thermodynamic dynamics, macroscopic
current, physical vacuum instability or experimental fit was computed.

There was no failed scientific execution. The original working argument,
complete program snapshots, streams, receipts and read-only check remain
unchanged. Root had already read the independent42 charge checks and other
earlier campaign results before this derivation; no fresh blindness is claimed.
No independent45 argument was read or used. The exact source pins and author
seal distinguish existing supplied premises from the new conditional observable.
'''
p.write_text(s)
sources=[]
for row in json.loads((E/'native-birth-charge-cluster-personal/SOURCE_PINS.json').read_text())['sources']:
 q=R/row['git_path'];assert sha(q)==row['sha256']
 raw=subprocess.check_output(['git','show','origin/main:'+row['git_path']],cwd=R);assert hashlib.sha256(raw).hexdigest()==row['sha256']
 sources.append(dict(origin=str(q),sha256=sha(q),role='Unchanged supplied common-law premise; prior complete read reused'))
for q,role in [(E/'native-birth-charge-cluster-personal/ORIGINAL_BIRTH_CHARGE_CLUSTERS_ROOT.md','Original branch-isometry law, restated in this proof'),(E/'native-birth-charge-cluster-personal/AUTHOR_SEAL.json','Original personally sealed42 identity'),(E/'native-birth-charge-cluster-independent/PRE.md','Previously read independent42 exposure; not new independence'),(E/'native-birth-charge-cluster-independent/POST.md','Previously read released-source42 comparison exposure'),(R/'AGENTS.md','Instructions'),(R/'docs/ai_methodology/SCIENCE_WORKFLOW.md','Current unchanged workflow')]:sources.append(dict(origin=str(q),sha256=sha(q),role=role))
pins=dict(at=datetime.now(timezone.utc).isoformat(),main=subprocess.check_output(['git','rev-parse','origin/main'],cwd=R,text=True).strip(),sources=sources,independent46_requested_before_author_seal=False,independent45_read=False)
with (D/'SOURCE_PINS.json').open('x') as f:json.dump(pins,f,indent=2);f.write('\n')
print(json.dumps(dict(note_sha256=sha(p),sources=len(sources),source_pins_sha256=sha(D/'SOURCE_PINS.json')),indent=2))
