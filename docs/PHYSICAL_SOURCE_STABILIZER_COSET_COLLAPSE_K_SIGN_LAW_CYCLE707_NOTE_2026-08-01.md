# The all-24 frame sign law of the source-driven K field, derived by source-stabilizer coset collapse — Cycle 707

Date: 2026-08-01

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed, joined Cycle-696 compiler contract inventoried below; that compiler is a
landed but audit-excluded support surface, not an independent audit authority.

The frame sign behaviour of the un-averaged, source-driven endpoint field `K` is
derived here as a composition of two exactly executed statements. First, the
stated **pointwise** transport law holds on the constant-sign signed permutations:
for a frame whose nonzero entries all share one sign, the coframe conjugates, the
per-axis parts permute with that common sign, and `K` carries the common sign at
every site, with measured floors `9.3e-15` on the all-plus branch and `1.5e-11`
on the all-minus branch at `L = 3`. Second, **every** proper
rotation's image of the single-edit source domain collapses exactly onto a
constant-sign representative's image, because the source's own proper stabilizer
is the four-element rotation quartet about the edited axis and each coset of that
quartet contains exactly one constant-sign element. The all-24 multiset sign law
`multiset(K^{g.dom}) = multiset(sx(g) K^{dom})` is therefore a corollary of the
pointwise law rather than an independent measurement, with the `12 / 12` split of
`chi(g) = sx(g)` derived from the coset structure. The stated coframe-conjugation
relation fails on every mixed-sign proper rotation in this fixed source/compiler
test: the minimum over the 18 mixed proper rotations is `2.4e-01` at `L = 3` and
`6.3e-01` at `L = 7`. This does not exclude averaged, relabelled, source-dependent,
or otherwise reformulated laws. Finally, a stage ladder locates the reflection floor:
the source multiset is bit-exact, the assembled load multiset agrees at `2.1e-14`,
and the response multiset already carries `6.9e-11`, so the negation floor enters
at the linear-response solve, and the endpoint defect nearly doubles at each step
of the sampled `AMP` ladder `0.05 / 0.10 / 0.20`, with successive displayed ratios
`2.0e+00` and `2.0e+00`.

## Improper-frame framing

The runner also executes the six constant-sign signed permutations with
determinant `-1`. These are bookkeeping, not physics:
improper (det = -1) signed permutations are NOT axiom symmetries
— the Lattice axiom names proper cubic rotations only. They enter this note ONLY
as derived computational identities of the compiled chain (exact relabelings
composed with the reflection asymmetry measured here), and
every physical frame-scope statement in this note is over the 24 proper rotations.
Nothing in this cycle enlarges the framework's symmetry group, and no statement
below counts elements outside the 24.

## Setup

The compiled chain is the landed
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
used verbatim and never re-implemented:

```
rho = c696.rho_vector(dom, model["site_index"])
b   = rho @ model["G"]
eps = c696.response(model, sol, b)["eps"]
mc  = c696.metric_and_coframe(L, AMP * eps, model["index"])
kf  = c696.k_field(mc["e_clipped"])
```

with `model = c696.assemble_static_hessian(L, wrap=False)` and
`sol = c696.sector_solve(model)`. `k_field` returns the per-axis parts stacked on
a trailing axis together with their sum `K`; the parts are the objects that carry
the transformation law, and the pointwise claim is a statement about them.

Two decorated source domains are used at each box size `L` in `(3, 7)`, with
`A = (L-1)//2` and the response amplitude `AMP = 2.0e-01`:

- `dom0` (called x5): `edits = {((A,A,A),(A+1,A,A)): 5}`, a single relabelled link
  on the `+x` ray;
- `dom1` (called x5y7): the same edit together with
  `((A,A,A),(A,A+1,A)): 7` on the `+y` ray.

Frames are `c696.c576.FRAMES`, the 24 proper cubic rotations. The site action is
`c696.frame_site_map(L, R)`, the exact affine map `s -> R(s - c) + c`; the
decorated action on a domain is `c696.apply_frame_to_domain(dom, R)`, which maps
sites, links, anchor, ports, and ray directions together.

Signed-permutation conventions. For a frame `R`, `p[i] = argmax|R[i]|` is the
permutation word and `s[i] = R[i, p[i]]` the sign word; `sx` is the sign attached
to the `x` axis, `sx = s[p.index(0)]`, and `sy = s[p.index(1)]` likewise. A frame
is **constant-sign** when every nonzero entry shares one sign, which is exactly
the condition under which the landed `frame_K_parity` returns `+1` or `-1` rather
than `None`. Of the 24 proper rotations, 6 are constant-sign — 3 all-plus and
3 all-minus — and 18 are mixed.

### Imported compiler contract

The following are supplied inputs, not outputs of this cycle:

