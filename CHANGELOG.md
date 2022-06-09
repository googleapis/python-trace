# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-trace/#history

## [0.24.2](https://github.com/googleapis/python-trace/compare/v0.24.1...v0.24.2) (2022-06-09)


### Bug Fixes

* **deps:** require protobuf<4.0.0 on v0 branch ([#235](https://github.com/googleapis/python-trace/issues/235)) ([30229b3](https://github.com/googleapis/python-trace/commit/30229b335fd348d0a737d44e1063214311d414c3))

### [0.24.1](https://github.com/googleapis/python-trace/compare/v0.24.0...v0.24.1) (2022-04-03)


### Bug Fixes

* **deps:** allow google-cloud-core v2 ([#209](https://github.com/googleapis/python-trace/issues/209)) ([195cbf0](https://github.com/googleapis/python-trace/commit/195cbf085732ffdf2c01b61108062937c4648969))
* **deps:** require google-api-core >= 1.31.5, >= 2.3.2 on v0 release ([#198](https://github.com/googleapis/python-trace/issues/198)) ([cded8ea](https://github.com/googleapis/python-trace/commit/cded8ea4b9d3ff307dd7d986d156a31ea2c61c7e))

## [0.24.0](https://www.github.com/googleapis/python-trace/compare/v0.23.0...v0.24.0) (2020-08-06)


### ⚠ BREAKING CHANGES

* **trace:** remove `span_path` resource helper method from v2; modify retry configs; standardize usage of 'optional' and 'required' for args in docstrings; add 2.7 deprecation warning (via synth)  (#10075)

### Features

* **trace:** add `client_options` to constructor ([#9154](https://www.github.com/googleapis/python-trace/issues/9154)) ([a5b4f7a](https://www.github.com/googleapis/python-trace/commit/a5b4f7aa4575364868ba80aa0a3b1289dc7f0c3e))
* added support for span kind ([#28](https://www.github.com/googleapis/python-trace/issues/28)) ([23ba194](https://www.github.com/googleapis/python-trace/commit/23ba194fdc59c34bfa5f66aba89a6baa8d7bb527))


### Bug Fixes

* **trace:** remove `span_path` resource helper method from v2; modify retry configs; standardize usage of 'optional' and 'required' for args in docstrings; add 2.7 deprecation warning (via synth)  ([#10075](https://www.github.com/googleapis/python-trace/issues/10075)) ([4c02194](https://www.github.com/googleapis/python-trace/commit/4c02194a8c1390b2a382e1f3aaef8138baf02f07))


### Documentation

* add python 2 sunset banner to documentation ([#9036](https://www.github.com/googleapis/python-trace/issues/9036)) ([52f3ab5](https://www.github.com/googleapis/python-trace/commit/52f3ab5db26a2b49d1e292ea9b349c1b698fa695))

## 0.23.0

10-15-2019 06:59 PDT


### Dependencies
- Pin 'google-cloud-core >= 1.0.3, < 2.0.0dev'. ([#9445](https://github.com/googleapis/google-cloud-python/pull/9445))

### Documentation
- Change requests intersphinx url (via synth). ([#9410](https://github.com/googleapis/google-cloud-python/pull/9410))
- Fix intersphinx reference to requests ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- Remove compatability badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))

## 0.22.1

08-12-2019 13:51 PDT

### Implementation Changes
- Remove send/recv msg size limit (via synth). ([#8973](https://github.com/googleapis/google-cloud-python/pull/8973))

### Documentation
- Fix links to googleapis.dev ([#8998](https://github.com/googleapis/google-cloud-python/pull/8998))
- Fix pip / usage examples in README.rst. ([#8833](https://github.com/googleapis/google-cloud-python/pull/8833))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

## 0.22.0

07-24-2019 17:50 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8408](https://github.com/googleapis/google-cloud-python/pull/8408))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8526](https://github.com/googleapis/google-cloud-python/pull/8526))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- All: Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8368](https://github.com/googleapis/google-cloud-python/pull/8368))
- Add disclaimer to auto-generated template files (via synth). ([#8332](https://github.com/googleapis/google-cloud-python/pull/8332))
- Fix coverage in 'types.py' (via synth). ([#8167](https://github.com/googleapis/google-cloud-python/pull/8167))
- Add empty lines (via synth). ([#8075](https://github.com/googleapis/google-cloud-python/pull/8075))

## 0.21.0

05-16-2019 12:58 PDT


### Implementation Changes
- Add routing header to method metadata (via synth).  ([#7602](https://github.com/googleapis/google-cloud-python/pull/7602))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add `client_info` support to clients. ([#7899](https://github.com/googleapis/google-cloud-python/pull/7899))

### Dependencies
- Pin `google-cloud-core >= 1.0.0, < 2.0dev`. ([#7993](https://github.com/googleapis/google-cloud-python/pull/7993))

### Documentation
- Update docstring for `page_size` (via synth). ([#7688](https://github.com/googleapis/google-cloud-python/pull/7688))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Pick up stub docstring fix in GAPIC generator. ([#6985](https://github.com/googleapis/google-cloud-python/pull/6985))

### Internal / Testing Changes
- Add nox session `docs`, reorder methods (via synth). ([#7783](https://github.com/googleapis/google-cloud-python/pull/7783)) and ([#7784](https://github.com/googleapis/google-cloud-python/pull/7784))
- Copy lintified proto files (via synth). ([#7455](https://github.com/googleapis/google-cloud-python/pull/7455))
- Add clarifying comment to blacken nox target. ([#7406](https://github.com/googleapis/google-cloud-python/pull/7406))
- Remove unused message exports (via synth). ([#7278](https://github.com/googleapis/google-cloud-python/pull/7278))
- Copy proto files alongside protoc versions ([#7254](https://github.com/googleapis/google-cloud-python/pull/7254))
- Trivial gapic-generator change. ([#7236](https://github.com/googleapis/google-cloud-python/pull/7236))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers (via synth). ([#7161](https://github.com/googleapis/google-cloud-python/pull/7161))
- Protoc-generated serialization update. ([#7098](https://github.com/googleapis/google-cloud-python/pull/7098))

## 0.20.2

12-17-2018 17:06 PST


### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))

## 0.20.1

12-07-2018 16:06 PST

### Implementation Changes
- Fix trace client memory leak ([#6856](https://github.com/googleapis/google-cloud-python/pull/6856))

### Dependencies
- Update version of google-cloud-core ([#6858](https://github.com/googleapis/google-cloud-python/pull/6858))

### Internal / Testing Changes
- Add baseline for synth.metadata

## 0.20.0

12-05-2018 13:16 PST


### Implementation Changes
- Use moved iam.policy now at google.api_core.iam.policy ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6577](https://github.com/googleapis/google-cloud-python/pull/6577))
- Fix client_info bug, update docstrings and timeouts. ([#6424](https://github.com/googleapis/google-cloud-python/pull/6424))
- Pass credentials into TraceServiceClient ([#5596](https://github.com/googleapis/google-cloud-python/pull/5596))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/googleapis/google-cloud-python/pull/5364))

### New Features
- Add 'synth.py'. ([#6083](https://github.com/googleapis/google-cloud-python/pull/6083))

### Dependencies
- Bump minimum 'api_core' version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Add static HTML redirect page for 'trace/starting.html'. ([#6142](https://github.com/googleapis/google-cloud-python/pull/6142))
- Prep docs for repo split. ([#6024](https://github.com/googleapis/google-cloud-python/pull/6024))
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Updates to noxfile and other templates. Start Blackening. ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792)),
  ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701)),
  ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698)),
  ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666)),
  ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Add kokoro for trace, remove trace from CircleCI ([#6112](https://github.com/googleapis/google-cloud-python/pull/6112))
- Use inplace installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))
- Add Test runs for Python 3.7 and remove 3.4 ([#5295](https://github.com/googleapis/google-cloud-python/pull/5295))
- Fix bad trove classifier
- Move unit test from gax to gapic ([#4988](https://github.com/googleapis/google-cloud-python/pull/4988))

## 0.19.0

### Dependencies

- The minimum version for `google-api-core` has been updated to version 1.0.0. This may cause some incompatibility with older google-cloud libraries, you will need to update those libraries if you have a dependency conflict. (#4944, #4946)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)

## 0.18.0

### Breaking changes

- The underlying autogenerated client library was re-generated to pick up new 
  features and resolve bugs, this may change the exceptions raised from various
  methods. (#4799)

## 0.17.0

### Notable Implementation Changes

- Default to use Stackdriver Trace V2 API if calling `from google.cloud import trace`.
  Using V1 API needs to be explicitly specified in the import.(#4437)

PyPI: https://pypi.org/project/google-cloud-trace/0.17.0/

## 0.16.0

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)

PyPI: https://pypi.org/project/google-cloud-trace/0.16.0/
