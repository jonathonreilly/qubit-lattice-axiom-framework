# Focused independent scalar-clock check

No material mathematical error was found in the frozen candidate at its stated supplied-model and analytic-time scope. The positive constraint-energy refinement is valid and allows constraint propagation on the metric evolution's full constructed interval T1. It does not establish smooth-data metric evolution, exact finite closure or a physical Record clock. This is a focused analytic check, not formal review, audit, retention or framework adoption.

The candidate is WORKING_PROOF.md SHA256 `bff81bc6385b0804ac86c22ddd5b5b7335aa9ab0e6e940bf8d685077a08b1779`, with CONSTRAINT_ENERGY_REFINEMENT.md `c2f47d92466f36b75cad59d8d9bc0d07f49611099ef97478028bd1d4f009cacd`, bound by FINAL_IDENTITIES.json `a39d2a62816d732df80bd65edbcde387d250057ac3465553e761b5e8fd887355`. The exact contract is `f77dc148f733ed10a1883d6783997aea2eaa03b04f79f086c5d9072a83ed91e8`.

## Independence and premises

PRE.md `3101c66980d94a17c170733a9a43652757e8de63336d81693bf264ad6e809096` was frozen before opening the new proof, refinement, implementation or results. It already derives the lapse correction, both constraint equations, the positive constraint energy, the actual finite augmentation and a nonconstant compatible tensor family. The prior root brief and the contract's candidate Hamiltonian were disclosed. I authored the underlying PR9398 unit; this check is independent reconstruction of the new continuation, not independent review of that parent.

The complete parent note at commit `6515ffa8570f21a0b3a8790fdd8a2879347550b8`, SHA256 `f09e518e2163498bad78f0c3f81cb4fcbdb613be2c20cb8ffdd89198b20a16c2`, was freshly read before PRE. Its canonical pairing, literal law, continuum constraint algebra, analytic Wiener estimates, compactness/Volterra argument and both full-alias consistency bounds are the mathematical input. That open-PR input remains explicitly provisional. The complete argument needed here is in that canonical source; old campaign precursor reports are not substitutes for it.

Current mainfb5 and selected7146 framework/procedure reads are reused only at the verified unchanged bytes recorded in PRE_INPUTS and SOURCE_BINDINGS. In particular, the memo, registry and all three registered primitive sources retain their actual grants. A continuous classical metric/scalar carrier, expectation convention, positive a,K, the normalization s=aK, canonical action, torus/refinement, analytic initial state, fixed clock density, orientation and zero shift are supplied additions. Neither the original walker nor a microscopic record process supplies them. No native density theorem or numerical result enters this check.

## Actual gradient and reduced-branch comparison

Use q=sqrt(det g), N=q/w0 and chi=C_g+w0^2/(2q). The reduced Hamiltonian is exactly mean(N chi)=mean(q C_g/w0+w0/2), with w0 held fixed in its canonical variation. Its derivative is mean(N delta chi+chi delta N). Thus, relative to the full scalar equations varied at fixed lapse N, the metric velocity agrees and the metric-momentum velocity has the additional term -chi N_g. For diagonal coordinates N_g=N g^ii/2; an off-diagonal canonical coordinate varies both entries and gives N_g=N g^ij. These factors match pi_ij=p_ij/2 and the normalized grid bracket.

This correction recovers the full scalar metric stress when chi=0; it is not optional at a finite residual. The density factor q cannot be held fixed merely because a lapse is often an external smearing in ADM formulas.

With W=sqrt(-2q C_g)>0, direct variation before integration by parts gives

    delta H_clock-delta H_red
      =mean[(1/w0-1/W)delta(q C_g)],   H_red=-mean W.

On an identically constrained field W=w0, so the gradients agree for every canonical direction. This statement works for the literal finite functionals too when the pointwise constraint is identically zero. It does not identify their off-surface vector fields or prove preservation of that finite surface. Off the surface, derivatives of the coefficient in this displayed variational identity can enter the integrated gradient. Their different values on the constrained submanifold are consistent with equal ambient gradients there.

## Fixed-density propagation and positive energy

