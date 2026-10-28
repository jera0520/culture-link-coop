#!/usr/bin/env python3
"""IndexNow 핑 — push해서 배포가 끝난 뒤 sitemap.xml의 URL을 IndexNow에 알린다(Bing 등 참여 검색엔진이 받는다).

    python3 _src/indexnow.py            # sitemap.xml의 URL 전부
    python3 _src/indexnow.py /hahoe-jumak/ /llms.txt   # 고친 쪽만

키 파일은 저장소 루트의 <키>.txt(내용 = 키). 지우면 핑이 거절된다.
구글은 IndexNow를 받지 않는다 — 구글은 sitemap.xml lastmod로 알린다.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "munlink.co.kr"
SITE = "https://" + HOST

keys = [p for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}\.txt", p.name)]
if len(keys) != 1:
    sys.exit(f"키 파일이 1개여야 합니다: {[p.name for p in keys]}")
key = keys[0].stem

if len(sys.argv) > 1:
    urls = [SITE + a if a.startswith("/") else a for a in sys.argv[1:]]
else:
    urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))

body = json.dumps({
    "host": HOST,
    "key": key,
    "keyLocation": f"{SITE}/{key}.txt",
    "urlList": urls,
}).encode()
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=body,
    headers={"Content-Type": "application/json; charset=utf-8"},
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(r.status, len(urls), "URL")
except urllib.error.HTTPError as err:
    # 200·202 = 받음, 403 = 키 파일을 못 찾음(배포 전), 422 = URL이 host와 다름
    print(err.code, err.read().decode(errors="replace")[:300])
    sys.exit(1)
