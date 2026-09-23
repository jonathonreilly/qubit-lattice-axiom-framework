from pathlib import Path
import json,gzip,hashlib,subprocess,ast,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';O=R/'drain8029-originals';d=json.loads((R/'drain8029-original-inventory.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
note='docs/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md';runner='scripts/gauge_wilson_selected_infinite_static_source_sector_2026_09_07.py';parent='docs/GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md';parentcommit='ada534009f57600495176fa85d327592d4a20abc';history='docs/work_history/review_loop/pr8029/'
assert len(d['original_paths'])==57;assert sum(x['path'].startswith('.claude/') for x in d['original_paths'])==53
assert not (W/note).exists() and not (W/runner).exists() and not (W/parent).exists()
parentbytes=subprocess.check_output(['git','show',parentcommit+':'+parent],cwd=W);assert sha(parentbytes)=='ea01dd24fe7ab4432c0f8c09ae1d3273c02b09ff11c51757440807921ae0df4f';snapshot=R/'drain8029-reviewed-parent-source.md';assert not snapshot.exists();snapshot.write_bytes(parentbytes)
manifest=[];owned=[]
for i,e in enumerate(d['original_paths']):
 b=(O/e['path']).read_bytes();assert sha(b)==e['sha256'];assert subprocess.check_output(['git','rev-parse',d['head']+':'+e['path']],cwd=W,text=True).strip()==e['blob'];assert sha(subprocess.check_output(['git','cat-file','blob',e['blob']],cwd=W))==e['sha256']
 dest=history+f'8029_{i:03d}_{Path(e["path"]).name}.gz';p=W/dest;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(gzip.compress(b,mtime=0));owned.append(dest)
 manifest.append({**{k:v for k,v in e.items() if k!='recovery_path'},'head':d['head'],'delta_base':d['delta_base'],'stored':dest,'archive_sha256':sha(p.read_bytes()),'encoding':'gzip deterministic mtime0','recovery':d['head']+':'+e['path'],'disposition':'Complete original version retained as historical provenance; no old verdict/cache or generated graph manifest imported as current authority.','canonical_path':e['path'] if e['path'] in [note,runner] else None})
original=(O/note).read_text();text=original.replace('Both complete independently frozen proofs and all three cross-reviews remain in the packet.','Both complete original proofs and all three cross-reviews remain in the [historical recovery archive](work_history/review_loop/pr8029/README.md), with exact original identities in its [manifest](work_history/review_loop/pr8029/original-manifest.json). Their independence and timing statements describe the original campaign, not this repair.')
text=text.replace("This derivation was frozen independently before reading root's block39 draft. Candidate exposure is recorded in PREREGISTRATION.md.",'Historical provenance: the original author recorded freezing this derivation before reading the completed root draft; the candidate route had already been exposed. The exact prospective contract and later reviews are archived. This is not a new independence claim.')
text=text.replace('as block38','as the linked finite charged-sector parent').replace('The reviewed block38 estimate','The linked finite charged-sector estimate').replace('in the source convention of block37/38','in the normalized tensor-vector source convention of the linked finite charged-sector parent')
old='The finite-rank spectral projections of this sum therefore carry all but 8delta|F|/R of every reduced density matrix. Finite-dimensional compactness and this tail estimate imply trace-norm precompactness of those density matrices.'
new='''Let P_R be its finite-rank spectral projection below energy R. Each reduced density matrix rho obeys Tr((I-P_R)rho)<=8delta|F|/R. The gentle-compression inequality

    ||rho-P_R rho P_R||_1 <= 2 sqrt(Tr((I-P_R)rho))
                          <= 2 sqrt(8delta|F|/R)

controls the off-diagonal coherences as well as the discarded mass. The finite-dimensional compressions form a compact bounded set, and their uniform trace-norm approximation proves trace-norm precompactness of the density matrices.'''
assert old in text;text=text.replace(old,new)
text+='''

## No-Go Discipline Gate

N1: this is a positive selected-representation energy-bound theorem. The finite spectral-measure, moving-eigenvector and combined-charge examples challenge particular limit inferences; they do not supply five exhaustive routes for a universal exclusion.

N2: no physical no-go wall is a premise. The sector spectral exclusion is the quantitative lower bound transferred from the linked finite-sector theorem under its explicit hypotheses.

N3: one fixed interaction, its consistent finite restrictions, sufficiently small coupling, full local bounded-operator algebra, exact boundary Gauss action and supplied endpoint spaces remain essential. An attained charged minimum and convergence of minimizing vectors are not assumed.

N4: the linked finite-sector parent supplies the actual uniform estimate and normalized path trial. Yarotsky Theorems2–3 and equation6 supply the neutral local state and local-vector resolvent limit, with cell gap1 and interaction norm3av/4. The general imported theorems are not proved by the finite runner.

N5: per_element covers three exact rational spectral-measure examples; per_site covers three finite Z3 charge labels, explicitly a toy; per_mode covers two fixed local resolvent modes; per_block covers three adverse-control families. Local normality, continuous SU3 averaging, spectral support transfer and the limiting form-domain bound are analytical, not executed infinite-volume simulations. The resource guard is separate from the fifteen scientific predicates.

N6: the conditional construction supplies no new axiom, primitive, physical quark dynamics or selected coupling.

N7: finite charged-minimum convergence, other boundary-selected representations, a bottom eigenvector, temporal Wilson potential, tension limit and continuum behavior remain open questions here, not disproved alternatives.

N8: the original two proofs and three reviews are historical corroboration. Present source confirmation and execution require their own identities; no broad negative certificate or audit verdict is asserted.

## Canonical execution evidence

The [canonical runner cache](../logs/runner-cache/gauge_wilson_selected_infinite_static_source_sector_2026_09_07.txt) must bind the current runner and its literal own-note and finite-sector-parent inputs. The expected scientific total is `TOTAL: PASS=15 FAIL=0`; the resource check remains separate. This expected output is not a claim of a new execution. Original failed attempts, proof variants, outputs and review records are preserved in the linked archive.
'''
(W/note).write_text(text);owned.append(note)
source=(O/runner).read_text();pin='''from pathlib import Path
AUDIT_INPUT_PATHS = ('''+repr(note)+', '+repr(parent)+''')
_REPO = Path(__file__).resolve().parents[1]
_own_note = (_REPO / AUDIT_INPUT_PATHS[0]).read_text()
_parent_note = (_REPO / AUDIT_INPUT_PATHS[1]).read_text()
assert 'claim_id: gauge_wilson_selected_infinite_static_source_sector_bounded_theorem_note_2026-09-07' in _own_note
assert '(4/a)(1-kappa)d <= inf Spec H_xy <= 4d/a,' in _own_note
assert 'claim_id: gauge_wilson_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07' in _parent_note
assert '(4/a)(1−η)L ≤ E_xy−E_0 ≤ (4/a)L.' in _parent_note
# These are literal proof-identity reads, not numerical verification of the imported theorem.
'''
assert '(4/a)(1−η)L ≤ E_xy−E_0 ≤ (4/a)L.' in parentbytes.decode();newsource=source.replace('import json\n','import json\n'+pin,1);newsource=newsource.replace("print('lattice_wide: 0 numerical infinite-volume simulations; theorem is analytical')","print('lattice_wide: checked and not executed — local normality, selected GNS sector and resolvent/form bounds are analytical; no numerical infinite-volume simulation')");newsource += "\nif sys.argv[1:] != ['--json']:\n print('TOTAL: PASS=%d FAIL=0'%checks)\n";ast.parse(newsource);(W/runner).write_text(newsource);owned.append(runner)
for e in manifest:
 if e['canonical_path']:e['canonical_sha256']=sha((W/e['canonical_path']).read_bytes());e['disposition']='Full canonical argument/calculation preserved with finding-scoped packaging and proof-explication fixes; exact original separately archived.'
