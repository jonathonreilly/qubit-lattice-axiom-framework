# Distinct check: mediated-source linear energy mass

Conditional support for the local Taylor diagnostic; no correction to the target calculation is required. The exact source-coordinate linear mass and ratio inequality follow. This does not validate the incorrect port-installation wording in the originally pinned stationary ancestor, or establish a loaded spectral/dynamical theorem.

## Reconstruction

I read the complete target and refreshed the complete stationary three-mediator and isolated-mediator sources. For the internal adjacency A_l, the genuine gap a=J-q>0 gives an analytic resolvent for complex |z|<a. Differentiating (zI+A_l)^-1 gives -A_l^-2 at zero. Chiral symmetry removes the diagonal even powers and the off-diagonal odd powers. The endpoint inverse-square diagonal is

    d_n=J^-2 sum_{r=0}^{n-1}(q/J)^(2r).

Thus s_l(z)=-gamma_l^2 d_n z+O(z^3), while t_l(z)=t_l(0)+O(z^2). This derivative sign is essential: the eliminated E-H equation subtracts Sigma, so it has positive coefficient 1+c_l, not 1-c_l. The fixed endpoint sign gauge affects the hopping signs but not these diagonal coefficients.

Summing the contributions of the two incident mediator edges at the shared source endpoints gives exactly

    Z_s=diag(1+c1, 1+c1+c2, 1+c2+c3).

All entries exceed one. At any fixed finite lengths and positive supplied coefficients, the constant invertible congruence diag(Z_s^-1/2,I_background) makes the source linear coefficient the identity. It scales the constant source off-diagonals by the corresponding two endpoint factors and the source-to-port off-diagonal by the s2 factor only. Hence the three effective magnitudes in the target are correct. The higher Taylor remainders are still present after this congruence; it is not an exact constant-Hamiltonian reduction or an isometric transformation of physical preparation and norms.

The port coefficient c3 z survives unchanged because the congruence leaves the background coordinates fixed. Scaling the port too would rescale all its contacts and the physical port Green-function relation. It cannot preserve the old background by notation. This is a local scalar Taylor statement at z=0 (or the selected shared-fiber channel there); it is not a Taylor replacement of complementary physical channels at their nonzero D values, nor a full noncommuting loaded-inverse theorem.

For n1=n2 and gamma2/gamma1=8^(1/4), the same d_n occurs in c1 and c2, so c2=sqrt(8)c1. The exact stationary bare ratio has (a2/a1)^2=8. Therefore

    (a2_eff/a1_eff)^2=8(1+c1)/(1+c2+c3)<8,

because c2+c3>c1 for c1>0,c3>0. This holds already at m=1 and for every finite m. The strict inequality is not a numerical truncation effect. It shows failure of the naive identification with the old critical linear-energy chain; it does not exclude another tuning, target, or direct nonlinear analysis.

At fixed 0<q<J and fixed positive gamma_l, both 2m-1 and m tend to infinity. The geometric sum tends to 1/(J^2-q^2). Substitution yields the displayed limit, strictly below eight. Neither that ratio discrepancy nor its relative deficit goes to zero merely because the bandcenter hoppings go to zero. Conversely, c_l <= gamma_l^2/(J-q)^2 shows why separately small gamma_l/(J-q) can reduce it. That is an additional supplied scale, not a conclusion that integer length alone supplies a small preparation or pulse error. No uniform-in-length finite-band remainder bound is needed for this exact zero-energy derivative and limit argument; a dynamical use would need such control separately.

## Required ancestor port correction

The stationary source at 2972451d says H_bg already retains j n_p, then literally adds Q_gamma3 and (j-gamma3)n_p at the port. Their compression adds another j n_p. Read literally, that doubles the retained cap and does not preserve the intended background. Root has identified this required correction during the distinct stationary review: remove the existing cap contribution before installing its replacement, so the final compressed port contribution remains j n_p. This is not permission to delete a physical term silently, and the final corrected construction must state the replacement explicitly.

The target linear-mass proof does not use that erroneous port onsite value in Z_s, in the source-only congruence, or in the ratio limit. Consequently its diagnostic survives as stated for the intended corrected common-onsite construction. Its observations about the additional port derivative remain necessary after the correction. This review does not certify the uncorrected stationary installation, loaded bandcenter equivalence or substitute for the separate stationary installation review. No ancestor was edited by this reviewer. During final hashing, concurrent root correction was detected: current PROPOSAL.md is d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3. I read the complete delta against ORIGINAL_2972451d.md: it explicitly replaces the cap, distinguishes mediator J from the old calibrated J, and records correction provenance. No Taylor formula changed. Its scoped installation recheck remains separate.

## Exposure, identities and limits

Root authored this new diagnostic and exposed the proposed ratio/length interpretation and the port issue. I authored both mediator ancestors, so their formulas are shared source work, not independently rediscovered evidence. I am distinct from this target's author and reconstructed the Taylor derivative, congruence and strict limit algebra here. The original isolated gap and positive-head setup are reused conditionally; this is not a blind review or a new audit of the physical supplier.

| Source relative to renewal directory | SHA256 |
|---|---|
| mediated_source_linear_mass/PROPOSAL.md | 51b3461c0ed92f304a34cc97f017e1cda53876ec5904b0868682dfe09dffc44d |
| mediated_critical_source_interface/PROPOSAL.md | d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3 |
| bipartite_mediator_supply/PROPOSAL.md | 836caee25d87e31c757e8965b4de85d5998a613dcc5862072d6cddc2a380c8dc |

No dynamic bound, prepared-product overlap, hidden-pole exclusion, actual mass estimate, source pulse, full-apparatus transfer, native supplier or universal obstruction follows. Alternative renormalized tuning and direct noncritical analysis remain open as the target states. No scientific execution, numerical spectrum, sweep, canonical/Git/PR/checkpoint/prompt/model changes or delegation occurred. Only this review was written.

Preserved original stationary bytes: `mediated_critical_source_interface/ORIGINAL_2972451d.md`, SHA256 `2972451d77aae751d5cf64c7022468e372d078a5bfda36b7a9c7b8477036596e`. The table current-proposal identity reflects the concurrent corrected revision; the target itself still pins the preserved original.
