The three checks are complete and all stayed within budget (each under 42 s and under 100 MB). I have what I need for the report.

# Lane G report: moving-record event rate as a clock, and a clock potential around concentrations

## 1. Question

Under I1–I3 (set ticks; records move at most one step per tick; contention settled by relative odds; sites reusable after their record leaves), does the local rate of record events become a genuine clock, with repeated, steady, per-site events of the kind the landed rate and Regge notes had to supply by hand?

And can odds set by the neighbourhood make that rate vary around a concentration of records like a gravitational potential? Specifically: rate ∝ 1+Φ, with Φ obeying a Poisson-like equation sourced by record density, a 1/r tail in 3D, and clocks slower near the concentration.

## 2. Answer

**Conditional yes, but the source is different from the one asked for.**

- **(i) Moves supply the clock; formations do not.**
  - Under I2 a site sees an unending stream of arrivals and departures with a steady positive rate. Per-edge hop counts reproduce the landed endpoint-mean sharing rule exactly at first order in density (EXACT; CHECKED).
  - Formations cannot. In any evolution that treats all sites alike, "one record per site" plus permanence caps the expected number of formations at a site, over all time, at one (EXACT).
- **(ii) A clock potential appears under these conditions:**
  - free records wander with direction-blind odds through a void where nothing forms or sticks;
  - a concentration captures them for good (a net sink);
  - free records are a minority (far density u∞ < 1/2).

  Then the steady move-event rate is r = r∞(1+Φ). Near the concentration Φ ≤ 0, so clocks run slower. Φ satisfies Δ_lat Φ = σ ≥ 0, which is the sign the Regge note requires. Its tail is Φ = −(J/κu∞)·G(x) + O(|x|⁻²), where G is the exact lattice Green's function, 1/(4π|x|) at large |x|. Grade: EXACT for the mean dynamics; CHECKED to within 0.006 in a tick-level toy.
- **(iii) The 1/r coefficient is the net capture current J (discrete Gauss law).** Detailed-balance (equilibrium) odds therefore give a flat far field and no clock potential at all (EXACT).
- **(iv) The source is the capture distribution, not the record density.**
  - The two agree only for dispersed, weakly capturing matter.
  - For a compact lump that wandering records cannot enter, the source saturates at the lump's capacity. Capacity grows like the lump's width, i.e. N^(1/3) rather than N (EXACT bound; CHECKED).
- **(v) Failure modes:**
  - spontaneous formation or capture in the void: screening (EXACT);
  - breeding re-formation: anti-screening, the same sign class as the landed vacuum surrogate (EXACT linearization);
  - exporting concentrations, or a majority-carrier background: wrong sign, clocks faster (CHECKED for the dense background);
  - a half-filled background: no first-order effect (CHECKED).
- **(vi) As physics this is an analog of the time-time (lapse) part only.** It faces additivity, universality, post-Newtonian (β_eff = 1/2) and establishment-time problems (ARGUED).

## 3. Derivation

**3.0 Supplied toy (nothing adopted).**
- Global ticks. Occupancy n_x ∈ {0,1}.
- **Free records** (carriers) hop to each neighbour with odds κ per tick (κ = 1/12 in the toy: lazy 1/2 × 1/6). The target must be empty; contention is settled with equal odds (I3, Q4). Contents are unused, so the clock is content-blind.
- **Held records** (the concentration B) do not move.
- **Capture:** a free record arriving on the contact shell S (empty sites adjacent to B) sticks for good.
- Reading I2 means a record keeps its existence and content while its site changes. That is a reading of "records are permanent", not in the axioms, and not adopted.

**3.1 What the landed notes needed (task 1).** All sources below are on origin/main and unaudited.
- **Regge note** (`THE_FORMATION_RATE_DEFINES_THE_STATIC_REGGE_EDGE_LENGTHS_…_2026-09-03`)
  - It says a repeated tick or local formation rate is extra structure, not supplied by Record.
  - It supplies the reading r/r0 = 1+Φ (temporal edge 1+Φ).
  - Its static source relation has an essential plus sign: ΔΦ = 4πG·P0ρ, i.e. Φ = −4πGφ with φ > 0. So the rate sits below r0 near a positive source.
  - The constant mode is removed by a zero-mean convention.
  - A 1/r asymptotic needs an infinite-lattice Green kernel.
