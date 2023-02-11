import streamlit as st
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import numpy as np
import pandas as pd

cred = {'type': 'service_account',
 'project_id': 'etf-model-369713',
 'private_key_id': '45aad76af9ae8f68ff8868b177ade3106abbb6f0',
 'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0Sgnt59iKyLHQ\nZn7SowrdqUNOj+ColMW5ai1coBfFUTBb1dEhl0NAggJr8mSYvZW8PZy2rnknSgjI\ngLgyNfZSMPSLBw8Nzqzgd3v4GKPoErTZoJaZiht+WHvWkIpjDZbm3eGpf79onpVU\ncN+Ac1lRrQYD8k6qIa9aqnKm8Qqfe+ZUFForO94bBNa+4Dxd3B9iOlIasONTuZNI\ndEIeq0JFuY4oJYlNBWaiLAEfhqCRVnwL6cJUXPAU5goxAX/NKfzSVCL1mHAv03j7\npy/98EtxDXl3SFxMfqXwW7l2CgUOdUpU/Ctpkc3kua22zYA9/Q1sV737X8GgscQx\nRA2vhUQ/AgMBAAECggEABQCq7t2Iji1Mdc5qRXj9s7HfKr5mSvc510/Ba3kLv89l\nap7vuyFh3dfdrlYfAXf9QChrgUwtE3CD9uBPfCEwMQ6nsnXjLoxmEqJuH6+7WJSw\nTPueQitpYOOeqBEBrgbyAXz1pojjbEk+NoYdRYit2UzWRmTCVwkxPvBM1yIIG+29\nt56lSeo1lg8Ibui6mmZteQ2Q9u7GwbhPBJwgjzVwdwKFfxMdr7uuwnNuJRwAAoBt\n1M6ENoB1zUWeUStQlCgCR/xh8VbtwA5xe9p8nKOfwK2hesiskJrojTWXiszWaBu6\nHfAxHce+lSEacpBEI2FRWSiqxVgBlNmrgOu1C1DecQKBgQDsg2AEOH2xvVKSapyn\nwNazJVVxzuwuJYf8G9HQf2/ibHZrCL34Uo9o449NjS1o7FIyFP2rFcX2EwQTJUSg\nPbFVEjOc3X/xYO0ILrJ4bCN7vBFh0QrO/2Y/3XqbkQZGbosxmAsKEPCRA7spIMTk\nDcsGZTAYaI3EAVeoBlqK+1i7DwKBgQDDJMRBmP+0PzOj/oJLUlXk0I/YaaY0BQH5\nlnoogyW9rsABCp/W9wfD3fpxwOy7sQ/JHzSWXLD6L5NUVuSthNSXI8Xf4KX2Qhj5\nK4+lLj0YTfQdyP2FPNbqhtupWQfMSZmuo/swIa05GIEBgC7xaDrvPX3zs8sIaXhT\nsNSKO2aj0QKBgG1y/mP1oHU4H5YSMByRaMnOZRQdpb5VL/DDDv1le+lUOBigGwln\na2YmqJJC2tjLQ95ZSGp70PhnJGOXw4JECmRL4Aafmi2hpQ88TOrdYC5KgeC6VD4m\ngrLbU3naSwUc8t0odzNZU3pIN7x4paTDnUiAWxlwiOpDlMT068GVPyKRAoGBAIB/\nrmgPqplzYLrldcDJh9vzZjU4ZIQuo/bc1qa9zrfgt0zu9dqgu79v2nz3xvxeyd4path3cjfn\nQPSeNr+YImjQCycjp6WancrtL/u3zKAPCjjX+M0PT+dpGV/qDw9CHFUoVhU0helU\n+6vXESzesNxfHwpB+0TcdhrK0rBIWz6o21vm/5BxAoGASW1SzD/wYvaXqMzBNWWz\nxumt5MPEg6wJ1byc1w50UZJe0ie2sby9G8n1x3D32Q6ixsEXywBCqKn8fzAfGPE1\nnl1XOfAgXO8CpK/8ZA/HzRIbEXyH+ufvyS/pgPdBR31XkD+sX5h5fB6RnlolT/Ys\n5HZ6sPgD1hwK16wBxtXTNB0=\n-----END PRIVATE KEY-----\n',
 'client_email': 'etf-model-83@etf-model-369713.iam.gserviceaccount.com',
 'client_id': '104785831308812239864',
 'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
 'token_uri': 'https://oauth2.googleapis.com/token',
 'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
 'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/etf-model-83%40etf-model-369713.iam.gserviceaccount.com'}


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_info(cred, scopes=SCOPES)

