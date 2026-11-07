lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T05:00Z

## State of attack

*Lead note, 2026-11-01 (Opus 5.5, not independent, not an audit).* Launched as `codex exec -m gpt-6-astra` at reasoning effort max on the Mac mini: 12:35Z finish, 33,197 output tokens. The lead read this report and not the proofs in `library/dm-stopped-kernel.md`; nothing here has had an independent read.

Honest stop: DM remains open. The conditional reduction and its elementary
proofs have been checked by their author; there has been no independent read.
Source pinned to `ae6bb189621a8f54d84347c84c59de476152eda4`.
Task: Theorem DM only, on the mapped side. No sibling attempt or gates on it
are read. No numerical experiment has been run. This is an author derivation,
not an independent review or an audit.

- **Discharged (defect in the argument):** the level-(i-1) stop with W fixed
  does not localize the outer level-i integral. Thus its free-bond count is
  not uniform in the region. This is not a counterexample to DM itself.
- **Discharged:** positive stopping-ratio algebra, a rooted graph entropy
  bound, and a corrected finite-depth column count, in
  `../library/dm-stopped-kernel.md`.
- **Implication:** (S) and (LMK) in that note imply a precisely quantified DM+
  with the same final per-mark factors as DM. The modified budget includes
  brick-support multiplicity and the finite hierarchy's top boundary.
- **Gap:** prove (S), especially its actual integration-volume/certificate
  coding, and (LMK)/(PAY) for the SU(2) integrals. Same-level certificates
  cannot be bounded by citing the DM under proof.
- **Discharged tests:** many separated marks require a factor per root;
  a long thin component requires a cost per added cell. Induction on fewer
  marks fails; proper-region induction alone does not prevent repeated
  same-level losses. A direct local estimate would avoid an inner induction.
- **Gap, inherited:** same-threshold fills and uniform-data analytic inputs
  are not supplied by a T to C_a T extension.

If resumed, the next mathematical target is (PAY_i), with actual
stopped measures and original mark events, not another formal summation.

## Scope and starting point

The starting source is `library/quiet-boundary-rarity.md:89-105`, and defect 1
of `gates/theorem-dm-codex-892504e4c.md`. The gate permits a counterexample to
the bond count while explicitly leaving the probability bound undecided.
The user restricts all output to this file, new lemmas in `library/`, and
`checks/dm/`; those restrictions override the general workflow's delivery and
campaign steps.

## Result: what a level-i stop would repair

**Discharged (algebra), gap (lattice estimate).** A stop including level i
does cancel the exterior of the W integral, provided its event is measurable
on and outside the final layers for each fixed enlarged support. This is
Lemma C of [the new note](../library/dm-stopped-kernel.md). Certificates inside
the support must remain in the numerator. The resulting inequality is

    Q_i <= sum_h sup_(Sigma,d) I_h^N/I_h^D,

not a normalized average over h. The sum needs an estimate on the actual
stopped integrals, including terminal supports that occupy the whole region.
The existing level-(i-1) stop does neither job for the outer integral.

**Gap (LMK_i), exact replacement obligation.** With the fully quantified
definitions in the new note, the required local bound is

    I_h^N/I_h^D <= exp[-G(M)+P_i(M_<i)
                       +(w_i/2)(a_i(M)+|M_i|)] u_i^v_i(h),
    u_i = C_u exp(-c_u x_i eps_q^2 T^2).

Here h specifies the certificates and interior rough restrictions; v_i(h)
counts their encoded extension cells; P is the corrected lower-level
cluster budget; w_i=C_E log(e+max_(r>=i) x_r). All constants are fixed before
volume, depth, region and compatible quiet data are chosen. **The physical
inequality above was not derived.** Its raw energy version (PAY_i) in the
note states precisely how much surplus must remain after the marked gains
and C n_active log x_i have been paid.

**Implication, proved.** If the stopped representation (S) and LMK hold,

    Q_i <= exp[-G(M)+P_(i+1)(M)] <= product_b z_b             (DM+)

uniformly in all the original parameters, with the original final z_b of
DM. P corrects the brick-support multiplicity and the last N_c levels of a
finite hierarchy. This is an explicit conditional replacement, not a claim
that DM has now been proved. The new note proves the positive-integral
algebra, graph summation and budget bound; it does not assume a small loss
per cluster without summing the extensions.

## The induction concern and its stress tests

**Discharged logical analysis.** Using DM_i to price a level-i certificate
in a proof of DM_i is circular unless another decreasing parameter is
actually supplied. Merely drawing a new stopping layer supplies no such
parameter. Induction on the number of marks goes the wrong way: M becomes
M union Y. Induction on the number of free top bonds is well founded on
strict subregions, with all mark sets quantified at each size, but has two
remaining obligations: B=Omega need not decrease that size, and losses from
repeated same-level restrictions must not accumulate. The recurrence
f(n)<=(1+u) max_(m<n) f(m) allows f(n)=(1+u)^(n-1); the coupling's decay over
levels does not control this same-level repetition.

**Implication, acyclic order.** One can instead aim for

    I_0 -> LMK_0 -> DM+_0;
    (all earlier I,Z,DM+) -> Z_i -> I_i -> LMK_i -> DM+_i.

LMK_i must then price its top certificate marks directly by local energy
and integration, with only lower-level DM available. This would need no
inner induction. The base LMK_0 and the uniform classical inputs are still
owed, and the earlier Z/I closure and the change from Psi to P are not
certified here. Thus the lead's concern is real for the circular use, but
does not establish an unavoidable same-level cycle.

**Discharged bookkeeping tests, not SU(2) probability computations:**

