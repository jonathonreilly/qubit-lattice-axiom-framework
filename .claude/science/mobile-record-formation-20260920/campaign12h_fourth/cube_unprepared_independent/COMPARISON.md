# Original cube consequence: bounded post-PRE comparison

September 23, 2026. **No required mathematical correction or consequential
code/prose discrepancy was found in the authorized frozen candidate.** Its
ordinary-time, fixed-electric-window density theorem agrees with the
independently frozen reconstruction. The author also proves a stronger
uniform-input time-average lemma than the fixed-input version stated in
the independent PRE. That addition is checked below and remains explicitly
attributed to the author.

This is a selective scientific comparison. It is not a formal audit,
retention decision, publication, or a no-go packet PASS. In particular, the
trace-norm subsequence obstruction has only the specified model, scaling,
initial-sector and embedding scope.

## 1. Exact source binding and exposure

The independent PRE remains byte-for-byte fixed:

```
PRE_COMPARISON_SEAL.json
5d7d37fcc06fb75a647a1b5e2fe40b49ed6467c2185f5218da78b2fa2f8ca715
REPORT.md
2d33b037ebbdc469cb81db26af37554c3b8ba5aad47cf2772ca8cdd66c0b1294
```

Its five source and twenty artifact bindings were all reauthenticated.
The authorized candidate identities are:

| Source | SHA-256 |
|---|---|
| `cube_unprepared_author/AUTHOR_SEAL.json` | `ed066b95b18992f86718fe960ed6624c163854d142d0f90a742a4c85377159f4` |
| `CUBE_ACTUAL_FORMATION_LOCAL_DENSITY_LIMIT.md` | `5a546e000b2cea8309df035506f2c759daaa824712ca001d057567a91a9152d9` |
| `cube_physical_controls.py` | `20f0a6abf4066098cf719b74af22f9826d803b6ee51d9d772ed9ab56e104ce80` |
| `CUBE_LOCAL_LIMIT_CONTROLS.json` | `72f9ff4014d3b0744e3b59464d0e84e8ba66878fe65bef0260b5cc2c32ca6b40` |

The entire argument, runner, saved result and command receipt were read.
All six author artifact bindings authenticate. The three consecutive JSON
objects in its full stdout were parsed: the two spin rows and final result
agree exactly with the saved result. Its stderr is empty; its receipt says
exit zero and binds the executed runner hash and actual command.

No author runner was imported or executed. In particular, the transitive
`second_event_author/second_event_probe.py` source named by the author was
not opened in this task. The comparison instead rebuilt its load-bearing
rules from the independently frozen `cube_controls.py`. The named spectral
author seal was also not opened. Those two transitive identities are
recorded as deliberately unopened, not falsely reported as reauthenticated.
The other four already permitted source rows in the author seal were
authenticated.

The author freeze is dated 19:32:26 UTC and the independent PRE 19:56:19 UTC.
The independent PRE preceded this checker's candidate access. Reconstruction
progress was sent to the coordinator before PRE; no reciprocal author
blindness is claimed. The candidate explicitly credits the positive
trace-class commutant/time-smearing insight to the earlier independent ring
report, which the author had read. Its cube extension is source-informed.

## 2. Physical conventions and complete controls

Both constructions use edges
`01,02,04,13,15,23,26,37,45,46,57,67`, oriented low to high,
A=`{0,3,5,6}`, and Gauss `div E=q-1_A`. A forward hop of charge c
changes its directed field by `-c`; the hopping amplitude is negative.
Birth `(sigma,-sigma)` on the directed edge changes its field by `sigma`.
The normalized spin amplitudes and the effective sign `B=-jA` agree.

The five chord indices are `[5,8,9,10,11]` in both builders. The independent
tree solver deletes vertex 7 from the incidence matrix and has tree minor
determinant -1. The author deletes vertex 0 and has determinant +1. Each
solves the same full Gauss equation with the same fixed chord fields, whose
tree solution is unique. Thus the coordinates and physical fields agree;
there is no Fourier, hopping or magnetic-face sign change to reconcile.
Matter enumeration order is immaterial to the scalar checks.

The new comparison runner imports only the immutable independent builder.
It enumerates every charge-four matter word, applies grade selection, and
constructs every field in the complete physical spin box. It does not
truncate to a common small electric window. The reconstructed dimensions
are exactly:

