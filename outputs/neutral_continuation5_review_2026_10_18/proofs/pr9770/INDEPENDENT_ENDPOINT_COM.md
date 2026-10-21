<!-- Original PR9770 source SHA256 76734343424d82a2e71f1912266bab1261968d8a1747e2a33bfcebe3f4ac5432. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Four-column endpoint COM and readout: exact extension check

Disposition: PASS in the same K1 one-wall-per-column height sector as /private/tmp/neutral-fourendpoint-bound-check.md. No extension to a full-native pole or finite paired-endpoint eigenstate is implied.

Use the physical center R=(h1+h2+h3+h4)/4 to define Bloch fibers. Common integer shifts change R by an integer. A pair raise/lower changes R by +/-1/2; a height-difference-one swap leaves R unchanged. For each edge between canonical ray states, the two equal-direction moves that coincide after common-shift quotient therefore sum to +/-2 cos(k/2). The same is true of the flat-to-ray edges. The diagonal-node swap edges remain -1. Defining fibers directly with R accounts for the shape-dependent center offsets and avoids mistakenly attaching only the canonical minimum-height phase.

Set gamma=cos(k/2). The normalized combination

 b_n=[X+_n+X-_n+(-1)^n(Y+_n+Y-_n)]/2

still cancels all diagonal-node couplings, independent of k. Its hopping is -2gamma and flat coupling -4gamma. Consequently H_bright(k)=gamma H_bright(0) exactly. For gamma>0,

 E_b(k)=-8gamma/sqrt(3), r=1/sqrt(3), |c_flat|^2=1/3.

The normalized internal vector is independent of k in this R-based gauge. At k=0 its lower eigenvalue has a positive gap to every other channel in this component. Operator-norm continuity in k preserves a nonzero isolation gap on a sufficiently small fixed neighborhood. Other-channel eigenvalues can emerge from a threshold away from zero; this does not invalidate the local isolation argument. No claim is made at gamma=0 or throughout the full Brillouin zone. The half-angle representation can acquire an internal gauge twist under k -> k+2pi, so the displayed local branch should not be identified with an unchanged global fiber label without that twist.

For the density factor D_p=sum_c exp[ip(h_c-R)], the flat configuration has value 4. On each of the four ray configurations at height n, two heights are R-n/2 and two R+n/2, giving 4cos(pn/2). The bound-state probabilities are 1/3 on flat and (4/3)3^(-n) on the normalized b_n state. Thus

 F(p)=4/3+(16/3)sum_(n>=1)3^(-n)cos(pn/2)
     =4(1+cos(p/2))/(5-3cos(p/2)).

In particular F(0)=4. Since the initial and final bound internal vectors agree in this gauge, this expectation is also the inter-fiber bound-band form factor whenever both momenta lie on the isolated bright branch.

For a single wall between h and h+1, the centered original longitudinal distance-two readout differs from the uniform value only for the two crossing pairs. Their contributions are

 -2[exp(iph)+exp(ip(h+1))]
 =-4cos(p/2) exp[ip(h+1/2)].

Summing four walls and projecting to the bright band therefore gives the vertex

 V(p)=-4cos(p/2) exp(ip/2) F(p)
     =-16 cos(p/2)(1+cos(p/2))/(5-3cos(p/2)) exp(ip/2).

This is the coefficient multiplying exp(ipR), with the corresponding momentum-transfer sign set by the Fourier ket convention. V(0)=-16, exactly the four-wall diagonal readout shift. V(-p)=conjugate(V(p)), as required. At finite p it transfers COM momentum rather than acting as a constant. A volume-normalized source requires its additional stipulated Fourier normalization; none is hidden in this four-column vertex.

The semi-infinite reference readout must be understood through this localized difference from the uniform value, or an equivalent finite-volume subtraction, since the unsubtracted infinite bond sum is not a finite observable. This subtraction does not change any of the local crossing-pair calculations. The constant p=0 projected vertex alone is not an inelastic internal excitation; the finite-p statement is a bound-band scattering matrix element within the specified coefficient sector.
