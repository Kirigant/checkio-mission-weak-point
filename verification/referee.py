from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.signals import ON_CONNECT

from tests import TESTS


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "weak_point",
            "js": "weakPoint",
        }
    ).on_ready)
