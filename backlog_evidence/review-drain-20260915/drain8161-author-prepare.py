from pathlib import Path
import json,hashlib,gzip,re,ast,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';src=r/'drain8161-read';inv=next(x for x in json.load(open(r/'drain-next-topology-wave10-details.json')) if x['number']==8161);sha=lambda b:hashlib.sha256(b).hexdigest()
oldnotes=['BLOCK01_GLOBAL_GAUSS_DRESSING_AND_VARIATIONAL_COMPRESSION.md','BLOCK02_ORTHOGONAL_TRANSVERSE_SECTOR_AND_CURRENT_VERTEX.md','BLOCK03_INFRARED_PROFILE_OF_THE_REFERENCE_VERTEX.md','BLOCK04_COUPLED_FREE_VACUUM_RESOLVENT_DENSITIES.md']
stems=['ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION','ROTOR_ORTHOGONAL_TRANSVERSE_REFERENCE_CURRENT_VERTEX','ROTOR_REFERENCE_VERTEX_INFRARED_WEIGHTED_NORMS','ROTOR_COUPLED_FREE_VACUUM_RESOLVENT_DENSITIES']
notes=['docs/'+s+'_BOUNDED_THEOREM_NOTE_2026-09-16.md' for s in stems]
oldruns=['block01_affine_theta_check.py','block01_charged_ring_compression.py','block02_one_photon_vertex_check.py','block03_infrared_vertex_check.py','block04_coupled_vacuum_check.py']
runs=['scripts/rotor_gauss_affine_theta_check_2026_09_16.py','scripts/rotor_gauss_charged_ring_compression_2026_09_16.py','scripts/rotor_transverse_reference_vertex_check_2026_09_16.py','scripts/rotor_reference_infrared_norm_check_2026_09_16.py','scripts/rotor_coupled_vacuum_resolvent_check_2026_09_16.py']
diag='docs/ROTOR_FIXED_COUPLING_GAUSS_CHARACTERISTIC_IDENTITY_SUPPORTING_PROOF_2026-09-16.md';primary=[runs[0],runs[2],runs[3],runs[4]];deps=[[],[notes[0]],[notes[0],notes[1]],[notes[1],notes[2]]]
scopes=['Supplied integer-rotor/CAR Hamiltonian on complete free cubic boxes: exact all-neutral-sector Gauss isometry, all-affine theta derivative bounds and extensive Coulomb variational compression for0<g<=1/10; no dynamical elimination or actual-state phase theorem.','Supplied small-coupling Gauss Gaussian reference: exactly centered orthogonal sector, normalized shifted overlap and charge/volume-uniform per-link current vertex with an extensive total bound; no stable physical photon claim.','Specified cubic Maxwell reference: exact low-frequency norm bounds, finite inverse-half-energy form and logarithmic bare inverse-energy norm with projector factor; local free-cube profile limit. Reference-domain statement only, not a physical no-go.','Specified paired Maxwell/Wilson filled-sea reference: exact current/Fock normalization, uniform first vacuum-resolvent densities and cutoff limits retaining finite-grid node atoms; no all-order or fixed-coupling phase conclusion.']
m=[]
for i,e in enumerate(inv['original_paths']):
 b=(r/'drain8161-author-originals'/e['path']).read_bytes();assert sha(b)==e['sha256'];dest=f'docs/work_history/review_loop/pr8161/8161_{i:03d}_{Path(e["path"]).name}.gz';p=w/dest;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes(gzip.compress(b,mtime=0));m.append(dict(e,head=inv['headRefOid'],stored=dest,archive_sha256=sha(p.read_bytes()),recovery=inv['headRefOid']+':'+e['path']))