- the finite field `F_17`, centered lift, ray-source convention, and the landed
  source scale `SRC_SCALE = 0.17`;
- edit labels `5` and `7`, the open spatial box, `L_T = 2` periodic tick fold, and
  the static-sector Regge Hessian/response construction;
- central finite-difference step `1.0e-4`, barycentric source-row convention,
  absolute null cut `1.0e-8`, and regular-sector pseudoinverse;
- metric least-squares reconstruction, principal symmetric square root,
  positive-definite margin `1.0e-6`, and open-boundary derivative defining `K`;
- the selected samples `L = 3, 7`, `AMP = 0.20` (plus the stated amplitude
  ladder), and every numerical gate tolerance in the runner.

There is no measured, fitted, or literature constant imported by this cycle. The
normalization, boundary, convention, and support inputs above are load-bearing:
the numerical floors are claims about this fixed compiler only. The exact signed-
permutation and decorated-domain enumeration is independent of the floating-point
coframe construction.

## Claims

### Constant-sign pointwise transport law and its two floors

For every constant-sign signed permutation `R` with common sign `eps_R`, and at
every site `x`, with `sigma = frame_site_map(L, R)`:

```
e^{R.dom}(sigma x)       = R e^{dom}(x) R^T
parts_i^{R.dom}(sigma x) = eps_R * parts_{p[i]}^{dom}(x)
K^{R.dom}(sigma x)       = eps_R * K^{dom}(x)
```

The coframe relation is sign-blind, since `s_i s_j = +1` entrywise on a
constant-sign frame, while the parts relation carries the sign once and `K`
inherits it. Measured as the maximum over sites of the largest of the coframe,
parts, and `K` defects, and then over the frames of each branch (6 proper plus
6 improper constant-sign elements):

| branch | `L = 3` | `L = 7` |
|---|---|---|
| all-plus | `9.3e-15` | `3.1e-13` |
| all-minus | `1.5e-11` | `3.1e-10` |
| identity frame | `0.0e+00` | `0.0e+00` |

The identity frame's total defect is exactly zero, bit-for-bit, at both box
sizes. The minus-branch magnitudes agree at the displayed numerical floor across
the six minus elements, proper and improper alike; raw floating-point values are
not asserted to be identical. The six are related by the numerically equivariant
plus subgroup and probe one reflection asymmetry rather than six independent
ones. The branch asymmetry is gated directly — the minus floor
exceeds ten times the plus floor by measured factors `1.6e+03` at `L = 3` and
`9.9e+02` at `L = 7`.

### Mixed-sign failure of the stated coframe relation

Every mixed-sign proper rotation breaks the stated coframe-conjugation relation
in this source/compiler test. The minimum over the 18 mixed proper rotations of
the max-site coframe defect measures `2.4e-01` at `L = 3` and `6.3e-01` at
`L = 7`. Thus the `None` region of the landed `frame_K_parity` is outside this
particular pointwise sign law. The finite test does not prove the absence of every
alternative relation; in particular, the source-stabilizer argument below
recovers an all-24 multiset statement after exact domain collapse.

### Source stabilizer quartet, transversal, and `sx` invariance

This section is exact integer and decorated-domain computation, independent of `L`
and of every floating-point stage.

- The proper stabilizer of `dom0` by Cycle696's canonical `domain_key` equality
  (anchor, order-independent ports, and links) is the frame set
  `(20, 21, 22, 23)` — four elements.
- Those four are exactly the four powers of the `x`-axis rotation
  `[[1,0,0],[0,0,-1],[0,1,0]]`, verified as a set of integer matrices.
- Every proper rotation `g` has **exactly one** quartet element `t` with `g t`
  constant-sign: `24/24`.
- `sx(g t) = sx(g)` for every proper `g` and every quartet element `t`: `96/96`.
  The quartet fixes the `x` axis with sign `+1`, so composing with it cannot move
  the `x` sign.

### Exact coset collapse and the all-24 multiset corollary

Because each quartet element fixes `dom0` exactly, the decorated image of `g` and
of its constant-sign coset representative `g t` are the *same* domain:

- canonical decorated-domain equality `g.dom0 == (g t).dom0` holds `24/24` at `L = 3` and
  `24/24` at `L = 7`;
- the number of distinct domain images over the 24 frames is exactly `6`, which
  is `24` divided by the four-element quartet;
- on one representative per distinct image, the compiled `K` arrays of
  `chain(g.dom0)` and `chain((g t).dom0)` are bit-identical, `6/6` at `L = 3`.
  That row is chain determinism, stated as such: equal link states produce equal
  arrays, which is what licenses transporting the pointwise law from the
  representative to `g`.

Consequently the all-24 multiset law
`multiset(K^{g.dom0}) = multiset(sx(g) K^{dom0})` follows from the constant-sign
pointwise law rather than
standing on its own measurement. Measured multiset defects, maximum over the
frames of each sign class:

