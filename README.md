# Mahatav Arora — Portfolio

An editorial, spatial portfolio built with Astro, with a small Django JSON API that reads the same project data.

## Deploy to GitHub Pages

1. Push this repo to GitHub and keep your default branch as `main`.
2. In GitHub, open Settings -> Pages, then set Source to `GitHub Actions`.
3. In GitHub, open Settings -> Secrets and variables -> Actions and add:
	- `PUBLIC_WEB3FORMS_ACCESS_KEY` = your Web3Forms access key.
4. Commit and push these changes. The workflow at `.github/workflows/deploy.yml` will build and deploy automatically.

Astro base-path handling is automatic for project Pages URLs (for example `/repo-name`).

If you attach a custom domain and want root deployment, set `DEPLOY_BASE=/` in your build environment.

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
