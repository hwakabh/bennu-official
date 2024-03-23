# Changelog

## [0.7.3](https://github.com/hwakabh/bennu-official/compare/v0.7.2...v0.7.3) (2024-03-23)


### Dependencies

* updated frequencies of checking. ([f78f9fd](https://github.com/hwakabh/bennu-official/commit/f78f9fd7da05e11e54e063c8d6e9729862f10a95))

## [0.7.2](https://github.com/hwakabh/bennu-official/compare/v0.7.1...v0.7.2) (2024-03-08)


### Bug Fixes

* **ui:** enabled to flip active class in both &lt;li&gt; and <a> ([78ad1ff](https://github.com/hwakabh/bennu-official/commit/78ad1ff127c410b5759cf86e559e2def6b245a61))


### Performance Improvements

* **build:** enabled caches on nginx Pods. ([f0f48e7](https://github.com/hwakabh/bennu-official/commit/f0f48e7bbd19233f1cf79350dc61265c9878a73b))
* **build:** enforced replicas of django Pods. ([6529d2e](https://github.com/hwakabh/bennu-official/commit/6529d2ecc566857269e71c43fb43c7b104f1c8af))
* fixed routing unstable issues with LabelSelectors. ([3570e1d](https://github.com/hwakabh/bennu-official/commit/3570e1d5bc328435b94531aa381d98ccdc6e5cf7))

## [0.7.1](https://github.com/hwakabh/bennu-official/compare/v0.7.0...v0.7.1) (2024-02-04)


### Bug Fixes

* **docs:** added notes for deployment. ([8b0b94e](https://github.com/hwakabh/bennu-official/commit/8b0b94e8208e55cf27c70c67ec6e109992425931))
* **release-please:** removed version from PR body. ([c2e214e](https://github.com/hwakabh/bennu-official/commit/c2e214ee82a646f57f9933a669fbb9f945e5b147))
* **release-please:** typo. ([6d2c9ff](https://github.com/hwakabh/bennu-official/commit/6d2c9ffeb515770dce7b64fb4664cb1a54a3d2c6))

## [0.7.0](https://github.com/hwakabh/bennu-official/compare/v0.6.3...v0.7.0) (2024-02-04)


### Features

* **ci:** added release-please config for labelings. ([9f2233f](https://github.com/hwakabh/bennu-official/commit/9f2233fa16791177a2ac393b7159f0073f27c6d2))


### Bug Fixes

* **ci:** added branches to pull_request_target. ([c14fcee](https://github.com/hwakabh/bennu-official/commit/c14fceee680131900775af218a90f2a92e81c485))
* **ci:** added manifest-file for release-please. ([54e848e](https://github.com/hwakabh/bennu-official/commit/54e848ee3897f1417c1df28da57c8c43da7b3e14))
* **ci:** removed branches associations. ([5ffd7ed](https://github.com/hwakabh/bennu-official/commit/5ffd7edcf04540e12c5b041cbba23cf0c3654b4b))
* **ci:** updated manifest-file for release-please. ([34712d9](https://github.com/hwakabh/bennu-official/commit/34712d96463b27704d7c57a7630c8bf9891a8f7e))


### Reverts

* **ci:** added relations to all branches for e2e. ([081eba0](https://github.com/hwakabh/bennu-official/commit/081eba0966a945bcf113c9ae81a72c8bce02eb4a))

## [0.6.3](https://github.com/hwakabh/bennu-official/compare/v0.6.2...v0.6.3) (2024-02-04)


### Bug Fixes

* **ci:** added workflow_dispatch to release-please. ([0fbbacd](https://github.com/hwakabh/bennu-official/commit/0fbbacd3638e1127f2044a04dbef20eb89cd18ec))
* **ci:** updated workflow triggers. ([c4c4f11](https://github.com/hwakabh/bennu-official/commit/c4c4f11a4c53d54fc35dd156cab3386c1e6fe96a))

## [0.6.2](https://github.com/hwakabh/bennu-official/compare/v0.6.1...v0.6.2) (2024-02-04)


### Bug Fixes

* **ci:** changed token-type from github-token to PAT. ([6a264ae](https://github.com/hwakabh/bennu-official/commit/6a264ae829aae6d966919c1c2f612bab36efd025))
* **ci:** updated workflow triggers to run all branch updates. ([5c69207](https://github.com/hwakabh/bennu-official/commit/5c692073240d1134a417f9c46df8d2b34449bde0))

## [0.6.1](https://github.com/hwakabh/bennu-official/compare/v0.6.0...v0.6.1) (2024-02-04)


### Bug Fixes

* **ci:** escaped hyphen ([ef99919](https://github.com/hwakabh/bennu-official/commit/ef999192286a860d5bef27f8f0222b77061f68b0))
* **ci:** Simplified regexp of head-branch ([189bc3d](https://github.com/hwakabh/bennu-official/commit/189bc3d2e247560c9bda2350385e44425a1feb6b))
* **ci:** updated regexp in config. ([cd43a75](https://github.com/hwakabh/bennu-official/commit/cd43a75ee240d9f04596904e62183d572299ff2d))

## [0.6.0](https://github.com/hwakabh/bennu-official/compare/v0.5.0...v0.6.0) (2024-02-03)


### Features

* **ci:** added retention policies for GHCR. ([21aa6fe](https://github.com/hwakabh/bennu-official/commit/21aa6fe8ebb82f1966ade27c3358fb5a94791024))


### Bug Fixes

* **ci:** updated timezone and added workflow_dispatch for debug. ([23ae5f8](https://github.com/hwakabh/bennu-official/commit/23ae5f8f3b5c6d64c75d60971206646fc1e3fb71))

## [0.5.0](https://github.com/hwakabh/bennu-official/compare/v0.4.0...v0.5.0) (2024-02-01)


### Features

* added RWX volumes using nfs-server instead of MinIO. ([780d93a](https://github.com/hwakabh/bennu-official/commit/780d93af1f45e695d5d1279044bfb52728eb53cd))
* **compose:** added local MinIO with bitnami/minio image. ([c0f8b32](https://github.com/hwakabh/bennu-official/commit/c0f8b32a0e4dce99f7711338e21733d425cb920c))
* **deploy:** added installer manifests of ingress-nginx-controller. ([9e67fc5](https://github.com/hwakabh/bennu-official/commit/9e67fc574cae88d9487595c58e5db3560f25d6e0))
* **deploy:** replaced shared volume with object storage. ([2f8989f](https://github.com/hwakabh/bennu-official/commit/2f8989f31514a34440e7366b068fd170fdceecdb))
* **deploy:** replaced with statefulset for MySQL/MinIO. ([f4bc591](https://github.com/hwakabh/bennu-official/commit/f4bc59196f0dc34967411963cd38651bffb43295))


### Bug Fixes

* **ci:** added envars of MinIO for runnings tests. ([2c0c72b](https://github.com/hwakabh/bennu-official/commit/2c0c72b7c34b18bd1acf123e24f11df250144345))
* **ci:** enabled STATIC_URL for test CI. ([c254560](https://github.com/hwakabh/bennu-official/commit/c254560530d834d397de0e42571a3decc20ff647))
* **ci:** replaced minio image from official to bitnami. ([8ebd917](https://github.com/hwakabh/bennu-official/commit/8ebd917927102afc4f9c47583d3b1c477186e692))
* **deploy:** fixed collectstatic configurations. ([c805875](https://github.com/hwakabh/bennu-official/commit/c805875d2a7b307933bb6ddd2ae320fb42289687))
* **deploy:** updated nginx config and manifests. ([984384f](https://github.com/hwakabh/bennu-official/commit/984384f78d0548e12e9a109cc90123a0ea5f288e))
* **security:** moved secret as github env. ([23498f4](https://github.com/hwakabh/bennu-official/commit/23498f43321e46d867c3bc1177625dd55a11bca5))


### Performance Improvements

* added ingress and scaled out backend nginx pods. ([2ce6d18](https://github.com/hwakabh/bennu-official/commit/2ce6d185ccf52abb97fafe1bba0b48e316b17e6d))
* commented out annotations as external load balancer. ([8342017](https://github.com/hwakabh/bennu-official/commit/8342017ad9d2dc2119075b9ea846aeb72d7e8068))
* commented out annotations as external load balancer. ([742c067](https://github.com/hwakabh/bennu-official/commit/742c067b13bd063f7a709cf3c714c5aef9a57640))
* scaled deployment/django and notes as nginx-controller. ([cb56c48](https://github.com/hwakabh/bennu-official/commit/cb56c48688a414bada569fe0792497155591a936))

## [0.4.0](https://github.com/hwakabh/bennu-official/compare/v0.3.0...v0.4.0) (2024-01-28)


### Features

* **deploy:** implemented bitnami/nginx for serve staticfiles, instead of whitenoise. ([c552873](https://github.com/hwakabh/bennu-official/commit/c5528731429910b1e244626f7c9906a272a389ea))


### Bug Fixes

* **ci:** service name same as compose.yaml. ([450f297](https://github.com/hwakabh/bennu-official/commit/450f2973419a29f177f117a3949d54981dfc7bdf))
* **deploy:** volume mounts with nginx. ([964caba](https://github.com/hwakabh/bennu-official/commit/964caba7a0e48079e34c53fde30bbf32b80b6409))

## [0.3.0](https://github.com/hwakabh/bennu-official/compare/v0.2.1...v0.3.0) (2024-01-17)


### Features

* updated LiveSchedules models with adding packages. ([cf61df4](https://github.com/hwakabh/bennu-official/commit/cf61df47acc4280a26797318467a0197f8feafc1))


### Bug Fixes

* **ui:** adjusted live information. ([e862625](https://github.com/hwakabh/bennu-official/commit/e8626252d2779d8ca22f115daddab368fa0e60e7))


### Performance Improvements

* changed worker_class to gthread from sync, default. ([89cd7c6](https://github.com/hwakabh/bennu-official/commit/89cd7c6f11dc99254d0906bb856f15e532e0a21e))

## [0.2.1](https://github.com/hwakabh/bennu-official/compare/v0.2.0...v0.2.1) (2024-01-15)


### Bug Fixes

* added namespace by app_name in urls.py. ([83b3a0d](https://github.com/hwakabh/bennu-official/commit/83b3a0d1bbfcb95280794384529f13e561d84620))
* **ui:** added jQuery snippets for make active list dynamic. ([3690a00](https://github.com/hwakabh/bennu-official/commit/3690a0079e7aab16d41386a18bc569503aaec168))
* **urls:** fixed typo in function name. ([9d69a85](https://github.com/hwakabh/bennu-official/commit/9d69a8520ecb9f03e0b6fe491e492e28756660c1))

## [0.2.0](https://github.com/hwakabh/bennu-official/compare/v0.1.1...v0.2.0) (2024-01-12)


### Features

* added /healthz with class-based view. ([228c80f](https://github.com/hwakabh/bennu-official/commit/228c80f419e6f3f1ec9bafe3a8949af00c37241a))
* added readiness probes for healthz. ([b4b754a](https://github.com/hwakabh/bennu-official/commit/b4b754a482af1eae7d34d936b42236627aa59f31))


### Performance Improvements

* updated gunicorn config. ([d99451a](https://github.com/hwakabh/bennu-official/commit/d99451ada650e79e643fce8a59601f22afaf2945))


### Reverts

* removed draft drawio files. ([a7fd404](https://github.com/hwakabh/bennu-official/commit/a7fd4046a97c13d0abd20b4792358d4da165a2a5))


### Documentation

* added drawio as .svg and linked from README. ([6a133fd](https://github.com/hwakabh/bennu-official/commit/6a133fdfcfe2ae4422af84d2fcdb70b7725b28e0))

## [0.1.1](https://github.com/hwakabh/bennu-official/compare/v0.1.0...v0.1.1) (2024-01-10)


### Bug Fixes

* **deploy:** updated orders of middleware for whitenoise. ([89f9839](https://github.com/hwakabh/bennu-official/commit/89f983934f3bf6cf8458695ca99602e44e7434f8))
* **deploy:** updated start process and tests with debug logs. ([78bc2c7](https://github.com/hwakabh/bennu-official/commit/78bc2c7c8ffc136fecbcc03b3c2acaea2bf9f1ff))

## [0.1.0](https://github.com/hwakabh/bennu-official/compare/v0.0.2...v0.1.0) (2024-01-09)


### Features

* **templates:** added sorry page. ([7655b21](https://github.com/hwakabh/bennu-official/commit/7655b2132ba51fa6bb1159abe06ba3a64da71484))


### Bug Fixes

* **ci:** removed unexpected inputs. ([039cc51](https://github.com/hwakabh/bennu-official/commit/039cc51f936d54572e690f07a41e9436837427ba))
