# Exact input-cap forcing factorization before differentiation

ROOT candidate requiring distinct check. This is an algebraic reduction of the unchanged endpoint forcing, not a numerical derivative certificate or a runtime claim. It retains all eight internal forcing coordinates and the actual retarded order.

Use the physical new-port matrices Q, A=[j(Q-Q^-1)]^-1, T=S A, with S the input-input block of the full generalized new-port scattering matrix. All roots are nonzero on the retained physical windows; A and Q commute. The existing input cap ell=20 has

 X=Q^20 T Q^20, Z=A+Q X Q,
 Bbr=I-Q Z^-1 Q(A+X), alpha=A Q^20 Bbr.

These exact identities were refreshed from bandcenter_converter_endpoint/PROPOSAL.md22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a and record_attached_recovery_sharp/PROPOSAL.md07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11, necessary sections1--3 read fully. Their historical narrower numerical claims are not transferred; only the exact cap identities and the current wide-domain scattering premises are relevant.

Set Y=Q^-1 Z Q^-1=A Q^-2+X. Then Q Z^-1 Q=Y^-1 and

 Bbr=Y^-1(Y-A-X)=Y^-1 A(Q^-2-I)
     =Q Z^-1 Q A(Q^-2-I)
     =Q Z^-1 A(Q^-1-Q)=-Q Z^-1/j.

No X is commuted with Q. Let D=Q^21 and Fcap=(I+D S D)^-1. Since T=S A,

 Z=A+Q^21 S A Q^21=(I+D S D)A,
 alpha=-A Q^21 Z^-1/j=-D Fcap/j.                 (1)

The cancellation removes both A and Z from the final physical forcing. It is exact on the full fiber, not just the selected scalar formula. In particular it does not assume S commutes with Q, and it preserves the sign and the21-step phase.

With physical E derivative and fixed j,

 Fcap'=-Fcap[D'SD+DS'D+DSD']Fcap,
 alpha'=-(D'Fcap+D Fcap')/j.                    (2)

For any finite input site n=0,...,20, retain the exact incoming product

 Q^-n alpha=-Q^(21-n) Fcap/j,
 (Q^-n alpha)'=-[(Q^(21-n))'Fcap+Q^(21-n)Fcap']/j. (3)

Thus no growing closed power has to multiply an unstructured tiny coefficient or its derivative. The outgoing coefficient remains beta=S alpha, with its ordinary exact product derivative. These are not replacements of the source/gate response by a scalar.

For explicit future bounds let P be the fixed selected new-j channel, C=I-P, |Q_P|=1, ||Q_C||<=q<1, and let N=21. Suppose actual pointwise physical derivative bounds are available:

 ||S||<=s0, ||P S P||<=r0,
 ||P S' P||<=s1, ||S'||<=swide,
 ||D'||<=d1, ||Q_C'||<=c1.

The first two are values; the next two must be derived from physical equations or valid complex neighborhoods, not inferred from those values. On the current checked real band s0<1.3 and r0<4.81e-5, q=1/60 are available. Keep s1,swide explicit pending a genuine derivative check.

Split the sandwich into four fixed blocks. Then

 rho=r0+s0(2q^N+q^(2N)), ||D S D||<=rho,
 f=1/(1-rho), ||Fcap||<=f, provided rho<1.

The derivative sandwich obeys

 ||D S' D||<=s1+(2q^N+q^(2N))swide,
 K=2d1 s0+s1+(2q^N+q^(2N))swide,
 ||Fcap'||<=f² K.

These are triangle bounds on full matrices; selected and closed outputs are not presumed orthogonal after application. Consequently

 ||alpha||<=f/j,
 ||alpha'||<=(d1 f+f²K)/j,
 ||C alpha||<=q^N f/j,
 ||C alpha'||<=[N q^(N-1)c1 f+q^N f²K]/j.           (4)

Since Q_C is a fixed-projector diagonal function, its power derivative bound N q^(N-1)c1 is valid. The same argument applies separately on both lips. For the actual roots one may take d1=N/.0053 and c1=1/[.0027(60²-1)] on the stated current domain; the open derivative is1/(2j sin q_angle), and closed root differentiation gives |Q_C'|=|Q_C|²/[j(1-|Q_C|²)]. The symbol q=1/60 in(4) is a root bound, not the open angle q_angle.

The old finite response is Phi_old,in alpha. Its derivative must still pay (Phi P)'Palpha+Phi P Palpha' and (Phi C)'Calpha+Phi C Calpha'. Equation(4) supplies exact cancellations that may help bound the latter, but no numerical (Phi C)' or s1/swide claim is established by this note. The output return/gate and cable coefficients likewise remain separate. Therefore no new full Lprime, background bound or complete device point follows yet.

Root derived(1)--(4) directly while investigating the retained cap/direct-action bottleneck in prepared_full_recovery_derivative53f571b6. That candidate's smaller full Lprime is not used. The exact physical cap equations are unchanged; the proposed factorization and derivative inequalities need an independent order/sign/closed-product check. No native interaction, coefficient supply or product-seed theorem is inferred. No computation, solver, scientific runner, Git/PR/audit/prompt/axiom/model change occurred. Only this research note was created.
