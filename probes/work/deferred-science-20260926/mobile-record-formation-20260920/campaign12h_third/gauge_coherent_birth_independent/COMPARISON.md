# Frozen-source comparison: partial gauge hops and coherent birth

The mathematical arguments and stated finite results agree with the sealed
independent reconstruction. The additional open-box jam certificates and
observability claims also pass the bounded checks below. There is one
terminology/scope correction, F1: the parameter chi classifies the summed
birth CP map, not a refinement in which individual mu outcomes are retained.
No formula or numerical correction is indicated. This is scientific source
scrutiny, not an audit or publication disposition.

## F1: distinguish the coarse map from a marked instrument

Section 2 of `COHERENT_NEUTRAL_PAIR_FORMATION_AND_GAUGE_MEMORY.md` is headed
"Complete instrument family on these two formation transitions" and allows
arbitrarily many environment outcomes. Its formulas correctly classify the
coarse birth map and the birth generator by chi. They do not, on their own,
classify the individually retained mu outcome maps.

For beta=1, consider the two Kraus lists

    {V_+, V_-},
    {(V_++V_-)/sqrt(2), (V_+-V_-)/sqrt(2)}.

They are related by an exact unitary Kraus rotation and both give chi=0.
Their summed maps and total losses agree on every input. On a vacant
negative-flux input, however, their conditional-on-birth outcome
probabilities are respectively (1,0) and (1/2,1/2). The corresponding
retained outcomes therefore describe different instruments. The independent
post-seal check verifies these probabilities and the exact Kraus rotation.

A narrow sufficient correction is an explicit sentence saying that the
chi classification concerns the coarse birth CP map/generator after summing
over mu; a retained mu record requires the separate outcome maps as extra
data. The finite-step Choi-rank conclusion concerns that coarse channel and
its minimal coarse event/no-event realization, rather than arbitrary finer
outcome records. The calculations themselves already operate at this scope.

The author accepted this correction and is preserving the reviewed bytes
until this seal. **F1 remains open against the frozen source identities in
this report.** A subsequent corrected-source acknowledgment must check its
actual delta separately.

## Completion theorem and the finite-box claims

The author's partial-bijection hypothesis is the one needed by the
independent proof: it controls the total map between each pair of distinct
occupation patterns. The allowed graph is defined from those nonzero tU
maps. The proof neither treats arbitrary H0 edges as such controlled maps
nor assumes that occupation monitoring measures individual field states.

