install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

build:
	poetry build

package-install:
	pip install --user dist/*.whl

package-uninstall:
	pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 brain_games