manifestpath=W/history/'original-manifest.json';manifestpath.write_text(json.dumps(manifest,indent=2)+'\n');owned.append(history+'original-manifest.json')
(W/history/'README.md').write_text('''# PR8029 original recovery

The [manifest](original-manifest.json) preserves all 57 original versions, including 53 historical packet paths, with exact head/base, path, Git mode/blob and original/archive SHA-256. Each uniquely named gzip payload decodes to the exact original. The manifest and archived payloads preserve original source independently of branch retention.

The complete selected full-local-algebra GNS proof is canonical; the explicit gentle-compression bound retains the local trace-norm compactness detail from the original native double review. Both complete original derivations, all three proof reviews, prospective contracts, exact adverse controls and their outputs remain here. Original independence, timing, candidate exposure and review statements are historical, not current authority. The original generated citation manifest and cache are historical recovery only; neither overwrites current generated state or substitutes for new execution.

The selected representation, fixed interaction, common existential small-coupling regime, supplied nine-dimensional static endpoint space, exact boundary Gauss constraints and lower-semicontinuous form-energy bound remain unchanged. No finite charged-minimum convergence, bottom eigenvector, temporal potential or continuum conclusion is added.
''');owned.append(history+'README.md')
patch=''.join(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile=note,tofile=note))+''.join(difflib.unified_diff(source.splitlines(True),newsource.splitlines(True),fromfile=runner,tofile=runner));(R/'drain8029-author-corrections-v1.patch').write_text(patch)
assert not subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=W,text=True)
receipt={'status':'UNTRACKED AUTHOR PREPARATION; PARENT LANDING AND FINAL REVIEW PENDING','base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'note':note,'runner':runner,'parent':{'path':parent,'source_commit':parentcommit,'sha256':sha(parentbytes),'pending_landing':True,'external_read_snapshot':str(snapshot)},'archive_original_count':57,'history_count':53,'manifest_sha256':sha(manifestpath.read_bytes()),'inputs':[note,parent],'helpers':[],'scientific_total':15,'resource_plan':{'seconds':180,'process_tree_rss_mib':180,'capture_count_after_cold':1,'resource_guard_separate':True},'finding_dispositions':{'F1':'Literal own and corrected parent proof identity reads; actual parent absent until guarded FF.','F2':'TOTAL15 and canonical cache link; resource guard separate.','F3':'All57 archived exactly; live aliases replaced; historical claims labeled.','F4':'Honest analytical/finite N1–N8 boundary retained.','F5':'Historical gentle-compression inequality made explicit; no new hypothesis.'},'files':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in sorted(owned)],'original_review_sha256':sha((R/'drain8029-original-review.json').read_bytes()),'remaining':'No primary execution/maps/staging. Parent must land at exact reviewed bytes before root guarded FF and final cold/preflight/capture.'};out=R/'drain8029-author-prepared-v1.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(len(owned),sha(out.read_bytes()))
