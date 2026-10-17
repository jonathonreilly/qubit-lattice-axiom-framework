# Distinct check: factored input-cap forcing

Disposition: conditional support; no necessary correction found. The exact full-fiber factorization, sign, reference plane, finite-input cancellation and stated conditional derivative inequalities follow. This is not a numerical full-recovery derivative certificate: S' and the complementary old recovery derivative remain obligations.

Reviewed complete ROOT source `input_cap_factored_forcing/PROPOSAL.md`, SHA256 `95755c3a08b6434a7ec7f86897a80f975c7575be747d1a9f09cdf34c9cce4376`. I refreshed the complete necessary physical kernel/cap sections of the endpoint and sharp-recovery sources and the complete wider-band argument. Their original physical calibration and matching premises remain conditional. No slow gate is incorporated into S in this identity: S is precisely the uncapped, two-converter input-input block at its original first-new-site planes. A later attached response must use its separate feedback equations.

## Physical convention and exact order

The actual new-port kernel is

    G_ab(m,n)=delta_ab A Q^|m-n|+Q^m T_ab Q^n,
    A=[j(Q-Q^-1)]^-1, S_ab=T_ab A^-1.

Thus T=S A, with A on the RIGHT; this is the generalized physical-amplitude scattering convention, not an assumed unitary matrix on closed incidence. The fixed real B basis makes A and Q diagonal and commuting, while T and S need not commute with either. Dirichlet deletion at site21, retaining input sites0 through20 and their original diagonal, gives the quoted X, Z and bracket. The actual physical incident coefficient is alpha=A Q^20 Bbr, as the recovery source independently identifies by comparing T_ba Q^20 Bbr with S_ba alpha. This fixes both normalization and phase origin.

Let Y=Q^-1 Z Q^-1=A Q^-2+X. Then Y^-1=Q Z^-1 Q and

    I-Y^-1(A+X)=Y^-1[Y-(A+X)]
                   =Q Z^-1 Q A(Q^-2-I).

Only diagonal A,Q factors are commuted on the RIGHT of Z^-1. In particular Q A(Q^-2-I)=A(Q^-1-Q)=-I/j, so Bbr=-Q Z^-1/j. With D=Q^21,

    Z=A+D S A D=(I+D S D)A,
    Z^-1=A^-1(I+D S D)^-1.

Consequently alpha=-A D A^-1 Fcap/j=-D Fcap/j. No S, X or inverse crosses a noncommuting factor. Existing invertibility of Z and A establishes existence of Fcap; alternatively the later rho<1 estimate proves it directly. All roots are nonzero on the retained windows, so the intermediate inverse powers are defined. The selected scalar reduction -w^21/[j(1+R w^42)] confirms the negative sign and21-step phase independently; the reflection round trip is42 steps, not40.

For finite n=0,...,20, left multiplication by Q^-n gives exactly -Q^(21-n)Fcap/j. The minimum remaining exponent is1, so no growing closed root remains. This equality is for the full forcing domain, including the forced endpoint n=20; only the bond equation has the forcing jump. The other term is Q^n beta with beta=S alpha. Its derivative must still include S' and alpha'; it is not erased by this cancellation.

## Derivative bounds and domains

The projectors P,C are fixed spectral projectors of shared B on a chosen physical window. Q(E), its powers and their derivatives commute with these projectors. For D=Q^N, N=21, ||D||=1, ||CD||<=q^N and ||CD'||<=N q^(N-1)c1. Splitting D S D into its four blocks and taking the triangle inequality gives

    ||D S D||<=r0+s0(2q^N+q^(2N))=rho.

This uses ||PSP||<=r0 and ||S||<=s0, and makes no inference from selected unitarity to closed rows. The same splitting applied to S' gives s1+(2q^N+q^(2N))swide. The remaining derivative terms D'SD and DSD' are each bounded by d1 s0. Therefore the stated K bounds the full derivative of DSD. Neumann inversion and the actual inverse derivative yield

    ||Fcap||<=f, ||Fcap'||<=f²K, f=(1-rho)^-1.

Differentiating alpha=-D Fcap/j at fixed hardware j proves its full and complementary inequalities. In the complementary estimate C acts on D and D', not on Fcap; no small bound on CFcap is assumed. Thus even cross-channel mixing inside Fcap' is retained. Equations(2) and(3) are exact product rules, not derivatives inferred from value inequalities.

The wider-band source first puts |q_angle-pi/2|<=4e-6 inside the original certified energy interval. It then establishes v_new=2j sin(q_angle)>.0053, ||Q_C||<1/60, ||S_full||<1.3 and selected reflection <1e-20+12|q_angle-pi/2|<4.81e-5. The input-input block inherits those norm ceilings. Hence rho<1 with ample margin. Narrower historical numerical margins are not needed.

For an open root |Q_P'|=1/v_new, so its Nth power derivative is bounded by N/.0053. Closed roots satisfy, by differentiating the actual dispersion at physical E,

    |Q_C'|=|Q_C|²/[j(1-|Q_C|²)]
          <=1/[.0027(60²-1)].

Their Nth-power derivative is smaller than N/.0053. Since Q is a diagonal normal matrix with fixed projectors, the full derivative norm is the maximum of these channel bounds; there is no hidden nonnormal estimate. Root signs do not alter these absolute values. Lower-lip conjugation in the fixed real basis preserves the norms and derivatives; the algebra is independently valid on each lip. These claims are restricted to the inherited physical windows and fixed positive j, not a threshold limit or moving-projector family.

The symbols s1 and swide are hypotheses on actual physical E derivatives. A small reflection or full scattering value cannot supply them. Similarly the finite old response derivative still has four terms from the fixed P/C split of Phi alpha. In particular (Phi C)' C alpha requires an actual complementary recovery derivative; the new small coefficient is not a proof of that derivative. Cable, output load and gate feedback derivatives are separate. The source correctly leaves all of these obligations explicit and makes no new Lprime or temporal claim.

## Exposure and verification limits

Root authored the new reduction. I authored the sharp-recovery ancestor and later full-recovery derivative work, and reviewed or authored other converter/endpoint ancestors. I did not author this new factorization. This review reconstructs its order, sign, physical planes and every changed inequality; shared ancestry is disclosed rather than presented as blind independence. Necessary exact kernel and cap passages were refreshed, and the complete wider-domain source was read. Unchanged original physical source/filter calibration was not rerun or blanket-recertified.

No numerical inverse, scientific runner, dynamics, sweep, parameter selection, Git/canonical/publication/checkpoint/prompt/model change or delegation occurred. Only this review was created. This is a useful algebraic reduction with explicit derivative obligations, not closure of the full prepared-recovery derivative bottleneck.

Exact reused source identities:

- `bandcenter_converter_endpoint/PROPOSAL.md`: `22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
