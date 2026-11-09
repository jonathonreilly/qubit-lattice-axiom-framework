# Source-exposed comparison of quantum outcome formation

Date: 2026-11-09. Research proof/implementation/axiom comparison; no landing
approval, audit verdict or new premise adoption. The original independent
note is preserved at SHA-256
`1eea23f7ba75a9b269eb40b2667cf3a54002eecdd56396a5e4eefdc01b9ec999`.

This follows the independent derivation and is explicitly source-exposed.
Requested worker profile remains `gpt-6-astra`, effort `max`; backend
attestation is unavailable. Current-main instructions remain those already
read at `bf92a1d763030836ed55631d5d7a7ef3b288f284`.

## 1. Findings at the frozen source

The local absorbing channel, its semigroup, state-independent empty-sector
hazard, both single-wing intermediate sectors, pointer protection, no-message
identity, finite pointer-capacity theorem and measurable-instrument density
argument are mathematically sound on their stated domains. They add a
different finite occurrence model to the instrument-tree proof; they do not
turn the quantum premises into deductions from the old axioms.

One source sentence needs an explicit domain restriction, and one numerical
fixture differs from its nearby prose. The proposed axiom also benefits from
three precise conventions before becoming governing text:

1. In RESULT section 4, the state `(I-a n.sigma)/2` is Bob's conditional
   state after Alice's outcome **before Bob has formed**. It is not Bob's
   full-history conditional state after both outcomes. For `n=z,m=x,a=b=+`,
   a positive-probability branch leaves Bob in `|+x><+x|`, not `|-z><-z|`.
   Insert “while Bob's pointer remains empty, before his formation.” This
   does not alter the intended full-history/neighborhood collision.
2. `check.py:310` uses `rho0=|0><0|` for the unordered-history test, whereas
   RESULT section 5 uses `I/2` and says both two-outcome prefixes have mass
   `1/4`. The executable's normalized future probabilities are still the
   correct `1/2` and `1`, but its two prefix masses are `1/2` and `1/4`.
   Either change the fixture to `I/2` and check the equal prefix masses, or
   describe it as a separate pure-state variant. The mixed-state hand proof
   is correct and is not refuted by this evidence mismatch.
3. The physical pointer clause should require **one readout decoder fixed
   independently of the stored value**, per specified pointer type. The
   capacity theorem uses precisely that hypothesis. “Its permitted readout”
   should not admit a different value-dependent readout for each content.
4. The general-state axiom is stated in terms of compatible finite-region
   functionals. Its update clause should therefore use a finite-support
   density or the dual state-functional formula, not leave “trace of the
   joint conditional state” potentially referring to an infinite global
   density matrix. Hold the actual instrument and local controls fixed when
   changing only the record information used for conditioning.
5. The measurable-instrument theorem supplies conditional states only almost
   everywhere. If the inherited qualification still demands one answer at
   **every** admitted exact history, the complete law must specify a
   measurable version and its null-history domain convention. The theorem
   does not choose a unique posterior at every supported singleton.
   The content map must be measurable; when it coarsens outcomes, push
   forward the instrument itself before conditioning on recorded contents.

Items 3-5 refine the adoption surface; they do not invalidate the finite
construction. Suggested exact wording and counterexamples appear below.
No source edits or reruns are performed by this worker.

## 2. Absorbing dynamics checked by generator eigenoperators

Write `E=I_system tensor Pi_e`, `O=I-E`, and
`R(X)=sum_a J_a X J_a^*`. Then `sum_a J_a^*J_a=E`, `J_a O=0`, and
`R(X)=R(EXE)` has support in the occupied block. In particular `R^2=0`.
The proposed generator is

```text
L(X) = kappa R(X) - (kappa/2)(EX+XE).
```

For arbitrary matrices, not only density matrices, decompose
`X=X_ee+X_oo+X_eo+X_oe`. The following are generator eigenspaces:

```text
L(X_ee-R(X_ee)) = -kappa (X_ee-R(X_ee)),
L(X_oo+R(X_ee)) = 0,
L(X_eo) = -(kappa/2) X_eo,
L(X_oe) = -(kappa/2) X_oe.
```

Exponentiating these four linear subspaces gives

```text
exp(tL)(X) = q X_ee + X_oo + (1-q) R(X_ee)
             + sqrt(q)(X_eo+X_oe),
q=exp(-kappa t).
```

This equals the stated Kraus channel. It proves its semigroup on all matrix
units, including empty/occupied coherences and the unused `11` sector,
through an eigenoperator route rather than relying on population dynamics.
Kraus completeness gives complete positivity and trace preservation with
arbitrary untouched references. The algebra also covers `q=0,1` and the
discrete composition identity `Phi_n(q)Phi_n(r)=Phi_n(qr)` at fixed `n`.
It does not claim that different axes satisfy the same semigroup identity.

