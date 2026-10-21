# Distinct check of the outgoing source-pole boundary estimate

## Disposition and exposure

SUPPORT at the stated bounded scope. I find the estimate

    E_boundary,out < 5 rho B_net/(h^2 ell)

valid under the proposal's explicit domains, its actual quintic cutoff, normalization p>=1/2, and the previously checked real network inverse hypotheses. The new third-order network bounds are conservative but sufficient. No correction is requested. This is an outgoing contact estimate, not a new simultaneous finite-family resource theorem.

Reviewed source: `common_product_outgoing_pole_tail/PROPOSAL.md`, SHA256 `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80`. I read its complete changed argument, including all derivative formulas and scope qualifications. The review reconstructs the new Laplace, phase, weak-derivative, third-jet and contact arguments below.

This is source-exposed, same-model checking. ROOT proposed the outgoing lower-pole route; the author wrote the packet and related ancestors. I previously authored/reviewed several router, writer and finite interfaces, including finite532866, and authored the separate incoming estimate4eb53. Thus this is a distinct calculation check of the NEW outgoing argument, not a blind review or independent revalidation of the entire ancestry. The incoming result is not used to establish the outgoing estimate. No numerical evidence is needed or used.

## 1. Exact source, direction and normalization

With x=tan(k-pi/2), cot k=-x, A=2-rho^2 and b=rho^2/A, the frozen exact source becomes

    F(k(x))=i sqrt(2/pi) rho exp(ik(x))/(A(x+ib)).

For real x and b>0, integrating exp((ix-b)v) gives 1/(b-ix)=i/(x+ib). Consequently multiplication by -i produces exactly the proposed reciprocal. Combining this with the leading i in F and the Fourier factor 1/sqrt(2pi) gives the real prefactor rho/(pi A sqrt(p)); no minus sign, Fourier factor or phase is missing. The Jacobian k'(x), exp(ik(x)) and matrix M_a all belong in a_a.

The cutoff remains the original upper-band cutoff. There is no full-circle rational replacement and hence no accidental factor-two source mass. The denominator p is precisely ||chi F||_2^2; p>=1/2 is an explicit hypothesis, not a consequence silently inferred merely from rho^2<=h. For each fixed rho>0, Fubini follows from the finite majorant ||a_a||_1/b. Dropping exp(-bv) is done only after obtaining the integrable positive-frequency estimate, so it does not invalidate that preliminary interchange.

The sign is load-bearing: v adds to the outgoing phase derivative. It would not supply the same bound for the incoming component. M_a contains the ordinary-to-flux conversions J^-1/2 and sqrt(sin k), as well as the exact demodulation exp(-57ik). In particular, record1 carries sqrt(sin k/sin q)=sqrt(q'). The physical common scalar phase is untouched. Operator bounds apply to the whole outgoing port vector and tensor with passive references without a dimension factor.

## 2. Phase bounds, including the fourth derivative

Differentiating cos q=cos k+r/2 four times gives the proposal's equation (7). The coefficient -4 of cos q q' q''' includes the derivative of the left-hand sin q q''' from the preceding identity; it is correct. Using the stated sharp real bounds gives an absolute numerator below .0382 and division by sin q>.99 remains below .04. The replacement |q''''|<=10 is therefore safe.

At n between ell and ell+2, t<=7ell/(8j), the positive first derivative is at least .99ell+ell-1.75ell=.24ell; the +57 contributes positively. For the subsequent derivatives, n<=1.002ell and |E^(s)|<=2j give ceilings below 2ell, 5ell and 20ell respectively. The loose upper first-derivative ceiling 4ell is also safe. These estimates hold for both k_a=k and k_a=q.

The actual support has |k-pi/2|<=3h/4, so |x|<.001. Direct derivatives of atan give the stated bounds on k', k'', k''' and k''''. The four-term chain formulas through order three and the five-term fourth formula then establish (9). For example the fourth bound obtained from the displayed individual ceilings is below 45ell, well within 128ell. The first derivative is at least .999*.24ell>.23ell. Thus p_v>=.23ell+v while its next three derivatives are bounded by 4ell,32ell,128ell uniformly in v.

## 3. Three integrations by parts and actual cutoff regularity

Writing D_p f=(f/p)' and iterating the adjoint integration operation gives, apart from a common power of i,

    a'''/p^3 -6a''p'/p^4 -4a'p''/p^4
    +15a'(p')^2/p^5 -a p'''/p^4
    +10a p'p''/p^5 -15a(p')^3/p^6.

This independently reproduces every coefficient and denominator in equation (10). The trace conditions needed at the compact-support endpoints follow from chi=chi'=chi''=0 there. The internal joins introduce no boundary terms because these three quantities are continuous.

An arbitrary C2 function would not justify the claimed weak third derivative. The specified quintic does: its third derivative in its unit transition coordinate is -60+360s-360s^2, whose absolute value is at most60. Scaling the transitions by h/4 yields 3840/h^3 in supremum norm, and their combined length h/2 yields 1920/h^2 in L1. Continuity through the second derivative excludes distributional atoms through order three. Composing with atan preserves W^{3,1}. In the formula for chi_x''', the main term is bounded by this L1 norm and the two other terms, 3chi''k'k'' and chi'k''', are much smaller than the remaining allowance. The other L1 ceilings 2h,20,300/h are likewise sufficient. Thus (13) is valid for the actual cutoff, not an unstated smooth replacement.

The auxiliary-frequency integrals are elementary and convergent: integral_0^infinity (.23ell+v)^(-m)dv=(.23ell)^(1-m)/(m-1). Substitution term by term gives precisely B in (11), including the final coefficient 15/5=3. Since A>=7/4 and p>=1/2, the remaining prefactor 1/(pi A sqrt(p)) is less than1. No rho-dependent loss remains besides the explicit rho.

The chain bounds in (12) also check: exp(ik(x)) has derivative ceilings (1,1,2,5), k'(x) has (1,1,3,10), and M(k(x)) has (M0,M1,M2+M1,M3+3M2+3M1). Ordered Leibniz products give (14). Replacing each by Cbar_s/h^2 is conservative for h<=1. Consequently (15) follows with the stated B_net.

## 4. Actual network derivatives through order three

These are new estimates, rather than automatic consequences of the packet's earlier two-derivative result. I checked their construction against the actual threshold conversions and ordered feedback interface.

For J, its third derivative in record1 is -cos q(q')^3-3sin q q'q''+cos q q'''. The sharp bounds make it much smaller than5; the elastic channel is also covered. Similarly the third derivative of exp(iq) is bounded by |q'''|+3|q'q''|+|q'|^3<5. The scalar square-root and inverse-square-root derivative formulas with J>=.99 therefore fit comfortably inside D3=100 and R3=200. For exp(34iq), the loose ceilings used in the source give 34^3*8+3*34^2*2*6+34*3=356150<10^6. No third derivative of the record bias itself appears.

The full biased writer inverse acts on both record channels; no X_R-sector diagonalization is being imported after adding the bias. Differentiating the ordered inverse three times gives the norm bound

    ||G'''|| <= 6 B^4 L1^3+6 B^3 L1 L2+B^2 L3.

