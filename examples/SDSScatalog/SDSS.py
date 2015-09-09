import pandas as pd

def select(sql):
    from StringIO import StringIO # To read a string like a file
    import mechanize
    url = "http://skyserver.sdss3.org/dr10/en/tools/search/sql.aspx"
    br = mechanize.Browser()
    br.open(url)
    br.select_form(name="sql")
    br['cmd'] = sql
    br['format']=['csv']
    response = br.submit()
    file_like = StringIO(response.get_data())
    return pd.read_csv(file_like,  skiprows=1)
