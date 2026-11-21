# Saturation tests for the same-threshold fill

Author: openai/gpt-6-astra/max, mac-mini-codex. Pinned source:
`6d28846d6c9052ed1937173587a32c5c9351e141`. Author mathematics, not an
independent check or audit. No numerical experiment was run. Write `t=T_2`,
`H=diag(i,-i)` and `theta_p=d(1,U_p)` in `[0,pi]`. An abelian filling
requires **every link of the candidate**, as well as the input, to lie in
this fixed U(1) subgroup. Its obstruction is not an SU(2) counterexample.

## 1. A disc: the integer cannot be silently fixed

**Discharged.** Let D be an a by b rectangular lattice disc, N=ab,
with all boundary links prescribed. The minimum over matching SU(2)
fields of the maximum plaquette angle is

    d(1,Hol(partial D))/N.                                      (D)

Proof. Removing plaquettes row by row writes boundary holonomy as a
product of conjugates of their holonomies. Bi-invariance and the triangle
inequality give the lower bound. Choose A in su(2) with
exp(A)=Hol(partial D), |A|<=pi, in the chosen orientation and based frame.
On vertices (x,y), put U_1=1 and U_2=exp(x A/N). Each plaquette is
exp(A/N), and the boundary product is exp(A). Two connections on a cycle
with identical based holonomy are related by a vertex gauge equal to 1 at
the base point: solve the gauge equation successively on the edges;
equality of holonomies is exactly its closing equation. Extend this gauge
arbitrarily to the interior. It preserves plaquette angles and gives the
prescribed boundary links exactly. QED.

**Discharged consequence.** Take commuting input angles t on D except
one t+eta, with Nt+eta<pi. An axial potential obtained by summing these
angles realizes them. The boundary forces maximum >=t+eta/N, a genuine
SU(2) counterexample if this *small* D is all that can change. This does
not refute the draft's widths: if Nt>=pi, (D) always supplies a filling
with maximum <=t. The principal boundary angle, not the unwrapped sum
Nt+eta, is the lower bound. In U(1) a 2pi integer change is allowed; in
dimension two there are no cubes imposing a closure condition on it.

**Discharged (two-dimensional mesh version).** Fix 0<t<=1 and
n=ceil(sqrt(pi/t)). On a finite rectangular mesh in dimension two with
integer side lengths in [n,2n], prescribe a subcomplex with fine plaquette
angles <=t. Choose unprescribed coarse-edge links arbitrarily, then fill
each unprescribed coarse face by (D). Its fine angles are <=pi/n^2<=t,
and boundary links agree exactly. If V has flux <=t off X, select precisely
the coarse faces meeting X and prescribe the others; modifications stay
within 4n of X in l^1. Prescribed whole frozen mesh cells are preserved.
Thus saturation gives no counterexample for this
geometry at sufficiently large fixed multiple of t^(-1/2). Arbitrary
internal frozen edges are not covered.

## 2. Four dimensions: one defect defeats every abelian filling

**Discharged (U(1) only).** For every 0<t<pi/6 and every finite radius r,
there is a finite four-torus and a U(1) field V with exactly one plaquette
above t such that no U(1) field W has angles <=t and agrees with V on all
bonds outside the radius-r neighbourhood of that plaquette. The torus is
chosen *after* t,r, and can be arbitrarily large. This includes every
finite r(t), even r(t)>>t^(-1/2). There are no frozen bonds.

Construction. On a sufficiently long periodic x_1 lattice choose a real
periodic h with increments +1 on an interval containing
[-r-10,M+r+10], increments -1 on a disjoint interval of equal length,
and increments 0 elsewhere. Here M>4r+40. Sum the increments to define h.
Choose transverse periods >8r+80. Put a_2^0(x)=t h(x_1), all other
components zero. Its curls are 0 or +/-t, with F_12=t on that interval
on every transverse slice. Add to a_2 the real 1-cochain

    eta * 1_{1<=x_1<=M} * 1_{x_2=0} * 1_{x_3=0} * 1_{x_4=0},
    eta=t/2,

