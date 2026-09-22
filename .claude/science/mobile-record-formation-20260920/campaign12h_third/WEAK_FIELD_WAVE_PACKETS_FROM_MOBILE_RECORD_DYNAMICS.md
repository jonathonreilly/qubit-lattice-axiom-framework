# Weak field wave packets from the supplied mobile-record construction

Status: author conditional derivation with finite controls; independent check
pending. The compact-rotor input below depends on the separately provisional
large-spin and uniform-local-dynamics packets. This note proves a finite-box,
prepared-packet harmonic limit of that rotor input. It does not infer a
thermodynamic phase or select this construction from the minimal site axioms.

## 1. Concrete result and its order of limits

The supplied record construction has a candidate compact-rotor limit

\[
 H_{\rm rot}=K\sum_e E_e^2-J\sum_p(W_p+W_p^\dagger),
 \qquad \operatorname{div}E=0.                                      \tag{1}
\]

Here \(E_e\in\mathbb Z\), \(U_e=e^{iA_e}\), and \(W_p=e^{i(CA)_p}\) is
the oriented plaquette product. The previous packet obtains both terms from
virtual hard-core record motion, with growing link spin, supplied energy
scales and a local dressing of the initial matter-field state. Its proof
obligations and independent-review status remain dependencies of this note.

On a finite three-dimensional cubic torus, choose the further scales

\[
 K={c g^2\over2a},\qquad J={c\over2a g^2},\qquad c,a,g>0.             \tag{2}
\]

In the zero electric-winding sector, explicitly prepared packets near a flat
connection evolve, for fixed times, within \(O(g^2)\) in vector norm of a
finite collection of free transverse harmonic oscillators. There are

\[
 2(V-1)\quad\hbox{real oscillators},\qquad
 \omega(k)={c\over a}\sqrt{4\sum_{\mu=1}^3\sin^2(k_\mu/2)}           \tag{3}
\]

with two polarizations for each nonzero lattice momentum. For a fixed
physical periodic box and finitely many fixed physical momenta, their
frequencies tend to \(c|k_{\rm phys}|\) as the spacing tends to zero.

The full conditional composition takes the limits in this order:

1. link spin \(S\to\infty\) at fixed finite box, \(g,a,c\), with the
   record penalty, hopping, birth rate and initial dressing from the
   large-spin packet;
2. \(g\to0\) at that fixed finite box and spacing, for the packets defined
   below;
3. \(a\to0\), through even lattice sides at least six, at fixed physical
   box size, for a fixed finite set of oscillator excitations.

This is a prepared free-wave consistency construction. It does not establish
a simultaneous volume/weak-coupling limit, a stable photon phase at fixed
parameters, interacting charged matter, gravity, or a prediction for \(c\).

## 2. Remove gauge and harmonic zero directions explicitly

Let \(B:\mathbb R^{3V}\to\mathbb R^V\) be the outgoing-minus-incoming
divergence matrix and \(C:\mathbb R^{3V}\to\mathbb R^{3V}\) the oriented
plaquette curl. Then \(CB^T=0\). Let \(\mathcal H\) be the three-dimensional
space of constant link fields, one for each direction, and define

\[
 \mathcal S=(\operatorname{im}B^T\oplus\mathcal H)^\perp,
 \quad r=\dim\mathcal S=2(V-1),\quad
 \Gamma=2\pi P_{\mathcal S}\mathbb Z^{3V}.                           \tag{4}
\]

All matrices defining these subspaces have rational entries, so the
orthogonal projection has rational entries. Its image of the integer lattice
is a discrete full-rank lattice in \(\mathcal S\). Thus

\[
 \mathcal Q=\mathcal S/\Gamma                                       \tag{5}
\]

is a compact flat torus with a positive injectivity radius at each fixed
finite lattice. Wavefunctions invariant under gauge translations and constant
link translations identify with \(L^2(\mathcal Q)\). In the electric basis,
this is exactly \(BE=0\) and \(\sum_xE_{x,\mu}=0\) for each direction.
For a divergence-free integer field, the latter fixes all three electric
winding fluxes to zero. We use the induced flat volume measure on the quotient;
its constant normalization is absorbed in this identification.

The curl annihilates the removed subspaces. Consequently

