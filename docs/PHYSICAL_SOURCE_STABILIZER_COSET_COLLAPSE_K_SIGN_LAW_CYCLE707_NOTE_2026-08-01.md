# The all-24 frame sign law of the source-driven K field, derived by source-stabilizer coset collapse — Cycle 707

Date: 2026-08-01

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied.

The frame sign behaviour of the un-averaged, source-driven endpoint field `K` is
derived here as a composition of two exactly executed statements. First, a
**pointwise** transport law holds on the constant-sign signed permutations and
only there: for a frame whose nonzero entries all share one sign, the coframe
conjugates, the per-axis parts permute with that common sign, and `K` carries the
common sign at every site, with measured floors `6.1e-15` on the all-plus branch
and `1.5e-11` on the all-minus branch at `L = 3`. Second, **every** proper
rotation's image of the single-edit source domain collapses exactly onto a
constant-sign representative's image, because the source's own proper stabilizer
is the four-element rotation quartet about the edited axis and each coset of that
quartet contains exactly one constant-sign element. The all-24 multiset sign law
`multiset(K^{g.dom}) = multiset(sx(g) K^{dom})` is therefore a corollary of the
pointwise law rather than an independent measurement, with the `12 / 12` split of
`chi(g) = sx(g)` derived from the coset structure. The mixed-sign obstruction is
real and is measured at the coframe stage, not assumed: the minimum over the 18
mixed proper rotations of the coframe-conjugation defect is `2.4e-01` at `L = 3`
and `6.3e-01` at `L = 7`. Finally, a stage ladder locates the reflection floor:
the source multiset is bit-exact, the assembled load multiset agrees at `2.1e-14`,
and the response multiset already carries `6.9e-11`, so the negation floor enters
at the linear-response solve, and the endpoint defect is linear in the amplitude
dial with successive ratios `2.0e+00` and `2.0e+00` over `AMP` `0.05 / 0.10 / 0.20`.

## Improper-frame framing

The runner also executes the six constant-sign signed permutations with
determinant `-1`. These are bookkeeping, not physics:
improper (det = -1) signed permutations are NOT axiom symmetries
— the LATTICE axiom names proper cubic rotations only. They enter this note ONLY
as derived computational identities of the compiled chain (exact relabelings
composed with the reflection asymmetry measured here), and
every physical frame-scope statement in this note is over the 24 proper rotations.
Nothing in this cycle enlarges the framework's symmetry group, and no statement
below counts elements outside the 24.

## Setup

The compiled chain is the landed Cycle-696 open-coframe endpoint compiler
`scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`, used
verbatim and never re-implemented:

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
the transformation law, and the whole of Claim C1 is a statement about them.

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

## Claims

### C1 — the constant-sign pointwise transport law, and its two floors

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
| all-plus | `6.1e-15` | `4.6e-13` |
| all-minus | `1.5e-11` | `3.1e-10` |
| identity frame | `0.0e+00` | `0.0e+00` |

The identity frame's total defect is exactly zero, bit-for-bit, at both box
sizes. The minus-branch magnitudes are identical across all six minus elements,
proper and improper alike: the six are related to one another by the exactly
equivariant plus subgroup, so they share one reflection asymmetry rather than six
independent ones. The branch asymmetry is gated directly — the minus floor
exceeds ten times the plus floor by measured factors `2.5e+03` at `L = 3` and
`6.7e+02` at `L = 7`.

### C2 — the mixed-sign obstruction is real, at the coframe stage

Every mixed-sign proper rotation breaks the coframe conjugation relation
outright. The minimum over the 18 mixed proper rotations of the max-site coframe
defect measures `2.4e-01` at `L = 3` and `6.3e-01` at `L = 7`. There is no
pointwise law to floor there: the `None` region of the landed `frame_K_parity` is
the true absence of a law, not a weaker version of one. This reproduces, at the
coframe stage and from the un-averaged source-driven field, the landed six-frame
restriction of the single-carrier transport rows.

### C3 — the source's stabilizer quartet, its transversal, and `sx` invariance

All of C3 is exact integer and link-dictionary computation, independent of `L`
and of every floating-point stage.

- The proper stabilizer of `dom0` by link-dictionary equality is the frame set
  `(20, 21, 22, 23)` — four elements.
- Those four are exactly the four powers of the `x`-axis rotation
  `[[1,0,0],[0,0,-1],[0,1,0]]`, verified as a set of integer matrices.
- Every proper rotation `g` has **exactly one** quartet element `t` with `g t`
  constant-sign: `24/24`.
