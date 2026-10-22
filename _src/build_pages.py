#!/usr/bin/env python3
"""질문 하나 = 쪽 하나. 이 파일 하나에서 화면 HTML과 FAQPage JSON-LD를 함께 만든다.

값을 고치면 이 파일만 고치고 `python3 _src/build_pages.py`로 다시 만든다.
(밑줄로 시작하는 폴더라 GitHub Pages(Jekyll)는 이 폴더를 배포하지 않는다.)
근거: 카카오톡 채널 안내문 원문(2026-10-12, munlink-work/_review/카카오채널_자동응답_원문_2026-10-12.md),
볼트 wiki/topics/하회주막민박_판매정보_2026-09-18.md, 사이트 index.html 문구.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://munlink.co.kr"
ASOF = "2026-10-12"
MODIFIED = "2026-10-20"
KAKAO = "https://pf.kakao.com/_iKJxaX"
AIRBNB = "https://www.airbnb.co.kr/rooms/1516268030786572692"
ADDR_JUMAK = "경상북도 안동시 풍천면 하회북촌길 20-6"

CONTACT_A = (
    f"카카오톡 채널로 희망 날짜와 인원을 메시지로 남기거나 054-841-2783으로 전화해 주세요. "
    f"이메일 mun_link@naver.com으로도 받습니다."
)

PAGES = [
    {
        "slug": "hahoe-jumak",
        "nav": "하회마을 주막 체험",
        "title": "안동 하회마을 주막 체험 — 하회주막 위치·프로그램·예약 | 문화링크협동조합",
        "desc": "안동 하회마을 안 120년 된 초가집 하회주막에서 종가음식 만들기, 전통주 만들기·시음 체험을 합니다. 위치, 프로그램, 금액 안내 방법, 찾아오는 길, 예약 방법.",
        "h1": "안동 하회마을 주막 체험은 어디서, 무엇을 하나요?",
        "answer": "하회마을 안 120년 된 초가집 「하회주막」에서 종가음식 만들기와 전통주 만들기·시음을 합니다. 가족·단체 모두 가능하고, 금액은 날짜와 인원에 따라 안내드립니다.",
        "img": ("images/p1.webp", "하회마을 야외 주막 체험장"),
        "facts": [
            ("장소", f"하회주막 · {ADDR_JUMAK} (하회마을 안)"),
            ("프로그램", "종가음식 만들기 · 전통주 만들기 · 시음"),
            ("진행 단위", "90분 단위 프로그램"),
            ("대상", "가족 · 단체"),
            ("군자주 담그기", "체험 키트 1세트 22,000원"),
            ("금액·구성", "날짜와 인원에 따라 달라지며 문의하시면 안내드립니다"),
        ],
        "faq": [
            ("체험 금액은 얼마인가요?",
             "인원과 날짜에 따라 구성이 달라집니다. 희망 날짜와 인원을 남겨 주시면 가능한 프로그램과 금액을 안내드립니다. 군자주 담그기 체험은 키트 1세트 22,000원입니다(2026-10-12 기준)."),
            ("군자주 담그기는 어떤 체험인가요?",
             "매화·오미자·국화·녹차 네 가지 재료로 군자주를 직접 담그는 체험입니다. 담근 병은 그대로 가져가실 수 있습니다."),
            ("하회주막은 어떻게 찾아가나요?",
             "차는 하회마을 매표소 주차장에 세우고, 매표소 앞에서 마을로 들어가는 셔틀버스를 탑니다. 버스에서 내려 마을 입구의 큰 안내판(지도)을 지나 걸어서 7분쯤 오시면 하회주막입니다."),
            ("예약은 어떻게 하나요?", CONTACT_A),
        ],
    },
    {
        "slug": "jongga-food",
        "nav": "종가음식 체험·단체 식사",
        "title": "안동 종가음식 체험·단체 식사 — 하회마을 하회주막 | 문화링크협동조합",
        "desc": "안동 하회마을 하회주막에서 종가음식 만들기 체험을 운영하고, 단체는 체험 뒤 이어지는 식사(상차림·식음)까지 맡길 수 있습니다. 대상, 식사 방식, 단체·기관 문의 방법.",
        "h1": "안동 종가음식 체험과 단체 식사는 어떻게 하나요?",
        "answer": "하회마을 하회주막에서 종가음식 만들기 체험을 운영하고, 단체는 체험이 끝난 자리에서 바로 이어지는 식사까지 맡길 수 있습니다. 금액은 날짜와 인원에 따라 안내드립니다.",
        "img": ("images/p2.webp", "유기 반상에 차려진 종가음식 상차림"),
        "facts": [
            ("체험", f"종가음식 만들기 · 하회주막({ADDR_JUMAK})"),
            ("식사 운영", "체험 뒤 이어지는 식사 · 상차림 · 단체 식음 · 야외 운영"),
            ("상차림", "날이 좋으면 마당, 비가 오면 그늘막 아래"),
            ("단체·기관", "단체 종가음식 체험과 식사 운영 · 기획부터 운영·정산까지"),
            ("금액·인원", "날짜와 인원에 따라 달라지며 문의하시면 안내드립니다"),
        ],
        "faq": [
            ("가족이나 소규모로도 할 수 있나요?",
             "가족·단체 모두 가능합니다. 인원과 날짜에 따라 구성이 달라지므로 희망 날짜와 인원을 먼저 남겨 주세요."),
            ("단체·기관 행사도 맡길 수 있나요?",
             "지자체·기관·기업 단체 프로그램을 기획부터 운영·정산까지 진행합니다. 단체 종가음식 체험과 식사 운영을 함께 맡길 수 있습니다. 행사 성격과 인원, 희망 일정을 남겨 주시면 제안 내용을 정리해 회신드립니다."),
            ("식사는 어디서 하나요?",
             "종가에서 먹던 방식대로 상을 차립니다. 날이 좋으면 마당에서, 비가 오면 그늘막 아래에서 드십니다."),
            ("문의는 어떻게 하나요?", CONTACT_A),
        ],
    },
    {
        "slug": "hahoe-minbak",
        "nav": "하회마을 한옥 민박",
        "title": "안동 하회마을 한옥 민박 — 하회주막&민박 요금·시설·예약 | 문화링크협동조합",
        "desc": "안동 하회마을 안 120년 된 초가집 하회주막&민박을 집 한 채 통째로 빌려 드립니다. 1박 50만 원, 최대 10명, 침실 4·욕실 2, 체크인 17:00·체크아웃 12:00(2026-10-12 기준).",
        "h1": "하회마을 안에서 묵을 수 있는 한옥 민박이 있나요?",
        "answer": "있습니다. 하회마을 안 120년 된 초가집 「하회주막&민박」을 집 한 채 통째로 빌려 드립니다. 1박 50만 원, 최대 10명입니다(2026-10-12 기준).",
        "img": ("images/p4.webp", "햇살이 드는 한옥 실내, 좌탁과 방석이 놓인 방"),
        "facts": [
            ("이름", "하회주막&민박"),
            ("위치", f"{ADDR_JUMAK} (하회마을 안)"),
            ("요금", "1박 50만 원 · 집 전체 사용"),
            ("인원", "최대 10명"),
            ("구성", "침실 4 · 욕실 2 · 장작을 때는 전통 온돌방 · 주방"),
            ("시설", "세탁기 · 건조기 · 에어컨 · 무료 주차"),
            ("입·퇴실", "체크인 17:00 · 체크아웃 12:00"),
            ("별도 옵션", "조식(선지해장국·야채죽) · 전통주 시음·만들기 · 종가음식 만들기"),
        ],
        "faq": [
            ("화장실은 어디에 있나요?",
             "화장실은 별채에 2개 있고 샤워할 수 있습니다."),
            ("차를 숙소 앞까지 가져갈 수 있나요?",
             "숙박 손님은 숙소 앞에 주차할 수 있습니다."),
            ("예약은 어떻게 하나요?",
             "카카오톡 채널로 원하시는 날짜를 남겨 주시면 예약 가능 여부를 확인해 안내드립니다. 에어비앤비로도 예약할 수 있으며, 이 경우 플랫폼 수수료가 별도로 붙습니다."),
        ],
        "extra_links": [("에어비앤비에서 보기", AIRBNB)],
    },
    {
        "slug": "andong-sool",
        "nav": "안동 전통주 맛보기·구매",
        "title": "안동 전통주 시음·만들기·선물세트 — 하회주막 체험 | 문화링크협동조합",
        "desc": "안동 하회마을 하회주막 체험에서 전통주를 만들고 시음할 수 있고, 주류 소매 면허를 갖춘 문화링크협동조합이 안동 전통주와 특산품 선물세트를 취급합니다. 군자주 담그기 체험 키트 안내.",
        "h1": "안동 전통주는 어디서 맛보고 살 수 있나요?",
        "answer": "하회마을 하회주막 체험에서 전통주를 만들고 시음할 수 있습니다. 주류 소매 면허를 갖춘 문화링크협동조합이 안동 전통주와 특산품 선물세트를 취급합니다.",
        "img": ("images/p3.webp", "안동 전통주 선물세트"),
        "facts": [
            ("맛보기", "하회주막 체험의 전통주 만들기 · 시음"),
            ("직접 담그기", "군자주 담그기 체험 키트 1세트 22,000원"),
            ("판매", "안동 전통주 · 특산품 선물세트"),
            ("주류판매신고", "508-5-36883"),
            ("구매 문의", "전화 054-841-2783 · 이메일 · 카카오톡 채널"),
        ],
        "faq": [
            ("체험에서 맛본 술을 나중에 다시 살 수 있나요?",
             "조합은 현장에서 맛본 상품을 집에서 다시 주문할 수 있게 연결합니다. 상품과 주문 방법은 전화·이메일·카카오톡 채널로 문의해 주세요."),
            ("군자주 담그기는 어떤 체험인가요?",
             "매화·오미자·국화·녹차 네 가지 재료로 군자주를 직접 담그는 체험입니다. 담근 병은 그대로 가져가실 수 있습니다. 체험 키트는 1세트 22,000원입니다(2026-10-12 기준)."),
            ("문의는 어떻게 하나요?", CONTACT_A),
        ],
    },
]

CSS = """
:root{--bone:#F7F4EE;--bone-2:#EFEAE1;--card:#FCFAF6;--ink:#1B1916;--ink-2:#4B463E;--mute:#8C8579;
  --line:rgba(27,25,22,.13);--hair:rgba(27,25,22,.08);--accent:#2F4A38;
  --logo:linear-gradient(90deg,#4FA45C,#2E9E8F,#2F62C4,#6A4BB4,#8E46A8,#A93B72)}
*{box-sizing:border-box}
body{margin:0;background:var(--bone);color:var(--ink);
  font-family:"Noto Sans KR","Apple SD Gothic Neo",system-ui,sans-serif;font-weight:300;font-size:16px;line-height:2;
  word-break:keep-all;overflow-wrap:break-word;-webkit-font-smoothing:antialiased}
h1,h2,h3{margin:0;font-family:"Nanum Myeongjo",serif;font-weight:700;line-height:1.32;letter-spacing:-.015em;word-break:keep-all;text-wrap:balance}
p{margin:0}
a{color:inherit}
img{display:block;max-width:100%}
.wrap{width:min(860px,calc(100% - 32px));margin:0 auto}
.lab{font-size:10.5px;letter-spacing:.26em;font-weight:400;color:var(--mute)}
.top{position:sticky;top:0;z-index:10;background:rgba(247,244,238,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--hair)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 0}
.top::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:var(--logo)}
.lock{display:flex;align-items:center;gap:10px;text-decoration:none}
.lock img{width:30px;height:30px}
.wm{font-family:"Nanum Myeongjo",serif;font-weight:700;font-size:15px}
.top nav a{font-size:13px;text-decoration:none;color:var(--ink-2);margin-left:18px}
.top nav a.cta{border:1px solid var(--line);padding:6px 14px;border-radius:999px;color:var(--ink)}
main{padding:clamp(48px,9vh,96px) 0 clamp(40px,8vh,80px)}
h1{font-size:clamp(26px,4.4vw,42px);margin-top:14px;max-width:18em}
.answer{margin-top:22px;font-size:17px;line-height:1.95;color:var(--ink);border-left:2px solid var(--accent);padding-left:16px;font-weight:400}
.ph{margin-top:36px;aspect-ratio:16/9;overflow:hidden;background:var(--bone-2)}
.ph img{width:100%;height:100%;object-fit:cover}
h2{font-size:clamp(20px,2.6vw,26px);margin-top:clamp(48px,8vh,72px)}
.facts{margin:20px 0 0;border-top:1px solid var(--line)}
.facts div{display:grid;grid-template-columns:150px 1fr;gap:16px;padding:12px 0;border-bottom:1px solid var(--hair)}
.facts dt{color:var(--mute);font-size:13.5px;font-weight:400}
.facts dd{margin:0;font-size:15px}
.asof{margin-top:12px;font-size:12.5px;color:var(--mute)}
.qa{margin-top:20px}
.qa h3{font-size:18px;margin-top:28px}
.qa p{margin-top:8px;color:var(--ink-2);font-size:15.5px}
.note{margin-top:14px;color:var(--ink-2);font-size:15.5px}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.btn{display:inline-block;text-decoration:none;font-size:14px;padding:10px 20px;border-radius:999px;border:1px solid var(--line)}
.btn.fill{background:var(--ink);color:var(--bone);border-color:var(--ink)}
.more{list-style:none;padding:0;margin:16px 0 0}
.more li{border-bottom:1px solid var(--hair)}
.more a{display:block;padding:12px 0;text-decoration:none}
.more a::after{content:" →";color:var(--mute)}
footer{border-top:1px solid var(--hair);padding:clamp(32px,5vh,52px) 0}
footer small{color:var(--mute);font-size:11.5px;line-height:2.1;display:block}
footer a{text-decoration:underline;text-underline-offset:2px}
@media(max-width:620px){.facts div{grid-template-columns:1fr;gap:2px}.top nav a:not(.cta){display:none}}
""".strip()

FOOTER = """<footer>
  <div class="wrap">
    <small>문화링크협동조합 · 대표 김영숙 · 사업자등록번호 508-81-38111 · 주류판매신고 508-5-36883<br>
    경상북도 안동시 경동로 574, 1층 (우)36674 · 2014년 4월 설립<br>
    전화 <a href="tel:0548412783">054-841-2783</a> · 이메일 <a href="mailto:mun_link@naver.com">mun_link@naver.com</a> · <a href="/">문화링크협동조합 홈</a></small>
  </div>
</footer>"""

e = html.escape


def build(p):
    url = f"{SITE}/{p['slug']}/"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "FAQPage",
                "@id": url + "#faq",
                "url": url,
                "name": p["h1"],
                "inLanguage": "ko",
                "dateModified": MODIFIED,
                "publisher": {"@id": SITE + "/#org"},
                "mainEntity": [
                    {"@type": "Question", "name": p["h1"],
                     "acceptedAnswer": {"@type": "Answer", "text": p["answer"]}}
                ] + [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in p["faq"]
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "문화링크협동조합", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": p["nav"], "item": url},
                ],
            },
        ],
    }
    facts = "\n".join(
        f'      <div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in p["facts"]
    )
    qa = "\n".join(
        f'      <h3>{e(q)}</h3>\n      <p>{e(a)}</p>' for q, a in p["faq"]
    )
    extra = "".join(
        f'\n      <a class="btn" href="{e(h)}" target="_blank" rel="noopener">{e(t)}</a>'
        for t, h in p.get("extra_links", [])
    )
    others = "\n".join(
        f'      <li><a href="/{o["slug"]}/">{e(o["h1"])}</a></li>'
        for o in PAGES if o is not p
    )
    img, alt = p["img"]
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="문화링크협동조합">
<meta property="og:title" content="{e(p["h1"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&family=Noto+Sans+KR:wght@300;400;500&display=swap">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<style>
{CSS}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="lock" href="/"><img src="/images/mark.png" alt="문화링크협동조합 로고"><span class="wm">문화링크협동조합</span></a>
    <nav aria-label="주요 메뉴"><a href="/#works">사업</a><a class="cta" href="#contact">예약·문의</a></nav>
  </div>
</header>
<main>
  <article class="wrap">
    <p class="lab">자주 묻는 질문 · {e(p["nav"])}</p>
    <h1>{e(p["h1"])}</h1>
    <p class="answer">{e(p["answer"])}</p>
    <div class="ph"><img src="/{img}" alt="{e(alt)}"></div>

    <h2>한눈에 보기</h2>
    <dl class="facts">
{facts}
    </dl>
    <p class="asof">금액·시간은 {ASOF} 기준 조합 안내입니다. 바뀔 수 있으니 예약 전에 확인해 주세요. (쪽 갱신 {MODIFIED})</p>

    <h2>자주 묻는 질문</h2>
    <div class="qa">
{qa}
    </div>

    <h2 id="contact">예약·문의</h2>
    <p class="note">편한 방법으로 연락해 주세요. 희망 날짜와 인원을 함께 남겨 주시면 빨리 안내드릴 수 있습니다.</p>
    <div class="btns">
      <a class="btn fill" href="{KAKAO}" target="_blank" rel="noopener">카카오톡 채널로 문의</a>
      <a class="btn" href="tel:0548412783">054-841-2783</a>
      <a class="btn" href="mailto:mun_link@naver.com">이메일 문의</a>{extra}
    </div>

    <h2>다른 질문</h2>
    <ul class="more">
{others}
      <li><a href="/">문화링크협동조합이 하는 다섯 가지 일</a></li>
    </ul>
  </article>
</main>
{FOOTER}
</body>
</html>
"""


if __name__ == "__main__":
    for p in PAGES:
        out = ROOT / p["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(build(p), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
