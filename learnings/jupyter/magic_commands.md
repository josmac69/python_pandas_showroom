# Jupyter Notebook Magic Commands

* Jupyter Notebook has many built-in "magic commands" that provide useful functionality to enhance your workflow.
* Magic commands are prefixed with a percent sign % for line magics or %% for cell magics.

#### Here's a list of some of the most important and frequently used magic commands:

* %run: Runs a Python script as a program, with command-line arguments passed as arguments. `%run script.py arg1 arg2`
* %load: Loads the contents of a file into a code cell. `%load path/to/your/script.py`
* %pwd: Prints the current working directory.
* %cd: Changes the current working directory. `%cd path/to/your/directory`
* %ls: Lists the contents of the current directory.
* %history: Shows the command history.
* %reset: Resets the namespace by removing all names defined by the user.
* %who: Lists all variables in the namespace.
* %whos: Provides more information about all variables in the namespace.
* %time: Times the execution of a single statement. `%time my_function()`
* %timeit: Measures the execution time of a statement or expression using multiple runs, providing an average time. `%timeit my_function()`
* %%time: Times the execution of a cell (cell magic version of %time).
* %%timeit: Measures the execution time of a cell using multiple runs, providing an average time (cell magic version of %timeit).
* %matplotlib inline: Configures the integration of Matplotlib with Jupyter Notebook to display plots inline.
* %config: Configure settings of various aspects of the Jupyter Notebook, such as InlineBackend for %matplotlib inline. `%config InlineBackend.figure_format = 'retina'`
* %debug: Activates the interactive debugger.

These magic commands can help you streamline your work in Jupyter Notebook. You can also find more magic commands and their documentation by running %lsmagic in a code cell, which lists all available magics, or by referring to the official IPython documentation: https://ipython.readthedocs.io/en/stable/interactive/magics.html
