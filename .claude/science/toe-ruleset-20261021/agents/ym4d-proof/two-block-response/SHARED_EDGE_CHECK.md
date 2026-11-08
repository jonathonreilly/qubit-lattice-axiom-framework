# Independent shared-edge SU(2) moment check

Status: exact local identities proved below, conditional on the normalized product kernel stated in the assigned source. This check does not establish an infrared or mass-gap conclusion.

Source inspected: [MASS_GAP_CONSTRUCTION_ASTRA.md](../MASS_GAP_CONSTRUCTION_ASTRA.md), lines 256–320, at verified commit `89faef229ff6e6bde42baad15ed8270c2f4087d8`. Whole-file SHA-256: `a5d31da82721607e0ba04fef84675706bd3f2c568644224cce7dc86b0bb968e2`. Inspected-line SHA-256: `2f5382a458c3221e6a721fa8584cf69dd639549e6cad8b061c740a8c22ea935e`. No other source argument was inspected; no repository file was edited.

The derivation uses the singlet/triplet decomposition of the fundamental representation and an explicit character integral. It does **not** obtain the second moment by differentiating the normalizer. Quaternion coordinates supply a separate sign and positivity check.

## 1. Scope and exact formulas

Fix the fine field $U$ and real $\lambda\geq0$. The shared coarse link has normalized law

\[
 k_\lambda(V\mid M)\,dV
 =\frac{\exp[\lambda w(V^\dagger M)]}{Z(\lambda r)}\,dV,
 \qquad M=rW,\quad 0<r\leq1,\quad W\in SU(2),
\]

where $w(Q)=\tfrac12\operatorname{Re}\operatorname{tr}Q$, Haar measure has total mass one, and $Z(z)=2I_1(z)/z$. Every matrix to which $w$ is applied below is a real quaternion, so its trace is real. Initially also fix the six other links, and hence $A,B\in SU(2)$, with loops

\[
 P=w(VA),\qquad Q=w(V^\dagger B).
\]

Products within $A$ and $B$ retain their actual oriented order. Set

\[
 z=\lambda r,\quad b(z)=\frac{I_2(z)}{I_1(z)},\quad
 q(z)=\frac{I_3(z)}{I_1(z)},\quad t(z)=\frac{1-q(z)}4,
 \quad c=w(WA),\quad d=w(W^\dagger B).
\]

At $z=0$, the removable values are $b=q=0$ and $t=1/4$. Then

\[
 \boxed{\mathbb E_V[P]=bc,\qquad \mathbb E_V[Q]=bd,}
 \tag{1}
\]

\[
 \boxed{\mathbb E_V[PQ]=t\,w(AB)+qcd,}
 \tag{2}
\]

\[
 \boxed{\operatorname{Cov}_V(P,Q)
       =t\,w(AB)+(q-b^2)cd.}
 \tag{3}
\]

The subscript $V$ means that the other six links are held fixed. In particular, the two occurrences of the shared link have not been replaced by independent copies or by independent means.

The underlying second matrix moment is

\[
 \boxed{\mathbb E_V[V_{ij}(V^\dagger)_{kl}]
   =q\,W_{ij}(W^\dagger)_{kl}
    +\frac{1-q}{2}\delta_{il}\delta_{jk}.}
 \tag{4}
\]

This is a raw second moment; subtracting the product of matrix means replaces $q$ by $q-b^2$ in its first term.

## 2. Character and tensor derivation

Write $V=WX$. Haar invariance gives the central law

\[
 d\nu_z(X)=Z(z)^{-1}e^{z w(X)}dX.
\]

For the spin-$j$ character, put $n=2j+1\in\{1,2,\ldots\}$. The class coordinate $X\sim\operatorname{diag}(e^{i\theta},e^{-i\theta})$ has Haar class density $2\sin^2\theta/\pi$, and

\[
 \chi_j(\theta)=\frac{\sin(n\theta)}{\sin\theta}.
\]

Consequently,

\[
 \begin{aligned}
 \int e^{z w(X)}\chi_j(X)\,dX
 &=\frac2\pi\int_0^\pi e^{z\cos\theta}
                      \sin\theta\sin(n\theta)\,d\theta\\
 &=I_{n-1}(z)-I_{n+1}(z)
 =\frac{2n}{z}I_n(z).
 \end{aligned}
 \tag{5}
\]

