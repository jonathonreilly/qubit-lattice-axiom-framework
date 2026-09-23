---
claim_id: compact_rotor_magnetic_excursion_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_reflection_and_path_check_2026_09_16.py
claim_scope: "Whole-interval magnetic-excursion bounds for the same supplied rotor ground law, with volume-uniform constants at fixed positive g and T."
upstream_dependencies: ["compact_rotor_sampled_magnetic_event_bounded_theorem_note_2026-09-16"]
---

# Magnetic excursions throughout time intervals

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

Whole-interval magnetic-excursion bounds for the same supplied rotor ground law, with volume-uniform constants at fixed positive g and T. This is a positive conditional theorem for the explicitly supplied Hamiltonian, geometry and limit order, not a derivation of that Hamiltonian from framework axioms. No audit verdict or retained promotion is asserted.

Load-bearing mathematical parents: [COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md](COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md). These are supplied-model proof dependencies, not retained axioms.

## 1. Continuous-time events

For a spatial plaquette p and a time interval I_n=[nT,(n+1)T], define

    A_(p,n)(alpha) = {sup_(s in I_n) d_T((Ctheta(s))_p,0) >=alpha},
                     0<alpha<pi, T>0.                      (1)

These are events on continuous compact Brownian/Feynman-Kac paths. No
sampling of the supremum is used in the proof. Define

    c_alpha=1-cos(alpha/2),
    q_exc(g,T,alpha)=min(1, exp[-T c_alpha/g^2]
                           +16exp[-alpha^2/(512g^2 T)]),
    eps_exc(g,T,alpha)=min(1,exp(C0 T) q_exc^(1/4)),
    C0=3pi^2/16+12(1/3-2/pi^2).                             (2)

For k specified distinct plaquette/interval pairs of one orientation,

    P_ground(intersection A_(p,n)) <= eps_exc^k.             (3)

For arbitrary orientations, replace k by ceil(k/3). This is uniform in
even L>=4, at fixed positive g<=1 and fixed T. It controls excursions
within each whole interval, not just its boundary configurations.

## 2. A one-plaquette path bound from any starting angle

Write independent real lifts of free link Brownian increments as gW_e.
Suppose all four links of a plaquette obey

    sup_(0<=s<=T)|gW_e(s)| <=alpha/16.                       (4)

Then for ANY two times s,t in this interval, the circle distance between
their plaquette fluxes is at most4*(2alpha/16)=alpha/2.
If event (1) occurs, continuity on the compact interval supplies a time
attaining the supremum. Its distance from zero is at least alpha.
The flux therefore has distance at least alpha/2 throughout the interval.
Its potential action is at least T c_alpha/g^2. This reasoning needs no
assumption about the initial angle.

The reflection-principle/normal tail union bound gives

    P((4) fails on at least one of the four edges)
                                 <=16exp[-alpha^2/(512g^2 T)].

Consequently, from every starting link configuration,

    E_theta[exp(-g^(-2) integral_0^T (1-cos F_p(s))ds)
             1_(A_(p,0))] <= q_exc(g,T,alpha).              (5)

The bound includes all real-lift windings of the circle path. It does
not equate small principal flux with a small global raw curl.

## 3. The constrained interval kernel need not be positive semidefinite

Fix one orientation and one normal-plane parity, and let D consist of
all N/2 plaquettes of that orientation in those planes. Let K_D(T;x,y)
be the actual Feynman-Kac transition kernel of (1) in the sampled-event note, with
the additional event that EVERY plaquette of D has event (1) somewhere
in [0,T]. Their bad times can differ. K_D is a nonnegative kernel and
is symmetric under time reversal. It obeys pointwise

    0<=K_D(T;x,y)<=exp(-TH)(x,y).                            (6)

Select the N/4 edge-disjoint checkerboard plaquettes from the sampled-event note
section5. Discard all other event indicators and all other nonnegative
plaquette potentials. Free Brownian independence on the selected edge
sets, together with (5), proves the row bound

    sup_x integral K_D(T;x,y)dy <= q_exc^(N/4).              (7)

Symmetry and Schur's test imply ||K_D||<=q_exc^(N/4).
The Hilbert-Schmidt norm is finite and (6) gives

    Tr K_D^2 <= Tr exp(-2TH).                               (8)

Pointwise nonnegative kernel and a nonnegative quadratic form are
different properties. No positive-semidefinite claim about K_D is
needed. For even M>=2 its real eigenvalues satisfy

    0<=Tr K_D^M <= ||K_D||^(M-2) Tr K_D^2
                       <= q_exc^[(N/4)(M-2)] Tr exp(-2TH).  (9)

