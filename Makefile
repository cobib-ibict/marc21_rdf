pre-commit-install-hooks:
	pre-commit uninstall
	pre-commit install --install-hooks
	pre-commit install --hook-type pre-push

pre-commit-uninstall-hooks:
	pre-commit uninstall

test:
	pytest -v -x