| `chi(g) = sx(g)` | count | `L = 3` | `L = 7` |
|---|---|---|---|
| `+1` | 12 | `7.4e-15` | `2.0e-13` |
| `-1` | 12 | `1.0e-11` | `3.1e-10` |

The `12 / 12` split is derived: `sx` is constant on quartet cosets by the exact
stabilizer enumeration, and
each coset carries exactly one constant-sign representative whose common sign is
its `sx`. Two rejectors keep the rows discriminating. Testing the pointwise law
on an all-minus frame with the sign forced to `+1` gives a `K` defect of
`6.7e-01` at `L = 3` and `9.9e-01` at `L = 7`. Comparing an all-minus frame's
multiset against the unsigned base gives `2.1e-01` at `L = 3`; the same quantity
prints `4.1e-02` at `L = 7` and is reported unscored there.

### Two-edit upstream trichotomy and coframe-domain boundary

For `dom1` the mirror `m_z = diag(1, 1, -1)` fixes the domain exactly, by canonical
decorated-domain fingerprint, at both box sizes. Writing `u = g` when `g` is constant-sign and
`u = g m_z` otherwise, `u` is constant-sign exactly when `(sx, sy)` lies in
`{(+,+), (-,-)}`, and the sign classes count `6 / 6 / 12`. On those 12 frames the
collapse is again exact: `12/12` frames have a constant-sign coset member, and
`12/12` satisfy `g.dom1 == u.dom1` as decorated domains, at both box sizes. The
resulting **source-sign classification** is therefore derived rather than
tabulated.

The downstream coframe is not in the compiler's declared principal-square-root
domain for this source at `AMP = 0.20`. The base and every transformed source use
the compiler's eigenvalue-clipped surrogate: 5–6 sites are clipped at `L = 3`
and 24–28 at `L = 7`. Accordingly the following values are diagnostics only and
are excluded from theorem gates:

| class | count | clipped-surrogate diagnostic | `L = 3` | `L = 7` |
|---|---|---|---|---|
| `(+,+)` | 6 | `CONDITIONAL_ON_CLIP`, preserved compare | `2.7e-14` | `6.9e-13` |
| `(-,-)` | 6 | `CONDITIONAL_ON_CLIP`, negated compare | `9.7e-11` | `5.5e-10` |
| mixed `(sx, sy)` | 12 | `CONDITIONAL_ON_CLIP`, min of both signs | `1.9e-01` | `1.0e-01` |

The mixed-class diagnostic is the minimum over those 12 frames of the smaller of
the two compare-sign multiset defects. It is not evidence for a downstream
theorem while clipping is engaged. What is derived here is the exact upstream
`6 / 6 / 12` source classification and coset collapse, consistent with frozen-
main Cycle706's downstream quarantine.

### Measured floor location and amplitude scaling

The ladder is run for one all-minus proper rotation against one all-plus
three-cycle rotation, comparing sorted multisets stage by stage:

| stage | all-minus `L = 3` | all-plus `L = 3` | all-minus `L = 7` | all-plus `L = 7` |
|---|---|---|---|---|
| `rho` | `0.0e+00` | `0.0e+00` | `0.0e+00` | `0.0e+00` |
| `b` | `2.1e-14` | `3.1e-15` | `1.0e-14` | `1.8e-15` |
| `eps` | `6.9e-11` | `8.4e-15` | `1.5e-09` | `7.2e-13` |

The source multiset is bit-exact and the assembled load multiset matches at the
`1e-14` level, while the response multiset already carries the leading defect —
the measured ladder first resolves the negation floor at the linear-response
solve. The metric stage inherits it through the amplitude dial: the
per-site sorted edge-length defect measures `1.4e-11` at `L = 3` against the
predicted `AMP * d_eps = 1.4e-11`, a product identity gated at half the predicted
value. At `L = 7` the same length defect prints `2.7e-10` and is reported
unscored. The sampled endpoint consequence is near-doubling of the negation floor:
the all-minus multiset defect measures `2.5e-12`, `5.0e-12`, `1.0e-11` at `AMP`
`0.05`, `0.10`, `0.20`, with successive ratios `2.0e+00` and `2.0e+00`.

## Derivation sketch

The argument has three finite steps, each verified exactly by finite computation
in the runner using integer matrices and canonical decorated-domain equality.

1. *Every quartet element fixes the source.* The edited link lies on the `+x`
   ray. A rotation about the `x` axis fixes the anchor and the `+x` direction, so
   it fixes the edited link and permutes the remaining rays among themselves;
   those rays carry one common weight, so the link dictionary comes back
   unchanged. Hence `t.dom0 = dom0` for all four `t`, and therefore
   `g.dom0 = (g t).dom0` for every proper `g` and every `t` — the decorated action
   is an action, so applying `g` to equal states gives equal states.

