# Show room demonstating usage of Python Pandas for data analysis

### Overview

* I used Pandas a lot for data analysis but those scripts have been created for specific use cases for specific companies and their data so I cannot reference them. Therefore I created this "show room" demonstrating usage of pandas and related library.
* I also used this oportunity to test programming with ChatGPT, ChatSonic and Github Copilot AIs. My experiences with these tools are generally very positive but it is necessary to ask properly formulated questions and also understand the code and do proper testing.

### Environment

* All databases and python examples run in docker containers.
* All operations are done using `make` command
  * build image with required python libraries
  * code linting using pylint
  * run python image
  * run databases
  * stop and remove all containers

### Usage

* All examples use one common image `python_pandas_showroom`
* build image using `make build`
* run exapmle script using `make run-python SCRIPT=pandas_matplotlib_graphs` or other directory name
  * directories with examples start with `pandas_` prefix and contain script.py file, short README and 2 files used by pylint
* to test PostgreSQL related examples you need first to build PostgreSQL `adventureworks` image from the repository https://github.com/josmac69/postgresDBSamples
* Start postgresql image from this pandas repository using `make run-postgresql`
  * it will start image with proper network so python containers can address it
  * login credentials into image are in the directory `secrets` in this repo - directory is mapped to the container
* Each python container runs in terminal interactive mode and exists at the end.
* To test changes in `script.py` you simply run image again - script is NOT included in image, directory is mapped inside the container
* When you are done with tests you can delete created pandas image using `make delete-pandas-images`

### Data sources

For this show room I use different data sources:

* example PostgreSQL databases from repository - https://github.com/josmac69/postgresDBSamples
* sample data from internet:
  * [Yahoo finance AAPL data](https://finance.yahoo.com/quote/AAPL/history?p=AAPL)
  * [NASA json data](https://data.nasa.gov/data.json)
  * [Pandas sample student DataFrame](https://www.plus2net.com/python/pandas-student.php)
  * [Kaggle datasets](https://www.kaggle.com/datasets):
    * [Titanic dataset](https://www.kaggle.com/datasets/vinicius150987/titanic3)
    * [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
  * 

### Learning resources

* [Pandas cheat sheet: Top 35 commands and operations](https://www.educative.io/blog/pandas-cheat-sheet)
* 

### Covered use cases

ChatSonic:

Great question! Here are some use cases for the Pandas library that are must-haves for demonstrating its capabilities:

1. Data Wrangling: Pandas provides a powerful set of tools for cleaning, transforming, and merging datasets. This is a must-have use case to demonstrate how to handle missing data, remove duplicates, and merge datasets.
2. Data Visualization: Pandas integrates seamlessly with the Matplotlib library to create a wide range of visualizations, including line charts, bar charts, histograms, and scatter plots. This is a must-have use case to demonstrate how to create visualizations from Pandas data.
3. Time Series Analysis: Pandas provides robust support for time series data, including resampling, shifting, and rolling window calculations. This is a must-have use case to demonstrate how to work with time series data in Pandas.
4. Machine Learning: Pandas provides support for many machine learning algorithms, including regression, classification, and clustering. This is a must-have use case to demonstrate how to use Pandas data for machine learning tasks.
5. Financial Analysis: Pandas was originally developed for financial analysis, and it provides support for many financial calculations, including moving averages, volatility, and returns. This is a must-have use case to demonstrate how to use Pandas data for financial analysis.

These are just a few examples of the many use cases for Pandas. By demonstrating these must-haves, you can showcase the full capabilities of the library and provide a solid foundation for further exploration and experimentation.

---

ChatGPT:

Here are some "must-have" use cases for a GitHub repository demonstrating the use of pandas:

1. Reading and writing data to/from various file formats (CSV, Excel, SQL databases, JSON, etc.)
2. Data cleaning and preprocessing (e.g., removing duplicates, handling missing values, data type conversion)
3. Basic data analysis (e.g., summary statistics, exploring relationships between variables)
4. Data manipulation (e.g., filtering, sorting, merging/joining, grouping/aggregating)
5. Data visualization (e.g., basic charts and graphs, histograms, scatterplots, etc.)
6. Time series analysis (e.g., handling dates and times, resampling, rolling windows)
7. Handling large datasets (e.g., chunking, parallelization, using Dask or other distributed computing frameworks)

Of course, there are many other use cases that could be included, depending on the specific goals of your repository and your intended audience.
