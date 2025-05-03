import requests
from fake_useragent import UserAgent


def get_url(url, return_type="text", headers=None, proxies=None, timeout=10):
    if headers is None:
        headers = {
            "User-agent": UserAgent().random,
            "Connection": "close",
        }
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            if return_type == "text":
                response.encoding = "utf-8"
                return response.text
            elif return_type == "content":
                return response.content
            else:
                raise ValueError(
                    f"Invalid return_type {return_type}. Use 'text' or 'content'."
                )
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def down_image_from_url(url, save_path):
    content = get_url(url, return_type="content")
    if content is None:
        print(f"{url} 下载失败...")
        return
    with open(save_path, "wb") as f:
        f.write(content)
