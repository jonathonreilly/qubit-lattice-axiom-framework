# Your scale comparison over one window, your index $`k_0`$, and the cells of your action sequence

Provenance: Claude Opus 5.5 wrote Lemmas G, W and C with their corollaries, and Claude Fable 5.2 checked them line by line. Claude Fable 5.2 wrote Example F and Lemma K, and Claude Opus 5.5 checked them line by line. Claude Opus 5.5 added the last sentence of Lemma K and its proof during that check; Codex (gpt-6-astra) then checked that addition line by line and found no failing step. Not an audit.

The frame, the geometric rules and the notation are yours. The ceiling, the counterexample and the deductions added below are ours. The source is `YM4/YM4_1400.tex` at commit `c7fef8b21b58` of ethanwsussman/Yang--Mills-LLM-experiment ([the file](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/c7fef8b21b58/YM4/YM4_1400.tex)). "Line n" means line n of that file. Two passages are in `YM4/EM/YM4_EM.tex` and `YM4/RT/YM4_RT.tex` at the same commit; for those the file is named.

The note has three parts.

- Part 1 treats your comparison $`\check R_{h_t}\le L\check R_t`$ at lines 73382-73383. Your frame definition alone does not give it (Example F). It holds under one added ceiling (G) on $`\gamma`$ (Lemma W, Corollary S).
- Part 2 proves that your index $`k_0`$ of lines 63775-63778 exists, with $`h<k_0\le k-2`$, under the same ceiling (Lemma K).
- Part 3 proves that every region of your action sequence is a union of cells of its own level (Lemma C). So the first case of your rule at lines 1475-1477 always applies to the action sequence (Corollary C).

No step uses a computation. Every number is displayed and can be checked by hand.

## Part 1. The comparison of scales over one waiting window

### 1.1 Your sentence, and what your text gives for it

Lines 73376-73384 read: "Its carriers are in the enlargements of older islands or of strips of levels at most $`h_t=t-\mathsf N_t`$, where $`\mathsf N_t`$ is the number of preparatory stages. The stored bonds are in the inner core. The enlargement costs at most one cell of level $`h_t`$, and the next two shells have widths at least $`M\check R_t\xi_{h_t}`$ and $`LM\check R_t\xi_{h_t}`$. The scale comparison $`\check R_{h_t}\le L\check R_t`$ therefore puts every carrier inside $`Z''_{h_t+2}`$."

The sentence names the comparison as known. The lines before it give the widths of the shells, which are the reason for "puts every carrier inside". No reason for the comparison itself is given at these lines.

The following comparisons in your text relate neighbouring levels:

- Line 1110, in the frame definition: $`\check R_j\le L\check R_{j+1}`$.
- Lines 73081-73082: "The size sequence has $`R_{j+1}/R_j\in\{1,L^{-1}\}`$, and two size drops are not consecutive."
- Line 62001: "Moreover $`\check{R}_k\le L\check{R}_{k+1}`$, and two consecutive drops never occur, because $`x`$ changes by $`O(1)`$ per step and $`\gamma`$ is small."
- `YM4/EM/YM4_EM.tex`, lines 448-452, prove the ratio of one step: "If the minimum drops, $`y_j-y_{j+1}\le\theta_j-\theta_{j+1}\le\bar B`$. Above a fixed floor this makes the ratio of $`(\log y_j)^r`$ to $`(\log y_{j+1})^r`$ less than $`L`$. Rounding up to the next $`L`$-power gives $`\check R_j/\check R_{j+1}\in\{1,L\}`$."
- `YM4/RT/YM4_RT.tex`, lines 1027-1033 (`rt:eq-adjacent-cell`), prove the ratio of one step: "If the running minimum drops, its drop is at most $`B_{\rm s}`$. The cell condition in `rt:lem-constant-order` makes the ratio of $`(\log y)^r`$ at the two successive minima less than $`L`$. Taking the least $`L`$-powers gives $`R_j/R_{j+1}\in\{1,L\}`$."

The levels $`h_t`$ and $`t`$ are $`\mathsf N_t=\check R_t\ge L`$ steps apart. Applied at each step between them, these one-step statements bound $`\check R_{h_t}/\check R_t`$ only by a power of $`L`$ that grows with $`\check R_t`$.

### 1.2 Your frame and your waiting depth

Lines 1102-1113: "A frame is a real sequence $`\theta_0,\ldots,\theta_k\ge\gamma^{-2}`$, with $`0<\gamma<e^{-1/2}`$, such that, for $`i\le j`$,"

```math
\underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\bar B(j-i),\qquad \check R_j=R(\min_{i\le j}\theta_i),\qquad \check R_j\le L\check R_{j+1},
```

"where $`R(y)`$ is the smallest power of $`L`$ not below $`(\log y)^r`$."

