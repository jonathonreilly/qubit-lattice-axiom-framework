# Repository AI Model Policy

Use the best available model for all AI-assisted tasks in this repository.

AI planning surfaces (agent instructions, TOE closure scorecard) live on the
standing `ai/execution` branch, which never merges into `main`:
`git fetch origin ai/execution --quiet && git show origin/ai/execution:README.md`.
