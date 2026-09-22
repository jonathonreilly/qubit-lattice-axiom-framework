---
claim_id: admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_for_the_ledger_rest_energy_needs_the_bonds_own_amplitude_no_first_order_strain_gap_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk (open PR #8570; not adopted), the frame coupling of block 62 (#8592), the relabelling and strain couplings of blocks 63–64 (#8593, #8595) with their family of field energies, and the coupling to the bond's own amplitude named in block 82 (#8628): exact position-space operators on the 4³ torus (Gaussian rationals), the ring of four (exact symbolic spectrum), the sixteen corner states; spectra on 6³ and the sea on 8³ executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_rest_energy_needs_the_bonds_own_amplitude_2026_09_22.py
---

# Alternating lengths are a relabelling: invisible to the walk and free for the ledger; a rest energy needs the bond's own amplitude; no strain gaps at first order

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact operator identities on the 4³ torus that hold on every even torus by their proofs; exact spectrum on the ring of four; executed spectra and sea energies labelled; nothing adopted or registered; unaudited)

This note works within block 54's walk, the frame and strain couplings of blocks 62-64 and the coupling to the bond's own amplitude of block 82; it reports what an alternation of the lengths is in each, and what the sea's energy does under it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 82 (PR #8628) found that an alternation of the hop amplitudes, `t_j(x) = 1 + δ(−1)^{x_j}`, gives every one of the walk's eight species the rest energy `√3β|δ|`, and named the lengths — a field the lane already carries (blocks 59–61) — as the one candidate for a rest energy that is not a record pattern. This note asks what an alternation of the lengths is in the lane's own couplings. It is a relabelling: nothing.

1. **Invisible to the walk, exactly (T1).** Through block 62's site frame, `½{e_jσ_j, S_j}` with `e_j = 1 + δ(−1)^{x_j}`, the walk is exactly the free walk: `(−1)^{x_j}` anticommutes with `S_j`. Through block 64's strain coupling, `Σ_a σ_a ½{C_a[B_a^a], S_a}` with `B_a^a = δ(−1)^{x_a}`, the added operator is exactly zero: the bond-weighted hop of an alternating weight is `iδ(−1)^{x_a}S_a`, which anticommutes with `S_a`.
2. **Free for the ledger, exactly (T1(c)).** The alternation is the relabelling `B_a^a = d_aξ_a` with `ξ_a = −(δ/2)(−1)^{x_a}` — the sites displaced alternately by `∓δ/2` along each axis. Every plaquette curl of it vanishes and the volume sum over the torus is exactly `N`: block 64's whole family of field energies, curvature member included, charges nothing for it. Block 64 T1 said curls are blind to relabellings; here is the relabelling that block 82's rest energy would need, and the lane sees none of it.
3. **No frame or strain pattern gives a first-order rest energy (T2).** Every term of the form `½{X, S_j}` — the frame coupling and every strain coupling of the lane, for any site or bond function `X` — has exactly zero matrix elements inside the sixteen-state corner subspace, because `S_j` annihilates every corner plane wave on either side. A rest energy at the species points cannot come from such a term at first order. The coupling that does give one, `Σ_a σ_a (1/2i)(t_a(x)T_a − T_a†t_a(x))`, reads the bond's own amplitude; its corner block squares to exactly `3δ²`. The difference is exact: the lane's couplings see a bond through the average of a site quantity over its two ends or through a difference across it, and for an alternation both vanish; a rest energy needs the value on the bond.
4. **The sea never rises under an alternation, but never sees one (T3).** The sum of the lowest `N` eigenvalues is concave in the generator and, for the bond-amplitude coupling, even in `δ` (translation by one step carries `+δ` to `−δ`, exactly); so it is largest at `δ = 0` — on the ring of four the spectrum is `±|δ|, ±1` (twice each) and the sea's energy `−2 − 2|δ|`. In the lane's own couplings the alternation is not there to lower anything.
5. **Executed (control; floating point).** On the `6³` torus with `δ = 3/10`, the frame-coupled and strain-coupled alternations differ from the free walk by exactly `0` in every matrix element (least `|E|` stays `0`); the bond-amplitude alternation differs by `0.15` and has least `|E| = 0.5196 = √3δ`. A smooth random strain through block 64's coupling (`|V|` up to `0.33`) has corner matrix elements at the level of `10⁻¹⁸` and moves the sixteen exact zero modes to within `4·10⁻⁵` of zero (the species points shift slightly off the torus grid): no gap. The sea's energy per site on `8³` falls from `−1.190` to `−1.732` under the bond-amplitude alternation as `δ` goes from `0` to `1` and is constant to every digit under the frame-coupled one.

