# Re-parameterizing workflows with `params` and config files

Spend a minute or two familiarizing yourself with `greet.py`. The script simply writes the given greeting to the given name the given number of times to the specified output file. 

This script might be analogous to a pieces of analyses we often do in research. We want to apply a given algorithm to a given dataset and repeat the experiment a given number of times. We then want to save the results to disk.

As great as wildcards are, sometimes, wildcards can become cumbersome and hard to understand; we can't rely on file names for the parameterization of all experiments. Instead, we can use **configuration files** with snakemake split the parameterization of workflows between filenames and a 'config file' that can be versioned (say with Git etc.).

Try running:

	$ snakemake all --configfile configs/en_william.yml

What did it do? How many times did `hello william` get written to disk?

You will see that when a configuration file is passed with the `--configfile` flag, the specified dictionary (in YAML) format, can be accessed in the during Snakemake's execution in the global `config` "python" dictionary.

Moreover, instead of using wildcards, we use the `params` keyword in the rule to specify the parameters in `shell`. 

Try running the workflow with `es_william.yml`. Also try to write your own configuration file.

## Some use cases where configs and params are useful
- Config files can be used to determine search spaces for hyperparameters
- Config files can be used to parameterize/pass long input file paths to the workflow

## Word of warning
Configuration files decouple parameterization in your workflow with the filenames of inputs and outputs. This can be useful when the parameterizations are cumbersome. However, this decoupling must also be done with caution. When a part of the parameterization of your workflow is in a config file not managed by the Snakemake input-output-wildcards paradigm, the same rule with different configuration files can produce the same file (outputs) with different content. This means that as a user, you have to be careful to either track, or make it easy to determine which configurations produced which outputs.