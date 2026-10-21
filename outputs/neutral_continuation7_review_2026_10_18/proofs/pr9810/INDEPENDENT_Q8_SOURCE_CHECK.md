<!-- Original PR9810 source SHA256 e98594a8d2f239014de5e4af6556d0d2c98e8607a39ea3628f7c93dd21f69494. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Focused check: Q8 original-source coefficient

The proposed order-lambda^18 coefficient is correct in the retained native N0 frame, under the stated two-intermediate geometry and source derivatives. The high-wall canonical-frame connection contributes only later to this transition. A subsequent flux-block-diagonal frame must not drop its own connection; the calculation below deliberately stays before that reduction.

## Explicit matrix-element calculation

Use basis 0, I1, I2, S with diagonal energies 0,E,E,F and off-diagonal entries -t1 between 0 and either I, and -t2 between either I and S. Let a prime denote the uniform source derivative at h=0. To second order in t, the relevant normalized eigenvectors have components

|g> = |0>+(t1/E)(|I1>+|I2>)+[2t1 t2/(FE)]|S>+...,

<S_exc| = <S|-[t2/(F-E)](<I1|+<I2|)
 +[2t1 t2/(F(F-E))]<0|+... .

Normalization corrections affect the requested source element only at higher hopping order. Direct insertion of H' gives

<S_exc|H'|g>
 =2t1 t2 [F'/(FE) - (t2'/t2)/E
          +(t1'/t1)/(F-E) - E'/(E(F-E))]
 + higher hopping order.

This includes the derivative of both hopping legs and the diagonal derivative; retaining only F' times the ground S component would fail even for independent excitations. In the additive limit F=2E and t1=t2 with identical derivative ratios, the entire displayed expression cancels exactly.

## Binding correction

Set F=2E+U, E'/E=3/J, U'/U=5/J, t'/t=A/(2J). Expanding to first order in U/E gives

amplitude_binding = (t^2 U/(J E^2))(8-A).

With U=-3J D lambda^6, E=J Delta lambda^4 and t=J gamma lambda^10, this is

3D(gamma/Delta)^2(A-8) lambda^18.

The sign is the one in the root expression. The negative binding U combines with 8-A, rather than with A-8 directly.

## Detour correction

At U=0 let t1=t+2d_phys, t2=t-2d_phys, where d_phys=J d lambda^12. If d_phys'/d_phys=B/J, then

(t1'/t1)-(t2'/t2)
 =4(d_phys/t)(B-A/2)/J+O((d_phys/t)^2).

The matrix element above reduces to 2t1t2 times this difference divided by E. Hence

amplitude_detour = [8 gamma d/Delta](B-A/2) lambda^18.

The product of the detour correction and U/E is two further powers of lambda and is not part of the displayed order. Thus the total proposed coefficient is their sum. Here C is the unnormalized uniform source; apply any separately specified volume normalization afterward.

## Canonical connection order

For the high-wall reduction U(h), the derivative of the retained Hamiltonian differs from the matched original observable by a commutator with A_h=(partial_h U)U^dagger (up to the chosen sign convention). In a real, symmetry-preserving analytic frame this connection is real antisymmetric. Its diagonal N0 entries vanish. Its first off-diagonal matrix element changing two full height-ten columns needs at least twenty physical flips, hence at least ten transverse insertions: it is O(lambda^10/J). The h derivative changes diagonal energies/denominators but does not supply missing spin flips.

Multiplication by the Q4 or Q8 diagonal energy difference, O(J lambda^4), makes the corresponding two-column source correction O(lambda^14). To connect the exact vacuum and this two-pair Q8 state it must additionally use one hopping admixture t/E=O(lambda^6), giving O(lambda^20), later than lambda^18. A direct connection changing all four columns begins no earlier than lambda^20/J and its commutator is later still. Lower diagonal connection entries cannot evade this count because they vanish in the real frame. Terms involving off-diagonal Hamiltonian entries likewise do not lower the order.

This argument concerns the native N0 frame obtained by eliminating order-J wall excitations. A further Q-sector rotation has small-denominator generators of order lambda^6 and a nontrivial source connection already at the leading winding-source order. One may use that frame only by transforming the observable consistently. The direct eigenvector insertion above avoids that pitfall and explicitly includes ground and excited-state mixing.

## Scope

The coefficient assumes the specified two equivalent intermediate states, the established binding U and the independently checked plaquette-dependent detour. Any additional same-order native path or source term outside that established local classification would have to be included; this algebra alone does not classify the full Q8 spectrum. It establishes neither a Q8 pole nor a transition rate. The source is the derivative of the original microscopic observable, not an added physical interaction.
