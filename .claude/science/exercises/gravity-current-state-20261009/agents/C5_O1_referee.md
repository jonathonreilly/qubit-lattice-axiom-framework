# VERDICT: NOT CONFIRMED

The computations and most elementary group-theoretic lemmas survive, but the report’s two headline conclusions do not: O1-N imports an unproved universal natural-size premise through H2, and the claimed counterexample addresses only dimension-four matter, not the registered matter-plus-gravity claim. Those are substantive, not editorial, corrections.

## 1. Lemmas A–E and scripts

- All four scripts reran successfully and reproduced their `.out` files byte-for-byte. I also independently recomputed the finite-group dimensions using character averages and obtained the same \(V,S_2,S_3,S_4,\mathrm{MASS},\mathrm{KIN}\) counts. The axioms’ group gives \((V,S_2)=(1,2)\), \(B_4^+\) and \(W(B_4)\) give \((0,1)\) and \(3/9\) mass/kinetic forms, and the arrow-preserving subgroup gives \((1,2)\). [o1_invariants.out:2](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/o1_invariants.out:2)

- Lemma A’s tensor implication \(V_2^{\rm tl}=0\Rightarrow V_1=0\) is correct. Its “operator is allowed iff” wording is only a geometric criterion: it presupposes that no additional exact internal, chiral, custodial, gauge-representation or selection-rule constraint forbids that particular operator. `O1_report.md:78-86`.

- The continuum counts \(2\) mass and \(4\) kinetic forms are correct, but the implementation is a floating-point SVD, not the “exact Lie-algebra null space” claimed in the report. [o1_continuum_counts.py:21](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/o1_continuum_counts.py:21)

- Lemma B is correct only with its restrictive premise that every symmetry fixes or reverses the chosen evolution generator. Its title, “a real-time law has a preferred frame,” is false in general: Lorentz boosts are symmetries of Hamiltonian laws but do not commute with \(H\). The premise at `O1_report.md:108` already excludes ordinary boosts; the universal consequence at `:112` therefore does not follow from “real time” alone.

- Lemma C is correct. Corollary C′ is also correct after adding to its statement the condition used in its proof: covariance must preserve a norm of the nonzero kernels, such as through a unitary internal action. `O1_report.md:120-137`.

- The script does not generate the full \(O(1,3;\mathbb Z)\) as stated. Every displayed generator preserves the future time component, so they generate at most a time-orientation-preserving subgroup; time reversal is absent. This does not invalidate the computed \(V=0,S_2=1\) result for that subgroup. The further phrase “Lorentz-clean at every rank” was not tested or proved. [o1_lorentz_lattice.py:16](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/o1_lorentz_lattice.py:16)

- Lemma D’s abstract connected-group theorem is correct with strong continuity. Its physical conclusion is too strong: it establishes only that a connected microscopic symmetry normalizing \(\mathbb Z^d\) acts trivially on that translation group. The report itself acknowledges the emergent-momentum loophole at `O1_report.md:150`. “Therefore a continuum fibre and a violation of Qubit” imports B1/I1 assumptions; I1 expressly proved only a one-particle statement, not an infinite microscopic on-site Hilbert space. [TESTS.md:1402](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/TESTS.md:1402)

- Lemma E is correct for an invariant **proper convex** future cone or half-space. Convexity, which the averaging proof uses, should be in the statement. `O1_report.md:155-163`.

## 2. Theorem O1-N and H2

O1-N is not DERIVED as written. `O1_report.md:167-181`.

H2’s first sentence is a familiar Wilsonian naturalness heuristic, but it is not a sufficient mathematical definition of “no tuning.” The existence of an allowed invariant tensor does not establish:

1. that every species coefficient is nonzero;
2. that every independent relative-speed combination is of order \(10^{-2}\);
3. that no additional exact symmetry correlates or removes coefficients; or
4. that the observations listed span every allowed tensor direction.

The \(6\!-\!9\times10^{-3}\) premise comes from two specific lattice-QED regulators. The F2 referee explicitly classified the result as regulator-specific, not a universal lower bound for preferred-frame theories. [C4_F2_referee.md:53](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/C4_F2_referee.md:53)

A defensible conditional theorem would have to assume explicitly that every independent observable relative-speed direction allowed by all exact symmetries has a known lower natural-size bound exceeding observation. Under that stronger assumption, \(V_2^{\rm tl}=0\) becomes a sufficient symmetry-protection condition and a stipulated necessity—not an observationally derived theorem.

“Every pair of species needs tuning” is also inaccurate: with \(N\) scalar speeds there are \(N-1\), not \(N(N-1)/2\), independent relative-speed directions. F2’s eight-matter-plus-graviton count is bookkeeping, and not all directions have independent observational bounds. `C4_F2_referee.md:37-42`.

## 3. The REFUTED claim versus F2’s scope

The registered claim included matter bounds **and GW170817**, and asked about complete substrate classes. [TESTS.md:2330](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/TESTS.md:2330)

The report silently narrows this to “matter at dimension \(\le4\)” at `O1_report.md:29,257`. F2 proves \(\Delta(1)=0\) only when the action, masses and regulator all respect \(W(B_4)\). [C4_F2_referee.md:31](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/C4_F2_referee.md:31) Gravity still carries K1’s gauge-restoration codimension, while a coupled reflection-positive chiral matter-plus-gravity construction has not been exhibited.

Therefore:

- **REFUTED:** “The continuous Lorentz group itself is necessary to protect dimension-four matter kinetic terms.”
- **Not refuted:** “Only Lorentz-in-law complete substrates avoid all matter-and-gravity tuning.”
- The original registered claim remains **INCONCLUSIVE/open**, not REFUTED.

## 4. Class table and cited costs