Line 1121: "The waiting depth is $`\mathsf N_j=\check R_j`$." Line 73378: $`h_t=t-\mathsf N_t`$.

Constants, as your text fixes them: $`r\ge2`$ (line 62001); $`L\ge13`$ odd (lines 650-651); $`\underline\lambda=\tfrac14c_0`$ and $`c_5=2c_2`$ (line 72936). The lemmas below assume $`\underline\lambda\ge0`$, $`c_5\ge0`$ and $`\bar B\ge0`$. If a frame has $`\bar B<0`$, its upper bound also holds with $`0`$ in place of $`\bar B`$.

Write $`m_j=\min_{i\le j}\theta_i`$, so that $`\check R_j=R(m_j)`$.

### 1.3 Example F: a frame that breaks the comparison

Take $`r=2`$, $`L=13`$, $`0\le\underline\lambda\le12`$, $`c_5\ge0`$, $`\bar B\ge e^{14}`$ and $`e^{-1}\le\gamma<e^{-1/2}`$. The frame has length $`k=14`$:

```math
\theta_j=e^{14}+\underline\lambda\,(10-j)\quad(0\le j\le10),\qquad \theta_{11}=e^5,\quad \theta_{12}=e^4,\quad \theta_{13}=e^3,\quad \theta_{14}=e^2 .
```

Each condition of lines 1102-1110 holds. The checks use only $`2.7<e<3`$.

- Floor. The least member is $`\theta_{14}=e^2`$. Since $`\gamma\ge e^{-1}`$, $`\gamma^{-2}\le e^2`$.
- One-step drops. Put $`d_j=\theta_j-\theta_{j+1}`$. Then $`d_j=\underline\lambda`$ for $`0\le j\le9`$, $`d_{10}=e^{14}-e^5`$, $`d_{11}=e^4(e-1)`$, $`d_{12}=e^3(e-1)`$ and $`d_{13}=e^2(e-1)`$.
- Each drop is at least $`\underline\lambda`$. Indeed $`e^2(e-1)>2.7^2\cdot1.7=7.29\cdot1.7=12.393>12\ge\underline\lambda`$, the drops $`d_{11},d_{12}`$ are larger than $`d_{13}`$, and $`d_{10}=e^5(e^9-1)\ge e^5>12`$.
- Each drop is at most $`e^{14}-e^5\le\bar B`$. Indeed $`\underline\lambda\le12<e^{14}-e^5`$, and $`d_{11},d_{12},d_{13}<e^5<e^{14}-e^5`$ because $`e^9>2`$.
- Two-sided bound. For $`i<j`$, $`\theta_i-\theta_j`$ is the sum of the drops $`d_m`$, $`i\le m<j`$. So it lies between $`\underline\lambda(j-i)`$ and $`\bar B(j-i)`$. Since $`c_5\ge0`$, the lower bound $`\underline\lambda(j-i)-c_5`$ holds. At $`i=j`$ both bounds hold trivially.
- Running minimum. Every drop is non-negative, so $`m_j=\theta_j`$.
- Values of $`\check R_j`$. With $`r=2`$ and $`L=13`$: $`R(y)=13`$ when $`1<(\log y)^2\le13`$; $`R(y)=169`$ when $`13<(\log y)^2\le169`$; $`R(y)=2197`$ when $`169<(\log y)^2\le2197`$.
- For $`j\le10`$: $`e^{14}\le\theta_j\le e^{14}+120\le e^{15}`$, because $`e^{15}-e^{14}=e^{14}(e-1)>120`$. So $`196\le(\log\theta_j)^2\le225`$ and $`\check R_j=2197`$.
- $`(\log\theta_{11})^2=25`$ and $`(\log\theta_{12})^2=16`$, so $`\check R_{11}=\check R_{12}=169`$.
- $`(\log\theta_{13})^2=9`$ and $`(\log\theta_{14})^2=4`$, so $`\check R_{13}=\check R_{14}=13`$.
- Ratio condition. The ratio $`\check R_j/\check R_{j+1}`$ is $`1`$, except $`2197/169=13`$ at $`j=10`$ and $`169/13=13`$ at $`j=12`$. So $`\check R_j\le L\check R_{j+1}`$ for every $`j`$.
- The two drops of $`\check R`$ are at $`10\to11`$ and $`12\to13`$. They are not consecutive. So lines 73081-73082 and the claim of line 62001 also hold on this frame.

The comparison fails at $`t=14`$. Here $`\mathsf N_{14}=\check R_{14}=13`$ and $`h_{14}=14-13=1`$. Then

```math
\check R_{h_{14}}=\check R_1=2197=13^2\,\check R_{14}>L\,\check R_{14}=169 .
```

