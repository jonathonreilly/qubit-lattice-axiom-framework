# VERDICT: CONFIRMED WITH CORRECTIONS

The gravity-side conditional no-go is sound and is sufficient for the fixed **DERIVED** reading. Several ancillary claims require narrower scope: full reflection positivity was not proved beyond the free curvature sector; the CP result depends essentially on unbroken \(K\); the strong-CP conclusion applies only to the law-level angle, not automatically to physical \(\bar\theta\); and Hammersley–Clifford does not follow from the literal axiom without extra positivity and compatibility assumptions.

## 1. Lemma W and vDVZ

- The differentiation is correct:
  \[
  \partial_i\partial_j\log Z
  =\operatorname{Cov}(S_i,S_j)-\langle S_{ij}\rangle .
  \]
  For a finite-range or exponentially decaying source functional, \(S_{ij}(x,y)\) has the same locality, so its Fourier transform is bounded/analytic near \(p=0\). It cannot change a \(1/p^2\) residue. Thus the long-range residue comes from a covariance and is positive semidefinite. [R2-4_report.md:114](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/R2-4_report.md:114)

- For \(\theta_{\mu\nu}=\delta_{\mu\nu}-p_\mu p_\nu/p^2\) in four dimensions, \(\theta^2=\theta\), \(\operatorname{tr}\theta=3\), hence
  \[
  \theta\!:\!\theta-a(\operatorname{tr}\theta)^2=3-9a.
  \]
  Positivity gives \(a\le 1/3\).

