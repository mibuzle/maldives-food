# Import libraries

import numpy as np
import pandas as pd

#load in hhlevel dataset
df=pd.read_excel(Non-Raised_hhlevel.xlsx)

# remove unwanted columns
imp=['uqhh__id','hh_build_ownshp','housing_loans','otlnyn',''psu','hh_rented','hh_disaster__1','hh_disaster__2','hh_disaster__3','hh_disaster__4','hh_disaster__5','hh_disaster__n96']
newdf=df[imp].copy()

#rename columns
dff=newdf.set_axis(['hhid','dwellingownrship','housingloan','othrloan','psu','rented','hh_disaster1','disaster2','disaster3','disaster4','disaster5','disaster6'),axis=1]
],axis=1)

#destring the dwelling ownership variable (by mapping)
dff['dwellingownrship'] = dff['dwellingownrship'].map({'Owned by a member of this HH/own place': 0, 'Other':1, 'Owned by a relative not living in this household':1, 'Arranged by the employer':1})

#turning string variables into binaries
df['rented'] = df['rented'].isin(["Yes"]).map({True: 0, False: 1})

#combining disasters into one column and turning it into a binary
df['disaster'] = df['d1'] + df['d2'] + df['d3'] + df['d4'] + df['d5'] + df['d6']
df['disaster'] = df['disaster'].isin([0]).map({True: 0, False: 1})

#dropping old variables for disaster
to_drop = ['d1','d2','d3','d4','d5','d6']
df = df.drop(to_drop,axis=1)

Load in the usual members dataset
df=pd.read_excel('file_location.xlsx')

