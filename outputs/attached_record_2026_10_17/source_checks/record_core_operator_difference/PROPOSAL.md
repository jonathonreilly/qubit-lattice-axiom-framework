# Record-projected complete-core difference: exact Schur formula and spectral interface

Status: authored conditional operator interface, awaiting a separate check. No attached-record apparatus is asserted to satisfy its bounds. The decisive formula is

    F_+-F_- = [ kappa² T_+ DeltaG T_- ;
                -kappa DeltaL T_-
                -kappa³ L_+ T_+ DeltaG T_- ].           (1)

Here the upper block includes every emitter internal coordinate and the lower block includes all chosen finite source/core coordinates. Sector labels +,- are NOT upper/lower spectral boundary labels. The emitter difference has the scalar mechanism's kappa² numerator, with noncommuting factors kept in order. The source difference also has a direct kappa DeltaL term with ONE resonant inverse. This term does not cancel merely because DeltaG is small or zero. A useful all-time absolute core-map bound requires control of both DeltaG and DeltaL, full background recovery, BOTH boundary lips, and the actual omitted seed spectral amplitude.

## 1. Exact block setting, common seed and retained old system

Let F be the full finite-dimensional emitter internal fiber, including the literal old and source registers. Let B be the common background Hilbert space. Supply two bounded self-adjoint conserved-record-X sectors on F direct_sum B:

    H_s = [[H_e, -kappa V*],[-kappa V,H_b,s]],
    s in {+,-}, kappa real, V:F->B an isometry.

H_e and V are the SAME in both sectors. All shared K dynamics, source interactions and physical scalar offsets belong to these actual blocks. They need not commute. A differing emitter block or coupling requires additional difference terms and is not hidden inside (1).

Let S0:O->F be the fixed isometric embedding of arbitrary old input O into the prepared emitter/source internal seed, and E_e:F->F direct_sum B the emitter inclusion. Set S=E_e S0. Let Q:B->C be the coordinate restriction onto ALL selected finite background vertices, with all their internal coordinates; Q is a contraction, and C may be their orthogonal direct sum. Define the full core restriction Pi=diag(I_F,Q). Thus the retained core includes the full emitter, all finite source vertices, converters/cables/gadget positions chosen for the application, and any other finite vertices included in Q. No per-site count is assumed to be free. Infinite asymptotic tails are not automatically included by this finite-core statement and need their own bound if the final output contract requires them.

The exact record Hamiltonian is H_+ tensor |+><+|+H_- tensor |-><-| with initial record |0> and final |1>. Identifying the final record factor with |1>, the core map is

    C1(t)=(1/2) Pi[exp(-itH_+)-exp(-itH_-)]S.           (2)

It maps the ENTIRE old space to all selected core coordinates. It is not an expectation against the initial emitter vector. Tensoring a passive reference is understood throughout and preserves every stated operator norm.

## 2. Exact operator identities and the uncancelled source term

For z off the real axis let

    R_b,s(z)=(z-H_b,s)^-1,
    G_s=V*R_b,s V, L_s=Q R_b,s V,
    D_s=z-H_e-kappa² G_s, T_s=D_s^-1.

The exact emitter-to-core resolvent column is

    F_s(z):=Pi(z-H_s)^-1 E_e=[T_s;-kappa L_s T_s].     (3)

The minus sign follows from the positive off-diagonal kappa V in z-H_s. Set DeltaG=G_+-G_- and DeltaL=L_+-L_-. The resolvent identity, without commuting any factor, gives

    T_+-T_-=T_+(D_--D_+)T_-
             =kappa² T_+ DeltaG T_-.

Expanding L_+T_+-L_-T_-=DeltaL T_-+L_+(T_+-T_-) proves (1). An equally valid asymmetric alternative uses DeltaL T_+ and L_-(T_+-T_-); one may choose whichever recovery bound is better. The emitter contribution is order kappa² times TWO inverses, while the source contribution has both the direct one-inverse term and a three-kappa two-inverse term. Subtraction of scalar self-energies cannot eliminate the direct recovery difference.

For each boundary lip sigma in {up,down}, suppose these boundary values exist almost everywhere on a declared energy set I and put

    u_s^sigma=||T_s^sigma||,
    g^sigma=||DeltaG^sigma||,
    l_D^sigma=||DeltaL^sigma||, l_+^sigma=||L_+^sigma||,
    e^sigma=kappa² u_+^sigma g^sigma u_-^sigma,
    b^sigma=|kappa| l_D^sigma u_-^sigma
            +|kappa|³ l_+^sigma u_+^sigma g^sigma u_-^sigma.

The full-fiber column difference obeys

    ||F_+^sigma-F_-^sigma||
       <=r^sigma:=sqrt((e^sigma)²+(b^sigma)²).          (4)