\[
 CP_{\mathcal S}=C,\qquad C\Gamma\subset2\pi\mathbb Z^{3V},          \tag{6}
\]

and the plaquette cosines are well-defined on the quotient. At the origin,

\[
 D=(C^TC)|_{\mathcal S}>0.                                         \tag{7}
\]

One can check this without a phase assumption: Fourier transformation gives
one gradient null direction and two equal positive curl eigenvalues at each
nonzero momentum, and the three constant null directions at zero momentum.
We use a coordinate neighborhood of this minimum; we do not require a
classification of all compact minima or a ground-state localization theorem.

The zero-winding restriction is made on the target field and its initial
packet. Microscopic matter hopping and live births need not preserve a
field-only winding number during virtual excursions. The previous comparison
controls their effect after dressing and taking its stated limit.

## 3. A finite-box wave-packet theorem

Subtract the constant \(-2J\) per plaquette from (1), which changes only a
global phase. The shifted operator on \(L^2(\mathcal Q)\) is

\[
 H_g={c\over2a}\left[-g^2\Delta_{\mathcal Q}
       +{2\over g^2}\sum_p(1-\cos(CA)_p)\right].                    \tag{8}
\]

On the real vector space \(\mathcal S\), define

\[
 H_{\rm h}={c\over2a}(-\Delta_x+x^TDx).                            \tag{9}
\]

Let \(\psi\) be a normalized finite linear combination of its Hermite
eigenstates. Fix a real \(C^\infty\) cutoff \(0\le\chi\le1\), supported
strictly inside an injective coordinate ball of \(\mathcal Q\) and equal
to one on a smaller ball around zero. The explicit packet map is

\[
 (I_g\psi)(A)=g^{-r/2}\chi(A)\psi(A/g),                            \tag{10}
\]

extended by zero outside that coordinate ball. No discontinuity is introduced:
the cutoff has compact support in the chart. Its normalization satisfies

\[
 \|I_g\psi\|=1+O(e^{-b/g^2})                                     \tag{11}
\]

for some \(b>0\), where a polynomial prefactor is absorbed by decreasing \(b\).
The same estimate holds uniformly for

\[
 \psi_s=e^{-isH_{\rm h}}\psi,\qquad 0\le s\le T,                   \tag{12}
\]

because this evolution changes only the phases of finitely many
Gaussian-times-polynomial eigenfunctions.

For each fixed finite lattice, \(a,c,T,\psi,\chi\), there are constants

\[
 \sup_{0\le s\le T}
 \left\|e^{-isH_g}{I_g\psi\over\|I_g\psi\|}
       -{I_g\psi_s\over\|I_g\psi_s\|}\right\|
 \le C_{\psi,\chi,L,a,c,T}g^2+C'e^{-b/g^2}.                         \tag{13}
\]

### Proof, including the residual and cutoff terms

Taylor's integral remainder gives, for every real \(z\),

\[
 |2(1-\cos z)-z^2|\le {|z|^4\over12}.                             \tag{14}
\]

With \(A=gx\), the potential part of

\[
 (H_g I_g-I_gH_{\rm h})\psi_s                                    \tag{15}
\]

therefore has norm at most

\[
 {c g^2\over24a}\sum_p
       \|(Cx)_p^4\psi_s\|.                                       \tag{16}
\]

The sum is finite at fixed volume and uniformly bounded on the time interval.
For example, on the harmonic vacuum,

\[
 \|(Cx)_p^4\psi_0\|=\sqrt{105}\,v_p^2,\qquad
 v_p=\tfrac12(CD^{-1/2}P_{\mathcal S}C^T)_{pp}.                    \tag{17}
\]

The kinetic commutator with the cutoff consists, after rescaling, of

\[
 -{c\over2a}g^{-r/2}
 \left[2g\nabla\chi(A)\cdot\nabla_x\psi_s(A/g)
             +g^2(\Delta\chi)(A)\psi_s(A/g)\right].               \tag{18}
\]

