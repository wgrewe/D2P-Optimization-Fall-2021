# The Circuit Less Travelled: A Path of Gentrification Through Colorado Neighborhoods

### Introduction
Large so-called superstar cities are often afflicted with gentrification due to an influx of new wealth moving into the city. For the Fall 2021 Data to Policy Symposium at the Auraria Library we analyze gentrification in the City of Denver over the last 15 years. One issue with studying gentrification is that snapshots of the distribution of wealth are only available on large time scales. This can make studying small changes difficult. To remedy this problem, we construct circuit walks between time-dependent clusterings of Denver neighborhoods for 3 different time instances.

### Resources
For this project, we pulled data on Denver neighborhoods from the [American Community Surveys (ACS)](https://github.com/wgrewe/D2P-Optimization-Fall-2021/tree/main/Data) for the City of Denver. The ACS contains a five year average of information collected about Denver including information about race, income, and education level. For this project, we use the ACS averages for 2006-2010, 2010-2014, 2015-2019.

For plotting purposes, we also make use of the [Denver Statistical Neighborhoods shapefile.](https://github.com/wgrewe/D2P-Optimization-Fall-2021/tree/main/Data)

### Data Clensing
In the [data cleaning notebook](https://github.com/wgrewe/D2P-Optimization-Fall-2021/blob/main/Data/Survey%20Data%20Cleaning.ipynb) we remove the columns from the ACS data sets that we do not care about for this analysis. Additionally, some fixing of names is required so that naming conventions are consistent across all ACS datasets.

After cleaning the data, K-Means Clustering is used to group neighborhoods with similar level of privilege (here, privilege is measured as blend of race, income, and education). The clusterings found give start and end points to the circuit walks we construct. 

Cleaned and clustered data is exported and located in the [Data folder](https://github.com/wgrewe/D2P-Optimization-Fall-2021/tree/main/Data) for access without running the Jupyter Notebook.

### Circuit Walk
Transitions from one clustering to another can be described through circuit walks. We construct walks from the clusterings for the 2006-2010, 2010-2014, 2015-2019 data sets. This process is involved and the tools used can be found in the [Circuit-Functions folder](https://github.com/wgrewe/D2P-Optimization-Fall-2021/tree/main/Circuit-Functions).

### Results
After running the main for the circuit walk functions, the circuits used are exported to [Circuit-Functions folder](https://github.com/wgrewe/D2P-Optimization-Fall-2021/tree/main/Circuit-Functions. A visual representation can be found in the [Circuit Walks notebook](https://github.com/wgrewe/D2P-Optimization-Fall-2021/blob/main/Circuit%20Walks.ipynb). This project included presentations during class and at the Data to Policy Symposium. Check out our [Data to Policy Slides](https://github.com/wgrewe/D2P-Optimization-Fall-2021/blob/main/Presentations/The%20Circuit%20Less%20Travelled_%20A%20Path%20of%20Gentrification%20Through%20Colorado%20Neighborhoods%20D2P.pptx) and [Data to Policy recording: ADD LINK!!!](https://github.com/wgrewe/D2P-Optimization-Fall-2021/). For the more mathematically interested, check our [class presentation slide deck](https://github.com/wgrewe/D2P-Optimization-Fall-2021/blob/main/Presentations/The%20Circuit%20Less%20Travelled_%20A%20Path%20of%20Gentrification%20Through%20Colorado%20Neighborhoods%20Final%20Presentation.pptx).