- **Star-ticks note** (`THE_RULERS_PER_SITE_FORMATION_RATE_IS_THE_STAR_TICKS_RATE_…_2026-09-04`)
  - The axioms supply no intensity, schedule, repeated same-site formation or clock. The note itself says: "A permanent one-record-per-site history does not itself implement repeated endpoint events."
  - The sum-sharing rule S1 gives the edge's endpoint mean, r_e/(2r0) − 1 = (Φ_u+Φ_v)/2.
  - A clock counting the six incident edges (C2) smooths Φ to (Φ + mean_nn Φ)/2.
  - A class-uniform tick keeps only a Θ(L⁻⁴) share of the point-source profile, so the clock must be per site.
- **Formation-clock note** (`FORMATION_RATE_FUNCTIONS_…_2026-09-24`): a hazard that depends only on neighbour records is constant between neighbour events. Flow parameter and rate units are supplied.
- **Density-ruler note** (`THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_…_2026-09-03`): the factor-2 reading needs κν = 1. The half-filled gapped massless sea gives κ = 0.

So lane G must supply:
1. per-site repeated events with a steady positive rate;
2. a relative rate 1+Φ with ΔΦ = (positive) × source and Φ → 0 far away;
3. per-site resolution and the endpoint-mean edge rule;
4. a treatment of the constant mode.

Moves supply items 1 and 3. Re-formation does not supply item 1, and it endangers item 2 (see 3.2 and 3.9).

**3.2 Formation counts cannot be the steady clock (EXACT).**
- The setup: a law that is the same at every site, one record per site, permanent records, and moves that only relocate records.
- Then n_x(t+1) − n_x(t) = F_x(t) + (arrivals − departures), where F_x(t) is the number of formations at x on tick t.
- Under translation invariance, the mean inflow to x along each axis direction equals the mean outflow from x along it.
- Hence E[number of formations at x over [0,t)] = E n_x(t) − E n_x(0) ≤ 1.
- In a region R, formations over [0,t) are at most |R| + (bonds leaving R)·t. So sustained formation is a surface effect and must be exported.
- This extends the block-41 note's T5 remark that sustained production is incompatible with bounded occupancy.
- Corollary: "time as accumulation of records" saturates locally unless records are carried in from elsewhere.

**3.3 Moves are a clock.**
- **Steady rate.** For continuous-time symmetric exclusion at density u ∈ (0,1), the product measure is stationary and ergodic (named import: Liggett). The per-site event rate is 12κu(1−u) > 0 (EXACT). The tick toy measures r∞ = 0.0382, 0.2279 and 0.1832 events/site/tick at u = 0.04, 0.5 and 0.7 (CHECKED).
- **Edge rule.** The edge hop count is r_e = κ(u_u + u_v) + O(u²). With u = u∞(1+Φ) this gives r_e/(2κu∞) − 1 = (Φ_u+Φ_v)/2, which is S1 exactly at first order in density (EXACT).
- **Site count.** The site count is the sum over its six edges, which is the C2 form. It equals Φ wherever ΔΦ = 0, so the C1/C2 mismatch is confined to capture sites (EXACT).
- **Hazard.** The hazard is constant between neighbour events, consistent with the formation-clock note.

**3.4 Mean equation (EXACT).**
- For exclusion, d⟨n_x⟩/dt = κΣ_y⟨n_y(1−n_x) − n_x(1−n_y)⟩ = κΔ⟨n⟩. The exclusion products cancel; this is the same closure as block-41 T5.
- Impenetrable held records and linear capture keep the equation closed and linear.
- With perfect capture, u = 0 on S.

**3.5 Gauss law (EXACT).**
- Statement: if u is bounded, u → u∞, and −κΔu = s with s finitely supported, then u = u∞ + G∗s/κ = u∞ + (Σs/κ)G(x) + O(|x|⁻²).
- Proof: the difference is bounded and harmonic on Z³, hence constant (Liouville), and it tends to zero.
- With Σs = −J: Φ = −(J/κu∞)G + O(|x|⁻²).
- Corollary: where hops ignore the neighbourhood, the mean bond current is κ(u_x − u_y). Detailed balance makes every bond current zero, so u is constant on the free region. Odds derived from a static law therefore give no long-range clock profile. A 1/r tail needs irreversible capture, i.e. a non-equilibrium net sink.

