## Repo search

The lead's search covered main and PRs #10114, #10133, #10134 and #10141.
The [record](prior/repo-search-2026-11-08.md), section 1, found conditional operator results, not an all-address supplier.
There was no `prior/stage-cubes.md` at this checkout's pin.
The decisive local hit is **[arr, §7](arr.md#7-hand-completion-of-the-exceptional-cube-move), lines 145–184**.
It already proves the exact exceptional move requested here.

| Hit checked | Closeness and use |
|---|---|
| [arr](arr.md), 145–184, with its checkpoint and 635–655 | Exact statement, same exceptional indices and same CA-I hypotheses. Existing hand proof; do not repeat it. |
| [iem-supply](iem-supply.md), read whole | Exact consumer. Its ordinary original-nest fits and numerical tests are reused. |
| [adm-pl](adm-pl.md), 636–657 | Exact exceptional case. It retains `O-stage-cubes` and distinguishes raw members from cube clauses. |
| [p10-stability](port/p10-stability.md), 766 | Exact source locator and incomplete status, not a proof. |
| [layer-thm-part](layer-thm-part.md), 1385–1408 | Same exceptional supplier and the separate whole-read admission problem. |
| #10141, `research/ym4d/library/layer-thm-part.md`, 1385–1408 | Freshly read at `fb99b4dddc7254e6124ac124887d58eeb3a77802`. Same snapshot and same open case. |
| #10141, `research/ym4d/library/out-pi.md`, 273–329 | Conditional inverse consumer. It does not prove cube-family transport. |

The registry assigns `O-stage-cubes` to this lane.
The broader admission tasks retain their owners.
The other PR searches above are the lead's recorded searches, not fresh searches claimed here.
The workflow was read from fetched main at `bf92a1d763030836ed55631d5d7a7ef3b288f284`.
It supplies procedure only.

**Stop: the requested proof is already covered.**
The supplied search digest did not expose this local result.
A targeted search for `prf-stage-move-cubes` and `O-stage-cubes` found it.
I read its complete §7 and matched its conclusion to I 134506–134524.
This lane stops under the user's duplicate-work instruction.
It adds a coverage record, not another proof or a registry closure.

## Contract and sources

Codex. FINISH row 603. Checkout `93cbff3385dab83ef91ae6e6da98be77db1d734b`.
Research text, not an audit; this grants no scientific status.
Only this file is a repository output.
No numerical run or machine enumeration discharges a step.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**.
Credit **Tadeusz Bałaban** for the large-field preparation and cube methods.

- **I:** [complete account I, `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
- **Y:** [YM4_1400, `2bc0658f91d2`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).
- **SA:** [outline, `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).

Numbers following these keys are source lines.
The requested `/tmp` copies were present and reused without another download.
The permitted Balaban paper folder was absent. His construction is read through the account's transcriptions.
The outline index, neighbouring rows and obligations preceded the relevant outline excerpts.
The CA 4.12–4.19 index located the operation class and its historical hypotheses.

The target is I's `4.27:prf-stage-move-cubes`, 134184–134544.
The exceptional case has

```math
C=2,\qquad j+1=k,\qquad m=k_0+1,\qquad N_0\ge2.
```

Its question is geometric. A later gauge may be restricted only after its containing family cube has been supplied.
The numerical R tests in `iem-supply` are not re-attacked here.

## Port first: what Y actually proves

Searches for stage move, arrest, completion, cube families and one class per step found no matching stage-cube lemma in Y.
The relevant positive result is Y 63684–63770, especially `eq:elab-history-quiet-boxes`.
SA 17575–17583 already states its class conditions and box formula.
Y adds the component-restriction and history-tracing argument.

For a selected component $`X`$, put $`G_i=Z_i\cap X`$ and let $`H_i`$ be its predecessor's grid hull.
Y requires a single predecessor component at every level, no joining, no creation and quarantine throughout the waiting window.
It then proves

```math
\Omega_i^c\cap X=H_i^{[8a_i]},\qquad
G_i=H_i^{[10a_i]},\qquad h<i\le k.
```

Here $`a_i`$ is Y's cell side and brackets enlarge each face by the indicated distance.
The component restriction preserves each hull, enlargement and boxing operation.
Quarantine lets the surviving earlier component be traced through the intermediate labels.
The oldest component is a box. Rounding its coordinate intervals gives a box hull.
Enlargement preserves that property, and boxing fixes a box.
Induction proves the formula and the single-box conclusion.
This is Sussman and Alpoge's argument, not a new derivation here.

At $`i=k_0+1>h`$, that conclusion implies the condition marked $`(*)`$ immediately.
Any neighbourhood meets at most one component of a single box.
This supplies the exceptional step **on Y's stated class**.

The full Y class cannot simply replace the CA-I class.
I 45985–46001 requires size, no recent creation and exclusion of specified earlier operations.
That definition alone does not exclude a joining or require a single predecessor at every level.
Y 63684 explicitly adds the no-joining condition to Bałaban's class.
I 131563–131565 instead refers to a geometric declaration and nesting condition without stating their content there.
The needed account-specific match is already made in `arr`, §7.
There is no reason to create a second proof through Y's stronger class.

## Exact prior coverage

`arr`, §7 uses the regions of the retained label in force.
It does not combine regions from different historical labels.
Its hypothesis match cites these account passages:

| Input | Source and scope |
|---|---|
| No creation | I 53737–53831 and 49768–49809; the creation set includes failures attached to an existing component. |
| No joining | I 115864–115868; I 118394–118406 explicitly reads the condition over the preceding density steps. |
| Connected generators | I 50145–50313 and 50790–50859; incoming hulls and enlarged creation cubes remain connected. |
| Containment in the successor | I 50316–50457 and 50859–51125; the geometric recursion does not split an incoming component. |
| Rectangular components | I 134487–134495; this geometric input remains part of the source setting. |

The source ranges in this table are the prior proof's citations.
This lane directly read the no-joining passages, the one-step component statement, the creation recursion and the stage-move argument.
It did not repeat an independent check of every cited source lemma.

The existing argument excludes two predecessor components by their first joining inside $`X`$.
It excludes every creation-generated piece by the no-creation condition.
The remaining excluded region at $`s=k_0+1`$ is one box or empty.
This supplies the exact condition $`(*)`$, including the exceptional $`C=2`$ case.
The existing proof then obtains

```math
Q\subset Q'\subset\Omega_s,\qquad
s(Q)=2\xi_{k-1},\qquad s(Q')=2\xi_k,
\qquad w_{Q'}=\mathsf L_0^2w_Q.
```

The old witness cell in $`\Omega_{s+1}^c`$ remains in $`Q'`$.
Thus $`Q'`$ stays in the same old-shell family $`(\mathrm{ii})_s`$.
This is the requested conclusion, not the more expensive new-shell alternative.
`arr`, line 184, also accounts for every remaining family in I's lemma.

I 143963–143970 separately uses the same single-box conclusion under its nesting hypothesis.
It is consistent with this coverage; it is not another proof attempted here.
The corridor example in I 139822 onward omits that declaration.
It is not a counterexample to the retained-label hypotheses used by `arr`.

`arr`, 655, records that its note had not received independent mathematical review.
This coverage check adds no such review and grants no scientific status.

## Consequences already available for IEM-LOCAL-SUPPLY

The following is a reconciliation of existing results after the duplicate-work stop.
It is not a new attack on the four G entries.

The prior cube move removes the cited stage-transport obstruction for **already assigned family cubes**.
I 134549–134586 supplies the other dated family containments and the conditional gauge restriction.
For the same pair, a gauge supplied on a later containing cube restricts to the earlier family cube.
This covers the geometric moves at stages, arrest, T-steps and completion.
It does not construct a gauge on a larger cube from an earlier smaller-cube gauge.
These results do not assign every native whole read to such a family.
They also do not supply a gauge of a newly presented real reference at a moved raw address.

- **G-zero:** its later-image part remains open on the full quantifiers.
  The missing raw whole-read gauge is outside the conclusion about supplied positive-level families.
  I 136538–136555 retains the completion-site limitation explicitly.
- **G-next-0:** its matched ordinary fit remains proved in `iem-supply`.
  A later read already assigned to a supplied family has the existing transport result.
  Assignment at every actual level-one address and supply of the same reference remain open.
- **G-next:** the same distinction applies at positive next-layer indices.
  The old-family stage transport is covered; the complete-address certificate assignment remains open.
- **G-address:** the separately cited stage-move gap is already covered by `arr`, §7.
  The native-to-family assignment, complete stencils and moved raw-reference supply remain open.

These conclusions retain the numerical R tests exactly as recorded in `iem-supply`.
They do not assert an actual-source counterexample.

The completion-collar supplier is also already owned elsewhere.
Registry row **CA**, owned by **`ca-claude`**, cites `arr`'s Result at line 959.
It requires admission on the fixed birth domains, including whole cubes and all completion parameters.
This lane does not reopen that target.

## Status table and first open input

| Target | Disposition | Extent |
|---|---|---|
| O-stage-cubes, step $`(*)`$ | ALREADY COVERED | `arr`, §7, on CA-I's retained-label no-creation/no-joining hypotheses. No new proof or status grant. |
| G-zero, later images | OPEN | Actual raw whole-read gauge, especially after completion, remains unsupplied. |
| G-next-0, later images | OPEN | Assigned-family transport is covered; all-address level-one assignment remains. |
| G-next, later images | OPEN | Assigned-family transport is covered; all-address next-layer assignment remains. |
| G-address, later images | OPEN | Stage-cube obstruction covered; native family assignment and raw-reference supply remain. |
| IEM-LOCAL-SUPPLY | OPEN | No all-source admission theorem follows from cube transport. |
| Completion-collar admission | OWNED ELSEWHERE | Registry CA; owner `ca-claude`. |

**First open input remains G-zero at $`q=0`$, $`N=12`$, as stated in `iem-supply`.**
For every original item-10 source and required raw cube, supply a gauge of its actual real reference on the whole read.
This includes endpoints and retained differences after substitution, with

```math
U^u=e^{i\eta A},\qquad
\eta|A|\le a_\flat^Y,\qquad
\eta^2|\nabla A|\le a_\flat^Y.
```

Its completion-collar instance belongs to CA. No further proof work is opened here.