- `sx(g t) = sx(g)` for every proper `g` and every quartet element `t`: `96/96`.
  The quartet fixes the `x` axis with sign `+1`, so composing with it cannot move
  the `x` sign.

### C4 — exact coset collapse, and the all-24 multiset law as a corollary

Because each quartet element fixes `dom0` exactly, the decorated image of `g` and
of its constant-sign coset representative `g t` are the *same* domain:

- link-dictionary equality `g.dom0 == (g t).dom0` holds `24/24` at `L = 3` and
  `24/24` at `L = 7`;
- the number of distinct domain images over the 24 frames is exactly `6`, which
  is `24` divided by the four-element quartet;
- on one representative per distinct image, the compiled `K` arrays of
  `chain(g.dom0)` and `chain((g t).dom0)` are bit-identical, `6/6` at `L = 3`.
  That row is chain determinism, stated as such: equal link states produce equal
  arrays, which is what licenses transporting the pointwise law from the
  representative to `g`.

Consequently the all-24 multiset law
`multiset(K^{g.dom0}) = multiset(sx(g) K^{dom0})` follows from C1 rather than
standing on its own measurement. Measured multiset defects, maximum over the
frames of each sign class:

| `chi(g) = sx(g)` | count | `L = 3` | `L = 7` |
|---|---|---|---|
| `+1` | 12 | `4.8e-15` | `3.8e-13` |
| `-1` | 12 | `1.0e-11` | `3.1e-10` |

The `12 / 12` split is derived: `sx` is constant on quartet cosets by C3, and
each coset carries exactly one constant-sign representative whose common sign is
its `sx`. Two rejectors keep the rows discriminating. Testing the pointwise law
on an all-minus frame with the sign forced to `+1` gives a `K` defect of
`6.7e-01` at `L = 3` and `9.9e-01` at `L = 7`. Comparing an all-minus frame's
multiset against the unsigned base gives `2.1e-01` at `L = 3`; the same quantity
prints `4.1e-02` at `L = 7` and is reported unscored there.

### C5 — the two-edit trichotomy, derived

For `dom1` the mirror `m_z = diag(1, 1, -1)` fixes the domain exactly, by link
dictionary, at both box sizes. Writing `u = g` when `g` is constant-sign and
`u = g m_z` otherwise, `u` is constant-sign exactly when `(sx, sy)` lies in
`{(+,+), (-,-)}`, and the sign classes count `6 / 6 / 12`. On those 12 frames the
collapse is again exact: `12/12` frames have a constant-sign coset member, and
`12/12` satisfy `g.dom1 == u.dom1` as link dictionaries, at both box sizes. The
resulting trichotomy is therefore derived rather than tabulated:

| class | count | behaviour | `L = 3` | `L = 7` |
|---|---|---|---|---|
| `(+,+)` | 6 | preserved | `9.5e-15` | `9.7e-13` |
| `(-,-)` | 6 | negated | `9.7e-11` | `5.5e-10` |
| mixed `(sx, sy)` | 12 | broken | `1.9e-01` | `1.0e-01` |

The broken-class entry is the minimum over those 12 frames of the smaller of the
two compare-sign multiset defects, so no choice of overall sign rescues them.
This derives the landed `6 / 6 / 12` classification of the same field.

### C6 — where the floor lives, and how it scales with the dial

The ladder is run for one all-minus proper rotation against one all-plus
three-cycle rotation, comparing sorted multisets stage by stage:

| stage | all-minus `L = 3` | all-plus `L = 3` | all-minus `L = 7` | all-plus `L = 7` |
|---|---|---|---|---|
| `rho` | `0.0e+00` | `0.0e+00` | `0.0e+00` | `0.0e+00` |
| `b` | `2.1e-14` | `2.9e-15` | `1.0e-14` | `1.8e-15` |
| `eps` | `6.9e-11` | `9.8e-15` | `1.5e-09` | `1.5e-12` |

The source multiset is bit-exact and the assembled load multiset matches at the
`1e-14` level, while the response multiset already carries the whole defect —
the negation floor enters at the linear-response solve, and no later stage
amplifies it. The metric stage inherits it through the amplitude dial alone: the
per-site sorted edge-length defect measures `1.4e-11` at `L = 3` against the
predicted `AMP * d_eps = 1.4e-11`, a product identity gated at half the predicted
value. At `L = 7` the same length defect prints `2.7e-10` and is reported
unscored. The endpoint consequence is amplitude-linearity of the negation floor:
the all-minus multiset defect measures `2.5e-12`, `4.9e-12`, `1.0e-11` at `AMP`
`0.05`, `0.10`, `0.20`, with successive ratios `2.0e+00` and `2.0e+00`.

