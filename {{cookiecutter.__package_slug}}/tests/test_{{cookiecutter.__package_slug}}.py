from {{cookiecutter.__package_slug}} import __version__


def test_version():
	assert __version__ == "{{cookiecutter.package_version}}"
