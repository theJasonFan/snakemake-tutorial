Snakemake is a tool that allows you to specify how scripts and tools should be run.

The following rule named *echo*. Will run the the commands specified under *shell*, a keyword.

Here is a snippet of a rule where a local variable is declared, and a rule is defined to simply `echo` the message onto standard output.

``` Python
  
msg =  'hello world'
rule echo:
	shell:
		'''
		echo {msg} from echo!
		'''
```

In this directory, try running:
	
	$ Snakemake

Then try:

	$ Snakemake echo

You will see that the results are the same. Snakemake runs the rules defined by the `Snakefile` in the current directory. With `Snakemake {rule}` you ask Snakemake to run the named rule. If no rule is supplied, Snakemake runs the first rule in the specified `Snakefile`.

What will the following command do?

	$ Snakemake py_hello