# Independent vertex-output derivation (2026-11-08)

Status: bounded conditional mathematical construction; no retained/audit verdict.
Checkpoint: bounded derivation complete; record-sufficiency obligation remains open.

## Provenance and scope

Assigned read-only worktree: `/Users/jonreilly/.codex/worktrees/admissibility-mediated-influence/Physics`;
HEAD `b41467898cc49537960667bf6411c0eb7a867483`.
Science sources read completely from `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/docs/`,
at initial clean source HEAD `985f174411be88e0cb7e826f0df8f2ad3c16ea35`:

- `SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md`
  SHA256 `0d457372fe995529ad1fc13e3c9d6f696fe27b9a5ee3b1ef78852214a928604c`.
- `SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_BOUNDED_THEOREM_NOTE_2026-11-08.md`
  SHA256 `1cb33015822b869b4baf24ceaf04502c50e88ef92ec412642300ffac2423d51e`.

Final read-only refresh found source-worktree HEAD
`5a90fb30e3ff99fac9cd51a5823fcbd31e5a6aff`; both scientific file bytes still matched
`git show 985f174:<path>` exactly, with the above pinned hashes. A parent update
reported an axiom PR merge; this proof imports no new axiom premise.
Source statuses and premise choices are not independent scientific authority.
No parent candidate formula, runner, or numerical result was supplied or used.
Host-subagent task requested inheritance of the session model and maximum reasoning;
no model substitution or external worker was launched. This worker's interface does
not expose an actual model/effort identifier, so that configuration is requested,
not independently verified. No cross-family independence is claimed. The restricted
brief contained the two source notes, but no parent candidate construction; independence
does not by itself establish correctness.
First shell command was `python3 scripts/lab_ops.py preflight` (exit 0). Full stdout:
```text
ok      disk: 116 GB free, limit 10
ok      memory: 37% free, limit 25
note    load: 9.8, limit 8
note    model floor: no target named, no floor checked
ok      nice: works here
note    memory cap: ulimit unavailable; a job must watch its own memory
ok      network: origin reachable
preflight: go
```
No numeric job was run.
Methodology was read from the assigned worktree and is byte-identical to remote-main
`f5af11cd0102cfd0b51aef0911f600130bf5beb1` (read-only ls-remote and local diff checked).
SCIENCE_WORKFLOW SHA256: `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`.
workhorse/SKILL.md SHA256: `e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8`.
The matching SKILL_FRESHNESS_CHECK.md was also read; no instruction file was edited.

## Lemma 1: freeing precisely the vertices preserves origin separation

Let Lambda=(Z/(5n)Z)^3, n>=3. For p in (Z/5Z)^3 let V_p be the native sites
whose three residues equal p; A_p the sites with exactly one differing residue;
and S_p the sites with at least two differing residues. These disjoint sets
partition Lambda. Put the given four-qubit link code J(R) on each coarse edge
interior A_p, arbitrary qubits on V_p, and |0> on every site of S_p. The resulting
isometry is I_p: L_p tensor O_p -> H_site, where H_site is the native qubit
Hilbert space and
L_p=R^(tensor 3n^3), O_p=(C^2)^(tensor n^3); denote its range C_p^+.
Thus dim C_p^+=5^(3n^3) 2^(n^3), with 112n^3 still-fixed qubits.

For p!=q let Delta be the set of differing residue coordinates. If |Delta|=1,
choose a q-edge direction i outside Delta. Every interior site differs from p
in the fixed Delta coordinate and in i. If |Delta|=2, choose i outside Delta;
there are already two fixed differences. If |Delta|=3, any direction leaves
two fixed differences. In every case the entire chosen q-edge lies in S_p,
not in the newly freed V_p. The p-subspace has |0000> on that edge; the q-subspace
has range Q=JJ^dagger, and Q|0000>=0. The corresponding orthogonal tensor
factors prove C_p^+ perpendicular C_q^+, even with arbitrary link/output
entanglement. Hence C^+=direct-sum_p C_p^+ has 125 orthogonal sectors.

Let D_x be the existing product of six Q's on the disjoint incident edge
interiors S(x), with |S(x)|=24. If x has residue p, every factor acts as identity
on C_p^+. Otherwise the preceding proof, with q=residue(x), finds one of
these incident edges wholly in S_p, so its Q annihilates C_p^+. Therefore
D_x I_p = delta_(residue(x),p) I_p. No detector includes the site x itself.
The proof uses only Q|0000>=0 and disjointness, not basis sampling.
Translations and proper cubic rotations permute V_p,A_p,S_p and map Q to Q
under either edge orientation; therefore they permute the enlarged sectors
and send D_x to D_(g x) exactly as before.

