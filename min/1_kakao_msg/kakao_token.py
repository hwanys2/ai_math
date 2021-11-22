# 1. 사용자 토큰 받기
import requests

def getNewToken():
    url = "https://kauth.kakao.com/oauth/token"
    rest_api_key = 'd13fdd39cf5b49a76e7d747a3a5bf6bd'
    redirect_uri = 'https://example.com/oauth'
    authorize_code = 'BIpmUYf0EzL6iqe12IqRO2G92cSzrgw96X7BlsqY3CDWDSR0urNatsAk6JDRpeMU7YkaXAo9dNoAAAF8WPdBYg'
    #authorize_code 요청 => https://kauth.kakao.com/oauth/authorize?client_id=d13fdd39cf5b49a76e7d747a3a5bf6bd&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends

    data = {
        'grant_type' : 'authorization_code',
        'client_id' : rest_api_key,
        'redirect_uri' : redirect_uri,
        'code' : authorize_code
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)


    # 2. json 저장
    import json
    with open(r"D:\Project\py\study\kakao_code.json","w") as fp:
        json.dump(tokens, fp)

    print("토큰 완료")
#네이티브 앱 키	0e9308f544287eab284b8bc8c050cb11
#REST API 키	d13fdd39cf5b49a76e7d747a3a5bf6bd
#JavaScript 키	cd9eb23f3b1026a55e91f337a006793e
#Admin 키	e94f3e59aa00555c400f02169736d9c1

getNewToken()

# 로그인 : 인가코드받기, 토큰받기