Orthogonality of emitter and background ranges justifies this square-sum upper bound. It does not assume orthogonality between the two terms within the background block. All G,T norms act on the full emitter fiber, and L norms recover the whole chosen finite core, not a favorable scalar column.

## 3. The actual spectral jump requires both lips

For a self-adjoint H_s the cross spectral measure is the operator-valued measure

    M_s(Borel set)=Pi E_(H_s)(Borel set) S.

It is generally neither positive nor a scalar probability measure. Require that its restriction to I is absolutely continuous with a Bochner-integrable operator density and the ACTUAL boundary formula

    M_s'(E)=[F_s^down(E)-F_s^up(E)]S0/(2pi i).         (5)

This is an explicit spectral regularity/synthesis hypothesis, not a consequence of writing (3). A sufficient stronger application condition is absolute continuity of every seed spectral component on I together with limiting-absorption control establishing (5) and its integrability. Cutoff atoms and other singular local contributions must either be excluded by proof or put in the remainder. Purely algebraic Schur denominators do not establish this alone.

For an off-diagonal column,

    [(E-i0-H_s)^-1]_(core,e)
       = ([(E+i0-H_s)^-1]_(e,core))*.

It is NOT the adjoint of the upper core,e column, and replacing it by an ordinary operator imaginary part of that rectangular column is invalid. One must bound both the lower column and upper column as used in (4). Equivalently, the lower bounds can come from controlled upper recovery ROWS. Since G_s^down=(G_s^up)*, the full-fiber u_s and g bounds transfer between lips; L_s^down=Q R_b,s^down V=(V*R_b,s^up Q*)* requires the reverse row. An upper-column bound alone does not supply that row for general complex H_b,s.

If the actual H_b,s,V,Q are real in fixed conjugations, there is a separate valid simplification: lower columns are conjugates of upper columns (with the domain/range conjugations), so their norms and sector-difference norms agree. This must be a verified real-structure premise. Even then (5), not a scalar seed density, is the synthesis identity. Arbitrary complex old input is still allowed.

## 4. Uniform absolute bound on the whole finite core

Require omitted SEED spectral amplitudes

    ||E_(H_s)(R\I)S||<=epsilon_s.                     (6)

Here I may be a finite union of physical energy intervals. Any locally singular contribution not represented by (5) must be included in the omitted part by an explicitly corresponding spectral projection/decomposition. For definiteness the formulas below use (5) on all of I and (6) on its complement.

Combining (2),(5), Bochner's inequality and (4) gives, for every real t,

    ||C1(t)||
      <=min{1, (epsilon_++epsilon_-)/2
                   +(1/(4pi)) integral_I
                          [r^up(E)+r^down(E)]dE}.      (7)

The factor 1/2 is the record-basis factor, and 1/(2pi) is the full spectral jump normalization. The remainder bound follows from Pi being a contraction, spectral projections commuting with their own unitary evolutions, and (6). These epsilons are amplitudes, not scalar masses: positivity of a scalar return measure cannot replace (6). If instead an operator seed-mass bound ||S*E_(H_s)(R\I)S||<=m_s is established, then epsilon_s=sqrt(m_s) suffices exactly. Cross-sector or upper/lower cancellations can improve (7), but none are assumed.

An alternative useful estimate integrates emitter and background bounds separately. Let

    Ecore=(1/(4pi)) integral_I (e^up+e^down),
    Bcore=(1/(4pi)) integral_I (b^up+b^down).

Their physical ranges are orthogonal, so another valid right-hand side is (epsilon_++epsilon_-)/2+sqrt(Ecore²+Bcore²), capped by one. This controls emitter PLUS all retained source coordinates, not merely the initial seed projection. It supplies one sufficient local-error input to a complete herald theorem; it supplies no downstream correct profile, return-ray bound, success lower bound or normalized conditional correctness by itself.

All integrals use one common physical energy E for each sector. If old input energies are b_j, an application may take a union of windows centered near Ee+b_j and prove these full operator bounds on each window. It must not apply four favorable scalar estimates and combine them by a maximum when the error columns overlap. In the present formulation full operator norms and S retain the complete old input from the outset. No factor exp(-itK) has been pulled through a noncommuting source resolvent or through (5). Such a factorization would require a separately proved column parameterization and common comparator, and is unnecessary for (7).

## 5. Transparent one-window sufficient envelopes and scaling

For one window |delta|<=d, delta=E-Ec, suppose BOTH lips and BOTH sectors satisfy full-fiber bounds

    u_s^sigma<=1/[c sqrt(delta²+gamma²)],
    g^sigma<=a_G+b_G|delta|,
    l_D^sigma<=a_L+b_L|delta|, l_+^sigma<=L0,

with d,gamma,c>0 and all a,b,L0 nonnegative. These are hypotheses to prove for the actual attached device; no device-specific values are assigned here. Define

    I_G=2a_G arctan(d/gamma)/gamma
                        +b_G log(1+d²/gamma²),
    I_L=2a_L asinh(d/gamma)
                        +2b_L[sqrt(d²+gamma²)-gamma].

