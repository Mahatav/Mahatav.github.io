"""Read-only JSON API that serves the portfolio content.

Both views back onto the same portfolio.json the Astro frontend builds from, so
the API and the site never drift out of sync.
"""

import json
from pathlib import Path

from django.http import JsonResponse

# portfolio.json lives in the frontend source tree, two levels up from here.
DATA_PATH = Path(__file__).resolve().parents[2] / "src" / "data" / "portfolio.json"


def health(_request):
    """Liveness probe for uptime checks and deploy smoke tests."""
    return JsonResponse({"status": "ok", "service": "mahatav-portfolio-api"})


def portfolio(_request):
    """Return the full portfolio dataset as JSON."""
    with DATA_PATH.open(encoding="utf-8") as data_file:
        return JsonResponse(json.load(data_file))
