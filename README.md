# CAPIR Transfronteriza2 2023
Data analysis of anti-rights groups from Brazil, Ecuador, Colombia and Honduras.

Created by: Fer Aguirre

---
## Directory Structure
```
|- .gitignore              # Customized .gitignore for python projects
|- LICENSE                 # Project's license
|- README.md               # Top-level README for this project
|
|- assets                  # Resources for the project
|
|- data                    # Categorized data files                      
|  |- processed            # Cleaned data
|  |- raw                  # Original data
|
|- docs                    # Explanatory materials
|  |- references           # Papers, manuals, articles, etc.
|  |- data-dictionary.md   # Information about the data
|
|- notebooks               # Jupyter notebooks
|  |- 0.0-process.ipynb    # Data processing (fixing column types, data cleansing, etc.)
|  |- 1.0-analyze.ipynb    # Exploratory data analysis
|  |- 2.0-visualize.ipynb  # Data visualization methods
|
|- outputs                 # Exports generated by notebooks
|  |- tables               # Generated pivot tables to analyze data
|  |- figures              # Generated graphics, maps, etc. to be used in reporting
| 
|- project                 # Python package
|  |- __init__.py
|  |- data                 # Functions to manipulate data
|  |  |- load.py           # Module to load data
|  |  |- process.py        # Module to process data
|  |  |- analyze.py        # Module to analyze data
|  |  |- export.py         # Module to save exports
|  |  |- __init__.py 
|  |  
|  |- utils                # Functions to make common patterns shorter and easier
|     |- paths.py          # Module to generate relative paths
|     |- __init__.py
|
|- scripts                 # Python files
|
|- setup.py                # Import project as a python module
|
|- Pipfile                 # Project dependencies
```
---

## License

This project is released under [MIT License](/LICENSE).

---

This repository was generated with [cookiecutter](https://github.com/cookiecutter/cookiecutter).