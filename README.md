# **OpenCTI 2 LLM**
Produce Suricata rule with ChatGPT3.5 turbo by exporting report from OpenCTI

## Install 
- [How to install OpenCTI](https://ithelp.ithome.com.tw/articles/10336576)

## Prepare
```bash
# clone this repository, or fork first and clone your fork
$ cd (to this repository)
$ pip install -r requirements.txt
```
- Add a .env file and Put OpenAI api in .env file

` OPENAI_API_KEY = *****`
- Change opencti_api_client variable in api.py : OpenCTIApiClient('url','OPENCTI_ADMIN_TOKEN')
## Use
```bash
$ cd (to your opencti docker folder)
$ sudo docker-compose up -d
$ cd (to this repository)
$ streamlit run streamlit.py
```
