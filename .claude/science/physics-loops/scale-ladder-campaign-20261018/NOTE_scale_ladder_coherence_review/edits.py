# Proposed old -> new edits for the scale-ladder note (coherence review, 2026-10-18).
# Each old string must occur exactly once in the note; verify_edits() checks this and
# can write a patched copy to this directory (never to docs/).
EDITS = []
def E(tag, old, new): EDITS.append((tag, old, new))

# ---------- front matter / status ----------
E("F1 claim_scope item 6 tail + new items 7-8 + Not claimed",
"escapes it, and S R_link U with Clifford-phase on-site U has isolated isotropic spin-1/2 Weyl nodes at +-k* (speed sqrt2/3, chirality +-1, anisotropy ~ |q|^2) with six further anisotropic Weyl nodes at the other points (pi/2)(+-1,+-1,+-1), net chirality zero, and no other states at the node quasi-energy. Not claimed: completeness of the sampled symmetric families, any interaction or many-body statement, infinite-volume or general-L statements beyond the stated representation arguments, any coarse-graining map from a one-qubit-per-site rung producing this model, a common speed across different fields, or any physical identification.",
"escapes it; the step S R_link U_H U_Lambda (two Clifford-phase on-site factors, labels H23 and L110) has, at its node quasi-energy pi/2, isolated isotropic spin-1/2 Weyl doublets at +-k* (speed sqrt2/3, chirality +-1, anisotropy ~ |q|^2) and six uniaxial Weyl doublets at k* + pi e_i and -k* + pi e_i (speeds 0.2467 axial, 0.5837 transverse; net chirality zero), with a mirror eight-node set at -pi/2; numerically (runner coarse grid with minimum distance > 0.05, and refined searches; not a certificate) no other momentum reaches pi/2. (7) Exact (runner Part 1): the eight points (pi/2)(+-1,+-1,+-1) form the orbits {k*}, {-k*} (little group O) and two 3-point orbits k* + pi e_i, -k* + pi e_i (little group D4 about e_i, containing all three axis C2s); so in every symmetric corner Hamiltonian or step, levels there are even, a linear touching at +-k* is isotropic, and a linear touching at k* + pi e_i has a cone metric uniaxial about e_i. (8) Proved here, not independently checked (its ingredient, the global anticommutation of the dressed axis-C2 lifts, is the checked companion odd-filling theorem): if a finite-range step commuting with the translations and these two lifts has a quasi-energy gap and an exactly 2-fold, linearly split spin-1/2 doublet at k* at quasi-energy E, then E is also reached away from +-k*; the gap hypothesis is not established for the step in (6). Not claimed: completeness of the sampled symmetric families or of the step searches, any interaction or many-body statement, general-L statements beyond the stated representation arguments and the Bloch-symbol identities of (6), any coarse-graining map from a one-qubit-per-site rung producing this model, a theorem on a common speed across different fields (the campaign's conditional, leading-order constraint-closure results are in companion lane notes and are reported here as interpretation), or any physical identification.")

E("F2 status line",
"Exact statements on the L = 4 torus for a supplied model, plus representation arguments; the program sections are interpretation, not claims. Nothing is adopted.",
"Exact statements on the L = 4 torus for a supplied model, plus representation arguments and the infinite-volume Bloch-symbol identities of item 6. The program sections, the probe and campaign tables and the answer section are interpretation, not claims; the campaign's lane theorems are in companion notes. Nothing is adopted.")

E("F3 question paragraph",
"The program sections then look at the ladder from five directions and record what probes on other lanes found.",
"The program sections then look at the ladder from five directions, record what probes on other lanes found, and report what a 12-hour campaign (2026-10-18) then established. A summary opens the answer section.")

# ---------- item 6 ----------
E("I1 runner illustration number",
"Random symmetric on-site unitaries between link reflections give a largest doublet half-splitting/q of 2e−9.",
"Random symmetric on-site unitaries between link reflections give a largest doublet half-splitting/q of 4.9e−9 in the current runner, at finite-difference level.")

