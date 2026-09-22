from pathlib import Path
import json,re,gzip,hashlib,ast
r=Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';inv=json.loads((r/'drain8154-original-inventory.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
names={8154:'SPHERE_STATIC_LAW_FINITE_TORUS_MAGNETIZATION_BOUNDS',8155:'SPHERE_STATIC_LAW_WEAK_COUPLING_COMPARISON_AND_CORRELATION_BOUNDS',8157:'SPHERE_STATIC_LAW_PLANAR_COMPLEX_ROTATION_CORRELATION_UPPER_BOUNDS'}
scopes={8154:'For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained.',8155:'For a supplied uniform-sphere exponential nearest-neighbour static specification on Z^3: W1 bounds the one-site total-variation response, W2 gives alpha=2sqrt(3)beta, W3 proves finite-window comparison, W4 constructs the unique rotation-invariant DLR law when alpha<1, and W5 bounds correlations, torus magnetization and structure factors. Torus results require L>=2. No strong-coupling comparison or physical kernel classification is retained.',8157:'For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained.'}
manifest=[];live={}
for u in inv:
 n=u['number'];orig=r/'drain8154-originals'/str(n)
 for e in u['original_paths']:
  b=(orig/e['path']).read_bytes();assert sha(b)==e['sha256']
  dst=f'docs/work_history/review_loop/pr8154/{n}/{n}_{Path(e["path"]).name}.gz';p=w/dst;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(gzip.compress(b,mtime=0));assert gzip.decompress(p.read_bytes())==b
  manifest.append(dict(e,pr=n,head=u['headRefOid'],stored=dst,archive_sha256=sha(p.read_bytes()),recovery=u['headRefOid']+':'+e['path']))
 old=next(e['path'] for e in u['original_paths'] if e['path'].startswith('docs/ADMISS'));runner=next(e['path'] for e in u['original_paths'] if e['path'].startswith('scripts/'))
 note='docs/ADMISSIBILITY_RULE_'+names[n]+'_BOUNDED_THEOREM_NOTE_2026-09-15.md';cid=Path(note).stem.lower();s=(orig/old).read_text();rs=(orig/runner).read_text();assert not (w/note).exists() and not (w/runner).exists()
 sec=dict(re.findall(r'(?ms)^## ([^\n]+)\n(.*?)(?=^## |\Z)',s))
 premise=sec['Premises and declared objects'];decl= premise[premise.index('Declared objects.'):]
 decl=decl.replace('`L ≥ 1`','`L ≥ 2`').replace('The torus law `μ_L` of block 19','The torus law `μ_L`').replace('as in block 20','with each positive-coordinate bond counted once and L ≥ 2').replace(" (block 20's count)",'').replace(" (block 03's specification reading)",'').replace('`H_R = Σ_{j=1}^R 1/j`','`H_R = Σ_{j=1}^{floor(R)} 1/j`')
 if n==8154: decl=decl.replace('`L ≥ 1`','`L ≥ 2`')
 parents=ast.literal_eval(next(x.value for x in ast.parse(rs).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in x.targets)))[1:]
 links='; '.join('['+Path(p).stem+']('+Path(p).name+')' for p in parents)
 premises='The linked repository context is '+links+'. The possibility parent supplies conditional representation vocabulary; it does not select this probability law. We explicitly supply the uniform surface measure on S², beta>0, the exponential pair weight and the static specification. These are mathematical model premises, not consequences selecting physics from the axioms. The independent d-dimensional nearest-neighbour model omits all couplings outside that dimension; a two-dimensional model is not the marginal of a plane in an interacting three-dimensional model. All torus claims below use L>=2 (side at least four), so neighbours are distinct.\n\n'+decl
 keep=[]
 for title,body in sec.items():
  if title.startswith(('Theorem H1','Theorem H2','Theorem H3')) and n==8154 or title.startswith(('Theorem W1','Theorem W2','Theorem W3','Theorem W4','Theorem W5')) and n==8155 or title.startswith(('Theorem P1','Theorem P2','Theorem P3','Theorem P4')) and n==8157:
   body=body.replace('L ≥ 1','L ≥ 2');title=title.replace('; no massless channel','').replace(', and the placement','')
   if n==8154:
    body=re.sub(r'[^\n]*H4[^\n]*\n','',body)
   if n==8155 and title.startswith('Theorem W4'):
    body=body.replace('for every local `f`','for every continuous local `f`').replace('for a finite window `Λ` and local `f`','for a finite window `Λ` and continuous local `f`').replace('For a finite window `Λ` and local `f`','For a finite window `Λ` and continuous local `f`')
    body=body.replace('(d) If `ν`', 'The preceding DLR identity is first obtained on continuous local test functions. Both sides define probability measures; equality on continuous functions on each compact finite product implies equality of their Borel laws, and a monotone-class extension gives the DLR identity for bounded measurable functions. (d) If `ν`')
   if n==8157 and title.startswith('Theorem P2'):
    body=body.replace('on a window `Λ ⊇ {y : d(y) < R}`','on a window with `0,x ∈ Λ` and `Λ ⊇ {y : d(y) < R}`')
    start=body.index('Since `1/(1+m_b)²');end=body.index(' Multiply:',start)
    body=body[:start]+'Charge each active bond to one endpoint attaining the smaller distance `m_b<R` (choose either endpoint for a tie). Each site receives at most four bonds. Thus `Σ_{b:m_b<R}(1+m_b)^{-2} ≤ 4Σ_{y:d(y)<R}(1+d(y))^{-2}`. The origin contributes one; the sup-norm shell `j≥1` has at most `8j` sites and `d(y)≥j`. Every charged site has `j<R`, so including all `1≤j≤floor(R)` only increases the sum. Consequently it is at most `1+Σ_{j=1}^{floor(R)}8j/(1+j)² ≤ 1+8H_R`. This charging applies to noninteger R as well as integer R.'+body[end:]
   if n==8157 and title.startswith('Theorem P4'):
    body=re.sub(r' \(c\) On planes.*?(?=\n\n\*\*Proof)', '',body,flags=re.S)
    body=re.sub(r' \(c\) is the reading.*?∎',' ∎',body,flags=re.S)
   keep.append('## '+title+'\n'+body)
 fence=scopes[n]+' This note does not select a physical reading, coupling, rule or dimension and adopts no clause.'
 fence2='No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.'
 fence3='The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.'
 imports=sec['Imports'];imports='\n'.join(x for x in imports.splitlines() if not any(z in x for z in ['PR #','PRs #','possibility-covariance note','minimal_axioms']))
 prior=sec['Prior art and what is new'].split('On `main`')[0]+' The contribution retained here is the explicit mathematical bounds for the supplied model. No comparison with physical channels is used.'
 review='The original branch, full note, runner, cache, historical programs and outputs are preserved byte-exact in the recovery archive. Historical controls are evidence of their recorded finite domains, not a new execution or a proof of an infinite-lattice statement. The canonical primary retains its original twenty finite checks and thirteen mutation definitions; the historical mutation census is not a new review.'
 if n==8157: review+=' The historical 4×4 refuter used heat-bath Monte Carlo with 6000 sweeps, 500 burn-in sweeps, free boundary and 24 bonds. It was not direct quadrature or a truth calculation, supplied no error analysis, and did not test arbitrary fixed exterior records.'
 deferred='Broad negative certification is withheld. The original five-route tables listed proof obligations and changes of scope rather than five independent attacks on the exact exclusion. They do not establish a negative certificate. Full original arguments remain available in the archive and original branches are retained. '
 deferred+= {8154:'H4 is withdrawn: vanishing M_N² degenerates this particular lower bound; it does not exclude every possible kernel or establish a statement about every infinite-volume state.',8155:'W6 and the comparison with a strong-coupling gravity channel are withdrawn. W1–W5 remain mathematical comparison, construction and quantitative bounds for the supplied specification.',8157:'P4(c) is withdrawn: a coupling-dependent upper exponent does not exclude a faster fixed power. For example, (1+R)^(-2) satisfies every upper bound (1+R)^(-kappa) with 0<kappa<=1. The upper bound does not identify the true rate.'}[n]
 text='---\nclaim_id: '+cid+'\nclaim_type: bounded_theorem\nclaim_scope: '+json.dumps(scopes[n])+'\nupstream_dependencies:\n'+''.join('  - '+Path(p).stem.lower()+'\n' for p in parents)+'runner: '+runner+'\n---\n\n# '+names[n].replace('_',' ').title()+'\n\n**Status:** bounded-support; conditional supplied model; unaudited.\n\n## Result up front\n\n'+scopes[n]+'\n\n## Premises and declared objects\n\n'+premises+'\n\n## Prior art and what is new\n\n'+prior+'\n\n'+''.join(keep)+'## No-Go Discipline Gate\n\n'+deferred+'\n\n## Falsifiers\n'+sec['Falsifiers']+'## Boundaries and non-claims\n\n'+fence+'\n\n'+fence2+'\n\n'+fence3+'\n\n## Imports\n'+imports+'\n\n## Review record\n\n'+review+'\n\n## Verification\n'+sec['Verification']
 # Retained proof wording is conditional on explicit torus model, not coordinate-plane physics.
 text=text.replace('on any plane or line','for the stated one- and two-dimensional torus sequences')
 rs=rs.replace(old,note);rs=re.sub(r'^CLAIM_ID = .*$', 'CLAIM_ID = '+repr(cid),rs,flags=re.M)
 rs=re.sub(r'(?ms)^FENCES = \(.*?^\)', 'FENCES = '+repr((fence,fence2,fence3)),rs)
 rs=re.sub(r'    "lattice_wide:.*', '    "lattice_wide: checked and not executed — written conditional model proofs and bounds only; the finite runner does not execute an infinite lattice or physical classification",',rs)
 rs=rs.replace('no long-range order on any coordinate plane or line','finite torus magnetization bounds in dimensions one and two').replace('no massless channel below beta = sqrt(3)/6','bounded structure factors when beta < sqrt(3)/6')
 rs=rs.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = '+('300' if n==8155 else '180'))
 (w/note).write_text(text);(w/runner).write_text(rs);live[str(n)]=dict(note=note,runner=runner,original_note=old,scope=scopes[n])
base=w/'docs/work_history/review_loop/pr8154';(base/'original-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(base/'README.md').write_text('# PR8154, PR8155 and PR8157 original recovery\n\nAll 66 original path occurrences are preserved as deterministic gzip payloads, grouped by original PR. The manifest records original path, Git mode/blob/head and SHA-256 plus stored path and archive SHA-256. Decode each payload with gzip and verify its original SHA-256. These historical claims and outputs are not current scientific authority. Original branches must remain for deferred negative-certificate recovery. Live notes contain the narrowed mathematical scope; original complete proofs, programs and outputs remain here.\n')
(r/'drain8154-author-live.json').write_text(json.dumps(live,indent=2)+'\n')
print('Prepared',len(manifest),'originals and',len(live),'live pairs')
