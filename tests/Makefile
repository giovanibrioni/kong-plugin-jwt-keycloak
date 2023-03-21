INTE_TEST_IMAGE:=jwt-keycloak-inte-test-image

_build-inte-test-image:
	@echo "Building integration test image ..."
	@docker build -q -t ${INTE_TEST_IMAGE} -f integration_tests/Dockerfile ..

_tests-integration: _build-inte-test-image
	@docker run -it --rm --net=host -v ${PWD}/integration_tests/tests:/tests:ro ${INTE_TEST_IMAGE} python -m unittest discover -s /tests -t /tests -p *.py -v