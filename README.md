# Best pratcices for reproducible research with (Snakemake)

## Requirements
This repo containes tutorials that require [miniconda](https://docs.conda.io/en/latest/miniconda.html) and  [Snakemake](https://snakemake.readthedocs.io/en/stable/). Setup the conda environment for this tutorial with:

    conda env create -f environment.yml

Activate the environment with:

    source activate snakemake-tutorial

## Tutorials
Go through these tutorials to learn about Snakemake (and a bit of conda)!

0. Setup - good patterns and anti-patterns with Conda
1. Hello world with snakemake
2. Inputs, outputs and dependencies with snakemake
3. Introduction to wildcards
4. Configuration files and `params` for even better parameterization of workflows
5. Final thoughts, additional tips and tricks

## An opportunity to practice with Git/Github
Once you are done with the tutorials, you can get some practice with Git and Github and do the following:
1. Fork this repository
2. Create a Pull-Request that adds the following features:
    - Add a language to `3_wildcards/greet.py`
    - Add a langauge to the files generated in `3_wildcards` by change line 6 in the `Snakefile`
    - Add a configuration file to say hello in `4_configs-and-params`!
3. Submit the Pull-Request and get someone to review it :)

## Resources
- Git and Github, ([git handbook](https://guides.github.com/introduction/git-handbook/))
- [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html) documentation
- [Snakemake FAQ](https://snakemake.readthedocs.io/en/stable/project_info/faq.html)
- [Conda cheatsheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Understanding Conda and Pip](https://www.anaconda.com/understanding-conda-and-pip/)
- [Pull Requests and forks](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/)