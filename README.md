# Mahatav Arora — Portfolio

An editorial, spatial portfolio built with Astro, with a small Django JSON API that reads the same project data.

## Deploy to GitHub Pages

This project is configured for the root user site:

`https://mahatav.github.io`

To publish at that exact URL:

1. Rename the GitHub repository from `Portfolio` to `Mahatav.github.io`.
2. Keep the default deployment branch as `master`.
3. Open repository Settings -> Pages and set Source to `GitHub Actions`.
4. In Settings -> Secrets and variables -> Actions, add:
   - `PUBLIC_WEB3FORMS_ACCESS_KEY` = your Web3Forms access key.
5. Push to `master`. `.github/workflows/deploy.yml` will build and publish automatically.

The Astro `site` is set to `https://mahatav.github.io` and intentionally has no
repository `base`, because GitHub serves specially named user-site repositories
from `/`. The workflow also checks the repository name, preventing an accidental
broken deployment from the old `Portfolio` repository path.

## Frontend

```bash
npm install
npm run dev
```

Astro runs at `http://localhost:4321`.

## Django API

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/manage.py runserver
```

The API is available at:

- `GET /api/health/`
- `GET /api/portfolio/`

Portfolio content lives in `src/data/portfolio.json`, which is imported by Astro and served by Django. Update it once and both layers stay aligned.
