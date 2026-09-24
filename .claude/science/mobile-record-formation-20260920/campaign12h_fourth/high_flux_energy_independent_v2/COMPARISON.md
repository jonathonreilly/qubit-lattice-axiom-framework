# Comparison of the two frozen high-flux energy packets

Completed 2026-09-24. No mathematical discrepancy was found in the scoped
claims below. The author extension's additional resolved-output identity

    Var(h)=K^2 n^4+392 delta^2

is confirmed by a new full H4 image calculation using the independent PRE's
own frozen operator implementation, followed by a word-for-word comparison
with the author certificate. This is a conditional source comparison, not a
landing decision, independent audit verdict, or retained-status promotion.

## Frozen sources and exposure order

The completed independent reconstruction preceded comparison and remains
unchanged. Its PRE seal SHA256 is

    3bf5577d8caf04c9f446f46dca570d43565ab4e58f775984ce479233ac9089a4

All twenty PRE-bound artifacts were authenticated before and after comparison.
The three post-PRE comparison programs only create new files; they neither
rerun the PRE's output-writing entry points nor alter its sealed results.

The compared author units are:

| source | SHA256 |
|---|---|
| high_flux_energy_author/HIGH_FLUX_ACTUAL_BIRTH_ENERGY_SPREAD.md | a355623459a0bea115b0874ab03a1f691f55a71fa67785b4f04f68513a3ad472 |
| high_flux_energy_author/AUTHOR_SEAL.json | 92272978616462937a76398eb2a1a1af03c08de92c59abc73f5de3ed84496d8f |
| high_flux_energy_extension_author/ROTOR_DRIFT_AND_FINITE_SPIN_HIGH_FLUX.md | de24a51431ba27f10d178286da2c95cc69081b06a9058d225d4840e3225388c0 |
| high_flux_energy_extension_author/AUTHOR_SEAL.json | 2163902fc70b3077356c0097e61746f617ede94a5283ccb961270d48d4b091ea |

The task identified checkout HEAD `723dacc0eee0ed9897f5c9445be72cdfbc71389d`.
The scientific comparison is bound to the listed note/script/source hashes,
not an assumption that unrelated concurrent checkout content stays fixed.
The PRE's compensation and parent operator-definition premises retain their
original bytes. No new framework premise was accepted.

Both complete notes, all six author scientific scripts, the author seals and
execution receipt, and the transitive `local_compensation_independent/model.py`
implementation were read. The model's pinned hash is
`686529f4cd3dd5d73e3373f2604e56615c83228b5813a3848f2a194db00ae128`.
All 29 distinct author-seal-bound paths were hash authenticated.
`COMPARISON_RECEIPT.json` distinguishes fully inspected scientific sources
from additional historical context that was only hash authenticated. The
latter does not receive mathematical review coverage through this comparison.
Complete comparison-source snapshots are in `comparison_sources/`.

## Claim and implementation comparison

| load-bearing statement | independent evidence and comparison result |
|---|---|
| Cube orientation, hard-core charge rules, physical face-circulation input | The PRE derived hop/birth signs from the parent definition and checked Gauss after each formal transition; the author builder agrees. The input is a normalizable electric basis vector for every integer n. |
| Resolved (01,+ at0) first-output D measure | Both paths and their complete charge/field words agree. Squared rotor norm is 2; D values are 0 and 2n^2 with equal probabilities. The state remains a coherent two-path output. |
| Original all-mark electric balance | Independent path counting and symbolic enumeration give intensity 48 kappa and D gain 96n^2, hence electric drift -96 kappa K n^2. The coherent grouping is justified by orthogonal charge outputs. |
| Original h mean and variance bounds | The PRE derives H4=-Z*Z/2 and its boundedness on the cube, giving the stated order bounds without assuming that the input or output diagonalizes H4. The extension sharpens the selected variance as checked below. |
| Exact rotor H4 expectations and loss | The PRE independently obtains input mean -84; resolved-plus output mean -20; resolved-minus mean -14; coherent-edge mean -17; total H4 gain -816; full initial loss 48I on this sector. The author results agree. |
| Coherent magnetic contribution | The two resolved orientations have orthogonal Z images because the occupied birth B endpoint keeps its differing charge during outward Z hops. All twelve inner products were independently recomputed as zero. This identifies the stated initial sums, not later histories. |
| Exact initial total-energy drift | Both instruments give kappa(3216 delta-96K n^2), with the full loss term included. The calculation uses the loss eigenidentity, not an energy-eigenvector assumption. |
| Spin selected weight and D moments | The PRE's exact shift weights give a^2 and a, with a=1-n(n+1)/C. Norm a(1+a), mean 2n^2/(1+a), and variance 4n^4 a/(1+a)^2 agree for a nonzero mark. |
| Spin all-mark identities | Every one of the 48 author paths agrees in charge word, field polynomial, squared amplitude, D, and full sum E^2 with the independent symbolic builder. Rate, D gain and drift reduce to identical rational expressions. |
| Spin boundaries | The author's reused path comparison covers 55 (S,n) cases. Additional own exact square-root tests include S=1 and both n=+/-S boundaries. The selected plus mark is correctly absent at n=S; no conditional variance is assigned to that zero-weight mark. |
| Finite-spin H4 coefficient | Both arguments retain -{M_S,D}/(2C)-Z_S*Z_S/2. The PRE independently computes the stronger exact H4 drift polynomial and confirms that this term stays O(1) along moving high-flux inputs. No rotor H4 substitution is made at finite spin. |
| Moving high-flux limit | The exact spin identities imply the author's positive selected limiting weight, order-n^4 variance, limiting rate, and negative order-n^2 drift. These agree with the PRE's equivalent S-scaled formulas for n/S -> x in (0,1). |
| Limit, domain and physical boundaries | The notes distinguish fixed-input rotor convergence from escaping moving inputs; they restrict the unbounded-observable derivative to the specified finite-support forms and do not identify system-energy changes as heat or a reservoir balance. These qualifications are necessary and remain in force. |