| S | P4 | Q4 | P6 | Q6 | R6 | P8 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 69 | 840 | 1,308 | 3,168 | 1,128 | 672 |
| 2 | 767 | 11,112 | 22,092 | 56,832 | 20,856 | 14,964 |

All author combinatorial diagnostics agree: P6-to-Q6 maximum column/row
degrees are 6/3, Q6-to-R6 degrees are 3/6, the bare-creation Gram is diagonal
with range `[0,2]`, and fixed-edge opposite-orientation cross-Grams vanish.
The first-sector electric identity is exact at S=1 and has residual at most
`3.56e-15` at S=2. The largest discrepancy from an author floating diagnostic
is `1.78e-15`, arising from summation order. First-loss diagonal ranges are
`[20,48]` at S=1 and `[112/9,48]` at S=2; the zero-field value is 48.
These losses omit the common factor kappa in this comparison table.

The independent exact path construction also reproduces all six oriented
face vectors, H2 diagonal -12, Z-dagger-Z diagonal 168, H4 diagonal 60,
face coefficient -2, and thirteen total H4 Laurent terms. Both correctly
keep only five independent circulations despite writing six geometric faces.

The author bounds follow for all spins from its local path degrees and
amplitudes at most one:

```
||A_S|| <= sqrt(18),  ||H2_S|| <= 18,
||Pi2 T_S Pi1|| <= sqrt(18),  ||H4_S|| <= 486,
Gamma6,S <= 36 kappa I.
```

The last inequality uses at most one edge joining the one A hole and one B
hole in Q6, with two newborn orientations, so `sum j* j <=2I`.
Their ranges are orthogonal for a fixed edge even at finite S: the two
newborn charge patterns differ. Thus coherent and resolved total losses
coincide at finite S. Interference between different old-hop predecessors
within a single resolved channel remains possible, as both packets state.

The independent PRE's sharper all-spin bound `Gamma6,S<=16 kappa I` is
compatible with the author's conservative 36. Its proof uses at most eight
resolved paths per input and at most two predecessors of each fixed-channel
output. As additional post-comparison corroboration, the full S=1 and S=2
Gram matrices both have maximum absolute row sum 16. Coherent/resolved Gram
differences are zero at S=1 and at most `1.78e-15` at S=2. These computations
corroborate the path proof; they do not infer an all-spin theorem by sampling.

## 3. The author's stronger uniform-input lemma

The PRE stated time-averaged local escape for a fixed positive trace-class
input and trace-convergent spin approximants. The author proves, for every
fixed finite-rank Pi and finite T,

```
sup_(rho_S>=0, tr rho_S<=1, physical at S)
    integral_0^T tr(Pi V_S(t) rho_S V_S(t)*) dt ->0.
```

This stronger assertion is valid. For any sequence of admissible initial
densities and a fixed nonnegative smooth weight w, define
`R_S=integral w(t) V_S(t)rho_S V_S(t)* dt`. It is positive with trace at most
`||w||_1`. The trace-class unit ball is weak-star compact as the dual of the
compact operators; on the separable physical Hilbert space one can use a
countable finite-rank basis and diagonal extraction. Positivity and bounded
finite diagonal sums yield a positive trace-class subsequential limit R.
No singular state on the algebra of all bounded operators is substituted.

For every finite-rank finite-field L, the integrated equation divided by
eta makes the boundary and w-derivative terms O(eta^-1), independently of
rho_S. The bounded H4 and loss contributions are also O(eta^-1), using the
complete-space bounds. Strong convergence of the uniformly bounded H2_S
and its adjoint implies norm convergence of `[H2_S,L]` to `[H2,L]`. Hence
`tr([H2,L]R)=0` for every such L, and finite-rank approximation gives
`[H2,R]=0`.

A nonzero positive compact R has a positive finite-dimensional eigenspace.
Commutation makes that eigenspace invariant under bounded self-adjoint H2,
whose restriction then has a normalizable eigenvector. The supplied empty
point-spectrum result on physical H6 excludes this. Consequently R=0.
Taking w=1 proves the integral limit for every arbitrary initial sequence.
If the supremum failed to vanish, approximate maximizing densities would
provide a contradicting sequence. This proves the displayed uniformity.

