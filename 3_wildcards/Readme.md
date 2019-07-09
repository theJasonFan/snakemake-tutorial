# Intro to wildcards

# Fun with wildcards

Take a quick look at `greet.py`, this python script simply takes a language and greeting as input and outputs said greeting in said language to the specified output file. Fun.

Now, run,
	
	$ snakemake spanish_hello

and inspect the output in `output`. This should make sense for you if you have seen the previous tutorial. The specified rule  produces `L=es_G=hello.txt` and simply passes the required arguments via the `shell`.

Now, what if we want to produce more than just a spanish hello?

Obviously, the rule `spanish_hello` only works with the hard-coded output and parameters that we wrote and does not generalize. However, Snakemake allows to **generalize rules by using named wildcards**. 
- We create a new, general, `greet` rule, replacing `es` with `{language}` and `hello` with `{greeting}` in the output file name. The `{}` represents wildcard names that we can use later.
- In `shell:` we can then refer to the wildcards `language` and `greeting`.

Now, the rule `greet` will be able to produce a files with names that match the target (`output/L={language}_G={greeting}.txt`) specified in `output:`.

For example, try running the `french_goodbye` rule. This rule requires the file `output/L=fr_G=goodbye.txt`. Then, Snakemake determines that this rule can be applied to generate a target file by replacing the wildcards `{language}` and `{greeting}` in the output file with an appropriate value, it will propagate that value to all occurrences of these wildcards throughout the rule files and thereby determine the necessary input and shell commands for the resulting job. (Note that you can have multiple wildcards in your file paths, however, to avoid conflicts with other jobs of the same rule, **all output files** of a rule have to **contain exactly the same wildcards**.)

## Using `expand()`
Try running `snakemake all`. In the rule, you will see that instead of listing all combinations of languages and greetings, we instead pass the templated target to `expand(...)` and pass corresponding lists of values of wildcards as keyworded arguments (that match said wildcards). `expand(...)` produces all combinations of these lists.

Try replacing line 5 with an uncommented line 6. What would `snakemake all` now do?

## Acknowledgements
This was adapted from https://snakemake.readthedocs.io/en/stable/tutorial/basics.html?highlight=expand#step-2-generalizing-the-read-mapping-rule