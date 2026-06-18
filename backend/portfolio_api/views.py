import json
from pathlib import Path

from django.http import JsonResponse

DATA_PATH = Path(__file__).resolve().parents[2] / "src" / "data" / "portfolio.json"


def health(_request):
    return JsonResponse({"status": "ok", "service": "mahatav-portfolio-api"})


def portfolio(_request):
    with DATA_PATH.open(encoding="utf-8") as data_file:
        return JsonResponse(json.load(data_file))