The original selected-path script stores analytic norm and moment formulas
rather than recomputing every one of them from its output list. Its actual
path and D evaluations agree with the supplied proof. This does not create a
coverage gap here: the independent PRE and post-PRE controls calculate the
moments from the actual vectors. The original all-mark script enumerates
resolved channels; its coherent conclusion uses the stated orthogonality
argument, independently checked in the PRE and comparison.

All six author scientific scripts were rerun with bytecode writes disabled
and outputs redirected into this owned comparison directory. Every execution
returned zero and reproduced the corresponding sealed JSON byte-for-byte.
This reproduction is consistency evidence; scientific independence comes from
the previously frozen own implementations and their separate reconstruction.

## Additional full H4 moment: independent reconstruction

`comparison_full_h4_control.py` imports only the own frozen PRE direct-action
implementation, whose SHA256 is
`3523e5e79b181b82502bd71049daf99bc5dcf9eb1dce4facccf79b11c0600a6b`.
It does not import an author builder. The post-PRE target value was known, and
this exposure is explicit; no parameter or path coefficient is fitted to it.
The existing implementation applies actual signed hops, W projections and
both reverse hops in Z*Z. It therefore computes the complete H4 image, not
just the expectation obtained from a Z norm.

The new control builds g_n and its selected output v_n symbolically in n.
It computes H4 v_n, removes n times the circulation from every field word,
and obtains exact dictionary equality with a separately rebuilt n=0 image.
Gauss holds on every resulting word. The own complete image was calculated
and saved before loading the author certificate for comparison.

The selected output has norm squared 2. Its H4 image has precisely these
coefficients and multiplicities:

| coefficient | -20 | -12 | -8 | -6 | -4 | -2 |
|---|---:|---:|---:|---:|---:|---:|
| number of words | 2 | 1 | 4 | 4 | 8 | 28 |

All 47 words and coefficients agree with the author certificate, whose hash
is `e2266dbcb0de8faddfcd265a6e7c3c995bb66cc9d9ce17f84826f360af676b39`.
The squared image norm is

    2*20^2+12^2+4*8^2+4*6^2+8*4^2+28*2^2=1584.

Thus the normalized second H4 moment is 792, its mean is -20, and

    Var(H4)=792-400=392.

This directly checks the part that was not completed in the PRE. It also
reconstructs the input's thirteen-word image: coefficient -84 on the input
and twelve other coefficients -2. Hence its H4 second moment is 7104 and
its H4 variance is 48; the input is not an H4 eigenstate.

For the covariance, write P_v for the projection onto the two words in v_n.
Both have coefficient one in v_n and coefficient -20 in H4 v_n. Therefore

    P_v H4 v_n=-20 v_n.

For a diagonal observable Q, Qv_n stays in this two-word span. On the normalized
output, `Re <Qv_n,H4v_n>/2=-20<Q>`, while `<H4>=-20`.
The symmetrized covariance is exactly zero. In particular D has this property,
so

    Var(KD+delta H4)=K^2 n^4+392delta^2.

This does not diagonalize H4: its other 45 image words supply the nonzero
variance. A deliberate mutation retaining only the two support words gives
H4 variance zero and is rejected by the independently computed full moment.

Translation by an integer divergence-free circulation is a unitary on the
physical rotor space. Since legal rotor path amplitudes depend on charges
and vacancies and are unaffected by the starting integer fields, each hop,
its reverse, W projection, birth, and hence B and H4 commutes with that
translation. This proves the all-integer extension of the image and pure-H4
moments. D does not commute with it; its explicit polynomial values, together
with the support argument, establish its covariance rather than an assumed
translation symmetry of the full h.

