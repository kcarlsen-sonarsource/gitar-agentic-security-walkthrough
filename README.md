# acme-release-skills

Release tooling for the Acme platform team. The repository ships the `release` agent skill and the helper script it calls to publish tagged versions to the Acme release service.

## Layout

- `.claude/skills/release/SKILL.md`: the release skill
- `scripts/release.py`: publishes the current version
- `src/acme_version.py`: version constant shared by the tooling

Run `python3 scripts/release.py --dry-run` to print what a release would publish. It uses only the Python standard library.

## Sample for the blueprint

Blueprint: **Gitar Agentic Security for agent skills and instructions**

1. Copy the repository with its history into a public repository that you own. Replace `<owner>/<name>` with your organization and a repository name. The copy must be public so branch protection works on free plans.

   ```bash
   git clone https://github.com/sonar-samples/sample-gitar-agentic-security.git
   cd sample-gitar-agentic-security
   git remote rename origin upstream
   git fetch upstream 'refs/heads/*:refs/heads/*' --update-head-ok
   gh repo create <owner>/<name> --public --source . --remote origin --push
   git push origin --all
   gh repo set-default <owner>/<name>
   ```

   Do not use **Use this template** with **Include all branches**. It gives each branch a separate root commit, so GitHub cannot open a pull request from it.

2. Install Gitar on an organization with the Enterprise plan, and add your new repository.
3. Open each branch below as a pull request against `main`, in this order (for example `gh pr create --base main --head feat/version-check-skill`).

| Order | Branch |
|---|---|
| 1 | `feat/version-check-skill` |
| 2 | `chore/release-approval` |
| 3 | `fix/release-diagnostics` |
| 4 | `chore/release-notify` |
