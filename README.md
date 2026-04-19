# QM Visual

Interactive quantum mechanics modules delivered as a Streamlit application: fourteen numbered chapters — **1–5** (postulates, Hilbert space, measurement, Pauli observables, uncertainty) and **6–14** (wave packets through time evolution in a box), with one spherical-harmonic visualization on the unit sphere.

## Repository layout

| Path | Description |
|------|-------------|
| `app.py` | Application entry and course index |
| `pages/` | One module per numbered chapter |
| `qm_course/` | Shared numerical helpers and models |
| `dft_course/` | Reserved package for a separate DFT track (see `dft_course/README.md`) |
| `requirements.txt` | Python dependencies |
| `.streamlit/` | Streamlit configuration |

## Local run

```bash
cd "QM Visual"
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deployment — Streamlit Community Cloud

1. Push this repository to GitHub (see [Git](#git) if you are starting from an uninitialized folder).
2. Sign in at [share.streamlit.io](https://share.streamlit.io/) with the **same GitHub account** that owns the repo (or one that has access).
3. **Create app** → pick the repository → set **Main file path** to `app.py` → **Deploy**.
4. Share the issued `https://<name>.streamlit.app` URL. Sidebar entries come from every `pages/*.py` script.

**Branch:** Cloud defaults to `main`; deploy from another branch in the app settings if needed.

**Secrets:** never commit credentials. Use the Cloud dashboard **Secrets** UI for keys; keep `.streamlit/secrets.toml` local only (it is gitignored).

## Deployment — Hugging Face Spaces

Create a Space with the Streamlit SDK, set `app_file: app.py`, and install dependencies from `requirements.txt`.

## Git

```bash
cd "/Users/devcmrl/Desktop/Work/Devi/Semesters/Software/QM Visual"
git init
git add .
git commit -m "Initial commit: QM Visual"
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

Replace the remote URL with your repository (for example `https://github.com/devCMRL/Quantum-Mechanics-Visualized.git`).

## Extending the course

Add new chapters as `pages/NN_Title.py`; the numeric prefix controls sidebar order. Optional numerical packages (e.g. [qmsolve](https://github.com/quantum-visualizations/qmsolve), [QuTiP](https://qutip.org/)) belong in `requirements.txt` when a chapter imports them.

The `dft_course/` directory is reserved for a separate density-functional-theory track; it is not referenced by `app.py` until corresponding pages are added.

## Attribution

Third-party libraries are listed in `THIRD_PARTY.md`. Any adapted external material should be credited there with license references.

## License

See the `LICENSE` file at the repository root (MIT).