E("I2 symbolic-check provenance",
"satisfies M³ = (|q|²/3)M exactly (checked symbolically)",
"satisfies M³ = (|q|²/3)M exactly (checked symbolically: `B1_check/check_item6.log`; that check has a log but no REPORT.md)")

E("I3 eight-node 'clean semimetal'",
"It is reached only at the eight points (π/2)(±1,±1,±1): a refined search in exploration, and a coarse grid in the runner (minimum distance to it elsewhere > 0.05). So this is a clean eight-node Weyl semimetal at that quasi-energy.",
"Numerically it is reached only at the eight points (π/2)(±1,±1,±1). The evidence is a refined search in exploration, a 20³ grid with 25 refinements in the B17 check, and a coarse grid in the runner (minimum distance to it elsewhere > 0.05). None of these is a certificate. So, as far as tested, the step has exactly eight Weyl nodes at that quasi-energy.")

E("I4 doubler speeds (early wording)",
"The other six are anisotropic Weyl nodes (speed spread about 0.3), chiralities three +1 and three −1. The net is zero.",
"The other six are uniaxial Weyl nodes (0.2467 axial, 0.5837 transverse; see below), chiralities three +1 and three −1. The net is zero.")

E("I5 node count",
"So the step has 16 Weyl nodes in all.",
"So the step has 16 Weyl nodes at E = ±π/2. The B18 check found further Weyl doublets at the doubler momenta at four other quasi-energies (±1.1449 and ±1.9967; speeds 0.12336 axial and 0.06168 transverse).")

E("I6 uniaxial is allowed, not forced",
"         - a touching at k* + πe_i is uniaxial about e_i.",
"         - a linear touching at k* + πe_i has a cone metric that is uniaxial about e_i: isotropy there is not forced.")

E("I7 pocket-free hypothesis (1+3 form)",
"At odd filling all eight touch (B7, C20), so the forced low-energy content always has this 1 + 3 form.",
"For a pocket-free state at odd filling all eight touch the chemical potential (B7, C20), and the forced low-energy content then has this 1 + 3 form. Otherwise there are pockets.")

E("I8 corollary label",
"- **Corollary (doubling, exact).**",
"- **Corollary (doubling; proved here, not yet independently checked; its ingredient is the checked B7 anticommutation).**")

E("I9 corollary proof, last line",
"       - The same counting at odd filling forces the touchings of Hamiltonians (campaign C20).",
"       - The same counting, for a pocket-free state at odd filling, forces the touchings of Hamiltonians (campaign C20).")

E("I10 corollary explanation",
"- For Hamiltonians at odd filling the same counting gives C20's stronger pointwise obstruction: all eight points touch the chemical potential.",
"- For a pocket-free state of a Hamiltonian at odd filling, the same counting gives C20's stronger pointwise obstruction: all eight points touch the chemical potential.")

E("I11 grid evidence is not a crossing proof",
"- All of those have other bands crossing the node quasi-energy elsewhere: the best minimum distance on a 12³ grid away from ±k* is 0.007.",
"- All of those appear to have other bands crossing the node quasi-energy elsewhere (grid evidence, not a crossing proof): the best minimum distance on a 12³ grid away from ±k* is 0.007. B20's sign-change test, whose check is in progress, later proves crossings for 99.1% of a wider search.")

# ---------- program section 3 ----------
E("P1 item 5 is no longer 'what would'",
"This is the clearest place where the ladder does not supply the answer by itself. Item 5 shows what would: time on the same footing as space (see the answer below).",
"This is the clearest place where the ladder does not supply the answer by itself. Item 5 gives one sufficient route: time on the same footing as space. The campaign found a second route, constraint closure with gravity; it comes with a derivation, but one that is conditional and leading-order (see the answer below).")