## Lemma 2: the supplied generator is identity on the enlarged outputs

Keep precisely the source's H_native, including its D-sandwiched electric and
magnetic seeds; do not alter its coefficients. In sector p a translated seed
based at x vanishes unless x has residue p. Every remaining detector and every
encoded electric/plaquette factor acts only on A_p, never V_p or S_p. The same
coarse counting as in the source therefore gives the stronger intertwiner

    H_native I_p = I_p (H_p tensor I_(O_p)).

This is an operator identity for every output state, including states entangled
with links or an external system. Each C_p^+ is invariant and, by self-adjointness,
reducing. Exponentiation gives the corresponding identity for every finite time.
It is sector-wise output triviality, not a global commutator with the physical
qubit algebra at each site: a vertex in one phase is a data site in other phases.
No off-code output-protection assertion follows for the unmodified H_native.

## Lemma 3: an explicit finite covariant readout instrument

Conditions: ordinary finite tensor quantum mechanics and Born/Kraus instruments;
the supplied encoding/electric observable; fresh pointer preparation; a classical
record-status map; and the selection rule below. These are supplied constructions,
not conclusions from an axiom or from code geometry. Assign trivial gauge action
to output qubits. No adjacent-gate implementation of the origin test is asserted.

Let r: Lambda partially maps to {0,1}, Rec(r)=dom(r), with absence meaning blank.
An on-code compatible state has Rec(r) subset V_p, every recorded pointer equal to
|r(y)>, and every unrecorded vertex prepared in |0>. Permit arbitrary active-link
states and external entanglement. With r empty, permit coherent superpositions
of every p. More generally permit coherence among all p compatible with r;
a nonempty Rec(r) already fixes the residue p. Denote this joint domain by K_r.
The geometry and generator lemmas hold on all C^+, beyond this prepared domain.

For an incident *unoriented* coarse edge ell at x put

    q_(ell,0) = J_ell |0><0| J_ell^dagger,
    q_(ell,1) = Q_ell - q_(ell,0).

They are orthogonal projections, sum to Q_ell, and commute with D_x.
Because K|0>=|0> and K preserves its orthogonal complement, reversing the four
positions leaves both q's invariant. All six edges have the same orientation-free
meaning. Let B_x=|0><0|_x D_x, an orthogonal projection, and set

    m_x(r) = 1 if ({x} union S(x)) intersect Rec(r) is empty, and 0 otherwise,
    F_x(r) = m_x(r) B_x,
    A_(x,ell,b)^r = sqrt(m_x(r)/6) |b><0|_x q_(ell,b) D_x,
    N_x^r = I - F_x(r).

The guard checks every site acted on. In particular already-filled x gives only
the identity branch. The extra exclusion of old records from S(x) is unnecessary
on a compatible true-phase input, but protects them for the off-code completion.
No operator product of different D_x's is used; they need not commute off-code.

Exact normalization follows without a matrix computation:

    sum_(ell,b) (A_(x,ell,b)^r)^dagger A_(x,ell,b)^r
      = (m_x(r)/6) |0><0|_x D_x sum_ell Q_ell
      = m_x(r) B_x = F_x(r),
    (N_x^r)^dagger N_x^r = I-F_x(r).

There are six incident links. Thus the local success branches plus the null
branch form a trace-preserving instrument on the *entire* native Hilbert space.
Success appends r(x)=b; null leaves r unchanged. Every branch factors as identity
on old recorded sites. For consistent old pointer contents this preserves their
values in every outcome, not only on average. If an unrecorded pointer is |1>,
B_x rejects it; no reset or overwrite is hidden in the formula. Off-code actions
are defined by these formulas, without an electric interpretation there.

Choose one x uniformly from N=|Lambda|=125n^3 at each supplied discrete step.
The global Kraus operators are N^(-1/2) A_(x,ell,b)^r and N^(-1/2) N_x^r, with
outcome tags (x,ell,b) and (x,null), and the preceding record update. Their squared
operators sum to I. This is a finite instrument and a time-homogeneous hybrid
quantum/record update under the supplied clock and scheduler. If ell is not
publicly observed, sum its six CP branches, not their amplitudes.

For a space-group element g, site permutation U_g, and reindexed record map gr,

    U_g A_(x,ell,b)^r U_g^dagger = A_(gx,gell,b)^(gr),
    U_g N_x^r U_g^dagger = N_(gx)^(gr).