**Range.** For $`r=2`$, $`L=13`$, $`0\le\underline\lambda\le12`$ and $`c_5\ge0`$, this sequence is a frame exactly when $`e^{-1}\le\gamma<e^{-1/2}`$ and $`\bar B\ge e^{14}-e^5`$. The first condition comes from the floor at $`\theta_{14}=e^2`$. The second comes from the drop $`d_{10}`$, the largest one. The round form $`\bar B\ge e^{14}`$ used above lies inside this range.

**What Example F shows.** With $`r=2`$ and $`L=13`$, the frame definition of lines 1102-1113 does not give the comparison of lines 73382-73383. So the comparison needs a further condition. Every ceiling $`\gamma<e^{-1}`$ excludes Example F. Example F does not show that a ceiling which does not depend on $`\bar B`$ fails. The ceiling (G) below depends on $`\bar B`$, and your order of constants allows that.

### 1.4 The ceiling (G), and its place in your order

**(G).** For all $`y\ge\gamma^{-2}`$:

```math
\big(\log(y+c_5+\bar B\,L\,(\log y)^r)\big)^r\le L\,(\log y)^r .
```

(G) depends on $`r,L,c_5,\bar B`$ only. Your order of constants is at lines 72930-72931. Its end reads

```math
\cdots\prec(\underline\lambda,c_5,\bar B)\prec\gamma\prec(\varrho,c_a)\prec(g,\ell,\beta,K),
```

and $`r`$ and $`L`$ come at its start. So all constants of (G) come before $`\gamma`$. Line 72946 says: "a condition arising in the construction fits the order if, at the last of the constants on which it depends, it is of the kind named." The kind named at $`\gamma`$ is a ceiling. So (G) is one more ceiling on $`\gamma`$ that fits your order, and it restricts no earlier constant.

Your text already uses a small $`\gamma`$ for the one-step comparison. Line 62001: "two consecutive drops never occur, because $`x`$ changes by $`O(1)`$ per step and $`\gamma`$ is small." (G) is a ceiling of the same kind for one window of $`\check R_t`$ steps. In the passages found by our search, we found no explicit condition (G) or proof of this one-window comparison.

### 1.5 Lemma G

**Lemma G.** (G) holds when $`\gamma\le\gamma_0:=y_0^{-1/2}`$, where

```math
y_0=\max\Big\{\,2c_5,\ \ 4\big(\bar B\,L\,(2r)^r\big)^2,\ \ 2^{1/(L^{1/r}-1)},\ \ e\,\Big\}.
```

*Proof.* Let $`y\ge y_0`$. Then $`y\ge e>1`$. Put $`u=y^{1/(2r)}`$, so that $`u>1`$ and $`0<\log u\le u`$.

Then $`\log y=2r\log u\le2ru`$. Both sides are positive, so $`(\log y)^r\le(2r)^ru^r=(2r)^ry^{1/2}`$.

So $`\bar B\,L\,(\log y)^r\le\bar B\,L\,(2r)^ry^{1/2}`$. This is at most $`y/2`$, because $`y\ge4(\bar B L(2r)^r)^2`$ gives $`y^{1/2}\ge2\bar B L(2r)^r`$.

Also $`c_5\le y/2`$, because $`y\ge2c_5`$.

So $`y\le y+c_5+\bar B\,L\,(\log y)^r\le2y`$. The lower bound uses $`c_5\ge0`$ and $`\bar B\ge0`$. In particular the argument of the outer logarithm is larger than $`1`$.

Next, $`\log(2y)=\log y+\log2\le L^{1/r}\log y`$. This is $`(L^{1/r}-1)\log y\ge\log2`$, which holds because $`y\ge2^{1/(L^{1/r}-1)}`$ and $`L^{1/r}>1`$.

So $`0<\log(y+c_5+\bar B L(\log y)^r)\le L^{1/r}\log y`$. Raise both sides to the power $`r`$.

Last, if $`\gamma\le\gamma_0`$, every $`y\ge\gamma^{-2}`$ satisfies $`y\ge\gamma_0^{-2}=y_0`$. $`\square`$

### 1.6 Lemma W

Lemma W uses the index $`k_0`$ of lines 63775-63777, with $`a_i=M\check R_iL^i`$ (line 63749) and $`u_k=ML^k`$ (line 63774): "let $`k_0+1`$ be the last index with $`a_{k_0+1}=u_k`$, with $`h<k_0\le k-2`$." Here $`h=k_\flat=k-\mathsf N_k`$ (line 63684). Part 2 proves that this index exists.

**Lemma W.** Assume the frame and (G).

- (S) For every $`t`$ and every $`i`$ with $`\max(0,t-\check R_t)\le i\le t`$: $`\check R_i\le L\check R_t`$.
- (W) For an operation of level $`k`$ with $`h=k-\check R_k\ge0`$ and with $`k_0`$ as above: $`2(k-k_0)\le k-h`$, that is, $`k-k_0\le k_0-h`$.