# ---------- probe table (historical; mark superseded entries) ----------
E("T1 probe-table intro",
"Each verdict is the probing agent's, with its own numbers. None is checked here beyond what the runner does.",
"Each verdict is the probing agent's, with its own numbers. None is checked here beyond what the runner does. Entries the campaign later superseded are marked.")
E("T2 electron row: C20 is done",
"Mass mechanism (campaign C20 in progress; no report yet)",
"Mass mechanism (campaign C20, since done: see the follow-up table)")
E("T3 gravity row: g3",
"({1, 1.10} along [100] at g3 = 0.1)",
"({1, 1.10} along [100] at g3 = 0.1; in the repo's curvature member, constraint closure forces ε₃ = 0: campaign B4)")
E("T4 native row: 7/4 is 2D",
"matching gives τ_eff = (3/β)(1 + 7/(4β) + …)",
"matching gives τ_eff = (3/β)(1 + 7/(4β) + …) (campaign B12: the 7/4 is the 2D shift)")
E("T5 formation row",
"hence at the trivial fixed point (proof to be written)",
"hence at the trivial fixed point (proof since written and checked: campaign B3)")
E("T6 readout row",
"hence ergodicity (conditional; to be checked)",
"hence ergodicity (conditional; since checked: campaign B8)")

# ---------- campaign follow-up table ----------
E("C1 define 'independently checked'",
"Workers and checkers are fresh-context agents of the same model family, not independent human reviewers.",
"Workers and checkers are fresh-context agents of the same model family, not independent human reviewers. Here \"checked\" and \"independently checked\" mean a different code path, not a different model lineage.")
E("C2 formation scope",
"Every iid-priority, finite-range formation rule is a finitary factor",
"Every iid-priority, finite-range formation rule (iid activation times, or a fixed, state-independent rate profile; the 09-22 state-dependent rates are not covered) is a finitary factor")
E("C3 electron row: corollary, B11 provenance, closure pointer",
"The doubling corollary holds for gapped steps and odd-filling Hamiltonians. In mean-field RPA, interaction channels favour the chiral triangle term over the Dirac mass for T ≲ 0.03; at higher temperature the channel is unresolved (checked). The step is an exact depth-25 circuit on the corner code, but not Clifford+T. |",
"The doubling corollary (proved here, unchecked) holds for gapped steps and pocket-free odd-filling Hamiltonians. In mean-field RPA, interaction channels favour the chiral triangle term over the Dirac mass for T ≲ 0.03; at higher temperature the channel is unresolved (checked; C20 lane note). The step is an exact finite-depth circuit on the corner code (about 25 two-mode layers); its on-site factors are not exact Clifford+T (B11, unchecked). Constraint closure rejects its doublers (B17–B22, below). |")

