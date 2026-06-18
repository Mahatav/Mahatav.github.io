# Mahatav Arora — Portfolio

An editorial, spatial portfolio built with Astro, with a small Django JSON API that reads the same project data.

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