STOCK_SHEET_ID = '13mS_ier4GgJiqbR0ak8lgV7lWaJyY7ItWUuJH-CyEQg'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=STOCK_SHEET_ID,
                            range='STOCK_DATA!A:ZZ').execute()
values = result.get('values',[]) 

STOCKS = pd.DataFrame(values)
new_header = STOCKS.iloc[0] 
STOCKS = STOCKS[1:] 
STOCKS.columns = new_header
STOCKS.reset_index(drop=True, inplace=True)
tickers = STOCKS['Ticker']
STOCKS[['Beta','Price','Change_1D','Return_1W','Return_1M',
      'Return_3M','Return_6M','Return_12M','PctRank_1W',
      'PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M',
      'ShortMoM_avg','MoM_avg','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M',
      'ChgRnk_12M','Fallin1Mmore20','Fallin1Wmore10','StdevNegativeReturn',
      'HistExcessReturn_1W','HistExcessReturn_1M','HistExcessReturn_3M',
      'HistExcessReturn_6M','HistExcessReturn_12M']] = STOCKS[['Beta','Price','Change_1D','Return_1W','Return_1M',
                                                             'Return_3M','Return_6M','Return_12M','PctRank_1W',
                                                             'PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M',
                                                             'ShortMoM_avg','MoM_avg','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M',
                                                             'ChgRnk_12M','Fallin1Mmore20','Fallin1Wmore10','StdevNegativeReturn',
                                                             'HistExcessReturn_1W','HistExcessReturn_1M','HistExcessReturn_3M',
                                                             'HistExcessReturn_6M','HistExcessReturn_12M']].astype(float)

STOCKS['Ticker_Index'] = STOCKS['Ticker']
STOCKS.set_index('Ticker_Index',inplace = True)


stock_dma  = STOCKS.loc[(STOCKS['50DMAModel'] == 'INVESTED') & (STOCKS['100DMAModel'] == 'INVESTED') & (STOCKS['200DMAModel'] == 'INVESTED')]
stock_tr_1 = STOCKS.loc[(STOCKS['200DMAModel'] == 'INVESTED') & (STOCKS['50DMAModel'] == 'CASH')]
stock_tr_2 = STOCKS.loc[(STOCKS['200DMAModel'] == 'CASH') & (STOCKS['50DMAModel'] == 'INVESTED') & (STOCKS['Fallin1Wmore10']<= 10)]
stock_ex_1 = STOCKS.loc[STOCKS['HistExcessReturn_12M']>=80]
stock_ex_2 = STOCKS.loc[(STOCKS['HistExcessReturn_12M']<=20) & (STOCKS['HistExcessReturn_12M'] != 0) ]
stock_vol  = STOCKS.loc[(STOCKS['HistExcessReturn_12M']<=30) & (STOCKS['Fallin1Wmore10'] >=15) & (STOCKS['HistExcessReturn_12M'] != 0)]
stock_ex50 = STOCKS.loc[(STOCKS['HistExcessReturn_12M']>=20) & (STOCKS['50DMAModel'] == 'CASH') & (STOCKS['100DMAModel'] == 'INVESTED') & (STOCKS['200DMAModel'] == 'INVESTED')]

st.header('ETF Frame Work')