The direct derivation in PRE agrees with candidate(C4)–(C6). The undifferentiated scalar potential leaves the CC bracket unchanged because its two mixed kinetic terms have the same smearing product. Metric dependence of N gives

    {C[f],N}=f a tr(g pi)/(2w0)=f zeta.

For the momentum equation, w0 must be fixed in the reduced Poisson bracket even though its coordinate transformation law is that of a density. I checked the correction explicitly:

    {G[X],C[l]}=C[X.grad l]+mean[l(w0/q)div(w0 X)].

Including the bracket on N and integrating the periodic divergence gives

    J_dot_i=w0 partial_i(q chi/w0^2).

An independent shortcut is that q C_g has density weight two under the metric Lie variation. Varying mean(q C_g/w0) with w0 fixed gives the same result. Treating the frozen w0 as if it were an extra canonical field in this step would remove a necessary term.

The scalar equation is

    chi_dot=s g^ij J_i partial_j N
              +s partial_j(N g^ij J_i)+zeta chi.

The trace of the actual metric velocity gives q_dot/q=-zeta. Consequently, with u=q chi/w0^2 and A_clock=N^2 g^-1,

    u_dot=(s/w0)div(A_clock J),
    J_dot=w0 grad u.

My PRE instead used v=J/w0, which is exactly equivalent because w0 is time independent. Its energy becomes precisely refinement(E4):

    F=(1/2)mean[w0 u^2+(s/w0)J_i A_clock^ij J_j].

Direct differentiation gives only

    F_dot=(s/2)mean[w0^-1 J_i (A_clock^ij)_dot J_j].

The spatially varying w0 cancels before integration by parts; no derivative of it has been discarded. Positivity of g,w0 and s=aK supplies the positive quadratic form. On a compact interval of the analytic solution, the relative operator norm of A_clock_dot is bounded, hence |F_dot|<=k(t)F. Gronwall proves propagation of all four zero continuum constraints throughout T1. This replaces the proof's earlier, valid but smaller, constraint-only analytic interval. It supplies no Sobolev or smooth-data existence theorem for the nonlinear metric equations.

As a separate sign check, mean(q chi/w0)=H_clock has derivative equal to the mean of a periodic divergence. Conservation of this indefinite Hamiltonian agrees with the canonical law; it does not make it a positive physical energy.

## Literal finite equations and analytic continuation

The exact skew-adjoint rewrite uses Z=det(g)g^-1/w0, q_l=D_l g and r_l=D_l Z as analysis variables. The new kinetic density is a/w0 times the DeWitt quadratic, with no determinant denominator. Varying r=D Z gives delta r=D(Z_g delta g). Moving this D by its adjoint puts Z_g OUTSIDE D V_r, with a positive contribution in p_dot. The proof's(C8) therefore has the correct sign, ordering and all six-coordinate factors. It does not use a finite chain rule; in particular D Z is not replaced by Z_g Dg or by a continuum expansion involving D(1/w0).

Ordinary time differentiation preserves the two auxiliary relations because w0 is fixed. There are still six physical canonical pairs, not independent canonical Z or derivative fields. Every component has at most one spatial derivative of a local analytic function after this augmentation. Including eta=1/w0 as a frozen component is sufficient to retain its spatial variation in the majorants; no evolving inverse eta is needed.

I checked applicability of the parent's analytic machinery to these actual new maps. The hypotheses explicitly require finite Wiener norms for both w0 and its reciprocal at the stated radius and a real positive lower bound. Real positivity alone at a preassigned complex radius would have been insufficient; that omission does not occur here. The M0 bound controls actual initialized Dg and DZ with one radius reserve. The constants are recomputed for T_c,Z,V and the new M ball, so no unchanged numerical constant is silently imported. The shrinking-radius bootstrap keeps g uniformly inside the inverse-metric domain and bounds the full finite ODE independently of grid size.

