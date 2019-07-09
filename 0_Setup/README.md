# Setup - good patterns and anti-patterns with Conda

## Why Conda?
I recommend using Conda and not PIP.

> Conda is an open source **package management** system and **environment** management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.
> (From: https://docs.conda.io/projects/conda/en/latest/)

We want to use Conda (over say `pip`) because the following reasons:
1. We want to isolate packages and requirements between different projects. Conda environments allow us to do this.
2. Explicitly isolating and specifying packages with Conda, we ensure that our research can be easily shared and reproduced
3. Conda manages *python itself*. (Managing projects that need different python versions would otherwise be difficult)
4. Conda can manage other packages such as `R`, and other binaries/tools/langauges (e.g. `gcc', C libraries etc.) required for a project

## 0. Install Miniconda
Install Python 3.7 version of Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html). Simply download