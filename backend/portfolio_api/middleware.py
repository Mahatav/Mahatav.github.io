class DevCorsMiddleware:
    """Allows the local Astro dev server (:4321) to call this API during
    development. Intentionally permissive and dev-only — production serves the
    site statically, so no cross-origin access is needed there.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "http://localhost:4321"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
