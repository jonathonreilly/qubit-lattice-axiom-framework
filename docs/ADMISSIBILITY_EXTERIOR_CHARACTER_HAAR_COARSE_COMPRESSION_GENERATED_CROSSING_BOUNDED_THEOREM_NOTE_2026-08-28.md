---
claim_id: admissibility_exterior_character_haar_coarse_compression_generated_crossing_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "On a supplied finite O(3) three-path/two-plaquette gauge cell, compute the exact gauge-projected Haar compression J* T_f J of the actual normalized exterior-character transfer with both spatial half-actions. Prove that eliminating one plaquette produces the normalized positive crossing p proportional to a(m*a*m), derive its all-character fusion coefficients, strict support and injectivity, give exact log-density and convolution-operator comparisons, and exhibit the first determinant/vector generated term. This is a one-cell and finite shared-edge-family mathematical compression theorem, not an iterable renormalization flow, bare intertwining, locality or continuum theorem, physical clock, Hamiltonian identification, selected action, Lorentz result, or gravity result."
depends_on:
  - admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
  - minimal_axioms
runner: scripts/admissibility_exterior_character_haar_coarse_compression_generated_crossing_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_haar_coarse_compression_generated_crossing_independent_2026_08_28.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "For genuine spatial refinement, control the renormalized compression J* T_f J or construct a perfect/nonlocal action with an exact comparison; the fixed-carrier temporal product and the bare cylindrical obstruction do not supply a spacetime continuum or physical clock."
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Construct an associative iterated Haar-compression flow on an indexed graph family, with a disclosed generated-character basis and a uniform locality or truncation estimate; the present exact finite shared-edge family does not supply a spatial continuum or physical clock."
conditional_surface_status: "exact finite-cell projected Haar-compression and generated-crossing theorem, conditional on the supplied exterior-character co-scaled temporal family; no iterable renormalization, locality, continuum, or physical-time theorem"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "normalized Haar disintegration, an exact full-transfer kernel identity, Peter-Weyl fusion arithmetic, strict multiplier support, and explicit comparison bounds prove the stated bounded theorem without fitted data"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exterior-character Haar coarse compression and generated crossing

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `conditional-support` — an exact bounded theorem on the supplied
finite cell and unmerged parent family, not an audit verdict.

## Result up front

The canonical Haar compression left open by the parent note can be computed
exactly on the disclosed three-path cell that both retains and eliminates a plaquette.
The compression exists as a positive projected transfer, but it does not
return the inherited bare crossing.  It generates a new central crossing
whose coefficients are an exact character-fusion contraction.

Let `G=O(3)`.  The fine cell has three oriented two-edge paths from `s` to
`t`, with path holonomies

```text
A=a_2 a_1,       B=b_2 b_1,       C=c_2 c_1,       (1)
```

and two spatial plaquette words

```text
W_1=B A^-1,       W_2=C B^-1.                       (2)
```

The coarse cell retains `A,B` and `W_1`; it deletes the `C` path and `W_2`.
Put

```text
H_f=L^2(G^6,dg^6),       H_c=L^2(G^2,dA dB),
pi(a_1,a_2,b_1,b_2,c_1,c_2)=(A,B),
(J psi)(fine)=psi(pi(fine)).                         (3)
```

Normalized Haar convolution makes `pi_* dg^6=dA dB`, so `J` is an
isometry.  Fine gauge frames at the three internal path vertices cancel in
the ordered products (1).  The endpoint frames act simultaneously by
`(A,B,C)->(q_t A q_s^-1,q_t B q_s^-1,q_t C q_s^-1)`.  Therefore

```text
P_f J=J P_c,             J* P_f=P_c J*.              (4)
```

This includes both connected components of `O(3)`: the determinant of every
coarse path is the ordered product of its two fine determinants, and the
conditional Haar fiber sums all compatible component assignments.  No
`SO(3)` restriction or determinant-sector selection is used.

The retained two-path theta cell has the nontrivial loop `W_1`; after endpoint
gauge projection its class characters survive.  On a gauge tree the same
external projection can collapse all such loop modes, so the topology in
(1)--(2) is load-bearing and is not extrapolated to trees.

## Actual exterior transfer and exact compression

Fix one finite exterior member `n>=1`, a strict temporal coefficient
`kappa>0`, and a strict spatial coefficient `beta>0`.  With the notation of
the linked [co-scaled exterior theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md), let

