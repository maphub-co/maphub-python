# maphub-client

## Local testing
1. Make changes to the code.
2. Install package locally for testing:
```sh
pip install -e .
```

## Deploying package
1. Make changes to the code.
2. Adjust version in
   - `pyproject.toml`
3. Deploy package:
```sh
python -m build               # Build package
python -m twine upload dist/* # Deploy package to PyPi
rm -R ./dist                  # Delete local build files
```