The first-order scale Lipschitz bound, compactness and ordered Volterra estimate consequently apply with the displayed smaller radius and T1. Spectral and centered symbols need only their upper bound by |k_j|. The two parent sampling commutators include every alias: the spectral tail is exponential, and the centered global sine remainder is O(epsilon^2). Local algebraic maps commute with sampling even when eta varies. Initial eta and its evolution have no comparison defect; the derivative variables have precisely the stated initial mismatch. The true finite C,J add one derivative of an analytic augmented map, so a further radius reserve preserves the rates. These steps justify(C10) on T1 after the energy refinement.

For the centered law, the integrated Hamiltonian density uses a radius-one star. Functional differentiation couples two such stars and has radius at most two. The literal scalar diagnostic uses radius two and momentum uses radius one. The spectral law retains line support. This is the changed collocated comparator, not restoration of the fixed staggered seed or exact finite constraint algebra.

## Compatible data and orientation

At g0=I and pi0=lambda I+A with A symmetric, traceless and divergence free, direct contractions give tr(pi0^2)-tr(pi0)^2/2=tr(A^2)-3lambda^2/2 and J0=-2div A. Thus the candidate's positive w0=sqrt(3a lambda^2-2a tr(A^2)) gives all four constraints exactly.

The matrix entry Wiener bound |A|<=|lambda|/4 implies |2tr(A^2)/(3lambda^2)|<=1/24. The binomial series and its reciprocal then converge at the prescribed radius; both displayed norm bounds and the real lower bound sqrt(3a)|lambda|sqrt(23/24) are safe. No unspecified analyticity radius is needed for this family. The concrete transverse diagonal cosine is genuinely nonconstant, and its finite divergence vanishes for both actual derivatives because each diagonal component is independent of its own derivative coordinate. The sampled scalar constraint is a pointwise identity. This proves exact initial finite compatibility only.

For the homogeneous control, direct differentiation of g(t)=exp(-a lambda t/w0)I and pi(t)=lambda exp(a lambda t/w0)I satisfies the actual kinetic Hamiltonian and chi=J=0. The supplied positive w0 makes phi_dot=Nw0/q=1; its sign and nonvanishing are hypotheses. The sign of lambda remains free. Constants and common time need not remain uniform as w0 approaches zero. The inhomogeneous evolution is not restricted to this homogeneous or transverse ansatz.

## Actual evidence inspected and limits

SOURCE_BINDINGS.json verifies all20 files in the frozen candidate manifest, the manifest itself, and all18 author source/provenance identities against actual file or commit bytes. I read the complete new proof/refinement, implementation, wrapper, result, resource receipt and readback. The complete provisional canonical parent was read before PRE. Prior search output identities were verified, but their content is not used to assert exhaustive novelty.

The author code compares literal curvature-Hamiltonian complex-step derivatives to the skew-adjoint local variation, with nonconstant w0 and all six symmetric slots. On n=3 it checks324 coordinate derivatives for each derivative law; on n=5 it checks12 dense tangents each. It also checks six compatible-data fixtures at n=3,5,7. The recorded maximum gradient error is4.85722573273506e-16. Nonzero omitted-adjoint and omitted-eta/chain-rule discriminators test consequential terms. The original and augmented energies and explicit kinetic variation are compared separately.

The result bytes equal the actual stdout, all capture hashes agree, and the managed run exited0 without termination:6.150038wall seconds,5.85294reaped CPU seconds including monitoring,35,618,816bytes OS peak RSS. The script's internal wall timing begins after NumPy import, as its readback states. These are author-reused floating controls, not interval certificates or an independent numerical result. I did not execute/import the author runner or run a new numerical control. The decisive independent work is the frozen first-principles variation, density transformation and energy derivation above. No PDE trajectory or certified useful time was computed.

There is no mathematical correction to request. The frozen proof's closing sentence that its gradient control had not yet run is an as-of proof-freeze statement; the later separately bound execution supplies the actual status. Any consolidated downstream source should use the current evidence status without changing that historical file.

Permitted reuse is the stated short-time analytic theorem for the explicit supplied scalar-clock finite laws and their compatible continuum limit, with the provisional parent and added hypotheses named. It does not establish native M2 realization, original matter action, physical source or Record-clock selection, exact finite first-class closure, smooth-data stability, long-time evolution, or a different off-constraint square-root Hamiltonian. No author file or delivery worktree was edited by this check.
