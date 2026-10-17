# Same-carrier slow-lead interface: selective check

Disposition: conditional support for the exact scalar interface, positive realization, reference-only reflection estimate and conditional finite-length substitution. No correction is requested. The altered Hamiltonian has not thereby acquired an actual attached-device mass, profile, runtime or herald theorem.

## Source and exposure

Read the complete root-authored `../same_carrier_slow_lead/PROPOSAL.md` at SHA256 `a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4`. I did not author this interface. The candidate and illustrative g, M and T were exposed. This is a separate analytical reconstruction, not blind or model-diverse checking.

Reuse the previously completely read attachment `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457` and its checked site-count conventions; corrected outgoing source `52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788` and my review `44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026` for the unnormalized reference moment; and weighted finite-transfer note `735ec540842018f17ecde72b43d102f52dd76f9df65682eaaeec64498628c429`, read completely in the preceding finite-application check. Their identities and relevant premises remain unchanged. The suggested future use of gate inverse 26/j is not used to conclude invertibility of the changed apparatus here.

Applicable unchanged workflow and physics-claim-reviewer discipline were reused. No scientific execution, parameter sweep, numerical dynamics, delegation, W/Git, publication, model or prompt change occurred. Only source reading, deterministic bookkeeping and this sole review were performed; no editable prompt file changed.

## Indexing and positive realization

There are TWO distinct interface coordinates: old halfline endpoint n=0, which is the retained gate output port, and first slow site m=0, a new vertex adjacent to it. The formulas do not identify those two zeros. The old medium occupies n<=0 and the slow medium occupies m>=0 with their joining bond -tau.

For 0<g<j and tau=sqrt(jg), both tau<j and g<j hold. The old outgoing exchange diagonal changes from j to tau, so adding (j-tau)n at the old port restores its unchanged diagonal. The first slow site receives tau from its connector and g from its outgoing edge; its added (2j-tau-g)n makes the total 2j. Every later slow site receives 2g from its two edges, and 2(j-g)n supplies the rest. All these occupations are strictly positive in the specified parameter range and the exchange blocks are PSD on the full two-qubit space. Shared B is unchanged and no vacancy constant is introduced, so there is no additional common scalar.

At finite M=1 the first slow site has connector diagonal tau and cap g, with the same first-site occupation; its diagonal remains 2j. At M>1 the final site's one remaining g edge plus cap g and occupation 2(j-g) again give 2j. Thus the stated cap realizes exact compression for all M>=1, including the indexing corner case. It is not an absorber or a time-dependent switch.

## Exact scattering and flux

The old endpoint equation gives

    delta(1+r)=-j(w^-1+rw)-tau t,
    tau t=j(w+rw^-1).

The first slow-site equation gives delta t=-tau(1+r)-gvt, hence t=(tau/g)v(1+r). With tau^2=jg, substitution yields

    r=(w-v)/(v-w^-1)
      =w sin((q-k)/2)/sin((q+k)/2).

For q,k strictly between zero and pi the sine denominator is positive and the displayed scalar solution is well-defined. At the common carrier center r=0 and t=i sqrt(j/g). Multiplying by sqrt(g sin k/(j sin q)) gives t_flux=i, as claimed.

The oriented incident/reflected currents are 2j sin q and -2j sin q |r|^2, while the transmitted current is 2g sin k |t|^2. The two real boundary equations preserve their sum. Alternatively the identity sin^2((q+k)/2)-sin^2((q-k)/2)=sin q sin k directly verifies |r|^2+|t_flux|^2=1. This confirms the velocity factor, not just a formal modulus-one assertion.

For momentum-normalized packets the Jacobian is essential. Differentiating the common energy gives dk/dq=j sin q/(g sin k). Changing an old outgoing integral into a k integral produces coefficient t F(q(k)) dq/dk, with any chosen plane phase retained. Its squared k norm becomes integral |t_flux(q)F(q)|^2 dq. Thus t itself is neither a unit-flux coefficient nor a coefficient that may be used under an unchanged momentum measure. The proposal explicitly warns against that error and does not yet claim an attached slow-ray packet.

