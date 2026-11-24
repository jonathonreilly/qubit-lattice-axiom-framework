# Alpoge–Claude RH explainer: remaining sections

## Repo search

**Refs searched:** `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` in `/Users/jonreilly/Projects/Physics`.

**Terms:** `Alpoge|Rubinstein|zeta-paper|RH explainer|gap RH`; then the more specific `gap-rh-tools-transfer|lemniscate|zeta-paper_v2|Alpoge-Claude RH|Rubinstein.*RH|RH.*Rubinstein`; and `chain of lifts|monotone quantity|fixed point|Landau lemma|kernel.*decide|uniformity in.*scale`.

The broad search returned many unrelated hits. The closest were `research/mass-gap/README.md:9`, whose exact target is “a positive Hamiltonian gap for a volume-first continuum limit of four-dimensional Wilson SU(2) Yang–Mills,” and which says “This snapshot neither verifies that account nor establishes continuum existence.” This is adjacent YM provenance, not RH method. `research/mass-gap/library/gap-os-equiv.md:28` says the separate argument's “proof of contraction (its eq. (18))” uses the spectral theorem, while the file's own section “builds H as a generator.” That contraction is not a step in the RH explainer. The specific RH-explainer, lemniscate, and transfer-note search returned no hits on the five refs. The final broad search returned only unrelated matches, with no RH-specific hit. `library/prior/repo-search-2026-11-08.md` was absent.

Within this checkout, the exact-target search in `library/open-registry.md` found no RH explainer, Rubinstein, lemniscate, or Alpoge RH owner; the SA index and obligations search likewise found no corresponding RH-method row. The requested `library/prior/gap-rh-explainer-rest-luna.md` did not exist before this work. The prior row 1481 report, `library/gap-rh-tools-transfer-fable.md` §2.5, is credited below for the sections it had already covered; this digest addresses its listed unread passages.

## Reading and scope

I read the requested passages of Michael Rubinstein's explainer in full:

- III.5 §§4–6: 3850–4190; III.6 §§3–7: 5033–5410; III.7: 5411–6482.
- III.8 §2: 6694–7021; §§4–6: 7137–7375.
- III.9 §2: 7528–7615; the remainder of §4 and §§5–6: 7761–8241.
- III.10 §§1–3: 8397–8887; §§5–9: 9068–9671.
- Assembly §§2, 4, 4a, 7, 9: 9887–9978, 10173–10440, 10441–10529, 10796–11056, 11115–11333.
- Lemniscate section: 11334–12884.
- Census table: 12979–13461.

I skimmed the paper's heading map and the existing row-1481 report to locate the requested boundaries and avoid repeating its completed reading. The rest of the paper was not read in full. The lemniscate section explicitly calls itself illustrative and says it is not used in the RH deduction (11334–11343).

## Findings

### (a) A contraction, monotone quantity, or fixed point through the lifts?

**None found.** The chain is assembled by summing per-lift divisibility and size contributions, with endpoint and per-lift error terms; its parameter `m` is chosen to balance those terms. The assembly's stated lift and slope bounds are inequalities conditional on inputs, not an iteration that contracts a quantity or converges to a fixed point (III.6 §§3–7, 5033–5410; III.7, 5411–6482; assembly §§4a and 7, 10441–10529 and 10796–11056). The largest-slope lemma M10 is a one-step deduction from three assumed statements and a lattice inclusion, not a monotonicity scheme (10441–10529).

### (b) Positivity beyond Landau's lemma, norms, and counts?

**None found.** The positive expressions used in the requested trace and theta arguments are squared norms, Gram/trace expressions, positive weights, and counts or representation numbers (III.8 §2, 6694–7021; §§4–6, 7137–7375; III.10 §§5–9, 9068–9671). The lemniscate computations and identities are not part of the RH deduction. I found no separate positivity principle serving as an additional proof step.

### (c) A relied-upon finite computation larger than a kernel decision?

**None found in the RH deduction.** The explainer reports exact finite calculations and numerical checks, including the bounded hypothesis-(B) checks in III.5 §§4–6 (3850–4190) and many lemniscate tests (11334–12884). They are presented as examples, checks, or observations, not as discharge of the RH proof's open inputs. The lemniscate section expressly says it is not used in the RH deduction (11334–11343); the assembly instead states H12 as an assumption and identifies the Lean development as its source (10796–11056; 11115–11333). I found no non-kernel finite calculation carrying a proof obligation. The paper does not give enough evidence here to certify which reported arithmetic tests, if any, were themselves kernel checked.

### (d) Scale-uniformity by a method other than existential constants with `x^(C eps)` slack?

**None found.** The one-scale theorem is extended across windows only under H12: constants are required to be independent of `x`, and arbitrarily large windows must be supplied. The explainer says those uniformity and window conditions are not supplied by the earlier O23 statement; it gives only an unbounded set of admissible scales (assembly §7, 10796–11056). Corollary M11 then obtains one exponent on each window using the uniform constants in H12 and slack `x^((C_abs + e_L + 8) eps)` (assembly §7, 10796–11056). The corresponding Lean statement has existential constants and windows, not another established scale-uniformity mechanism (assembly §9, 11221–11333).

## Credit and status

This is a reading digest, not an audit or a status claim. Credit for the RH proof belongs to Levent Alpoge, with Claude, and credit for this explainer belongs to Michael Rubinstein. The four answers above describe only the passages read and the proof structure Rubinstein reports; they do not independently verify the RH proof or the Lean development.
