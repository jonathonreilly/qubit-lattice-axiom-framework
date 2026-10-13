# Panel dossier: grid stretching, the grid's extra mass, and the strain-covariant critical-mass rule (2026-10-13)

## The owner's request (Jon, verbatim)

"I want a panel of physicists on this. what is grid stretching, why does the grid give extra mass, what is the size relative grid/fermion how is a fermion built on the grid etc"

Jon also pasted the supervisor's plain-language explanation back. Judge it for accuracy:

> The setup. On a grid, fermions such as electrons and quarks have a known problem: the grid tries to give them a huge mass, about the grid's own energy scale. To get light particles like the ones we see, the law includes a correction, the "critical mass", that exactly cancels this. The root already does this on the ordinary, unstretched grid.
>
> The problem we found. Stretch space slightly more in one direction than another, as a passing gravitational wave or the strain inside the Earth does. The grid's push on the fermion's mass then changes a little. The correction was set for the unstretched grid, so it no longer cancels exactly. Every fermion in the stretched region picks up a tiny leftover mass that depends on the stretch. Added up over all the matter in the Earth, that leftover acts like a heavy "drag" on gravitational waves. It is strong enough that GW170817 could not have passed through the Earth to reach the detectors, yet it did.
>
> The rule. Make the correction follow the stretch. Wherever space is stretched, the cancellation is done for that stretched grid, not for the unstretched one. In one sentence: fermions stay exactly as light as they are, however the grid is stretched.

**Owner's standard:** we only need to match observed physical outcomes, not a particular theory. Axiom or rule changes are named as prices; Jon decides adoption.

## Where things are

Repo root: `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790`. Below, `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.

- **The axioms:** `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines). Read them in full. They are the framework: qubit sites on a lattice, a local rule, and records.
- **TESTS:** `P/TESTS.md`. The section "C5 follow-up: the root's own strain law on hot matter" is near the end and covers F1–F5 with referee records. Also see the C5 closing record and R19 entries.
- **Key reports** (`P/agents/C5_<ID>_report.md`, with `_referee_verdict.md` where one exists):
  - F1: the SF-strained QED law, Hessian +2.424e-2 e². Referee: OPEN, because a unitary lift moves it through zero.
  - F2: environment bounds. GW170817 crossed 9,300–11,300 km of Earth before reaching L1 and H1; μ_ρ ≲ 1.5e-29 eV² m³/kg for the massive sign. Referee: confirmed with corrections.
  - F3: an O(t²) unitary dressing acts as a Pauli/clover-type term that moves the critical mass; zero reachable at a* = 0.014. Referee running.
  - F4: gauge-path families shift the answer by +0.4% to +6.9%; no convex zero. Referee running.
  - F5: tests the strain-covariant critical mass (P-R19-34a) as a rule. **Running; no result yet.**
  - R19-34 and its verdict: the original H-cov calculation and the definition of P-R19-34a (~line 177).
  - R19-31 and its verdict: the hot gauge/Yukawa channels and the Wilson ψ̄ψ channel.
  - R19-21 and its verdict: the canonical mapping (strain stiffness → graviton mass); the history.
  - R19-15 Lemma H (~lines 120–140): the SF strain flow, defined as a Liouville flow of each band in momentum space.
  - R16-1 and R18-9: the root's D1 fermion edge.
  - R19-24: the D1∞ / counterterm-as-clause precedent.
- **The root's fermion operator:** `P/scripts/C5/R18-5/dirac.py` (header). It is a 4-component Wilson-type band:
  - h(k) = Σ_a c_a γ_a, with c = (S_x, S_y, S_z, M) and M = m + W_x + W_y + W_z;
  - the root edge is D1(b_f, r) = (0.909103708, 0.555604226), box-exact Wilson-type;
  - 22.5 Dirac fields are placed on this one edge (S26).
- **How strain is registered (SF):**
  - each band's momenta move along its own flow v = ½h·∇(E²/2);
  - F1's interacting realization is D_t(k) = D(Φ_t(k)), the photon with flowed symbols, and Psym gauge links;
  - UD is the first-order graviton vertex.
- **Canonical mapping** (conditional; `PRICE_NOTE:22`, R19-34):
  - m_g² a² = 16π μ_SF, with μ_SF = ⟨ψ̄ψ⟩a³ × coupling × ∂²_t δm;
  - the grid spacing a is taken as the Planck length in these size estimates.
- **Price note:** `P/PRICE_NOTE.md`, prices named and not adopted. P-R19-34a is at about line 679.

## What each panelist must deliver

Work in your lens. Read the axioms in full plus whatever repo files your answer needs, and cite file:line. You may write tiny scripts in your own folder `scratchpad/C5/panel_F/<lens>/`. Keep them under 300 MB of RAM, because the machine is memory-limited. **Do not edit repository files.**

1. **Plain answers to Jon's questions, from your lens:**
   - (a) **What is "grid stretching" here?** Is it a real change in site spacing, or an effective metric field (the graviton) that changes how matter hops? Is "stretching" even meaningful on a fixed Z³ lattice?
   - (b) **Why does the grid give fermions extra mass?** Cover doublers, the Wilson term, chiral symmetry breaking, and the additive renormalization ~ e²/a. Is "about the grid's own energy scale" right, and what is the actual size here?
   - (c) **How do the grid and a fermion compare in size?** Compare the electron Compton wavelength, a quark, and a nucleon with the spacing a, if a is the Planck length. How many sites does a fermion span?
   - (d) **How is a fermion built on this grid?** Where do the 4 components and the Dirac structure come from, given that the axioms are qubit sites? Is that derived or supplied?
2. **Accuracy of the pasted explanation.** Mark what is right, what is wrong or overstated, and give a corrected version. Pay particular attention to:
   - "drag";
   - "the grid tries to give them a huge mass";
   - "what Einstein's theory already says";
   - whether "fermions stay exactly as light" is the right statement of the rule.
3. **Your verdict on the proposed rule** (strain-covariant critical mass), under the "match observations" standard: sound / sound with conditions / unsound.
4. **The strongest argument from your tradition**, and the **steelman AGAINST** your verdict.
5. **What evidence would change your mind**, and **one concrete next test**, specified.

Report in plain words first, then the technical part. Label claims proved / checked / suggested / reading / comparator. RECALLED means from memory.
