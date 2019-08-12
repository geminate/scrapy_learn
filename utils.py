# 将浏览器中的 cookie 转换为 dict 格式
def cookie_to_dict(cookie):
    return dict([l.split("=", 1) for l in cookie.split("; ")])