```text
v(g)=f_n(Q(g)),              0<=v<=16/n,
w(g)=exp[-kappa v(g)] / integral exp[-kappa v] dg,
a=w*w,                       m(g)=exp[-beta v(g)/2].  (5)
```

All functions in (5) are real, central, inversion invariant, and strictly
positive.  The normalized temporal extension applies `w` independently on
all six fine links.  The spatial half multiplier and complete projected fine
transfer are

```text
M_f=m(W_1)m(W_2),
T_f=M_f P_f C_w^(tensor 6) P_f M_f.                  (6)
```

This is a pure-gauge finite specialization of the supplied exterior action.
No vector matter, source, or coframe response is silently retained.

After the two links of each path are Haar-composed, the path crossing density
is `a`.  Put

```text
Delta_A=A' A^-1,       Delta_B=B' B^-1,
X=C B^-1,              X'=C' B'^-1.                 (7)
```

The exact conditional integral over the deleted path is

```text
H(delta)
 = integral dX dX' m(X') a(X' delta X^-1) m(X)
 = (m*a*m)(delta).                                  (8)
```

Both endpoint half-actions in (8) are load-bearing.  The coarse kernel is

```text
K_eff((A',B'),(A,B))
 =m(W_1')m(W_1) a(Delta_A)a(Delta_B)H(Delta_B).      (9)
```

Define

```text
Z=integral a(delta)H(delta) ddelta,
p(delta)=a(delta)H(delta)/Z,
M_c=m(W_1).                                         (10)
```

Equations (4), (8), and (9) prove the projected operator identity

```text
J* T_f J = Z M_c [C_a tensor C_p] M_c
           on P_c H_c.                              (11)
```

Thus this is the actual canonical compression `J* T_f J`, not the bare
intertwining equation `T_f J=J T_c`.  Isometric compression preserves
self-adjointness and positive-operator order.  Since `T_f` is injective on
`P_f H_f`, for nonzero `psi in P_c H_c`,

```text
<psi,J*T_fJ psi>=<J psi,T_f J psi> > 0.             (12)
```

The compressed transfer is therefore injective on the projected coarse
space.  This does not assert reflection positivity for an arbitrary new
cylinder algebra; only the Hilbert transfer compression in (11) is claimed.

## Exact all-character fusion law

For an irreducible real `O(3)` representation `rho`, let `d_rho` be its
dimension and use normalized Peter--Weyl scalars

```text
a_rho=(1/d_rho) integral a chi_rho,    a_triv=1,
mu_rho=(1/d_rho) integral m chi_rho.                   (13)
```

Strict exterior support gives `a_rho>0` for every `rho`.  Convolution in (8)
gives

```text
H(g)=sum_lambda d_lambda a_lambda mu_lambda^2 chi_lambda(g).   (14)
```

Let `N_(rho lambda)^sigma` be the nonnegative tensor-product multiplicity.
Pointwise multiplication by `a` in (10), not another convolution, yields

```text
kappa_sigma
 =(1/d_sigma) sum_(rho,lambda)
    d_rho d_lambda N_(rho lambda)^sigma
    a_rho a_lambda mu_lambda^2,
Z=kappa_triv=sum_rho d_rho^2 a_rho^2 mu_rho^2,
p_sigma=kappa_sigma/Z.                              (15)
```

Writing the `O(3)` irreducibles as `(ell,p)` with dimension `2ell+1` and
inversion parity `p`, the multiplicity in (15) is explicitly

```text
N_((ell,p),(j,q))^((k,r))
 =1  iff  |ell-j|<=k<=ell+j and r=pq,
 =0  otherwise.                                    (15a)
```

Every term in (15) is nonnegative.  The `lambda=triv,rho=sigma` term is
strict because `a_sigma>0` and `mu_triv>0`; hence

```text
p_sigma>0       for every sigma.                    (16)
```

So `p` has full Fourier support and its convolution is injective.  Pointwise
positivity also follows directly from (8)--(10).  These are distinct facts:
a positive density alone would not prove (16).

