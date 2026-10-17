# Autonomous record route: selective local construction check

Disposition: support for the stated local stationary gate and its conservative finite-band scattering estimate. No load-bearing error found in the terminal/mixer phases, two-cell repair, explicit local geometry or full-space positive blocks. This is not a complete-device temporal theorem or an all-time heralded completion certificate. The proposal identifies those missing interfaces correctly.

## Source and scope

Read the complete ../autonomous_record_route/PROPOSAL.md and verified SHA256 93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56. The idea, claimed construction and intended result were exposed before reconstruction. I am independent of this proposal's author, not blind to its argument. My prior temporal and finite-composition reviews supply context, not evidence for an attached gadget's runtime. The earlier frozen canonical source identity 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff and wider-band identities d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 / 3f721b75911630e0aec48688893c6bae84a182cafaa1012c977e9e262d6e180d remain exposed ancestry, not newly re-audited results. The local calculation below is reconstructed directly from the supplied blocks.

Applicable unchanged instructions/workflow are reused. No scientific execution, numerical solver/run, delegation, W/Git/checkpoint/prompt/model edit or publication occurred. Only reading, hashing and this report were performed. No editable prompt file changed.

## Terminal and phase-cell calculation

In the record-X sector x=+/-1, the endpoint equation is E psi_0=(2j+jx)psi_0-j psi_1. Substituting psi_n=w^-n+r w^n and E=2j-j(w+w^-1) gives

    r=-(x+w)/(x+w^-1).

At w=i this is -i for x=+1 and +i for x=-1, hence -i X_R. In fact the stronger exact interior-band identity is r_+=-w and r_-=w, so r_terminal=-w X_R for 0<q<pi. This is an optional sharpening, not a correction needed by the proposal: its <=3x deviation from -i X_R is conservative. The endpoint contact does not implement irreversible writing; it implements a coherent X on arbitrary record input after stationary reflection.

For a phase cell, the extra occupations plus the strengthened bond and the two neighboring ordinary bonds give diagonal 3j on each cell site. At q=pi/2, left-site incoming/reflected amplitude 1+a and right-site amplitude b obey exactly the two equations in the proposal. Their difference forces a=0 and b=(1+i)/sqrt(2). Relative to the free one-edge transmission i, eta=(1-i)/sqrt(2). Symmetry gives the same transmission from the other direction and zero reflection. A double traversal gives eta squared=-i; two separated cells give eta to the fourth=-1. No intercell return survives at the center, and their existing free propagation remains included in the common arm length.

The mixer transforms the physical two arms into two independent lead continuations because U is real orthogonal and its square is I. With terminal-to-attachment distance L=10, the port-origin reflection factor is w^(2(L+1))=w^22. Therefore the arm return matrix at the center is diag(i X_R,-i X_R), and U diag(1,-1) U^T=X_port gives S=i X_port tensor X_R. The claimed common +i phase and absence of same-port reflection are correct in the stated reference planes.

## Finite-band bound

For real v, differentiating r_v=-(v+jw)/(v+j/w) gives

    |r_v'|=2j |j+v cos(q)| / |v+jw| squared.

Since |j+v cos(q)|<=|v+jw| and |v+jw|>=j sin(q) on this band, |r_v'|<=2/sin(q)<3. This is uniform over the terminal and cell parity potentials. The symmetric cell's two parity reflection eigenvalues have potentials j(1-sqrt(2)) and j(1+sqrt(2)); half-sum/half-difference give its physical reflection/transmission. Thus |a|<=3x, |b'|<=3, and B=b/w satisfies |B'|<=4 using real-axis unitarity |b|<=1. It follows that |B-eta|<=4x and |B squared-eta squared|<=8x.

For a unit-modulus terminated load, cell concatenation has a direct reflection of size <=3x and a repeated-return denominator bounded below by 1-3x. After extracting the free bond phase, subtraction of eta squared times the unmodified return is bounded by 3x+(8x+3x)/(1-3x). For x<=.001 this is <=15x. Propagation between cells is unimodular, and the first transformed terminated load is again unit modulus. Applying the estimate twice therefore gives <=30x relative to minus the unmodified arm return; no derivative bound on that load is required.

