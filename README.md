# maphub-client

## Build package
1. Make changes to the code.
2. Adjust version in
   - `src/__init__.py`
   - `setup.py`
3. Build package: `python -m build`
4. Deploy package: `python -m twine upload dist/*`
5. Clean dist folder: `rm -R ./dist`
