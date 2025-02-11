import os
import time

import requests
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.auth import ExpiringTokenAuthentication

LATENCY_CHECK_URL = os.getenv("LATENCY_CHECK_URL")


class LatencyView(APIView):
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_time = time.time()
        try:
            response = requests.get(LATENCY_CHECK_URL, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return Response(
                {"error": f"Unable to reach {LATENCY_CHECK_URL}"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        return Response(
            {
                "result": f"{latency_ms:.2f}ms",
                "value": latency_ms,
                "unit": "ms",
            }
        )