The proof never used convergence of rho_S, a moment bound, absolute
continuity, a spectral gap, or a quantitative dispersive estimate. Its
whole-box zero extensions are uniformly bounded and converge strongly on
the finite-field core, sufficient for the compact commutator test.

There is no conflict with the PRE's varying-source refocusing counterexample.
Here one initial density is held fixed through each age integral, although
that density can depend arbitrarily on S. An adversarial source that varies
with age can prepare a different reverse-evolved input for every age. The
actual source therefore still needs the compact temporal control used in
both packets. This checked uniform-input addition is credited to the author;
the frozen PRE is not edited to claim it was already stated there.

## 4. Domains, first source, composition and topology

The complete first-sector identity

```
eta (H2_(4,S)+12I) = K sum_e E_e^2
```

holds up to and including physical spin boundaries. Its linear field term
cancels by zero-divergence Gauss. The rotor H4 is
`60I-2 sum_faces(W_p+W_p*)`, and the rotor first loss is `48 kappa I`.
The finite-spin first loss is field dependent; the candidate does not copy
the ring's exact finite-spin clock to this cube.

The diagonal electric operator is self-adjoint on `D(sum E^2)` with
finite-support core. Extending the spin generator using this same diagonal
operator plus uniformly bounded H4/loss perturbations preserves the
physical spin box as a reducing subspace. The bounded perturbations converge
strongly. Duhamel's formula on compact vector orbits, or the bounded
perturbation expansion, gives strong semigroup convergence uniformly on
compact time intervals. Trace-class approximation then applies to any
fixed normalizable initial field density with trace-convergent physical
spin embeddings. No unbounded field moment is silently assumed.

It follows that the N4 density and its positive first-source curve converge
in trace norm uniformly on compact times. The limiting source is continuous
and has compact range in trace norm. Its trace is `48 kappa exp(-48 kappa t)`;
its state depends on the evolving first-sector field, including for the
original zero-field initialization. The source is not replaced by a fixed
post-mark vector at every first-event time.

The exact triangular N6 equation is its no-event propagator convolved with
this time-dependent first source. Approximate the compact positive source
curve by finitely many positive trace-class anchors. Positivity lets each
age subset assigned to an anchor be bounded by its full age interval.
The time-averaged escape lemma then gives uniform compact-time disappearance
in every fixed N6 electric window. The author's lemma is sufficient; the
weaker fixed-anchor PRE lemma already suffices for this composition.

The absorbing N8 equation then transfers the result by finite jump range.
The author uses the safe enlarged window R+2. Each allowed old-hop/birth
path actually changes two distinct links by one unit, so the independent
R+1 enlargement is sharper but does not correct an error. The bounded
summed Gram controls all interfering paths entering the output window.

Both packets therefore determine the same local density:

```
rho_loc(t) = exp(-48 kappa t) exp(-it h_f) rho0 exp(it h_f),
h_f = K sum_e E_e^2 - 2 delta sum_faces(W_p+W_p*),
```

supported on N4. The omitted `60 delta I` is an irrelevant scalar phase in
the density. The limiting trace is `exp(-48 kappa t)`. At t>0, a full
trace-norm convergent subsequence would have these same finite matrix
elements and hence this density, contradicting trace continuity from the
normalized states. This is a precise statement about the fixed common
embedding. It does not supply a full normalized limiting state or a
rescaled electric distribution. The limiting S/window orders differ.

The parent deterministic microscopic-to-target trace-density estimate is
uniform in normalized spin on this fixed graph and tends to zero as
`epsilon^2=delta/[K S(S+1)]`. Applied to the original P-supported initial
sequence, it transfers the local density and subsequence obstruction.
Neither packet invokes a new conditioned microscopic restart estimate at
a random first mark. The microscopic transfer remains dependent on the
source-bound parent target theorem, not a new independent reproof here.

## 5. Separately attributable independent additions

The following conclusions were in the independently frozen PRE and are
not attributed to the narrower cube candidate:

1. The sharper loss bound 16 kappa and window R+1; the compact interference
   counterexample to a proposed bound of 8 (rotor expectation 10).
2. An explicit zero-field finite-spin first-clock counterexample. With
   C=S(S+1), the first survival differs from `exp(-48 kappa t)` by
   `16 delta^2 kappa(32/C-8/C^2)t^3+O_S(t^4)`. At S=1 and K=delta=kappa=1,
   the cubic coefficient difference is 224. This reinforces the candidate's
   caution without contradicting its limiting first clock.
