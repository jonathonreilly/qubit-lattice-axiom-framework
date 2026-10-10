# Independent research review of the spatial quantum construction

**Conclusion:** no consequential mathematical defect was found in the frozen
draft and discriminator listed below. The construction and finite-step bound
are supported under their explicitly supplied finite-register, marked-channel,
fresh-ancilla, clock and scheduling premises. This is a focused research review,
not a formal audit verdict, retained-status promotion, or native-M2 result.

No author or repository source was edited. No network, commit, PR, or model
change was used. The review preserves the selected model and reasoning effort.

## Frozen sources and coverage

Base directory:
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`.

| Source read completely | SHA-256 |
|---|---|
| `spatial_continuation/QUANTUM_SPATIAL_DRAFT.md` | `f2619055e7bc2d03d08d8d097e45cbf40cb93b3d686fb52ff0856e7d5a18f42e` |
| `spatial_continuation/quantum_spatial_discriminator.py` | `b20e556c6e6d7f94f6ac41041ac8512f194caa345b8d460a952eb9fbca07a070` |
| `worktree/docs/LOCAL_QUANTUM_COLLISIONS_AND_RAPID_MIXING_BOUNDED_THEOREM_NOTE_2026-10-09.md` | `b607e16371688f2d8d71268bd13d642f2ed8ed4f5e02332cd1eb3147b8d40c2a` |
| `worktree/docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md` | `888ede1aba130d9bf4df5ffecfbadf9c4e45dd94a49ca3a350894a052e0677c0` |

The two author files were rehashed after the review computations; their bytes
still match the assigned frozen source. The prior collision source had also
been read completely during this reviewer's particle assignment; its matching
identity was checked before reuse. The new quantum argument does not require
the older rapid-mixing or mass-action persistence theorems.

The applicable science workflow and focused claim-review guidance were read
from the local source snapshots, including current local `origin/main`
`d9b869b97944676aaa759915462c529dc276a04c`. Network freshness was not checked,
as required by this assignment. This review covers the complete quantum draft,
including its normalization, closure, finite-time constants, supplied locality,
resource statements and author evidence; it does not cover a subsequently
integrated note, a new particle/amplitude/fluid composition, or changed bytes.

## Independent derivation of the load-bearing claims

### Pair normalization and exact occupation lumpability

For one cell and distinct species `i,j`, write `P_ai` for the diagonal
projector that labelled particle `a` is at that cell with velocity `i`.
The operator identity on the labelled computational basis is

\[
 \sum_{a<b}(P_{ai}P_{bj}+P_{aj}P_{bi})=n_i n_j.
\]

This counts each eligible unordered label pair once. For any one existing
input orientation, exactly two separately marked operators in draft (4)
lead to the two ordered target arrangements. Therefore the outgoing rate
is `2 gamma_r n_i n_j`. With
`gamma_r=c kappa_r/(2 N w)`, this is exactly
`c kappa_r n_i n_j/(Nw)`, including empty inputs and arbitrary repeated
occupancy of the distinct species. There is no second factor from input
orientation. The reverse calculation is identical. Thus the factor in
draft line 140 is correct.

Each hop has `n_xv` eligible labels, giving the stated one-particle rate.
These target occupation rates depend only on the current counts, not the
arrangement of labels. The lift intertwining `Q L=L G` follows on every
count observable. Finite-dimensional exponentiation proves exact generator
semigroup lumpability for every labelled population law. No averaging over
fibers, propagation of chaos or rapid mixing has entered this derivation.

Dividing a collision count jump by `Omega=Nw` gives density drift
`(1/Omega)(c kappa_r/Omega)n_i n_j=c kappa_r F_i F_j`.
The use of normalized cell weight `w`, rather than physical volume `ell^3`,
is consistent throughout. At `N=1` there are no eligible label pairs.

### Arbitrary-coherence population closure

For any of the specified marks, `J` maps each basis vector in its domain to
one distinct basis vector, with no two sources having the same target.
Consequently `J^dagger D_f J` and `J^dagger J` are diagonal whenever `D_f`
is diagonal. This proves draft (7) directly for all computational basis
entries. It proves closure for arbitrary density matrices, not merely
diagonal initial states.

Tensoring with an untouched reference introduces no exception: apply the
same identity to `D_f tensor R` for every reference matrix `R`. The diagonal
system blocks, now reference-operator-valued, still satisfy the same classical
transition rules. The result does not assert full dephasing of the state.

Separating marks is substantive. A common-target sum
`J=|t><s1|+|t><s2|` has noninjective source map and target gain from `E_s1,s2`.
The draft's counterexample to that particular replacement is valid.

### Fresh-ancilla channel

Let `A=J tensor |1><0| - J^dagger tensor |0><1|`, so that
`-i H_j=sqrt(q) A`. Because `J` is a partial isometry, on the initial ancilla
subspace its even powers alternate between the source projection
`P=J^dagger J` and its negative, while its odd powers map through `J`.
Summing the exponential gives

\[
 \langle0|W_{j,h}|0\rangle=I-P+\cos(\sqrt{hq})P,
 \qquad
 \langle1|W_{j,h}|0\rangle=\sin(\sqrt{hq})J.
\]

Thus the exact Kraus formula, its completeness, and the lack of a reverse
hop from an ancilla prepared in `|0>` all check. The Hermitian conjugate
Hamiltonian term acts from the excited ancillary sector; its presence does
not make the reduced hop symmetric. This is conditional on fresh preparation.

The specified system endpoints have identical momentum and kinetic energy,
so both `J` and `J^dagger` commute with those global diagonal observables.
The enlarged Hamiltonian therefore conserves their full spectral laws when
the ancillary free energy is zero. The draft correctly keeps preparation,
switching, erasure and apparatus costs outside that mathematical statement.

### All diamond-error constants

The argument is dimension independent at the operator-norm step: even though
each mark has spectator identities and the global Hilbert space is large,
`||J||=||P||=1`. Completely bounded trace norms of left/right multiplication
are bounded by the corresponding operator norms.

For `x=hq<=1/4`, set `u=cos(sqrt(x))-1` and `p=sin^2(sqrt(x))`. Alternating
Taylor remainders and `(t-sin(t))(t+sin(t))<=t^4/3` on `0<=t<=1/2` give

\[
 |u+x/2|\le x^2/24,\quad u^2\le x^2/4,
 \quad |p-x|\le x^2/3.
\]

The exact channel expansion has coefficients of `{P,rho}`, `P rho P`, and
`J rho J^dagger` with superoperator norm bounds `2,1,1`. Hence its remainder
from `I+h B_j` is bounded by
`(2/24+1/4+1/3)x^2=(2/3)x^2`. Since
`B_j=q_j D[J_j]` has diamond norm at most `2q_j` and its semigroup is CPTP,
the integral exponential remainder costs at most
`h^2 ||B_j||^2/2<=2h^2q_j^2`. The local channel-to-semigroup cost is therefore
`(8/3)h^2q_j^2`, with exactly the stated constant.

For successive partial sums `A` and the next generator `B`, differentiation
of `e^{(h-s)(A+B)}e^{sA}e^{sB}` gives

\[
 e^{(h-s)(A+B)}
 \int_0^s e^{(s-u)A}[A,B]e^{uA}\,du\ e^{sB}.
\]

All factors are CPTP semigroup contractions. Integration over the triangle
`0<=u<=s<=h` gives `h^2||[A,B]||/2`. Bounding each pair commutator by
`2||B_i||||B_j||<=8q_iq_j` gives the total splitting cost
`4h^2 sum_{i<j}q_iq_j`. This uses the actual sum/product generators and does
not assume commuting gates. The full one-step bound is

\[
 h^2\left[\frac83\sum_jq_j^2+4\sum_{i<j}q_iq_j\right]
 \le\frac83h^2\Lambda^2.
\]

The rate sum also checks independently:

\[
 \Lambda_{\rm hop}=54NM\frac b\ell=\frac{54Nb}{w\ell},
 \qquad
 \Lambda_{\rm collision}
 =4\binom N2M\frac{cK}{2Nw}
 =\frac{(N-1)cK}{w^2}.
\]

Here `M=m^3=1/w` is the number of cells, as in the quantum draft.
`h Lambda<=1/4` implies every local `h q_j<=1/4`. Telescoping
`k=floor(T/h)` contractive steps costs at most `(8/3)Th Lambda^2`.
For `r=T-kh<h`, integrating the generator over the remaining time gives
`r||mathcal L||<=2h Lambda`. Thus draft (10), including its time-floor term,
holds for every `T>=0`. The observable bound has the stated factor
`||f||_infinity`; occupation measurement gives the stated total-variation
bound with an additional factor one-half. No unexplained factor of two or
hidden Hilbert-space dimension factor was found.

### Finite ordered schedule versus generator

The schedule is not silently treated as an exact occupation chain. Recomputing
the four collision gates with formal jump-probability variable `p` gives
product-occupation probabilities

\[
 s_1:\ 2p-3p^2+2p^3,\qquad
 s_2:\ 2p-p^2.
\]

Their difference is `-2p^2(1-p)` despite equal initial occupations; their
first-order coefficients both equal 2. This reproduces the draft's exact
counterexample and supports its careful distinction at lines 320–327.
The finite schedule still has a classical labelled population channel, and
the diamond comparison bounds its final occupation law without asserting
that the occupation sequence alone is Markov.

## Executed evidence and its limits

The author discriminator was reproduced successfully with bytecode disabled.
Its complete output is `quantum_review_author_reproduction.log`. The printed
4096 configurations, 330 fibers, 15920 outgoing targets and exact rate
`1485/91` match the declared census. All four author mutations were rerun;
each exited 1 for its intended discrepancy. Their complete outputs are
`quantum_review_mutant_gamma.log`, `quantum_review_mutant_drop_output.log`,
`quantum_review_mutant_symmetric_hop.log`, and
`quantum_review_mutant_merged_mark.log`. These were inspected beyond exit codes.

The separately written `quantum_review_independent_check.py` imports none of
the author code or repository runner. Its complete output is
`quantum_review_independent_check.log`. It:

- Constructs a `10x10` joint dilation by a polynomial of its skew generator,
  using a proper partial injection with overlapping source/target subspaces;
  checks unitarity, derived Kraus operators, and all 25 matrix-unit population
  images exactly at `cos=12/13`, `sin=5/13`.
- Checks the pair-projector count identity and density normalization on 15,552
  cell configurations for `N=5`, including 5100 active collision cases, with
  rational `gamma=2457/1870`. Doubled/halved coefficients fail on active cases.
- Derives the finite-schedule probability polynomials without importing the
  author's rational outputs.
- Tests the need for time-floor control by a one-channel directed jump with
  `h=1/16`, `T=1/32`. No macrostep is executed; its true trace-distance error
  is at least `2T-T^2=63/1024`, larger than the first term alone `1/192`.
  The complete declared bound is `25/192` and is consistent. The lower bound
  uses `exp(-T)<=1-T+T^2/2`, so it is exact rational evidence.

Review helper SHA-256:
`5e7577030c34ff01306537d3f377e84b76508a9eb1f6c2f44137c680a8f7b60c`.
Review helper log SHA-256:
`f91971e42da197c6878cbf922c3d1491505cf473c6a7fa02d63960f8d6400a95`.

The independent checks were designed after reading the source claims; they
are independent derivations/implementations, not a blinded experiment or a
different-model guarantee. This reviewer previously authored the separate
particle draft, but did not author the quantum unit. The rational finite
checks do not certify the all-size or diamond-norm theorem by enumeration;
those conclusions rest on the separately reconstructed argument above.

## Scope and formal-verification disposition

The only supported locality is the supplied particle-register and spatial-label
locality. The draft explicitly does not identify these tensor factors with
native spatial qubits and does not hide the all-label-pair addressability,
fresh ancillary supply, singular coupling schedule, directional instrument,
clock or rate selection. Its finite gate-resource formula and the possibility
of choosing `h` after all other scales are consistent with its error bound.
No resource bound uniform in `N,m,delta` or physical cost accounting follows.

No unresolved mathematical obligation requiring Lean before conditional
milestone reuse was identified. No Lean checker was run, and this review is
not formal verification. Useful later audit/formalization targets are the
partial-permutation diagonal-algebra identity, labelled-count intertwining,
partial-isometry dilation formula, and completely bounded Duhamel/telescoping
estimate with the precise norm convention. A Lean theorem about those objects
would still not discharge the native-carrier or physical-instrument interface.

Recommended research disposition: use this exact frozen quantum unit as
reviewed conditional support, keeping its stated premises and finite-schedule
error intact. Reopen review for changed source or a stronger downstream claim.

## Final repository packaging confirmation

The same reviewer subsequently read the **complete** packaged note and runner,
the complete diff from the frozen author sources, and the final claim-scope
correction. This is final-source coverage of the following files in `worktree`
at checkout HEAD `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192`, before the
supervisor's commit:

| Final reviewed file | SHA-256 |
|---|---|
| `docs/SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md` | `f02fe7fae147bf5aedac035334ab8a34ac89deb3220c9381918e58e30711fff2` |
| `scripts/spatial_quantum_collision_realization_2026_10_09.py` | `e4b969804fe943ed69279446ed96ffc5ad87bcb8359f1150c41d34155feb8543` |

All 22 displayed equation blocks are byte-identical to the reviewed author
draft. Sections 1–5 are byte-identical after the single wording replacement
`The proposed occupation generator is` -> `The occupation generator is`.
The new front matter, introduction, proof-obligation table, evidence references,
review-scope paragraph and conditional-status block were read in full. They
do not change the hypotheses or promote the supplied construction to a native
framework realization or retained audit result.

An initial packaging wording ambiguity was raised: `channels have exact
occupation rates` could conflate the generator with the finite ordered gate
schedule. The supervisor changed the front-matter claim scope to identify
**the summed Lindblad generator of separately marked jumps** as the object
with exact occupation rates and arbitrary-coherence population closure. The
corrected line was read and is included in the final hash above. This resolves
the scope ambiguity; no mathematical repair to the body was required.

The runner diff consists only of the new source-name docstring,
`AUDIT_TIMEOUT_SEC=180`, and `AUDIT_INPUT_PATHS` naming the final note and its
supplied collision-contract dependency. Both paths exist. A deterministic AST
comparison confirms that, after removing those metadata items, all executable
runner content is identical to the already reproduced source. The complete
runner was also read. The earlier successful reproduction and mutation checks
therefore retain their coverage; an identical rerun was not used as additional
scientific evidence. The deterministic comparison receipt is
`quantum_review_packaging.log`.

Final source conclusion: the earlier no-material-defect finding and independent
derivations cover these precise packaged note/runner bytes. Generator lumping,
finite ordered-schedule approximation, normalization, diamond constants and
physical scope remain as reviewed. There is no new Lean prerequisite and no
formal audit verdict.

Packaging verification limit: at this source check the newly named repository
cache `logs/runner-cache/spatial_quantum_collision_realization_2026_10_09.txt`
and `SPATIAL_RUNNER_MUTATIONS.txt` were not yet present in the checkout; this
review report was present in the sibling `spatial_continuation` directory.
The supervisor was informed to include or locate those evidence artifacts in
the remaining packaging work. This confirmation does not attest a cache
envelope or artifact publication that had not yet occurred. The raw reproduction
and mutation logs actually inspected by this reviewer are listed above.


<!-- Packaging: relative repository links rebased; historical draft links rendered as provenance text. Mathematical/review assertions unchanged. Original raw report SHA-256: e2232489bbd0aff537a4400a34eb848cae2295d18dda7af0cd762ab0ff4c2ba1. -->