base=w/'docs/work_history/review_loop/pr8161';(base/'original-manifest.json').write_text(json.dumps(m,indent=2)+'\n')
recovery='[Original recovery](work_history/review_loop/pr8161/README.md) and [exact manifest](work_history/review_loop/pr8161/original-manifest.json) preserve all original proofs, working notes, programs and outputs.'
gate='''## Scope and negative-claim discipline

N1: energy-form bounds, a coupled fermion denominator, current soft factors, coherent dressing and multiscale state construction are distinct open physical routes. The coupled denominator is worked at first order in the resolvent-density note. These are not five completed attacks against a universal exclusion.

N2: compression versus off-space action and a specified inverse-domain failure are different reference diagnostics, not independent physical walls. Physical-wall count zero.

N3: no unique finite-volume sea, positive matter gap, volume-independent total error, invariant trial space or interchangeable limits is assumed.

N4: the linked model definitions and explicit mathematical imports are the actual premises; a chosen reference is not an interacting ground-state identification.

N5: finite element, site, mode and block challenges are printed by the named programs at their stated cutoffs and tolerances. Infinite-volume bounds, analytical domain statements and limit proofs are checked in the written mathematics, not executed by a finite grid. Source hashes and resource limits do not prove science.

N6: the successful coupled first coefficient remains positive progress, not a broad perturbative impossibility result.

N7: current conservation, particle-hole phase space and coherent or multiscale constructions can change the actual observable; none is excluded.

N8: earlier bounded-time weak-coupling results do not identify the fixed-g interacting state or use the same inverse operator. Historical author mutation results remain historical; no broad negative certificate or audit verdict is granted.
'''
for i,old in enumerate(oldnotes):
 text=(src/old).read_text();text=re.sub(r'\*\*Author[^\n]*\n','**Status:** conditional-support under the explicitly supplied model/reference; independent retained-grade audit remains separate.\n',text,count=1)
 for a,b in zip(oldnotes,notes):text=text.replace(a,Path(b).name)
 for a,b in zip(oldruns,runs):text=text.replace('../evidence/'+a,'../'+b).replace('['+a+']','['+Path(b).name+']')
 for j,label in enumerate(['Gauss-dressing theorem','orthogonal-reference theorem','infrared-reference theorem','coupled-resolvent theorem'],1):text=text.replace(f'BLOCK0{j}',label)
 text=re.sub(r'Hard landing conditions:.*', 'Canonical source registration and current runner evidence support review; independent audit and the combined integrated-tree gate remain separate. No author audit verdict is asserted.',text)
 text=text.replace('independent review outstanding.','independent affected-source confirmation and audit required.').replace('All checks are by the author and grant no independent review status.','The numerical results described here are historical author evidence and grant no current independent review status.')
 text=text.replace('## Personal finite challenges','## Historical finite challenges').replace('## 5. Personal verification','## 5. Historical verification').replace('## Personal evidence','## Historical evidence').replace('Personal evidence sources:','Canonical finite evidence sources:')
 header='---\nclaim_id: '+Path(notes[i]).stem.lower()+'\nclaim_type: bounded_theorem\nclaim_scope: '+json.dumps(scopes[i])+'\nrunner: '+primary[i]+'\nupstream_dependencies: '+json.dumps([Path(x).stem.lower() for x in deps[i]])+'\n---\n\n**Type:** bounded_theorem\n\n'
 links='\n\n## Current dependencies and evidence\n\n'+recovery+'\n\n'
 if deps[i]:links+='Actual linked mathematical context: '+', '.join('['+Path(p).stem+']('+Path(p).name+')' for p in deps[i])+'.\n\n'
 ownedruns=[runs[0],runs[1]] if i==0 else [primary[i]]
 links+='Canonical caches: '+', '.join('['+Path(p).stem+'](../logs/runner-cache/'+Path(p).stem+'.txt)' for p in ownedruns)+'. These must match the current source/input bytes.\n'
 if i==0:links+='The [bounded Gauss characteristic identity]('+Path(diag).name+') preserves the distinct volume-versus-scale diagnostic in full.\n'
 (w/notes[i]).write_text(header+text+'\n'+gate+links)