The table is useful as a candidate taxonomy, but it is neither exhaustive nor uniformly “refereed.” `O1_report.md:204-214`.

- **I:** The specific continuous-time QED tuning is correctly cited. The claimed \(Z^3\times\mathbb R\) total \(\ge6\) is explicitly an unrefereed assembly. [PRICE_NOTE.md:311](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/PRICE_NOTE.md:311)

- **II:** Matter protection is correct under whole-action hypercubic symmetry. K1’s \(11=3+8\) is a full linearized gauge-restoration operator codimension, not eleven measured graviton-speed tunings or a GW170817 count. “Four tastes” and leapfrog instability are implementation-specific rather than class-wide. [C4_K1_referee.md:3](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/C4_K1_referee.md:3)

- **III:** The RZ exclusion is accurately bounded to stable scalar-layer readouts, regular finite emissions and a shared \(\ell_k\); edgeless sources and the photon bridge remain open. `TESTS.md:2129-2154`.

- **IV:** “Continuous translations and continuum fibre” is conditional on microscopic normalization and B1/I1 assumptions. Calling this a demonstrated Qubit price overstates the one-particle result. `PRICE_NOTE.md:364`.

- **V:** E1/E2 exclude their stated spectator-gravity and weakly coupled examples, not all strong-dynamics or emergent-gravity mechanisms. `TESTS.md:1527-1539`.

- **VI:** Correctly left open.

- **VII:** Correctly left open, but the \(10^9\) and \(10^{38}\!-\!10^{39}\) hierarchies were established only for explicit RF3 subcases, not every sequestered realization. `TESTS.md:1589-1600`.

The “possible only for \(\alpha\)-\(\delta\)” claim at `O1_report.md:189-193` is consequently not a proved classification.

## 5. Bound numbers

Most fetched numbers and the arithmetic are correct:

- \(2.66449\times10^{-19}\) for 1.4 PeV photon survival and the \(3.116\times10^{-17}\) electron–photon ratio are correct. [LHAASO observation](https://www.nature.com/articles/s41586-021-03498-z)
- The dimension-five and dimension-six LHAASO limits are correctly transcribed. [LHAASO LIV](https://arxiv.org/abs/2106.12350), [GRB 221009A](https://arxiv.org/abs/2402.06009)
- The GW170817 interval and conditional \(7\times10^{-14}\)–\(3\times10^{-13}\) ratio are correct. [GW170817/GRB 170817A](https://arxiv.org/abs/1710.05834)
- Hohensee, IceCube and neutron-comagnetometer orders are correctly quoted, subject to the report’s stated combination/projection qualifications. [Hohensee](https://arxiv.org/abs/0904.2031), [IceCube](https://arxiv.org/abs/1303.5843), [Smiciklas et al.](https://arxiv.org/abs/1106.0738)

Corrections:

- The \(6\times10^{-20}\) UHECR result is not a clean “proton–photon per-species” bound. The source uses a 212 EeV event with a conservative **52 GeV iron-nucleus** mass and notes that hadronic applications of its point-Dirac model are indicative. The conditional tuning arithmetic is correct, but the physical label is too strong. [Klinkhamer–Schreck](https://arxiv.org/html/0809.3217)

- The dimension-six lattice scale is inverted in `o1_bounds.py:28-30`. If the coefficient is \(a^2p^4/12\), then \(E_{\rm QG}=\sqrt{12}/a\), not \(1/(\sqrt{12}a)\). At \(a=\ell_{\rm Pl}\), the pass is about **7.76 decades**, not 6.68. The qualitative conclusion remains unchanged. [o1_bounds.py:28](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_O1/o1_bounds.py:28)

- The neutrino paper uses \(\delta=v^2-1\), so identifying it directly with \(v-1\) carries an order-one convention factor.

- The \(k_{AF}\sim6\times10^{-43}\,\mathrm{GeV}\) entry remains only partially verified and should stay non-load-bearing.

## 6. Reading labels

- **DERIVED:** finite invariant counts; \(V_2^{\rm tl}=0\Rightarrow V_1=0\); Lemma C; abstract Lemma D; Lemma E after adding proper convexity; K1’s form counts.
- **DERIVED only after correction:** C′ with norm-preserving covariance; Lemma B under its explicit commuting-evolution premise.
- **SUGGESTED/conditional, not DERIVED:** O1-N; the restricted “only four exits” no-go; Lemma D’s continuum-fibre/Qubit consequence; universal per-species loop sizes; the graviton natural-size ratio.
- **REFUTED correctly:** a uniform \(10^{-20}\) bound “per species”; necessity of continuous Lorentz symmetry for dimension-four matter protection.
- **REFUTED incorrectly:** the original registered full matter-plus-gravity “only Lorentz-in-law substrates” claim.

## Strongest correct statement

Under the geometric-EFT hypotheses, \(V_2^{\rm tl}=0\) is a sufficient symmetry condition for forbidding dimension-four preferred-tensor speed operators, and it implies \(V_1=0\); the axioms’ proper-cubic group has \((V,S_2)=(1,2)\), while \(B_4^+\) and \(W(B_4)\) have \((0,1)\), so a genuinely hypercubic whole matter law can protect dimension-four matter kinetic terms without continuous Lorentz symmetry. In the specific F2 continuous-time lattice-QED realization, the generated electron–photon split is \(8.55\times10^{-3}\), requiring a relative counterterm of about \(3.1\times10^{-17}\), whereas \(\xi=1\) removes that split exactly. This establishes a severe regulator-specific matter naturalness problem and a valid finite-symmetry matter counterexample, but not a universal necessity theorem, not one tuning for every species pair, and not a counterexample to the registered complete matter-plus-gravity claim.