Stationary positive birth loss vanishes; the Hilbert-Schmidt dephasing
identity forces commutation with all n_x. The off-pattern (c',c) block of
the stationary Hamiltonian equation then contains only tU rho_cc and
rho_c'c' tU. Partial bijectivity removes all other same-pattern coherence
terms from that block. Unitary conjugacy propagates traces to a positive-loss
configuration and eliminates each nonfull component. This agrees with the
pre-seal argument, including arbitrary occupation-preserving H0.

The finite-dimensional Cesaro/absorbing-corner argument supplies convergence
of occupation probability, a fixed-model exponential survival bound, and a
finite mean. The even-sector premise and number-phase argument appropriately
scope the counted first-completion statement. Neither convergence of the
whole internal density nor a size-uniform bound is asserted. The theorem's
condition is sufficient; its failure alone does not prove failure after
adding other occupation-preserving interactions.

The original independent enumeration already verified the ordinary-hop
criterion on all 375 and 25386 physical basis states of the two small boxes.
The new comparison also reconstructs the additional support-reachability
claim: every one of these states is reachable from the positive-flux vacant
basis state by a directed sequence of legal hops and births. This is a
support-graph claim, not an independent claim of full quantum controllability.
The quantum completion result comes from the separate operator proof.

The author uses bits for negative links; the independent enumerator uses
bits for positive links. Complementing the internal bit string relates the
two conventions. Both include the same frozen positive outside reference
fields and omit boundary transitions. There is no periodic-boundary or
electric-sign mismatch in the compared counts.

### A separate observability argument and independent certificate

For a stationary nonfull density, its support must be contained in the
kernel of the birth loss and invariant under H and every occupation
projector. The orthogonal complement of this support contains all contact
basis states and their orbit under those operators. If the generated space
is the whole nonfull sector, no stationary nonfull density remains.

Projecting onto entire occupation patterns does not introduce field
measurement: each such projector is a product of n_x and I-n_x. Conversely
n_x is a sum of pattern projectors. The algebra generated by these two
projector families is the same. The author's closure code retains linear
combinations inside each pattern block, rather than projecting onto each
field basis vector.

The integer Hamiltonian construction retains the multiplicities of forward
and reverse occupied-record cycles. The prime 1000003 is checked by trial
division through its integer square root. Full rank over this field certifies
full characteristic-zero rank; a modular deficit alone would not certify
a dark subspace. The code and prose state this distinction correctly.

The new independent check does not rerun the author's elimination. It
constructs the complete transition matrices from the independently assembled
physical configurations and square traversals, with coefficients
(kappa,field,cycle)=(2,3,5). It explicitly sums the two record-cycle
orientations before comparing matrix elements. The maximum cycle-channel
multiplicity is one on the small cube and two on the 2x2x3 box.

For every ordinary hop c->d, it verifies the exact single-column identity

    Pi_(s(d)) H |c> = 2 |d>.

The target pattern differs from the source. All field and record-cycle
terms stay inside the source pattern and are therefore removed by this
projection. Starting from the contact basis states, a breadth-first path
in the ordinary-hop graph thus constructs every remaining basis vector
by a word of projected H maps. Division by 2 is valid over Q and over the
stated prime. This gives a direct basis certificate for the asserted rank,
without numerical spectral tolerances or a second use of the same elimination
routine. The argument also covers the declared kappa=1 cases and arbitrary
same-pattern coefficients; it is not restricted to the chosen H0 values.

The certified nonfull sector dimensions, in increasing record number, are

    2x2x2: 1, 30, 156, 170,
    2x2x3: 1, 82, 1427, 7394, 11684, 4598.

The largest required projected-hop word lengths are respectively two and
three. The independently counted contact ranks agree with every model row
in the author output. This checks the substantive rank claims, while the
author's insertion-count bookkeeping is authenticated as output rather
than independently reproduced.

### Larger open-box jams are appropriately limiting controls

The additional check decodes every negative-edge, charge and birth-sequence
entry of the N=4,6,8 certificates using an independent open-box geometry.
It checks that each listed birth acts on two still-vacant endpoints and
that the final negative links form the matching claimed. It then recomputes
all possible vacancy hops, births and both elementary field-loop orientations.

| N | Internal links | Elementary faces | Legal sequential births | Final hops/births/field channels |
|---|---:|---:|---:|---|
| 4 | 144 | 108 | 31 | 0 / 0 / 0 |
| 6 | 540 | 450 | 107 | 0 / 0 / 0 |
| 8 | 1344 | 1176 | 255 | 0 / 0 / 0 |

All 64,216,512 charge entries respectively agree with the decoded fields;
the two stated interior vacancies and boundary conventions agree as well.
These vectors are isolated inactive components of the ordinary-hop graph,
so they fail the sufficient criterion. They do not contradict the small-box
theorem. In particular this check does not turn their existence into a
claim about arbitrary enlarged H0, universal failure under record cycles,
or a thermodynamic phase. No matching search or large production trajectory
was replayed; the stored finite certificates themselves were reconstructed.

## Birth coherence and fresh-memory results

Apart from F1, the local classification is correct. The two domain and range
orthogonalities, common loss beta P, Gram positivity |chi|<=1, converse Kraus
construction and real-chi edge-reversal condition match the independently
derived identities. The explicit fixed reversal action matters; the note
does not introduce an unstated phase convention. Positive stationary-loss
arguments indeed transfer to this family without measuring charge orientation.
The source also correctly says that equal loss does not imply identical
transient histories in every interacting model.

The complete C4 density, not just its occupation probabilities, agrees with
the independently verified 16-state equation. The survival probability is
(4 exp(-beta t)-exp(-4 beta t))/3, its mean is 5/(4 beta), and the terminal
two-state density is [[1,chi^2],[chi^2,1]]/2. The stated purity
(1+chi^4)/2 and normalized cycle expectation chi^2 follow directly. Forward
and reverse record-cycle terms give H_cycle=2g X_cycle on this ring; that
factor is included consistently in the note and runner.

The occupation-monitoring and specified real loop/cycle Hamiltonian
commutators hold for the whole displayed trajectory. The prepared initial
cat is an explicit resource. This exact control makes no claim of arbitrary
initial-state phase preservation, no unstated interacting Hamiltonian is
included in its clock, and no native record-only measurement is inferred
merely from the existence of a gauge-invariant operator.

The fresh-memory unitary, its two Kraus operators, composition law and
semigroup matching at collision boundaries agree with the pre-seal
calculation. The note explicitly keeps the intermediate-time reversal,
freshness assumption, sqrt(beta/Delta_t) coupling cost and failure of exact
finite-step composition for general noncommuting generators in view. The
retained-probe pi/2 countercontrol is the same exact return-to-vacancy
mechanism independently checked earlier.

The rest-energy statement is precisely [m N_record+2m P_fuel,C]=0 for a
supplied m and probe gap. The source does not extend it to arbitrary field
or kinetic energies and does not derive an autonomous supply or clock.
Its finite pure-environment dimension claim follows from the three Choi
eigenvalues 16+2c^2 and (1-c^2)(1+/-chi), at the stated 0<c<1. The ranks two
and three agree with the independent controls, and the pure-resource/
purification caveat is explicit. F1 clarifies the scope if finer mu marks
are to be retained beyond the coarse event instrument.

## Read, execution and provenance boundary

All three notes, all five current scripts, every result field, all receipts
and the complete logs were read. Four stdout/result pairs are byte-identical.
The jam stdout deliberately prunes its long matching/charge/history arrays;
the exact pruning relationship was checked against the full result, whose
arrays were independently decoded. All five final receipts have zero exit
status, their checker hashes match, and all final stderr files are empty.
The observability result also binds its actual inventory-script dependency.

The 28 frozen author artifacts and all 20 prior independent source/artifact
bindings authenticate. No author checker was imported or rerun. The new
`comparison_check.py` imports only the sealed independent helpers; it passed
on its first execution. Its full log, empty stderr, result and dependency-
bound receipt are preserved. The earlier harmless report-edit mismatch
remains recorded; no scientific failure was discarded.

The three named source histories were also inspected. The observability
revision adds only the primality assertion and its import; all previous
scientific result fields are identical. The two preserved failed receipts
stop at structural symbolic-equality assertions. Replacing only those
assertions exactly recovers the current full scripts, and both recorded
expanded differences are identically zero. Their failure streams and source
identities are bound in `SOURCE_HISTORY_REVIEW.json` and the final seal.
This confirms their limited diagnosis without replaying the failed runs.

The reviewed note identities are

    PARTIAL_BIJECTIVE_GAUGE_HOPS_AND_QUANTUM_COMPLETION.md
    eb46b801aa126fbcf4b950c5f6a2fb775f247b07fde8900556a3101338cce8b1
    COHERENT_NEUTRAL_PAIR_FORMATION_AND_GAUGE_MEMORY.md
    1e7dd9088f8835455fa274bafe019a455acd340c97231a86bc44243db515ad38
    FRESH_MOVING_MEMORY_DILATES_COHERENT_PAIR_BIRTH.md
    88c14c443b9dc2457d494e27ec9bfeb52f45b91784556fb7ed5766c49a93aa08

The frozen author seal is
`016efff81e95874edb19222e7d5b490bc0b1e1693aed003b04a58d444fa71f08`.
The unchanged independent pre-comparison report and seal are
`eb588f78316fe92791af32c698ed7991fa92fe5f3d64e978e959486866b87d57`
and `fc30598ddaf5e586a999301ba3ad4561a78a6614268399d09fa8fb435519cc3b`.
All full source, runner, result, log, receipt and historical identities used
here are recorded individually in `FINAL_COMPARISON_SEAL.json`.

The repeated-interaction literature citation is contextual and was not
independently reread; no theorem from it is an input to this comparison.
Autonomous rail, formation-count/global-coherence follow-up, virtual-Hubbard
work and the root checkpoint remained unopened. No new model, thermodynamic
claim, native encoding, quantum-history ontology, publication decision or
formal audit status is supplied by this report.
