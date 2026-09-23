---
claim_id: compact_rotor_spatial_ground_path_limit_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_reflection_and_path_check_2026_09_16.py
claim_scope: "Subsequential infinite-volume continuous compact ground paths, their local Brownian-bridge specification and transferred excursion bounds."
upstream_dependencies: ["compact_rotor_sampled_magnetic_event_bounded_theorem_note_2026-09-16", "compact_rotor_magnetic_excursion_bounded_theorem_note_2026-09-16"]
---

# Continuous compact ground paths in infinite spatial volume

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

Subsequential infinite-volume continuous compact ground paths, their local Brownian-bridge specification and transferred excursion bounds. This is a positive conditional theorem for the explicitly supplied Hamiltonian, geometry and limit order, not a derivation of that Hamiltonian from framework axioms. No audit verdict or retained promotion is asserted.

Load-bearing mathematical parents: [COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md), [COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md). These are supplied-model proof dependencies, not retained axioms.

The complete path-law construction below includes both reversible tightness and the actual compact local Brownian-bridge specification; the latter is part of the result.

## 1. A reversible diffusion estimate independent of spatial volume

For each finite torus, the ground-state transformed Markov generator is

    L f = -psi^(-1)(H-E0)(psi f)
        = (g^2/2) Delta f + g^2 grad log(psi) dot grad f.    (1)

Its invariant probability measure is psi^2 times Haar and it is
reversible. Smoothness and strict positivity of psi on the finite
compact torus make (1) an ordinary smooth, nonexplosive diffusion.
No bound on grad log(psi) uniform in volume is asserted or needed.

Let f be a smooth real function with |grad f|<=a. Over a fixed interval
[0,R], the forward Ito decomposition is

    f(X_t)-f(X_s) = M_t-M_s + integral_s^t Lf(X_u)du,
    d<M>_u = g^2 |grad f(X_u)|^2 du <= g^2 a^2 du.         (2)

By stationarity and reversibility, the reversed path X_(R-u) is a
diffusion with the SAME generator L. Applying Ito to that reversed
path and subtracting yields

    f(X_t)-f(X_s) = (M_t-M_s)/2
                      -(Mhat_(R-s)-Mhat_(R-t))/2.           (3)

The drift integrals cancel. Mhat is a martingale in the reversed
filtration, with the same bound on its bracket. Forward and backward
martingales need not be independent. This elementary smooth-case proof
is the Lyons-Zheng forward/backward decomposition; no new stochastic
calculus principle is claimed.

If a continuous martingale increment Z of duration h has bracket
d<Z>_u<=b du, Ito's formula gives

    E Z_h^4 =6 E integral_0^h Z_u^2 d<Z>_u
            <=6b integral_0^h bu du =3b^2 h^2.             (4)

Localization justifies the identity before using the finite bracket
bound. Apply it separately to the two increments in (3) and use
|x-y|^4<=8(|x|^4+|y|^4). Then

    E|f(X_t)-f(X_s)|^4 <=3g^4 a^4 |t-s|^2.                 (5)

For f=cos(theta_e) and f=sin(theta_e), a=1. Since
(u^2+v^2)^2<=2(u^4+v^4), this gives the circle-chord estimate

    E|exp(i theta_e(t))-exp(i theta_e(s))|^4
                                      <=12g^4 |t-s|^2.    (6)

It holds for every link e and every finite L. The large magnetic
coefficient and the number of links do not enter this estimate because
reversibility cancels the ground drift. This is a statement about
stationary Euclidean paths, not a real-time propagation speed.

## 2. Tightness and a subsequential continuous-path state

The finite-volume processes have two-sided stationary versions. Extend
each spatially periodically to links of Z^3. On any compact time window,
(6), compactness of initial circle values and the Kolmogorov tightness
criterion make each link-path family tight in C(window,circle), with the
uniform topology. One may use any Holder exponent less than1/4 in
the fourth-moment criterion; no optimal regularity claim is needed.

Taking finitely many links preserves tightness. Diagonal compactness
over countably many links and windows gives a subsequence L_j->infinity
and a probability law mu on

    product_(e in edges(Z^3)) C_loc(R,R/(2pi Z))             (7)

