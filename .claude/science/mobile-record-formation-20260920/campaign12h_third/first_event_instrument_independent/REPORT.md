# First-event instrument: source-informed check and correction acknowledgment

The individual-channel Gram identities, positive-rate first-time/mark law,
and full-output retained-mark logical recovery are supported. Two issues in
the initial draft were identified and have been corrected in the final source:
F1, the missing zero-total-rate case; F2, the overbroad claim that tracing out
matter could destroy the input's recoverability with all links and the mark
retained. No unresolved mathematical finding remains within this corollary's
scope. This is source-informed scientific review, not a blind derivation,
formal audit or publication decision.

## 1. Sources, changes and authenticated premises

Initial note SHA256:
`3f3794aa3473ae9442de9d48b7bccbbd0e000c6ae1a00c262975efa7ed6bca29`.
Initial three-artifact seal:
`5b0039fd58733af4a43b614299ce5f01d16cebc8635be462a21dad304c0d2353`.
Intermediate note after F1:
`8e9b0fa908b3b8c32256a019e72ad7ae2a163102768d048a83c7e6a2ea13c5d7`.
Final note:
`4b9dc935444bdfb3c01835c0c21e2d6cf420f5ea09cc1a5b2f52795cb00492ac`.
Final nine-artifact seal:
`2c446eb379dafa054df99ecb872e25ba0a9799d0f4801398132506bf0f2c48da`.

The complete original and final arguments and full two-step deltas were read.
The original and intermediate seals recover through their preserved
same-basename notes; all other dependencies retain their exact bytes. Every
current author binding authenticates. The exact deltas and separate
CORRECTION_ACK.json are retained here. Only the two identified scope repairs
and their provenance paragraphs changed; the Gram formulas and full-output
recovery argument did not change.

The supplied rotor/hopping/birth premises are reused from the immediately
preceding reviewed source at
`002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`
and the balanced formation source at
`b577c14e992fe74feb8a9f17c33e503f446f7052f83512031c2bf82cf2e3538d`.
Their independent final seals are bound here. This report does not import a
verdict across scalings: it checks the unit-rotor first-channel algebra and
its instrument consequence, with the earlier no-event field evolution as
an explicit premise. No new author scientific runner existed for this short
corollary; the exact control below is independently assembled.

## 2. Individual Gram operators

Initially every A site is plus and every B site is vacant. Fix edge (a,b).
For its birth to act after a single hop, that hop must empty a by moving its
old plus record to a neighbor d other than b. Hops from another A site do
not empty a, while the hop to b blocks the birth. These are all possible
terms of `-P j_mu T P` on the initial sector.

Write the resulting operator as

    B_mu = sum_l |q_l><q_initial| tensor U_l,

where l is the destination d for a resolved charge mark, or the pair (d,c)
for the unnormalized coherent sum of the two charges. Each U_l is a product
of two different unitary rotor shifts. It maps the zero-divergence input
field space isometrically onto the appropriate shifted Gauss sector. It is
not necessary to identify these different field sectors with the same
constraint space.

For fixed mark, distinct d have distinct final occupied B-site sets. The two
coherent charges also differ at a. Therefore the matter words q_l are
pairwise orthogonal and

    B_mu^dagger B_mu = sum_l U_l^dagger U_l = c_mu I,

with `c_mu=z_a-1` for either resolved charge and `c_mu=2(z_a-1)` for the
unnormalized coherent channel. This conclusion holds on all normalizable
physical input fields, including coherent superpositions, and is not a
classical diagonal-state calculation. Changing the coherent channel to a
normalized charge sum would change the coefficient; the note uses the
same unnormalized sum as its supplied model.

For c_mu>0, `V_mu=B_mu/sqrt(c_mu)` is an isometry. Degree-one channels are
zero and require no normalized V_mu. No assertion is made for bounded spin
at its cutoff, where rotor shift unitarity fails.

## 3. Time, mark and recovery

Let the self-adjoint pre-event Hamiltonian preserve the initial field sector,
as in the reused no-event calculation. The total loss is

    kappa sum_mu B_mu^dagger B_mu = r I,
    r=kappa sum_mu c_mu.

Consequently the unnormalized no-event density is
`exp(-rt) U_t rho U_t^dagger`. The joint first-event measure is

    Pr(T in dt, M=mu)=kappa c_mu exp(-rt) dt.

For r>0 the first time is exponential of rate r and the mark is independent
with probability `p_mu=kappa c_mu/r`. These are probabilities, not an assertion
that the quantum output state is independent of event time. The pre-event
state is `U_t rho U_t^dagger`, so recovering the original initial state needs
the known intervening evolution and event time.

