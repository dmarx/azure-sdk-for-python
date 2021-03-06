# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Answer
    from ._models_py3 import CreativeWork
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import Identifiable
    from ._models_py3 import Query
    from ._models_py3 import QueryContext
    from ._models_py3 import Response
    from ._models_py3 import ResponseBase
    from ._models_py3 import SearchResponse
    from ._models_py3 import SearchResultsAnswer
    from ._models_py3 import Thing
    from ._models_py3 import WebMetaTag
    from ._models_py3 import WebPage
    from ._models_py3 import WebWebAnswer
except (SyntaxError, ImportError):
    from ._models import Answer
    from ._models import CreativeWork
    from ._models import Error
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import Identifiable
    from ._models import Query
    from ._models import QueryContext
    from ._models import Response
    from ._models import ResponseBase
    from ._models import SearchResponse
    from ._models import SearchResultsAnswer
    from ._models import Thing
    from ._models import WebMetaTag
    from ._models import WebPage
    from ._models import WebWebAnswer
from ._custom_search_client_enums import (
    ErrorCode,
    ErrorSubCode,
    SafeSearch,
    TextFormat,
)

__all__ = [
    'Answer',
    'CreativeWork',
    'Error',
    'ErrorResponse', 'ErrorResponseException',
    'Identifiable',
    'Query',
    'QueryContext',
    'Response',
    'ResponseBase',
    'SearchResponse',
    'SearchResultsAnswer',
    'Thing',
    'WebMetaTag',
    'WebPage',
    'WebWebAnswer',
    'ErrorCode',
    'ErrorSubCode',
    'SafeSearch',
    'TextFormat',
]
