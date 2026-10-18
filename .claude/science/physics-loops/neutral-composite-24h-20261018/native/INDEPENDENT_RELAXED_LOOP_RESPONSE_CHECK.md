# Relaxed particle-conditioned loop response

Focused check of the consequence of the dressed-patch estimate <F>=O(lambda^(3/2)). That estimate is taken as the input theorem here; it is not rederived.

## Exact singleton algebra

Within the normalized singleton sector, the position projectors satisfy sum_i n_i=I. The plaquette signs commute with these position projectors, and four plaquettes are incident on each site on the nondegenerate periodic transverse graph. Therefore

    F=sum_i n_i sum_(p incident i) (1-P_p)/2,
    0<=F<=4I,
    W=sum_i n_i sum_(p incident i) P_p=4I-2F.

It follows that spec(W) is contained in [-4,4]. For any state, pure or mixed,

    Var(W)=<(W-4)^2>-(<W>-4)^2
          <=4<F²> <=16<F>.

No commutation with the Hamiltonian, clustering, or independent-defect premise enters this inequality. Thus the supplied patch estimate implies Var(W)=O(lambda^(3/2)). In particular <W>=4-O(lambda^(3/2)), and the norm of the centered loop action on a pure relaxed state is O(lambda^(3/4)).

## Response interpretation

For an exact stationary eigenstate, the sum of all transition weights of W to orthogonal states equals its variance; weight strictly away from zero energy is at most that quantity because degenerate elastic transitions may also be present. For a stationary mixed state, the nonzero-frequency dynamic structure-factor weight is likewise bounded by the total variance. Thus the total inelastic weight of this particle-conditioned operator is O(lambda^(3/2)) under these stationary-state hypotheses.

A merely near-minimal variational or quasimode state need not be stationary. In that case the proven conclusion is the small centered-action norm/variance. Calling it a positive frequency-resolved response of a stationary relaxed state requires the additional stationary-state construction. The inequality itself remains exact and useful for the prepared state. It does not by itself give a fixed-time return probability under a Hamiltonian that can move the state outside the controlled low-energy sector.

## Dressed actual state

The assertion should be made for the normalized dressed singleton projection and the consistently dressed W. Odd global parity excludes the even half-column branch, but alone does not exclude every higher-wall odd sector. The actual-state projection error must therefore still be retained.

If the actual dressed state has probability epsilon outside the singleton sector, defining a bounded extension of W there and returning through the same unitary adds an error controlled by that leakage (a conservative pure-state norm comparison gives O(sqrt(epsilon)); a block-diagonal extension gives O(epsilon) in the moments). To preserve the displayed power, the corresponding error must be no larger than O(lambda^(3/2)), or be listed separately. Alternatively state the result exactly for the normalized projection, as the task proposes, without identifying it with the unprojected microscopic readout.

## Why the distinction is useful

The earlier vacuum bound Var(P_p)>=0.36 concerns a specified local plaquette operator acting on the unrelaxed vacuum neutral state. Here W averages plaquettes conditioned on where the heavy excitation is, in a different state selected to favor locally flat transport. There is no contradiction: the heavy excitation can correlate with low-flux regions while flux fluctuations remain elsewhere. A small conditioned variance does not imply that the unconditioned plaquette operator or original uniform distance-two source is quiet everywhere.

Indeed the same estimate bounds each directed incident-loop contribution. If F_a=sum_i n_i(1-P_(p_a(i)))/2, then 0<=F_a<=F and W_a=sum_i n_i P_(p_a(i))=I-2F_a. Hence Var(W_a)<=4<F_a><=4<F>. The suppression is not solely an accidental cancellation between the four terms in W; it reflects the conditional concentration on locally flat plaquettes.

## Conclusion

The proposed inequality and the prepared-versus-relaxed environment distinction are sound. With a stationary relaxed state they give a suppressed total inelastic response of the particle-conditioned loop observable. For a general near-minimal state retain the variance formulation. Neither statement identifies W with the unconditioned original source or supplies a universal matter/environment coupling.