# ---------- answer section ----------
E("A1 'three exact tools'",
"It gives three exact tools that every lane can use.",
"It gives three tools that every lane can use: the first two rest on exact statements, and the third is a reading.")
E("A2 fourth tool: pocket-free, uniaxial allowed",
"The gauge-dressed symmetry action forces even levels at the momenta fixed by commuting C2s, and odd filling then forces touchings at all of them. So the long-wavelength content is not free: in the corner model it is always one isotropic spin-½ pair plus three axis-labelled uniaxial pairs.",
"The gauge-dressed symmetry action forces even levels at the momenta fixed by commuting C2s, and odd filling without pockets then forces touchings at all of them. So the long-wavelength content is not free. In the corner model the forced touchings are one isotropic spin-½ pair at ±k* plus three axis-labelled pairs, whose cones are uniaxial (isotropy not forced).")
E("A3 formation reading",
"Rung-0 formation with random priorities is provably at the trivial fixed point. Any long-range structure in Records must therefore come from the Hamiltonian rung or from the start, and spatial Record frequencies are then consistent.",
"Rung-0 formation with random priorities (state-independent rates) is provably mixing, with factorially decaying correlations: the trivial fixed point, in RG language. Any long-range structure in Records must therefore come from the Hamiltonian rung, from the start, or from rules outside the class. Spatial Record frequencies then converge; they equal the rule weights only for order-blind rules (a partial, conditional discharge).")
E("A4 gravity 'precisely'",
"- **Gravity.** Every gauge-invariant kernel gives a single cone, and lattice constraint closure selects DeWitt. The open gravity item is now precisely an underived seagull, which fixes the induced 1/G.",
"- **Gravity.** Every gauge-invariant two-derivative kernel gives the two TT polarisations a single cone, and lattice constraint closure selects DeWitt (supplied clauses, leading order). The induced-gravity item is now precise: the 06-08 bubble needs an underived seagull, so the induced 1/G is not fixed. With matter, see the closure route below.")
E("A5 protection is one-fermion",
"   - Masslessness and small masses are protected.",
"   - At one-fermion level, masslessness is protected and small masses are technically natural. Interactions can escape the quartet protection (B7).")
E("A6 spin-2 isotropy superseded by B4",
"- A common speed across fields is not, and neither is spin-2 isotropy, when each field's speed is a tunable coupling.",
"- A common speed across fields is not free when each field's speed is a tunable coupling. Neither is spin-2 isotropy with Hamiltonian time and only spatial O_h (the probe's g3). In the repo's curvature member, though, constraint closure forces ε₃ = 0 (B4).")
E("A7 'third route' wording",
"**A third route to a common cone: closure of the gravity constraint algebra (campaign block B14, independently checked).**",
"#### Constraint closure (campaign blocks B14–B22)\n\n**Another route to a common cone: closure of the gravity constraint algebra (campaign block B14, independently checked).**")
E("A8 B14 cone value: normalisation-relative",
"  - every matter species is forced onto one common cone, set by the gravity coefficients (c = K/(4α));",
"  - every matter species is forced onto one common cone, set by the gravity coefficients: c = K/(4α) in block 62's normalisation (K1 = K2 = K, unit relabelling weight). The invariant form is B21's graviton cone K2/(4α);")
E("A9 B14 supplied list",
"- **Supplied:** the matter Hamiltonian, its positivity and the scalar-lapse rule. Newton's constant is not fixed.",
"- **Supplied:** the matter Hamiltonian, its positivity, the relabelling generators and their normalisation (δ_ξh = 2∂ξ; B19 and B21 say what is later derived), and the scalar-lapse rule. Newton's constant is not fixed.")
E("A10 B15 premises and doubler caveat",
"So, given K, α > 0, the Lorentzian sign follows without a positivity premise on the matter. All eight naive doublers share the cone.",
"So, given K, α > 0 and a common relabelling orientation, the Lorentzian sign follows without a positivity premise on the matter. All eight naive doublers share the cone; six of them need momentum-dependent spin structure in the lattice relabelling (B15 check).")
E("A11 B16/B19/B21 restructure: normalisation applies to all species",
"""  - Among translation-invariant timings this needs one of eight one-sided timings. Reflection-symmetric alternatives break unit translations and appear to fail elsewhere.
  - **Normalisation.** The relabelling normalisation that sets the cone is partly derived (B19, independently checked).
    - In the continuum at leading order, {G, G} and the single lapse rule force the scalar and Maxwell generators onto one structure constant. So those matter cones equal each other with no premise.
    - For spin ½ this is open. The Kosmann relabellings do not form a Lie algebra unless a triad or rotation constraint is added (companion lane note, Result 4).
    - Their value relative to the gravity coefficients additionally needs gravity's own {G, C} at order h, with a quadratic relabelling term. That bracket gives every matter cone = the graviton's TT cone, K₂/(4α). This is K/(4α) because block 62 carries one K on both curvature terms, reading block 101's quadratic Hamiltonian as the unit-lapse value of one lapse-smeared constraint. Further premises: one total constraint and relabelling, a local first-order lapse rule, and a one-derivative quadratic relabelling term.
    - On the lattice the relabellings do not close: the scalar at O(a²), Maxwell at O(a). There the normalisation is selected only in the continuum limit.
    - **Invariant form (B21, independently checked).** The canonical rescaling (h, P) → (ρh, P/ρ) preserves every bracket while moving K2/K1. So the coordinate-invariant statement is v² = K2/(4α) for every species, where K2 is the coefficient of the TT (second-order √gR) term: the matter cone is the graviton cone.
    - "K/(4α)" with the linear-curvature coefficient holds only once h is normalised as g − δ. Equivalently: unit matter coupling, structure function δ − h, DeWitt metric on δ + h, or block 62's single K. No bracket can force this normalisation unless one of these is fixed.
  - The one-sided timing forces an O(a) lattice obstruction.""",
"""  - Among translation-invariant timings supported on link endpoints and plaquette corners, this needs one of eight one-sided timings. Reflection-symmetric alternatives break unit translations and appear to fail elsewhere.
  - The one-sided timing forces an O(a) lattice obstruction.
- **What sets the cone's value, for every species (B19 and B21, independently checked).** The relabelling normalisation is partly derived.
  - In the continuum at leading order, {G, G} and the single lapse rule force the scalar and Maxwell generators onto one structure constant. So those matter cones equal each other with no normalisation premise, given one total constraint and one lapse rule.
  - For spin ½ this is open. The Kosmann relabellings close only up to an on-site rotation term, which needs a triad or rotation constraint (companion lane note, Result 4).
  - Their value relative to the gravity coefficients additionally needs gravity's own {G, C} at order h, with a quadratic relabelling term. That bracket gives every matter cone = the graviton's TT cone, K₂/(4α). This is K/(4α) because block 62 carries one K on both curvature terms, reading block 101's quadratic Hamiltonian as the unit-lapse value of one lapse-smeared constraint. Further premises: one total constraint and relabelling, a local first-order lapse rule, and a one-derivative quadratic relabelling term.
  - On the lattice the relabellings do not close: the scalar at O(a²), Maxwell at O(a). There the normalisation is selected only in the continuum limit.
  - **Invariant form (B21).** The canonical rescaling (h, P) → (ρh, P/ρ) preserves every bracket while moving K2/K1. So the coordinate-invariant statement is v² = K2/(4α) for every species, where K2 is the coefficient of the TT (second-order √gR) term: the matter cone is the graviton cone. Every "K/(4α)" above is this value in block 62's normalisation.
  - "K/(4α)" with the linear-curvature coefficient holds only once h is normalised as g − δ. Equivalently: unit matter coupling, structure function δ − h, DeWitt metric on δ + h, or block 62's single K. No bracket can force this normalisation unless one of these is fixed.""")
