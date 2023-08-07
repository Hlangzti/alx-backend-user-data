#!/usr/bin/env python3
"""
Basic Authentication module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple, TypeVar
import hashlib


class BasicAuth(Auth):
    """Basic Authentication class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str)\
            -> str:
