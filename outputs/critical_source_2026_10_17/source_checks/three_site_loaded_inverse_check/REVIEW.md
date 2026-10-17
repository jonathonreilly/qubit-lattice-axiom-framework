# Distinct check: full-fiber three-site inverse

Conditional support, no necessary correction, for the complete `three_site_loaded_inverse/PROPOSAL.md`, SHA256 `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.

The open-channel polynomial, complementary physical-root bounds, ordered full-fiber factorization, Theta3 criterion, selected forcing-column comparison and seed-block subtraction are valid on the stated domain. This is a conditional algebraic inverse interface. It establishes no actual three-site installation, scalar spectral normalization, seed mass, temporal escape or full old-output theorem.

## Exposure and sources

Root authored the target and exposed the requested checks. I did not author it. I authored or checked earlier source/endpoint/reference work, and checked the two-site scalar and physical attachment qualifications, so this is a distinct reconstruction with shared ancestry rather than blind review. The full target and the cited `two_site_loaded_mass/PROPOSAL.md` were read and hash-verified. The latter has SHA256 `f2b34e07c37ee4a72b1a0301eb6f364431c71055a0a1a5b2ade90159dee9c39f`; only its definitions of D, full physical reference, both-window/sector interpretation and background hypotheses are reused. Its two-site mass conclusion is not a premise of this check. The separate three-site scalar/moment work is not reviewed or assumed here.

## Exact columns and order

Let A=D-kappa^2G and P(D)=D^2-a1^2I. Substituting the proposed columns in row 3 cancels -a1 A Q^-1 against a1 A Q^-1. Row 2 cancels D A and a2^2 terms without commuting D and A. Row 1 becomes

    [D(D A-a2^2I)-a1^2 A]Q^-1 f
      =[P(D)A-a2^2D]Q^-1 f=f.

Thus all three columns have the stated signs and order. The kernel argument eliminates psi1 and psi0 using only the nonzero scalar a2 and a1. It reduces to Q psi2=0, so invertibility of Q implies invertibility of the finite source matrix S. No inverse of D, P(D) or A is required, including at delta=0 or delta^2=a1^2.

## Physical reference polynomial

Because G0=m_j(D) is a scalar functional-calculus function of self-adjoint D, all reference factors commute. In an open channel,

    kappa^2m_j(x+i0)=(3lambda/(2j))x-i3lambda s_x.

Together with a1^2=lambda^2/3 and a2^2=8lambda^2/3 this gives exactly the displayed q0. Put y=x/lambda, r=lambda/j, U=y^3-3y and V=y^2-1/3. Then q0/lambda^3 has real part U-(3r/2)yV and imaginary part 3s_x V, with s_x^2=1-r^2y^2/4. Squaring cancels both r^2 terms and gives

    U^2+9V^2-3rUyV
       =(1+y^2)^3-r(3y^6-10y^4+3y^2).

Subtracting (1-3r)(1+y^2)^3 leaves exactly 19r y^4+6r y^2+3r. Since r<=1e-8/.0027, 1-3r is positive. The open reference denominator is therefore nonzero, with the stated modulus bound. The polynomial estimate includes the real band endpoints as well; it does not insert an imaginary bath on closed channels.

The sharper identity

    (1+y^2)^3-9(y^2-1/3)^2=y^2(y^2-3)^2

proves |P/q0|<=1/[3lambda sqrt(1-3r)]. Independently, |x^2-lambda^2/3|<=x^2+lambda^2 proves the weighted |x||P/q0| bound. These are separate bounds used for the constant and slope terms, respectively.

## Complementary channels and full norm envelopes

For |x|>=.185, the reference channel is outside [-2j,2j] because 2j<.006. The physical root is real and satisfies |m_j(x)|<=1/j on both exterior components. Triangle inequality gives the proposed lower bound for |q0(x)|. After dividing by |x|^3, the discarded terms are bounded by

    3(lambda/|x|)^2+3lambda/|x|+(lambda/|x|)^3,

which is far below .01 for lambda/|x|<=1e-8/.185. Thus |q0|>.99|x|^3, giving |1/q0|<170 and |P/q0|<6. No upper bound on complementary |x| is needed for these estimates.

The selected inverse envelope is larger than 170 throughout |delta|<=2.4e-8 and lambda<=1e-8. Since the reference is a normal function of D, its norm is the maximum of its channel values. The stated full inverse bound follows; adding 6 to the selected P/q0 envelope is a safe bound for the full functional-calculus norm. No channel multiplicity factor is required.

## Theta3 and selected forcing

The exact noncommuting factorization is

    Q=Q0-kappa^2P(D)(G-G0)
      =Q0[I-kappa^2Q0^-1P(D)(G-G0)].

Only the reference Q0 commutes with P(D). The actual deviation remains on the right. Applying the constant ratio bound to a0, the |delta| ratio bound to b0|delta|, and the complementary allowance to both yields exactly Theta3, using kappa^2/(3lambda)=j. This retains the energy dependence before taking the uniform bound.

If Theta3<1, Neumann inversion gives Q^-1=(I-K)^-1 Q0^-1 and the advertised full inverse envelope. For selected f, Q0^-1 f=f/q0(delta), and

    psi2-psi2,ref=[(I-K)^-1-I]psi2,ref.

Its full internal norm is at most Theta3/(1-Theta3) times the reference norm. This is a full output-column estimate for selected forcing, not a claim that arbitrary full-fiber forcing has scalar reference q0(delta). The independent full inverse estimate does cover that larger domain.

Lower physical boundary kernels have the same deviation norm by self-adjoint boundary symmetry. Reapplying the factorization on that lip is valid. The warning that actual Q_lower is not generally Q_upper-adjoint is essential because P(D) and G need not commute; it is correctly retained.

## Seed resolvent subtraction and scope

The load perturbation is only -kappa^2(G-G0) in S's last diagonal block. Thus the exact ordered identity R-R0=R0(S0-S)R gives

    R00-R00,0=kappa^2 R02,0(G-G0)R20.

Reference commutation gives R02,0=a1a2 Q0^-1, while the exact column calculation gives actual R20=a1a2 Q^-1. This proves the displayed subtraction with its positive sign and correct factor order. Applying the two full inverse bounds yields the denominator (1-Theta3)(1-3r)(delta^2+lambda^2)^3, exactly as stated.

The conclusion requires the supplied full background envelope and matching hypotheses. It does not demonstrate that a proposed physical three-site attachment satisfies them, derive its scalar measure or local moments, or integrate the resolvent bound into an actual seed-mass theorem. Nor does it transfer a one-/two-source waveform, old K/W evolution, runtime, finite cut or success claim. Those exclusions are maintained in the source.

Only analytical reconstruction and deterministic hashing were performed. No scientific runner, numerical sweep, delegation, model change, Git/canonical edit, publication, checkpoint or editable prompt change occurred.
