# VERDICT: CONFIRMED WITH CORRECTIONS

The overall **INCONCLUSIVE** reading is right. Results A and parts of B/Lemma 1 survive, but the advertised scattering no-go does not: Lemma 2 needs an additional global integrability/domain premise, and Lemma 4 is substantially narrower than its theorem statement.

## Findings

1. **Result A — confirmed, with three corrections.**

   Rerunning `r74_two_species.py` reproduced all cached values exactly. An independent rational-arithmetic calculation also gave zero residual for both identities and for \(d(\sum_xP_j)/dt\). The exact convention implemented is
   \[
   \dot T_{00}(x)=c_s^2\sum_j[P_j(x)-P_j(x-e_j)],\qquad
   \dot P_j=G[T]_j .
   \]
   Thus the factor \(J_E=c_s^2P\), the symmetric stress, and conservation of total \(P\) are correct, but the prose sign \(\dot T_{00}=-\mathrm{div}J_E\) is opposite to the code’s defined backward divergence. See [r74_two_species.py:53](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/scripts/r74_two_species.py:53>), [R7-4_report.md:64](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:64>).

   Scaling the shift source from \(P\) to \(a_sc_s^2P\) correctly changes the RN-L1 closure value to
   \[
   c'_s=-\frac{\kappa a_sc_s^2}{J}.
   \]
   The observable formulas also check:
   \[
   \gamma_s=\frac{c_s^2}{c_g^2},\qquad c_g^2=Jg,
   \]
   and slow acceleration is \(-a_sc_s^2\nabla n\). See [R7-4_report.md:71](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:71>), [RN_L1_referee.md:28](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/RN_L1_referee.md:28>).

   Two numerical-wording corrections remain:

   - \(0.69\) is the differential acceleration normalized to species A, not the conventional symmetric Eötvös parameter, which would be \(2(1.69-1)/(1.69+1)\simeq0.513\); see [r74_two_species.py:93](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/scripts/r74_two_species.py:93>).
   - T4 is not established as a compulsory counterterm tuning. The supplied RN-L1 referee constructs a coefficient-determined local seagull that exactly cancels the free scalar’s uniform-strain susceptibility; extending it to a full nonconstant-\(h\) algebra remains open. See [RN_L1_referee.md:11](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/RN_L1_referee.md:11>), versus [R7-4_report.md:106](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:106>).

2. **Result B — correct only conditionally.**

   For nondegenerate energy-exchanging scattering with sharp asymptotic bands, full-support regular collision shells, and an additive conserved source charge, energy exchange forces a common \(a_s\); conservation of \(a_s\omega_s\nabla\omega_s\) then forces a common \(a_sc_s^2\), hence equal \(c_s^2\). This agrees with RC-C1 along connected mutual-scattering edges. It is not a theorem about every interaction: separately conserved sectors, exceptional/integrable charges, interspecies-only scattering, gapless continua, and an independently coupled interaction-energy density are not covered. See [R7-4_report.md:113](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:113>) and [RC_C1_referee.md:9](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/RC_C1_referee.md:9>).

3. **Lemma 1 — confirmed as a formal common-core identity, not yet as an integrated boost charge.**

   Given regular local/transfer-regular cohomology, decay or suitable boundaries, and states with finite first energy moment, constraint preservation gives
   \[
   i[H,D]=J,\qquad [H,J]=0.
   \]
   Strictly, \(D\) is not conserved; the time-dependent combination \(D-tJ\), up to sign convention, is. Nor does the commutator identity prove that \(D\) is essentially self-adjoint or exponentiable. The cited curl-plus-constant theorem is rigorous at finite range and needs the extra transfer-regular hypothesis for the report’s full quasi-local class. See [R7-4_report.md:123](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:123>) and [RC_C1_referee.md:5](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/RC_C1_referee.md:5>).

4. **Lemma 2 — not confirmed from H1–H4 as written.**

   The Cook argument establishes all-rapidity invariance only after adding:

   - essential self-adjointness of \(D\) and \(D_0\);
   - common invariant cores and domain preservation by the wave operators;
   - norm-controlled decay of both \(D-D_0\) and \(t(J-J_0)\);
   - strong Møller intertwining, not merely a quadratic-form commutator;
   - sufficient regularity of \(\omega\) to define the first-order generator—mere continuity in H1 is insufficient.

   Under those strengthened assumptions, \(S\) strongly commutes with \(D_0\), hence with \(e^{isD_0}\) for every \(s\). Without them one has, at most, a generator identity on a restricted domain. See [R7-4_report.md:133](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:133>).

   R7-1 deliberately occupies the missing-domain escape: its generators are globally self-adjoint, but the Poincaré identities hold only on the box domain and are expressly not required to integrate there; the continuum action agrees only until the state-dependent rapidity budget \(\eta_*\). See [R7-1_report_unrefereed.md:33](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-1_report_unrefereed.md:33>), [R7-1_report_unrefereed.md:105](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-1_report_unrefereed.md:105>), and [R7-1_report_unrefereed.md:171](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-1_report_unrefereed.md:171>). Thus Lemma 2’s decisive premise is the same global exponentiation/integrability wall used by B1 Theorem U, although identifying the stress bridge with this flow is a useful new application.

