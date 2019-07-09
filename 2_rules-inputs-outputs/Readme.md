# Intro to inputs and outputs

From the Snakemake docs:

> Snakemake workflows are essentially Python scripts extended by declarative code to define  **rules**. Rules describe how to create  **output files**  from  **input files**.

> -   Similar to GNU Make, you specify targets in terms of a pseudo-rule at the top.
> -   For each target and intermediate file, you create rules that define how they are created from input files.
> -   **Snakemake determines the rule dependencies by matching file names**.
> -   Rules can either use shell commands, plain Python code or external Python or R scripts to create output files from input files.

In the `Snakefile`:
- Running `snakemake all` will produce files required as **input** to the rule `all`
- The rule `all` requires **inputs** `hello.txt` and `goodbye.txt` which are produced by the rules `goodbye` and `hello`.

What would `snakemake all` do?:

Try running:

	$ snakemake all

Did it produce the files you expected?

Now try uncommenting line 14. What new dependencies did you just add to the workflow?

Try running:

	$ snakemake all -n

The `-n` flag makes snakemake do a 'dry-run' and it simply mocks up and simulates running the workflow. Inspect the output of what you just ran. What does the rules `all` and `complicated` now depend on?

Try running:

	$ snakemake all 

Did it produce the new file you expected?