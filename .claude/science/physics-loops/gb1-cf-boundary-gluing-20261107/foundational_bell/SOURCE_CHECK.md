# Source-exposed comparison of the foundational Bell application

**Date:** 2026-11-09. **Phase:** source-exposed comparison after the independent
original-source proof check was frozen. This is not a second blind derivation,
an audit verdict, a retained-status decision, or empirical validation.
**Work state:** FROZEN comparison for the exact input hashes below. Three
wording/premise findings are recorded; corrected sources require a separate
changed-content comparison.

## Exact inputs

All four application files were read completely. They were taken from
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/foundational_bell/`.

| Input | SHA-256 | Lines |
|---|---|---:|
| `RESULT.md` | `74097336b7a8227cf2d49c940fc96a2c3c14f87ae33eb7ed095b2d90970cd5ac` | 260 |
| `ASSUMPTIONS.md` | `ec6f65db0239eb6811c688e9edae1ea32bb18353539558b820858427b6f15577` | 106 |
| `check.py` | `139618a1d9bbfde610351d528deeceae0b701fc7ebc11fccadcf946d96f63ae1` | 315 |
| `outputs/exact.stdout` | `890ae5e4a5a85e3ff428e69ac1281194dbd604ee163486f1b5fcb57cc38c8e77` | 104 |

The separate original-source artifact `INDEPENDENT.md` remains byte-identical:
SHA-256 `dab9366f3a01adbdbe92c907a79f60f64b4e64d03cc9aef3fb1e52450a518d86`,
576 lines. Its scientific source identity table and proofs are reused rather
than reread from a moving checkout. No supervisor `PRIMARY.md` was read in
either phase. The supervisor supplied the final application directly and,
during this comparison, specifically requested scrutiny of setting/private-
noise independence and the wording “independent resets”. Those are therefore
source-exposed findings, not claimed as independent discoveries of this phase.

## Findings requiring precise wording

### 1. Distinguish an assumed factorization from its stronger DAG derivation

**Location:** RESULT section 3 and ASSUMPTIONS C3-C4.

The displayed local-response factorization with setting-independent `rho`
is sufficient, and the subsequent `S<=2` proof is correct. C4 explicitly names
local responses, so the conditional theorem can be read correctly as assuming
that factorization. However, the text also says the factorization follows
from the fixed DAG and common exogenous ancestors. “Common-source variables”
in C3 does not by itself control the setting dependence of nominally private
exogenous noise. RESULT's “pre-choice/common source” wording is not a precise
replacement for that missing quantifier. Do not treat an unspecified causal
privacy or independence condition as already proved.

A concrete counterexample to the **weaker common-outcome-source reading**
makes the issue explicit. Take independent roots

```text
lambda = a fair bit,
U = a bit with P(U=1)=1/4,
V = uniform on {(0,0),(0,1),(1,0)}.
```

Set `(x,y)=(1,1)` when `U=1`, and `(x,y)=V` otherwise. Let outcome bits be
`a=lambda`, `b=lambda xor U`. Every setting pair has probability `1/4`, so
the observed settings are themselves independent fair bits. The common
exogenous ancestor of the two outcomes is `lambda`, which is independent
of the settings. Neither setting has a directed path to the opposite
outcome: the settings have no outgoing edges to either outcome. Nevertheless
`U=xy` conditional on the settings, so `a xor b=xy`, both outcome marginals
are fair, and `S=4`. The variable `U`, private to B's outcome mechanism, is
correlated with the settings because it also helps generate them. This does
**not** refute C4 when C4 is the full local-response hypothesis, nor a reading
that explicitly includes U in the independent pre-choice information. It
refutes inferring C4 merely from independence of common *outcome* ancestors
and the absence of setting-to-opposite-outcome paths.

**Repair:** either make the displayed factorization an explicit additional
hypothesis and remove the claim that the weaker graph conditions imply it,
or use the clean sufficient condition from INDEPENDENT section 3.1: take
`x,y` themselves as exogenous setting inputs, jointly independent of **all
non-setting exogenous inputs**, including the initial preparation, and rule
out the remote-setting paths in the complete graph. Collect all non-setting
inputs into `lambda`; recursive substitution then gives
`a=a_x(lambda)`, `b=b_y(lambda)`. If the physical setting generators contain
additional variables, include them or prove their reduction to this form.
This is a premise-clarity repair; it does not change the CHSH algebra.

### 2. “Independent resets” should mean fresh prepared apparatus

**Location:** ASSUMPTIONS W6.

The row correctly says permanent sites cannot be reused by erasing them,
but its “Optional independent resets” label suggests exactly that mechanism.
Replace it with “independent fresh preparations” or “fresh prepared apparatus
copies”, while retaining that the current proof supplies only one trial per
preparation. A repeated physical apparatus or a composition of multiple
prepared patches needs its own legal domain and formation protocol; the
single-frame theorem does not silently prove that composition.

### 3. One endpoint exception in the program-content comparison

**Location:** RESULT section 2, final paragraph of the fixed-preparation variant.

“The two have equal data cylinders, not equal program-record contents” is
correct generically, but at `v=r=1` the preparations and kernels coincide.
Say “equal data cylinders, although their program-record contents generally
differ” or add “except at v=1”. This is an edge-case wording fix, with no
effect on the witnessed law freedom.

## Confirmed application after those qualifications

### Four-record witness and fixed readout

The chosen menu is one constant `P=diag(1,0)`, `Q=I-P` throughout every
history, setting pair and r value. Consequently `P->+1`, `Q->-1` is one
fixed function of content. It does not infer a bit by consulting the current
setting or the bank selected on that history. The source's generic variable-
projector label ambiguity is therefore absent. The physical calibration and
role/trial assignment remain explicit O1-O2 conditions; the text does not
pretend that A selects them. Native identity readout followed by this fixed
analysis is also within the stated content-only condition. The scalar 0/I
extension is accurately presented as an optional separately proved variant,
not silently mixed into the executed 103-record count.

The six-neighbor kernel, exact source/buddy geometry, unchanging data menu,
unique frame, prepared translated/rotated domain, and state-reconstructed
next site agree with the independent proof. The append process itself is a
supplied discrete transition law; a physical clock is neither required for
that probability construction nor claimed. Its global routing is exposed.
The source does not claim preparation from the empty lattice. Resources
`46+57<=103` and permanence/support are correct on the legal domain.

Direct multiplication gives
`P(x,y,a,b)=[1+r(-1)^(a+b+xy)]/16`; hence the conditional table has denominator
4, the setting mass is 1/4, both outcome marginals are fair, and `S=4|r|`.
At `r=3/4` the conditional atom weights are indeed `1/16` or `7/16`, all
strictly positive. The conclusion is an existence statement across supplied
prepared protocols with no Bell causal-separation premise, not a physical
superquantum prediction. No-signalling is correctly restricted to the named
outcome marginals, not all program/controller records.

### Equal-preparation law variant

The variant holds every initial matrix record and the readout fixed at the
`r=1` preparation and changes the law, once per model, to `F_v`.
For all `v in [-1,1]`, the affine map
`q_v(p)=(1-v)/2+vp` maps `[0,1]` into `[0,1]`; its endpoint values are
`(1-v)/2,(1+v)/2`. The first three fair probabilities are unchanged, while
each stored fourth-stage 0 or 1 becomes exactly the intended fourth-stage
probability for r=v. The decoder and selected path geometry remain unchanged.

The old-record proof still holds: metadata/copies use the untouched empirical
branch, and each data record retains the same local program/trigger condition
after its birth. Only supported branches occur. Every model has one fixed
covariant rule; `v=0` still varies with neighborhood conditions through its
unchanged fallback branches. Interior v values have the identical full set
of positive legal prefixes. Thus this variant avoids attributing different
answers to one law at one state; it exhibits different admissibility laws
under the same initial-record condition. The analytical-versus-executed
boundary is stated accurately.

### Classical, quantum and autonomous-model comparisons

Given the explicit Bell factorization, the conditional-mean inequality and
the bound 2 are correct. The repaired assumptions should explain its derivation
without relying on strict common-record ancestry. The copied-A-to-B example
correctly demonstrates why the common exogenous input must be retained.
The discussion of multi-step relays and scheduler control correctly tests
causal paths, not merely one-hop geometry or unchanged outcome marginals.

For all cross-wing commuting Hermitian dichotomic observables, C is Hermitian
and `C^2=4I-[A0,A1][B0,B1]`. Each commutator norm is at most 2, so
`||C||^2<=8`. A common normalized positive state and the specified expectation
bridge give `S<=2sqrt(2)`. The Phi+ example with Z,X and `(Z+/-X)/sqrt(2)`
has correlations `(1,1,1,-1)/sqrt(2)` and saturates the bound. Commuting
wing algebras suffice; tensor composition is correctly identified as a
sufficient realization. Q4 explicitly supplies the same rho across choices.
None of those quantum premises is attributed to one-site M2 alone.

The autonomous-runtime application stays within J's actual scope: its
apparatus-dependent radius and joint gate/distant-tick jump do not prove
physical detector separation or a uniform propagation speed. Record-state
sufficiency is not identified with Bell factorization. The next-obligation
paragraph is a research target with explicit open premises, not a claimed
solution, framework-wide no-go, forced axiom amendment, or novelty claim.

## Static code/prose comparison

The code was read, not executed or imported. Its mathematics uses Fraction
arithmetic on diagonal rational matrices. `menu` counts all six recorded
neighbor occurrences, including duplicate program-valued neighbors, and
excludes the candidate itself. `replay` obtains branch probabilities from
that menu, rather than substituting the final expected cylinder formula;
the latter is an assertion checked after enumeration. It checks all occupied
sites initially and at terminal states, and every locally affected site
after each append, which suffices because F is nearest-neighbor. Permanence
and blank targets are checked separately.

The actual replay family is `r=0,1/2,3/4,1,-1`, for the unchanged F with
different preparations. Spatial covariance is checked on three snapshots
for 24 proper rotations and a translation, not exhaustively at all prefixes;
the general covariance statement is analytical. `standard_bounds` checks
16 classical vertices and the displayed 4x4 quantum example/identity; it
does not numerically establish the general operator norm theorem. The prose
does not claim otherwise. It also expressly says F_v and the scalar-copy
extension are analytical checks, not executed variants.

The saved stdout identifies precisely the supplied check.py SHA-256 and its
reported examples agree with the independently checked algebra. Its counts,
elapsed time and RSS are historical reported execution evidence, not a run
reproduced by this checker. Fault modes exist in the source, but no fault
execution receipt was in scope here, so none is independently attested.

## Limits and recovery checkpoint

The complete stated mathematical application and these four exact files were
examined. Linked search records, primitive registries, source manifests,
negative-claim sidecars and handoff files were outside the authorized read
set; their existence/content claims are not separately confirmed here. The
four-axiom witness and conditional Bell/quantum proofs do not use the three
additional primitives mentioned in the ledger. This check does not promote
the result to a model of every registered framework primitive.

Only SOURCE_CHECK.md was written in this phase. INDEPENDENT.md is preserved.
No numerical job, network access, source edit, commit, push, audit operation
or empirical comparison was performed. Final identity refresh confirmed all
four reviewed application hashes and the original independent artifact were
unchanged. The complete comparison was reread after writing; any source
repair needs its own exact new hashes and changed-content comparison.
