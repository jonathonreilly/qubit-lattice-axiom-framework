from pathlib import Path
import json,hashlib,gzip,re,ast,subprocess
r=Path(__file__).resolve().parent;w=r/'author-draft-slot';o=r/'drain8028-originals';inv=json.loads((r/'drain8028-original-inventory.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest();m=[]
assert len(inv['original_paths'])==76
for i,e in enumerate(inv['original_paths']):
 b=(o/e['path']).read_bytes();assert sha(b)==e['sha256'];dest=f'docs/work_history/review_loop/pr8028/8028_{i:03d}_{Path(e["path"]).name}.gz';p=w/dest;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes(gzip.compress(b,mtime=0));m.append({**{k:v for k,v in e.items() if k!='recovery_path'},'head':inv['head'],'stored':dest,'archive_sha256':sha(p.read_bytes()),'recovery':inv['head']+':'+e['path']})
base=w/'docs/work_history/review_loop/pr8028';(base/'original-manifest.json').write_text(json.dumps(m,indent=2)+'\n');(base/'README.md').write_text('# PR8028 original recovery\n\nAll76 original path versions, including68 historical campaign paths, are preserved byte-exact as deterministic gzip payloads. The manifest records original Git path, mode, blob, head, SHA-256 and stored SHA-256. Decode gzip and verify the original hash. Both complete derivations, original sources, prospective contracts, exposed candidate timing, root syntax-only failure, finite controls and proof reviews are historical evidence. The live note preserves the full equivariant-coordinate, ghost-vacuum, charged-resolvent and Dirichlet-form proofs. Historical generated audit outputs confer no audit authority.\n')
note=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('docs/GAUGE_'));s=(o/note).read_text()
s=s.replace('[durable packet](../.claude/science/physics-loops/static-charge-uniform-20260907/PROOF_REVIEW.md)','[recovery archive](work_history/review_loop/pr8028/README.md), with exact original identities in its [manifest](work_history/review_loop/pr8028/original-manifest.json)')
s=s.replace('The complete independent derivation follows.', 'The complete original derivation follows; independence and timing statements below describe the historical campaign, not the present repair.')
s=s.replace('2026-09-07. Independent derivation after the exposed root candidate, before reading root\'s completed proof.', 'Historical provenance dated2026-09-07: the original author records derivation after the exposed root candidate and before reading root\'s completed proof.')
s=s.replace('This supplement was exposed by root and then independently checked here; its timing is recorded separately.', 'Historical provenance: this supplement was exposed by the original root and independently checked during that campaign; its timing is preserved in the archive.')
needle='Let E_0 be the ordinary neutral ground energy, and E_xy the bottom of the charged spectrum.'
assert needle in s;s=s.replace(needle,needle+' For every finite v>=0, the full link Hamiltonian has a positive gauge-invariant ground at E_0. Thus H_links>=E_0, tensoring with the finite endpoint space preserves this lower bound, and restriction to the charged fixed subspace gives E_xy>=E_0. This is the all-coupling nonnegativity assertion, independent of the small-coupling coordinate estimate.')
s+='''

## No-Go Discipline Gate

N1: this is a positive conditional energy-bound theorem for the supplied finite compact Hamiltonian and endpoint probes. The charged resolvent exclusion is an intermediate inequality with the stated small-coupling assumptions, not a universal physical-model exclusion or a five-route certificate.

N2: no repository no-go wall is an input. The occupied-component center proof supplies the exact free threshold; the cited coordinate estimate supplies the quantitative perturbation bound.

N3: the endpoint representations, full boundary Gauss constraint, link operator, lattice spacing and coupling are supplied. Ghost-vacuum padding cannot introduce actual shortcuts or boundary leakage.

N4: the linked three repository parents provide operator normalization, all-label electric energies and source-sector conventions. Yarotsky math-ph/0411042 Section2 equations8–15 is an explicit mathematical import with the onsite gap1 and fixed support mapped above. Its global spectral circles alone do not prove the charged bound.

N5: per_element, per_site, per_mode and per_block certificates describe the stated finite graph, source-norm, exact SU3 and finite algebra controls. Seven resolvent/sector toy controls and resource checks are separately labeled. The imported infinite-dimensional coordinate theorem, domain invariance and graph-uniform estimate are analytical and not executed by a finite runner.

N6: no new axiom or primitive follows. Infinite-volume convergence, continuum scaling and physical identification remain unresolved.

N7: finite matrices challenge signs, normalization and necessary sector restrictions; they do not establish the imported coordinate estimate or approximate the full interacting charged spectrum.

N8: original separate proofs and exposed-candidate timing are historical corroboration. Current independent review and bounded capture must be separately recorded; no audit verdict or broad negative certificate is asserted.

## Canonical execution evidence

The [sector primary cache](../logs/runner-cache/gauge_wilson_static_source_sector_controls_2026_09_07.txt) and [Dirichlet helper cache](../logs/runner-cache/gauge_wilson_static_source_dirichlet_controls_2026_09_07.txt) bind current source and actual declared inputs. Expected completed totals are `TOTAL: PASS=32 FAIL=0` and `TOTAL: PASS=42 FAIL=0`; each includes one resource check. Expected outputs do not assert a new execution. The original evidence remains archived.
'''
assert not (w/note).exists();(w/note).write_text(s)
parents=['docs/'+x+'.md' for x in ['GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07','GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07','GAUGE_WILSON_STATIC_SOURCE_GEODESIC_PERTURBATION_BOUNDED_THEOREM_NOTE_2026-09-07']]
runners=[e['path'] for e in inv['original_paths'] if e['path'].startswith('scripts/gauge_')]
for runner in runners:
 text=(o/runner).read_text();pin='\nAUDIT_INPUT_PATHS = '+repr(tuple([note,*parents]))+'\n_REPO = Path(__file__).resolve().parents[1]\n'
 for i,p in enumerate([note,*parents]):pin+=f'_input_{i} = (_REPO / AUDIT_INPUT_PATHS[{i}]).read_text()\nassert '+repr('claim_id: '+Path(p).stem.lower())+f' in _input_{i}\n'
 pin+='assert "Σ_J ||F_(JI) w_I|| ≤ c r |I| ||w_I||" in _input_0\n'
 text=text.replace('from pathlib import Path\n','from pathlib import Path\n'+pin,1).replace("print('TOTAL: '+str(expected))","print('TOTAL: PASS='+str(expected)+' FAIL=0')")
 text=text.replace("for key, item in scopes.items(): print(key+': '+str(item['checks'])+' checks; '+item['scope'])", "for key, item in scopes.items():\n            if key == 'lattice_wide':\n                print(key+': checked and not executed — imported coordinate/domain theorem and uniform estimate remain analytical; '+str(item['checks'])+' finite toy/resource controls only; '+item['scope'])\n            else:\n                print(key+': PASS '+str(item['checks'])+' checks; '+item['scope'])")
 ast.parse(text);assert not (w/runner).exists();(w/runner).write_text(text)
paths=[w/note,*[w/p for p in runners],*[p for p in base.rglob('*') if p.is_file()]]
record={'status':'UNTRACKED AUTHOR PREPARATION; staged cold/current-parent confirmation pending','base':subprocess.check_output(['git','-C',str(w),'rev-parse','HEAD'],text=True).strip(),'note':note,'runners':runners,'parents':parents,'archive_original_count':len(m),'files':[{'path':p.relative_to(w).as_posix(),'sha256':sha(p.read_bytes())} for p in paths],'remaining':'No existing maps touched, no staging or primary execution. Waittrain72 currentparent landing and root guardedFF before map registration, receipt and independent cold.'}
out=r/'drain8028-author-prepared-v1.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(len(paths),'owneduntrackedfiles prepared')