- The PPN conversion is correct for the assumed unscreened linear response: Newtonian–Newtonian exchange is proportional to \(1-a\), while Newtonian–traceless-light exchange is proportional to \(1\). Therefore
  \[
  1+\gamma=\frac1{1-a},\qquad a=\frac{\gamma}{1+\gamma}.
  \]
  Cassini measured \(\gamma=1+(2.1\pm2.3)\times10^{-5}\), and explicitly identifies light bending/delay as proportional to \(1+\gamma\). [Cassini result](https://www.nature.com/articles/nature01997)

- `r24_source_convexity.py` reran successfully and reproduced \(a_{\rm GR}=1/2\), \(a_A=1/3\), \(\gamma_A=1/2\), and \(W_{\rm GR}(\theta)p^2=-3/2\). [r24_source_convexity.py:24](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_source_convexity.py:24) The current script also emits the acknowledged, unused `eigen-check … False` diagnostic, which is absent from [r24_source_convexity.out:1](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_source_convexity.out:1).

- \(a=1/3,\gamma=1/2\) is exactly the **vDVZ conserved-source tensor structure**. Calling model A itself “massive Fierz–Pauli in the zero-mass limit” would be stronger than shown. The \(\gamma=1/2\) identification is standard for the linear vDVZ regime. [APS discussion](https://link.aps.org/accepted/10.1103/PhysRevD.87.064001)

- Correction: W3 is an explicit **linear, isotropic, unscreened-response assumption**. Cassini does not by itself identify the vacuum two-point residue in theories with nonlinear screening. Also, dropping W2 includes not only nonlocality but a non-real/rotated metric-source bridge; therefore the three advertised prices are not exhaustive without retaining W2’s “real observable” clause.

## 2. Signature, gauge fixing, unimodular gravity, and RP

- Confirmed for every nonzero momentum of the stated Fierz–Pauli symbol. In a frame \(p\parallel e_4\), the quotient consists of a spatial symmetric \(3\times3\) tensor: five traceless directions have eigenvalue \(+\tfrac12p^2\), while its normalized trace has eigenvalue \(-p^2\). At \(p=0\) the form vanishes, so “every momentum” should read “every nonzero momentum.” [r24_graviton_quotient.py:61](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_graviton_quotient.py:61)

- The gauge-fixing argument is sound for real linear FP conditions with \(F|_{\rm gauge}\) invertible: every gauge orbit has a representative in \(\ker F\), and the negative quotient orbit remains negative there. The 2,400 numerical tests agree but are not the proof. [R2-4_report.md:96](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/R2-4_report.md:96)

- The stated linearized unimodular restriction is also correct: after \(\operatorname{tr}h=0\) and quotienting transverse diffeomorphisms, the scalar eigenvalue is \(-p^2/4\). [r24_unimodular.py:21](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_unimodular.py:21)

- The free linearized curvature two-point function is reflection-positive: an independent residue check gives nonnegative reflected residue eigenvalues \(\{1/2,3/4\}\) for GR and \(\{1/4,1/2,3/4\}\) for model A, with only simple poles. But “GR is RP” must be restricted to this **free gauge-invariant curvature sector**, not nonlinear or coupled gravity. [r24_conformal_rp.py:61](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_conformal_rp.py:61)

- Model A’s non-contact Ricci correlations show extra long-range modes and inequivalence to vacuum GR; they do **not** by themselves show that its microscopic action is nonlocal. [r24_conformal_rp2.py:23](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_conformal_rp2.py:23)

## 3. Lemma K, Jarlskog, spontaneous CP, and strong CP

- Lemma K is correct under K1–K1′. Pointwise complex conjugation preserves the OS null space, is antiunitary after reconstruction, commutes with the real transfer semigroup, and—because it is antiunitary—reverses momentum and angular momentum. Its locality statement is support locality, not necessarily an on-site linear action on every emergent field. [R2-4_report.md:219](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/R2-4_report.md:219)

- The Jarlskog conclusion is sound after making explicit the observed nondegenerate quark masses and K4’s exclusion of additional IR sectors or exotic internal actions. A nonzero basis-invariant Jarlskog quantity then excludes generalized \(CP\) combined with flavour basis changes. [Jarlskog](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.36.2128)

- K3 is essential. A positive real law can yield observed effective CKM violation if the reconstructed state spontaneously breaks the resulting \(CP/T\)-type symmetry. That is an escape, not an exhibited positive lattice Standard Model.

- Exact law-level CP sends \(\theta\to-\theta\), so the **bare law parameter** is restricted to \(0\) or \(\pi\) modulo \(2\pi\). Spontaneous CP breaking does not automatically keep the physical
  \(\bar\theta=\theta+\arg\det M\) at those values; Nelson–Barr-type structure or another alignment mechanism is additionally required. [Nelson–Barr review](https://arxiv.org/abs/hep-ph/9307214) Thus [R2-4_report.md:243](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/R2-4_report.md:243) is correct only with its “at law level” qualification.

- “SU(2)\(_L\) is vector-like” is correct only after discarding hypercharge, colour and Yukawa assignments: an even number of pseudoreal SU(2) doublets can be paired, but the full Standard Model representation remains chiral.

## 4. GW Gröbner result and Nielsen–Ninomiya

- The exact Gröbner run reproduced `{1}` for \(d=2,3,4\), including the Rabinowitsch enforcement of nonzero doubler-corner masses. [r24_gw_generalR.py:18](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/r24_gw_generalR.py:18)

- Its scope is exactly the advertised scalar-plus-vector Clifford ansatz, unit-hypercube range, hypercubic symmetry, and scalar multilinear \(R\). It is not a proof against arbitrary Clifford structures, longer-range ultralocal operators, interacting mirror-gapping constructions, or all chiral lattice theories. The published broader canonical GW no-go is consistent with the result. [Horváth](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.81.4063)

- The Nielsen–Ninomiya winding argument is correctly used only for free, translation-invariant, continuous symbols with exact on-site chirality. It is not a nearest-neighbour-specific theorem and does not close the interacting SMG route. The report itself correctly acknowledges this at [R2-4_report.md:178](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/R2-4_report.md:178).

## 5. Hammersley–Clifford

The pair-potential conclusion is valid only after adding a **globally compatible, strictly positive Markov random field** assumption. Hammersley–Clifford then factors the distribution over graph cliques, and the nearest-neighbour \(Z^4\) graph has only vertex and edge cliques. Strict positivity is indispensable. [Original Hammersley–Clifford manuscript](https://ora.ox.ac.uk/objects/uuid%3A4ea849da-1511-4578-bb88-6a8d02f457a6)

The literal axiom says only that site distributions are neighbour-determined; it does not assert strict positivity, global Gibbs compatibility, or absence of hard support constraints. [MINIMAL_AXIOMS_2026-06-29.md:57](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/MINIMAL_AXIOMS_2026-06-29.md:57) Hence “literal Admissibility allows only pair interactions” is overstated. Standard link-variable Wilson plaquettes and Grassmann integrals are outside the direct strictly-positive site-MRF representation, but auxiliary-variable, hard-constraint, or emergent-fermion realizations are not thereby excluded.

## 6. Fixed-reading labels

- **Gravity (ii): DERIVED under W1–W3.** This is enough for the fixed “(i), and/or (ii)” criterion. [TESTS.md:2582](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R2-4/TESTS.md:2582)

- **Chirality (i): SUGGESTED/open in general.** The GW and free Nielsen–Ninomiya results are bounded. Lemma K gives a derived conditional obstruction to explicit CKM CP violation only when K1–K4, especially unbroken K3, hold.

- **Price:** for a real local source bridge reproducing linear GR, positivity of the sourced Euclidean weight must be abandoned; alternatively the bridge/constraint sector must become non-real or nonlocal. Power-law canonical reduction remains SUGGESTED, and “nearest-neighbour \(\to\) quasi-local” is not derived for chirality generally.

## Strongest correct statement

Under W1–W3—a positive source-tilted measure, a real finite-range or exponentially local stress-source functional, and an isotropic unscreened \(1/p^2\) gravitational response—the singular response is a positive-semidefinite covariance residue, so the conserved trace projector forces \(a\le1/3\), equivalently \(\gamma\le1/2\); linearized GR requires \(a=1/2\), consistent with Cassini’s \(\gamma\simeq1\), and therefore cannot arise from such a positive local Gibbs realization. This earns the fixed **DERIVED** reading through gravity alone, while allowing non-real or nonlocal source/constraint bridges as explicit escapes. No class-wide chiral no-go is established: Nielsen–Ninomiya covers the free exact-chiral class, the Gröbner certificate covers the stated unit-hypercube GW ansatz, and positivity forbids observed CKM CP only when the reconstructed antiunitary symmetry is unbroken and acts within the ordinary nondegenerate Standard Model sector. The Hammersley–Clifford pair-interaction conclusion additionally requires a strictly positive compatible global Markov field and is not a consequence of the literal Admissibility wording alone.