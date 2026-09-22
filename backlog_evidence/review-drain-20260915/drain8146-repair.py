from pathlib import Path
import json,gzip,hashlib,subprocess,re
R=Path('/private/tmp/review-drain-20260915'); W=R/'drain-author8146'
rows=json.loads((R/'drain8146-author-original-map-draft.json').read_text())
notes={row['pr']:row['original'] for row in rows if row['original'].startswith('docs/ADMISSIBILITY') and row['original'].endswith('.md')}
# Every original occurrence remains byte-exact, including superseded live science.
for row in rows:
 if row.get('encoding')!='gzip':
  b=subprocess.check_output(['git','show',row['head']+':'+row['original']],cwd=W)
  assert hashlib.sha256(b).hexdigest()==row['sha256']
  dst=Path('docs/work_history/review_loop/pr8146')/str(row['pr'])/(str(row['pr'])+'_'+Path(row['original']).name+'.gz')
  (W/dst).parent.mkdir(parents=True,exist_ok=True); (W/dst).write_bytes(gzip.compress(b,mtime=0))
  row['live_path']=row['stored'];row['stored']=str(dst);row['encoding']='gzip'
for row in rows:
 b=gzip.decompress((W/row['stored']).read_bytes());assert hashlib.sha256(b).hexdigest()==row['sha256']
 row['archive_sha256']=hashlib.sha256((W/row['stored']).read_bytes()).hexdigest()