E("A12 B17: 09-25 walk passes the leading test only",
"  - The repo's 2026-09-25 walk passes. It is naive-type, and the invariance of Σ sin² k_j under k_j → k_j + π makes all eight species isotropic at one speed. So the closure route reproduces its α = K/4.",
"  - The repo's 2026-09-25 walk passes the leading-order cone test. It is naive-type, and the invariance of Σ sin² k_j under k_j → k_j + π makes all eight species isotropic at one speed, so the closure route reproduces its α = K/4. It passes only that test: six of its species need momentum-dependent spin structure, and exact closure fails at O(a²) (B17 check).")
E("A13 B22: premise not met for the gapless corner step",
"    - So the premise above can be met, but by a choice. It also requires the node at quasi-energy 0 (a two-step lapse for the corner step, inferred), node-relative momentum, and a branch cut inside a gap. Otherwise the smeared step has 1/r tails.",
"""    - So, of the two definitions examined, the premise can be met only by a choice, Definition B. That choice adds three conditions: the node at quasi-energy 0 (for the corner step, a two-step lapse −W², inferred), node-relative momentum, and a branch cut inside a quasi-energy gap. Without the gap, the smeared step W_N has non-summable 1/r tails for non-integer N, so it is not quasi-local.
    - **For the corner step the gap condition fails.** The step is gapless away from ±π/2 (B17 check). Its band-projected bracket still has the direction-weighted form, so B17's rejection holds at the level of the low-energy bracket. That is an inference: the step's circuit was not run with a lapse.""")