For a normalized state wholly in the empty sector, the no-event branch has
weight `q` and its normalized system/reference state is unchanged. The
instantaneous jump intensity is
`kappa Tr(E rho)=kappa`; on an occupied sector it is zero. The resulting
waiting law is exponential with mean `1/kappa`, provided the supplied rate
and activation remain constant. For a coherent empty/occupied input the
conditional no-event dynamics is not scalar; the source correctly restricts
its record-sufficiency statement to legal empty/occupied record sectors.

`J_a` vanishes on every occupied output and `D(q)` is the identity there.
Consequently an old pointer, including all its system/reference correlations,
is fixed under later applications of this instrument. This is pointer
absorption, not repeatability of every possible future system measurement.
No finite closed-system unitary realization of irreversible exponential
decay has been proved. The source explicitly supplies the channel/occurrence
law and excludes reservoirs and actuation from its six-site count.

## 3. Two-wing process, conditioning and state sufficiency

Every A Kraus operator commutes with every B Kraus operator. Applying the
two maps to initially empty pointers therefore gives exactly the four
sector expressions in RESULT section 3, in either order. Their trace sum
is one. The total A-only mass is `(1-q_A)q_B`, the B-only mass is
`q_A(1-q_B)`, and the both-formed mass is `(1-q_A)(1-q_B)`, independently
of the input state and axes. Thus for interior `q_A,q_B` both kinds of
single-wing intermediate state occur with positive total probability.
Individual outcome sectors may vanish for special nonsinglet inputs.

These are two **local** two-record formation events. The proof supplies no
intermediate state containing just one bit of a single detector's two-bit
pointer; none is needed for the stated claim. It does supply the distant
single-wing intermediate states missing from the earlier atomic pair law.

For any outside observable `X`, the dual of a trace-preserving local map
fixes `I_local tensor X`. Therefore ignoring the local operation's outcome
leaves every outside expectation unchanged, including passive-reference
correlations. Selective conditioning on a particular outcome need not do
so. The same local map and controls are used in both calculations.

On the singlet and with B still empty, Alice's realized outcome gives
`rho_B=(I-a n.sigma)/2`; the local-history mixture over her outcome is
`I/2`. B's nonformation history supplies only a scalar survival factor and
does not alter this statement. The two positive Alice branches at equal
axes require opposite deterministic B outcomes, despite identical B record
neighborhoods. The full-record-local-odds reading fails; the no-message
theorem does not. After B also forms, its system state conditioned on both
outcomes is instead `P_b(m)`, which explains finding 1.

Constant, setting-independent occurrence removes outcome/setting bias from
the common-deadline conditioning. It is a supplied occurrence law. The
classical bound remains conditional on a complete setting-independent
causal factorization. The outcome-only relay witness correctly shows why
absence of a message named “setting,” or uniform designated output marginals,
does not establish this factorization or absence of setting information.

The record-sufficiency theorem agrees with the independent proof: a fixed
initial state and calibrated branch history determine a predictor, provided
the records distinguish all future-distinguishable histories. The source
correctly restricts this to a prepared domain. In the exhibited six-site
carrier the settings and activation are supplied controls; these six sites
alone are not claimed to encode the entire autonomous preparation/history.
All requisite control/preparation records must be supplied for H1.

The same-record examples `|0>` versus `|1>`, and singlet versus `I/4`, are
valid. The second pair also proves that separate one-site density matrices
are insufficient. Local Pauli product measurements recover all 16 real
coefficients in the Hermitian two-qubit Pauli basis. Thus equality for that
future test family implies full two-qubit density equality, while a restricted
test family requires only equality on its future-effect span. The source
does not turn this criterion into a proof of universal preparation genesis.

## 4. Pointer capacity and measurable instruments

### Capacity: correct theorem, keep the decoder hypothesis explicit

For one fixed readout POVM `{F_b}`, perfect recovery of value `a` from
`tau_a` gives `Tr tau_a(I-F_a)=0` and `Tr tau_a F_b=0` for `b!=a`.
All these operators are positive. If `Tr tau T=0` with `tau,T>=0`, then
`T^(1/2) tau^(1/2)=0`, so `T` vanishes on the support of `tau`.
Consequently `F_a` is identity on `supp tau_a` and zero on `supp tau_b`.
Hermiticity makes these nonzero supports pairwise orthogonal. There can be
at most `d` of them in dimension `d`. Mixed pointer states, additional
unused sectors and repeated readings do not evade this proof.