(R/'drain8146-author-original-map-draft.json').write_text(json.dumps(rows,indent=2)+'\n')
(W/'docs/work_history/review_loop/pr8146/original-manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
def edit(pr,fn):
 p=W/notes[pr];s=p.read_text();s=fn(s);p.write_text(s)
def rep(s,a,b):
 assert a in s,a[:100];return s.replace(a,b)
def scope(s,v):return re.sub(r'^claim_scope:.*$', 'claim_scope: '+json.dumps(v),s,flags=re.M)
def negative(s,pr):
 a=s.index('## No-Go Discipline Gate');b=s.index('## Falsifiers',a)
 return s[:a]+f'''## No-Go Discipline Gate — deferred broader certification

This revision retains the constructive identities, quantitative bounds and named
finite witnesses above. It does not certify the broader exclusion claims in the
original packet. The original N1–N8 text and every recovery route are preserved
byte-exact in [the PR8146 history manifest](work_history/review_loop/pr8146/original-manifest.json)
under PR{pr}; the original branch remains a recovery handle for unlanded work.

### N1 — Route coverage
The original list includes unattempted and out-of-domain routes. It is not a
completed route search; broader negative certification is deferred.

### N2 — Walls
The positive weights, six-axis menu, product rule and specified formation class
remain supplied conditions, not deductions or selected physical inputs.

### N3 — Hidden walls
The statements above carry their finite-window, parameter, nonvanishing and
invariance hypotheses explicitly. No unrestricted exclusion follows.

### N4 — Citation scope
Linked source arguments support only their stated mathematical hypotheses.
Historical branch review and cache records are provenance, not authority.

### N5 — Resolution
Exact finite witnesses and the proved formula domains remain as stated above.
They do not establish exhaustive route, phase or infinite-law classification.

### N6 — Partial closure
The positive results are preserved. Unproved exclusions remain open with their
original attempted routes recoverable; no new premise closes them.

### N7 — Steelman
A quantitative bound or finite discrepancy does not settle every alternative
law or order. This revision concedes that gap rather than asserting closure.

### N8 — Recovery
The history manifest binds original heads, paths, decompressed SHA256 hashes and
archive hashes. This deferred certificate is not a passing negative-claim gate;
any future broader exclusion must complete the applicable discipline.

'''+s[b:]
def common(s,pr):
 s=negative(s,pr)
 return s
# 8146
s=(W/notes[8146]).read_text()
s=scope(s,'For the positive six-axis product rule and supplied monotone formation class: exact level-time kernel; correspondence between spatially invariant stationary level laws and fully translation-invariant formation laws; closed noise formulas; strict majority preference across both 2:1 patterns iff p > max(q,r) and p^2 q > r^3; finite-island eroder bound; stochastic domination; finite nonempty cross-section metastability. The prescribed consistent two-dimensional rectangle family has a unique extension and exponential row/column correlations. No classification of all two-dimensional stationary laws or diagonal order is proved. The three-dimensional ordered phase remains conditional on the explicitly unproved stability obligation. Broader negative certification is deferred.')
s=rep(s,'records become traps. In two dimensions none of this happens: with only two\nearlier neighbors there is no majority, no error correction, and no ordered\nphase at any coupling.','records become traps. For the prescribed two-dimensional rectangle-law\nextension, row and column correlations decay at every positive coupling. With\nonly two earlier neighbors its limiting update chooses between distinct parents;\nthis does not classify all stationary laws or diagonal correlations.')
s=s.replace('invariant laws ↔ translation-invariant `Z^3` laws','spatially invariant stationary laws ↔ translation-invariant `Z^3` laws').replace('S5 two dimensions never order','S5 prescribed rectangle extension and axial correlation bound')
s=rep(s,'and its stationary two-sided\nchains are exactly the `Z^3`-translation-invariant laws','and its stationary two-sided\nchains with spatially translation-invariant level marginals are exactly the `Z^3`-translation-invariant laws')
s=rep(s,'same kernel, so a stationary two-sided level chain is invariant under all\ntranslations of `Z^3`, and conversely a translation-invariant law of the\nprocess is a stationary level chain.','same kernel. Stationarity gives invariance under this time shift; spatial\ntranslation invariance of the level marginal gives invariance under the two\nlevel-preserving generators. These three generators span all translations of\n`Z^3`. Conversely a fully translation-invariant formation law supplies both\ninvariances. An arbitrary stationary level law alone gives only time-shift\ninvariance, not spatial invariance.')
s=rep(s,'its most likely output iff `p > max(q, r)`.','its strictly most likely output across both patterns iff\n`p > max(q, r)` and `p² q > r³`.')
s=rep(s,'which holds\nwhen `p > max(q, r)`.','an additional condition not implied\nby `p > max(q, r)`. For example `(p,q,r)=(3,1/100,2)` has majority weight\n`9/100` below each orthogonal weight `8`. Combining the two patterns gives\nexactly the two stated strict inequalities.')
s=s.replace('condition on the two sides of `p = max(q, r)` (B4).','condition on both strict boundaries and the rational counterexample (B4).')
s=s.replace('For every finite cross-section `C` and every positive coupling','For every finite nonempty cross-section `C` and every positive coupling')
s=s.replace('## Theorem S5 — two dimensions never order','## Theorem S5 — the prescribed rectangle extension and axial correlation bound')
s=rep(s,'rectangle law; its plane extension by projective consistency) is unique at\nevery positive coupling,','rectangle law) has a unique plane extension with those prescribed rectangle\nmarginals at every positive coupling,')
s=rep(s,'so its plane extension is unique. The row','so its extension with those rectangle marginals is unique. This is not a\nuniqueness theorem for every stationary law of the two-predecessor automaton,\nnor a claim about diagonal order. The row')
s=s.replace('a coupling with `p > max(q, r)` at which','a coupling satisfying both `p > max(q, r)` and `p² q > r³` at which')
s=s.replace('no value, constant or theorem is imported as authority.','the probability and spectral results listed under Imports are mathematical inputs, not physical premises.')
s=s.replace('- Re-proved at scope: S0–S5.','- Mathematical imports: countable extension of consistent finite-dimensional laws on the finite-alphabet product space; existence of stationary two-sided Markov chains from invariant marginals; weak compactness and the Cesàro invariant-measure argument for a Feller kernel on a compact product space; continuity of roots of finite characteristic polynomials. Their hypotheses are the finite alphabet, positive local transition probabilities, finite dependence of each cylinder update, and (for the spectral argument) a finite nonempty cross-section. These are used as mathematical theorems, not merely definitions.\n- The exact algebra, eroder bound and coupling are proved above. The stability theorem in S6 remains an unproved conditional obligation.')
s=common(s,8146);(W/notes[8146]).write_text(s)
# 8139
s=(W/notes[8139]).read_text()
s=scope(s,'Under the supplied positive six-axis product rule and monotone formation class, for c < 1/3 the constructed infinite laws satisfy the finite-range DLR specification. The explicit single-site formula and full-support conditional uniqueness yield a containing Markov graph; genuine diagonal dependence is conditional on the stated nonzero mixed differences. The eight corner laws are proved distinct at (3,1,2), including the exact opposite-corner witness; no all-parameter opposite-corner distinctness is asserted. Covariance of the family and its equal probability mixture hold throughout c < 1/3. Exact finite-column irreversibility witnesses remain. Ergodic decomposition and broader negative certification are not established here.')
a=s.index('Hence, for every such box,');b=s.index('\n## Lemma L2',a)
s=s[:a]+'''For any fixed exterior cylinder event `E` (supported outside `Λ`), choose the
box also to contain its finite support. Multiplying the conditional identity by
`1_E` and integrating gives
`E_{μ^κ_B}[1_E 1_{v_Λ=a}] = E_{μ^κ_B}[1_E γ^κ_Λ(a | v_{∂Λ})]`.
Both integrands depend on finitely many coordinates. Finite-window convergence
therefore passes this identity to `μ_κ` for every exterior cylinder event.
The exterior cylinders form a generating π-system; equality of the two finite
measures extends to the entire exterior sigma algebra. Thus `γ^κ_Λ` is a
version of the conditional law given the full exterior, which is the DLR
identity. The displayed continuous kernel is defined for every exterior
configuration; conditional-law equality is almost sure. ∎
''' + s[b:]
s=rep(s,'**(b) Distinctness.** For `c < 1/3` at a triple with nonzero third difference,\nthe eight laws `μ_κ` are pairwise distinct.','**(b) Distinctness at the witnessed triple.** At `(p,q,r)=(3,1,2)`, where\n`c < 1/3`, the eight laws `μ_κ` are pairwise distinct. The following proof\ndoes not assert opposite-corner distinctness at every nonzero-third-difference triple.')
a=s.index('invariant (block 08\'s axis symmetry, Q1c);');b=s.index('\n## Theorem R4',a)
s=s[:a]+'''invariant (block 08's axis symmetry, Q1c). At `(3,1,2)`, (b) excludes every
other proper rotation. Throughout `c < 1/3`, the equal mixture
`μ̄ = (1/8) Σ_κ μ_κ` is a probability law invariant under all proper cubic
rotations, axis reflections and translations: these transformations permute
its summands. This is a mathematical construction; the supplied axioms do not
select its physical adoption. Single-site covariance decay alone does not
prove full translation mixing or an eight-component ergodic decomposition;
no such decomposition is claimed here. ∎
''' + s[b:]
s=rep(s,'**(a) On `Z^3`.** For `c < 1/3` at a triple with nonzero third difference,','**(a) On `Z^3` at the witnessed triple `(3,1,2)`.**')
s=s.replace('The result says only that any single monotone\norder leaves its direction readable in the record statistics, exactly and\nwithout a clock.','At the witnessed triple each of the eight supplied classes leaves a\ndistinct record law. This statement is not extended to every parameter triple.')
s=common(s,8139);(W/notes[8139]).write_text(s)
# 8138
s=(W/notes[8138]).read_text()
s=scope(s,'For the supplied positive six-axis product rule and monotone class: exact finite-box factorization and symmetry; finite discrepancy witnesses; positive finite-cross-section plane chain and its unique stationary law; under c < 1/3 the constructed infinite law and single-site exponential covariance bounds. Three-body irreducibility is conditional on a nonzero third mixed difference, witnessed at (3,1,2) and (5,2,4), not every nonconstant triple. Rotations map corner laws covariantly; distinctness is not inferred from covariance. Broader negative certification is deferred.')
s=s.replace('**(f) The three-body normalizer is irreducible.** At a nonconstant triple','**(f) Witnessed three-body irreducibility.** At a triple with nonzero third mixed difference')
a=s.index('`μ_{Z^3}` is not\ninvariant under');b=s.index(' ∎',a)
s=s[:a]+'''Rotations and axis reflections map `μ_{Z^3}` to the law of the transformed
corner class. This is covariance of the family; distinctness of the images
requires a separate argument. At the constant rule all images are the same
independent uniform law.''' + s[b:]
a=s.index('Under the monotone\nformation law',s.index('## Corollary Q5'));b=s.index('\n## No-Go Discipline Gate',a)
s=s[:a]+'''This is a quantitative statement about single-site record observables in the
specified class and parameter region. It does not classify other observables,
formation classes or added dynamics. For coincident sites use the trivial bound
`|Cov(g,h)| ≤ 2 ‖g‖ ‖h‖`; at `c=0` distinct sites are independent (the
conditional is neighbor-independent), so their covariance is zero. This avoids
an undefined `0` raised to a nonpositive exponent at short separation.
''' +s[b:]
s=common(s,8138);(W/notes[8138]).write_text(s)
# 8141
s=(W/notes[8141]).read_text()
s=scope(s,'For a finite window with supplied total formation order, positive six-axis product rule and records-only reading: exact recorded-set factorization and a containing Markov graph; vacuum-normalized potential and its maximal recorded-set terms. The converse minimal-graph and genuine k-body conclusions require nonzero mixed differences on every maximal recorded-set size that occurs, verified at (3,1,2) and (5,2,4). A nearest-neighbor graph suffices whenever every recorded set has size at most one. Exact plaquette and star witnesses remain; broader negative certification is deferred.')
s=s.replace('## Theorem T4 — nearest-neighbor Markov exactly when no site records two neighbors','## Theorem T4 — the converse graph criterion under nonzero maximal-set differences')
s=s.replace('A site with all six neighbors recorded (formed last in its\nneighborhood) carries a six-body term.','Under that nonzero sixth-difference hypothesis, a site with all six\nneighbors recorded (formed last in its neighborhood) carries a six-body term.')
s=common(s,8141);(W/notes[8141]).write_text(s)
# 8142
s=(W/notes[8142]).read_text()
s=scope(s,'For the positive six-axis product rule modulo scale, exact classification of all six parameter points with pair-additive three-neighbor log normalizer: the constant point and five nonconstant exceptional points, with exact polynomial isolation and sufficiency checks. The p=q family factors through the three unsigned axes; the p=r family retains six letters and has three triple-pattern values, not a three-letter quotient. At the nonconstant exceptional points the pair component is nonzero. Opposite corner single-site specifications coincide there; this does not prove equality or distinctness of infinite laws. Infinite-law discussion requires c < 1/3. Broader negative certification is deferred.')
a=s.index('pairs, and the vacuum-normalized pair term');b=s.index('\n*Proof.*',a)
s=s[:a]+'''pairs, and the vacuum-normalized pair term `Δ_2 g` is nonzero. This is a
pair-potential conclusion. In the constructed infinite-law region `c < 1/3`,
the opposite corners `κ` and `−κ` have the same six diagonal sites, and their
pair-additive denominators give the same single-site specification. A common
specification alone proves neither equality nor distinctness of infinite laws.
No eight-law distinction follows at these exceptional points, and no statement
about higher maximal-set differences follows from this three-body calculation.
''' +s[b:]
s=s.replace('dependence of block 09\'s R1 then comes from `Δ_2 g` in place of the mixed\nsecond difference of `log K_3`; the rest follows verbatim.','pair dependence comes from `Δ_2 g`. For opposite corners, each diagonal\npair contribution appears with the same multiplicity because their diagonal\nsets agree; regrouping a pair-additive triple sum does not change the\nsingle-site denominator. The stronger law-distinctness inference is not made.')
s=common(s,8142);(W/notes[8142]).write_text(s)
# Correct the sole numerical assertion being changed. No runner is executed.
p=W/'scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py';s=p.read_text()
s=s.replace('condition p > max(q, r).','condition p > max(q, r) and p**2*q > r**3.')
a=s.index('    # B4:');b=s.index('    # B5:',a)
s=s[:a]+'''    # B4: strict majority for both patterns needs both exact inequalities.
    def majority_most_likely(tr):
        rule = Rule(tr)
        c1 = rule.cond((x, x, y))
        c2 = rule.cond((x, x, mx))
        return c1[x] > max(c1[s] for s in range(M) if s != x) and c2[x] > max(c2[s] for s in range(M) if s != x)
    preference_triples = ((3, 1, 2), (2, 1, 3), (1, 2, 1), (2, 2, 1),
                          (3, F(1, 100), 2), (2, 2, 2), (4, F(1, 2), 2))
    pref = all(majority_most_likely((p, q, r)) ==
               (p > max(q, r) and p*p*q > r*r*r)
               for p, q, r in preference_triples)
    if mut("majority_preference_wrong"):
        pref = majority_most_likely((3, F(1, 100), 2))
    checks.check("B4", pref, "S1: strict majority across both 2:1 patterns iff p > max(q,r) and p^2*q > r^3; exact samples include the small-q counterexample and equality boundaries")
''' +s[b:];p.write_text(s)
print('Draft edits saved; original archives verified',len(rows))