The generated crossing is not the inherited crossing anywhere in the stated
strict domain.  For every finite `n` and `beta>0`, `v` and hence `m` are
nonconstant.  If `p=a`, strict pointwise positivity of `a` in (10) would make
`H=Z` constant.  Equation (14) would then give
`a_lambda mu_lambda^2=0` for every nontrivial `lambda`.  Since every
`a_lambda>0`, all nontrivial `mu_lambda` would vanish; Peter--Weyl completeness
would make `m` constant, a contradiction.  Therefore

```text
p != a       for every finite n and strict beta,kappa.            (16a)
```

This proves nonidentity with the inherited crossing at the same coefficients;
it does not exclude equality with an isolated differently coupled or enlarged
family member.

An independent nonabelian `S_3` arithmetic control checks every dimension
factor in (14)--(15).  For

```text
a_hat=(1,1/2,1/3) on (triv,sign,std),
m(e,t,c)=(1,1/2,1/3),
```

the direct group sum gives

```text
mu=(19/36,1/36,1/9),
H_hat=(361/1296,1/2592,1/243)=a_hat mu^2.           (17)
```

Direct pointwise multiplication agrees with the fusion contraction (15).
No finite group replaces `O(3)` in the proof; (17) is an exact independent
normalization control.

## Quantitative coarse-action comparison

The compact action range in (5) gives

```text
exp[-8 beta/n] <= m <= 1,
exp[-16 beta/n] <= H <= 1.                          (18)
```

More generally, attach `N>=1` independently eliminated two-edge paths to the
same retained path `B`, each with one eliminated plaquette half multiplier.
The identical Haar disintegration gives

```text
H_N=H^N,          p_N=a H^N/Z_N.                    (19)
```

Therefore, pointwise,

```text
exp[-16N beta/n] <= p_N/a <= exp[16N beta/n],
||(-log p_N)-(-log a)||_infinity <= 16N beta/n.      (20)
```

The normalization constant is included in (20).  Since convolution operator
norm is bounded by the `L^1` norm of its density,

```text
||C_pN-C_a||
 <= ||p_N-a||_1
 <= min{2, exp(16N beta/n)-1}.                      (21)
```

For the load-bearing one-cell pair there is a sharper quadratic estimate.
Put `ell=exp(-8 beta/n)`.  For each `delta`, the two variables in (8) have
normalized Haar marginals.  Cauchy--Schwarz and the bounded-variable variance
estimate give

```text
|H(delta)-(integral m)^2| <= Var_Haar(m),
Var_Haar(m) <= (1-ell)^2/4.
```

The same bound averaged against `a` applies to `Z`.  Since `Z>=ell^2`,

```text
||C_p-C_a|| <= ||p-a||_1
 <= (1/2)[exp(8 beta/n)-1]^2.                       (21a)
```

Let

```text
T_bare,N=M_c(C_a tensor C_a)M_c.
```

Because `M_c` and `C_a` are contractions, the full normalized-compression
comparison follows immediately:

```text
||Z_N^-1 J_N* T_f,N J_N-T_bare,N||
 <= ||C_pN-C_a||.                                  (21b)
```

Equations (19)--(21) are an exact finite shared-edge family and a named norm
comparison.  They are not an iterable graph-refinement flow: `N` counts
independent eliminated plaquettes in one disclosed cell geometry, and the
bound grows with `N`.

## Exact generated determinant/vector term

The linear member supplies a transparent continuous-group witness.  Write
`chi_triv` for the trivial character; then

```text
Q=14 chi_triv-2 chi_det-2 chi_V-2 chi_(det V).       (22)
```

For small spatial `beta`, the normalized Fourier coefficients of
`m=exp(-beta Q/2)` obey

```text
mu_triv=1-7 beta+O(beta^2),
mu_det=beta+O(beta^2),
mu_V=mu_(det V)=beta/3+O(beta^2).                   (23)
```

Consequently

```text
p(delta)
 =a(delta){1+beta^2[C_kappa(delta)-c_kappa]+O(beta^3)},
C_kappa
 =a_det chi_det +(a_V/3)(chi_V+chi_(det V)),
c_kappa=a_det^2+2a_V^2.                             (24)
```

The remainder is uniform on compact `O(3)` for fixed strict `kappa`.
For the actual exterior crossing,

```text
r_det=2 kappa+O(kappa^2),
r_V=r_(det V)=2 kappa/3+O(kappa^2),
a_rho=r_rho^2.                                     (25)
```

Modulo the scalar normalization in (24), (25) gives