5. **Lemmas 3–4 and numerics — Lemma 3 is conditionally correct; Lemma 4 is not proved at theorem scope.**

   Both numerical scripts reproduce their cached outputs exactly: continuum \(0/12\), SLAC \(12/12\), SMTH \(12/12\), random directions \(8/8\), and KG \(10/10\). See [r74_boost_flow.out:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/scripts/r74_boost_flow.out:1>) and [r74_kg_flow.out:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/scripts/r74_kg_flow.out:1>).

   If full \(U_s\)-invariance is granted, Lemma 3 is sound, and it gives a genuine bounded result: a nonzero amplitude supported in a proper momentum box cannot be invariant because the positive flow exits that box.

   Lemma 4 supports only:

   - generic SLAC \(2\to2\) configurations, modulo simultaneous face crossings;
   - smooth bands under the additional rational-independence hypothesis;
   - generic nearest-neighbour KG configurations.

   Numerically distinct periods do not establish rational independence, the \(n\to m\) extension is unproved, and “vanishes on an open dense set” does not imply “only forward/exchange survives” without continuity or unique-continuation assumptions on the reduced amplitude. Flat/resonant bands, degeneracies, singular shell-supported amplitudes, and exceptional invariant submanifolds are not excluded. Compare [R7-4_report.md:155](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:155>) with the broader theorem at [R7-4_report.md:172](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/R7-4_report.md:172>).

6. **Reading — INCONCLUSIVE overall; one bounded positive result and one conditional bounded FAIL.**

   The tuned free-scalar pair is a valid linear-order existence result: choosing \(a_A=a_B\) and \(c_A=c_B=c_g\), while allowing different masses, gives a universal tuned coupling, \(1/r\), and \(\gamma=1\). If the fixed PASS line is read purely existentially at linear order, that is a narrowly bounded PASS witness; it does not derive universality, cover energy-exchanging matter, or close the \(O(\kappa)\)/nonlinear algebra. The full campaign question therefore remains **INCONCLUSIVE**, consistent with [TESTS.md:3368](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R7-4/TESTS.md:3368>).

   A genuine bounded FAIL is available only for the strengthened class with a globally self-adjoint, exponentiating first-moment charge, domain-compatible Møller intertwining, short-range clustering, and box-supported scattering: that class has zero nontrivial box-supported \(T\)-matrix. It does not exclude R7-1’s local rapidity-limited algebra or general lattice scattering. The broad FAIL fails the no-go stress test because self-adjoint integrability is hidden, \(2\to2\)/generic conclusions are lifted to all scattering, and live routes remain through local rapidity domains, long-range/infraparticle sectors, noncompact fibres, resonant/touching bands, and non-quasi-local densities.

## Strongest correct statement

For the fixed 09-14 weak N-type constraint pair, two decoupled nearest-neighbour scalar species admit an exact linear-order lapse/shift bridge with \(J_E=c_s^2P\), symmetric stress, \(c'_s=-\kappa a_sc_s^2/J\), a lattice \(1/r\) limit, and \(\gamma_s=c_s^2/c_g^2\); universality and \(\gamma=1\) are obtained only by imposing equal couplings and a common matter–graviton cone, while generic connected energy-exchanging scattering would force equal couplings and speeds only under the regular collision-invariant hypotheses. Constraint preservation supplies the formal common-core relations \(i[H,D]=J\) and \([H,J]=0\), but it does not itself supply a self-adjoint globally exponentiating \(D\) or domain-compatible scattering intertwiner. With those additional global assumptions, every proper box-supported scattering amplitude is indeed excluded, so the R6-1/R7-1 box interaction cannot be a global exact stress bridge; R7-1 evades that result by asserting only a local algebra up to a rapidity budget. The reproduced SLAC, smooth-band, and KG numerics support this conditional obstruction but do not prove the advertised “only forward or exchange” theorem for arbitrary compact-zone matter, leaving the full R7-4 question **INCONCLUSIVE**.