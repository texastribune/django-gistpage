PROJECT=./example_project

help:
	@echo "make commands:"
	@echo "  make help    - this help"
	@echo "  make test    - run test suite"
	@echo "  make resetdb - drop and recreate the database"


test:
#
#   -s    don't capture stdout
#
	python $(PROJECT)/manage.py test -s


clean:
	find -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info


resetdb:
	python $(PROJECT)/manage.py reset_db --router=default --noinput
	python $(PROJECT)/manage.py syncdb --noinput


.PHONY: help test clean resetdb
