from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib

def select(sql, filename='SDSSobjects.csv'):
    """
    Executes an SDSS database query and stores the result in a csv file.

    Parameters
    ----------
    sql: string
        SQL query statement
    filename: string
        desired name of output csv file

    Notes
    -----
    Uses `astroquery` to query the SDSS database. Read more at https://astroquery.readthedocs.io
    """
    from astroquery.sdss import SDSS as now
    sdssdata = now.query_sql(sql)
    # sdssdata is a Table object that can be saved in a csv file with:
    from astropy.io import ascii
    ascii.write(sdssdata, filename, format='csv', fast_writer=False)
    print('SDSS data downloaded and written to '+filename)
    # Return a dataframe to the command line as well.
    return pd.read_csv(filename)

""" Old mechanize code:
def select(sql):
    from StringIO import StringIO # To read a string like a file
    import mechanize
    url = "http://skyserver.sdss3.org/dr12/en/tools/search/sql.aspx"
    br = mechanize.Browser()
    br.open(url)
    br.select_form(name="sql")
    br['cmd'] = sql
    br['format']=['csv']
    response = br.submit()
    file_like = StringIO(response.get_data())
    return pd.read_csv(file_like,  skiprows=1)
"""

def plot_everything(data, colorizer='size', limits=(0.0, 10.0)):
    # Get ready to plot:
    pd.set_option('display.max_columns', None)
    import seaborn as sns
    sns.set()
    # Set up a color map, limiting it to retain contrast between faint objects:
    norm = matplotlib.colors.Normalize(vmin=limits[0], vmax=limits[1])
    cmap = matplotlib.cm.jet
    m = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
    # Plot everything:
    plot = pd.scatter_matrix(data, alpha=0.2, figsize=[15,15], c=m.to_rgba(data[colorizer]))
    return
