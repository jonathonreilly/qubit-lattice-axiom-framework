from pathlib import Path
import json,re
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author8146'; rows=json.loads((R/'drain8146-author-original-map-draft.json').read_text());notes={x['pr']:x['original'] for x in rows if x['original'].startswith('docs/ADMISSIBILITY') and x['original'].endswith('.md')}
def replace(s,a,b):
 assert a in s,a[:90]; return s.replace(a,b)
s=(W/notes[8139]).read_text();a=s.index('Take the three-dimensional');b=s.index('\nExactly:',a)
s=s[:a]+'''The constructed three-dimensional formation laws have an explicit finite-range
conditional specification. At the witnessed triple `(3,1,2)`, changing a
face-diagonal record changes a site's conditional, and all eight corner laws
are distinct. The full-support conditional argument proves the conditional
separation stated below; it does not classify all parameter triples. Rotations
permute the corner laws, and their equal mixture is a probability law invariant
under those rotations. This construction supplies no physical selection of an
order or mixture. Exact finite-column joint laws also witness sweep reversal.
''' +s[b:]
s=s.replace('the\neight `μ_κ` are pairwise distinct (R3;','at `(3,1,2)` the\neight `μ_κ` are pairwise distinct (R3;')
s=s.replace('the mixture of eight laws, not a law','the equal probability mixture of eight corner laws, without physical selection')
s=s.replace('R3 proved (dependency sets) with the within-pair witness executed at (3,1,2)','R3 distinctness proved at (3,1,2); covariance of the family throughout the region')
s=s.replace('R1–R2 proved for every corner and every triple in block 08\'s region','R1 containing graph throughout the region; genuine diagonal dependence and R2 separation require the stated nonzero mixed difference')
s=s.replace('R4 executed on the 2x2 column at three triples and proved on Z^3 through R3','R4 executed on the 2x2 column at three triples and proved on Z^3 at (3,1,2) through R3')
s=s.replace('R2 and R3 are stated\nat triples where it is nonzero.','R2 requires the indicated nonzero difference; R3 opposite-corner\ndistinctness is confined to the witnessed triple.')
s=s.replace('the ergodic\ndecomposition are classical references re-proved or cited at the scope used;\nno value, constant or theorem is imported as authority.','finite-measure uniqueness theorem are mathematical inputs at the stated\nscope; no ergodic decomposition is claimed.')
a=s.index('- Cited, definition-level:');b=s.index('\n## Review record',a)
s=s[:a]+'''- Mathematical imports: existence and almost-sure uniqueness of conditional
  probabilities on finite-alphabet countable product spaces; uniqueness of
  finite measures agreeing on a generating π-system, used to extend the
  exterior-cylinder identity to the full exterior sigma algebra. Finite range
  makes the tested functions cylinder functions; positivity gives full support
  for the pointwise comparison. These are probability theorems, not definitions.
- The pointwise ergodic theorem and ergodic decomposition are not used here.
''' +s[b:];(W/notes[8139]).write_text(s)
s=(W/notes[8141]).read_text();a=s.index('Those extra pairs are never lattice');b=s.index('\nExactly:',a)
s=s[:a]+'''Those extra pairs are never lattice neighbors themselves. The displayed graph
always contains a valid Markov graph. Its minimality and genuine maximal-set
couplings require the nonzero mixed-difference hypothesis in T4, verified at
the two declared triples. Under that hypothesis nearest-neighbor Markovity is
equivalent to every recorded set having size at most one. Without it, only
the sufficient direction and the containing graph are asserted.
''' +s[b:];s=s.replace('nearest-neighbor Markov iff `max_x |A_x| ≤ 1` (T4)','under T4\'s nonzero maximal-set hypothesis, nearest-neighbor Markov iff `max_x |A_x| ≤ 1`')
s=s.replace('any single order induces a longer-range law than the rule','the containing graph and conditional minimality criterion')
s=s.replace('for T1, T2, T4\'s forward direction and T5','for T1, T2, T4\'s forward direction and the range bound in T5')
(W/notes[8141]).write_text(s)
s=(W/notes[8142]).read_text();a=s.index('Two settings where');b=s.index('Surprisingly',a)
s=s[:a]+'''On `p=q`, the rule factors through the three unsigned axes. On `p=r`,
the six-letter rule still distinguishes an antipodal partner, but its triple
normalizer has three pattern values; this is not a three-letter quotient.
Each line has one extra algebraic weight ratio where the third difference
vanishes; `q=r` is the parameter-swapped counterpart. '''+s[b:]
s=s.replace('even at the six points the two-way couplings across faces\nsurvive, so the earlier conclusions about what a site listens to still hold\nthere','at the five nonconstant exceptional points the pair component\nsurvives. This does not establish eight distinct infinite laws there')
s=s.replace('and their Markov-graph conclusions hold everywhere nonconstant through the pair part','and X4 retains the nonzero pair component, without an eight-law distinction or higher-body inference')
s=s.replace('proved (the same collapse with a different quotient)','proved (three triple-pattern values on the six-letter menu)')
(W/notes[8142]).write_text(s)
s=(W/notes[8138]).read_text();s=s.replace('- Cited, definition-level:','- Mathematical theorem imports (not definitions):')
s=s.replace('- No literature value, constant, or theorem enters as authority; the classical\n  names appear only in this section and under Prior art.','- Hypotheses for these imports: the finite menu gives a compact metrizable\n  countable product; the finite-dimensional distributions are consistent;\n  cylinder updates are continuous (the limiting plane kernel uses the proved\n  uniform coupling tail); Cesàro averages are probability measures on that\n  compact space. These are mathematical inputs, not physical axioms.')
s=s.replace('no value, constant or theorem is imported as authority.','the probability theorems listed under Imports are mathematical inputs, not physical premises.')
(W/notes[8138]).write_text(s)
# Tie runtime prose fences to the honest revised import statements; bound future captures.
for pr,path in notes.items():
 note=(W/path).read_text(); runner=re.search(r'^runner: (.*)$',note,re.M).group(1);p=W/runner;s=p.read_text()
 s=s.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 300')
 if pr==8138:s=s.replace('no value, constant or theorem is imported as authority.','the probability theorems listed under Imports are mathematical inputs, not physical premises.')
 if pr==8139:s=s.replace('no value, constant or theorem is imported as authority.','no ergodic decomposition is claimed.')
 if pr==8146:s=s.replace('no value, constant or theorem is imported as authority.','the probability and spectral results listed under Imports are mathematical inputs, not physical premises.')
 p.write_text(s)
# Repo-portable recovery instructions.
(W/'docs/work_history/review_loop/pr8146/README.md').write_text('''# PR8146 unit original source recovery

This archive preserves all 116 original path occurrences across PR8138, PR8139,
PR8141, PR8142 and PR8146. `original-manifest.json` records the original head,
path and SHA256 plus the gzip archive path and archive SHA256. Decompress with
Python `gzip.decompress` or `gzip -dc`; the decompressed bytes must match the
original SHA256. Compression uses a zero timestamp. Repeated inherited versions
remain separate per PR so the complete branch history is recoverable.

The live notes retain the constructive proofs, exact algebra and finite
witnesses with repaired hypotheses. Original broad negative certificates,
unproved parameter-wide distinctness and phase claims remain historical,
unlanded material: the live narrowing is not a passing negative certificate.
Keep the original branches as recovery handles. No audit verdict is supplied.

Original cache bytes are provenance only. They are not freshness evidence for
repaired notes/runners. New captures require independent cold source confirmation
and the cheap source/input-bound unit preflight first.
''')
print('followup draft saved')