3. Quantitative global count constraints. Set
   `a=e^(-48 kappa t)`, `g=(3/2)(e^(-16 kappa t)-e^(-48 kappa t))`,
   and `h=1-a-g`. Then p4 tends uniformly to a, p6+p8 tends to 1-a,
   p6 has asymptotic lower bound g, and the exact finite-spin target bounds
   are `0<=p6<=1-a` and `0<=p8<=h`. Number curves are equicontinuous;
   each subsequential limit obeys `0<=p8'<=16 kappa p6` almost everywhere.
   No unique limiting p6/p8 split or positive lower bound on p8 is supplied.
4. Explicit logical countercontrols: a rapidly varying positive source can
   refocus despite the time-average escape lemma; translated absorbing N8
   states can have vanishing fixed-window density with total N8 probability
   one. Neither counterexample is asserted to be the actual original cube
   output. They delimit inferences from temporal averaging and local topology.

The author's survival lower bound using 36 kappa is valid and can be
sharpened to 16 kappa by the independent bound. This quantitative difference
does not affect its local theorem. The numerical spin checks do not turn
the upper hazard bounds into exact exponential second clocks.

## 6. Spectral dependency status and limits

The additional authorization allowed these exact identities:

```
cube_point_spectrum_independent/FINAL_SEAL.json
f2df1efd5a7c7a63fb5200c0becb48278f79e448000afddcc8dc2bc48785111f
cube_point_spectrum_independent/COMPARISON.md
8872145e6701ca9ee33e33572a9bc01fc816af429ad36867582aa8b9b31cbe08
```

Both authenticate, and the full comparison was read. Its bound original
REPORT and PRE are unchanged. It records no required correction after an
independent reconstruction of the author's exact three-fiber certificate;
its own separately frozen two-fiber/modular certificate remains intact.
The domain is only the physical six-record, charge-four P-space rotor H2.

This closes the pending *comparison* dependency recorded at the present
packet's PRE. It does not constitute a new independent spectral proof in
this consequence packet, recursive authentication of every spectral
artifact, or a formal audit. No spectral author source was opened here.
In particular, the empty-point-spectrum premise is not applied to N4
(where rotor H2=-12I), N8 (where H2=0), or a zero extension to P-perp.

No material unresolved implication remains for the bounded local-density
consequence. The separate number split, fields growing with S, unbounded
electric observables, convergence rates, alternative models and scalings
remain outside the conclusion. All compensation/proposal packets, the
general compensation checker, campaign checkpoint/plans/registry and Git
remained excluded. The PRE's restricted scope stress test is not a formal
retained/no-go verdict.

## 7. Actual execution and preservation

`comparison_check.py` exited zero in about 1.993 seconds, with empty stderr.
Its receipt records the actual command, environment, source identity,
start time, duration, exit status, and stream hashes. The new runner source
is `7540325da9e91d9d4d086fcd29e4a564eca4dbce3113fce7beb63a4fd3d44120`.
Complete results, stdout and receipt are kept in `COMPARISON_RESULTS.json`,
`COMPARISON.stdout`, and `COMPARISON_RECEIPT.json`.

One read-only ad hoc metadata inspection initially used `Path('.').parent`
for a sibling path and raised FileNotFoundError. It was repeated correctly
with `Path.cwd().parent`; no science run or artifact was affected.
`POST_PRE_ADHOC_FAILURE.json` preserves the actual command, tool chunk,
observed exit and error, and explicitly records that no separate timed
receipt existed. A first FINAL-generation attempt then failed on an
incorrect manually counted artifact total before writing FINAL. Its source,
streams and observed receipt are preserved under
`failed_attempts/manifest_count`; the repaired sealer inventories all files
recursively and checks explicit required inclusions. Neither failure alters
the mathematics or PRE evidence. No failed mathematical run is hidden.

All PRE bytes, including the original historical checkpoint and limitations,
remain fixed. `POST_COMPARISON_CHECKPOINT.md` records the current completed
state. The FINAL seal binds the preserved PRE, the new comparison artifacts,
and the exact opened source identities. The final disposition asserts no
Git mutation, publication, formal audit, retained status, or general no-go.