Its support is separated from \(A=0\), hence \(|x|\ge b_0/g\) there.
Gaussian tails bound its norm by \(C'e^{-b/g^2}\), uniformly in \(s\).
Equations (16)-(18) give a uniform residual of size \(Cg^2+C'e^{-b/g^2}\).

The torus Schrödinger operator (8) is self-adjoint on its usual Sobolev
domain; the smooth compactly supported packets lie in that domain. Differentiate

\[
 e^{-i(t-s)H_g}I_g e^{-isH_{\rm h}}\psi                            \tag{19}
\]

and integrate from zero to \(t\). Unitarity and the residual bound yield

\[
 \|e^{-itH_g}I_g\psi-I_g\psi_t\|
       \le t(Cg^2+C'e^{-b/g^2}).                                  \tag{20}
\]

Normalizing the initial and reference packets changes this only by the
exponentially small quantities in (11). This proves (13). The statement is
about these declared packets; no completeness claim about low-energy compact
eigenstates is used.

## 4. Transverse propagation and continuum frequencies

Writing \(q_\mu=e^{ik_\mu}-1\), the curl-square Fourier symbol is, up to
the harmless link Fourier convention,

\[
 \lambda(k)I-qq^\dagger,\qquad
 \lambda(k)=\sum_\mu|q_\mu|^2=4\sum_\mu\sin^2(k_\mu/2).           \tag{21}
\]

The vector \(q\) is the gauge direction. Its orthogonal complement has two
polarizations with eigenvalue \(\lambda(k)\). For either polarization,

\[
 \dot x={c\over a}p,\quad \dot p=-{c\over a}\lambda(k)x,
 \quad\ddot x=-\omega(k)^2x,                                     \tag{22}
\]

with (3). These are the free lattice electromagnetic wave equations after
the stated removal of the zero modes.

Fix a physical box length \(\ell\), an integer momentum vector

\[
 k_{\rm phys}={2\pi n\over\ell},\qquad a={\ell\over L}.            \tag{23}
\]

For every fixed \(n\ne0\),

\[
 \left|\omega_L(n)-c|k_{\rm phys}|\right|
 \le {c a^2\over24}
       \sqrt{\sum_\mu |k_{{\rm phys},\mu}|^6}.                    \tag{24}
\]

Indeed \(|\sin z-z|\le|z|^3/6\), and the Euclidean norm is Lipschitz.
The two transverse planes also tend to the plane normal to
\(k_{\rm phys}\), after removal of the link-centering Fourier phases.
Identify a fixed finite list of oscillator occupation states and subtract the
vacuum energy at each lattice size. Their finite excitation energies and
relative evolution phases then converge to those of the corresponding free
Maxwell modes in the periodic box. This comparison concerns a finite list of
modes; no identification of entire infinite tensor-product Hilbert spaces or
uniform convergence of all ultraviolet modes is asserted.

## 5. Composition with finite record and link spaces

Write \(\widehat I_g\psi=I_g\psi/\|I_g\psi\|\). At each fixed
\(g,L,a\), the smooth compact packet has finite electric
moments of every order. Let

\[
 P_S=\prod_e1_{[-S,S]}(E_e),\qquad
 \psi_g^{(S)}={P_S\widehat I_g\psi\over\|P_S\widehat I_g\psi\|}.   \tag{25}
\]

This cutoff commutes with Gauss and the three electric winding operators;
it preserves their zero sector. At fixed finite volume its normalization
tends to one. Since \(P_S\) commutes with all electric moments, for large
\(S\) its normalized fourth moments are bounded by twice those of the
uncut packet. Thus it satisfies the initial-moment hypothesis of the
large-spin packet with a constant depending on the fixed \(g,L\), but not
on \(S\).

That packet uses \(C_S=S(S+1)\), \(\epsilon=t/\Delta\), and

\[
 \epsilon^2={J\over2K C_S}={1\over2g^4 C_S},\qquad
 \Delta={c g^6 C_S^2\over a},\qquad
 t={c g^4 C_S^{3/2}\over\sqrt2 a},\qquad
 \beta=\beta_0\epsilon^6                                           \tag{26}
\]

in three dimensions. The relevant initial microscopic state is its local
number/Gauss-preserving dressing of the A-record/B-vacant pattern tensored
with (25). The finite-box version of its observable comparison, followed by
the norm convergence of (25), supplies (1) on these states. For every bounded
observable on that fixed box, the packet theorem then controls the second
limit. Its norm comparison also controls all bounded functions of finitely
many prepared mode observables.

Neither the fourth-moment constant nor the packet theorem's constants have
been bounded uniformly as \(g\to0\) or \(L\to\infty\). Equation (26)
shows already that making \(\epsilon\) small at weak \(g\) requires
\(S\gg g^{-2}\). The ordered construction does not supply an economical
joint resource scaling. The state (25) is an explicit mathematical
preparation target; it has not been compiled into the earlier local record
cooling protocol or the native qubit-site rules.

The rate in (26) is the stronger author schedule from the provisional
finite-circuit result. Its independent comparison is pending at this source
revision. If that schedule is not established, this composition must be
revised to a verified sufficient preparation/rate pair; one cannot erase the
dependency because the harmonic step is familiar.

## 6. Finite checks and their limits

`weak_field_wavepacket_check.py` is self-contained. It checks integer cubic
incidence identities and ranks modulo 65521 on sides 3, 4 and 6, compares the
complete numerical curl-square spectra against (21), and computes the vacuum
quartic residual coefficient (17). The side-six case has 648 links and exactly
430 transverse oscillator directions. Its full spectral discrepancy is
\(1.25\times10^{-14}\). The computed bound (16), at \(c/a=1\), is
\(175.046\,g^2\) before the cutoff correction. This deliberately exposes
the volume dependence of the global packet estimate. Sides three and four
are controls of the harmonic mathematics, not microscopic tori meeting the
record model's even-side-at-least-six assumption.

A separate complete one-plaquette compact-rotor control has

\[
 H_g^{\square}=2g^2m^2+{1\over g^2}
             -{1\over2g^2}(\mathsf S+\mathsf S^\dagger),           \tag{27}
\]

where \(\mathsf S|m\rangle=|m+1\rangle\). The loop's metric gives harmonic
frequency two at \(c/a=1\). The periodized harmonic ground and first excited
packets have Fourier coefficients proportional to

\[
 e^{-g^2m^2},\qquad -2igm\,e^{-g^2m^2}.                            \tag{28}
\]

The checked residuals divided by \(g^2\) tend to

\[
 {\sqrt{105}\over24}=0.426956\ldots,\qquad
 {\sqrt{945}\over24}=1.280869\ldots.                              \tag{29}
\]

For their equal superposition at time one, the vector errors are

| \(g\) | 0.4 | 0.2 | 0.1 | 0.05 |
|---|---:|---:|---:|---:|
| error | 0.100583 | 0.0234332 | 0.00576050 | 0.00143415 |
| error / \(g^2\) | 0.628644 | 0.585830 | 0.576050 | 0.573660 |

Increasing the electric cutoff from \(\lceil7/g\rceil\) to
\(\lceil10/g\rceil\) changes the reported first four energies by at most
\(5.1\times10^{-14}\) and the dynamic errors by at most
\(1.17\times10^{-13}\). These are numerical stability controls, not rigorous
infinite-matrix enclosures. The runner also checks the analytic dispersion
bound (24) for three fixed modes over five lattice sizes. All runs completed
without a failed scientific assertion; complete outputs and the receipt are
bound by the author seal.

## 7. Attribution and unresolved selection problem

The compact gauge Hamiltonian and its free harmonic behavior are established
machinery, not newly discovered physics. The primary historical source is
[Kogut and Susskind, Phys. Rev. D 11, 395 (1975)](https://doi.org/10.1103/PhysRevD.11.395);
the accessible abstract identifies the canonical coupled-rotor formulation.
Its paywalled body was not used as a proof source. The virtual-motion mechanism
was already compared with the fully read relevant sections of
[Zohar, Cirac and Reznik (2013)](https://arxiv.org/abs/1303.5040) in the
large-spin note. The packet argument above is given in full, rather than
importing an unchecked semiclassical eigenvalue or Coulomb-phase theorem.
Simon (1983), [low-lying semiclassical eigenvalues](https://www.numdam.org/item/AIHPA_1983__38_3_295_0/),
was consulted for context; neither its theorem nor its later corrigendum is
a dependency here.

The contribution of this note is to make the last finite-box free-wave step,
the packet preparation, and the order of limits explicit for the supplied
record construction. The main TOE question remains why minimal site rules
would select its larger memories, quantum amplitudes, gauge/background sector,
statistics, prepared states, energy scaling and decreasing formation schedule.
These have been chosen in the construction. Recovering a known free sector
under those choices is a consistency test, not an empirical prediction or a
derivation of all physics.