to which the finite ground laws converge locally in the continuous-path
topology. For any fixed spatial support, periodic wrap identifications
are absent once L is sufficiently large. The limit is stationary and
time reversible, spatially translation invariant and gauge invariant
under time-independent gauge transformations of finite spatial support.
These statements follow by passing bounded continuous local path
functions through the corresponding finite-volume symmetries.

The time and coordinate-space reflection-positive inequalities pass
in the same way for continuous bounded local half-space functions.
Density in the relevant L^2 spaces extends them to bounded measurable
half-space functions. This is Euclidean reflection positivity; no
relativistic continuum limit or photon reconstruction is implied.

## 3. The local path specification is the actual compact one

The limit can also be matched to its local Feynman-Kac specification.
Choose a finite set S of links and a finite open time interval (a,b).
Condition on the paths outside S in that interval and on the two
endpoint angle configurations of S. In a finite-volume ground law,
the conditional distribution of the S paths is the product of compact
Brownian bridges of diffusivity g^2, weighted by

    exp[-g^(-2) integral_a^b
                 sum_(p touching S) (1-cos F_p(s)) ds].     (8)

Normalize this positive finite weight. All terms depending only on
outside paths cancel. The endpoint ground-state factors cancel too
once those endpoint configurations and the exterior are conditioned.
This follows directly from the Markov/Feynman-Kac factorization, and
does not replace the bridges by fixed-winding real bridges.

This specification has only finitely many neighboring link paths. Its
normalizing denominator is at least exp[-2 n(S)(b-a)/g^2], where n(S)
counts the touching plaquettes. For bounded continuous functions of the
interior paths, the normalized expectation is continuous in the endpoint
angles and the finitely many exterior paths in their uniform topology.
For the Brownian-bridge part, one can choose local endpoint charts and
sum real Gaussian bridges over all windings: the positive circle heat
kernel normalizes the sum, and its Gaussian tails give uniform convergence
on compact endpoint sets. The potential in (8) is a bounded continuous
functional of these paths. Thus the claimed specification continuity
does not require a uniform bound on the ground wavefunction.

Test the finite-volume conditional identity against bounded continuous
local functions of the exterior. Once the support embeds, its kernel
is precisely (8), with no L dependence. Pass both sides through the
local path limit, then extend by the monotone-class argument. This
shows that mu obeys the compact local path specification (8).

This identifies mu as a subsequential Euclidean Gibbs law obtained from
the actual finite-volume ground processes. It does not assert uniqueness,
purity, a limiting infinite-dimensional SDE drift, or equality with
the free-box equal-time limit in the contextual PR8164 construction.

## 4. Excursion and defect-cover estimates survive the spatial limit

For a fixed plaquette and finite interval, the functional

    omega -> sup_(s in I) d_T((Ctheta(s))_p,0)