*Proof.* (1) $`m_j`$ does not increase in $`j`$. Every $`m_j\ge\gamma^{-2}>1`$, and $`(\log y)^r`$ increases on $`y>1`$, so $`R`$ does not decrease there. Hence $`\check R_j=R(m_j)`$ does not increase in $`j`$.

(2) For $`i\le j`$, the lower frame bound and $`\underline\lambda\ge0`$ give $`\theta_i\ge\theta_j+\underline\lambda(j-i)-c_5\ge\theta_j-c_5`$. So $`\theta_j-c_5\le m_j\le\theta_j`$.

(3) Let $`t-\check R_t\le i\le t`$. By the upper frame bound, $`t-i\le\check R_t`$, $`\bar B\ge0`$ and (2):

```math
m_i\le\theta_i\le\theta_t+\bar B(t-i)\le\theta_t+\bar B\,\check R_t\le m_t+c_5+\bar B\,\check R_t .
```

Since $`m_t\ge\gamma^{-2}>e`$, $`(\log m_t)^r>1`$. Write $`\check R_t=L^p`$, the least power of $`L`$ not below $`(\log m_t)^r`$. Then $`p\ge1`$ and $`L^{p-1}<(\log m_t)^r`$, so $`\check R_t<L(\log m_t)^r`$.

(4) By (3), $`m_i\le m_t+c_5+\bar B\,L\,(\log m_t)^r`$. The logarithm increases, both logarithms are positive, and (G) holds at $`y=m_t\ge\gamma^{-2}`$. So

```math
(\log m_i)^r\le\big(\log(m_t+c_5+\bar B\,L\,(\log m_t)^r)\big)^r\le L(\log m_t)^r\le L\,\check R_t .
```

$`L\check R_t`$ is a power of $`L`$ not below $`(\log m_i)^r`$. So $`\check R_i=R(m_i)\le L\check R_t`$. This is (S). It is the only use of (G).

(5) Let $`\check R_k=L^p`$, with $`p\ge1`$ by (3). From $`a_{k_0+1}=u_k`$, that is $`M\check R_{k_0+1}L^{k_0+1}=ML^k`$, we get $`\check R_{k_0+1}=L^{k-k_0-1}`$. Since $`h+1\le k_0+1`$, (1) and (S) at $`i=h+1`$ give

```math
L^{k-k_0-1}=\check R_{k_0+1}\le\check R_{h+1}\le L\check R_k=L^{p+1},
```

so $`k-k_0\le p+2`$. Also $`k-h=\check R_k=L^p`$. So (W) follows from $`2(p+2)\le L^p`$. This holds for $`L\ge6`$ and every $`p\ge1`$. At $`p=1`$ it reads $`6\le L`$. If it holds at $`p`$, then $`2(p+3)=2(p+2)+2\le L^p+L^p\le L^{p+1}`$. Then $`2(k-k_0)\le2(p+2)\le L^p=k-h`$. $`\square`$

For a mark of level $`t<k`$ the same proof applies with $`t`$ in place of $`k`$.

### 1.7 Corollary S

**Corollary S (your scale comparison).** Assume the frame and (G). For every $`t`$ with $`h_t=t-\mathsf N_t\ge0`$:

```math
\check R_{h_t}\le L\,\check R_t .
```

*Proof.* $`\mathsf N_t=\check R_t`$ (line 1121), so $`i=h_t`$ satisfies $`\max(0,t-\check R_t)\le i\le t`$. Apply (S). $`\square`$

This is the inequality of your lines 73382-73383. (S) gives more: $`\check R_i\le L\check R_t`$ for every $`i`$ in $`[h_t,t]`$.

## Part 2. The index $`k_0`$

### 2.1 Your sentence

Lines 63774-63778: "Let $`u_i=ML^i`$ be the side of an $`M`$-cube at level $`i`$ in bare units. In the scale choice used for the preparation, let $`k_0+1`$ be the last index with $`a_{k_0+1}=u_k`$, with $`h<k_0\le k-2`$. Thus $`a_i\le u_k`$ up to $`k_0+1`$, and $`a_i\ge Lu_k`$ thereafter."

Here $`a_i=M\check R_iL^i`$ (lines 63748-63749: "set $`a_i=M\check R_iL^i`$, the side of a level-$`i`$ cell") and $`h=k_\flat=k-\mathsf N_k`$ (line 63684). Your text states that this index exists with $`h<k_0\le k-2`$. It gives no proof at these lines.

### 2.2 Lemma K

**Lemma K.** Assume the frame, (G), $`L\ge4`$ and $`h=k-\check R_k\ge0`$. Your $`L\ge13`$ (line 650) gives $`L\ge4`$. Then:

