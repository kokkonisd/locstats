# locstats contributing guide

If you'd like to contribute to locstats, please follow these steps:

1. Fork the repo, and clone the fork
2. Create a virtual environment to avoid collisions with locally installed packages.
   This step is optional but **strongly** recommended. You can do this via the following
   command:

   ```text
   $ python3 -m venv venv/     # Create the virtualenv
   $ source venv/bin/activate  # And now activate it
   ```
3. Install the regular dependencies & developer dependencies:

   ```text
   (venv) $ python -m pip install -r requirements.txt -r dev_requirements.txt
   ```
4. Set up pre-commit checks:

   ```text
   (venv) $ pre-commit install
   ```
5. Develop your local changes. Don't forget to test by running `tox -s`!
6. Commit local changes, pass pre-commit checks, and push to remote.
7. Create a pull request. It is **greatly** appreciated if you mention an
   [issue](https://github.com/kokkonisd/locstats/issues) on your PR (or create _then_
   mention it if it doesn't already exist).

A CI will automatically run on your PR; obviously, all PRs must pass all CI checks
before even being reviewed.