The proof is permutation of the supports, orientation-invariance of the q's,
and the geometric guard; uniform x and ell preserve the weights. This proves
translation and proper-cubic covariance of both the outcome-resolved instrument
and its unobserved channel. Each branch uses at most 25 qubits, in radius four;
this is finite support, not an elementary nearest-neighbor formation rule.

On K_r in sector p, a fresh x in V_p has m_x=1 and B_x=I. Conditional on the
chosen x, branch (ell,b) is exactly 1/sqrt(6) times the logical operation

    |0>_x tensor psi  ->  |b>_x tensor P_(ell,b) psi,
    P_(ell,0)=|0><0|_ell,  P_(ell,1)=I_R-P_(ell,0).

Its probability is Tr(P_(ell,b) rho)/6, and it reports E_ell^2=3b/4.
Completed branches preserve every link code and the Gauss subspace, since the
P's project onto invariant endpoint-representation summands. Tensoring every
operator with I_A proves all statements for arbitrary external entanglement,
including mixed inputs; no product-state assumption entered the proof.
For x outside V_p, D_x annihilates the whole sector and the attempt is null.
Thus the joint update maps K_r into the appropriate K_(r') and never reuses Rec(r).

For a coherent input sum_p I_p psi_p, the success branch at x keeps only
p=residue(x); null acts by I-F_x on the whole superposition. A record of the
physical location x therefore resolves its origin. Null outcomes can also
reduce origin coherence. This is a well-defined quantum instrument on coherent
inputs, not a claim that readout preserves origin coherence or treats it as an
initial classical mixture. The Hamiltonian itself does not mix or measure p.

## Finite capacity and meaning of the contents

The pointer state |0> represents both blank and recorded zero; the native qubit
does not distinguish them. The separate partial map r makes that distinction
and controls the guard. It is explicit extra state information relative to the
native qubit state, not a third orthogonal pointer state and not an axiom derived
here. Only vertex qubits have been freed; no native quantum factor was added.

In one realized sector there are n^3 output sites. With k records, at most
n^3-k additional outcomes can be stored, with success probability (n^3-k)/N per
uniform attempt on K_r. A first recorded location selects p, so the 125 origins
do not multiply this capacity. Exhaustion gives null attempts; no recycling or
indefinite output supply follows. The supplied H_native can be interleaved at
chosen times on K_r and keeps every old pointer unchanged; its off-code action
is not covered by this permanence claim.

Content b means the *measured past* value 3b/4 under the supplied observable map
and instrument; subsequent magnetic evolution need not preserve that link value.
If only r is retained, the sampled ell is not retained. The outcome-b effect
conditional on a fresh true vertex is (1/6) sum_ell P_(ell,b), the mixture of
six electric measurements, not the energy of an identified edge or their sum.
An identified-edge interpretation requires a known selector or additional
recorded provenance. Spatial covariance alone supplies neither interpretation.

## Exact residual: closure on current records

The formulas close a finite live-quantum-plus-record process under their supplied
conditions. They do not close a law whose complete current state is only r.
For an explicit failure of that closure on the present domain, fix p and empty r.
Compare all links in the vacuum to a state with exactly one elementary plaquette's
four links occupied. The latter can be Gauss invariant: regroup the occupied
endpoint factors and choose the singlet of the two spin-1/2 ends at each of the
four vertices; all other endpoints are trivial. Both have the same blank pointers
and current records. At a corner x of that plaquette the probability of b=1,
conditional on that x, is respectively 0 and 2/6. Equivalently the probability
of next record r'={x:1} is 0 versus 1/(3N). This tests the mixture instrument,
not merely a hypothetical directed-link instrument.

The named remaining obligation is record sufficiency with invariant updating:
specify allowed live-state classes S_r (or a reconstruction from current records)
such that Tr(Phi_(r->r')(rho)) is independent of rho in S_r for every r', and
every conditional updated state lies in S_(r'); any inserted Hamiltonian step
must preserve the same sufficiency. Then prove the resulting record-only kernel
has the required neighborhood dependence and formation rule. History-based
reconstruction requires its own consistency proof. The witness excludes closure
on the full supplied domain, not every possible restriction or another record
instrument, and does not prove that an axiom change is necessary.

## Final verification limits

This is a direct proof check using geometric supports, projector algebra, and
an explicit Gauss-compatible probability witness; no numerical runner, giant
matrix, source edit, commit, push, retained promotion or audit was performed.
The two source notes' cited prior-work discussions were read; no outside result
is required by this proof and no additional literature search or novelty claim
was made in this bounded two-source assignment. Completed claims: enlargement,
local detectors, generator restriction, finite covariant normalized instrument.
Remaining physical-law obligation: the record-sufficiency condition above.