and set V_mu=exp(H a_mu). The 12 curls acquire +eta at
p_0=(0,0,0,0;12) and -eta at p_1=(M,0,0,0;12). The 23 and 24 curls
are 0 or +/-eta along the intervening strip. Other curls are unchanged.
All curls have magnitude <pi, so they are exactly the signed principal
fluxes. Only p_0 has angle >t, while p_1 is outside the tube. Bianchi
holds on every cube since these fluxes are the real cochain da. Thus a
single above-threshold plaquette is possible: regular mixed plaquettes
carry the return flux.

Proof. For a putative abelian W let f^W be its signed principal angles
in [-t,t]. Around a cube their oriented sum is 2pi times an integer.
Its magnitude is <=6t<2pi, so the integer is zero and df^W=0 as a real
cochain. Also df^V=0. Thus b=f^W-f^V is closed and supported on
plaquettes within r+2 of p_0 (enlarge this fixed buffer for the bond
assignment convention). On a transverse slice put

    S(z,w)=sum_{x_1,x_2} b_12(x_1,x_2,z,w).

Summing (db)_123=0 over x_1,x_2 cancels the two periodic tangential
differences and gives S(z+1,w)=S(z,w). The 124 equation similarly gives
S(z,w+1)=S(z,w). A slice outside the support has S=0, hence every slice
does. But on (z,w)=(0,0), every possibly changed 12 plaquette has
f^V=t except p_0 with t+eta. Their contributions are <=0, with <=-eta
at p_0. All other contributions vanish, including at fixed p_1. Thus
S(0,0)<=-eta, a contradiction. QED.

For the draft tube around a singleton choose r larger than 2d_x+t_0
and a fixed cell/plaquette assignment buffer, then choose the torus.
This defeats the *abelian* statement at every permitted finite width;
widening the tube by any finite volume-independent factor does not fix it.
No numerical test was used.

## 3. Closed sheets and frozen ends

**Discharged (closed product-sheet control).** Make the perturbation
independent of x_3,x_4. The high 12 plaquette is now a dual sheet wrapping
both transverse circles. Choose a 12 rectangle D around it, excluding
p_1, inside the allowed tube, with |D|t>=pi. Apply (D), with a U(1)
logarithm and U(1) boundary gauge, identically on every transverse slice,
and set U_3=U_4=1. The correction sheet closes; mixed plaquettes are 1;
every cube satisfies Bianchi; the maximal angle is <=t. The support lies
in D times the transverse torus. This rules out the closed flat product
sheet as a counterexample, not arbitrary curved closed sheets.

**Discharged (abelian sheets with an end).** Replace the two transverse
singleton indicators in Section 2 by the indicator of a proper transverse
rectangle S. The high plaquettes form a finite sheet; mixed plaquettes
on its boundary remain <=eta. If its tube misses a transverse slice,
the same conserved S(z,w) forbids an abelian fill. One may instead fix a
whole transverse 12 slice outside S: unchanged signed flux there again
forces S=0, so the correction cannot end on that frozen slice. This
frozen data can have flux t. It need not be **quiet** in the draft's
stronger sense, nor a union of whole frozen bricks. No such claim is made.

**Gap (quiet frozen end).** For a sheet ending at quiet whole frozen
bricks, the relative cycles and the slack near its end must be checked
using the actual bond convention. An integer vortex correction may end
only on an allowed relative boundary. Adding one independently on every
disc does not check this. No matching SU(2), quiet-frozen-brick
counterexample or extension is established here.

## 4. The precise SU(2) limitation

**Discharged logical limitation; gap (EXT=).** The abelian proof uses
real scalar closure and conservation of S. SU(2) plaquette holonomies on
a cube are multiplied after parallel transport; their logarithms are not
an additively closed real 2-cochain. Small angles alone do not make them
closed in one fixed color direction. The original V is abelian, but W
can leave that subgroup. No argument here forces it back, and no bound
on the noncommuting terms restoring the contradiction is proved. A
non-abelian core is an unexcluded escape. The original SU(2) inequality
is therefore **gap**, not refuted. A count of failed attacks establishes
no impossibility theorem for it.