- the set of $`i`$ with $`a_i=u_k`$ is non-empty, and its last element $`i^*`$ satisfies $`h+2\le i^*\le k-1`$; so $`k_0=i^*-1`$ satisfies $`h<k_0\le k-2`$;
- $`a_i\le u_k`$ for every $`i\le k_0+1`$, and $`a_i\ge Lu_k`$ for every $`i`$ with $`k_0+2\le i\le k`$.

*Proof.* Step 1. Each $`\check R_i`$ is a power of $`L`$. Put $`e_i=i+\log_L\check R_i`$, an integer. Then $`a_i=ML^{e_i}`$, so $`a_i=u_k`$ exactly when $`e_i=k`$, $`a_i\le u_k`$ exactly when $`e_i\le k`$, and $`a_i\ge Lu_k`$ exactly when $`e_i\ge k+1`$.

Step 2. $`\check R_k\ge L`$. The frame gives $`m_k\ge\gamma^{-2}`$ with $`0<\gamma<e^{-1/2}`$ (lines 1102-1103), so $`m_k>e`$ and $`(\log m_k)^r>1`$. $`\check R_k=R(m_k)`$ is the smallest power of $`L`$ not below this number (lines 1109 and 1113). So $`\check R_k=L^p`$ with $`p\ge1`$. This step uses neither (G) nor the bound on $`L`$.

Step 3. $`e_{i+1}-e_i`$ is $`0`$ or $`1`$ for every $`i`$. By (1) of Lemma W, $`\check R_{i+1}\le\check R_i`$. By the frame (line 1110), $`\check R_{i+1}\ge\check R_i/L`$. Both are powers of $`L`$, so $`\check R_{i+1}/\check R_i`$ is $`1`$ or $`L^{-1}`$. Hence $`e_{i+1}-e_i=1+\log_L(\check R_{i+1}/\check R_i)`$ is $`1`$ or $`0`$. In particular $`e`$ does not decrease.

Step 4. $`e_k=k+p\ge k+1`$.

Step 5. $`k-h=\check R_k=L^p\ge L\ge4`$, so $`h+2\le k`$.

Step 6. $`e_{h+2}\le k`$. The index $`i=h+2`$ satisfies $`\max(0,k-\check R_k)=h\le i\le k`$. So (S) of Lemma W gives $`\check R_{h+2}\le L\check R_k=L^{p+1}`$. Hence $`e_{h+2}\le h+2+p+1=h+p+3`$. Now $`p+3\le L^p`$ for every $`p\ge1`$: at $`p=1`$ it reads $`4\le L`$; and if $`p+3\le L^p`$, then $`p+4\le L^p+1\le L^{p+1}`$. So $`e_{h+2}\le h+L^p=k`$.

Step 7. Let $`j`$ be the largest index in $`[h+2,k]`$ with $`e_j\le k`$. It exists by Step 6. It is at most $`k-1`$ by Step 4. Then $`e_{j+1}\ge k+1`$, and by Step 3 $`e_{j+1}\le e_j+1\le k+1`$. So $`e_{j+1}=k+1`$ and $`e_j=k`$.

Step 8. Since $`e`$ does not decrease (Step 3), the indices $`i`$ with $`e_i=k`$ form an interval. It contains $`j`$ and not $`j+1`$. So its last element is $`i^*=j`$, and $`h+2\le i^*\le k-1`$. Put $`k_0=i^*-1`$. Then $`h+1\le k_0\le k-2`$, that is, $`h<k_0\le k-2`$.

Step 9. For $`i\le k_0+1`$: $`e_i\le e_{k_0+1}=k`$, because $`e`$ does not decrease. So $`a_i\le u_k`$.

Step 10. By Step 3, $`e_{k_0+2}`$ is $`k`$ or $`k+1`$. It is not $`k`$, since $`k_0+1`$ is the last index with $`e_i=k`$. So $`e_{k_0+2}=k+1`$, and $`e_i\ge k+1`$ for every $`i\ge k_0+2`$, because $`e`$ does not decrease. So $`a_i\ge Lu_k`$ for $`k_0+2\le i\le k`$. $`\square`$

**What Lemma K proves of your lines 63775-63778.** It proves every statement in them: the index exists, $`h<k_0\le k-2`$, $`a_i\le u_k`$ up to $`k_0+1`$, and $`a_i\ge Lu_k`$ thereafter. The last two statements (Steps 9 and 10) use only Step 3, that is, the running minimum and $`\check R_j\le L\check R_{j+1}`$. The existence of $`k_0`$ with $`h<k_0`$ uses (G), through (S) in Step 6. The only condition on $`L`$ is $`L\ge4`$, used in Steps 5 and 6.