With B=11 and L1,L2,L3=4,12,10 this is exactly (16). The L3 ceiling follows from the energy derivative at most2 and the port self-energy third derivative at most5. The writer scattering derivative is bounded by differentiating -I-2i D E_P^*G E_P D; the constant -I contributes nothing at positive order. The star-product W entries therefore hold, with unitarity used only to sharpen order zero.

For the core, three derivatives of the reciprocal scalar denominators give the displayed alpha_s,beta_s, including the beta powers zeta^2,zeta^3,zeta^4. The real core band has E/j<=3, giving the positive margins lambda and lambda_b. With inverse norm2, the third inverse derivative coefficients are 96l1^3+48l1l2+4l3. Multiplication by the numerator whose derivatives are bounded by2 establishes Rraw. Composing with q gives the third chain ceiling 8Rraw3+36Rraw2+3Rraw1. Both thresholds remain in the required real band.

Cr and Wr use the checked reflection bounds e,w at order zero and the larger full scattering derivative ceilings at positive orders. Their use in the ordered feedback product is valid. Repeated inverse differentiation of I-F gives the three denominators and coefficients displayed for Kjet. The formulas for Ujet,Vjet,Sbound are the actual ordered feedback maps with sums replaced by norm sums; the scalar star arithmetic does not assert commutation of any physical factors. The final factors R, exp(-57ik), S and D in (18) are exactly those in M_a. These facts establish the necessary real C3 operator bounds for both record channels and all logical/reference inputs.

The constants can diverge as den approaches zero. That dependence is explicitly retained. At the specified small-parameter finite family the real margins stay separated from zero, so boundedness of these jets as epsilon tends to zero is justified. This is only boundedness of these coefficients, not an inferred overall resource order.

## 5. Physical cut factor and permitted substitution

The frozen finite cut consists of the hopping-only three-site I perturbations and the F end cut. Their direct-sum contact norm is at most sqrt(2)j. It does not acquire a factor from the number of ports, programs or passive-reference dimensions. For each fixed record, the three radial levels cost sqrt(3) in norm. Summing two record contributions with a factor2 is conservative. Applying (15) uniformly in time thus gives

    2sqrt(6)jT rho B_net/(h^2 ell^2)
      = (7sqrt(6)/4)rho B_net/(h^2 ell)
      <5rho B_net/(h^2 ell).

This is an integral of norms, not an unjustified cancellation inside Duhamel. It includes unwanted outgoing ports and both record values. The cut changes neither record threshold nor endpoint diagonal. Restricting to any subinterval preserves the bound.

The minimum in (20) is legitimate because both estimates upper-bound the same outgoing contribution. It leaves the separate incoming term intact. Neither this minimum nor the separate accepted incoming estimate automatically controls other internal, source-matching, flag or truncation allocations. Rebuilding the simultaneous finite budgets remains necessary before stating an improved resource theorem.

## 6. Source identities and coverage limits

The following unchanged premises were previously fully read in this coherent task history and reused only at their stated scopes; the packet, its review and finite identities were refreshed for this check:

- Packet `common_product_biased_record_packet/PROPOSAL.md`: `cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf`; its distinct review: `315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916`. Used for the exact real network/ordinary-amplitude and order-two interface, not as prior validation of the new third-order estimates.
- Finite `common_product_biased_record_finite_seed/PROPOSAL.md`: `532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123`. Used for the actual source cutoff, contact geometry and old outgoing allocation. I authored this premise; its reuse is not independent checking of it.
- Exact source `common_product_endpoint_launch/PROPOSAL.md`: `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`; source derivative note `common_product_launch_derivative_bounds/PROPOSAL.md`: `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`. Their complete arguments were read in the preceding source-profile/incoming tasks; exact rational F and its upper-band normalization are reused here.

The new source itself was read completely without truncation. The review does not re-audit old local block realization, prove spectral completeness, exclude point spectrum, provide a cooling/loading mechanism, or transfer a permanent halt/normalized rare-branch claim. No global exponent or publication status is established. Only this review file was created; no source, W, Git, checkpoint, axiom or editable prompt was changed, and no delegation or scientific executable was used.