E("A14 consequence: accidental isotropy, D4 points",
"- **Consequence for the target below.** A parameter-free step can feed a closing gravity sector only if its doublers are isotropic at the ±k* speed. That takes a taste-type symmetry relating the 3-orbits to ±k*, or no doublers, which by the doubling corollary needs gaplessness or broken axis C2s.",
"- **Consequence for the target below (given B17's premise).** A parameter-free step can feed a closing gravity sector only if every species at its node quasi-energy is isotropic at one speed. Apart from accidental (non-generic) isotropy, that takes one of two things. The first is a taste-type symmetry relating the D4-point nodes to T-fixed ones. The second is having no such nodes, which by the doubling corollary needs gaplessness in quasi-energy or broken axis C2s.")
E("A15 B20 search scope",
"  - Of 69,894 parameter-free (word, node quasi-energy) pairs with up to six letters, none reaches its node quasi-energy only at isotropic cones of one speed. Each has an explicit failure witness.",
"  - Of 69,894 parameter-free (word, node quasi-energy) pairs with up to six letters and a linear spin-½ Weyl doublet at k*, none reaches its node quasi-energy only at isotropic cones of one speed. Each has an explicit failure witness. Four-fold (Dirac-type) levels at ±k* were outside this screen.")
E("A16 B20 lemma labels",
"  - Exact lemmas for this word class:",
"  - Lemmas for this word class (the worker's proofs; the check is in progress):")
E("A17 B20 chirality is conditional",
"    - the 3D winding vanishes for every word, so with the Floquet Nielsen–Ninomiya theorem the net chirality at any node quasi-energy is zero;",
"    - the 3D winding vanishes for every word (exact). With the Floquet Nielsen–Ninomiya theorem (Bessho–Sato 2021, checked at abstract level only), the net chirality at any point-node quasi-energy is then zero (conditional);")
E("A18 B20 L4 scope",
"    - isotropy is symmetry-forced only at momenta whose little group contains T. The cube doublers and the X- and M-type points have only D4.",
"    - isotropy is symmetry-forced only at momenta whose little group contains T (T-fixed points found exhaustively on a (π/8)Z³ grid). The cube doublers and the X- and M-type points have only D4.")
E("A19 B20 continuous-phase control",
"Moving it off the node quasi-energy with continuous phases opens Fermi pockets instead.",
"Moving it off the node quasi-energy with continuous phases (a control, not parameter-free) opened Fermi pockets in every tested case; there is no counting proof.")
E("A20 information-minimal target: status",
"- full octahedral symmetry at the node pushes anisotropy to (a/w)².",
"- full octahedral symmetry at the node pushes anisotropy to (a/w)².\n- **Status after the campaign:** no parameter-free step found so far meets the closure selection rule (B17, B18; the B20 check is in progress), because each has anisotropic species at its node quasi-energy.")
E("A21 'anisotropic' doublers in item-6 summary",
"Like naive lattice fermions, they come with doublers: six anisotropic Weyl nodes at the other cube points.",
"Like naive lattice fermions, they come with doublers: six uniaxial Weyl nodes at the other cube points.")
E("A22 corollary scope; 'every Weyl step found'",
"The doubling corollary settles the open problem for gapped steps and odd-filling Hamiltonians: with the axis C2s, the doublers are forced, as in Nielsen–Ninomiya. The minimal clean form puts them at the other six cube points. The remaining escape routes are steps gapless in quasi-energy, which is the case for every Weyl step found, or giving up the axis C2s.",
"The doubling corollary settles the question for gapped steps and pocket-free odd-filling Hamiltonians: with the axis C2s, the doublers are forced, as in Nielsen–Ninomiya. The minimal clean form puts them at the other six cube points. The remaining escape routes are steps gapless in quasi-energy, as the eight-node step appears to be (B17 check, numerical; not tested across the searched families), or giving up the axis C2s.")
E("A23 redundancies after B14-B19",
"- **Exact redundancies at the coarse rung.** Gauss is exact; diffeo is only locus-closed.",
"- **Exact redundancies at the coarse rung.** Gauss is exact. Diffeo is only locus-closed, and the lattice relabellings close only at leading order: O(a²) for the scalar and O(a) for one-sided Maxwell (B14, B16, B19).")

