# Setup - good patterns and anti-patterns with Conda

## Why Conda?

I recommend using Conda and not PIP.

> Conda is an open source **package management** system and **environment** management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.
> (From: https://docs.conda.io/projects/conda/en/latest/)

We want to use Conda (over say `pip`) because the following reasons:

1. We want to isolate packages and requirements between different projects. Conda environments allow us to do this.
2. Explicitly isolating and specifying packages with Conda, we ensure that our research can be easily shared and reproduced
3. Conda manages *python itself*. (Managing projects that need different python versions would otherwise be difficult)

4. Conda can manage other packages such as R, and other binaries/tools/langauges (e.g. `gcc', C libraries etc.) required for a project

## 0. Install Miniconda

Install Python 3.7 version of Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html). Simply download the `.sh` script and run:

	sh Miniconda3-latest-Linux-x86_64.sh

### Tips for installing Conda on a cluster

We want to install Conda somewhere where we have lots of drive space. This is because for each Conda environment you create, Conda will create a directory containing the required packages; this might take up lots of space.

 When the Conda installation script prompts for a installation location. Enter an absolute path to a directory that you own, in a location in which you have lots of drive space. (e.g. `{absolute_path_to_lots_of_space}/miniconda3`). Note that you need to name the folder (ideally: `miniconda3`) that you will install Conda to.

Once Conda has been installed check that Conda was installed where you intended with:

	$ which conda
	> {absolute_path_to_lots_of_space}/miniconda3/bin/conda
	$ echo $CONDA_PREFIX
	> {absolute_path_to_lots_of_space}

## 0. Always use an environment
You want to isolate packages and dependencies between the projects you work on. *Always use a conda environment* - never just use the `base` environment.

## 1. Always use environment files
You will read in the conda documentation that you can create a conda environment with:
	
	conda create -n new-environment

And once you activate the environment, many packages (e.g. Snakemake) with documentation will recommend that you install said package with using the commands:
	
	pip install snakemake
 
 or

	conda install snakemake
\
But *these are anti-patterns* - a couple months down the line, how will you know which packages you installed? how will you know which versions of these packages you have updated or changed?

*The solution to mitigate these problems is to always use environment (YAML) files to create and update your environments.* You can read about the environment files [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually). An annotated environment file can be found at the root level of this repo.

### To create an environment use
	conda env create -f {environment YAML file}

### To add or update a package
*Always specify the primary version number of the packages you desire. This avoids breaking changes!* To add a package, or update a package, edit your environment file. And add or change a corresponding line like the following:
```YAML
	# env.yml
	name: my-env
	...
	dependencies:
	  - python=3.7 # Always specify a python version
	  - ...
	  - new_package=8.* # New package with version 8+!
```

Then run:
    conda env update -f {environment YAML file}

## 2. Always manage the python version.
*Always manage version of python you are trying to do/distribute your research with*. Otherwise, conda will just copy the python environment of the 'current' python interpreter in your shell.

## TL;DR:
1. Use Conda
2. Always use environment files and use `conda env {update, create} -f ...`.
3. Never use `conda create -n ...` or `conda install ...`
4. Always manage your python version.