## Derivation sketch

The argument has three finite steps, each verified exactly by finite computation
in the runner using integer matrices and link-dictionary equality.

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
   the `24/24` transversal row of C3, and it is what makes the coset
   representative unique rather than merely existent.

3. *The invariant is `sx`.* Each quartet element carries `sx = +1`, so `sx` is
   constant along each coset (the `96/96` row of C3). The unique constant-sign
   representative's common sign is its own `sx`, which is `sx(g)`. Composing step
   1 with C1 at the representative gives the multiset statement for `g` itself,
   with sign `chi(g) = sx(g)`.

Steps 1 and 3 are exact. The only floating-point content in the final statement
is the floor inherited from C1, which is why C6 locates that floor rather than
leaving it as an unexplained residue.

## Honest boundary

- The all-plus branch is exactly equivariant to within accumulation noise; the
  all-minus branch is not, and the size of its floor — `1.5e-11` at `L = 3`,
  `3.1e-10` at `L = 7` — together with its growth in `L` is
  measured, not derived. No constant is fitted anywhere in this cycle, and none
  is claimed.
- The magnitude of the mixed-sign breakage is likewise measured, not derived. The
  statement that is derived is its *scope*: the law holds on constant-sign frames
  and nowhere else, which the `frame_K_parity` biconditional gates in both
  directions at both box sizes.
- Improper elements are computational identities of the compiled chain only, per
  the framing section above.
- The collapse mechanism is specific to these two source domains and their
  stabilizers. A classification of stabilizers and collapse behaviour for general
  edit sets is not attempted here and is named as a next route below.
- Nothing in this cycle touches the amplitude dial's status, the response
  normalization, or any coupling; `AMP` is a supplied nuisance scale and the
  linearity row of C6 is a statement about it, not a derivation of it.

## The next paths opened

- **Derive the response-stage reflection floor constant.** C6 localizes the
  defect to the `b -> eps` solve; the next path opened is to characterize the
  constant itself from the open-box static operator and its sector
  regularization, turning a measured floor into a derived one.
- **Classify stabilizers and collapse for general edit sets.** The quartet and
  the mirror are the stabilizers of two particular sources. The next path opened
  is a general statement: for which edit sets does the stabilizer meet every
  coset of the constant-sign subgroup, and what replaces the multiset law when it
  does not.
- **Derive the `L`-scaling of the two branch floors.** The plus branch moves from
  `6.1e-15` to `4.6e-13` and the minus branch from `1.5e-11` to `3.1e-10` between
  `L = 3` and `L = 7`; the next path opened is a scaling law for both, which would
  also predict the mixed-sign breakage's mild decrease.

## Relation to the sibling cycles

The orbit-averaged all-24 carrier transport law of cycle 705
(`PHYSICAL_ORBIT_AVERAGED_K_ENDPOINT_TRANSPORT_D3_SELECTION_CYCLE705_NOTE_2026-08-01.md`)
concerns the AVERAGED carrier, whereas this note concerns the un-averaged
source-driven `K` field, whose all-24 law arises by coset collapse instead. The
frame classification measured in cycle 706
(`PHYSICAL_ENDPOINT_READOUT_QUBIT_STINESPRING_CHANNEL_CYCLE706_NOTE_2026-08-01.md`)
— the `12` plus / `12` minus single-axis split, the `6 / 6 / 12` two-axis
trichotomy, and the `1.0e-11` negation floor — is here derived in its counts and
located in its floor stage. Both sibling notes are unaudited open work, which is
why they appear in backticks here rather than as links.

## Runner

`scripts/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01.py`
executes every row above and reports

```
TOTAL: PASS=71 FAIL=0
```

with exit code `0`, `3483` characters of standard output, and a wall clock of
about `5.8` seconds on the development machine. Two consecutive runs produce
byte-identical standard output and a byte-identical receipt. The receipt is
written to
`outputs/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01_receipt_2026-08-01.json`
and carries no timestamp, no wall clock, no host name, and no absolute path, so
it is comparable across machines.

Every number quoted in this note is the runner's own measurement in the run that
produced that `TOTAL` line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [joined-compiler tournament note](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)

Cycle 700 and the joined-compiler tournament note are landed. Backticked context
only, with no links: `physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`,
`PHYSICAL_ORBIT_AVERAGED_K_ENDPOINT_TRANSPORT_D3_SELECTION_CYCLE705_NOTE_2026-08-01.md`,
and `PHYSICAL_ENDPOINT_READOUT_QUBIT_STINESPRING_CHANNEL_CYCLE706_NOTE_2026-08-01.md`.