# ---------- structure: subheadings in the answer section ----------
E("S1 heading: common cone",
"**The answer the probes converge on.**",
"### The common light cone\n\n**The answer the probes converge on.**")
E("S2 heading: target",
"**The information-minimal target.**",
"### The information-minimal target and its status\n\n**The information-minimal target.**")
E("S3 heading: open",
"**The other shared primitives the ladder isolates.**",
"### What stays open\n\n**The other shared primitives the ladder isolates.**")

# ---------- check, gate, references ----------
E("K1 independent-check heading scope",
"## Independent check\n",
"## Independent check (original note, items 1–5)\n")
E("K2 item 6 check provenance",
"- **Lane table.** Four rows were corrected against the probe reports.",
"""- **Item 6: checked in parts, by campaign checkers (fresh-context, same family).**
  - B1_check (log only, no REPORT.md) covers the minimal automaton, the reflection step (H_link² = 2, M³ = (|q|²/3)M, the six-fold node) and the constant-spectrum lemma.
  - B17_check and B18_check re-derived the eight-node step's cones, chiralities and second node set.
  - The anticommuting C2 lifts are B7-checked.
  - The doubling corollary's argument and the 1 + 3 orbit statement (runner Part 1) have no independent check.
- **Lane table.** Four rows were corrected against the probe reports.""")
E("N1 no-go gate N6/N7",
"  - A common speed across fields is not addressed.",
"  - A common speed across fields is not a theorem of this note. The campaign's closure results on it are conditional, leading-order and in companion lane notes.")
E("R1 misplaced citation (remove)",
"- **Multifold fermions.** Bradlyn et al., Science 353, aaf5037 (2016).\n  - Almheiri, Dong and Harlow, JHEP 04 (2015) 163.",
"- **Multifold fermions.** Bradlyn et al., Science 353, aaf5037 (2016).")
E("R2 misplaced citation (re-insert) + campaign prior art",
"  - Swingle, PRD 86, 065007 (2012).",
"  - Swingle, PRD 86, 065007 (2012).\n  - Almheiri, Dong and Harlow, JHEP 04 (2015) 163.\n- **Constraint closure and a universal cone (campaign B14–B22; as cited in the check reports).** Teitelboim 1973; Hojman, Kuchař and Teitelboim 1976; Kuchař 1974–76; Schwinger, Phys. Rev. 130, 800 (1963); Deser 1970; Barbour, Foster and Ó Murchadha 2002.\n- **Taste symmetry and Floquet doubling (campaign B18, B20).** Kogut and Susskind 1975; Karsten and Smit 1981; Golterman and Smit 1984; Bessho and Sato, PRL 127, 196404 (2021), checked at abstract level only.")
E("R3 new-here list",
"  - The doubling corollary for gapped steps with anticommuting axis-C2 lifts.",
"  - The doubling corollary for gapped steps with anticommuting axis-C2 lifts.\n  - The symmetry-forced 1 + 3 node pattern at the eight cube points.")
E("V1 runtime",
"(about three minutes)",
"(about two to three minutes; 1 min 52 s in the coherence review)")

SUMMARY_ANCHOR = "## Answer to the question (interpretation)\n\n"

import sys, pathlib
NOTE = pathlib.Path("/home/user/qubit-lattice-axiom-framework/docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md")
def verify_edits(write_copy=None, summary=None):
    s = NOTE.read_text(); bad = 0
    for tag, old, new in EDITS:
        n = s.count(old)
        if n != 1: print(f"[FAIL] {tag}: old occurs {n} times"); bad += 1
    print(f"{len(EDITS)} edits, {bad} with non-unique/missing old strings")
    if write_copy and not bad:
        t = s
        for tag, old, new in EDITS: t = t.replace(old, new, 1)
        if summary: t = t.replace(SUMMARY_ANCHOR, SUMMARY_ANCHOR + summary + "\n\n### Detail\n\n", 1)
        pathlib.Path(write_copy).write_text(t); print("patched copy:", write_copy)
    return bad
if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    summ = (here / "summary_block.txt").read_text().rstrip("\n") if (here / "summary_block.txt").exists() else None
    sys.exit(verify_edits(write_copy=str(here / "patched_note_preview.txt"), summary=summ))
