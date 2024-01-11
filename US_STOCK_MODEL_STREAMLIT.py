import streamlit as st
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import numpy as np
import pandas as pd
cred = {
  "type": "service_account",
  "project_id": "us-sock-model",
  "private_key_id": "f001070ec4a7a2d9a8333cd689fd01aa4e92c831",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0NTu+9ZAIu0NT\nNI9tLLQAOBLBSvJz6yNx5bFkZF6odSUgGKF6pi5pAOJIf1SNrtdWeJrsMBMs/ZDZ\n+CfGqHtyFrAxe75ehJWQiVAKJk3mv4av7uzuaAF/kk54axELEg9EwkIi4nA4UxMy\n/1KNpORp9WRaSLf+EskEQ3MY919pt1rG1PAqH+jO4+ImPILXYj01tzcwJ8KEgATG\nt6wjsBLiOWQX5zHbmXdLsYSVc0jk+Sb0LartywShTJ1xnELgVutUjjmFp/bP11Xv\nBV9RUYb3Yg5TBRrEo6AkJt2OqvRKcdvVwnnX9QFfWWo8qPbWLpwv+CpUL9ms1wS5\nba9N1HibAgMBAAECggEAS8fdBYsPVFSnVayTKeZ0FWl/HZCuT2fQwntEc0Kv+ag1\ngf9JnKGYf6iS/8in3mLphB/4ih0XW0KQMNElrOk57Dq1QkHWxrl7icnsgjAkb0YY\nVhCjyweqpaJ5ZDMl+iFQkWodVL0jUtRAjSAIb68pLJO4bS0KTopIxQW2N4gDNBlk\nhYTVZxkUQA0vIzBhHoq/wezpoi+bHgyHnttxft1lNClYlk22JHwxvdc9dn/i3RrS\niTcZo4u+DLp6NaUaColuBu+sTNiGoJe857gxeJtzrQnZXco8wWquoXIrjbj8btqB\nPTBMvt6cWB+oGr/VUbnRKIugV7va2qO2o48g96oVAQKBgQDwWbXCYKA0GGyBEPcV\n1xN7ZRLfp9K5i+p0fDkuW6JsrMIYVEBUVU/fTI3iEtSvUBe5x3nJ3wirYm3LdI9c\nAOpHuXM+raScTUQGIE/dsjKdNN87kFLSu9yU+5KCY7KUDkKBnS+gksjIlWyQv08q\nbaPA7d9Aqlv5WQGH8gKZUkTHAQKBgQC/8Qk/jr3SpAOsfNfjGij+mu5xvsNw8ijW\ny6XNwI7giK5Ut6u/SEyEhZ25/GZOJU8KN/gMOhWKOgo0gHMY/X9s7D4tpScgLvF4\nOpmJEFvjWbnvjhxHFKsCS64JGcCxDQLq7FHmkzq/ccldDh/834YbMhNnyTabsO/X\npDEkERL7mwKBgEuE5IdetPepdO5Y1koWehibeYKsyJlkTRassYrPYAmlfpcGYfAd\nnisbcrlGEW3ETLAi7TFw0tiG5Ni4lxLhdrtymbNn/ADghi8ml/GgvCaJJlsgzeVJ\nAdYN9criaIn8sQjoyr45YL0lticE9WrvaDSGiU9YN+3w+XotoINsRhABAoGBAIOb\nOcQik3VCkGJMl5pX7ZPll2jWbBudbvMYX29cgJrkHORpq5FUeWLEWwmTTnJ2kmNn\nTOTVTr+gXC7zg/e2mRCOS3PwsYsXpOnTBEM+vEJ+20auIiV6vmasjYAf8Ed1rHJ3\n5xA6EyYBVxg+/x/cA4/SHgwjoxXNlCY/ppIcQu/RAoGART7kJzdVLmPZMt7OTnFX\nDQunJkLDX3Mn/ilMgkUx9TKnIkBjxIFEI1ajDCrXVrbBUcbokx8ktRmSan4d2ugf\n1CEIiO4/FFqkgKH2n45Eas9YJc19YGvNyl8dhlJWJ7T6/hq12b/nhTV9on2B/CeW\n60jvLjjKYeE/NWpD/fP+BJ8=\n-----END PRIVATE KEY-----\n",
  "client_email": "us-stock-model@us-sock-model.iam.gserviceaccount.com",
  "client_id": "107107385298300590664",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/us-stock-model%40us-sock-model.iam.gserviceaccount.com"
}

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

st.header('US LARGE CAP Frame Work')

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

  url = "https://drive.google.com/file/d/17ik5Xj2OBbIkau5sJtOsu9mlUFq4bFFD/view?usp=sharing"

  st.write("Click on the link to view charts(%s) " % url)

  url2 = "https://docs.google.com/spreadsheets/d/13mS_ier4GgJiqbR0ak8lgV7lWaJyY7ItWUuJH-CyEQg/edit?usp=sharing"
  
  st.write("Click on the link to view database(%s) " % url2)
  
  url3 = "https://etf-model.streamlit.app/"
  st.write("Link to the ETF Model(%s) " % url3)

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