## Band and reflection constant

On |delta|<=d<2.4e-8 with g=1e-6, the slow detuning satisfies |delta|/(2g)<.012; the old detuning is still smaller. Both channels are open. Writing q=pi/2+asin(delta/(2j)) and k=pi/2+asin(delta/(2g)), their displacement difference is bounded by |delta|/[2g sqrt(1-.012^2)]. This is conservative because it discards the subtraction of the old displacement.

The sum of absolute displacements is below .01201: the slow one is at most .012/sqrt(1-.012^2), and the old one is below (2.4e-8/.0054)/sqrt(1-(2.4e-8/.0054)^2). Hence the reflection denominator is at least cos(.01201/2), while its numerator is at most |q-k|/2. Therefore

    |r| <= |delta|/[4g sqrt(1-.012^2) cos(.01201/2)]
         <.251 |delta|/g, delta!=0.

At delta=0 the exact result is r=0, so the non-strict version includes the center. The uniform ceiling .251*.024=.006024 is below .0061. No false strict inequality at a zero right-hand side appears.

For the inherited unnormalized reference in q, |delta|=2j|sin(q-pi/2)|<=.006u. Thus its reflected coefficient norm is at most (.251/g)*.006 sqrt(M2), with M2<1.9e-17. Using sqrt(1.9e-17)<4.36e-9 gives a result below 6.56616e-6, hence below 6.6e-6. This calculation is for one scalar reflection multiplying the old reference. It includes neither coherent repeated returns nor actual changed-apparatus mass, and is correctly labeled only an orientation estimate.

## Conditional storage length and counts

The weight is zero on the entire upstream apparatus and on first slow site m=0. The strong connector tau has zero weight difference. The slow path has f(m)=m, so only its g bonds contribute to the imaginary-part norm, bounded by 2g sinh1. The seed is upstream, the cut endpoint has f=M-1, and the sole cut magnitude is g. All onsite terms, including the large diagonal 2j and internal B, remain exact self-adjoint blocks in the weighted proof. Their norms are not replaced by g.

The inherited single-cut theorem therefore gives the stated complete finite/infinite difference <=1.2 exp[-M+4gT sinh1] on [0,2T]. At g=1e-6, T=1e15 and M=5e9, sinh1<1.2 makes the exponent strictly below -5e9+4.8e9=-2e8. This easily yields <1e-6, for example by reducing the exponent only to 21 and using 1.2/2^21<1e-6. The bound includes later returns inside the declared horizon.

The original final ray counted its gate output origin among its M sites. Here that old origin is retained upstream and M entirely new slow sites follow it. Relative to the old convention, the head count therefore gains one: M+236 heads, and four old/source qubits plus the shared record give M+241 physical qubits. At the illustrative M the latter is 5,000,000,241. Positive occupation blocks are newly installed at every slow site and the old port, so inheriting the old positive-block count unchanged would be false; the proposal correctly withholds that count pending explicit re-inventory.

## Load and remaining obligations

The free slow surface resolvent is -v/g on its physical upper branch. Its old-port selfenergy is tau^2(-v/g)=-jv, compared with -jw for the former uniform j lead. Thus the new rank-one load difference is exactly -j(v-w), with the stated sign and no additional coefficient. It changes the gate response even though both carrier centers agree. This is not the same Hamiltonian as the already checked attached device.

The scalar calculation does not prove full record-sector matching, inverse margins, closed-channel behavior, actual seed spectral regularity or omitted mass, wrong-window input bounds, common slow-output phase, temporal concentration or a complete herald map. Those tasks must retain the new momentum Jacobian and all B channels. The illustrative T is only an input to the conditional finite-compression inequality; the old actual onset is not borrowed. No same-quality resource ratio, permanent storage, irreversible record latch, reset, reuse or native supplier is established.
