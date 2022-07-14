"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
    dat_file='2002FemResp.dat.gz',
    nrows=None
):
    """
    Reads the NSFG *respondent* data
    
    @params `dct_file`: strata dict string file name
    @params `dat_file`: string file name
    @returns `DataFrame` 
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    pass

def ValidatePregnum(resp):

    """
    Read preg dataframe
    @returns preg df
    """
    preg = nsfg.ReadFemPreg()
    # print(preg.head()) - first 5 rows of pregnancy dataframe

    # Map caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    # print(type(preg_map)) - default dict mapping of {caseid: [idx]} 

    # iterate through the respondent `pregnum` series
    for idx, pregnum in resp.pregnum.items():
        caseid = resp.caseid[idx]
        


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = ReadFemResp()
    ValidatePregnum(resp)

    # print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
