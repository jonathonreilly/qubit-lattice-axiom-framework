lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T09:00Z

## State of attack

**Honest stop — author check completed.** Pinned source:
`b58dac27c53adb17f47520c8ca2f784014a8dcbe`. This is author mathematical
research, not an audit or independent review. Mapped side only; the
independent attempt and its gates have not been read. No numerical job
has been run.

**Discharged:** the literal site-centered frozen bonds fail FG; the
walls are half-integral and a bond between two frozen bricks crosses
their common wall. **Implication:** a half-unit translation of the
auxiliary fill tiling repairs containment, with the same fill constant,
provided all plaquettes in each resulting closed vertex brick obey
the input bound. That last face-regularity check is explicit and is
not inferred from the present quiet definition. See
`../library/paid-inputs-frozen-mesh.md`.

**Discharged (counterexample to the untrimmed-energy formula):**
(CI-paid^d) with Z imported unchanged from (CI-N) subtracts action
which can be locked into quiet frozen data. An explicit abelian
SU(2) field has identity parents at every positive level, is a regular
constrained minimizer, and has positive A^Z at enough depth. Its paid
error is zero. See `../library/paid-inputs-frozen-energy.md`.

**Gap:** a different interpretation using only active energy is not
refuted by that example and is not proved here. It needs the precise
local target estimate (QT^d), fixed-link RF/bump bounds, and uniform
response to nested quiet data. The point-incidence argument for C_J
does not supply them. W1/W2 and LNC are not attempted after this stop.
The mapped part at this commit still lists frozen-data CI and junction
stability as open; its current reference convention has not adopted the
paid-reference proposal. The exact source comparison and scope limits
are recorded below.

## Scope and labels

**Unchecked (inherited analytic inputs).** The paid-reference proposal is read from
`../library/threshold-paid-reference.md` and `hard-core--threshold.md`.
Its multiplicative fill, regular-chain minimum, RF gluing, and nested
stability inputs are not silently promoted to proved facts. Each result
below is labelled **discharged**, **implication**, **gap**, or
**unchecked**, with constant dependencies stated.

Only this part and the three new library notes linked below were
written. No numerical job was needed, so no numeric-lock acquire,
memory preflight or numerical PASS is claimed. No consumer file,
axiom or ledger was edited; no commit, push, PR, audit, external post
or subagent was used.

## 1. Source convention and FG

**Discharged (source comparison).** At the pinned commit the mapped
State of attack still calls F2, (CI-N)^d and C_J open; Text 5.9 still
uses the T -> C_a T -> T_2 threshold discussion. The reference at
`quiet-boundary-rarity.md:47,69,81` and OW at 189 still use the old
fill and cells above T_2. There is no adoption or rejection of P,
N_ref, N_pay or Lhat in the mapped file. The paid proposal is therefore
tested as a proposed repair, not as already integrated source text.

**Discharged (literal FG fails).** BG's site bricks have half-integer
walls. Integer translation cannot turn them into the vertex walls
required by section 6 of the fill note. More substantially, the
actual rule freezes a bond when both endpoints are frozen; a bond
crossing between two frozen bricks is contained in neither closed
brick. The field 1 already exhibits this geometric failure.

**Implication (local repair).**
[`paid-inputs-frozen-mesh.md`](../library/paid-inputs-frozen-mesh.md)
proves that translating only the auxiliary fill tiling by half a unit
in each coordinate makes every original frozen bond belong to a
closed lattice-vertex brick. No block center, kernel or tree root is
changed. The fixed mesh then works with exactly the inherited fill
constant, provided every plaquette of these closed vertex bricks has
flux <=2T. This is the exact additional check (G3). Only previously
uncertified faces in a one-cell collar need adding to the quiet test.
The present Dev definition has not been shown to certify those faces,
especially at relative-quiet junctions. The repair is proposed here,
not imposed on the consumer. The geometry proof itself uses no
manifold or half-ball conclusion from BG.

## 2. CI-paid^d: a class-top frozen-action obstruction