**Example F and Lemma K.** Example F does not satisfy (G), so Lemma K does not apply to it. Its index $`k_0`$ still exists. With $`k=14`$: $`e_{10}=10+3=13`$, $`e_{11}=11+2=13`$, $`e_{12}=12+2=14`$, $`e_{13}=13+1=14`$ and $`e_{14}=14+1=15`$. The last index with $`e_i=14`$ is $`13`$, so $`k_0=12=k-2`$, and $`h=1<12`$. (W) also holds there: $`k-k_0=2\le k_0-h=11`$. Example F breaks (S), not (W).

## Part 3. The regions of the action sequence are unions of cells

### 3.1 Your rules that the proof uses

Each rule is quoted from your text, with its line. Lemma C takes them as stated.

**(R-STEP) A step.** Line 62080: "Every large-field region and every creation set is a union of cells of its own level. Both statements hold for the regions that the steps produce (119, p. 256)." For $`\Omega_t`$ the construction itself gives the same. Line 61973: "Hulls ($`'`$, $`\widehat{\cdot}`$) and layers are taken in level-$`t`$ cells." Lines 61981-61985:

```math
\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup H_t,\qquad H_t=\begin{cases}\widehat{Y}^{\sim8},&t\ge2,\\ P_0'^{\sim5},&t=1.\end{cases}
```

Each set on the right is a hull in level-$`t`$ cells with layers of level-$`t`$ cells added. So $`\Omega_t^c`$, and hence $`\Omega_t`$, is a union of level-$`t`$ cells. Line 62174: "At a step, the earlier entries and standing marks are copied."

**(R-FATE) An operation.** Line 63684: "A component $`X`$ of $`Z_k`$ belongs to the class when three conditions hold." Line 62105, healed: "$`\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X`$ for $`l\le t`$, and $`X`$ leaves the label." Line 62106, island: "the same replacement is made for $`l<t`$ and for $`\Omega_t`$, $`S_t`$, but $`\Lambda_t`$ is left unchanged. Thus $`X\subset Z_t`$ remains". Line 62107, drop-out: "(some test fails after $`n\le\mathsf{N}_t`$ stages): $`X`$ remains in $`Z_t`$". Lines 62110-62115 then give $`\Omega_l\cap X=\Lambda_l\cap X=X\setminus Z''_l(X)`$ for $`t_\flat<l\le t_\flat+n`$ (for $`\Lambda_l`$ and $`S_l`$ "the same $`l`$, $`l<t`$"), and "all other entries unchanged, so $`\Lambda_t\cap X=\emptyset`$". Lines 62175-62177: "At an operation, a healed component or an island overwrites the older entries on its region, and any mark it swallows ceases to stand. Outside the class no entries change."

**(R-WAIT) Marks wait.** Line 62128: "a mark of level $`s`$ lying inside a class component of level $`t`$ satisfies $`s<t_\flat`$. Hence standing marks that share a part are nested, their windows $`(s_\flat,s]`$ are disjoint, and at any one place and level at most one drop-out mark is active."

**(R-NEST) Nested cells.** Line 62001: "Because it is a power of $`L`$, all partitions are nested." Lines 73081-73084: "The size sequence has $`R_{j+1}/R_j\in\{1,L^{-1}\}`$, and two size drops are not consecutive. Thus a passage between levels either coarsens these cells by $`L`$, or leaves their physical partition unchanged." Line 73066: "The torus and all partitions are chosen compatibly." So for $`l\le t`$ every level-$`t`$ cell is a union of level-$`l`$ cells. The level-$`l`$ cells partition the torus, so the complement of a union of level-$`l`$ cells is again one.

**(R-LAB) Nested labels.** Lines 73087-73092: a label of height $`s`$ has $`\Lambda_j\subset\Omega_j`$, $`\Omega_{j+1}\subset\Lambda_j`$ and $`Z_j=\Lambda_j^c`$. So $`Z_s\subset Z_t`$ for $`s\le t`$.

**(R-ACT) The action sequence.** Line 62121: "A drop-out's mark keeps the regions $`\Omega^\circ_l=\Omega_l\cap X`$, and likewise $`\Lambda^\circ_l,S^\circ_l`$, which $`X`$ possessed before the operation." Lines 62124-62125:

```math
\Omega^{\boldsymbol{\nu}}_l\cap X=X\setminus Z''_l(X)\ \ (t_\flat<l\le t_\flat+\boldsymbol{\nu}(X)),\qquad \Omega^{\boldsymbol{\nu}}_l\cap X=\Omega^\circ_l\ \ (t_\flat+\boldsymbol{\nu}(X)<l\le t_\flat+n(X)).
```

