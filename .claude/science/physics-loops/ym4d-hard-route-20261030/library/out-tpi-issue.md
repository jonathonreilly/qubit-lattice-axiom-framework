**Title:** A proof of the coarse covariance bound at YM4_1400 line 102280

Ethan and Levent,

At [YM4_1400 102280–102281](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex#L102278-L102281) your free calculation uses
\(|G_{k_1}(p,q)|\le CL^{-4k_1}\). We found this statement and its later
uses. We did not find a proof of it in the pinned file. The note records
the whole-file searches and the passages we read.

[This note](@NOTE_LINK@) gives a proof at every level, the terminal level
included, uniformly in mesh and volume. The statement is yours. So are the
pieces: your CF12 precision bound (lines 5631–5634), your strong inverse
and your curvature minimizer. The note reads CF12 as a variance bound for
the blocked potential, bounds its diagonal, and lifts it to the fine
lattice. This gives the coarse factor in your error at 102283–102289.
The free-field method is Balaban's.

The scope is one real colour, unit coupling and the trivial flat reference on compatible four-dimensional periodic tori. Your written strong inverse and curvature identification are ported inputs. We quote your slice estimate at lines 4337 and 100994 for the full tower.
We do not reprove it. The proof of the bound does not use it.

The note does not prove spatial decay of the retained covariance, the separated-background bound, or the slice estimate. It does not prove an interacting source law, cutoff-window comparison, or your main theorem. The bound covers the terminal level. It does not set \(G_K\) to zero.

Codex (gpt-6-astra) wrote the proof and this note. Claude (Opus 5.5) checked the proof line by line, and its repairs are applied.

This is a proposed proof for your review. It is research text, not an audit, and grants no status.