**Discharged (necessary test).** At a class top P(V_i)=V_i and
N_ref(V_i)=empty. If U attains Acal_i^d(V_i), the proposed estimate
forces A^{Z_{i-1}(U)}(U)=0. Thus enlarging the paid support or C_W
cannot repair a positive, immovable contribution to that term.

**Discharged (explicit counterexample, exact scope).**
[`paid-inputs-frozen-energy.md`](../library/paid-inputs-frozen-energy.md)
constructs the following with the deterministic class kernel:

- In one fine parent block, the direction-1 links at offsets
  (0,1,0,0) and (0,-1,0,0) have angles +a and -a in one fixed
  abelian subgroup. All other links are 1. Exactly twelve plaquettes
  have angle a, and the all-lines parent is exactly 1. Reflection
  cancels the contour averages, and paired transverse lines cancel
  the straight averages. No small-angle truncation is made.
- Put one copy inside each of many fine frozen bricks, with its entire
  plaquette support frozen. Choose a>0 so each brick's Dev is at most
  eps_q^2 T^2; equality is possible at the usual small quiet threshold.
  Every higher-level field is 1, every label is zero, and all other
  frozen data are identity. Planar nested slab layers satisfy (N),(B)
  and the clearance, so neither a thin strip nor a junction pathology
  is being substituted for the prescribed data geometry.
- Each copy has positive, exactly fixed action e(a)=12(1-cos a).
  U makes all remaining plaquettes identity, hence
  A(U)=M e(a)=Acal_i^d(1). At large enough fixed depth, a level-(i-1)
  cell in the frozen band contains M copies with M e(a)>kappa T^2.
  Thus it belongs to the untrimmed Z and A^Z(U)>0.

The displayed inequality becomes M e(a)<=M e(a)-A^Z(U)/16, which
is false. All constants and the quiet threshold were fixed before
choosing the depth and volume. The example is already below 2T
everywhere and satisfies the extra face regularity of (G3).

**Scope limit.** The energetic coarse cell in this construction is
frozen. It refutes the formula with the *untrimmed Z expressly imported
from (CI-N)*, not a formula that excludes this fixed action. If the
author intends a meaning restricted to the region's active action,
that restriction must be stated and proved. Subtracting the same
frozen constant from A and Acal while keeping A^Z does not help.
Dropping every frozen coarse cell is also not automatically enough:
some such cells have free descendants that still need TE payment.

**Gap (a repaired active-energy comparison).** The exact local target
inequality used in the proposed proof at line 203 is

    E_Q(W^d) <= C_Q T^2 [ eps_q^2 + (T_2/T)^2 (r/L)^4 ],
    r<=r_*,                                               (QT^d)

for the portion of Q on which the descent may change the action,
with W^d satisfying the parents and every existing frozen datum.
C_Q,r_* must be absolute, independent of L, x, depth, volume and
the number/order of freezes. The descent needs, for instance,

    C_f C_Q [ eps_q^2 + (T_2/T)^2 (r_*/L)^4 ] <= kappa/4.

RF must also preserve the exact frozen links on the gluing band and
permit the parent-restoring bump at its stated cost. The no-data
proof of (CI-N) in lines 281-285 has no such hypotheses or conclusions.
Its support substitution is valid only conditional on these analytic
estimates; it is not a frozen-data proof. No error proportional only
to N_ref can pay a failure of QT^d at a class top.

## 3. Saturated data, junctions and long histories

**Discharged (what the hostile tests decide).** The fixed-action
construction works with arbitrarily small positive quiet residuals,
and can reach the quiet limit. A planar layer suffices; junctions are
not needed for that obstruction. Many levels allow many immovable
fine fluctuations under one coarse cell even though all coarse fields
are identity. This is a failure of the energy being subtracted, not
evidence that relative lift stability itself is false.

**Gap (junction stability).** The assertion at line 33 that a bound
on the number of bricks in one ball bounds a dependency chain is
invalid as an inference. A bounded-degree path has arbitrarily many
predecessors. Exponential decay of a fixed-background inverse is
not yet a uniform nonlinear response estimate for successive,
relative-quiet boundary insertions.