These are exact integrals of (a_G+b_G|delta|)/(delta²+gamma²) and (a_L+b_L|delta|)/sqrt(delta²+gamma²), respectively. Equations (4)–(7) imply

    Ecore<=kappa² I_G/(2pi c²),
    Bcore<=|kappa| I_L/(2pi c)
                         +|kappa|³ L0 I_G/(2pi c²).     (8)

Hence sqrt of their squares plus the amplitude remainder is a sufficient all-time bound. The scalar return formula is recovered only in its emitter expectation subcase; the background term is additional and cannot be suppressed by notation.

If gamma=eta kappa², eta and c are uniformly bounded below, d is bounded, and the envelope coefficients are uniformly controlled as kappa tends to zero through positive values, these upper bounds have the scales

    Ecore=O(a_G+kappa² b_G log(1/|kappa|)),
    Bcore=O(|kappa| a_L log(1/|kappa|)
             +|kappa| b_L d
             +|kappa| L0 a_G
             +|kappa|³ L0 b_G log(1/|kappa|)).           (9)

The source direct term has the weaker kappa-log mechanism, not the emitter's kappa²-log mechanism. Its on-resonance pointwise size can be of order a_L/|kappa| even while its finite-band integral shrinks for uniformly bounded a_L. A nonzero self-energy floor a_G gives an O(a_G) emitter contribution. If L0, a_L, inverse conditioning or omitted seed amplitude deteriorate with kappa, no small-limit conclusion follows. In particular a second background resonance can invalidate uniform recovery bounds. These are sufficient envelopes, not claimed sharp asymptotics of an actual device.

At kappa=0 and common H_e the initialized emitter never enters the background and the sectors agree there, so C1(t)=0 directly. A resonance parametrization with gamma proportional to kappa² must not be substituted at zero into (8). For gamma>0, every displayed finite-window integral is regular; a bound above one is simply capped.

## 6. Exact algebraic discriminator: identical endpoint self-energy is insufficient

Take a scalar emitter fiber, background basis b,y, V=|b>, Q=<y|, and

    H_b,+=[[b0,h],[h,b1]], H_b,-=[[b0,-h],[-h,b1]],
    H_e=Ee, kappa h nonzero,

with all parameters real. The background diagonal sign transform diag(1,-1) fixes V. Thus G_+=G_- exactly while L_-=-L_+ with

    G_s=(z-b1)/[(z-b0)(z-b1)-h²],
    L_+=h/[(z-b0)(z-b1)-h²].

The common emitter T is identical. Equation (1) gives zero emitter difference but source difference -2kappa L_+T, generally nonzero. The actual record-1 y amplitude begins as kappa h t²/2+O(t³), obtained by the two-step emitter-to-b-to-y path. This confirms the direct recovery-difference term with an actual real self-adjoint model. It is an algebraic discriminator, not an example satisfying the absolutely continuous spectral hypotheses: this finite model has point spectrum, which would have to be charged by (6). No conclusion from (7) is improperly applied to it.

## Precise remaining application obligations and exposure

To use this interface, the attached-device analysis must supply: exact conserved record sectors and common emitter/coupling; full physical-energy G and BOTH recovery columns/rows for all selected source vertices; full-fiber T bounds with all emitter complements; actual operator spectral synthesis and local singular-mass handling; omitted seed spectral AMPLITUDES; and uniform recovery/conditioning constants if small-kappa scaling is claimed. Complete closed tails, other open rays and the common downstream old-system target remain separate inputs to the full herald contract. Shared K is retained throughout; no new old-encoding or phase alignment is introduced.

Read the complete autonomous_record_herald_route/PROPOSAL.md, SHA256 653e37a16d328af0f02f38ae08c18a41716cd69236a39d60fb59e0fe0d4469b7, especially its local-resonance and matrix-Schur sections. Reused record_emitter_resolvent_difference/PROPOSAL.md SHA256 c8a2880f3210446f6fbf839a5d2f7d1d01afc493be2a61dddec7a2a4df1d1047 and my scalar review ade88e55d824b18744fe1d7bea686baa89225dbf4cea7cd40b99d6d9d8dac06e, whose projection counterexample motivated keeping the entire core. Those hashes were verified. Root requested this operator extension and explicitly emphasized both spectral lips and noncommuting K. This is exposed author derivation, not an independent check of itself or of the attached-record device.

Previously read applicable AGENTS/workflow instructions are reused. No scientific execution, solver, experiment, new agent, parameter choice, W/Git/publication/model/prompt/checkpoint modification occurred. Only source inspection, hashing and this sole proposal were performed. The next independent check should reconstruct the ordered identity (1), rectangular-column jump (5), normalization/remainder factors in (7), and exact integrals and uniformity in (8)–(9).