is continuous in the finite-link uniform path topology. For alpha'<alpha,
the closed event of all specified suprema being at least alpha is
contained in the OPEN event of all being greater than alpha'. By
Portmanteau and the magnetic-excursion note,

    mu(all suprema>=alpha)
      <=mu(all suprema>alpha')
      <=liminf_j mu_(L_j)(all suprema>alpha')
      <=eps_exc(g,T,alpha')^r,                              (9)

where r=k for one orientation and r=ceil(k/3) otherwise. Send
alpha' up to alpha at fixed sampling/block duration T. The explicit
eps_exc is continuous in alpha, proving exactly the same joint bound
in mu. This avoids using the reversed Portmanteau inequality for a
closed event.

Define occupied cube/interval cells by the six-face excursion cover
at threshold pi/3, as in the magnetic-excursion note section5. This cover contains every
nonzero principal magnetic cube charge anywhere in the interval.
The same deterministic witnesses and tree count give

    mu(component at a fixed cell has at least s vertices)
                       <=8^(2s-2) p_exc^s.                 (10)

For the explicit g=0.01, T=0.126439394990932821... values of the magnetic-excursion note,
64p_exc<0.4. Thus every occupied component is finite mu-almost surely
in this specified nearest-neighbor cell graph. The assertion for all
cells follows by a countable union over the zero-probability events
that an individual component is infinite.

This is an infinite-volume bound on a magnetic-excursion cover, not
an assertion that all compact spacetime defect currents have already
been constructed or shown finite. The electric and winding joins,
the susceptibility lower bound, and the photon phase remain open.

## 5. Source credit and checks

The forward/backward identity is classical. A primary treatment is
Gerald Trutnau, *A short note on Lyons-Zheng decomposition in the
non-sectorial case*, preprint07-06-262, Theorem3.2 and its symmetric
specialization (PDF5-6),
https://bibos.math.uni-bielefeld.de/preprints/07-06-262.pdf .
PDF SHA256 a57f23e927ea680cf66100c3f8b812b699153dbadc4147813eb0327143deac08;
all8 pages extracted and read. The original cited source is T.J.Lyons
and W.Zheng, *A crossing estimate for the canonical process on a
Dirichlet space and a tightness result*, Asterisque157-158(1988),249-271;
that original text has not yet been read in the original source review.

Here only the smooth finite-dimensional reversible case is used, and
(2)-(4) derive the needed formula and constant explicitly. Separate
checks compare the fourth-moment estimate with an exactly soluble
free circle diffusion and a Fourier approximation to an interacting
single-rotor ground process. A kinetic normalization fault is rejected;
drift cancellation is checked analytically in (2)-(3). This cannot numerically prove
tightness or uniqueness of a thermodynamic state.

## Evidence and execution boundary

Primary runner: `scripts/compact_rotor_reflection_and_path_check_2026_09_16.py`. The reflection/path runner jointly supports the magnetic-excursion and spatial-path-limit notes.

The three calculations retain every original fixture, arithmetic operation, assertion and tolerance. Each retains a 120-second timeout. A 512 MiB external process cap is proposed from the bounded representations and library overhead; it is not a measured peak or a completed execution. Each runner reads and hash-pins its declared source-note inputs and writes JSON under `logs/runner-cache/`. `TOTAL: PASS=3 FAIL=0` counts three completed diagnostic families, not three assertions or exhaustive theorem coverage. The JSON separately labels the static source assertion count.

The [historical recovery packet](work_history/repo/review_feedback/pr8165-evidence/README.md) preserves all 88 original paths, modes, blobs and byte hashes, all four full working proofs, all three calculations, eleven mutation histories and the failed Fourier attempt. Historical output is not current-source execution evidence. PR8164 is contextual comparison only; no theorem or status is imported from it.

## No-Go Discipline Gate

**N1 — Actual routes.** Formal negative-packet certification is deferred: the source does not supply five qualifying refuted routes. The actual approach registry and finite countercontrols are preserved; no extra routes are invented. This does not negate the positive supplied-model proofs or the exact finite counterexamples.

**N2 — Shared scope.** One supplied Hamiltonian and the stated compact geometry underlie the chain. Reflection/chessboard is a shared mathematical premise; future source-response, harmonic-sector and microscopic-current obligations are not independent walls proved here.

**N3 — Conditions.** Compact Haar angles, the full thermal trace followed by its neutral ground limit, even L>=4, fixed positive g and T, and the oriented principal branch are explicit. No limiting-state uniqueness, positive-semidefinite constrained kernel or finite-clock Brownian behavior is assumed.

**N4 — Credit and failures.** Biskup supplies the matched chessboard theorem; the finite smooth reversible identity is derived and credited. The failed Fourier cutoff attempt, exact subsequent refinement, eleven mutation outcomes and prior source versions remain recoverable without treating them as current captures.

**N5 — Resolution.** Finite geometry, circle/rotor matrices and integer cochains test the stated identities and constants. Volume-uniform bounds, continuous-path tightness and the infinite-volume specification are analytic proofs, not exhaustive numerical runs. The five execution-scope lines report only the program that actually finishes.

**N6 — Partial closure.** Sampled events, full excursions, a continuous-path spatial limit and a fixed-T current construction are successive positive results. No new primitive is proposed.

**N7 — Strongest boundary.** Rare coarse conserved currents do not by themselves give a photon, a native Hamiltonian, a unique vacuum, microscopic T->0 control, exhaustive harmonic sectors or physical electric reconstruction. These are open extensions, not impossibility claims.

**N8 — Reopening.** Smooth-field/current weighting and source-response control may resolve the remaining physical questions. The periodic spatial subsequence is not equated with the contextual free-box state. No broad negative certification is claimed.
