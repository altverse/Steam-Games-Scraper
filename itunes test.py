import requests

itunes_id = "6740277618"
url = "https://itunes.apple.com/lookup"
params = {
    "id": itunes_id,
    "country": "kr"  # 한국 앱 스토어 기준
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # 반환된 데이터는 JSON 형식으로, "results" 배열 내에 앱(게임) 정보가 포함됩니다.
    if data.get("resultCount", 0) > 0:
        game_info = data["results"][0]
        print("게임 정보:", game_info)
        # 기타 필요한 정보를 여기서 활용하세요.
    else:
        print("해당 조건에 맞는 게임 정보를 찾을 수 없습니다.")
else:
    print("API 요청 오류:", response.status_code)