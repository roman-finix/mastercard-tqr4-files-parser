Preparation:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy
python3 -m pip install pandas
```
usage:
```
# find . -iname "YTF*" -exec cat {} > all.positional \;
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-fwf-reader

$ python3 main.py YTF.AR.TQR6.S.E0098531.D240321.T182740.A001.positional
```