```text
-log p+log a
 =-4 beta^2 kappa^2
   [chi_det+(chi_V+chi_(det V))/27]
   +O(beta^2 kappa^3+beta^3 kappa^2).              (26)
```

For an improper `delta=zR`, `chi_det=-1` and the vector pair cancels.  For a
proper `R`, the bracket is

```text
1+2 chi_V(R)/27.                                   (27)
```

Thus the compression generates both a determinant response and a resolved
proper-component vector-character response.  It is not equal to the inherited
bare crossing `a` at the inherited coefficients.  More sharply, it is not a
scalar coupling shift near `kappa=0`.  The uncompressed path family has

```text
-log a_kappa
 =-4 kappa^2 chi_det
  -(4/3)kappa^2(chi_V+chi_(det V))+O(kappa^3).       (27a)
```

Matching the induced determinant term in (26) with
`kappa'=kappa(1+beta^2/2+...)` would predict a vector-pair shift
`-(4/3)beta^2 kappa^2`, whereas (26) gives
`-(4/27)beta^2 kappa^2`.  The mismatch is a factor of nine.  This local
statement does not rule out an isolated finite-coupling coincidence or an
enlarged/perfect action family.

The exact `Z_2` quotient is a second hostile control.  With

```text
a(s)=1+s/2,       m(+)=1,       m(-)=1/2,
```

direct four-variable normalized Haar enumeration yields

```text
a(+)H(+)=57/64,     a(-)H(-)=17/64,
Z=37/64,            p_det=20/37.                   (28)
```

Dropping either spatial half-action changes (28); replacing the pointwise
product `aH` by convolution also changes the fusion law.  The quotient is a
diagnostic, not authority for the full `O(3)` theorem.

## Imports and physical boundaries

| Input | Role | Status |
|---|---|---|
| finite three-path/two-plaquette cell, orientations, and coarse map `pi` | carrier and incidence | supplied mathematical geometry |
| normalized product Haar measures on all `O(3)` links | isometry and conditional disintegration | supplied measure |
| finite `n`, strict `kappa,beta`, and the actual exterior `f_n` | crossing and half-action | supplied action family |
| independent linkwise temporal extension | produces `a=w*w` | supplied temporal extension |
| simultaneous fine/coarse local Haar projectors | gauge-invariant Hilbert spaces | supplied kinematics |
| density normalization | defines `w,p` and (11); `Z` is not the full-transfer top eigenvalue | mathematical normalization |
| graph scale, lattice spacing, clock, RG basis, truncation norm, component jump | interpretation or iteration | not supplied |

The theorem is about a finite mathematical transfer.  It is not a physical
probability law, physical time, Hamiltonian, continuum, Lorentz, Einstein,
gravity, stress, or action-selection theorem.  It does not identify the
exterior connection with a measured Standard Model field.  The improper
component is retained exactly, not selected or removed.  These boundaries
follow the [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), which do not supply
the missing physical or refinement identifications.

## No-Go Discipline Gate

The negative content is only that the inherited bare crossing does not equal
the computed compression and that one exact cell is not already an RG tower.
It is not a no-go for enlarged perfect actions, quasilocal flows, alternative
blocking maps, or physical continuum models.

### N1 -- failed attack routes

| Route | Exact attempt | Why it fails | Marker |
|---|---|---|---|
| infer compression from bare intertwining | use `T_fJ=JT_c` | the parent proves bare defects; (11) instead uses conditional Haar integration | `ATTEMPTED` |
| delete the hidden path without its environment | replace `H` by one | both endpoint half-actions produce (8) and (28) | `ATTEMPTED` |
| treat the generated product as convolution | replace `aH` by `a*H` | pointwise multiplication gives fusion, not diagonal multiplication | `ATTEMPTED` |
| omit representation dimensions | use multiplicities alone in (15) | the independent `S_3` control fails | `ATTEMPTED` |
| infer strict support from positive density | skip the Fourier calculation | (16) needs the positive `lambda=triv` fusion term | `ATTEMPTED` |
| call one cell a perfect-action flow | recursively reuse (11) without typing new fibers | no associative coefficient/measure map or uniform bound is supplied | `ATTEMPTED` |
| remove the improper component | work only on `SO(3)` | (27)--(28) lose the determinant discriminator and change the carrier | `ATTEMPTED` |
| read `N` in (19) as a continuum scale | send `N` to infinity | the comparison (20) grows and no spacing or embedding is supplied | `ATTEMPTED` |