The only special-function inputs here are the cosine integral for integer-order $I_n$ and its adjacent-order recurrence; both are recorded in [NIST DLMF 10.32.3](https://dlmf.nist.gov/10.32.E3) and [10.29.1](https://dlmf.nist.gov/10.29.E1). All values at zero follow by continuity of the integrals. Dividing (5) by its $j=0$ case yields

\[
 \mathbb E_{\nu_z}\chi_j=(2j+1)\frac{I_{2j+1}(z)}{I_1(z)}.
 \tag{6}
\]

The fundamental representation has scalar central average $bI$, since its normalized trace average is $I_2/I_1$. For the second moment use

\[
 \mathbb C^2\otimes\overline{\mathbb C^2}
   =\mathbf1\oplus\mathbf3.
\]

Under vectorization this is the decomposition of $2\times2$ matrices into scalar matrices and traceless matrices. $X\otimes\bar X$ acts as conjugation $T\mapsto XTX^\dagger$: it is the identity on the scalar part, while the traceless part is the irreducible spin-one representation. Centrality and Schur's lemma therefore give

\[
 \mathbb E_{\nu_z}[X\otimes\bar X]=P_0+qP_1,
 \qquad q=\frac{\mathbb E\chi_1}{3}=\frac{I_3}{I_1}.
 \tag{7}
\]

Here $P_0(T)=\tfrac12\operatorname{tr}(T)I$ and $P_1=I-P_0$. In indices this says

\[
 \mathbb E[X_{ij}(X^\dagger)_{kl}]
 =q\delta_{ij}\delta_{kl}
   +\frac{1-q}{2}\delta_{il}\delta_{jk}.
 \tag{8}
\]

Multiplication by $W$ and $W^\dagger$ gives (4). Contract (4) with $A_{ji}B_{lk}/4$. The first term gives $qcd$; the singlet contraction gives

\[
 \frac{1-q}{8}\operatorname{tr}(AB)
 =\frac{1-q}{4}w(AB).
\]

This proves (2), including the factor $1/4$ for normalized traces. Subtracting (1)'s product proves (3). No commutation of $A,B,W$ was used. In particular, $AB$, $WA$, and $W^\dagger B$ are the products forced by the specified opposite orientations.

## 3. Regular form at $M=0$, and small coupling with remainders fixed

For $r>0$, equations (2)–(3) can be written without normalized polar factors:

\[
 \mathbb E_V[PQ]
 =t(\lambda r)w(AB)
  +\frac{q(\lambda r)}{r^2}w(MA)w(M^\dagger B),
 \tag{9}
\]

\[
 \operatorname{Cov}_V(P,Q)
 =t(\lambda r)w(AB)
  +\frac{q(\lambda r)-b(\lambda r)^2}{r^2}
                         w(MA)w(M^\dagger B).
 \tag{10}
\]

The coefficient limits at $r=0$ are respectively $\lambda^2/24$ and $-\lambda^2/48$. Both multiplied terms are then zero because $M=0$. Thus the formulas have a regular extension with no choice of $W$.

The series are

\[
 \begin{aligned}
 b(z)&=z/4-z^3/96+z^5/1536+O(z^7),\\
 q(z)&=z^2/24-z^4/384+O(z^6),\\
 t(z)&=1/4-z^2/96+z^4/1536+O(z^6),\\
 q(z)-b(z)^2&=-z^2/48+z^4/384+O(z^6).
 \end{aligned}
 \tag{11}
\]

Hence, with $A,B$ fixed,

\[
 \mathbb E_V[PQ]
 =\frac14w(AB)
  +\lambda^2\left[-\frac{r^2}{96}w(AB)
                  +\frac1{24}w(MA)w(M^\dagger B)\right]
  +O(\lambda^4),
 \tag{12}
\]

\[
 \operatorname{Cov}_V(P,Q)
 =\frac14w(AB)
  -\lambda^2\left[\frac{r^2}{96}w(AB)
                  +\frac1{48}w(MA)w(M^\dagger B)\right]
  +O(\lambda^4).
 \tag{13}
\]

These remainders are uniform for $A,B\in SU(2)$ and $r\in[0,1]$ in a fixed sufficiently small coupling interval. Analyticity follows from the explicit Bessel series and the nonvanishing normalized denominator near zero; all matrix products have bounded norm.

If $\lambda=0$, or if $M=0$ at any $\lambda$, the shared link is Haar:

\[
 \mathbb E_V[P]=\mathbb E_V[Q]=0,\qquad
 \mathbb E_V[PQ]=\operatorname{Cov}_V(P,Q)=\tfrac14w(AB).
 \tag{14}
\]

For the explicit fixed-remainder test M=0 and A=B=1, the covariance equals 1/4 while the product of first moments equals zero. The source's transport statement concerns disjoint coarse edges.

## 4. Conditioning only on the fine field: the actual two-plaquette formula

Now integrate the six other coarse links. Assume the two simple plaquettes share exactly one unoriented edge, used once in each, and their other three-edge paths are disjoint. Conditional on $U$, these six links and $V$ are independent under the stated normalized kernel. Consequently $A,B,V$ are independent as three random objects, although $P$ and $Q$ share $V$.

For an oriented external edge $e$, let

\[
 m_e=f_\lambda(r_e)M_e^{(\epsilon_e)},\qquad
 f_\lambda(r)=b(\lambda r)/r,\qquad f_\lambda(0)=\lambda/4,
\]

where $M_e^{(+)}=M_e$ and $M_e^{(-)}=M_e^\dagger$. Define the ordered path means

\[
 \bar A=\mathbb E[A\mid U]=m_{a_1}m_{a_2}m_{a_3},\qquad
 \bar B=\mathbb E[B\mid U]=m_{b_1}m_{b_2}m_{b_3}.
\]

They are real quaternions, generally not unitary. The trace contractions remain linear separately in $A,B$. Independence of these two paths gives the exact identities

\[
 \boxed{\mathbb E[PQ\mid U]
 =t\,w(\bar A\bar B)
  +q\,w(W\bar A)w(W^\dagger\bar B),}
 \tag{15}
\]

\[
 \boxed{\operatorname{Cov}(P,Q\mid U)
 =t\,w(\bar A\bar B)
  +(q-b^2)w(W\bar A)w(W^\dagger\bar B).}
 \tag{16}
\]

The individual conditional means are $b\,w(W\bar A)$ and $b\,w(W^\dagger\bar B)$. Equations (9)–(10) with $A,B$ replaced by $\bar A,\bar B$ give their regular $M=0$ forms.

To state the coupling order without hiding the other six kernel factors, put

\[
 A_M=M_{a_1}^{(\epsilon_{a_1})}M_{a_2}^{(\epsilon_{a_2})}
                  M_{a_3}^{(\epsilon_{a_3})},\qquad
 B_M=M_{b_1}^{(\epsilon_{b_1})}M_{b_2}^{(\epsilon_{b_2})}
                  M_{b_3}^{(\epsilon_{b_3})}.
\]

For a common small $\lambda$ on all seven links,

\[
 \bar A=(\lambda/4)^3A_M+O(\lambda^5),\qquad
 \bar B=(\lambda/4)^3B_M+O(\lambda^5).
\]

It follows that

\[
 \boxed{\mathbb E[PQ\mid U]
       =\operatorname{Cov}(P,Q\mid U)+O(\lambda^8)
       =\frac{\lambda^6}{4^7}w(A_MB_M)+O(\lambda^8).}
 \tag{17}
\]

The coefficient may vanish for a particular $U$; “order six” means the first allowed generally nonzero coefficient. The product of the two plaquette conditional means is only $O(\lambda^8)$. Equations (17)–(18) are pointwise fine-field-conditional expansions, with the fine field and its path means $M_e(U)$ fixed as $\lambda$ varies. No expansion of a coupling-dependent exterior posterior, or remainder after integrating against such a posterior, is asserted.

For an additional coefficient check, set $S=\sum_{e\text{ among all seven links}}r_e^2$ and $H=w(MA_M)w(M^\dagger B_M)$, with $M$ the shared-edge mean. Direct expansion gives

\[
 \begin{aligned}
 \mathbb E[PQ\mid U]
 &=\frac{\lambda^6}{4^7}w(A_MB_M)
  +\frac{\lambda^8}{4^6}
       \left[-\frac S{96}w(A_MB_M)+\frac H{24}\right]
  +O(\lambda^{10}),\\
 \operatorname{Cov}(P,Q\mid U)
 &=\frac{\lambda^6}{4^7}w(A_MB_M)
  -\frac{\lambda^8}{4^6}
       \left[\frac S{96}w(A_MB_M)+\frac H{48}\right]
  +O(\lambda^{10}).
 \end{aligned}
 \tag{18}
\]

Their difference is $\lambda^8H/4^8+O(\lambda^{10})$, as independently obtained by multiplying the individual plaquette means.

Two different zero-limit statements must be kept separate. At $\lambda=0$ on all coarse links, $\bar A=\bar B=0$, so the fine-$U$-conditional moment and covariance in (15)–(16) are zero. At $M=0$ only on the shared edge and $\lambda>0$ elsewhere, both instead equal $\tfrac14w(\bar A\bar B)$, which need not vanish. If any external edge has zero mean, the corresponding path mean vanishes and both quantities are exactly zero.

## 5. Independent orientation and positivity checks

Write $X=x_0I+i\boldsymbol x\cdot\boldsymbol\sigma$. Centrality gives zero vector mean, zero scalar-vector mixed moments, and $\mathbb E[x_ix_j]=t\delta_{ij}$. Since the spin-one character is $4x_0^2-1$, equation (6) gives

\[
 a:=\mathbb E[x_0^2]=(1+3q)/4,\qquad
 t=(1-a)/3=(1-q)/4.
\]

For $C=AW=cI+i\boldsymbol c\cdot\boldsymbol\sigma$ and $D=W^\dagger B=dI+i\boldsymbol d\cdot\boldsymbol\sigma$, direct quaternion multiplication yields

\[
 P=x_0c-\boldsymbol x\cdot\boldsymbol c,\qquad
 Q=x_0d+\boldsymbol x\cdot\boldsymbol d,
\]

so $\mathbb E[PQ]=acd-t\boldsymbol c\cdot\boldsymbol d=t\,w(CD)+(a-t)cd$. Because $CD=AB$ and $a-t=q$, this independently checks (2)'s contraction and its dagger sign.

An explicit noncommuting check is

\[
 A=i\sigma_1,\quad B=i\sigma_2,\quad
 W=(I+i\sigma_1+i\sigma_2+i\sigma_3)/2.
\]

Here $AB=-BA$, $w(AB)=0$, $c=-1/2$, and $d=1/2$. Thus the raw moment is $-q/4$ and the covariance is $(b^2-q)/4=z^2/192+O(z^4)$. No commuting-orientation reduction is needed.

For the equal-loop check take fixed $B=A^\dagger$. Then $Q=P$, $w(AB)=1$, $d=c$, and

\[
 \mathbb E[P^2]=t+qc^2,\qquad
 \operatorname{Var}(P)=t+(q-b^2)c^2
   =t(1-c^2)+(a-b^2)c^2\geq0.
 \tag{19}
\]

Indeed $|c|\leq1$, $t=\mathbb E[x_1^2]\geq0$, and $a-b^2=\operatorname{Var}(x_0)\geq0$. Both coefficients are strictly positive for finite real $z$, because the density is strictly positive on all of $SU(2)$. At $z=0$, the variance is exactly $1/4$. This is a fixed-remainder algebraic check; imposing $B=A^\dagger$ on random paths would remove their independence and is not the distinct-plaquette hypothesis used in (15)–(18).

## Verification record and limit of conclusion

The source commit and hashes above were checked during this calculation. A deterministic SymPy expansion of $I_n(z)=\sum_{k\geq0}(z/2)^{2k+n}/(k!(k+n)!)$, using terms $k=0,\ldots,6$, returned

```text
b = z/4 - z**3/96 + z**5/1536 - z**7/23040
q = z**2/24 - z**4/384 + z**6/5760
t = 1/4 - z**2/96 + z**4/1536 - z**6/23040
q - b**2 = -z**2/48 + z**4/384 - z**6/3840 + O(z**8)
```

An exact symbolic Pauli-matrix contraction checked all 16 index choices in (8) using the quaternion second moments $a=(1+3q)/4$ and $t=(1-q)/4$. The displayed noncommuting example was also checked with exact matrices, including unitarity of $W$, $AB+BA=0$, and $(w(AB),c,d)=(0,-1/2,1/2)$. These are arithmetic checks of the written derivation, not additional independent scientific evidence. The source digest was unchanged at final verification.

The proof is the character integral, singlet/triplet decomposition, and exact contractions above. No sampling or simulation was used. The substantive correction to any attempted overlap factorization is the singlet term $t\,w(\bar A\bar B)$, together with the triplet covariance coefficient $q-b^2$. These identities address one shared edge only. They provide no decay estimate for separated observables and no retained-status or mass-gap claim.
