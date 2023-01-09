# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.trace import gapic_version as package_version

__version__ = package_version.__version__


from .services.trace_service import TraceServiceClient
from .services.trace_service import TraceServiceAsyncClient

from .types.trace import GetTraceRequest
from .types.trace import ListTracesRequest
from .types.trace import ListTracesResponse
from .types.trace import PatchTracesRequest
from .types.trace import Trace
from .types.trace import Traces
from .types.trace import TraceSpan

__all__ = (
    'TraceServiceAsyncClient',
'GetTraceRequest',
'ListTracesRequest',
'ListTracesResponse',
'PatchTracesRequest',
'Trace',
'TraceServiceClient',
'TraceSpan',
'Traces',
)