The successful route is the exact normalized disintegration (7)--(11), not a
failed attack.

### N2 -- pairwise independence of remaining interfaces

Let `A` be an associative iterated coefficient/measure flow, `B` a uniform
locality or truncation estimate, `C` changing-topology/holonomy control, `D`
physical time/continuum identification, and `E` restoration of the full
matter/source/coframe carrier.

| Pair | First closes second? | Second closes first? | Independence evidence |
|---|---:|---:|---|
| `A,B` | no | no | an exact recursion may be nonlocal; locality does not define the recursion |
| `A,C` | no | no | composition rules do not by themselves control new cycle sectors |
| `A,D` | no | no | a mathematical flow supplies no physical clock or spacing |
| `A,E` | no | no | pure-gauge recursion does not restore omitted carriers |
| `B,C` | no | no | decay bounds and holonomy bookkeeping are distinct |
| `B,D` | no | no | locality supplies no physical interpretation |
| `B,E` | no | no | a pure-gauge locality estimate does not type matter/source fibers |
| `C,D` | no | no | topology control supplies no clock |
| `C,E` | no | no | holonomy sectors and added carriers are independent inputs |
| `D,E` | no | no | physical scaling and carrier restoration require separate suppliers |

No pair collapses.  The one-cell compression itself is proved and is not
counted as a remaining interface.

### N3 -- hidden-wall scan

| Scan family | Occurrences checked | Disposition |
|---|---|---|
| chosen / by construction | cell, path order, coefficients, coarse map | all are explicit supplied mathematical choices |
| background / fixed | fixed `n,kappa,beta` and finite cell | theorem domain, not dynamical fixation |
| canonical / natural | canonical compression | means the adjoint compression for the disclosed Haar isometry only |
| registered / physical | time, Hamiltonian, probability, stress | absent and explicitly not inferred |
| assume / assumption / assumed | centrality, strict coefficients, temporal extension | stated in (5)--(6) or the import table |
| as is standard / framework provides / bridge context | whole note and runners | no unnamed bridge is consumed |
| obviously / standard QFT | whole note and runners | no rhetorical substitute for a derivation |
| imported exact values | fusion dimensions and diagnostic fractions | derived independently; no fitted values |

No hidden observational, literature, or authority-status input is
load-bearing.

### N4 -- residual matching

| Source anchor | Attacked residual | Claimed residual | Match? | Evidence |
|---|---|---|---:|---|
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md:18` | control `J* T_f J` or construct a perfect/nonlocal comparison | exact finite-cell compression and generated crossing | yes, partially | (7)--(21) |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md:256-282` | gauge-typed Haar pullback | full path pushforward and `P_fJ=JP_c` | yes | (1)--(4) |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md:579-591` | disintegration, coefficient flow, common projector, error estimate | disintegration/fusion plus finite-family norm bound; no tower | yes, partially | (8)--(21) |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:114-130` | dynamics/refinement are not axiom inputs | supplied action and map stay explicit | yes | import table |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:173-190` | physical time/action selection remain downstream | no physical or selection claim | yes | scope fences |
| this note, iterated-flow target | associative graph-family control | not claimed | no | next trace action |

The trace is a partial closure, not target substitution.

### N5 -- rhetoric and resolution audit

`T` means proved theorem, `H` a proved hard boundary, `U` unproved, and `N`
not claimed.

| Negative phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| bare crossing is not the compression | `T`: two half-actions | `T`: (8) | `T`: (15),(24) | `T`: (11) | `U`: no general graph claim |
| no original-coefficient closure | `T`: (28) | `T`: hidden path | `T`: determinant/vector term | `H`: inherited `a` differs | `U`: enlarged basis open |
| no iterable flow | `T`: one fiber | `T`: finite shared-edge family | `U`: coefficient tower absent | `N` | `N`: checked and not executed -- no indexed graph recursion |
| no locality/continuum theorem | `U` | `U` | `U` | `N` | `N`: checked and not executed -- bound (20) grows |
| no physical time/action selection | `U` | `U` | `U` | `N` | `N`: checked and not executed -- no physical supplier |

Primary execution prints exact `per_element`, `per_site`, `per_mode`,
`per_block`, and checked/not-executed `lattice_wide` certificates.

### N6 -- convention, primitive, and prior-art scan

The mandatory sweep was refreshed at
`origin/main=66e478505e055faf4a5b9e6f4883211e44304718` and separately across
the open connection stack through parent Block227.  Both noun orders,
hyphen variants, and the phrases `renormalized compression`, `J* T_f J`,
`perfect action`, `nonlocal gauge action`, `cylindrical closure`, `Haar
coarsening`, `transfer RG`, and `generated crossing` were searched.

```text
git fetch origin main --quiet
git rev-parse origin/main
git grep -n -i -E '(renormalized.{0,60}compression|compression.{0,60}renormalized|J\* T_f J|perfect.{0,40}action|nonlocal.{0,40}gauge.{0,40}action|cylindrical.{0,40}(closure|consistency)|Haar.{0,40}coarsen|coarsen.{0,40}Haar|transfer.{0,20}RG|RG.{0,20}transfer)' origin/main -- docs scripts
git grep -n -i -E '(constrained fiber|raw RG|coarse gauge|pullback identity|Schur|holonomy preservation|coarse grain)' origin/main -- docs scripts
for pr_number in 7761 7763 7764 7765 7767 7768 7774 7776; do gh pr view "$pr_number" --json number,headRefOid,state,baseRefName; done
```

The separately scanned heads were `#7761@311036fd`, `#7763@714ba06e`,
`#7764@488c07b6`, `#7765@6894cdde`, `#7767@5b9d9efe`,
`#7768@9b8ae896`, `#7774@205db872`, and parent `#7776@0d0d7282`;
all were open when refreshed and none is current-source authority.