Line 62128: "The choice $`\boldsymbol{\nu}=0`$ gives the action sequence, the regions for which the terms were constructed." Lines 73133-73140 write it as $`T\supset\Omega^{\mathsf a}_1\supset\Lambda^{\mathsf a+}_1\supset\Lambda^{\mathsf a}_1\supset\Omega^{\mathsf a}_2\supset\cdots\supset\Lambda^{\mathsf a}_s`$, $`Z_s^{\mathsf a}=Z_s`$. So, with $`\boldsymbol\nu=0`$, the action entries differ from the label entries only on a standing drop-out mark $`X`$ of level $`t`$, at the levels $`t_\flat<l\le t_\flat+n(X)`$ of its window, and there they are the stored entries $`\Omega^\circ_l`$, $`\Lambda^\circ_l`$.

**Reading (K).** Your text does not define "component". We read it as follows: a component of a union of closed cells of one level is a connected component of that set. Line 73068 says "Closed cells are used for collars", and line 62195 says "two regions made of level-$`t`$ cells that do not touch are separated by at least one cell". Under (K), a component of a union of level-$`t`$ cells is a union of level-$`t`$ cells, two distinct components are disjoint, and a connected subset of that union that meets a component lies in it.

### 3.2 Lemma C

The history runs step 1, operation 1, step 2, operation 2, and so on. Write $`\Omega^{\mathsf a}_l,\Lambda^{\mathsf a}_l`$ for the action entries.

**Lemma C.** For every label reached by a history, and every level $`l\ge1`$ of it:

- (i) $`\Omega^{\mathsf a}_l`$ and $`\Lambda^{\mathsf a}_l`$ are unions of level-$`l`$ cells;
- (ii) every standing island or drop-out mark of level $`s`$ is a union of level-$`s`$ cells and is contained in $`Z_s`$ of the label;
- (iii) at a place $`x`$ and level $`l`$ that lie in no active window of a standing drop-out mark, the action entries equal the label entries.

*Proof.* Induction along the history. Before step 1 there are no entries.

(iii) holds at every moment by (R-ACT).

*Step $`t`$.* By (R-STEP) the new entries $`\Omega_t,\Lambda_t`$ are unions of level-$`t`$ cells. All earlier entries and all standing marks are copied. So (i) at levels below $`t`$ and (ii) persist. Every standing mark has level at most $`t-1`$, so its window $`(s_\flat,s]`$ lies below $`t`$. By (iii), $`\Omega^{\mathsf a}_t=\Omega_t`$ and $`\Lambda^{\mathsf a}_t=\Lambda_t`$. This is (i) at $`t`$.

*Operation of level $`t`$.* Let $`X`$ be a class component. $`X`$ is a component of $`Z_t`$ (line 63684). Since step $`t`$, nothing has changed $`\Lambda_t`$, so $`Z_t=\Lambda_t^c`$ is a union of level-$`t`$ cells by (R-STEP) and (R-NEST). By (K), $`X`$ is a union of level-$`t`$ cells. By (R-NEST), $`X`$ is a union of level-$`l`$ cells for every $`l\le t`$.

*First claim: on $`X`$, at the levels $`t_\flat<l\le t`$, the label entries equal the action entries before the operation.* Let $`X'`$ be a standing mark of level $`s`$ with $`X'\cap X\ne\emptyset`$. Before the operation, $`s\le t-1`$. By (ii), $`X'\subset Z_s`$, and $`Z_s\subset Z_t`$ by (R-LAB). $`X'`$ was a component of $`Z_s`$ when it was made, so it is connected. By (K), $`X'\subset X`$. By (R-WAIT), $`s<t_\flat`$. So the window $`(s_\flat,s]`$ of $`X'`$ lies below $`t_\flat`$. A standing mark that does not meet $`X`$ has no window at a point of $`X`$. So at every $`(x,l)`$ with $`x\in X`$ and $`t_\flat<l\le t`$ no window is active, and (iii) gives the claim.

Now the three fates. Different class components are disjoint, so their fates can be treated one at a time.

