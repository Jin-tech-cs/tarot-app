# 브라우저에서 http://localhost:5000
#
# 1. 브라우저 -> flask 서버 (app.py) 접속
#
# 2. flask 서버가 요청을 받음 (app.py → templates/home.html 렌더링)
# (app.py)
# @app.route('/')  # ← "/" 주소로 접속하면
# def home():
#   return render_template('home.html')  # ← home.html 파일을 보여줌
#
# 3. HTML 파일 렌더링
# <!-- home.html -->
# {% extends "base.html" %}  <!-- ← base.html을 기본 틀로 사용 -->
# {% block content %}
#    <!-- 여기에 홈 페이지 내용 -->
# {% endblock %}
#
# (흐름)
# home.html
#  ↓ (extends)
# base.html ← 헤더, 네비게이션 포함
#  ↓ (link)
# style.css ← 디자인 적용
#  ↓ (script)
# script.js ← 인터랙션 추가
#
# 4. 사용자가 카드뽑기 클릭
# <!-- home.html -->
# <a href="/draw?spread=one">카드 뽑기</a>
#
# (흐름) 원카드 옵션 클릭 → /draw?spread=one 요청
#
# 5. Flask 서버가 요청을 받음 (app.py → templates/draw.html 렌더링)
# (app.py)
# @app.route('/draw')
# def draw():
#    spread_type = request.args.get('spread', 'one')  # ← URL에서 'one' 가져옴
#    
#    # data.py에서 데이터 가져오기
#    from data import TAROT_DECK, SPREAD_CONFIG
#    
#    # 카드 섞기
#    deck = TAROT_DECK.copy()  # ← data.py의 78장 카드
#    random.shuffle(deck)
#    drawn_cards = deck[:3]  # ← 3장 뽑기
#    
#    # draw.html에 데이터 전달
#    return render_template('draw.html', cards=drawn_cards)
#
# (흐름)
# app.py
#  ↓ (import)
# data.py ← 78장 카드 데이터
#  ↓ (shuffle & draw)
# app.py ← 카드 3장 선택
#   ↓ (render)
# draw.html ← 카드 데이터 전달
#
# 6. draw.html에서 카드 표시
# <!-- draw.html -->
# {% for card in cards %}  <!-- ← app.py에서 받은 cards -->
#    <div class="tarot-card">
#        <h3>{{ card.name }}</h3>  <!-- ← "바보" -->
#        <p>{{ card.upright }}</p>  <!-- ← "새로운 시작..." -->
#    </div>
# {% endfor %}
#
# (흐름)
# app.py의 cards 데이터
#  ↓ (Jinja2 템플릿)
# draw.html ← {{ card.name }} 자리에 실제 값 삽입
#  ↓ (CSS)
# style.css ← .tarot-card 스타일 적용
#  ↓ (JS)
# script.js ← 호버 효과, 클릭 이벤트

'''
┌─────────────────────────────────────────────────┐
│                   브라우저                        │
│  http://localhost:5000                          │
└────────────────┬────────────────────────────────┘
                 │ HTTP 요청
                 ↓
┌─────────────────────────────────────────────────┐
│              app.py (Flask 서버)                 │
│  - 라우팅 (@app.route)                            │
│  - 데이터 처리 (카드 섞기)                           │
│  - HTML 렌더링                                    │
└───────┬──────────────────────┬──────────────────┘
        │                      │
        ↓                      ↓
┌──────────────┐      ┌──────────────┐
│   data.py    │      │  templates/  │
│ - 카드 데이터   │      │ - base.html  │
│ - 스프레드     │      │  - home.html │
│ - 색상 설정    │      │  - draw.html │
└──────────────┘      │  - guide.html│
                      └───────┬──────┘
                              │
                              ↓
                      ┌──────────────┐
                      │   static/    │
                      │  - style.css │
                      │  - script.js │
                      └──────────────┘
'''

'''
data.py 
  ↓
TAROT_DECK = [카드 78장] ───┐
SPREAD_CONFIG = {...}       │
SUIT_COLORS = {...}         │
                            │ import
                            ↓
                         app.py
                            │ shuffle & select
                            ↓
                    drawn_cards = [카드3장]
                            │ render_template
                            ↓
                        draw.html
                            │ {{ card.name }}
                            ↓
                        브라우저에 표시
                            │
                            ↓ (CSS 적용)
                        style.css
                            │
                            ↓ (JS 효과)
                        script.js
'''

''' 
핵심 개념

# Jinja2 템플릿 엔진
Python 데이터를 HTML에 삽입:

python
# app.py
return render_template('draw.html', name="바보")

html
<!-- draw.html -->
<h1>{{ name }}</h1>  ← "바보"로 변환됨

# 템플릿 상속
html
<!-- base.html: 공통 부분 -->
<header>헤더</header>
{% block content %}{% endblock %}
<footer>푸터</footer>

<!-- home.html: 내용만 채움 -->
{% extends "base.html" %}
{% block content %}
    <h1>홈 페이지</h1>
{% endblock %}
'''

'''
app.py     | 서버, 로직 처리 | 두뇌 (명령 내림)
data.py    | 데이터 저장소   | 도서관 (정보 보관)
base.html  | 기본 틀       | 건물 뼈대
home.html  | 홈 페이지      | 현관
draw.html  | 결과 페이지    | 메인 무대
guide.html | 도감 페이지    | 백과사전
style.css  | 디자인        | 인테리어
script.js  | 인터랙션       | 전기 배선
'''

from flask import Flask, render_template, request
import random
from data import TAROT_DECK, SPREAD_CONFIG, SUIT_COLORS, ELEMENTS

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/draw')
def draw():
    spread_type = request.args.get('spread', 'one')
    spread_config = SPREAD_CONFIG.get(spread_type, SPREAD_CONFIG['one'])
    
    # 카드 섞고 뽑기
    deck = TAROT_DECK.copy()
    random.shuffle(deck)
    drawn_cards = deck[:spread_config['count']]
    
    # 역방향 랜덤 설정
    for card in drawn_cards:
        is_reversed = random.choice([True, False])
        card['is_reversed'] = is_reversed
        card['meaning'] = card['reversed'] if is_reversed else card['upright']
        
        # if is_reversed: 
        #   card['meaning'] = card['reversed']
        # else:
        #   card['meaning'] = card['upright']
    
    return render_template(
        'draw.html',
        spread_name=spread_config['name'],
        spread_layout=spread_config['layout'],
        cards=drawn_cards,
        positions=spread_config['positions'],
        suit_colors=SUIT_COLORS,
        elements=ELEMENTS
    )

@app.route('/guide')
def guide():
    return render_template(
        'guide.html',
        cards=TAROT_DECK,
        suit_colors=SUIT_COLORS,
        elements=ELEMENTS
    )

@app.route('/history')  # 히스토리 페이지 추가 요망
def history():
    return render_template('history.html')

''' (for localhosting)
if __name__ == '__main__':
    print("🌙 타로 앱 실행 중...")
    print("👉 브라우저에서 http://127.0.0.1:5001 열기") # 원래 (5000)
    app.run(host="0.0.0.0", port=5001, debug=True) # 원래 (port=5000, debug=True)
'''

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

