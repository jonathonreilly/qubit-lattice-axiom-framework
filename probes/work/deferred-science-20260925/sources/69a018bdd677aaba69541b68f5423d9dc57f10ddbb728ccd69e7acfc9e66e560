"""Preserve the working derivation and prepare the personally reviewed candidate."""
from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).resolve().parent
s=(P/'WORKING_DERIVATION.md').read_text()
old='''Personal candidate47, 2026-09-25. Unsealed working derivation, not independently
checked. It extends the personally sealed candidate46, whose independent PRE
is still pending.'''
new='''Personal conditional theorem candidate47, 2026-09-25. No independent check
is claimed at its author seal. It extends the personally sealed candidate46,
whose independent PRE is still pending.'''
assert old in s;s=s.replace(old,new,1)
old='''no Bochner norm continuity of conjugated rotor shifts is required.'''
new='''no Bochner norm continuity of conjugated rotor shifts is required.
The double integrands are jointly weak-star measurable: after pairing with a
normal state, continuity of C_u on trace class and weak-star continuity of
C_s^*O, together with their uniform bounds, justify the iterated integrals.
This also gives the stated scalar norm estimates by duality.'''
assert old in s;s=s.replace(old,new,1)
old='''## Pending checks

Personally review the weak-star integral argument and support counts, construct
exact finite-graph support-count controls and separate arithmetic/error checks,
then seal the candidate before any neutral independent reconstruction request.
Retain the provisional46 dependency and any failed bound or geometry attempt.
'''
new='''## 6. Exact controls and their limits

The personally authored standard-library local_support_controls.py checks the
support sets and all rational bound arithmetic on sides4,6,8,12,16,20. It runs
no earlier program and simulates no time evolution. The local enumeration is
compared with a separate exhaustive all-A-pair search on sides4,6,8. Complete
sets X1,X2 and both local group lists are saved for A, B and adjacent AB tests.
The initial two-site means and covariance are also checked explicitly.

For sides16 and20, the B test has6 formation groups and93 magnetic groups.
X1 has393 atoms, X2 has741, and the latter meets146 formation and1713 magnetic
groups. On side12 the last magnetic count is1710, so mere agreement of the
support sizes is not enough to assume all counted interactions have stabilized.
On side4, wrapping changes these counts to32 and240; the actual geometry is
used. No infinite-volume convergence theorem is inferred from these samples.

At sides16 and20 the computed conservative covariance constants are

 M_bb=2373055543296 delta^2+40572057600 delta kappa+170640000 kappa^2,
 M_ab=4371220795392 delta^2+75452083200 delta kappa+319680000 kappa^2.

For the purely illustrative delta=kappa=1 in model rate units, the rational
sufficient interval for the error in (6) to be at most1/60 reaches
t=5/12223805590224, approximately4.09038e-13 in the corresponding model time
unit. This is not seconds, a fitted scale, a useful experimental window, or a
claim that the actual dynamics departs from its initial law at that time.
These deliberately loose operator bounds are sufficient rather than optimal.

The primary ran once on2026-09-25 at09:41:24.985561UTC, exit0, empty stderr,
elapsed0.164348542s. Its complete raw output is bound by its execution receipt.
A separately authored root_readonly_check.py then enumerated every global
formation star and every distance-two A pair using closed coordinate offsets
on all six volumes, including36000 magnetic pairs and24000 electric terms
on side20. It rebuilt every saved support set, proved completeness of every
saved local group list by that enumeration, and checked all rational covariance
constants and ratio denominators. It imported or executed no primary code.
The fresh read-only run took0.724004959s, exit0, empty stderr; all eight observed
inputs retained their bytes and file metadata. All six compact result groups
were read completely. Large raw set lists were checked mechanically rather
than all manually read. This is root verification, not independent evidence.

No scientific execution failed. The original working argument, pre-control
copy, programs, snapshots, streams and exact source pins remain preserved.
The integral/domain proof and physical identification obligations are not
replaced by the finite geometric controls. Candidate46 remains a declared
provisional dependency until its independent result is reviewed. No laboratory
data or observed target was used to obtain the coefficient or the ratio.

## 7. Remaining observation decisions

The next bridge obligations are a justified physical preparation and local
charge/readout identification, calibrated length/time, and sharper usable
errors if the available measurement interval needs them. A possible further
bound could exploit that all purely magnetic histories preserve the initial
matter sector, to replace the coarse delta-squared error by one containing a
formation factor. That improvement is an unproved route here, not part of
this result. Fourier-volume control, finite-frequency noise and microscopic
transfer still require separate derivations. Do not promote (6) into a test
of nature until its preparation and measurement dictionary are supplied or
derived and independently assessed.
'''
assert old in s;s=s.replace(old,new,1)
dest=P/'LOCAL_CHARGE_FINITE_TIME_COVARIANCE_ROOT.md'
with dest.open('x') as f:f.write(s)
receipt=dict(prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),note_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),complete_personal_proof_and_code_read=True,all_six_compact_output_groups_read=True,raw_sets='Mechanically checked by separate full-graph enumeration; not all manually read.',independent_check_claimed=False,required_repairs=[])
with (P/'ROOT_READ_RECEIPT.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