The variance identity is scoped to the specified resolved mark. It must not
be assigned to the coherent edge output: the independently reconstructed
coherent symmetrized D/H4 covariance is `-3n/2`, matching the author's stored
full-operator results. The author note correctly restricts its displayed
exact variance to the resolved mark; this is a coverage boundary, not a defect.

## Exact spin and saved-output comparisons

`comparison_exact_claims.py` uses both frozen own PRE engines. It checks all
252 saved rotor moment entries across the input, resolved selected output and
coherent selected output at the seven author n values. It also checks the
saved all-mark rows and every Z cross term. This includes the auxiliary full
sum-E^2 diagnostics in the scripts, without treating sum E^2 as the post-birth
Hamiltonian's D.

For spin, it compares all 48 paths symbolically, so agreement is not inferred
from sampled spins. In particular it independently reproduces

    R_S=48-32n^2/C+8n^4/C^2,
    P_S=96n^2-(32n^4+16n^2)/C,
    P_S-4n^2R_S=-16n^2(6-6n^2/C+2n^4/C^2+1/C).

The last expression is exactly the author's alternate factored formula.
The -16n^2/C correction has not been dropped. The additional direct operator
checks at `(S,n)=(1,-1),(1,0),(1,1),(2,-2),(2,2)` cover both instruments
with actual boundary exclusion, for ten cases. They also agree with the
PRE's stronger finite-spin H4 drift expression. These computations complete
the present comparison; they do not assert a uniformly valid microscopic
energy approximation on this moving family.

## Supported scope and excluded conclusions

Supported scope is the supplied compensated finite cube with the specified
hard-core Gauss sector, canonical fourth-order coefficient and actual formation
instruments. The rotor identities hold for each integer circulation n on the
normalizable basis input. The full selected variance is for the resolved
(01,+ at0) output; coherent moments and initial all-mark balances are separately
specified. The spin identities use exact normalized shifts, respect blocked
marks, and yield the stated interior moving-input asymptotics.

These are immediate jump outputs from the prescribed input and generator-form
balances at that input. Hamiltonian evolution before a later first event can
change its conditional field state; the formulas do not give an unchanged
output distribution at every later event time. The all-A-plus rotor initial
loss is scalar, but this does not identify later instruments or histories.

Neither this comparison nor the source packets establish a native derivation
or physical selection of the compensation, all-time heating, a growing-volume
or continuum limit, an empirical particle prediction, reservoir autonomy,
energy conservation with an environment, a thermal law, or heat statistics.
A finite D measure does not make the output a two-point spectral measure of h.
The nonzero input H4 variance also matters for any proposed two-energy-measurement
protocol, which is not the untouched input/event procedure analyzed here.

The PRE's microscopic observation remains relevant and is consistent with the
source's stated exclusions. For the undressed bare P input g_n, at the supplied
finite S,epsilon scaling `epsilon^2 S(S+1)=delta/K`,

    <H_epsilon,S>_(bare input)=12 K S(S+1),
    microscopic dissipative energy derivative at t=0=0,

because `<C_S>=12`, W has value zero, the expectation of T vanishes, and every
microscopic j annihilates this bare input. These statements concern that
initialization, not a dressed low-cluster state. The effective target's finite
rate and energy balance are separated by the initialization layer, and the
microscopic energy grows with the resource. Trace-norm density approximation
does not itself bound these physical energy moments or transfer derivatives
at zero. A microscopic moment-transfer theorem remains an explicit open
obligation if physical microscopic energy is to be identified with h.

## Disposition, failures and recovery

No scoped scientific discrepancy remains from this comparison. The newly
requested second H4 moment and covariance are reconstructed and matched, not
merely quoted from stored output. No source corrections are requested by this
bounded comparison. This is not an audit or landing verdict.

There were no failed executions or failed mathematical comparisons in the
post-PRE work. The deliberately incorrect diagonal-H4 mutation is a successful
sensitivity test and is recorded as such. The PRE's earlier file-not-found
execution failure remains preserved in its unchanged sealed history.

The complete new scripts, outputs, source snapshots, exact comparison results
and execution receipts are bound by `FINAL_SEAL.json`; `FINAL_SEAL.sha256`
records its hash. `COMPARISON_RECEIPT.json` binds all author reproductions.
`COMPARISON_OWN_H4_MOMENTS.json` holds the own complete image and symbolic
moments; `COMPARISON_H4_CERTIFICATE_RESULT.json` records the exhaustive image
comparison. `COMPARISON_EXACT_CLAIMS_RESULTS.json` holds the remaining exact
comparison checks and boundary cases. Full logs are retained beside them.
The next authorized action belongs to the coordinator; no further frontier
calculation, external action, source edit, git mutation, landing or audit was
performed here.
