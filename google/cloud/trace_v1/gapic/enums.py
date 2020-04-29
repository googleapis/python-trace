# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class ListTracesRequest(object):
    class ViewType(enum.IntEnum):
        """
        Type of data returned for traces in the list.

        Attributes:
          VIEW_TYPE_UNSPECIFIED (int): See ``HttpRule``.
          MINIMAL (int): Minimal view of the trace record that contains only the project
          and trace IDs.
          ROOTSPAN (int): Root span view of the trace record that returns the root spans along
          with the minimal trace data.
          COMPLETE (int): If this SourceCodeInfo represents a complete declaration, these are
          any comments appearing before and after the declaration which appear to
          be attached to the declaration.

          A series of line comments appearing on consecutive lines, with no other
          tokens appearing on those lines, will be treated as a single comment.

          leading_detached_comments will keep paragraphs of comments that appear
          before (but not connected to) the current element. Each paragraph,
          separated by empty lines, will be one comment element in the repeated
          field.

          Only the comment content is provided; comment markers (e.g. //) are
          stripped out. For block comments, leading whitespace and an asterisk
          will be stripped from the beginning of each line other than the first.
          Newlines are included in the output.

          Examples:

          optional int32 foo = 1; // Comment attached to foo. // Comment attached
          to bar. optional int32 bar = 2;

          optional string baz = 3; // Comment attached to baz. // Another line
          attached to baz.

          // Comment attached to qux. // // Another line attached to qux. optional
          double qux = 4;

          // Detached comment for corge. This is not leading or trailing comments
          // to qux or corge because there are blank lines separating it from //
          both.

          // Detached comment for corge paragraph 2.

          optional string corge = 5; /\* Block comment attached \* to corge.
          Leading asterisks \* will be removed. */ /* Block comment attached to \*
          grault. \*/ optional int32 grault = 6;

          // ignored detached comments.
        """

        VIEW_TYPE_UNSPECIFIED = 0
        MINIMAL = 1
        ROOTSPAN = 2
        COMPLETE = 3


class TraceSpan(object):
    class SpanKind(enum.IntEnum):
        """
        Type of span. Can be used to specify additional relationships between spans
        in addition to a parent/child relationship.

        Attributes:
          SPAN_KIND_UNSPECIFIED (int): Unspecified.
          RPC_SERVER (int): Indicates that the span covers server-side handling of an RPC or other
          remote network request.
          RPC_CLIENT (int): Indicates that the span covers the client-side wrapper around an RPC or
          other remote request.
        """

        SPAN_KIND_UNSPECIFIED = 0
        RPC_SERVER = 1
        RPC_CLIENT = 2
