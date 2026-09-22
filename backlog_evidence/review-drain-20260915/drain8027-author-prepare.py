from pathlib import Path
import json,hashlib,gzip,re,ast,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'author-draft-slot';o=r/'drain8027-originals';inv=json.load(open(r/'drain8027-original-inventory.json'));sha=lambda b:hashlib.sha256(b).hexdigest();m=[]
for i,e in enumerate(inv['original_paths']):
 b=(o/e['path']).read_bytes();assert sha(b)==e['sha256'];dest=f'docs/work_history/review_loop/pr8027/8027_{i:03d}_{Path(e["path"]).name}.gz';p=w/dest;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes(gzip.compress(b,mtime=0));m.append({**{k:v for k,v in e.items() if k!='recovery_path'},'head':inv['head'],'stored':dest,'archive_sha256':sha(p.read_bytes()),'recovery':inv['head']+':'+e['path']})
base=w/'docs/work_history/review_loop/pr8027';(base/'original-manifest.json').write_text(json.dumps(m,indent=2)+'\n');(base/'README.md').write_text('# PR8027 original recovery\n\nAll 73 original path versions, including the complete 65-file campaign packet, are preserved byte-exact as deterministic gzip payloads. The manifest records original path, Git mode/blob/head, original SHA-256 and stored archive SHA-256. Decode gzip and verify the original SHA-256. Original full root and primary derivations, controls, failed attempts, raw outputs and timing/review records are historical evidence, not new executions or present review authority. Original branches remain available. Live source surfaces preserve the complete geodesic argument and the primary planar next-branch corollary.\n')
note=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('docs/GAUGE'));parent='docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md';s=(o/note).read_text();s=s.replace('Both independently frozen derivations, candidate timing and prior-art review remain in the evidence packet.','The original independently frozen derivations, candidate timing and prior-art review are historical records in the [recovery archive](work_history/review_loop/pr8027/README.md), with exact paths and hashes in its [manifest](work_history/review_loop/pr8027/original-manifest.json).');s=s.replace('# Root finite-volume static-source geodesic perturbation','# Finite-volume static-source geodesic perturbation');s=s.replace("Prospectively derived after20:39UTC contract and before primary's independent result. Prior-art search immediately found", "Historical provenance: the original root record states derivation after its20:39UTC contract and before the original primary result. Those timing and independence statements refer to the archived original campaign, not this repair. Its historical prior-art search found")
cor='''## Planar next-branch splitting at fixed box

For planar displacement (R,S,0) with R,S>0 and L=R+S fixed, use the equivalent R-particle encoding. The largest adjacency eigenvalue occupies modes1,...,R. Since the one-body eigenvalues strictly decrease, the next-largest replaces R by R+1. Consequently the next charged branch above the lowest has gap

    (v/9)[cos(pi R/(L+1))-cos(pi(R+1)/(L+1))] + O_(box,x,y)(a v²).

This follows by subtracting the two first-order energies from the complete subset spectrum above. The coefficient is positive; the perturbation radius and remainder depend on the fixed box and endpoints. Axis-aligned displacement has only one geodesic and is excluded from this internal splitting statement. No uniform source-distance or coupling-limit assertion is made. This explicitly preserves formula(8) of the original primary derivation section4.

'''
s=s.replace('## Scope and unresolved extension',cor+'## Scope and unresolved extension');s+='''
## No-Go Discipline Gate

N1: the retained theorem classifies the free finite-box equality space and its first-order matrix; it does not issue a confinement or physical-model exclusion. The analytical all-representation argument remains explicit above rather than inferred from a finite representation cutoff.

N2: no repository no-go wall is used as a premise. The occupied-component center transformation and positive link energy establish the stated free-space classification directly.

N3: the compact action, source representations, zero source rest/kinetic energy and fixed open box are supplied assumptions. They select no native physical matter or clock.

N4: the linked compact Hamiltonian parent supplies the kinetic normalization and compact plaquette operator. The archived prior-art abstract supplies historical attribution only, not an imported quantitative theorem. Haar character orthogonality, the representation decomposition, finite graph adjacency and bounded analytic perturbation are the mathematical tools used in the proof.

N5: per_element checks concern exact source/Haar factors; per_site checks enumerate the stated finite path and face geometries; per_mode checks concern planar spectra and stated finite label controls; per_block checks concern finite adjacency and the4096-support cube census. The all-representation classification, compact-resolvent isolation and fixed-box perturbative remainder are analytical; no runner executes the infinite representation space or a uniform interacting limit. Resource guards are resource checks, not lattice-wide science.

N6: no primitive or axiom update follows. Uniform charged-versus-neutral remainder control remains open.

N7: finite exact matrices do not prove the full interacting spectrum; their role is to challenge normalization and projected matrix identities independently of the analytical proof. The common first-order mechanism is not claimed as new.

N8: original root/primary corroboration and candidate timing remain historical, not newly independent evidence. No broad negative certificate or five-route exclusion is claimed.

## Canonical execution evidence

The [primary cache](../logs/runner-cache/gauge_wilson_static_source_geodesic_2026_09_07.txt) and [cube helper cache](../logs/runner-cache/gauge_wilson_static_source_geodesic_cube_check_2026_09_07.txt) must bind current source and declared inputs. Expected completed finite-check totals are `TOTAL: PASS=34 FAIL=0` and `TOTAL: PASS=37 FAIL=0`, respectively; these are expected outputs, not a claim of a new execution. Historical raw evidence remains in the recovery archive.
''';assert not (w/note).exists();(w/note).write_text(s)
runners=[e['path'] for e in inv['original_paths'] if e['path'].startswith('scripts/gauge')]
for runner in runners:
 text=(o/runner).read_text();pin='''\nAUDIT_INPUT_PATHS = ('''+repr(note)+', '+repr(parent)+''')
_REPO = Path(__file__).resolve().parents[1]
_note_text = (_REPO / AUDIT_INPUT_PATHS[0]).read_text()
_parent_text = (_REPO / AUDIT_INPUT_PATHS[1]).read_text()
assert "claim_id: gauge_wilson_static_source_geodesic_perturbation_bounded_theorem_note_2026-09-07" in _note_text
assert "P_geo (F-S) P_geo = F I - A_geo/18." in _note_text
assert "claim_id: gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07" in _parent_text
assert "H=-(3/(2a)) Delta+V." in _parent_text
'''
 text=text.replace('from pathlib import Path\n','from pathlib import Path\n'+pin,1);text=text.replace("print('PASS TOTAL='+str(result['TOTAL'])+' unique named checks')", "print('TOTAL: PASS='+str(result['TOTAL'])+' FAIL=0')");text=text.replace("print('PASS TOTAL='+str(result['check_count'])+' unique named checks')", "print('TOTAL: PASS='+str(result['check_count'])+' FAIL=0')");text=text.replace('lattice_wide: PASS 1 resource guard; no uniform interacting remainder','lattice_wide: checked and not executed — all-representation and fixed-box perturbation proof is analytical; resource guard does not establish a uniform interacting remainder').replace('lattice_wide: PASS 1 resource guard; all-representation proof remains analytical','lattice_wide: checked and not executed — all-representation proof remains analytical; resource guard is a separate finite resource check');ast.parse(text);assert not (w/runner).exists();(w/runner).write_text(text)
report={'status':'UNTRACKED AUTHOR PREPARATION; original full review and parent guarded advance pending','base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=w,text=True).strip(),'note':note,'runners':runners,'archive_original_count':len(m),'files':[{'path':p.relative_to(w).as_posix(),'sha256':sha(p.read_bytes())} for p in [w/note,*[w/x for x in runners],*sorted(base.rglob('*'))] if p.is_file()],'remaining':'No existing tracked helper maps touched; no staging, primary execution or commit. Wait8026 landing and guarded FF before additive helper registration/schema2 cold freeze.'};(r/'drain8027-author-prepared-v1.json').write_text(json.dumps(report,indent=2)+'\n');print(len(report['files']),'untracked files prepared; originals',len(m))