with st.sidebar:

  category = st.multiselect('Category:',STOCKS['Category'].unique())
  stock = st.multiselect('STOCK Tickers:', STOCKS['Ticker'])
  

  if (category == []) and (stock == []):

    d_stock = STOCKS.loc[STOCKS['Ticker'] == 'SPY']

  elif (category == []) and (stock != []):

    d_stock = STOCKS.loc[STOCKS['Ticker'].isin(stock)]
    stock_dma = stock_dma.loc[stock_dma['Ticker'].isin(stock)]
    stock_tr_1 = stock_tr_1.loc[stock_tr_1['Ticker'].isin(stock)]
    stock_tr_2 = stock_tr_2.loc[stock_tr_2['Ticker'].isin(stock)]
    stock_ex_1 = stock_ex_1.loc[stock_ex_1['Ticker'].isin(stock)]
    stock_ex_2 = stock_ex_2.loc[stock_ex_2['Ticker'].isin(stock)]
    stock_vol = stock_vol.loc[stock_vol['Ticker'].isin(stock)]
    stock_ex50 = stock_ex50.loc[stock_ex50['Ticker'].isin(stock)]

  elif (category != []) and (stock == []):

    d_stock = STOCKS.loc[STOCKS['Category'].isin(category)]
    stock_dma = stock_dma.loc[stock_dma['Category'].isin(category)]
    stock_tr_1 = stock_tr_1.loc[stock_tr_1['Category'].isin(category)]
    stock_tr_2 = stock_tr_2.loc[stock_tr_2['Category'].isin(category)]
    stock_ex_1 = stock_ex_1.loc[stock_ex_1['Category'].isin(category)]
    stock_ex_2 = stock_ex_2.loc[stock_ex_2['Category'].isin(category)]
    stock_vol = stock_vol.loc[stock_vol['Category'].isin(category)]
    stock_ex50 = stock_ex50.loc[stock_ex50['Category'].isin(category)]

  else:

    d_stock = STOCKS.loc[(STOCKS['Ticker'].isin(stock)) & (STOCKS['Category'].isin(category))]
    stock_dma = stock_dma.loc[(stock_dma['Ticker'].isin(stock)) & (stock_dma['Category'].isin(category))]
    stock_tr_1 = stock_tr_1.loc[(stock_tr_1['Ticker'].isin(stock)) & (stock_tr_1['Category'].isin(category))]
    stock_tr_2 = stock_tr_2.loc[(stock_tr_2['Ticker'].isin(stock)) & (stock_tr_2['Category'].isin(category))]
    stock_ex_1 = stock_ex_1.loc[(stock_ex_1['Ticker'].isin(stock)) & (stock_ex_1['Category'].isin(category))]
    stock_ex_2 = stock_ex_2.loc[(stock_ex_2['Ticker'].isin(stock)) & (stock_ex_2['Category'].isin(category))]
    stock_vol = stock_vol.loc[(stock_vol['Ticker'].isin(stock)) & (stock_vol['Category'].isin(category))]
    stock_ex50 = stock_ex50.loc[(stock_ex50['Ticker'].isin(stock)) & (stock_ex50['Category'].isin(category))]
   

  st.dataframe(d_stock[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

  url = "https://drive.google.com/file/d/1JYrj4AGBOCW8GhcmOlHU1fqQFgg9lt-R/view?usp=sharing"

  st.write("Click on the link to view charts(%s) " % url)

  url2 = "https://docs.google.com/spreadsheets/d/13mS_ier4GgJiqbR0ak8lgV7lWaJyY7ItWUuJH-CyEQg/edit?usp=sharing"
  
  st.write("Click on the link to view database(%s) " % url2)

  url3 = "https://docs.google.com/spreadsheets/d/1Qc7bDn5_9EKY6vOTju2WRRbdOY44IY0AkiQYhNvfQ8I/edit?usp=share_link"  

  st.write("Link to US data for 30, 60 AND 200 DMA(%s) " % url3)

st.write('## STOCKS above 50,100,200 DMA')
st.dataframe(stock_dma[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('## Change in Trend')
st.write('### Above 200 DMA And Below 50 DMA')

st.dataframe(stock_tr_1[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('### Below 200 DMA And Above 50 DMA')

st.dataframe(stock_tr_2[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('## Excess Returns')
st.write('### Excess Return above 80 percentile')
st.dataframe(stock_ex_1[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('### Excess Return below 20 percentile')
st.dataframe(stock_ex_2[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('## High volatility and Large Drawdowns')
st.dataframe(stock_vol[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

st.write('## Excess Returms > 20 and losing Short Term Momentum(50DMA)')
st.dataframe(stock_ex50[['Ticker','Name','Category','Price','PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M','HistExcessReturn_1M','HistExcessReturn_3M','HistExcessReturn_6M','HistExcessReturn_12M','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M','ChgRnk_12M']])

