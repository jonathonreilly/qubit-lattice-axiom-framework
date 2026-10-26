---
claim_id: relay_energy_as_local_odds_frequency_bounded_theorem_note_2026-10-21
claim_type: open_gate
claim_scope: "Finite diagnostics of a supplied squared-amplitude-weighted principal-phase statistic and fully weighted burn/transfer stress assignment. Exact conservation, continuum balance and physical-energy identification remain open."
runner: scripts/relay_energy_as_local_odds_frequency_2026_10_21.py
---

# Local principal-phase statistic: finite packet diagnostics

Claim type: open_gate.
Primary runner: `scripts/relay_energy_as_local_odds_frequency_2026_10_21.py`.

The filename and claim identifier are historical handles. This note records finite numerical evidence, not a theorem. The walks, state carriers, coins, packets and diagnostic rules are supplied; no axiom or candidate-law clause fixes them.

## Definition and conventions

For direction amplitudes psi_d at a site and next-tick amplitudes psi'_d, set P_d=|psi_d|^2, rho=sum_d P_d+delta and

    eps = sum_d P_d [-Arg(psi'_d conjugate(psi_d) + delta)] / rho,
    delta = 1e-300.

Arg is the principal phase used by NumPy, with its signed-pi branch convention; the tick is one dimensionless time unit. This is squared-amplitude weighting, not a continuous Hamiltonian expectation or an identified physical energy. The statistic may be negative. A constant common phase cancels in the product. A time-dependent uniform phase changes its reading by the negative phase increment, modulo branch wrapping. When an old nonzero amplitude has zero next amplitude its mathematical phase advance is undefined; adding positive delta sets the numerical product phase to zero. The same convention sets zero-old-amplitude products to zero; tiny nonzero products are also perturbed. These choices are part of the diagnostic.

All source terms use this same signed eps. With post-coin weights P1, D=P1-P, pos=max(D,0), neg=max(-D,0), supplied ordered flux and stress are

    F_ab = 2 eps P_a P_b/rho
           + eps neg_a pos_b/(sum_c pos_c + delta),   a != b;
    F_aa = 0;
    sigma_ij = -sum_ab F_ab (d_b-d_a)_i (d_b-d_a)_j / 4;
    force = eps sum_d D_d d;
    burn_ij = eps sum_d P1_d d_i d_j.

For two directions +-1 the scalar F is 4 eps P+ P-/rho + eps |D+| and sigma=-F. This consistently weights the transfer term as well as redraw, force and burn. It repairs the earlier mixed assignment. For normalized P=(.7,.3), D=(-.1,.1), eps=.2, the exact scalar stress is -.188; the earlier unweighted transfer gave -.268. Because eps can be negative these are signed algebraic assignments, not nonnegative transition probabilities.

## Finite domains and measurements

The 1D run is a periodic N=6000 grid with two components, coin exp(-i*.05*sigma_x), and opposite one-site shifts. Fourier packets have envelope exp(-(k-.06)^2*width^2/2), widths 30,60,120, and cutoff envelope>1e-9. At each retained mode the positive principal-eigenphase eigenvector is chosen and its first-component phase fixed; the packet is centered by exp(i*k*N/2) and normalized. The total statistic sum(eps*rho) is measured at t=0,...,160, using the next tick for the phase. Its observed ranges are 1.1e-4, 1.8e-5 and 1.2e-6. Mean values are .079640, .078450 and .078175; the supplied spectral mean frequencies are .079721, .078460 and .078175. Finite spread is not exact conservation.

The 1D residual samples t=70,...,89 with periodic Gaussian smoothing width/2 and centered spatial differences. It is sqrt(sum|smooth(force)+div(smooth(sigma))|^2 / sum|div(smooth(burn))|^2), summed over the stated sites/ticks. With the fully weighted assignment its values are .0820, .0145 and .0044.

The 3D runs are periodic L^3 grids (width,L)=(3,32),(5,40),(8,56), with six directions +-x,+-y,+-z. The coin is exp(-i*.3*M), where M=R-P+2I, R connects opposite directions and P connects perpendicular directions. A band is selected near eigenphase .3 at |k|=.02 in direction (1,1,0), then tracked by maximal eigenvector overlap through 60 points to |k|=.3. Fourier Gaussian packets use cutoff>1e-6; at each retained mode the eigenvector of largest overlap with the central vector is phase-aligned, centered at floor(L/2) and the full packet normalized. Evolution lasts 16 ticks; residual sampling uses t=6,...,9, with the same smoothing and centered differences. The fully weighted residuals are .147, .084 and .053. The simultaneous changes in width and grid size and selected finite windows do not establish a continuum or asymptotic law.

## Controls and open obligations

The runner checks the chosen transfer weighting against exact rational two-direction algebra and its six-direction embedding, and checks phase sign, constant phase cancellation, time-dependent phase shift, branch wrapping and the explicit zero-product convention. Trend thresholds only describe the selected runs. Failed original sign/redraw mutants and the original transfer-weight variant are preserved in the review evidence; original trend PASS did not validate the transfer factor.

Exact conservation of this phase statistic, an asymptotic leading-gradient or continuum balance, and a bridge to physical energy remain open. No field equation or derivation of these supplied rules is established. This note assigns no audit or retained status.