So the leading candidate of the rest-energy panel — a derived rest energy from the lane's lengths — closes on the lane's own terms: in every coupling the lane derived, an alternation of the lengths is a coordinate choice, invisible and free, and it can be neither selected nor felt. A rest energy of block 82's alternating kind needs a coupling that reads a bond's own amplitude, which is not a relabelling's deformation and is not in the lane; whether the axioms admit such a coupling is a question for the owner, named under Boundaries.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 82 (PR #8628): 'whether anything in the framework alternates the lengths is the next question'; decision record row 48"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the alternation is a relabelling in every lane coupling (invisible, free); no frame or strain pattern gives a first-order rest energy; block 82's rest energy needs a bond-amplitude coupling that is not in the lane; next: whether a bond-amplitude coupling is admissible (a bond's length as the hop's weight rather than a relabelling: the owner's fork); second-order gaps from smooth strains (executed here as null on 6³); the two-record exclusion problem on 4³"
conditional_surface_status: "T1 and T2 exact on the 4³ torus and on every even torus by their one-line proofs; T3 exact on the ring of four with concavity and evenness in general; the executed spectra and sea energies are the control's"
hypothetical_axiom_status: "the walk; the frame, strain and bond-amplitude couplings; the sea reading; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, proper rotations) and the Qubit axiom, and its silence on amplitude dynamics and on lengths. Blocks 54, 62, 63, 64 (open PRs #8570, #8592, #8593, #8595) supply the walk, the frame, the relabelling and the strain coupling with its family of field energies; block 82 (#8628) the bond-amplitude coupling and its rest energy. Nothing is adopted here.

- **Shifts and differences.** `(T_aψ)(x) = ψ(x + e_a)`; `S_a = (T_a − T_a†)/2i`; `(d_af)(x) = f(x + e_a) − f(x)`.
- **Walk.** `H = Σ_a σ_a S_a` on the `4³` torus (position space; every entry a Gaussian rational).
- **Frame coupling (block 62).** `H[e] = ½Σ_j{e_j(x)σ_j, S_j}` for a diagonal site frame `e_j(x)`.
- **Strain coupling (blocks 63–64).** `H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`, with `(C_a[v]ψ)(x) = ½[v(x)ψ(x + e_a) + v(x − e_a)ψ(x − e_a)]`; a relabelling by `ξ` shifts `B_a^j` by `d_aξ_j`; the curl `F_ab^j = d_aB_b^j − d_bB_a^j`; the field energies are functions of the curls (and the volume, `det e` with `e_a^a = 1 + B_a^a`).
- **The alternation.** `B_a^a(x) = δ(−1)^{x_a}` (no tilt), `δ = 3/10` in the runner; `e_j = 1 + B_j^j`.
- **Bond-amplitude coupling (block 82).** `Σ_a σ_a (1/2i)(t_a(x)T_a − T_a†t_a(x))`, `t_a(x)` the amplitude of the bond from `x` along `a`; `t_a = 1 + B_a^a`.
- **Corner states.** The eight plane waves with `k ∈ {0, π}³` (entries `±1`), each with two coin states: sixteen states, all annihilated by every `S_j`.
- **The sea.** `E_sea = Σ_{E<0}E` of the one-record generator; on the ring of four with the bond-amplitude coupling, exact.

That a lattice displacement pattern with period two is the dimerisation of Su, Schrieffer and Heeger, and that a hop amplitude depending on the bond's length is the Peierls coupling, are the comparators; that the sum of the lowest eigenvalues is a concave function of the operator is Ky Fan's principle. None is used as authority.

## Prior art and what is new

Block 64 T1 proved that the curls, and hence the field energies, are blind to relabellings, and block 63 T2 that a relabelling's deformation is what the strain couples to. Block 82 T3(a) gave the rest energy of an alternating hop amplitude. New, inside the framework's vocabulary: that the alternation which block 82's rest energy needs is exactly a relabelling; the two exact vanishings (frame and strain) by one anticommutation; the corner-subspace lemma for every `½{X, S_j}` term; the identification of what a rest energy needs from a bond (its own value); and the concavity-and-evenness argument for the sea. No gravitational claim is made.

## Exact target and obligation graph

Target: what an alternation of the lengths is in the lane's couplings and ledger. Obligations: (O1) the walk's response through the frame and the strain; (O2) the ledger's charge; (O3) first-order rest energies from any frame or strain pattern; (O4) the sea. T1 discharges O1, O2; T2 discharges O3; T3 discharges O4.

## Theorem T1 — an alternation of the lengths is a relabelling: invisible to the walk and free for the ledger

*Statement.* Let `B_a^a(x) = δ(−1)^{x_a}` on every axis, no tilts, on an even torus. (a) `½{e_jσ_j, S_j}` with `e_j = 1 + B_j^j` equals `σ_jS_j` exactly. (b) `½{C_a[B_a^a], S_a}` is exactly the zero operator. (c) `B_a^a = d_aξ_a` with `ξ_a(x) = −(δ/2)(−1)^{x_a}`; every plaquette curl of `B` vanishes and `Σ_x det e = Σ_x Π_a(1 + B_a^a(x)) = N`; every field energy of block 64's family takes its unstrained value.

*Proof.* (a) `ε_a = (−1)^{x_a}` anticommutes with `T_a` and `T_a†`, hence with `S_a`; `½{ε_aσ_a, S_a} = σ_a·½(ε_aS_a + S_aε_a) = 0`. (b) For `v(x) = δε_a(x)`, `v(x − e_a) = −v(x)`, so `(C_a[v]ψ)(x) = (δ/2)ε_a(x)[ψ(x + e_a) − ψ(x − e_a)] = iδ(ε_aS_aψ)(x)`, and `{ε_aS_a, S_a} = ε_aS_a² − ε_aS_a² = 0`. (c) `ξ_a(x + e_a) − ξ_a(x) = −(δ/2)((−1)^{x_a+1} − (−1)^{x_a}) = δ(−1)^{x_a}`; `d_bB_a^a = 0` for `b ≠ a` since `B_a^a` depends on `x_a` only, and `B_b^a = 0`; `Π_a(1 + δε_a)` summed over an even torus leaves only the constant term. Block 64 T1: functions of the curls are blind to relabellings. Family B checks (a)–(c) exactly on `4³` with `δ = 3/10`. ∎

## Theorem T2 — no frame or strain pattern gives a first-order rest energy; the bond's own amplitude does

*Statement.* (a) For every site or bond function `X` and every coin matrix, the term `½{X, S_j}` (and `½{C_a[X], S_a}`) has zero matrix elements between any two of the sixteen corner states. (b) The bond-amplitude coupling with `t_a = 1 + δε_a` has a nonzero block on the corner subspace whose square is exactly `3δ²·1`.

*Proof.* (a) `S_j` is Hermitian and annihilates every corner plane wave: `sin k_j = 0` at `k ∈ {0, π}³`. Then `⟨u|XS_j|w⟩ = 0` and `⟨u|S_jX|w⟩ = (S_ju)†Xw = 0`. (b) `(1/2i)(δε_aT_a − T_a†δε_a) = (δ/2i)ε_a(T_a + T_a†) = −iδε_aC_a`, `C_a` the symmetric hop with symbol `cos k_a`, which is `±1` at the corners; the corner block is block 82's mass matrix `δΣ_a σ_a τ^{(a)}` up to phases, whose square is `3δ²`. Family C computes both exactly on `4³` (generic rational `X` and `v`; the corner block and its square). ∎

*Remark.* The lane's couplings see a bond through `½{·, S_j}`: the average of a site quantity over the bond's two ends (the frame) or the bond-weighted symmetric hop composed with the momentum (the strain). For an alternation both vanish. A rest energy at the species points needs the amplitude on the bond itself — a coupling that is not a relabelling's deformation (block 63 T2) and does not belong to block 64's family. Second-order rest energies from smooth strains are not excluded by (a); the control finds none on `6³`.

## Theorem T3 — the sea's energy never rises under an alternation

*Statement.* For the bond-amplitude coupling, `E_sea(δ) ≤ E_sea(0)` for every `δ`. On the ring of four the energies are `±|δ|` (twice) and `±1` (twice), exactly, and `E_sea = −2 − 2|δ|`.

*Proof.* The sum of the lowest `N` eigenvalues of a Hermitian matrix is the minimum of `tr(PH)` over rank-`N` projectors `P`: a minimum of linear functions, hence concave in `H`, hence concave in `δ` along `H(δ) = H + δV`. Translation by one step along every axis carries `H(δ)` to `H(−δ)` (family D checks this exactly on `4³`), so `E_sea` is even; a concave even function is largest at `0`. The ring of four is an exact `8 × 8` symbolic spectrum. ∎

*Remark.* In the lane's own couplings (T1) the alternation is not present in the generator at all, so there is nothing for the sea to lower: the sea's preference (block 82's control) is a statement about the bond-amplitude coupling only.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block83_relabelling.py`, output in `.out.txt`; disjoint machinery: dense floating-point operators in position space).

*W1 — the three couplings on `6³`, `δ = 3/10`.*

| coupling | `max |H − H_free|` | least `|E|` |
|---|---|---|
| frame (block 62) | `0` | `0` (free: `0`) |
| strain (block 64) | `0` | `0` |
| bond's own amplitude (block 82) | `0.15` | `0.5196 = √3δ` |

*W2 — a smooth random strain through block 64's coupling.* Four long-wavelength modes, `|V|` up to `0.33`: the largest matrix element inside the corner subspace is `3.8·10⁻¹⁸`; the free walk's sixteen exact zero modes become sixteen energies within `3.9·10⁻⁵` of zero (the species points move slightly with the strain and no longer sit on the torus grid); there is no gap at second order for this strain.

*W3 — the sea's energy per site on `8³`.* Bond-amplitude alternation: `−1.190, −1.200, −1.223, −1.303, −1.491, −1.732` at `δ = 0, 0.1, 0.2, 0.4, 0.7, 1`; frame-coupled alternation: `−1.190` at every `δ` (exactly the free value, as T1(a) says).


## No-Go Discipline Gate

The note's negative sentences: the alternation of the lengths is invisible to the walk in the frame and strain couplings; it costs the ledger nothing; no frame or strain pattern gives a first-order rest energy.

### N1 — Routes by which the sentences could fail or mislead
1. *Other couplings.* T1–T2 cover the couplings the lane derived (site frame; relabelling strain) and the family of field energies built from curls. A coupling that reads the bond's own amplitude is outside them; whether it is admissible is the owner's question.
2. *Second order.* T2 is a first-order statement in the corner subspace; a smooth strain could in principle gap at second order through non-corner states. The control finds none on `6³`; not proved.
3. *Non-diagonal frames and tilts.* Only stretches along the bond's own axis are alternated; tilts alternating along another axis are a different pattern (block 82 T2's stripes are their site analogue), not examined.
4. *The sea reading.* T3 concerns the one-record sea, a comparator (block 78).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even tori; `δ = 3/10` in the exact checks (the identities are algebraic in `δ`); diagonal frames.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom; the Qubit axiom | yes (premise) |
| blocks 54, 62, 63, 64 (open PRs #8570, #8592, #8593, #8595) | the walk; the frame; the relabelling and strain couplings; the field energies | yes (restated) |
| block 82 (open PR #8628) | the bond-amplitude rest energy | yes (placed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "alternation = relabelling: invisible and free; no first-order strain gap; the bond's own amplitude gaps; the sea never rises" | executed: every matrix element on `4³`; every curl | executed: `ξ` and the volume at every site | executed: corner states against generic functions; the ring's spectrum; control on `6³`, `8³` | executed: the corner block's square; the translation conjugacy | T1, T2 by proof on every even torus; T3 by concavity and evenness

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have shown the lane's coupling is gauge-invariant; of course a gauge transformation does nothing." Reply: yes — and that is the finding: the one field-based rest energy the panel put forward is, in the lane's own terms, a gauge choice. What is new is the exact identification and the corner lemma that says no strain of the lane's kind can do it at first order either. Second objection: "A bond's length should change the hop." Reply: that is a coupling to declare; it is not a relabelling's, and the note says what it would need to be.

### N8 — Cross-cycle echo
Block 63: relabellings reach second neighbours; the strain couples as a relabelling's deformation. Block 64: curls are blind to relabellings. Block 82: alternating amplitudes gap all eight species. Here: the alternation is a relabelling; the lane's walk and ledger do not see it.

## Falsifiers

- A matrix element of the frame- or strain-coupled alternation that differs from the free walk's.
- A plaquette curl of the alternation that is nonzero, or a volume sum that differs from `N`.
- A site or bond function `X` for which `½{X, S_j}` has a nonzero matrix element between corner states.
- A `δ` at which the ring of four's sea energy exceeds `−2`.

## Boundaries and non-claims

Diagonal stretches only; first order in the corner subspace; the sea as a comparator; the bond-amplitude coupling's admissibility is the owner's question. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 54, 62, 63, 64, 82 (open PRs): restated or placed.
- Named standard imports at definition level: sparse exact matrices over the Gaussian rationals; exact symbolic spectra; Ky Fan's minimum principle for sums of eigenvalues; dense diagonalisation for the control.

## Review record
Supervisor-run block, the thirty-first of the source-link direction; the second after the rest-energy panel. Lens pass, in writing, by the supervisor: a foundations lens — the panel's foundations lens proposed the alternating-length rest energy with a hop amplitude that follows the bond's length; the lane's lengths do not enter the walk that way (blocks 62–64), and the block checks the lane's own couplings first; a rigour lens — each vanishing was derived by hand (one anticommutation each) and then checked as an exact operator identity on the torus, and the corner lemma was checked against generic rational functions rather than the alternation alone. Mutation census: eight mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_rest_energy_needs_the_bonds_own_amplitude_2026_09_22.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