**Implication, with proof.**
[`paid-inputs-junction-response.md`](../library/paid-inputs-junction-response.md)
states the exact missing incremental estimate (IR) and proves that
it would give C_J uniformly for any number of same-level freezes:
sum the spatially decaying responses over distinct bricks. The
summation constant is explicitly bounded by

    S_4(rho)=sum_{m>=0} [2(m+3)]^4 exp(-8rho m)<infinity.

This includes several touching bricks and data at the quiet limit.
For different levels the needed row-sum estimate is (IR-nest), with
the scale factors included and a bound independent of total depth;
or one needs a transfer contraction q<1. Neither estimate is proved
for the actual nonlinear lifts. A C(L) prefactor does not meet the
consumer's absolute C_J/C_Q requirement. No independence among these
analytic gaps is asserted.

## 4. Dependent items and constant ledger

**Gap; not attempted after the stop.** W1 and W2 with the paid wide
supports remain unproved uniformly in data. W2's proposed proof reads
CI-paid^d directly; W1 uses the same frozen-preserving trial/glue and
class-minimum inputs. Their set-theoretic support enlargement does not
repair those inputs. LNC for Lhat, with open marks fixed and settled
gains constant, is likewise not attempted. Finite-range dependence of
N_pay is not a descent estimate.

| Quantity | Status and allowed dependence |
|---|---|
| Half-unit mesh shift, one-cell collar, incidences | **Discharged:** absolute; free of x,L,depth,volume |
| A_f and support distance 8n | **Implication:** A_f is the inherited absolute fill constant; n depends on T=a_*/L^2; lengths are fixed before depth and volume |
| t_0,d_x | **Implication:** may depend on L,a_*; mesh compatibility and t_0>=8n required; free of x,depth,volume |
| Counterexample | **Discharged:** any fixed admissible odd L and positive quiet threshold; a fixed first, then depth/volume chosen; independent of x and defeats every C_W because N_ref=empty |
| C_Q,C_J,C_R,rho,C_sum | **Gap:** consumer needs absolute constants (fixed threshold ratio allowed), free of x,L,depth,volume; no such actual nonlinear bound proved |
| S_4(rho) | **Discharged algebra/count:** depends only on d=4,rho; free of x,L,depth,volume if rho is absolute |
| C_5(L) in W1, budget constants | **Gap:** L dependence is allowed there; still must be free of x,depth,volume as specified by the proposal |

## Final disposition and reading record

**Proved:** the literal FG mismatch; a sufficient vertex-mesh repair
under its explicit closed-face regularity check; the exact abelian
identity-parent construction, quiet frozen realization, nested-layer
packing and counterexample to CI with untrimmed Z; and the response
summation conditional on IR. These are author derivations only.

**Conditional:** the repaired fill uses Theorem S/F2-mult plus (G3);
the junction sum uses IR (or IR-nest across levels). They do not
establish the source's analytic premises.

**Still open:** automatic (G3) for the present quiet convention; the
correct active-energy/excess version of CI, its TE allocation, QT^d,
and frozen-preserving RF/bump and response estimates; then W1/W2 and
LNC for Lhat. No claim is made that these are independent obligations,
or that a different proof cannot work.

Source reads were bounded: GOAL/FINISH; the threshold part and paid
reference; fill sections 5-6 and its angle convention; BG, the frozen
rule and relevant F-D/nest paragraphs; mapped State of attack,
Text 3.1, 5.1-5.2 and targeted 5.9; quiet-boundary setting, region
definition, layer geometry, Step 5, OW and its data paragraph;
relative-density Prop 10, its corrected induction and CI-N, and the
TE kernel/energy definitions; RF's statement and proof; and short
read-only ranges of the two mapped check scripts cited in the mesh
note. No independent-side file or gate was read. No existing numeric
PASS was treated as a result of this session. No literature lemma
was imported. The absent workflow file was read with git show HEAD;
the planning AGENTS was read for instructions only. The explicit
user scope controls this one-item investigation and this honest stop.
