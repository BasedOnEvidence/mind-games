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

brain-prime:
	poetry run brain-prime

build:
	poetry build

package-install:
	pip install --user dist/*.whl

package-uninstall-0.1.0:
	pip uninstall dist/mrhex_brain_games-0.1.0-py3-none-any.whl

package-uninstall-1.0.0:
	pip uninstall dist/mrhex_brain_games-1.0.0-py3-none-any.whl

package-uninstall-1.0.1:
	pip uninstall dist/mrhex_brain_games-1.0.1-py3-none-any.whl

lint:
	poetry run flake8 brain_games
