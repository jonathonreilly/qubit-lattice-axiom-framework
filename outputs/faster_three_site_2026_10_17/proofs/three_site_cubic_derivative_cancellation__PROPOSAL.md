# Preserve the cubic derivative cancellation in nominal D3

New root derivation, requiring a distinct check. Nominal Delta=0 only, with the exact unchanged physical windows, full ordered inverse and all hypotheses of three_site_prepared_inverse_derivative/PROPOSAL.md (25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84), checked separately in3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c. No new physical coefficient or preparation premise is supplied here. This improves its reference derivative majorant by retaining the coherent cubic cancellation.

On the selected upper physical band, write delta real, |delta|<=d=2j sin h, h<=4e-6, eta=lambda/j, P2=delta²-lambda²/3, r=sqrt(delta²+lambda²). The physical Weyl function is

 m(delta)=delta/(2j²)-i sqrt(1-delta²/(4j²))/j.

It follows directly (without differentiating a norm bound) that

 |m'(delta)|=1/[2j² sqrt(1-delta²/(4j²))]<.501/j².

Since 1-sqrt(1-x²)=x²/(1+sqrt(1-x²)) and |delta|/j<=8e-6, the triangle bound gives

 |m(delta)+i/j| <= |delta|/(2j²)+delta²/[4j³(1+sqrt(1-delta²/(4j²)))]
                  <= |delta|/(2j²)+delta²/(4j³)
                  <.501 |delta|/j²,

with equality0 at delta0 handled directly. The strict last inequality is needed only when delta nonzero.

The exact physical denominator decomposes as

 q0(delta)=(delta+i lambda)^3-kappa² P2[m(delta)+i/j],
 kappa²=3jlambda.

Therefore its genuine derivative is

 q0'=3(delta+i lambda)²-kappa²{2delta[m(delta)+i/j]+P2 m'}.

Using |P2|<=r² gives

 |q0'| <= [3+3eta(1.002+.501)]r²
        =[3+4.509eta]r² <3.00002 r².                 (1)

The last ceiling uses lambda<=1e-8,j>.0027, hence4.509eta<.0000167. The lower lip is conjugate and has the identical bound. This is not a Markov replacement of q0: its exact difference and derivative have both been paid. In particular it preserves the cancellation between the real and imaginary cubic derivative components that the older6.01 estimate lost.

The complementary-channel estimates U0'C<4000 and T0'C<200 are unchanged. The new selected envelope dominates4000 throughout the old narrow window, just as the previous one did. Thus in the cited D3 source equations(9),(11)--(14), replace the selected derivative constant6.01 by

 A=3.00002,
 A_s=2/s+A/s², s=sqrt(1-3lambda/j).

All noncommuting Neumann differentiation, margins, actual Gprime envelope Zg, wrong-window inputs, per-window/lip conventions and scalar integrals are literally unchanged. This gives the tightened full bound

 D3 <= (c_a/lambda){n A pi/(2s²)
   +(3j n²/s)[A_s(4a/3+2b lambda/3)+400a lambda²+400b lambda³
                       +Zg(pi lambda/(2s)+12lambda²)]},

where c_a=2sqrt(2)/3 and a,b,Zg,n retain their exact definitions there. The complementary D3_C formula changes only A_s, and is still not an extra term to add to full D3. No actual denominator is assumed to commute with D, and the stronger bound is not asserted for residual or common-offset source families.

The gain is a smaller leading integrated reference derivative ceiling. It does not alone set a complete error, runtime or receiver size. A temporal composition must still include the derivative of full L, endpoints, both windows/lips, all spatial outputs and outside spectral mass. It may retain the older checked Lprime ceiling without claiming that old-core derivative losses have been resolved.

Root authored this calculation after reading the complete D3 source/check and the new background-IBP candidate. The physical Weyl expression and nominal source polynomial are unchanged checked premises. This is a different analytical organization, not an independent validation of its own constants. A distinct check should verify the physical Weyl sign, exact cubic decomposition, selected-band domain, derivative constant and scope of every substitution. No numerical computation, sweep, solver, scientific runner, Git/PR/audit/prompt/axiom/model change occurred. Only this source was written.
