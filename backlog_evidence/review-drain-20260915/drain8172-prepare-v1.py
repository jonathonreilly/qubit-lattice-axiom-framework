from pathlib import Path
import ast,difflib,gzip,hashlib,io,json,os,shutil,subprocess,tarfile
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';O=R/'drain8172-original'
sha=lambda b:hashlib.sha256(b).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p.read_bytes()))
write=lambda p,s:(p.parent.mkdir(parents=True,exist_ok=True),p.write_text(s))
owner=json.loads((R/'review-meta-slot.json').read_text());assert owner['owner']=='PR8172-author'
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert git('rev-parse','HEAD')=='8bf464953779b8ada8415208e89a656411f9f525' and not git('status','--porcelain')
inv=json.loads((O/'inventory.json').read_text());packet=json.loads((O/'complete-packet-inventory.json').read_text());assert len(inv['paths'])==24 and len(packet)==79
note='docs/SIX_AXIS_POINT_SENSITIVITIES_FINITE_ISLAND_HEALING_AND_DIRECTED_RECURRENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md'
runner='scripts/six_axis_point_sensitivities_finite_island_healing_directed_recurrence_bounds_2026_09_16.py'
cid=Path(note).stem.lower();archive=Path('docs/work_history/repo/review_feedback/pr8172-evidence');A=W/archive;assert not A.exists();A.mkdir(parents=True)
manifest=[]
for e in inv['paths']:
    o=e['original'];raw=Path(o['snapshot']).read_bytes();assert sha(raw)==o['sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==o['blob']
    op=Path(e['path']);stored='kept/'+op.stem+'-'+o['blob'][:16]+op.suffix;encoding='identity'
    if op.suffix in ['.txt','.json']:stored+='.gz';payload=gzip.compress(raw,mtime=0);encoding='gzip'
    else:payload=raw
    p=A/stored;p.parent.mkdir(exist_ok=True);p.write_bytes(payload);p.chmod(int(o['mode'],8)&0o777)
    manifest.append(dict(original_path=e['path'],original_mode=o['mode'],git_blob=o['blob'],raw_sha256=o['sha256'],encoding=encoding,stored_path=stored,stored_sha256=sha(payload)))
# Preserve exact inherited tar byte stream plus independently verified member identities.
tarraw=(O/'complete-inherited-packet.tar').read_bytes();members={}
with tarfile.open(fileobj=io.BytesIO(tarraw)) as t:
    for m in t.getmembers():
        if m.isfile():members[m.name]=(m,t.extractfile(m).read())
assert set(members)=={e['path'] for e in packet}
for e in packet:
    m,b=members[e['path']];assert sha(b)==e['sha256'] and m.mode==(int(e['mode'],8)&0o777)
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob']
(A/'complete-inherited-packet.tar.gz').write_bytes(gzip.compress(tarraw,mtime=0));(A/'complete-packet-inventory.json').write_bytes((O/'complete-packet-inventory.json').read_bytes())
manifestdoc=dict(schema_version=1,revision=inv['head'],entries=manifest,inherited_packet=dict(path='complete-inherited-packet.tar.gz',encoding='gzip of exact original tar',stored_sha256=sha((A/'complete-inherited-packet.tar.gz').read_bytes()),raw_tar_sha256=sha(tarraw),inventory_path='complete-packet-inventory.json',inventory_sha256=sha((A/'complete-packet-inventory.json').read_bytes()),members=79))
(A/'archive-manifest.json').write_text(json.dumps(manifestdoc,indent=2)+'\n')
originalnote=next(Path(e['original']['snapshot']) for e in inv['paths'] if e['path'].startswith('docs/') and e['path'].endswith('.md'));oldnote=originalnote.read_text()
oldrunner=next(Path(e['original']['snapshot']) for e in inv['paths'] if e['path'].startswith('scripts/'));old=oldrunner.read_text()
# Preserve the entire original healing proof; make only the explicit required recentering insertion.
healing=oldnote.split('## Theorem T2 — the healing bound\n\n',1)[1].split('\n\n*Reading.*',1)[0]
healing=healing[:healing.index(' ∎ (Executed:')]+ ' ∎'
healing=healing.replace('an island `I`','a nonempty finite island `I`',1)
healing=healing.replace('`P(η has a one in F_{D+1}(I)) ≤ |U(I)| ε ≤ 18(D + 1)³ ε`','`P(η has a one in F_{D+1}(I)) ≤ min(1, |U(I)| ε) ≤ min(1, 18(D + 1)³ ε)`')
healing=healing.replace('*The count.* A site','*The count.* Fix an island point `i⁰ ∈ I` and translate every lattice coordinate by `−i⁰`. Since `τ(i⁰)=0`, levels and `D` are unchanged, as are the region cardinality and the noise law. In these translated coordinates each maximum `M_j` is nonnegative, so `M_j ≤ D` and every island point obeys `i_j ≤ D`. The following count is in these translated coordinates. A site')
body=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "Exact point evaluations of the positive six-axis product conditional; a finite nonempty-island eroder and noise union bound for a supplied majority automaton; and a nonnegative directed recurrence comparison under an explicitly supplied coefficient. No interval uniqueness region, model coupling or asymptotic memory threshold is asserted."
upstream_dependencies: [minimal_axioms, admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06]
runner: {runner}
---

# Six-axis point sensitivities, finite-island healing and directed recurrence bounds

**Type:** bounded_theorem

**Status:** bounded-support; supplied mathematical models; unaudited.

## Result up front

The three results below are exact finite arithmetic, a full finite-island proof and a full recurrence comparison proof. The coefficient in the recurrence is supplied. No coupling for a sphere process is constructed by the recurrence calculation. Historical simulation scans are preserved with their actual protocols in the [recovery record](work_history/repo/review_feedback/pr8172-evidence/README.md); they do not establish permanent memory or a transition threshold.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Exact finite identities and conditional bounds for supplied local models."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent affected-source confirmation and bounded runner capture; broader model and threshold claims remain deferred."
conditional_surface_status: "Positive six-axis weights, finite nonempty island, independent Bernoulli noise and nonnegative recurrence coefficient are supplied conditions."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies framework vocabulary. The [finite-window product-rule source](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies the finite six-axis menu and product conditional. Neither selects the weights, synchronous update law, noise or recurrence coefficient as physical. No registered primitive supplies any of those choices.

Let `M={{±e₁,±e₂,±e₃}}`, and let `φ(v,w)` equal positive `p,q,r` for equal, antipodal and orthogonal pairs. Define

`K(v|a,b,c)=φ(v,a)φ(v,b)φ(v,c)/Σ_w φ(w,a)φ(w,b)φ(w,c)`.

For `(q,r)=(1,2)`, let `c(p)` be the maximum total-variation distance of these conditionals over all 216 predecessor triples and five replacements of their first entry. Total variation is half the sum of six absolute coordinate differences.

On `Z³` write `τ(x)=x₁+x₂+x₃`. For the healing result the supplied process is `η_x=maj(η_{{x−e₁}},η_{{x−e₂}},η_{{x−e₃}})∨ζ_x`, with independent Bernoulli(`ε`) noise for `τ≥1`, `0≤ε≤1`. Initially exactly the nonempty finite set `I⊂{{τ=0}}` has value one. Set `M_j=max_{{i∈I}}i_j` and `D=Σ_j M_j≥0`. The nonnegativity follows by comparing the maxima with any island point, whose coordinate sum is zero. Set

`F_T(I)={{x:τ(x)=T, x≥i for some i∈I}}`,

`U(I)={{y:1≤τ(y)≤D+1, y≤x for some x∈F_{{D+1}}(I)}}`.

All coordinate inequalities are componentwise. The empty island is excluded from this definition because its coordinate maxima are undefined. The event refers to a one somewhere in this specified cone, including a noise-created one; it is not genealogical persistence of an original site.

For the recurrence result separately supply `g≥0`, nonnegative arrays `D_t(x)` on level `t`, a level-zero site `x₀`, and

`D₀(x)≤2·1{{x=x₀}}`, `D_{{t+1}}(x)≤g Σ_{{j=1}}^3 D_t(x−e_j)`.

Let `p_t(z)` be the distribution of the sum of `t` independent uniform steps from `{{e₁,e₂,e₃}}`. In plane coordinates,

`p_t(a,b,t−a−b)=t!/[a!b!(t−a−b)!]·3^(−t)`

when all three coordinates are nonnegative integers, and zero otherwise.

## Exact point evaluations

**Statement.** `3c(37/10)=406962630/413162167<1` and `3c(19/5)=871815/862244>1`. These are two point evaluations, not an interval criterion. The explicit small-p check is `3c(1/10)=87/52>1`; failure of this sufficient numerical inequality does not prove nonuniqueness of any process.

**Proof and finite certificate.** Form the six positive weights above for each ordered triple and each replacement, divide by their exact sum, and take half the sum of absolute differences. There are exactly `216·5` comparisons. This exhaustive rational calculation is implemented by `conditional` and `sensitivity` in the paired runner. It evaluates both displayed maxima as reduced fractions; at the first two points a maximizing pair is `(a,b,c)=(e₁,e₁,e₁)` and replacement `a′=−e₁`. At `p=1/10`, predecessors `(e₂,e₁,−e₁)` and replacement `e₃` attain `87/52` after multiplication by three. The finite enumeration verifies the upper maximum as well as these witnesses; no monotonicity inference between or beyond these inputs is used.

For triples with at least two target entries, permutation and cubic symmetry leave three cases: `(a,a,a)`, `(a,a,−a)` and `(a,a,b)` with `b⊥a`. Their probabilities of a non-target value are respectively

`d₁=(q³+4r³)/(p³+q³+4r³)`,

`d₂=1−p²q/[pq(p+q)+4r³]`,

`d₃=1−p²r/[r(p²+q²)+r²(p+q)+2r³]`.

For the first case, the target, antipode and four orthogonal targets have weights `p³,q³,r³`. For the second they have weights `p²q,pq²,r³`. For the third, enumerating the six possible output values gives weights `p²r,q²r,pr²,qr²,r³,r³`. Summing each list and subtracting the normalized target weight proves the formulas.

At `(p,q,r)=(285717,1,2)` the three fractions are `11/7774759963232282`, `285749/81634489838`, `571445/81634775534`; at `(285718,1,2)` they are `33/23324524793166265`, `142875/40817530637`, `571447/81635346971`. Thus their maximum is greater than `7/10⁶` at the first integer and at most that number at the second, by cross multiplication. This note asserts these two evaluations, without extending them to all larger p or applying a phase theorem. ∎

## Finite-island healing theorem

{healing}

The probability of an empty target cone is therefore at least `1−min(1,18(D+1)³ε)`; equality is not asserted. For large D the bound may be vacuous. No ordered-phase hypothesis is needed for this finite assertion. At level t, the third coordinate of a represented site `(a,b)` is `t−a−b`, not `−a−b`.

The region enumerator first translates by an island point. In the normalized coordinates `B=2D+1` is a valid upper bound on all three coordinates. Since `y₁+y₂+y₃=s≥1`, each coordinate is also at least `s−2B≥1−2B`, so the retained wider lower bound `−3B−3` loses no site. A candidate y is in U exactly when `Σ_j max(i_j,y_j)≤D+1` for some i: necessity follows from i,y≤x; conversely raise any coordinate of `max(i,y)` by the nonnegative remaining integer to obtain a level-`D+1` witness x. This proves completeness of the enumeration, including arbitrarily translated islands. The singleton region has three sites; the triangle `{{(0,0,0),(1,0,−1),(0,1,−1)}}` has 76, invariant under a level-zero translation.

## Directed recurrence comparison theorem

**Statement.** Under the explicitly supplied recurrence hypotheses,

`D_t(x)≤2(3g)^t p_t(x−x₀)` and `Σ_{{τ(x)=t}}D_t(x)≤2(3g)^t`.

At `t=0` the right hand side is defined as `2·1{{x=x₀}}`; this also handles `g=0` without an ambiguous power. For `g=0`, all later arrays vanish by the assumed inequality. If `3g<1`, the displayed upper bound decays geometrically.

**Proof.** Define `E₀=2δ_{{x₀}}` and `E_{{t+1}}(x)=gΣ_j E_t(x−e_j)`. Nonnegativity and the initial upper bound give `D_t≤E_t` by induction: the inequality at the next level follows by multiplying each predecessor comparison by g and summing. Expanding the equality recursion, each directed path of length t contributes `2g^t`. A site at displacement `(a,b,c)`, `a+b+c=t`, is reached by exactly `t!/(a!b!c!)` paths; this is the multinomial count from choosing the ordered positions of each of the three steps. Consequently `E_t=2g^t·3^t p_t=2(3g)^t p_t`. Summing the normalized walk law, whose total is one by its product construction, gives the level-sum bound. The support is contained in the forward cone by the same induction. ∎

Substituting `g=β/√3` is only an algebraic specialization, giving `2(√3β)^t p_t`. To use it for a coupled sphere process one must separately prove that process satisfies the supplied recurrence, with its exact hypotheses and input identity. For two arbitrary distinct initial directions the chordal distance is at most two, not necessarily equal to two. No sphere coupling theorem from unlanded work is used here.

## Scope and recovery

The current static six-axis reflection result retains conditional contour implications because parity leaves a dissemination gap. The corrected cubic-walk/sphere-static result supplies `β>76/100` as a sufficient supplied-model condition under its zero-field parent and Gaussian-domination import, not a transition location. The current formation stability construction has its own supplied process and small-noise hypotheses. These comparisons are recorded as context with exact current paths in the recovery appendix; none is a premise of the three proofs here.

All original proofs, proposed broader statements, eight original mutations, five historical control/simulation programs and their full raw outputs, and the 79-entry inherited campaign packet are preserved in the recovery record. The false half-line statement and incomplete coupling application are superseded. Actual asymptotic threshold and broad negative certification remain deferred, with their research content and branch retained. Four historical attempted categories do not become five certified routes. No audit verdict is supplied.

## Verification boundary

[The paired runner](../{runner}) checks exact fractions, the original 300 seeded finite islands and 120 region counts, translated decisive examples, the original polynomial bound and the recurrence through six steps. These finite controls supplement the complete written proofs; they do not establish a universal theorem by check count. Proposed execution is pending. Its five resolution lines distinguish current exact controls from historical simulations and proof-only general statements. The primary never reads or executes historical simulation programs or outputs.
'''
write(W/note,body)
# Narrow source edits retain exact original computational kernels and fixtures.
s=old;docstart=s.index('"""');docend=s.index('"""',docstart+3)+3
s=s[:docstart]+'"""Exact point arithmetic, recentered finite-island controls and a supplied directed recurrence. No simulation or model-coupling execution."""'+s[docend:]
s=s.replace('import random','import hashlib, json\nimport random',1).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 900\nAUDIT_MEMORY_MB = 768',1)
oldnote_path=next(e['path'] for e in inv['paths'] if e['path'].startswith('docs/') and e['path'].endswith('.md'))
s=s.replace(oldnote_path,note).replace(Path(oldnote_path).stem.lower(),cid)
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md']
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','EXPECTED_INPUT_SHA256 = '+repr({p:sha((W/p).read_bytes()) for p in inputs})+'\nROOT = Path(__file__).resolve().parents[1]',1)
s=s.replace('    "claim_reading_injected": "F",\n    "claim_classical_name_in_theorem": "F",','    "translation_origin_wrong": "C",\n    "third_coordinate_wrong": "C",')
s=s.replace('        self.passed = 0','        self.results = []\n        self.passed = 0',1).replace('        if ok:\n','        self.results.append(dict(tag=tag,passed=bool(ok),detail=msg))\n        if ok:\n',1)
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist"','all(Path(ROOT, p).exists() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest()==EXPECTED_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared source/parent pins match"')
s=s.replace('3 * c_lo < 1 < 3 * c_hi,', '3 * c_lo == Fraction(406962630,413162167) and 3 * c_hi == Fraction(871815,862244) and 3 * c_lo < 1 < 3 * c_hi,')
s=s.replace("T1: block 08's criterion at (p, 1, 2):",'Exact point evaluations at (p, 1, 2):').replace("T1: block 25's condition epsilon(p, 1, 2) <= 7/10^6 holds at p = 285718 and fails at 285717 (closed forms of the three deviations)",'The maximum of the three deviations is <=7/10^6 at p=285718 and >7/10^6 at p=285717; two integer evaluations only')
s=s.replace('\n\n# ============================================================================================ family C','\n    checks.check("B3", 3*sensitivity(Fraction(1,10))==Fraction(87,52), "Exact p=1/10 value 3c=87/52; no half-line conclusion")\n\n# ============================================================================================ family C',1)
s=s.replace('def region_size(island3):\n','def region_size(island3):\n    assert island3 and all(sum(i)==0 for i in island3)\n    if not mut("translation_origin_wrong"):\n        origin=min(island3)\n        island3=[tuple(i[j]-origin[j] for j in range(3)) for i in island3]\n',1)
s=s.replace('and max(-a - b for a, b in nxt) <= max(-a - b for a, b in cur)','and max((2 if mut("third_coordinate_wrong") else 1)*t-a-b for a,b in nxt) <= max((2 if mut("third_coordinate_wrong") else 1)*(t-1)-a-b for a,b in cur)',1)
s=s.replace('\n\n# ============================================================================================ family D','\n    examples=[[(0,0,0)],[(0,0,0),(1,0,-1),(0,1,-1)]]\n    translations=[(0,0,0),(100,-100,0),(-73,19,54)]\n    checks.check("C3", all(region_size([tuple(i[j]+v[j] for j in range(3)) for i in I])[0]==expected for I,expected in zip(examples,[3,76]) for v in translations), "Singleton and triangle region counts 3 and 76 under three level-zero translations")\n\n# ============================================================================================ family D',1)
s=s.replace('# stands for beta/sqrt3; the identity is polynomial in g','# explicitly supplied recurrence coefficient; the identity is polynomial in g')
s=s.replace('T3: the influence recursion D_{t+1}(x) = (beta/sqrt3) sum_j D_t(x - e_j) from D_0 = 2 at x_0 is solved exactly by 2 (sqrt3 beta)^t p_t(x - x_0), whose sum over the level is 2 (sqrt3 beta)^t (t <= 6, exact)','Equality majorant E_{t+1}=g sum_j E_t(x-e_j), E0=2 delta, gives 2(3g)^t p_t and total 2(3g)^t through t=6; no sphere coupling tested')
fstart=s.index('# ============================================================================================ family F');fend=s.index('# ============================================================================================ main',fstart)
s=s[:fstart]+'''# Five truthful resolution lines; printing them is not an additional mathematical check.
N5_LINES = (
    "per_element: executed — exact six-axis sensitivities at three rational points and deviations at two integers",
    "per_site: executed — 300 seeded finite islands with true third coordinate and recurrence majorant through six steps",
    "per_mode: executed — 120 recentered region counts, polynomial inequality and translated singleton/triangle cases",
    "per_block: checked and not executed — historical finite simulation protocols and all raw outputs preserved; primary performs no simulation",
    "lattice_wide: checked and not executed — full general eroder, finite noise bound and supplied recurrence proofs; no asymptotic threshold or model-coupling inference",
)
def family_g(checks):
    for line in N5_LINES:
        print(line)


'''+s[fend:]
s=s.replace('    family_f(checks, texts[0])\n','')
s=s.replace('    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")','    output=ROOT/"logs"/"runner-cache"/(Path(__file__).stem+("--"+ACTIVE_MUTATION if ACTIVE_MUTATION else "")+".json")\n    output.parent.mkdir(parents=True,exist_ok=True)\n    output.write_text(json.dumps(dict(checks=checks.results,passed=checks.passed,failed=checks.failed,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=EXPECTED_INPUT_SHA256,mutation=ACTIVE_MUTATION),indent=2)+"\\n")\n    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")')
s=s.replace('# float-scan-marker-line\n','');write(W/runner,s);(W/runner).chmod(0o755);compile(ast.parse(s),runner,'exec')
# Readable correction and protocol scope accompany exact originals, without adopting old claims.
links={e['original_path']:e['stored_path'] for e in manifest}
readme='''# PR8172 exact scientific recovery

All material here is historical or explicitly deferred science, not current claim authority. The canonical note carries full corrected positive proofs; no active proof is hidden in this archive. Original branch retention is required for unique deferred claims and inherited research.

[The manifest](archive-manifest.json) records all 24 original paths, modes, Git blobs and raw SHA256 values. Gzip payloads decode to exact originals, including final newlines; they were not normalized. [The inherited inventory](complete-packet-inventory.json) records all 79 original campaign entries, each recoverable at its original path by decoding [the exact inherited tar](complete-inherited-packet.tar.gz). This archive does not overwrite the shared campaign, adopt any historical certificate or restore generated audit topology.

[Corrected deferred-science and protocol reading](DEFERRED_SCIENCE.md) explains what remains open. The complete original note and programs remain readable below; historical transcripts retain their original claims and errors rather than being retrospectively edited.

## Original files

'''+''.join(f'- `{p}`: [exact recovery]({q})\n' for p,q in links.items())
(A/'README.md').write_text(readme)
deftext='''# Deferred scientific claims and exact historical protocols

This appendix preserves the research boundary and supplies corrections to the historical reading. It is not a current supporting proof for the canonical results. Every original proof is recoverable in full through README and the manifest; none has been replaced by this explanation.

## Corrected versus original conclusions

1. The original p<=3.7 uniqueness region is false as a statement about the numerical criterion: p=0.1 gives 3c=87/52. This does not prove nonuniqueness. Current source keeps exact two-point facts and the explicit small-p counterexample.
2. The full finite healing argument is live after level-zero recentering, true third-coordinate control and a probability cap. The old translated-island count is wrong; original code and its successful-looking outputs remain exact history. The original abandoned 16(D+1)^3 proposal also remains in GOAL; it is not substituted for the proved loose18 bound.
3. The complete recurrence propagation is a valid conditional lemma with supplied g and initial upper bound. The old sphere interpretation requires a separate actual contraction/coupling theorem; its apparent proof imported unlanded work. Reopen only with independently reviewed precise model hypotheses and a landed or copied full proof, not an address.
4. Actual thermodynamic/asymptotic memory thresholds, universal absence claims and the purported one-third threshold ratio are deferred. Finite runs can be descriptive observations at their saved sizes/times only. No equilibration, mixing, error-bar or thermodynamic-limit certificate is supplied. Later memory loss and metastability remain unresolved; this does not show the models never order.
5. Formal negative certification is deferred. The four original categories (finite size; hysteresis/equilibration; memory observable; proved-region comparison) remain the four actual records with their limitations. No fifth attempt or independence certificate is invented. Preserve the original branch.

## Exact protocol coverage

All seed settings describe saved source, not fresh execution. Scans reset their named seed at each process invocation and then share its advancing stream over parameters; the records do not constitute independent replications.

- Formation six-axis scan: seed1, aligned start, synchronous L² updates, fraction of initial value averaged over t>T/2 and final fraction. L128/T4000 has p=4,6,8,10,12,15,18,22,26,30,35,40,50,60,80. L256/T8000 has p=15,18,22,26,30,35 plus a separate fine scan9,10,10.5,11,11.5,12,13.
- Static six-axis heat bath: seed2, checkerboard sweeps, aligned and random starts, majority fraction averaged over the last half. L16/1500 has p=1.5,2,2.5,3,3.5,4,5,6,8 (no3.6 or3.7). L24/1500 has2,2.5,3,3.5,4; L24/2000 fine has3.5,3.6,3.7,3.8,3.9,4; L32/2000 has3.6,3.7,3.8,3.9.
- Static sphere heat bath: seed3, aligned start, magnitude of mean spin averaged over last half. L16/1500 has beta=.5,.6,.65,.7,.75,.8,.9. L24/1500 has .6,.65,.7,.75; L24/2000 fine has .66,.68,.70,.72.
- The single refuter uses one advancing seed31 stream across its sections: random-start formation L128/T4000 p=9,10,11,12,13,15 with majority fraction (different from aligned-value memory); static six-axis checkerboard single-site proposals L16/2000 aligned p=3.4,3.6,3.8,4,4.5 (no3.7); random-start sphere L16/1500 beta=.6,.66,.7,.74,.8; then 400 trials per triangular island side1,2,3,4 on periodic L64 at epsilon=.001.
- The healing refuter actually reads a rectangular superset of the forward cone. For the singleton its 4×4 rectangle has16 sites while the true level-one cone has3. Thus its frequencies .003,.055,.098,.198 are for the saved rectangle event, not a direct frequency test of F. Its uncapped displayed bounds .018,.486,2.250,6.174 become vacuous above1. No output or original label is retroactively changed.
- The original exact control uses seed4, 300 eroder trials and200 counts; the old primary uses seed28,300 islands and120 counts. Their clipped region logic is preserved as failed/generalization-limited history, not reused as a valid translated-region execution.
- Sphere-formation observations mentioned by the old map belong to other research history and do not acquire missing source/input coverage here. The current primary neither executes nor consumes any such simulation evidence.

## Current-main context, not proof premises

The current `ADMISSIBILITY_RULE_STATIC_SIX_AXIS_REFLECTION_IDENTITIES_AND_CONDITIONAL_CONTOUR_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md` preserves the site-reflection parity/dissemination gap; p>=432 is not an unconditional phase theorem. The current `ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md` keeps beta>76/100 only as a sufficient supplied-model corollary of its corrected zero-field parent with Gaussian domination. The current `ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md` proves its own conditional small-noise formation statement; no static phase conclusion is imported. Current source does not require PR8170 or PR8171.

## Complete raw block28 outputs, unchanged

The following transcripts retain original labels, rounded values and execution claims as history. The corrected protocol distinctions above control their interpretation.

'''
for e in inv['paths']:
    if '/specs/' in e['path'] and e['path'].endswith('.out.txt'):
        deftext+='### '+Path(e['path']).name+'\n\n```text\n'+Path(e['original']['snapshot']).read_text()+'```\n\n'
(A/'DEFERRED_SCIENCE.md').write_text(deftext.rstrip()+'\n')
# Immutable handoff artifacts.
(R/'drain8172-author-correction-v1.diff').write_text(''.join(difflib.unified_diff(oldnote.splitlines(True),body.splitlines(True),fromfile=str(originalnote),tofile=note))+''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(oldrunner),tofile=runner)))
maprows=[]
for e in manifest:
    target=note if e['original_path']==oldnote_path else runner if e['original_path'].startswith('scripts/') else None
    maprows.append(dict(original_path=e['original_path'],original_mode=e['original_mode'],original_blob=e['git_blob'],original_sha256=e['raw_sha256'],recovery=(archive/e['stored_path']).as_posix(),recovery_encoding=e['encoding'],disposition='Narrowed and corrected positive science; full original exact recovery' if target else 'Historical/deferred exact recovery; no active authority; generated topology superseded where applicable',final_path=target,final_sha256=sha((W/target).read_bytes()) if target else None))
(R/'drain8172-author-full-mapping-v1.json').write_text(json.dumps(maprows,indent=2)+'\n')
oldast={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(old).body if isinstance(n,ast.FunctionDef)}
newast={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
same=[k for k in oldast if k in newast and oldast[k]==newast[k]]
(R/'drain8172-author-preservation-v1.json').write_text(json.dumps(dict(original_files=24,inherited_files=79,exact_originals_verified=True,exact_inherited_tar_and_members_verified=True,unchanged_function_asts=same,preserved_full_healing_proof='Original full proof with explicit nonempty domain, level-zero recenter insertion and capped probability; no formula stripping',formula_changes=['True third coordinate t-a-b','Explicit recenter before original complete region box','Exact point equalities and p=1/10 counterexample','Supplied nonnegative recurrence with initial <=2 delta; no model coupling import'],historical_mutations=8,current_math_mutations=8,retired_prose_mutations=['claim_reading_injected','claim_classical_name_in_theorem'],new_correction_mutations=['translation_origin_wrong','third_coordinate_wrong'],primary_executions=0),indent=2)+'\n')
print(note);print(runner);print('unchanged ASTs',same)