1. A long thin rough set of m cells needs an O(m)-cell tube and O(m log x_i)
   entropy. A surplus c x_i T^2 **per cell** can pay this and an exponential
   count of shapes for large x_i. One surplus for the entire component cannot.
   A shell must leave its thick pocket in the common exterior. The actual
   certificate-to-volume bound, including winding components, is in (S).
2. For N separated marked clusters, even N independent optional extensions
   have sum (1+u_i)^N. A single 1+epsilon_i or a bound of 2 fails. The proved
   graph lemma gives exp(C u_i N); its loss is summable per mark over levels.
   This permits arbitrarily many separated marks without multiplying
   unproved conditional probabilities.
3. Retaining R unanchored remote optional defects gives (1+u_i)^R. That
   factor cannot be charged to one mark. Cancellation must remove those
   defects before a pattern sum, rather than call “W rough somewhere” rare.

No numerical search was needed for these exact algebraic examples. They do
not refute DM for lattice Yang-Mills and do not rule out other repairs.

## What the pinned upper chain can read

**Implication, conditional on DM+ for the lattice measure.** Fix r>j, a
level-r field W_0 regular everywhere, take i=r-1, the whole torus and no
frozen data. This gives the law of all marks through level r-1 below W_0,
at arbitrary r-j. In particular:

- Type-I marks at level j give exp[-x_j c_S eps_q^2 T^2 |S|/4] for separated
  non-quiet bricks. With the mapped handoff w=6t_0, the upper chain's
  7w/3=14t_0 separation meets the stated 12t_0 requirement. Its cell/brick
  events must use the mapped local-lift definition of quiet. Choosing
  lambda_j with 8w_0 lambda_j<=x_j c_S eps_q^2 T^2/4 gives the numerical
  rarity input of Lemma 22.2. The flow permits one affine lower scale
  lambda_j=l_0+l_1(K-j), with l_0,l_1 fixed after the constants.
- Type-II marks at prescribed cells S_k, at any number of levels k<r, give
  product_k exp[-x_k c_T T^2 |S_k|/16]. Since non-regular flux >T_2>=2T
  implies membership in R_k, this is the prescribed-cell joint bound in
  (RAR^ch) at `upper-chain.md:823`, including nested stacks. Spatial choices
  of witnesses for Ch still incur the upper chain's stated union counts.
- These probability inequalities pass to mixtures of regular-top laws by
  integrating the same uniform upper bound. No depth-one restriction or
  factor proportional to r-j has been inserted.

The relevant pinned statements are LL_j and (K3) at `upper-chain.md:1236-1242`,
Lemma 20.5 at `:1252`, and the split (RAR^1)/(RAR^ch) at `:1476-1481`. For
the regular-top part of that lemma, DM+ would supply the one-level rarity
used to control failed separators and rough annuli, and the multilevel
rarity used by its (K2) stack recursion. It would **not** itself prove K3 or
Lemma 20.5: (MD*), (LOC), the lower-level class bounds and the other stated
closure hypotheses remain necessary.

The pinned consumer still describes quiet by a flux threshold in places;
the event-definition conversion requested in the mapped handoff is not
proved by this DM calculation and remains for that file's rewrite.

**Limit of the handoff.** LL_j also contains the mu marginal and point
masses at regular level-j fields. DM+ does not give the mu estimates or
the marked (U)/chessboard input. A point mass at the marked level is not
a law below a strictly higher regular top; one must not assert non-quiet
rarity for it from DM. Non-regular-cell events have probability zero under
a regular point mass, and applying the lower fibre kernel to a regular
point mass is covered by DM+. These observations do not extend DM to a
rough top or establish a locality bound for arbitrary LL_j by themselves.
The consumer file was not edited.

## Reference threshold and inherited conditions

**Gap, not solved here.** The algebraic stopping and graph lemmas require
no reference field. The proposed proof of LMK through the pinned Z_i and
OW does: W^# must have flux <=T_2, agree with W off tube{flux(W)>T_2}, and
retain all prescribed frozen bonds. This is exactly the same-threshold
(EXT=), not the T-to-C_a T fill. Substituting a C_a T_2 reference into I_i
would leave its stated class domain. Enlarging the tube to include cells
above T changes the class branch and its zero-extension factor, so is not
a silent repair.

Uniform-data W1/W2 and (CI-N)^d, nested-layer stability and the modified
energy exchange (LNC) remain inherited gaps in that route. Closing any one
is not claimed to close the others. In particular, the new graph lemma
cannot supply a patch energy inequality or a reference field.

## Final disposition

- **Proved:** fixed-support exterior cancellation, the anchored extension
  sum, finite-depth cluster counting with explicit support multiplicity,
  and `(S)+(LMK) => DM+ => the displayed per-mark factors`. The examples
  above prove failures of particular counts and induction proposals only.
- **Conditional, exactly on (S) and (LMK):** a uniform arbitrary-depth DM+
  for the actual lattice law and its regular-top rarity handoff. A proposed
  derivation of those hypotheses through I/Z/OW additionally inherits the
  analytic and same-threshold conditions just listed; they are not proved.
- **Still open:** (S), LMK/PAY for the stopped SU(2) integrals, the base local
  estimate, and hence DM itself. No counterexample to DM is established.
  This is an honest stop at the exact local inequality, not a no-go theorem.

Read scope: GOAL and FINISH; the supplied DM gate; targeted ranges of
`quiet-boundary-rarity.md` (setting, DM/CC, stopping Steps 1-6 and OW);
the fill report's threshold comparison; pinned upper-chain interfaces and
nearby stopping/consumer text; the mapped handoff at line 255. Searches of
the permitted library found the existing stopping scheme, not an already
proved LMK. Methodology files were read through git where absent from this
sparse checkout. No sibling part or gates on it were opened. No numerical
experiment, audit, subagent, commit, push or PR was run.
