# Independent supporting-proof receipt review — findings

Initial staged tree: ba41c2d2dfbf9263d6e3eb8b05b238ede9c68228.

Material finding: the supporting-proof guard tested normalized Type (extractor tuple index 1), accepting an explicit unknown Type whose raw field exists but normalized value is None. Actual API fixture with `**Type:** novel_theorem` returned mechanical ok. Require raw Type absence (index 0) for support; retain normalized Type validation for full note records. Final acceptance pending same-session correction confirmation.

Independent initial validation: 44 repository tests passed in 20.695s. Four additional fixtures confirmed schema2 empty acceptance, duplicate supporting classification rejection, helper-only input pin acceptance, and retained cache freshness requirement. No science execution or full pipeline was performed.