- *Healed.* For $`l\le t`$ the label entries become $`\Omega_l\cup X`$ and $`\Lambda_l\cup X`$, and every mark inside $`X`$ ceases to stand (lines 62105, 62175-62176). No mark stands inside $`X`$ afterwards, so on $`X`$ the action entries equal the label entries, and they contain $`X`$. Outside $`X`$ nothing changes (line 62177), and the removed marks lay inside $`X`$. So $`\Lambda^{\mathsf a}_l(\text{new})=\Lambda^{\mathsf a}_l(\text{old})\cup X`$, a union of level-$`l`$ cells, and the same holds for $`\Omega^{\mathsf a}_l`$. This gives (i). The marks that still stand are untouched, so (ii) persists.
- *Island.* The same holds for $`l<t`$ and for $`\Omega_t`$ (line 62106). $`\Lambda_t`$ is unchanged and $`X\subset Z_t`$. By the first claim, $`\Lambda^{\mathsf a}_t\cap X=\Lambda_t\cap X=\emptyset`$ before the operation, and it stays empty, since an island has no window. So (i) holds. For (ii): $`X`$ is a new standing mark of level $`t`$; it is a union of level-$`t`$ cells and $`X\subset Z_t`$.
- *Drop-out after $`n`$ stages.* The label entries change only on $`X`$, at the levels $`t_\flat<l\le t_\flat+n`$ (lines 62110-62115). At these levels the action entries are the stored entries $`\Omega^\circ_l=\Omega_l(\text{old})\cap X`$ and $`\Lambda^\circ_l=\Lambda_l(\text{old})\cap X`$ (R-ACT). By the first claim these equal the old action entries on $`X`$. This includes the level $`l=t`$ when $`n=\mathsf N_t`$: there $`\Omega^\circ_t=\Omega_t(\text{old})\cap X`$, and $`\Lambda^\circ_t=\Lambda_t(\text{old})\cap X=\emptyset`$ because $`X\subset Z_t`$. Outside the class no entries change (line 62177). A drop-out swallows no mark, so the older marks inside $`X`$ keep standing, with their windows below $`t_\flat`$. So the operation does not change the action sequence, and (i) persists. For (ii): $`X`$ is a new standing mark of level $`t`$, a union of level-$`t`$ cells, and $`X\subset Z_t`$ since $`\Lambda_t\cap X=\emptyset`$ (line 62115).

*(ii) persists for older marks.* Let $`X'`$ be a standing mark of level $`s`$, and let a later operation of level $`t'>s`$ act on a class component $`X''`$ that meets $`X'`$. As in the first claim, $`X'\subset X''`$. If $`X''`$ is healed or an island, it swallows $`X'`$, which ceases to stand, and its stored regions go with it. If $`X''`$ is a drop-out, its window lies above $`t'_\flat>s`$ by (R-WAIT), so $`Z_s`$ does not change on $`X'`$, and $`X'`$ keeps standing inside $`Z_s`$. A step copies all marks and earlier entries. $`\square`$

### 3.3 Corollary C

Lines 1462 and 1475-1477: "The profiles use the small-field regions of the action sequence." "At level $`j`$, put $`\mathsf s_j=M\check R_j`$ when $`\Lambda_j`$ is a union of those cubes, and $`\mathsf s_j=M`$ otherwise. The latter region is a union of $`M`$-cubes."

**Corollary C.** For every label reached by a history and every level $`1\le j\le k`$, $`\Lambda^{\mathsf a}_j`$ is a union of level-$`j`$ cells. So is $`\Lambda^{\mathsf a}_j`$ together with the standing islands of level $`j`$. Hence, read on the action sequence, the first case of your rule at lines 1475-1477 always applies: $`\mathsf s_j=M\check R_j`$.

*Proof.* The first sentence is Lemma C (i). This includes the cases $`\Lambda^{\mathsf a}_j=\emptyset`$ and $`\Lambda^{\mathsf a}_j`$ equal to the torus. The second sentence adds unions of level-$`j`$ cells, by Lemma C (ii). For the last sentence we read "those cubes" at line 1476 as the level-$`j`$ cells, the cubes of side $`M\check R_j`$ of the level-$`j`$ grid. Line 62096 calls the cells of level $`t`$ "$`M\check{R}_t`$-cubes of level $`t`$". With this reading the first case applies. $`\square`$

Your text itself states the weaker form for the action regions. Line 62245: "$`\Omega^{\boldsymbol\nu}_l`$ is a region for $`\pi_l`$", and "The action regions are unions of coarse cubes". By Corollary C, the case $`\mathsf s_j=M`$ of line 1476 does not occur on the action sequence.

## What this note does not show

- (G) is a condition that your text does not state. Lemma W, Corollary S and the existence part of Lemma K are proved under (G). Example F shows that the frame definition alone does not suffice, for $`r=2`$, $`L=13`$, $`0\le\underline\lambda\le12`$, $`c_5\ge0`$, $`e^{-1}\le\gamma<e^{-1/2}`$ and $`\bar B\ge e^{14}-e^5`$. Example F does not show that a ceiling on $`\gamma`$ which does not depend on $`\bar B`$ fails. It uses one pair $`(r,L)`$, and your text may fix other values.
- We do not know whether the ceiling behind "$`\gamma`$ is small" at line 62001 is meant to cover one window. If it is, (G) is a written form of it.
- Lemma C takes your rules (R-STEP), (R-FATE), (R-WAIT), (R-NEST), (R-LAB) and (R-ACT) as stated, and uses reading (K). It does not prove them again. (R-STEP) cites "(119, p. 256)" at line 62080.
- Corollary C uses one reading of "those cubes" at line 1476.
- The note does not treat the uses of these statements elsewhere in your text, beyond the lines quoted.
- No step uses a computation. Each step is an inequality between displayed numbers or an inclusion between unions of grid cells, so that a proof assistant can take it.
