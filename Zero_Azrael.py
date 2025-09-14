# fullscreen_with_close.py
import webview
from screeninfo import get_monitors

class Api:
    def close(self):
        try:
            webview.windows[0].destroy()
        except Exception:
            pass

if __name__ == "__main__":
    api = Api()

    # جلب أبعاد الشاشة
    monitor = get_monitors()[0]
    screen_w, screen_h = monitor.width, monitor.height

    # الموقع اللي عايز تفتحه
    url = "https://aneros112.github.io/Zero_A/"

    # HTML وسيط يحط الموقع + زر إغلاق فوقه
    html = f"""
    <html>
    <head>
    <style>
      html, body {{
        margin:0; padding:0; height:100%; width:100%;
        overflow:hidden;
      }}
      iframe {{
        border:none;
        width:100%; height:100%;
      }}
      button {{
        position:fixed; top:20px; right:20px;
        padding:12px 20px; border:none; border-radius:12px;
        background:linear-gradient(90deg, #d9363e, #ff4d4f);
        color:white; font-weight:bold; cursor:pointer;
        box-shadow:0 6px 16px rgba(0,0,0,0.35);
        z-index:9999;
      }}
      button:hover{{opacity:0.85;}}
    </style>
    </head>
    <body>
      <button onclick="window.pywebview.api.close()">إغلاق ✖</button>
      <iframe src="{url}"></iframe>
    </body>
    </html>
    """

    window = webview.create_window(
        title="Zero Azrael",
        html=html,
        width=screen_w,
        height=screen_h,
        resizable=True,
        frameless=False,       # خليه False عشان التفاعل شغال
        background_color="#0f0f10",
        js_api=api
    )

    webview.start(debug=False)