Adding the terminal estimate gives arm discrepancies <=3x and <=33x relative to the target -i w^22 X_port tensor X_R. Orthogonal mixer conjugation preserves the norm, so the complete two-port/record bound <=33x is valid. At x<=4e-6 it is <=1.32e-4. This is an amplitude/operator estimate including wrong port and wrong record, not a probability-only statement. All zero-displacement inequalities are properly non-strict. The stronger exact terminal identity could improve constants but is unnecessary for the claimed ceiling.

## Geometry, positivity and counts

Both listed arms have eleven vertices and ten unit cubic edges. Arm0's detour has four vertices through (1,1,0), followed by seven through (1,8,0); arm1 has nine vertices through (-1,8,0), then two to (0,8,1). They are disjoint from each other, the record and the two port vertices. All four mixer edges are unit edges of the displayed square. Both terminal contacts are nearest neighbors of the one shared record. The phase-cell edges at y=2--3 and y=5--6 have distinct endpoints and ordinary neighbors. The external lead rays introduce no local vertex collision. Selective installed coupling is required: additional geometric adjacency alone does not install another edge.

The local count 22 arm vertices+2 port vertices=24 head vertices and 20 arm edges+4 mixer edges=24 head-hopping edges is correct. There is one additional record qubit, not one per arm. Contacts with that record are physical interaction blocks but are not head-hopping edges. The inventory has 18 ordinary arm bonds, two replacement phase bonds and four mixer bonds, plus four phase occupations, four mixer vacancies and two terminal contacts: 34 local positive blocks in this displayed decomposition, before external lead bonds. This additional bookkeeping does not count the unspecified connecting cable.

Each Q(h) is PSD on the full pair space with norm 2|h| for either sign of h. The phase occupations are positive because 2-sqrt(2)>0. Each terminal term j n_T(I+X_R) is PSD on the full head/record space with norm 2j, despite not conserving record excitation. It conserves head excitation. The two contacts share the same X_R and commute with it, so resolving record-X sectors is exact, not a duplication of the record. Their incident-block norm sum on R is 4j.

At each mixer vertex the two square bonds contribute sqrt(2)j and the external arm/lead bond contributes j to the occupation diagonal. Subtracting gamma=(sqrt(2)-1)j via gamma(I-n) leaves 2j plus its scalar gamma. Four vacancies therefore contribute exactly c_R=4(sqrt(2)-1)j. The cells and contacts add no vacancy scalar. All listed terms are static, real and at most two-qubit; the full-space identities are not restricted to the one-head sector. A controlled exchange multiplied by X_R would instead be three-body on distinct head endpoints and record, and is not supplied here.

## Parity observation and completion limits

The parity obstruction holds for the quantified arrangement: terminals adjacent to the same cubic record vertex have equal parity, as do the two opposite-corner arm attachments. Each terminal-to-attachment path therefore has the same length parity, even after detours. An odd difference is impossible within those premises. A hopping sign traversed in both directions cancels from the round-trip phase. This is not a no-go for other junctions, layouts, extra degrees of freedom or completion mechanisms; the proposed positive phase cells already avoid it within the same length parity.

The supported result is stationary scattering by this isolated local gadget with ideal leads and supplied initial record. It does not justify appending it and adding 1.32e-4 to the previous full-device error. Attachment changes return Green functions, closed loads, spectral mass and possible localized states. The enlarged record fiber has two conserved X sectors which must be recombined coherently; the full system cannot inherit a rank-one selected-channel theorem without that work. The unspecified connecting cable also lacks a frozen geometry, phase, count and finite-cut convention. No onset or finite horizon follows here.

Record1 is not currently an all-time completion herald. While the head visits a terminal, its j n_T X_R coupling produces a record1 amplitude before the head has reached the designated output. For example the local first-order evolution of a terminal-occupied |0> includes -i j dt times the same terminal-occupied |1>; this demonstrates failure of any automatic logical implication from record1 to blank apparatus/output occupancy, without asserting a quantitative early-event probability for the actual emitter seed. An eventual full-device heralding theorem would have to bound those events for that seed at all relevant times. Once contact occupation vanishes the ideal free record has no further rotation, but a returning head can toggle it back. A finite device has not thereby acquired a stable irreversible latch.

The proposal explicitly acknowledges these distinctions. A future finite-window record-output theorem would still not remove its observation window or establish an arbitrary-time heralded map. Native Record identification, record initialization/readout supply, physical units, coefficient realization, permanent stability and reset remain open. Within its local stationary scope, the construction and stated bounds are supported; no broader completion claim is certified.
