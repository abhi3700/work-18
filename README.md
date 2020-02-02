# work-18
Bias monitor

## Installation
* Just install the executable file.

### Packages
* `pandas`: 1.0.0
* `retrying`: 1.3.3
* `plotly`: 4.3.0
* `tkinter`: 1.3.2

## Input
* The input file has to be downloaded from DMIS.

## Output
* The output is a "CD Monitor" which has 2 main charts - __ISO__ & __DENSE__.

## Coding
### A. Data Wrangling
* Here, the file extension doesn't match with its data type inside.
* So, pandas' `read_html()` function gives the output in list of HTML tables i.e. 
```
[         Lot ID        lot ID     ...       BIAS  DOSE_VALUE
0  F18370001.F1  F18370001.F1     ...       76.2        18.2
1  F18370001.F1  F18370001.F1     ...      251.2        18.2
2  F18370001.F1  F18370001.F1     ...      252.1        18.2
3  F18370001.F1  F18370001.F1     ...       74.1        18.2
4  F18370001.F1  F18370001.F1     ...      249.1        18.2
5  F18370001.F1  F18370001.F1     ...       76.3        18.2

[6 rows x 12 columns]]
```
* the dataframe will be the 1st element in this list.
* Now, ensure the DICD & FICD's respective columns (lotid, waferid) match. Otherwise, it will give the error.
	- (`DICD_lotid` == `FICD-lotid`) 
	- (`DICD_waferid` == `FICD_waferid`) 
* Then proceed with column filtering.

### B. Data Visualization
* There are 2 main charts - __ISO__, __DENSE__.
* Each chart has 3 traces - __DICD__, __FICD__, __Bias__.
* The charts opens in default browser.