The model's three control states `00,01,10` fit in its two-qubit pointer.
The proof does not imply that absence must always be a readable symbol;
the source explicitly keeps absence distinct from recorded zero. Nor does
it identify every matrix-valued content label with a density matrix.

To bind this theorem to the proposed physical encoding clause, specify a
common decoder fixed independently of the stored value. Without that
hypothesis, take every `tau_a` to be the identical state and choose, for each
pre-known `a`, a constant readout that always announces `a`. Each label is
then “reproduced with certainty by its permitted readout,” while no label
information is stored in the pointer. This is not physical decoding; it is
exactly the ambiguity the added fixed-decoder wording removes. Readout type
or calibration controls themselves cannot be an uncounted value-dependent
memory. The exhibited pointer already uses the ordinary fixed bit decoder.

### Measurable instruments: the density proof is valid

I checked Proposition 2, equations 38-39, in Chiribella, D'Ariano and
Perinotti, [*Realization schemes for quantum instruments in finite
dimensions*, arXiv:0810.3211v4](https://arxiv.org/pdf/0810.3211v4).
The paper supplies an almost-everywhere CP-map density with respect to the
trace of the Choi measure. The candidate's division by input dimension
normalizes that dominating measure to a probability measure; it is harmless.

For the candidate proof, every matrix-entry measure has finite variation
bounded on partitions by the total Choi trace and is absolutely continuous
with respect to `nu`. Scalar Radon-Nikodym therefore applies. There are only
finitely many entries. A countable dense set of test vectors then gives one
common full-measure set on which the density is Hermitian and positive.
Trace uniqueness gives `Tr C(x)=d` there. Choi inversion yields the CP
density. These facts justify the stated integral and normalized conditional
outputs; no infinite-dimensional Radon-Nikodym theorem is used.

In particular `g_rho` is a probability **density**, not a singleton
probability, and `J_x` need not individually be trace-nonincreasing.
Neither is required: measurable-event maps are trace-nonincreasing, their
total preserves trace, and `g_rho` integrates to one. The source does not
incorrectly assert either pointwise bound. Its continuous-outcome extension
closes the avoidable finite-menu limitation of the independent note.

This theorem is compatible with the finite pointer-capacity bound. A
continuous instrument can have a classical outcome parameter without a
finite quantum register containing mutually orthogonal, perfectly readable
encodings of every exact parameter value. Adding exact permanent physical
storage requires the appropriate allocated register or an explicit finite
coarse-graining. The source distinguishes these tasks and does not claim
that its six qubits store a continuum.

### What remains a law/domain convention at null histories

The RN density is fixed only up to a `nu`-null set; its posterior is fixed
only up to an outcome-law-null set. Every exact singleton can have zero
probability in an atomless experiment, but almost every drawn value still
has the displayed conditional state. “Singleton mass is zero” and “the
conditional version is undefined at this point” are different statements.

For a concrete version witness, let outcomes range over `[0,1]` and let
`I(B)(rho)=Leb(B) rho`. The CP density is the identity channel almost
everywhere. At the one point `x=0`, replace it by any other channel. All
event maps and all outcome probabilities remain identical, but the declared
pointwise posterior at 0 changes. This supported point has zero mass.
Thus the instrument measure does not uniquely specify every pointwise
posterior. A complete trajectory law may choose a measurable version,
declare the admitted-history domain, or give a convention on null histories;
none of these changes any positive-probability prediction.

The current proposal already correctly says “almost everywhere.” If its
unchanged qualification is still read as a pointwise answer at every
admitted state, make this version/domain choice explicit. This is a precision
requirement for the governing law, not a failure of the density theorem.
Also require the content map to be measurable: a pushforward probability
law through an arbitrary nonmeasurable map is not defined. For matrix-valued
contents the Borel structure of `M_2(C)` supplies a natural codomain; support
can then refer to that pushforward law as the proposal intends.

If `c` is a noninjective content map, the recorded-content instrument is
`K(C)=I(c^(-1)(C))`, not merely the scalar pushforward of probabilities.
Conditioning on a recorded content uses this pushed-forward instrument (or
its density). It must not silently retain an unrecorded fine-outcome index.
For example the two branch maps
`I_0(rho)=(Tr rho)|0><0|/2` and
`I_1(rho)=(Tr rho)|1><1|/2` are CP and have trace-preserving sum. If both
outcomes encode the same record content, that content occurs with certainty
and conditions the system to `I/2`. Selecting either fine-outcome pure state
instead is a different conditioning question. This is particularly relevant
when a finite pointer uses a finite readout of a continuous instrument. An
explicit extra fine-outcome state/history may be supplied, but is not then
reconstructed from that coarse record alone.

## 5. Proposed axiom wording: type-correct update and fixed controls

The proposed general state is a compatible family of finite-region positive
functionals, not a trace-class global density. This is a sound way to avoid
choosing an infinite tensor-product Hilbert representation. In its probability
clause, make the finite support used by “trace” explicit.

Let the actual operation have finite support `N`, with its local controls
held fixed. Denote its event map by `I_B`, and let `omega_h` be the state
functional conditional on the specified history. The exact formulas are

```text
p(B | h) = omega_h((I_B^* tensor id)(1))
         = Tr[I_B(rho_(h,N))],

omega_(h,B)(X)
  = omega_h((I_B^* tensor id)(X)) / p(B | h),  when p(B | h)>0.
```

The second formula applies to each local observable `X` in a region enlarged
to contain `N`; it gives consistent restrictions on overlaps. Complete
positivity ensures positivity with references, and normalization follows by
setting `X=1`. It can change conditional expectations outside `N` for a
selected event. Summing all events before conditioning uses a unital dual
map and leaves every observable outside `N` unchanged. Thus the formulas
express exactly the desired distinction between physical local operations
and remote conditioning, without suggesting a global density matrix.

A concise candidate sentence is:

> For a specified local instrument with its actual local controls held fixed,
> outcome probabilities are its event-map traces on the corresponding
> finite-support conditional state. The conditioned state on all finite
> regions is obtained by the compatible dual-map update. Changing only
> which records are used for conditioning does not change the physical
> instrument or its controls.

If a conditioning description also omits the local control value, one must
average the **joint control/state ensemble**, or include the classical
control register in a controlled CP map. Applying an arbitrary single
control's map to the averaged state does not in general give that mixture.
The current “for fixed accessible record controls” phrase points in the
correct direction; making it explicit in the update paragraph removes this
possible misreading.

Likewise a pointer wording that binds the proved capacity condition is:

> For each specified pointer type, a single readout decoder fixed
> independently of the stored value reproduces that readable value with
> certainty. Its pointer and readout-control registers are included in
> the allocated physical sites.

These are narrow clarifications of the proposed amendment. The amendment
still adds genuine quantum composition, positive probability states and
completely positive instruments, and chooses the larger general state
description while allowing record-sufficient restricted domains. It does
not prove that the old four axioms forced that ontology. The quantum CHSH
cap follows within the resulting quantum class; no singlet, violation,
Hamiltonian, clock rate, or particular realized outcome is forced.

The explicit one-outcome-per-formation rule is a supplied stochastic
actualization postulate. The source correctly distinguishes it from a
unitary premeasurement or a reduced-state decoherence calculation. A
conditional local channel with classical branch sampling is a mathematical
stochastic model. Calling it a derivation of unique actuality, or a native
physical synthesis of the required channel, would go beyond the checked
result; the submitted sources do neither.

## 6. Full code and cached-output comparison, without execution

All 321 lines of `check.py`, all 85 lines of `exact.stdout`, the execution
receipt, and all four relevant stderr files were read. No code was run by
this worker. The exact-output and execution receipts embed the SHA-256 of
the reviewed code. Their asserted successful/failing executions are cached
evidence supplied by the supervisor, not independent replays.

The field arithmetic, sparse multiplication/adjoint/tensor embedding,
projector construction, pointer occupancy parsing, append-only branch
updates and conditional normalization are consistent with the mathematical
model. The code distinguishes missing keys from stored bit zero. Its
two-wing register indexing agrees with two eight-dimensional detector
factors. The 7 tested axes are unit vectors in the exact arithmetic field.

| Cached count/result | Actual code coverage |
|---|---|
| 7 completeness checks | The 7 supplied ideal axes at `q=1/2` |
| 448 matrix-unit semigroup and 448 trace checks | All 64 local matrix units for each axis; composition `q=r=1/2` compared to `qr=1/4` |
| 252 occupied matrix units fixed | 6 occupied system-pointer basis states squared, at each of 7 axes |
| 49 setting pairs | Both channel orders and branch-ensemble equality for the singlet |
| 427 record histories | `49*9` possible sector/outcome rows minus the 14 forbidden same-axis equal-sign rows |
| 560 permanent reapplications | 196 one-wing occupied applications and 364 both-wing occupied applications |
| CHSH `-2 sqrt2` | Four maximizing setting pairs, using both-formation conditional probabilities |
| Conditional B-plus `0,1` | Equal-axis singlet branches, with no survival branch in that particular check |
| Polynomial diagonal `-5 sqrt2/8` versus quantum `-sqrt2/2` | Correct four-axis conditional-state inconsistency |
| Partial-transpose witness `-1/2` | Correct negative expectation in `Phi_+` after transposing one singlet factor |
| Unordered-history Z-plus `1/2,1` | Correct pure-input variant; does not verify the mixed-input equal-prefix-mass claim |

The all-axis, arbitrary-input, arbitrary-reference and continuous-time claims
rest on the mathematical proofs, not extrapolation from these counts. The
measurable-instrument and storage-capacity proofs are not numerical claims.

The saved fault failures are specifically:

- `overwrite`: first fails at `check.py:249`, “channel semigroup on
  coherences.” The swapped occupied codes are also a permanence violation,
  but the cached run stops at the earlier coherence/semigroup assertion.
- `frozen-condition`: fails at `check.py:268`, “record-history conditional
  update,” comparing the corrupted record tree with the correct channel.
- `remote-setting`: fails at `check.py:259`, “remote setting entered local
  formation,” on a product input selected to expose a dependency hidden by
  fair singlet marginals.

Thus all three cached faults are rejected for concrete relevant reasons.
The no-fault stderr is empty. The stdout explicitly says continuous time
was not executed. Nothing here is an assertion of independent numerical
implementation, physical apparatus validation, or exhaustive quantum-model
checking.

## 7. Frozen identities, verification and handoff

The input base directory is
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/outcome_conditioning/`.
Every named argument and all code lines were read, including the assumption
table and complete axiom proposal. SHA-256 identities at this comparison are:

| Input | SHA-256 |
|---|---|
| `RESULT.md` | `84ddf59db9ef34693aa4f802b18525cbc00f3a92e7dd47acaa68402ee6dcfc2e` |
| `ASSUMPTIONS.md` | `787ed5e97002ef53dc93798920584d71f91647a4dd19f65f5a49bd14a60d8848` |
| `AXIOM_PROPOSAL.md` | `62ec5f6a94ad65bf55deeaf2342015700296f785d175758d69efb858f7676311` |
| `check.py` | `46127f2c9050de484dc444e5a3543a9d9aa8d93072d65c34ec33ecc9f1d9e0d0` |
| `outputs/exact.stdout` | `663852ae828eb236c753d869e85e630f9cd7a7da3e3b8b83fdd1533b6a3c6c6e` |
| `outputs/execution.json` | `753a287902e4df1bd36d7f3153f3c8e983b7e1128a55a8d7b5920b46da1a32e0` |
| `outputs/exact.stderr` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `outputs/overwrite.stderr` | `f80abedb003948db266449a141e9f44eff4f819f40640c650089e401bcc19712` |
| `outputs/frozen-condition.stderr` | `069459b2c284693c90772741deb56a0940c4640cda9d91143fa1c19685cee51a` |
| `outputs/remote-setting.stderr` | `3bd4e371361199a15223a63799ba6e4d4cdde5fd43fe2846a377db0da2000010` |

The unchanged main axiom source is identified in the proposal and in the
independent note at SHA-256
`301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`.
Its previously read instructions and premise wording were reused at the
same pinned revision. This task did not inspect or claim to validate new
registry, approval-policy, canonical-axiom or companion-runner edits.

The source findings were communicated to the supervisor, who plans a
separate revised-unit comparison. This note checks the frozen originals;
future corrections need a bounded read of their actual changed content and
new hashes. No actual amendment has been adopted in this check.

Only this `SOURCE_CHECK.md` was written. `INDEPENDENT.md` is unchanged.
No source edit, numerical execution, commit, push, audit or landing action
was taken. The full note is read back and source identities are refreshed
before its final handoff. The result confirms the conditional mathematical
construction with the concrete scope/evidence corrections and proposed
wording conventions above; it supplies no general theory or physical
implementation certification.

At final source refresh, the supervisor's working prose had advanced during
this check. The new `RESULT.md` hash is
`d1204793cf72a4e6b6a3fc5ceaaedeb70ad074dd2e1395d98360737e875cbeaa`,
`ASSUMPTIONS.md` is
`97ee3285e305396b0b1b4565c1d76013c14edcdfd2e1e09e040d18283d00f869`,
and `AXIOM_PROPOSAL.md` is
`2b8511e8b00cc9d012524b3ce23ac247ec631fd00f558147a37cf87e091ff5e4`.
Those new contents were not read and are not covered by this comparison.
The reviewed code, exact stdout and execution receipt remain unchanged.
The next handoff is a separate bounded check of the supervisor's revised unit.