2. *Exactly one coset member is constant-sign.* At fixed `sx`, the quartet's four
   elements realize the four sign patterns available on the `(y, z)` block while
   leaving the `x` sign alone. Composing `g` with the quartet therefore sweeps
   those four patterns and reaches the all-same-sign pattern exactly once. This is
   the `24/24` transversal row above, and it is what makes the coset
   representative unique rather than merely existent.

3. *The invariant is `sx`.* Each quartet element carries `sx = +1`, so `sx` is
   constant along each coset (the `96/96` row above). The unique constant-sign
   representative's common sign is its own `sx`, which is `sx(g)`. Composing step
   1 with the constant-sign pointwise law at the representative gives the
   multiset statement for `g` itself,
   with sign `chi(g) = sx(g)`.

Steps 1 and 3 are exact. The floating-point content in the final single-edit
statement is the floor inherited from the pointwise computation; the stage ladder
locates that measured floor rather than leaving it as an unexplained residue.

## Honest boundary

- The all-plus branch is exactly equivariant to within accumulation noise; the
  all-minus branch is not, and the size of its floor — `1.5e-11` at `L = 3`,
  `3.1e-10` at `L = 7` — together with its growth in `L` is
  measured, not derived. No constant is fitted anywhere in this cycle, and none
  is claimed.
- The magnitude of the mixed-sign breakage is likewise measured, not derived. The
  runner checks the exact biconditional between its constant-sign predicate and
  the imported `frame_K_parity`, then shows that the stated coframe relation holds
  on the six constant-sign proper frames and fails on the other 18. It does not
  exclude alternative laws.
- Improper elements are computational identities of the compiled chain only, per
  the framing section above.
- The collapse mechanism is specific to these two source domains and their
  stabilizers. A classification of stabilizers and collapse behaviour for general
  edit sets is not attempted here and is named as a next route below.
- For `x5y7`, only the exact source classification and decorated-domain collapse
  are theorem content. Every downstream coframe/`K` comparison is
  `CONDITIONAL_ON_CLIP` and excluded from PASS/FAIL.
- Nothing in this cycle touches the amplitude dial's status, the response
  normalization, or any coupling; `AMP` is a supplied nuisance scale and the
  amplitude-ladder row is a measured three-sample scaling statement, not a
  derivation of exact linearity.

## The next paths opened

- **Derive the response-stage reflection floor constant.** The stage ladder localizes the
  defect to the `b -> eps` solve; the next path opened is to characterize the
  constant itself from the open-box static operator and its sector
  regularization, turning a measured floor into a derived one.
- **Classify stabilizers and collapse for general edit sets.** The quartet and
  the mirror are the stabilizers of two particular sources. The next path opened
  is a general statement: for which edit sets does the stabilizer meet every
  coset of the constant-sign subgroup, and what replaces the multiset law when it
  does not.
- **Derive the `L`-scaling of the two branch floors.** The plus branch moves from
  `9.3e-15` to `3.1e-13` and the minus branch from `1.5e-11` to `3.1e-10` between
  `L = 3` and `L = 7`; the next path opened is a scaling law for both, which would
  also predict the mixed-sign breakage's mild decrease.

## Relation to the interacting cycle

The frame classification measured in frozen-main cycle 706
(`PHYSICAL_ENDPOINT_READOUT_QUBIT_STINESPRING_CHANNEL_CYCLE706_NOTE_2026-08-01.md`)
— the `12` plus / `12` minus single-axis split, the `6 / 6 / 12` two-axis
source trichotomy, and the `1.0e-11` negation floor — is here derived in its exact
counts and located in its measured floor stage. Cycle706 also records the same
`x5y7` clip boundary; this note preserves that quarantine. It remains unaudited
context and is therefore named in backticks rather than linked as authority.

## Runner

The [Cycle707 runner](../scripts/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01.py)
executes every gated and diagnostic row above and reports

```
TOTAL: PASS=71 FAIL=0 CONDITIONAL_ON_CLIP=6
```

with exit code `0`. Two consecutive runs produce byte-identical standard output
and a byte-identical receipt. The receipt is written to
`outputs/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01_receipt_2026-08-01.json`
and carries no timestamp, no wall clock, no host name, and no absolute path, so
it is comparable across machines.

Every floating-point number quoted in this note is the runner's own measurement
in the run that produced that `TOTAL` line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [joined-compiler tournament note](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)

Cycle 700 and the joined-compiler tournament note are landed. The linked Cycle696
compiler and Cycle707 runner are support/code dependencies. Backticked context
only, with no authority edge:
`PHYSICAL_ENDPOINT_READOUT_QUBIT_STINESPRING_CHANNEL_CYCLE706_NOTE_2026-08-01.md`.