Closest current-source rows are non-authoritative prior art:

| Row | Live status | Applicability |
|---|---|---|
| `docs/UNIVERSAL_QG_CANONICAL_REFINEMENT_NET_NOTE.md:17-27,85-99,121-129` | `positive_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/un/universal_qg_canonical_refinement_net_note.json:6,17,31,35` | geometric/Gaussian projective compatibility, no exterior transfer |
| `docs/TWO_SEAM_FOREST_GAUGE_POLYAKOV_HOLONOMY_PRESERVATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:123-169` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/tw/two_seam_forest_gauge_polyakov_holonomy_preservation_bounded_theorem_note_2026-07-12.json:6,17,31,35` | normalized `SU(3)` forest disintegration, not this edge-product compression |
| `docs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md:11-75,191-220` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/wi/wilson_staggered_constrained_fiber_dobrushin_and_raw_rg_unit_directions_bounded_theorem_note_2026-07-12.json:6,17,27,31` | exact raw hidden-Haar directions, not the compressed transfer |
| `docs/WILSON_STAGGERED_DEEP_FIBER_COARSE_GAUGE_GIBBSIANNESS_BOUNDED_THEOREM_NOTE_2026-07-12.md:11-55,171-197` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/wi/wilson_staggered_deep_fiber_coarse_gauge_gibbsianness_bounded_theorem_note_2026-07-12.json:6,17,29,33` | deep-wedge quasilocal coarse specification; no original-family closure |
| `docs/WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md:11-74,78-159` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/wi/wilson_staggered_raw_constrained_action_hessian_decay_bounded_theorem_note_2026-07-12.json:6,17,29,33` | conditional-action Hessian decay, not normalized `J*T_fJ` |
| `docs/WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md:11-69,137-170,397-429` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/wi/wilson_staggered_two_horizon_skeleton_pullback_canonical_rehoeffding_intertwining_bounded_theorem_note_2026-07-12.json:6,17,30,34` | coefficient-grammar pullback, not actual `O(3)` transfer compression |
| `docs/PLAQUETTE_SOURCE_SECTOR_PULLBACK_IDENTITY_NARROW_THEOREM_NOTE_2026-06-12.md:25-49,78-132,177-208` | `no_go`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/pl/plaquette_source_sector_pullback_identity_narrow_theorem_note_2026-06-12.json:6,17,38,42` | warns that isometry alone does not imply transfer-invariant range |
| `docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md:42-59,94-132,228-328` | `positive_theorem`, current audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/ga/gauge_vacuum_plaquette_transfer_operator_character_recurrence_note.json:6,17,27,31` | finite `SU(N)` character recurrence/intertwiner, not full-Hilbert compression |

The branch-only historic factor-two Wilson--staggered note at commit
`9302f84` is not current or in-flight authority.  Its current wrapper,
`docs/historic_intake/HISTORIC_MASSIVE_WILSON_STAGGERED_SPATIAL_DLR_ACCUMULATION_OS_TRANSFER_BOUNDED_THEOREM_NOTE_2026_07_12_INTAKE_NOTE_2026-08-05.md:3-15,29-40`,
states authority `none`, audit `unset`, and `branch_only_never_mainlined`; it
defeats novelty of merely defining a conditional Haar integral, not (11)--
(28).

Primitive-registry and controlled-vocabulary scans found no refinement,
perfect-action, coarse-transfer, physical-time, or component-selection
primitive that could be imported silently.  No physics literature,
literature coefficient, or fitted datum is used.

### N7 -- steelman

The strongest escape is an enlarged perfect-action basis closed under repeated
conditional Haar integration.  One would supply graph embeddings, prove
associativity of successive disintegrations, track all generated character
and multiloop coefficients, and establish a uniform locality or truncation
estimate.  Such a flow could converge even though the inherited one-parameter
crossing changes at the first cell.  Nothing in (11)--(28) rules it out.  A
physical continuum theorem would additionally need lattice spacing, time
normalization, measure/coefficient scaling, and comparison maps.

### N8 -- cross-cycle echo and live status

| Echo | Live status | Retired here? | Mechanism/applicability |
|---|---|---:|---|
| universal geometric refinement net | `positive_theorem`, effective `unaudited` | no | geometric support only |
| constrained-fiber/raw-RG rows | `bounded_theorem`, effective `unaudited` | no | method context, different `SU(3)` action/carrier |
| two-horizon pullback | `bounded_theorem`, effective `unaudited` | no | coefficient-grammar identity, not this compression |
| plaquette pullback warning | `no_go`, effective `unaudited` | no | blocks isometry-only inference, respected by (8)--(11) |
| historic factor-two wrapper | authority `none`, audit `unset`, branch-only | no | prior-art evidence only |
| co-scaled temporal/refinement in-flight parent | `bounded_theorem`, current surface `conditional-support` | partially | its named `J*T_fJ` object is closed only on this supplied cell/family |

No row is imported as retained authority.  This theorem remains a branch
proposal requiring independent audit.

## Review and landing conditions

This proposal is stacked directly on Block227 commit `0d0d728271`.  Block227
and every declared upstream dependency must land first, or a reviewer must
re-establish the cumulative delta from refreshed `origin/main`; this note
must never merge out of order.  The independent helper is packet-reachable by
the primary runner's static import and `AUDIT_INPUT_PATHS`.  A fresh canonical
runner cache, refreshed citation-graph manifest containing exactly the two
declared internal dependencies, exact staged-byte review, and cumulative
current-main replay are hard landing conditions.  No generated audit surface
other than the manifest belongs in the science delta.

## Runner certificate

The primary SymPy runner executes exact finite diagnostics for normalized
`Z_2` ordered-path pushforward, all 48 proper/improper signed-permutation
frame controls, the two-half `Z_2` fiber, the nonabelian `S_3`
character/dimension fusion, diagnostic strict support, the quotient, the
comparison constants, and the linear-member determinant/vector arithmetic.
The full `O(3)` operator identity and all-channel support are the analytic
proof (1)--(16a), not a finite executable enumeration.  The runner also binds
every import and claim fence.

The independent checker uses only `Fraction`, exact `S_3` permutation
arithmetic, exact character products, direct double-Haar sums, and direct
`Z_2` enumeration.  It derives rather than copies the fusion coefficients,
normalization, and induced sector constants.  Every primary check family has
a dedicated hostile mutation changing its load-bearing input or conclusion.
No executable uses floating arithmetic, fitted data, or float-to-exact
reconstruction.

## Exact strongest remaining obligation

Construct an associative iterated flow on an indexed family of gauge
2-complexes.  The next theorem must give the coefficient and measure update
after every compression, prove compatibility of successive `J` maps and Haar
projectors, and control either a complete generated basis or a disclosed
truncation in a uniform locality/error norm.  Only then can one ask for a
spatial limit; physical time and continuum interpretation remain separate
suppliers.

No claim in this note is a framework axiom, primitive, audit verdict, or
authority-state mutation.