**3.6 Steady state on Z³ (EXACT).**
- Let D = B∪S. Then u = u∞·P_x(never hit D) = u∞(1 − h_D). So Φ = −h_D ∈ [−1, 0].
- Δ_lat Φ is the equilibrium charge on S. Its total is Cap(D) = J/(κu∞), and Φ ~ −Cap/(4π|x|).
- 3D is essential: transience gives h_D < 1. In 1D/2D an absorber empties everything.
- The approach to the steady state goes as t^(−1/2): establishment time grows as range² (consistent with the transit-halo note's T2).
- On a finite torus a net sink needs replenishment. Uniform replenishment turns σ into P0σ, which is exactly the Regge note's zero-mean convention.

**3.7 Sign (EXACT under local equilibrium; CHECKED).**
- In harmonic regions r = 12κu(1−u) exactly.
- Hence r/r∞ = 1 + [(1−2u∞)/(1−u∞)]·Φ_u + O(Φ²).

| concentration | u∞ < 1/2 | u∞ = 1/2 | u∞ > 1/2 |
|---|---|---|---|
| net sink | slower (GR sign) | no first-order term (r/r∞ = 1 − h²) | faster |
| net exporter | faster | none | slower |
| equilibrium | flat | flat | flat |

Odds-driven formation pushes concentrations toward the wrong-sign column: block-41 T5 (unaudited) finds agreement raises formation odds next to records. If the records so formed leave, the concentration is an exporter. The GR sign needs J_net = (captures that stick) − (exports) > 0.

**3.8 The source (EXACT; CHECKED).**
- **(a) Carriers that may enter recorded sites, absorbed with odds q per visit (relative to κ).**
  - Δ_lat N = q·n·N, with N the local activity relative to far away.
  - Linearized, Δ_lat Φ = q·n: Poisson sourced by record density, with the Regge sign.
  - The charge is Q = 1ᵀ(G_BB + I/q)⁻¹1 = qN − q²·1ᵀG_BB·1 + …
  - It is additive only when q·Σ_j G(x_i − x_j) ≪ 1, and saturates at Cap(B).
- **(b) Carriers that cannot enter recorded sites.**
  - This covers free records and, under Q1's wording, shared possibilities, which belong to sites without a record.
  - A record with no empty neighbour never meets a carrier, so Q ≤ Cap(B∪∂B), which is Θ(width).
  - The same capacity non-additivity appears in block 42's T6.
- **I5 analog:** a jammed perfect absorber has event rate zero on and inside it ("time stops"), and charge ∝ radius, like the Schwarzschild mass–radius scaling. Analog only.

**3.9 Mass terms (EXACT linearization).**
- Linearizing around the background gives m² = (k + f0 − P_b)/κ, where:
  - k is capture by background matter;
  - f0 is spontaneous void formation, which needs a vacancy, so its rate f0(1−u) falls as carriers rise;
  - P_b is the breeding slope (formation odds next to free records).
- Inert void (all zero): massless, 1/r.
- k > 0 or f0 > 0: screened.
- P_b > k + f0: negative m², i.e. anti-screening (sign-changing profile) plus exponential carrier growth.
- **Re-formation at vacated sites.** A just-vacated site has the departed record next to it, so re-forming there is breeding. With positive odds the carriers grow until jamming (I5 everywhere; ARGUED via Fisher-type invasion, comparator).
- **Answer to the brief's open question, conditional on lane G:** for a 1/r clock potential, empty sites far from records must not form on their own.
- **Landed vacuum-response note** (`THE_VACUUM_RESPONSE_UNDER_THE_RATE_RULER_ANTI_SCREENS_…_2026-09-04`, unaudited):
  - For a stipulated surrogate ΔΦ = P0[ρ + χΦ] with a fitted sea susceptibility (χ0 ≈ −2.40), it finds m_eff² ≈ −2.04 / −1.19: no positive decay length, and sign-changing kernels.
  - It stresses that this is reference-dependent. The fixed-sea reference has zero uniform but nonzero non-uniform response; the field-dressed reference is zero by definition.
  - It also stresses that χ is not a function of λ alone, and that losing positivity is not a runaway without an evolution law.
  - In lane-G terms the surrogate sits in the breeding class.
  - The axioms do not fix whether the actual vacuum breeds or absorbs carriers.

**3.10 Readable clocks (rate EXACT; readability ARGUED).**
- Per-site event counts are not records.
- A small capturing test lump accumulates records at κ·Cap_test·u(x) ∝ 1+Φ(x). Its record count is a readable clock that runs slow near a big concentration.
- This reconciles "time = accumulation" with a steady clock: accumulation continues at absorbers fed by wanderers.

**3.11 What the potential supplies (ARGUED).**
- **Universality.** All clocks shift alike only if every local event's odds scale with one local activity. Vacancy-limited formation scales with 1−u instead.
- **Motion.**
  - Carriers stream inward with mean velocity −κ∇ln(1+Φ): an overdamped inflow, not inertial fall.
  - Activity-paced walkers have stationary density ∝ 1/(1+Φ) (EXACT, detailed balance).
  - A supplied Hamiltonian time-changed by the activity is the H(1,1) case of the landed rate-ruler note. There the massless/rest acceleration ratio is 0.9997, i.e. half the GR light bending. The factor 2 needs a spatial sector (ν = 1, κν = 1) that this mechanism does not supply.
- **Post-Newtonian order.**
  - With density-independent hops, the exterior N is flat-harmonic (N = 1 − U), so N² = 1 − 2U + U².
  - Identifying g00 = −N², that is β_eff = 1/2; GR in isotropic coordinates has 1 − 2U + 2U² (β = 1).
  - Exclusion lowers β further: β = (1 − 2c2/c1²)/2 ≤ 1/2.
  - An exponential lapse (β = 1) would need carrier flux ∝ −∇ln u.
- **No waves.** Changes spread by diffusion.

## 4. Checks

All runs used `nice -n 10` with OMP, OPENBLAS, VECLIB and MKL thread caps set to 1. Scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A6/`.

**`g1_green_capacity.py`** (0.9 s, 85 MB): exact Z³ Green's function, G(x) = ∫Π ive(x_i, 2t) dt.

*Validation*
- G(0) = 0.252731009858, matching Watson/6 to 5.7e-13.
- −ΔG residual off the origin ≤ 1.3e-10.

*Tail, 4π|x|G(x) → 1*

| distance n | axis | face diagonal | body diagonal |
|---|---|---|---|
| 1 | 1.0815 | — | — |
| 5 | 1.0117 | — | — |
| 12 | 1.00177 | — | — |
| 30 | 1.00028 | 0.99997 | 0.99994 |

The axis deviation scales as about 0.25/n².

*Exact capacities on Z³*

| cube side s | N | Cap(B) | Cap(B + contact shell) |
|---|---|---|---|
| 1 | 1 | 3.96 | 11.62 |
| 2 | 8 | 11.11 | 20.69 |
| 3 | 27 | 18.94 | 29.41 |
| 4 | 64 | 26.97 | 38.00 |
| 5 | 125 | 35.10 | 46.52 |
| 6 | 216 | 43.27 | 54.99 |

Capacity grows with side length, not with N.

*Transparent absorber, Q/(qN)*

| q | s = 1 | s = 6 |
|---|---|---|
| 0.001 | 0.9997 | 0.9945 |
| 0.1 | 0.975 | 0.646 |
| 10 (Q/Cap) | 0.72 | 0.97 |

The second-order expansion has a relative remainder of 6.45e-6 at q = 1e-3.

**`g2_box_solves.py`** (0.7 s, 97 MB): conjugate gradient on a 31³ box (relative residual 6.9e-12); 3³ lump with its contact shell.

*Exact Z³ tail, 4πr·h/Cap*
- Axis: 1.0031 at r=6, 1.0012 at r=14, 1.00015 at r=40.
- Body diagonal: 0.998–0.9992.

*Box versus Z³*
- Cap_box = 34.06 versus 29.41 on Z³ (the reservoir boundary sits 15 sites away).

*Screening: r·Φ at r = 3 / 13*
- q̄ = 0: −2.13 / −0.50.
- q̄ = 0.05: −1.82 / −0.038.
- Background-only depletion at the centre: 0.16.

*Anti-screening (m² = −0.1)*
- Φ changes sign at r ≈ 8.5. The m² = 0 control stays negative.

**`g3_move_clock_mc.py`** (toy I1–I3 dynamics; seed 20261002; arguments burn-in, measurement ticks, reference ticks, u∞)
- Dynamics: lazy parallel hops, exclusion, random contention winner, capture on the shell, and a reservoir layer reset each tick.
- r∞ comes from a periodic run at exactly u∞·N records.

*u∞ = 0.04* (5000 burn-in + 200000 measured ticks, 28.6 s, 40 MB)
- Capture flux 0.11310 ± 0.00072 versus the Gauss prediction u∞·Cap_box/12 = 0.11353 (ratio 0.9961).

| r | r/r∞ (toy) | 1−h_box |
|---|---|---|
| 3 | 0.298 | 0.292 |
| 5 | 0.629 | 0.624 |
| 7 | 0.777 | 0.774 |
| 10 | 0.885 | 0.889 |
| 13 | 0.948 | 0.950 |

- Across all 11 bins the maximum |residual| is 0.0059 (tolerance 0.01; block standard errors 0.002–0.004).
- Density profile matches within 0.009.

*u∞ = 0.7* (41.8 s)
- Density still follows 1−h (within 0.015).
- The clock reads 0.84 at r=3 but 1.14 / 1.25 / 1.08 at r = 4 / 6 / 13: wrong sign.

*u∞ = 0.5* (33.1 s)

| r | 3 | 6 | 9 | 11 | 13 |
|---|---|---|---|---|---|
| r/r∞ | 0.53 | 0.94 | 0.992 | 1.0001 | 1.0026 |

The deficit follows h², not h. A first-order tail would give about −0.05 at r=13.

*Should be run (bigger, not run)*
- g3 at L=63, u∞=0.02, with h_box regenerated at L=63 (about 8× the cost).
- Neighbourhood-set capture odds (stick only on content agreement), to test Gauss with J_net emerging from odds rather than imposed.
- Breeding re-formation odds at vacated sites.
- Test-lump accretion clocks at several radii.

## 5. Real-physics match (comparators, not adopted)

**Matches**
- Gravitational time dilation: correct sign for net sinks in a minority-carrier gas.
- Exact 1/r tail.
- The nonlinear form Δ_lat N = q·n·N mirrors the static GR lapse equation D²N = 4πG(ρ+3p)N, but with a flat Laplacian and no pressure term.
- The landed P0 convention arises as uniform replenishment.
- Mass ∝ radius for jammed lumps is a black-hole-like scaling.
- Screening by the cosmic mean density sets in at λ = c/√(4πGρ̄) ≈ 2×10²⁶ m, about the Hubble length (dimensional estimate). So it does not obviously conflict with tests below Hubble scale.

**Mismatches and falsifiers**
- **Additivity.** Compact matter would gravitate by capacity, not mass. Null gravitational-shielding results and precise mass additivity cut against this.
- **Universality.** Different event types shift differently. Satellite clock redshift tests agree with GR to parts in 10⁵.
- **Post-Newtonian order.** β_eff = 1/2 versus β ≈ 1 to about 10⁻⁴ (perihelion, lunar ranging), unless a spatial-metric sector changes transport.
- **Waves.** Fields spread by diffusion; there are no waves, whereas gravitational waves travel at c to within about 10⁻¹⁵.
- **Establishment time.** Suppose one site per tick is light speed and there is one carrier population. A 1/r potential down to about 50 μm (laboratory inverse-square tests) needs a mean free path ℓ ≪ 50 μm. A profile established out to r within the age of the universe needs ℓ ≥ r²/(2cT). Together these allow at most r ≲ 0.2–1 AU. This agrees with the transit-halo note's units corollary.
- **Secular growth.** Capturing bodies would grow at a fractional rate κ·u∞·q₁; lunar ranging bounds on any change of GM constrain the carrier density.

## 6. Open edges and next steps

1. Find neighbourhood-set odds that give irreversible capture (zero departure odds on agreement, or burial under I5) while keeping Q4's equal odds when uninfluenced.
2. Where does the far gas come from if the void is inert? An initial condition on Z³ (I6)? Lumps deplete it, so all clocks slow over time; evaluate this.
3. Is there a carrier that can pass through recorded sites? Q1's wording puts shared possibilities only on unrecorded sites.
4. Universality (U): can formation odds be paced by the same activity as moves?
5. Find a spatial-metric dressing of carrier hops (Regge ν=1) that gives β = 1, for example flux ∝ −∇ln u.
6. If the mobile records in the vacuum are half-filled, the move clock has no first-order response. That is the move-clock analog of the density-ruler note's half-filled zero. The clock's carrier would then need to be a separate minority population.
7. Ballistic or axis-locked carriers (I4 conveyors, or "content as direction of travel") give axial wakes or 1/r² shadows rather than 1/r. Find what randomizes direction.
8. I1 local ticks: rate ratios r(x)/r(y) survive, but compare them through exchanged records.

## 7. Plain-language summary

If records can wander one step at a time, each place gets a steady beat: records keep arriving and leaving, and that count works as a clock. New records forming cannot keep a steady beat, because each place can only fill up about once.

If wanderers that touch a clump stick to it for good, the clump thins out the wanderers around it. Places near the clump then get fewer comings and goings, and their clocks run slow by an amount that fades as one over the distance, much as gravity slows clocks.

This only works if three things hold: empty places far from records stay quiet, the clump keeps taking records in rather than sending them out, and wanderers are not already crowding most places.

How strong the slowing is depends on how fast the clump swallows wanderers. For a loose sprinkle of records that grows with the number of records, but for a packed clump it grows only with its width, so it does not count records the way weight should.

These are toy results under ideas that have not been adopted, not a derivation of gravity.