F1 was necessary because arbitrary finite simple bipartite graphs can have
r=0. A single A--B edge is a decisive example: after a hop the B endpoint
is occupied, so the edge cannot form a pair. Both channel coefficients are
zero; there is no first event and `kappa c_mu/r` is undefined. The final
revision now explicitly separates this case and restricts normalized mark
and joint-output formulas to r>0. F1 is closed.

For a specified immediately pre-event density rho and a retained mark, the
joint channel has blocks `p_mu V_mu rho V_mu^dagger`. Let
`Pi_mu=V_mu V_mu^dagger`. A recovery on the complete marked output is obtained
blockwise from

    R_mu(sigma)=V_mu^dagger sigma V_mu
               +Tr[(I-Pi_mu)sigma] rho_*,

with any fixed normalized input density rho_*. This is completely positive
and trace preserving: the first term contributes trace Tr(Pi_mu sigma), the
second the complementary trace. On the code image it returns rho exactly.
Summing the marked blocks returns `sum_mu p_mu rho=rho`. The argument also
preserves an arbitrary reference system entangled with the input.

This mathematical recovery can lower record number and can require global
operations. It is not supplied as a physically allowed local inverse of
permanent record formation. The note correctly leaves that boundary explicit.

## 4. Matter erasure: the second finding

The original statement grouping matter erasure with possible input-information
loss was too broad for the stated retained-link/retained-mark setting. For a
fixed mark, each final matter pattern q_l fixes the field divergence by
Gauss: `div E=q_l-background`. Different q_l thus define orthogonal field
sectors F_l. Tracing matter gives

    N_mu(rho)=(1/c_mu) sum_l U_l rho U_l^dagger,

with mutually orthogonal ranges. Measure the divergence-sector label l and
apply U_l^dagger; this recovers rho exactly. Formally the map is the sum of
`U_l^dagger Pi_l sigma Pi_l U_l` on those ranges, completed by a fixed-state
term on the complement. The factors 1/c_mu sum to one.

Matter erasure removes coherence between output branches, but that does not
imply loss of the input's logical information. This conclusion depends on
retaining every field link and the mark, the known initial charge pattern,
and the unit-rotor model. It does not settle mark erasure, removal of some
links, later-event recovery, or available physical recovery operations.
The final note removes the loss assertion and states the orthogonal
field-divergence qualification. F2 is closed.

## 5. Independent exact cyclic-sector control

The chosen graph is K_{2,3}, with A={0,1}, B={2,3,4}, all six links oriented
from A to B. Each A degree is three, and the graph has two independent cycles.
Its zero-divergence fields can be parameterized by

    E=(x,y,-x-y,-x,-y,x+y).

The checker independently assembles every legal first hop and subsequent
insertion from nine input basis fields, x,y in {-1,0,1}. No spin or output
field cutoff is imposed. All output Gauss equations are checked. The resulting
finite matrices are exact restrictions of the unit-rotor maps, not finite-spin
approximations or imported author matrices.

For all twelve resolved marks it verifies exactly `B^dagger B=2 I_9`; for
all six coherent edge marks it verifies `B^dagger B=4 I_9`. The respective
output dimensions are eighteen and thirty-six. Thus both instruments have
total rate `24 kappa`, with different individually retained marks.

An exact complex superposition density tests the full isometric recovery.
After the matter trace, every distinct charge branch has a disjoint field
range; each branch's exact Gram matrix is I_9. The branch-conditioned field
recovery also returns the input density exactly for all eighteen channels.
These finite calculations check the normalization and erasure observation;
the general argument above does not depend on limiting the input to nine
flux states.

Both independent scientific and source-authentication runs passed their first
execution. Full stdout, empty stderr, exact result JSON and command receipts
are preserved. No failed probe was omitted and no scientific assertion was
relaxed. There is no author-grid replay or new numerical phase evidence.

## 6. Bounded disposition

Both requested repairs are explicitly acknowledged at the final identities
above. The unit-rotor individual-channel and retained-mark recovery corollary
is supported, with zero-rate and partial-output cases correctly qualified.
No physical measurement postulate, native register, fuel reservoir, local
record-annihilating operation, later-event law, erased-mark recovery theorem,
thermodynamic capacity, volume-uniform limit or audit status follows. Other
author packets, checkpoint, registry and Git state were not opened or changed.

All source and independent evidence identities are fixed in FINAL_SEAL.json.
