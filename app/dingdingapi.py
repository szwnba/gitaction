
import json
import requests

# 发送信息
def senddingding_news(product,infos):
    print('[INFO]:Start to send infos ' )
    token = "fc1ad21323ce73728bafc3770f27763c36761abe87abe03642038b52e869f85f"
    url="https://oapi.dingtalk.com/robot/send?access_token={}".format(token)
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    title = ""
    jsonContent =""
    for item in infos:
        title = title + item['title'] +'\n'
        jsonContent = jsonContent + '- '+ item['title']  + ' ['+ item['subtype'] +'](' + item['link'] + ')\n\n'
    json_text = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": jsonContent
        }
    }
    response = requests.post(url, data=json.dumps(json_text),headers=headers)
    print('[INFO]:End to send infos')
    return response.status_code


if __name__ == '__main__':

    print("response.content")
