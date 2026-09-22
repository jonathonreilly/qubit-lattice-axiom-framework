from pathlib import Path
import re,json,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author8146';rows=json.loads((R/'drain8146-author-original-map-draft.json').read_text());notes={x['pr']:x['original'] for x in rows if x['original'].startswith('docs/ADMISSIBILITY') and x['original'].endswith('.md')}
def field(s,k,t):return re.sub('^'+k+':.*$',k+': '+json.dumps(t),s,flags=re.M)
def section(s,start,end,t):a=s.index(start);b=s.index(end,a);return s[:a]+t+'\n\n'+s[b:]
p=W/notes[8139];s=p.read_text();s=field(s,'next_trace_action','Use the explicit DLR specification, containing graph, conditional and TV witnesses, and the covariant probability mixture. Certification of excluded nearest-neighbor Markovity and separation from every static Gibbs law is deferred with its full original proof archived.')
s=field(s,'conditional_surface_status','L1 full-exterior DLR identity and R1 containing graph hold in the c<1/3 constructed-law region; explicit diagonal dependence and mixed-ratio witnesses retain their stated hypotheses. R2 universal static-law/graph exclusion is deferred. R3 eight-law distinctness at (3,1,2); family covariance throughout the region; finite R4 witnesses unchanged.')
s=field(s,'claim_type_reason','Finite exterior-cylinder identities pass to the limit; L2 is full-support conditional uniqueness; explicit kernels, mixed ratios and finite TV witnesses support the retained constructions. R2 exclusion certification is deferred.')
s=s.replace('The full-support conditional argument proves the conditional\nseparation stated below; it does not classify all parameter triples.','The full-support conditional lemma and exact kernel witnesses are retained;\nthe universal static-law exclusion previously inferred from them is deferred.')
s=s.replace('law determines its finite-range specification (R2), so `μ_κ` is not a\nnearest-neighbor Markov field and differs from every static Gibbs law;','law determines its finite-range specification (L2); the universal exclusion\nformerly stated in R2 is deferred;')
s=s.replace('separation from every static Gibbs law on `Z^3` through the Markov graph and a\nfull-support uniqueness lemma (R2);','explicit conditional discrepancy and full-support conditional uniqueness (L2);')
s=re.sub(r'^\| R2:.*$', '| R2 universal static-law and nearest-neighbor graph exclusion | deferred; exact conditional/mixed-ratio witnesses retained |',s,flags=re.M)
a=s.index('The strongest missing lemma');b=s.index('## Lemma L1',a)
s=s[:a]+'''The nonzero third differences at the two declared triples are finite
witnesses. The exceptional-construction note displays nonconstant points with
vanishing third differences; its exhaustive-locus conclusion is deferred.
R3 opposite-corner distinctness remains confined to `(3,1,2)`.

'''+s[b:]
s=s.replace('| the third difference nonzero at every nonconstant triple; the eight laws\' distinctness outside the region; affine independence of the eight laws | open; not this note |','| nonzero third difference at every nonconstant triple | false at the displayed exceptional constructions; no exhaustive claim |\n| eight laws outside the witnessed parameter; affine independence | open |')
s=section(s,'## Theorem R2','## Theorem R3','''## R2 — retained conditional witnesses; exclusion certification deferred

R1 gives an explicit single-site conditional and the exact nonzero
face-diagonal TV witness at `(3,1,2)`. The third-difference ratios are
`2160/2197` at `(3,1,2)` and `686196/704969` at `(5,2,4)`, with ratio one
at the constant control. L2 supplies the conditional-uniqueness lemma.

The original conclusion excluding nearest-neighbor Markovity and every static
Gibbs law, and its full inference proof, are preserved byte-exact under PR8139
in the history manifest. Their negative certificate remains incomplete and
that universal exclusion is not asserted as a current certified conclusion.
The constructive DLR identity, containing graph and finite witnesses stand
within their explicit hypotheses.''')
s=s.replace('of R2 is the plane-law note\'s statement','of the conditional witness is the plane-law note\'s statement')
s=s.replace('### N1 — Route coverage\n','### N1 — Route coverage\nThe specifically deferred conclusions are R2 exclusion of nearest-neighbor\nMarkovity and separation from every static Gibbs law.\n')
s=s.replace('  L2 (uniqueness of finite-range kernels under full support), R1–R4.','  L2 (uniqueness of finite-range kernels under full support), R1 and the\n  stated finite R3–R4 witnesses; R2 exclusion certification is deferred.')
p.write_text(s)
p=W/notes[8141];s=p.read_text();s=field(s,'claim_scope','For a finite window with supplied total formation order and positive six-axis product rule: exact recorded-set factorization, containing Markov graph, vacuum-normalized potential and maximal-set mixed-difference identities. Exact plaquette/star and mixed-ratio witnesses at the declared triples. A nearest-neighbor graph suffices when every recorded set has at most one element. The converse/minimal-graph and excluded-graph conclusions are explicitly deferred; their full original proof is archived.')
s=s.replace('# Every formation law is a Gibbs law whose Markov graph is the recorded-set graph: nearest-neighbor Markov exactly when no site records two neighbors','# Recorded-set Gibbs factorization, a containing graph and exact potential witnesses')
a=s.index('always contains a valid Markov graph.');b=s.index('\nExactly:',a)
s=s[:a]+'''always contains a valid Markov graph. The explicit maximal-set potential
identities and mixed-ratio witnesses are retained. Certification of the
converse nearest-neighbor criterion and excluded-graph/minimality conclusions
is deferred; the sufficient direction is retained.
''' +s[b:]
s=s.replace("under T4's nonzero maximal-set hypothesis, nearest-neighbor Markov iff `max_x |A_x| ≤ 1`",'T4 retains the sufficient nearest-neighbor condition; its converse is deferred')
s=field(s,'next_trace_action','Use the recorded-set factorization, containing graph and explicit potential identities. The converse nearest-neighbor criterion and excluded-graph/minimality certification remain deferred with original proofs preserved.')
s=field(s,'conditional_surface_status','T1 and T2 finite-window factorization and containing graph; T3 potential identities under stated hypotheses; T4 sufficient direction only; T5 range bound and conditional body-count identities; exact T6 potential witnesses. Converse and excluded-graph certification deferred.')
s=s.replace('T4 combines T3 with the bipartite structure of the lattice','T4 retains the sufficient condition only')
s=s.replace('dimensions and, on `Z^3`, the Markov graph and the separation from static laws.','dimensions and, on `Z^3`, the containing graph and conditional witnesses;\ncurrent certification of the static-law exclusion is deferred.')
s=s.replace('the classification of nearest-neighbor\nMarkov formation laws (T4)','the sufficient nearest-neighbor condition (T4)')
s=re.sub(r'^\| T4 nearest-neighbor.*$', '| T4 sufficient nearest-neighbor condition | proved when every recorded set has size at most one; converse/excluded-graph certification deferred |',s,flags=re.M)
a=s.index('The strongest missing lemma');b=s.index('\n## Theorem T1',a)
s=s[:a]+'''The mixed differences are witnessed nonzero at the two declared triples.
Nonzero at every nonconstant triple is not a valid general premise: the
exceptional-construction note supplies three-body zero examples. The
higher-body identities retain their explicit nonvanishing hypotheses.
''' +s[b:]
s=section(s,'## Theorem T4','## Theorem T5','''## Theorem T4 — a sufficient nearest-neighbor condition

**Statement.** If every recorded set of `σ` has at most one element, `μ_σ`
is a Markov field for `E(W)`.

*Proof.* T1 has no normalizer term, so `G_σ=E(W)` and T2 applies. ∎

The original converse, excluded-graph conclusion and minimality inference,
including the full proof with its nonzero maximal-set hypotheses, are retained
byte-exact under PR8141 in the history manifest. Their negative certificate
is incomplete, so those conclusions are deferred. T3's explicit potential
formula and finite nonzero mixed-ratio witnesses remain live.''')
s=s.replace('diagonal `{b, c}`, not for the plaquette — the two-dimensional diagonal','diagonal `{b, c}` — an explicit two-dimensional diagonal')
s=s.replace('Theorem B), while the same tree swept leaves-first is not (T4).','the sufficient condition), while the leaves-first order has the displayed\nnonzero three-body potential witness. The excluded-graph inference is deferred.')
s=s.replace('### N1 — Route coverage\n','### N1 — Route coverage\nThe specifically deferred conclusions are the T4 converse/iff criterion and\nthe excluded-graph/minimality conclusions.\n')
s=s.replace("would refute T4's use of bipartiteness","would refute the stated lattice pair geometry")
p.write_text(s)
p=W/notes[8138];s=p.read_text().replace("(an edge 'clause-needed' for long-range record fields under positive product rules)",'(quantitative single-site covariance bounds only)');p.write_text(s)
p=W/notes[8146];s=p.read_text().replace('it has\nno majority and no error correction.','this is the stated two-parent limiting choice rule.');parent='docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md'
s=s.replace('### Linked source authority\n','### Linked source authority\n\n- [Monotone rectangle formation law]('+Path(parent).name+'): P1 supplies the prescribed rectangle law, P4 its row/column K-chains, and the finite rectangle consistency identity supplies the selected extension.\n')
s=s.replace('Admissibility Rule Three Body Term Exceptional Locus Exact Classification Bounded Theorem Note 2026-09-15]('+Path(notes[8142]).name+'): only its explicit hypotheses and conclusions are used.','Admissibility Rule Three Body Term Exceptional Locus Exact Classification Bounded Theorem Note 2026-09-15]('+Path(notes[8142]).name+'): only the five explicit triple-pattern formulas are used here; exhaustive classification is deferred.')
p.write_text(s)
# Scope-only paired runner changes; numerical domains preserved.
p=W/'scripts/admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15.py';s=p.read_text().replace('under which the law is not nearest-neighbor Markov and not a static law','retained as exact mixed-ratio witnesses; universal graph/static exclusions deferred').replace("R2's hypothesis:","R2 retained mixed-ratio witness:").replace('title.startswith("Theorem R2")','title.startswith("R2")');s=s.replace('lattice_wide: proved from L1–L2 in block 08\'s region at triples with nonzero third difference; executed only at (3,1,2) and (5,2,4); nothing claimed elsewhere','lattice_wide: DLR and containing graph in the stated region; witnessed corner distinctions only; universal static-law and excluded-graph certification deferred');p.write_text(s)
p=W/'scripts/admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_2026_09_15.py';s=p.read_text().replace('lattice_wide: proved on every finite window at triples with nonzero mixed differences (executed at two); infinite volume only by citation of blocks 08–09 for the monotone class','lattice_wide: finite-window factorization, containing graph and potential identities; converse and excluded-graph certification deferred');p.write_text(s)
p=W/'scripts/admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15.py';s=p.read_text();s=s.replace('AUDIT_INPUT_PATHS = (','AUDIT_INPUT_PATHS = (',1);a=s.index('\n)\nROOT =',s.index('AUDIT_INPUT_PATHS'));s=s[:a]+'\n    "'+parent+'",'+s[a:]
s=s.replace('AXIOM_NEEDLES = (','BLOCK05_CLAIM_ID = "'+Path(parent).stem.lower()+'"\nBLOCK05_FRAGMENT = "every row and every column"\nAXIOM_NEEDLES = (',1)
s=s.replace('b08: str, b09: str) -> None:','b08: str, b09: str, b05: str) -> None:')
s=s.replace('len(set(AUDIT_INPUT_PATHS)) == 4','len(set(AUDIT_INPUT_PATHS)) == 5').replace('the four declared inputs exist (this note, the axiom memo, block 08, block 09)','the five declared inputs exist (this note, axiom memo, plane-chain and DLR notes, actual rectangle premise)')
s=s.replace('BLOCK09_CLAIM_ID in f09,','BLOCK09_CLAIM_ID in f09 and BLOCK05_CLAIM_ID in b05 and BLOCK05_FRAGMENT in normalize_text(b05).lower(),')
s=s.replace("the parents' claim ids and block 08's strong-coupling fragment are present","actual parent claim ids, strong-coupling context and rectangle row/column proof identity are present")
s=s.replace('family_a(checks, texts[0], texts[1], texts[2], texts[3])','family_a(checks, texts[0], texts[1], texts[2], texts[3], texts[4])');p.write_text(s)
for path in W.glob('scripts/admissibility_rule_*2026_09_15.py'):ast.parse(path.read_text())
print('v3 scope and actual S5 input repairs saved')
