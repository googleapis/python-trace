Python Client for Stackdriver Trace API (`Alpha`_)
==================================================

`Stackdriver Trace API`_: Sends application trace data to Stackdriver Trace for viewing. Trace data
is collected for all App Engine applications by default. Trace data from
other applications can be provided using this API. This library is used to
interact with the Trace API directly. If you are looking to instrument
your application for Stackdriver Trace, we recommend using OpenCensus.

- `Client Library Documentation`_
- `Product Documentation`_

.. _Alpha: https://github.com/googleapis/google-cloud-python/blob/master/README.rst
.. _Stackdriver Trace API: https://cloud.google.com/devtools-cloudtrace
.. _Client Library Documentation: https://googleapis.github.io/google-cloud-python/latest/devtools-cloudtrace/usage.html
.. _Product Documentation:  https://cloud.google.com/devtools-cloudtrace

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Stackdriver Trace API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Stackdriver Trace API.:  https://cloud.google.com/devtools-cloudtrace
.. _Setup Authentication.: https://googleapis.github.io/google-cloud-python/latest/core/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-devtools-cloudtrace


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-devtools-cloudtrace

Preview
~~~~~~~

TraceServiceClient
^^^^^^^^^^^^^^^^^^

.. code:: py

    from google.cloud import trace_v2

    client = trace_v2.TraceServiceClient()

    name = client.project_path('[PROJECT]')

    # TODO: Initialize `spans`:
    spans = []

    client.batch_write_spans(name, spans)

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Stackdriver Trace API
   API to see other available methods on the client.
-  Read the `Stackdriver Trace API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `repository’s main README`_ to see the full list of Cloud
   APIs that we cover.

.. _Stackdriver Trace API Product documentation:  https://cloud.google.com/devtools-cloudtrace
.. _repository’s main README: https://github.com/googleapis/google-cloud-python/blob/master/README.rst