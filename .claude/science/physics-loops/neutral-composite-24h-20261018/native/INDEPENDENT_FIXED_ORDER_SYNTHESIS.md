# Fixed-order synthesis: localized stability and scaling check

Checked 2026-10-18. Read `native/FIXED_ORDER_COMPOSITE_POLE_PROOF.md`. Focus: section 4 and its composition with section 2. This report does not independently re-certify the new section-1 gauge calculation or every scalar-channel graph identification; those remain separate proof inputs.

## Localized finite-endpoint stability is valid

Let G0(E) be the baseline outgoing local Green matrix on the fixed finite collection of interface sites, before restoring the fast-sector correction. On the large Airy contour it has exactly one simple pole E0 inside, with residue A of rank one and ||A||=O(f). Its endpoint entries are O(1) on that contour. Therefore

    G0(E)=A/(E-E0)+B(E)

has B holomorphic inside and uniformly bounded there: the subtracted pole term is O(f/f^(2/3))=O(f^(1/3)) on the boundary, and the maximum principle applies entrywise. Matrix size is fixed at fixed m. None of these statements interprets A as a Hermitian or positive projection.

For an analytic finite-endpoint perturbation Delta(E), ||Delta||<=C delta, choose a smaller disk of radius c f around E0. Provided delta->0, I-B Delta is invertible by a finite-matrix Neumann series. The determinant lemma reduces the pole equation to

    E-E0-kappa(E)=0,
    kappa(E)=Tr[(I-B(E)Delta(E))^-1 A Delta(E)]

(up to the equivalent ordering convention). Its magnitude is O(f delta). On a slightly smaller concentric disk, Cauchy gives kappa'=O(delta). Thus there is a unique nearby simple root and its shift is O(f delta). This uses the endpoint residue scale f, not a global resolvent norm. The argument remains valid for complex outgoing Delta and a complex rank-one residue.

If the baseline includes fixed host sites as well as arm endpoints, their pole residues remain O(f) because the regular host Green matrices and interface couplings are bounded. The same finite matrix argument then applies. This is the clean way to include all short-interface corrections without assuming they act only at the first arm site.

## Important contour separation

The large radius-f^(2/3) contour must belong to the BASELINE slow-host/arm problem, before adding the fast-sector self-energy. The latter has only been continued and bounded on a depth-f disk in slow units; that estimate must not be silently extended to a contour which can cross the real axis or approach other fast poles. The draft's paragraph can be read correctly in this order, but stating this explicitly would prevent a real logical misuse.

First construct the baseline pole, whose imaginary part is a strictly negative constant times f. Choose the smaller disk from that known pole, with radius less than its distance to the real axis. The fast estimate is then established on that disk before finding the perturbed pole. This avoids circularly assuming that the final pole is in the required strip.

## Higher slope and bounded bulk terms

At fixed m, f_lambda=f+O(lambda^4), with f=lambda^2/8 and positive leading coefficient. The Airy spacing varies as f^(2/3), so its change is

    O(f^(-1/3) lambda^4)=O(lambda^(10/3))

in slow units. The offset/boundary f term changes by O(lambda^4). These are smaller than the allowed slow-unit O(lambda^(8/3)) remainder. The unbounded slope difference should be treated by using f_lambda as the Airy parameter from the start, not as a small bounded-operator perturbation.

Higher bounded bulk terms of size O(lambda^4) preserve the first-level contour: the spacing is O(lambda^(4/3)), so their norm/gap ratio tends to zero. Uniform baseline Riesz norms give an O(lambda^4) eigenvalue shift. The localized contour expansion also preserves the O(f) endpoint residue; it is stronger than a generic operator-norm projection estimate. Fixed range and fixed m ensure all relevant endpoint sets and constants remain fixed.

The K4 kinetic correction contributes the real constant lambda^2*(109/96), while its nonconstant part and finite boundary completion produce the previously controlled O(lambda^(8/3)) or smaller errors. No omitted affine slope term may be hidden inside the phrase 'bounded bulk terms'; the draft separates it correctly.

## Composition with the fast estimate

Section 2's finite-range Morse/log argument gives local continued fast Green entries O(log(1/lambda)) in fast units, after the confined-arm coupling and finite contacts. Its disk maps to the depth-f slow disk: physical depth O(lambda^4) corresponds to fast depth O(lambda^3) and slow depth O(lambda^2). S-fast vertices O(Jz lambda^2) therefore yield a finite-interface correction

    delta=O_m(lambda log(1/lambda))

in slow units. The determinant argument above gives shift O_m(f lambda log), hence physical O_m(Jz lambda^5 log). Since lambda^(1/3) log(1/lambda)->0, this is indeed smaller than Jz lambda^(14/3). Energy dependence costs at worst delta/f before multiplication by the residue f; it does not destroy the small derivative estimate.

The closed-arm O(lambda^2) slow-unit contact is smaller and can be restored simultaneously. Higher slow-host bulk/contact corrections require the already supplied regular-energy outgoing continuation, rather than a norm-only resolvent comparison; at E=-2 the hole determinant and strict radiation result provide the appropriate baseline stability. I find no extra singular denominator introduced by this composition under those inputs.

## Scope of the resulting claim

The localized stability step itself does not contain a missing Hermiticity assumption or an unfavorable power of f. It supports the stated expansion if the complete fixed-order compact operator has exactly the demonstrated finite-range host/arm/closed-channel decomposition and the asserted coefficient-gauge identification. Those are substantive hypotheses to be retained with their independent proofs; this stability check does not replace them.

In particular, finite-order coefficient normal forms and their actual local remainder bounds do not imply that an outgoing pole survives in the full many-body microscopic resolvent. No physical detector residue, equilibrium preparation, or cosmological scale is established here.

Conclusion: section 4 and its composition with section 2 pass with the explicit baseline-contour/small-disk separation above. Treat the slope through f_lambda, keep all endpoint residues and finite matrices localized, and do not extend the fast continuation outside its proved strip.