This replaces the positive-operator estimate for P_A exp(-TH)P_A used
in the sampled-event note. Reusing that estimate without this distinction would leave
an unsupported premise.

## 4. Chessboard dissemination

Use spatial unit cubes times intervals [nT,(n+1)T], with beta=MT and M
even. An excursion indicator on one normal face of the cube is a cell
function. Spatial reflection disseminates it to N/2 distinct faces,
each repeated twice. Time reflection preserves the whole-interval
supremum event. Unlike the endpoint event in the sampled-event note, dissemination
now imposes the event in EVERY interval; there is no factor-two temporal
duplication. The dense dissemination probability is

    Tr K_D(T)^M / Tr exp(-MT H).                            (10)

Endpoint coincidences between adjacent intervals do not invalidate the
Markov composition: conditioning on the shared boundary angle joins
the two path events exactly. Brownian paths are continuous and each
interval indicator includes its endpoints.

Apply the chessboard exponent1/(NM), (9), and E0<=C0 N. At fixed L,
take even M->infinity. The finite trace factor disappears, giving

    limsup dense_probability^(1/(NM))
                                  <=exp(C0 T) q_exc^(1/4). (11)

Finite collections of bounded interval-path events also converge from
the thermal loop measure to the stationary ground process. One way to
see this without a boundary-continuity assumption is to insert their
bounded Feynman-Kac kernels within a fixed window of duration W. The
remaining factor exp[-(beta-W)(H-E0)] converges in trace norm to the
rank-one ground projection. Dividing the full trace by exp(-beta E0)
leaves exp(W E0) times the constrained window kernel, precisely the
ground-process normalization. The window kernels are dominated by heat
kernels and bounded as operators. Thus no weak-convergence
claim for an indicator discontinuity is needed at this finite L step.

Assign each requested oriented plaquette to its anchor cube and choose
the inverse-reflected base face as in the sampled-event note. The time-interval event
is itself invariant under reversal. Distinct pairs of one orientation
occupy distinct cells, and (11) proves (3). For mixed orientations use
the largest orientation subcollection, of size at least ceil(k/3).

## 5. Clusters covering magnetic charge excursions at every time

Declare a cube/interval cell occupied if at least one of its six faces
has excursion event (1) at threshold pi/3. This measurable event contains
every path with a nonzero principal cube charge at any time in the
interval: at that time some face must have distance at least pi/3.
The union-of-witnesses argument, including the fact that a face belongs
to at most two cubes, gives

    P(n specified cells occupied) <= p_exc^n,
    p_exc=min(1,6 eps_exc(g,T,pi/3)^(1/6)).                 (12)

Occupation is defined by the finite union of continuous-path supremum
events, avoiding any need to regard Q_c(s) as a continuous function.
Branch values at pi are fixed consistently as in the sampled-event note for the charge
implication. A cell can be occupied even when its charge stays zero.

On the degree-eight nearest-neighbor graph of spatial cubes and time
intervals, the depth-first tree count again gives

    P(occupied component at a fixed cell has size >=s)
                           <=8^(2s-2) p_exc^s.             (13)

Use the same balanced T_alpha=alpha/[16sqrt(2)sqrt(c_alpha)] as before.
Now the exponent in q_exc is b_alpha/g^2, b_alpha=T_alpha c_alpha,
so

    eps_exc <=min(1,17^(1/4) exp[C0 T_alpha-b_alpha/(4g^2)]).
                                                               (14)

The leading negative exponent equals that in the sampled-event note(17), while the
prefactor is larger. At g=0.01 this expression gives the conservatively
rounded bounds eps_exc<1.269e-18, p_exc<0.006243,
and64p_exc<0.39954. A separate integral/constant checker
records the numerical evaluation; the inequalities follow from (14).

## 6. What this does and does not join

Equations (3) and (12) cover fluctuations between observation times in
the finite-volume stationary ground process. T remains a chosen block
duration, not a time lattice spacing. This is a stronger event than
the corresponding sampled event, with a suitably larger bound.

There is no assertion here that a magnetic current follows only nearest
neighbors in this chosen block graph, that every 4D compact defect has
been represented, or that electric winding sectors have been controlled.
The bounds establish sparse occupied cells in this specified graph.
Those missing identifications must be supplied before translating the
bound into a statement about an entire spacetime defect gas or phase.
Nor is existence of an infinite-volume continuous-path process proved
here; the estimates are uniform finite-volume statements. A spatial
path-tightness or direct cylinder-kernel construction is a separate step.

Known Feynman-Kac, chessboard and Schur tools are credited in the sampled-event note.
The theorem is a proposed composition with explicit hypotheses, not a
new axiom or a formal audit result. A dilute magnetic-defect regime
alone supplies no lower bound on the electric susceptibility target.

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