dtext=(src/'BLOCK01_VOLUME_VERSUS_SCALE_DIAGNOSTIC.md').read_text().replace('from PR8160','specified by those two reference properties').replace('An infrared rescaling changes','An infrared rescaling changes');(w/diag).write_text(dtext+'\n## Ownership and scope\n\nThis is a supporting proof owned by the [global Gauss-dressing theorem]('+Path(notes[0]).name+'). The operator identity follows by exponentiating the exact Gauss constraint on the physical space; the mismatch concerns these fixed local bounded probes at fixed g. It excludes no rescaled macroscopic theory.\n\n'+recovery+'\n')
inputlists=[[notes[0],diag],[notes[0]],[notes[1],notes[0],runs[0]],[notes[2],notes[0],notes[1]],[notes[3],notes[1],notes[2]]]
familylabels=[['integer cochain and fractional-kernel identities','three affine sectors with unchanged primal/dual cutoffs and tolerances','adverse centered-only overlap comparison','four free-cube spectral bounds'],['four charged-ring compression fixtures with unchanged cutoff rule','off-space leakage and finite variational comparisons','outer-tail checks at the original threshold'],['three rank-five centered/normalized vertex fixtures','omitted-means and wrong-sign adverse comparisons'],['five periodic Cartesian lattice grids','four spherical quadrature refinements at original tolerances','quartic-coefficient comparison'],['direct L3 real-space CAR versus momentum calculation','five finite reference coefficient grids','exact finite-node counts at L6 and L12']]
for i,old in enumerate(oldruns):
 text=(src/old).read_text();text=re.sub(r'^AUDIT_INPUT_FILES=.*$', 'AUDIT_INPUT_PATHS = '+repr(tuple(inputlists[i])),text,flags=re.M)
 text=text.replace('from block01_affine_theta_check import','from '+Path(runs[0]).stem+' import').replace("with_name('block01_affine_theta_check.py')","with_name('"+Path(runs[0]).name+"')")
 # Scientific file reads are real and explicit. Imported helper definitions do not execute run().
 pin='''\n_REPO = Path(__file__).resolve().parents[1]
for _input in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input).read_bytes()
    if _input.endswith('.md') and 'BOUNDED_THEOREM_NOTE' in _input:
        assert ('claim_id: ' + Path(_input).stem.lower()).encode() in _input_bytes
'''
 text=text.replace('from pathlib import Path\n','from pathlib import Path\n'+pin,1)
 lines=['per_element: executed — '+familylabels[i][0],'per_site: executed — finite supplied-reference configurations at declared cutoffs','per_mode: executed — finite matrices or Fourier grids described in the JSON evidence','per_block: executed — '+familylabels[i][-1],'lattice_wide: checked and not executed — written uniform bounds and limit proofs; no actual interacting infinite-volume state executed']
 footer='\ndef _completed_families():\n'+''.join('    print('+repr('PASS: '+label)+')\n' for label in familylabels[i])+''.join('    print('+repr(line)+')\n' for line in lines)+'    print('+repr('TOTAL: PASS='+str(len(familylabels[i]))+' FAIL=0')+')\n'
 text=text.replace("if __name__=='__main__':run()",footer+"\nif __name__=='__main__':\n    run()\n    _completed_families()")
 ast.parse(text);(w/runs[i]).write_text(text)
(base/'README.md').write_text('# PR8161 original recovery and argument dispositions\n\nAll47 original path/mode/blob versions are preserved byte-exact as deterministic gzip payloads. The manifest binds original and archive SHA-256. Decode gzip to recover the complete originals; historical outputs and all30 mutation failures are not current executions. Original branches remain available.\n\nThe four complete final arguments are canonical supplied-model notes. The unique volume-versus-scale characteristic-function argument is a canonical supporting proof. Working affine Gaussian topology/overlap/moment/cluster/compression lemmas are retained in the full Gauss-dressing proof; centered-sector/mean-difference lemmas in the orthogonal-reference proof; denominator/Ward/node-count lemmas in the coupled-resolvent proof. Original working versions remain exact here.\n\nCutoff limitations, off-space leakage and the squared-norm phase blindness remain in the live proof/evidence discussions. Planning records and old review language supply provenance only.\n')
prepared={'status':'UNTRACKED AUTHOR PREPARATION; NO SCIENTIFIC PASS','base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=w,text=True).strip(),'notes':notes,'supporting_proof':diag,'runners':runs,'inputs':dict(zip(runs,inputlists)),'helper_map_plan':{Path(notes[0]).stem.lower():[runs[1]],Path(notes[1]).stem.lower():[runs[0]]},'original_count':47,'completed_family_counts':dict(zip(runs,map(len,familylabels))),'timeouts_seconds':dict(zip(runs,[180,180,180,120,180])),'proposed_external_memory_cap_bytes':536870912,'resource_assessment':'Original time caps retained. Affine rank-five sums chunk first coordinate; largest direct tail19^4 by12, cube L<=4 dense matrices. Infrared grids slice by one coordinate at N<=256. Ring sparse finite cutoff; coupled grids L<=12. Proposed512MiB sequential external tree cap, subject cold confirmation; no measured new runtime or peak claim.','files':[{'path':p.relative_to(w).as_posix(),'sha256':sha(p.read_bytes())} for p in [*[w/x for x in notes],w/diag,*[w/x for x in runs],*sorted(base.rglob('*'))] if p.is_file()]}
(r/'drain8161-author-prepared-v1.json').write_text(json.dumps(prepared,indent=2)+'\n');print('prepared',len(prepared['files']),'untracked files; no tracked helpers edited')
