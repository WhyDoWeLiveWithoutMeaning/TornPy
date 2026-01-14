class BaseResource:
    def __init__(self, parent):
        self._parent = parent
        self._request = parent._request
        self._build_url = parent._build_url
        self._prepare_params = parent._prepare_params
        self._handle_response = parent._handle_response