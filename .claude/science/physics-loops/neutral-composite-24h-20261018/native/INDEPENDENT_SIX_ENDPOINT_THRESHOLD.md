# Discrete cluster-threshold check for the six-column endpoint operator

Read `/private/tmp/neutral_height_large.py`. The proposed essential-spectrum lower bound -7 is justified for the six-column relative-height operator, PROVIDED the assumed four-column bound -5 holds at every cluster COM momentum and on every allowed asymptotic internal component. A bound only on the four-column flat-generated component is not automatically sufficient.

## Exact parity and escape geometry

An allowed equal-height move transfers two columns from height h to h+1 or h-1; a mixed-height move swaps two heights. Hence the parity of the number of columns at each height is invariant. Starting from the flat six-column state, every occupied height has even multiplicity. Subtracting a common minimum height preserves this statement.

Consequently there are at most three distinct heights. For sorted heights h_(1)<=...<=h_(6), the gaps after ranks 1,3,5 are exactly zero. Only d2=h_(3)-h_(2) and d4=h_(5)-h_(4) can be nonzero, and the full range is d2+d4. Any escape to infinity in the relative configuration graph therefore has a diverging gap after rank2 or rank4, separating clusters of cardinalities2 and4. A finer three-cluster split has cardinalities2+2+2. Odd clusters cannot occur in this component: a large-gap cut cannot split a group of equal heights.

The cluster membership consists of physical transverse column labels, not just sorted heights. When a cut gap is large, bounded endpoint moves cannot change membership across that cut. A native cross-cluster edge has zero matrix element because its two heights differ by more than one. Thus on such configurations the operator is exactly the sum of internal cluster operators, with no long-range cross term.

## Uniform lower bounds required

For a two-column cluster, if the columns are not adjacent, its internal operator is zero. If adjacent, even-height parity forces equal heights, and simultaneous shifts have spectrum 2a cos(P) with |a|=1. The lower bound is -2 at every momentum, regardless of the XX/YY sign.

Assume each induced four-column internal operator is bounded below by -5 for all its COM momenta and all internal parity-allowed components that can arise. Then a separated2+4 configuration has form bound at least -7. The2+2+2 threshold is at least -6 and does not weaken this bound. Internal disconnected transverse graphs are included in these statements.

The all-COM qualification is necessary: fixing total six-column COM to zero does not fix each cluster momentum to zero. Fourier decomposition in the cluster translation coordinates gives a direct integral of internal fibers with a total-momentum constraint; a uniform individual lower bound survives that constraint.

The component qualification is also necessary. A cluster's restricted height configuration may have been prepared through interactions with the other columns before separation, and need not belong to its own flat-generated component. It is safe to prove -5 on the full even-multiplicity four-height graph, or explicitly classify all asymptotic components. Zero extension from the six-column reachable component into that larger cluster space then preserves the quadratic form bound.

## Discrete IMS construction

Choose smooth normalized cutoffs based on d2/R and d4/R, together with a compact-region cutoff, so their squared sum is one. The exterior cutoffs are supported where the corresponding gap exceeds cR, for a fixed c>0; refine each by the finitely many possible label partitions at that gap. Membership indicators introduce no edge discontinuity where a cutoff is nonzero when R is large, because one native move changes each physical height by at most one.

All cutoff differences along graph edges are O(1/R). The relative-height quotient does not spoil this: sorted-height gaps are invariant under a common shift and change by a bounded amount under an endpoint move. The native graph has bounded degree and bounded real edge coefficients, including any multiplicities from coincident quotient moves. For any finitely supported vector psi, the discrete IMS identity therefore gives an error bounded in absolute value by C R^-2 ||psi||^2. Signed XX/YY coefficients pose no problem: bound the error with their absolute values; no positivity-of-hopping assumption is used.

Each exterior localized vector is supported in a separated2+4 channel, so the preceding internal-operator lower bound applies. The interior cutoff is supported where d2+d4<=C'R, a finite set of integer relative-height configurations. Thus outside a finite set the form is bounded below by -7-C/R^2. Equivalently, every weakly vanishing Weyl sequence has liminf energy at least -7, after taking the sequence limit and then R->infinity. This proves

inf sigma_essential(H_relative,flat component) >= -7.

This is a lower threshold bound, not equality: some channels may be unreachable or have thresholds strictly above -7. The proof is a bounded-degree discrete localization argument, not an assumption of a continuum HVZ theorem.

## Consequence of a certified finite trial

Any finite-support vector in the actual infinite reachable component with exact Rayleigh quotient below -7 implies at least one discrete eigenvalue below the essential spectrum. The finite cutoff graph need only be a finite subgraph of that component: zero extension supplies a valid trial even if other states within the same height range were not reached without leaving the cutoff. A floating Ritz value alone is not the exact certificate; integer/rational trial coefficients and an exact quadratic-form inequality provide one.

This would establish a bound relative-height state for the specified first-order endpoint operator, conditional on the four-column threshold certificate. It does not establish a native full-H eigenstate, a lifetime, uniform large-feature rigidity, or coupling to the original scalar readout. In particular the previously derived bare uniform C is constant on the long-single-interval height chart. The zero-COM eigenstate also does not by itself supply a localized center-of-mass wavepacket or its dispersion.

### Four-column input scope clarified

The root reports that its separate four-column certificate covers the flat state plus all six pair-pattern rays, including components unreachable from flat, for all fifteen induced four-column subsets and all momenta. Its `/private/tmp/neutral_four_interval.py` uses 257 momentum samples with an explicit derivative bound and a positive interval margin. That stated coverage resolves the component-scope concern above. I have not replayed that independent numerical/interval certificate in this threshold check; its arithmetic validity remains its own verification task. Given that certificate, the lower essential threshold -7 follows by the argument here.
