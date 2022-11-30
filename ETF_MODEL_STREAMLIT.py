{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMLo+AYXF1QvJ7TXnSdyVxd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jprasham/ETF_STREAMLIT/blob/main/ETF_MODEL_STREAMLIT.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mMIAnqdXNq50",
        "outputId": "e8802832-5655-47a1-e14c-8dd374641c37"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.7/dist-packages (1.12.11)\n",
            "Collecting google-api-python-client\n",
            "  Downloading google_api_python_client-2.66.0-py2.py3-none-any.whl (10.5 MB)\n",
            "\u001b[K     |████████████████████████████████| 10.5 MB 4.4 MB/s \n",
            "\u001b[?25hRequirement already satisfied: google-auth-httplib2 in /usr/local/lib/python3.7/dist-packages (0.0.4)\n",
            "Collecting google-auth-httplib2\n",
            "  Downloading google_auth_httplib2-0.1.0-py2.py3-none-any.whl (9.3 kB)\n",
            "Requirement already satisfied: google-auth-oauthlib in /usr/local/lib/python3.7/dist-packages (0.4.6)\n",
            "Collecting google-auth-oauthlib\n",
            "  Downloading google_auth_oauthlib-0.7.1-py2.py3-none-any.whl (19 kB)\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.15.1-py2.py3-none-any.whl (10.3 MB)\n",
            "\u001b[K     |████████████████████████████████| 10.3 MB 34.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: httplib2<1dev,>=0.15.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client) (0.17.4)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client) (3.0.1)\n",
            "Requirement already satisfied: google-auth<3.0.0dev,>=1.19.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client) (2.14.1)\n",
            "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client) (2.8.2)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from google-auth-httplib2) (1.15.0)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /usr/local/lib/python3.7/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (1.57.0)\n",
            "Requirement already satisfied: protobuf<5.0.0dev,>=3.15.0 in /usr/local/lib/python3.7/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (3.19.6)\n",
            "Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /usr/local/lib/python3.7/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2.23.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.7/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (4.9)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (5.2.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (0.2.8)\n",
            "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /usr/local/lib/python3.7/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (0.4.8)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2022.9.24)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.7/dist-packages (from google-auth-oauthlib) (1.3.1)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib) (3.2.2)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (6.0.4)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.29-py3-none-any.whl (182 kB)\n",
            "\u001b[K     |████████████████████████████████| 182 kB 45.2 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.21.6)\n",
            "Collecting rich>=10.11.0\n",
            "  Downloading rich-12.6.0-py3-none-any.whl (237 kB)\n",
            "\u001b[K     |████████████████████████████████| 237 kB 39.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Collecting validators>=0.2\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "Collecting blinker>=1.0.0\n",
            "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
            "Collecting semver\n",
            "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-2.1.9-py3-none-manylinux2014_x86_64.whl (78 kB)\n",
            "\u001b[K     |████████████████████████████████| 78 kB 1.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.3)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.3.5)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 4.8 MB/s \n",
            "\u001b[?25hCollecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[K     |████████████████████████████████| 164 kB 10.8 MB/s \n",
            "\u001b[?25hRequirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[K     |████████████████████████████████| 62 kB 275 kB/s \n",
            "\u001b[?25hCollecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=1.4->streamlit) (3.10.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.19.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (22.1.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.10.0)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging>=14.1->streamlit) (3.0.9)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2022.6)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in /usr/local/lib/python3.7/dist-packages (from rich>=10.11.0->streamlit) (2.6.1)\n",
            "Collecting commonmark<0.10.0,>=0.9.0\n",
            "  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)\n",
            "\u001b[K     |████████████████████████████████| 51 kB 1.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.7/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19581 sha256=cfd248dac1227216f8028c5afbf86d2f5d739f84a58b362055911e5e6fdef682\n",
            "  Stored in directory: /root/.cache/pip/wheels/5f/55/ab/36a76989f7f88d9ca7b1f68da6d94252bb6a8d6ad4f18e04e9\n",
            "Successfully built validators\n",
            "Installing collected packages: smmap, gitdb, commonmark, watchdog, validators, semver, rich, pympler, pydeck, google-auth-httplib2, gitpython, blinker, streamlit, google-auth-oauthlib, google-api-python-client\n",
            "  Attempting uninstall: google-auth-httplib2\n",
            "    Found existing installation: google-auth-httplib2 0.0.4\n",
            "    Uninstalling google-auth-httplib2-0.0.4:\n",
            "      Successfully uninstalled google-auth-httplib2-0.0.4\n",
            "  Attempting uninstall: google-auth-oauthlib\n",
            "    Found existing installation: google-auth-oauthlib 0.4.6\n",
            "    Uninstalling google-auth-oauthlib-0.4.6:\n",
            "      Successfully uninstalled google-auth-oauthlib-0.4.6\n",
            "  Attempting uninstall: google-api-python-client\n",
            "    Found existing installation: google-api-python-client 1.12.11\n",
            "    Uninstalling google-api-python-client-1.12.11:\n",
            "      Successfully uninstalled google-api-python-client-1.12.11\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "tensorboard 2.9.1 requires google-auth-oauthlib<0.5,>=0.4.1, but you have google-auth-oauthlib 0.7.1 which is incompatible.\u001b[0m\n",
            "Successfully installed blinker-1.5 commonmark-0.9.1 gitdb-4.0.10 gitpython-3.1.29 google-api-python-client-2.66.0 google-auth-httplib2-0.1.0 google-auth-oauthlib-0.7.1 pydeck-0.8.0 pympler-1.0.1 rich-12.6.0 semver-2.13.0 smmap-5.0.0 streamlit-1.15.1 validators-0.20.0 watchdog-2.1.9\n"
          ]
        }
      ],
      "source": [
        "!pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from googleapiclient.discovery import build\n",
        "from google.oauth2 import service_account\n",
        "import json\n",
        "import numpy as np\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "3dIHx-KaQT3Z"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cred = {'type': 'service_account',\n",
        " 'project_id': 'etf-model-369713',\n",
        " 'private_key_id': '45aad76af9ae8f68ff8868b177ade3106abbb6f0',\n",
        " 'private_key': '-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0Sgnt59iKyLHQ\\nZn7SowrdqUNOj+ColMW5ai1coBfFUTBb1dEhl0NAggJr8mSYvZW8PZy2rnknSgjI\\ngLgyNfZSMPSLBw8Nzqzgd3v4GKPoErTZoJaZiht+WHvWkIpjDZbm3eGpf79onpVU\\ncN+Ac1lRrQYD8k6qIa9aqnKm8Qqfe+ZUFForO94bBNa+4Dxd3B9iOlIasONTuZNI\\ndEIeq0JFuY4oJYlNBWaiLAEfhqCRVnwL6cJUXPAU5goxAX/NKfzSVCL1mHAv03j7\\npy/98EtxDXl3SFxMfqXwW7l2CgUOdUpU/Ctpkc3kua22zYA9/Q1sV737X8GgscQx\\nRA2vhUQ/AgMBAAECggEABQCq7t2Iji1Mdc5qRXj9s7HfKr5mSvc510/Ba3kLv89l\\nap7vuyFh3dfdrlYfAXf9QChrgUwtE3CD9uBPfCEwMQ6nsnXjLoxmEqJuH6+7WJSw\\nTPueQitpYOOeqBEBrgbyAXz1pojjbEk+NoYdRYit2UzWRmTCVwkxPvBM1yIIG+29\\nt56lSeo1lg8Ibui6mmZteQ2Q9u7GwbhPBJwgjzVwdwKFfxMdr7uuwnNuJRwAAoBt\\n1M6ENoB1zUWeUStQlCgCR/xh8VbtwA5xe9p8nKOfwK2hesiskJrojTWXiszWaBu6\\nHfAxHce+lSEacpBEI2FRWSiqxVgBlNmrgOu1C1DecQKBgQDsg2AEOH2xvVKSapyn\\nwNazJVVxzuwuJYf8G9HQf2/ibHZrCL34Uo9o449NjS1o7FIyFP2rFcX2EwQTJUSg\\nPbFVEjOc3X/xYO0ILrJ4bCN7vBFh0QrO/2Y/3XqbkQZGbosxmAsKEPCRA7spIMTk\\nDcsGZTAYaI3EAVeoBlqK+1i7DwKBgQDDJMRBmP+0PzOj/oJLUlXk0I/YaaY0BQH5\\nlnoogyW9rsABCp/W9wfD3fpxwOy7sQ/JHzSWXLD6L5NUVuSthNSXI8Xf4KX2Qhj5\\nK4+lLj0YTfQdyP2FPNbqhtupWQfMSZmuo/swIa05GIEBgC7xaDrvPX3zs8sIaXhT\\nsNSKO2aj0QKBgG1y/mP1oHU4H5YSMByRaMnOZRQdpb5VL/DDDv1le+lUOBigGwln\\na2YmqJJC2tjLQ95ZSGp70PhnJGOXw4JECmRL4Aafmi2hpQ88TOrdYC5KgeC6VD4m\\ngrLbU3naSwUc8t0odzNZU3pIN7x4paTDnUiAWxlwiOpDlMT068GVPyKRAoGBAIB/\\nrmgPqplzYLrldcDJh9vzZjU4ZIQuo/1JFEmnCmwcLTzCVTyFUGyuuCK9ymVRk7Z5\\nQPSeNr+YImjQCycjp6WancrtL/u3zKAPCjjX+M0PT+dpGV/qDw9CHFUoVhU0helU\\n+6vXESzesNxfHwpB+0TcdhrK0rBIWz6o21vm/5BxAoGASW1SzD/wYvaXqMzBNWWz\\nxumt5MPEg6wJ1byc1w50UZJe0ie2sby9G8n1x3D32Q6ixsEXywBCqKn8fzAfGPE1\\nnl1XOfAgXO8CpK/8ZA/HzRIbEXyH+ufvyS/pgPdBR31XkD+sX5h5fB6RnlolT/Ys\\n5HZ6sPgD1hwK16wBxtXTNB0=\\n-----END PRIVATE KEY-----\\n',\n",
        " 'client_email': 'etf-model-83@etf-model-369713.iam.gserviceaccount.com',\n",
        " 'client_id': '104785831308812239864',\n",
        " 'auth_uri': 'https://accounts.google.com/o/oauth2/auth',\n",
        " 'token_uri': 'https://oauth2.googleapis.com/token',\n",
        " 'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',\n",
        " 'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/etf-model-83%40etf-model-369713.iam.gserviceaccount.com'}\n",
        "\n",
        "\n",
        "SCOPES = ['https://www.googleapis.com/auth/spreadsheets']\n",
        "\n",
        "creds = None\n",
        "creds = service_account.Credentials.from_service_account_info(cred, scopes=SCOPES)\n",
        "\n",
        "ETF_SHEET_ID = '1j38MEMdIPUbyGK2Vir7t-NRwaH5TJLNoUdf2l54lC7o'\n",
        "CL_PR_SHEET_ID = '1O7ZbPpO4L5i_VMJcGq4O-kRXKaXQtwvr1peh5MCwxgM'\n",
        "\n",
        "\n",
        "service = build('sheets', 'v4', credentials=creds)\n",
        "\n",
        "sheet = service.spreadsheets()\n",
        "result = sheet.values().get(spreadsheetId=ETF_SHEET_ID,\n",
        "                            range='ETF_DATA!A:ZZ').execute()\n",
        "values = result.get('values',[]) \n",
        "\n",
        "ETFs = pd.DataFrame(values)\n",
        "new_header = ETFs.iloc[0] \n",
        "ETFs = ETFs[1:] \n",
        "ETFs.columns = new_header\n",
        "ETFs.reset_index(drop=True, inplace=True)\n",
        "tickers = ETFs['Ticker']\n",
        "ETFs[['Beta','Price','Change_1D','Return_1W','Return_1M',\n",
        "      'Return_3M','Return_6M','Return_12M','PctRank_1W',\n",
        "      'PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M',\n",
        "      'ShortMoM_avg','MoM_avg','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M',\n",
        "      'ChgRnk_12M','Fallin1Mmore20','Fallin1Wmore10','StdevNegativeReturn',\n",
        "      'HistExcessReturn_1W','HistExcessReturn_1M','HistExcessReturn_3M',\n",
        "      'HistExcessReturn_6M','HistExcessReturn_12M']] = ETFs[['Beta','Price','Change_1D','Return_1W','Return_1M',\n",
        "                                                             'Return_3M','Return_6M','Return_12M','PctRank_1W',\n",
        "                                                             'PctRank_1M','PctRank_3M','PctRank_6M','PctRank_12M',\n",
        "                                                             'ShortMoM_avg','MoM_avg','ChgRnk_1M','ChgRnk_3M','ChgRnk_6M',\n",
        "                                                             'ChgRnk_12M','Fallin1Mmore20','Fallin1Wmore10','StdevNegativeReturn',\n",
        "                                                             'HistExcessReturn_1W','HistExcessReturn_1M','HistExcessReturn_3M',\n",
        "                                                             'HistExcessReturn_6M','HistExcessReturn_12M']].astype(float)\n",
        "result = sheet.values().get(spreadsheetId=CL_PR_SHEET_ID,\n",
        "                            range='Close_Price!A:ZZ').execute()\n",
        "values = result.get('values',[]) \n",
        "\n",
        "combined_df = pd.DataFrame(values)\n",
        "new_header = combined_df.iloc[0] \n",
        "combined_df = combined_df[1:] \n",
        "combined_df.columns = new_header\n",
        "combined_df.reset_index(drop=True, inplace=True)\n",
        "combined_df['Date'] = pd.to_datetime(combined_df['Date'])\n",
        "combined_df.set_index('Date', inplace=True)\n",
        "combined_df.replace('',np.nan,inplace = True)\n",
        "combined_df = combined_df.astype(float)"
      ],
      "metadata": {
        "id": "g9yGIALBP4Mj"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.header('ETF Frame Work')\n",
        "\n",
        "with st.sidebar:\n",
        "  etf = st.selectbox('ETF Tickers:', ETFs['Ticker'],)\n",
        "  st.write('You selected:', etf,': ',ETFs.loc[ETFs['Ticker'] == etf,'Name'])\n",
        "  d_etf = ETFs.loc[ETFs['Ticker'] == etf]\n",
        "  st.dataframe(d_etf)\n",
        "  data = {\"close\": combined_df[etf],\n",
        "          \"50_mean\": combined_df[etf].rolling(window=50).mean(),\n",
        "          \"200_mean\": combined_df[etf].rolling(window=200).mean()\n",
        "          }\n",
        "  d_plt = pd.concat(data,axis = 1)\n",
        "  st.line_chart(d_plt)\n",
        "\n",
        "st.write('# Top 5  ETFs Based on Short term Momentum')\n",
        "df_st = ETFs.nsmallest(5,'ShortMoM_avg')\n",
        "st.dataframe(df_st)\n",
        "st.write('# Top 5  ETFs Based on Long term Momentum')\n",
        "df_lt = ETFs.nsmallest(5,'MoM_avg')\n",
        "st.dataframe(df_lt)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_BRkD8JGUW3L",
        "outputId": "75a0b14e-4202-4d58-a7c0-838000130cc1"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:root:\n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n",
            "2022-11-30 10:07:02.103 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    }
  ]
}