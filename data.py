# 타로 카드 데이터 (78장 전체)
TAROT_DECK = [
    # 메이저 아르카나 (22장)
    {'id': 0, 'name': '바보', 'nameEn': 'The Fool', 'suit': 'major', 'number': '0', 'planet': '천왕성', 'element': '공기', 'upright': '새로운 시작, 순수함, 모험, 자유로운 영혼', 'reversed': '무모함, 경솔함, 위험, 방향 상실'},
    {'id': 1, 'name': '마법사', 'nameEn': 'The Magician', 'suit': 'major', 'number': 'I', 'planet': '수성', 'element': '공기', 'upright': '의지력, 창조력, 기술, 집중력', 'reversed': '조작, 속임수, 재능 낭비, 자신감 부족'},
    {'id': 2, 'name': '여사제', 'nameEn': 'The High Priestess', 'suit': 'major', 'number': 'II', 'planet': '달', 'element': '물', 'upright': '직관, 신비, 내면의 목소리, 영적 통찰', 'reversed': '비밀, 단절, 무시된 직관, 표면적 지식'},
    {'id': 3, 'name': '여제', 'nameEn': 'The Empress', 'suit': 'major', 'number': 'III', 'planet': '금성', 'element': '흙', 'upright': '풍요, 양육, 풍부함, 자연과의 연결', 'reversed': '의존, 질식, 공허함, 창조성 부족'},
    {'id': 4, 'name': '황제', 'nameEn': 'The Emperor', 'suit': 'major', 'number': 'IV', 'planet': '양자리', 'element': '불', 'upright': '권위, 구조, 통제, 안정성', 'reversed': '독재, 경직성, 지배욕, 권위 남용'},
    {'id': 5, 'name': '교황', 'nameEn': 'The Hierophant', 'suit': 'major', 'number': 'V', 'planet': '황소자리', 'element': '흙', 'upright': '전통, 영적 지혜, 교육, 관습', 'reversed': '반항, 비정통, 제한, 독단적 사고'},
    {'id': 6, 'name': '연인', 'nameEn': 'The Lovers', 'suit': 'major', 'number': 'VI', 'planet': '쌍둥이자리', 'element': '공기', 'upright': '사랑, 조화, 선택, 가치관의 일치', 'reversed': '불균형, 부조화, 잘못된 선택, 갈등'},
    {'id': 7, 'name': '전차', 'nameEn': 'The Chariot', 'suit': 'major', 'number': 'VII', 'planet': '게자리', 'element': '물', 'upright': '의지, 승리, 결단력, 통제력', 'reversed': '방향 상실, 공격성, 통제 불능, 좌절'},
    {'id': 8, 'name': '힘', 'nameEn': 'Strength', 'suit': 'major', 'number': 'VIII', 'planet': '사자자리', 'element': '불', 'upright': '용기, 인내, 내면의 힘, 자제력', 'reversed': '자기 의심, 약함, 불안, 인내심 부족'},
    {'id': 9, 'name': '은둔자', 'nameEn': 'The Hermit', 'suit': 'major', 'number': 'IX', 'planet': '처녀자리', 'element': '흙', 'upright': '내면 탐구, 성찰, 지혜, 고독한 여정', 'reversed': '고립, 외로움, 철수, 현실 회피'},
    {'id': 10, 'name': '운명의 수레바퀴', 'nameEn': 'Wheel of Fortune', 'suit': 'major', 'number': 'X', 'planet': '목성', 'element': '불', 'upright': '변화, 운명, 행운, 순환', 'reversed': '불운, 저항, 정체, 통제 불가능한 변화'},
    {'id': 11, 'name': '정의', 'nameEn': 'Justice', 'suit': 'major', 'number': 'XI', 'planet': '천칭자리', 'element': '공기', 'upright': '공정함, 진실, 책임, 균형', 'reversed': '불공정, 책임 회피, 부정직, 편견'},
    {'id': 12, 'name': '매달린 사람', 'nameEn': 'The Hanged Man', 'suit': 'major', 'number': 'XII', 'planet': '해왕성', 'element': '물', 'upright': '항복, 새로운 관점, 희생, 정지', 'reversed': '지연, 저항, 정체, 무의미한 희생'},
    {'id': 13, 'name': '죽음', 'nameEn': 'Death', 'suit': 'major', 'number': 'XIII', 'planet': '전갈자리', 'element': '물', 'upright': '변화, 끝과 시작, 변형, 재생', 'reversed': '저항, 정체, 집착, 변화 거부'},
    {'id': 14, 'name': '절제', 'nameEn': 'Temperance', 'suit': 'major', 'number': 'XIV', 'planet': '궁수자리', 'element': '불', 'upright': '균형, 절제, 조화, 인내', 'reversed': '과잉, 불균형, 극단, 조급함'},
    {'id': 15, 'name': '악마', 'nameEn': 'The Devil', 'suit': 'major', 'number': 'XV', 'planet': '염소자리', 'element': '흙', 'upright': '속박, 중독, 물질주의, 욕망', 'reversed': '해방, 자유, 깨달음, 속박으로부터의 탈출'},
    {'id': 16, 'name': '탑', 'nameEn': 'The Tower', 'suit': 'major', 'number': 'XVI', 'planet': '화성', 'element': '불', 'upright': '갑작스런 변화, 파괴, 계시, 붕괴', 'reversed': '재난 회피, 두려움, 지연된 재앙, 내적 변화'},
    {'id': 17, 'name': '별', 'nameEn': 'The Star', 'suit': 'major', 'number': 'XVII', 'planet': '물병자리', 'element': '공기', 'upright': '희망, 영감, 평온, 치유', 'reversed': '절망, 신념 상실, 낙담, 방향 상실'},
    {'id': 18, 'name': '달', 'nameEn': 'The Moon', 'suit': 'major', 'number': 'XVIII', 'planet': '물고기자리', 'element': '물', 'upright': '환상, 두려움, 잠재의식, 직관', 'reversed': '혼란 해소, 진실, 명료함, 불안 감소'},
    {'id': 19, 'name': '태양', 'nameEn': 'The Sun', 'suit': 'major', 'number': 'XIX', 'planet': '태양', 'element': '불', 'upright': '기쁨, 성공, 긍정, 활력', 'reversed': '지연된 행복, 과도한 낙관, 현실 부정'},
    {'id': 20, 'name': '심판', 'nameEn': 'Judgement', 'suit': 'major', 'number': 'XX', 'planet': '명왕성', 'element': '불', 'upright': '각성, 갱신, 평가, 부활', 'reversed': '자책, 의심, 내면의 비판, 용서 못함'},
    {'id': 21, 'name': '세계', 'nameEn': 'The World', 'suit': 'major', 'number': 'XXI', 'planet': '토성', 'element': '흙', 'upright': '완성, 성취, 여행, 충족감', 'reversed': '미완성, 지연, 부족함, 목표 달성 실패'},
    
    # 완드 (불의 원소) - 14장
    {'id': 22, 'name': '완드 에이스', 'nameEn': 'Ace of Wands', 'suit': 'wands', 'element': '불', 'upright': '새로운 시작, 창조적 에너지, 영감, 잠재력', 'reversed': '지연된 시작, 창조성 부족, 좌절'},
    {'id': 23, 'name': '완드 2', 'nameEn': 'Two of Wands', 'suit': 'wands', 'element': '불', 'upright': '계획, 미래 전망, 결정, 발견', 'reversed': '두려움, 계획 부족, 결정 지연'},
    {'id': 24, 'name': '완드 3', 'nameEn': 'Three of Wands', 'suit': 'wands', 'element': '불', 'upright': '확장, 선견지명, 해외 기회, 진전', 'reversed': '지연, 좌절, 기회 상실'},
    {'id': 25, 'name': '완드 4', 'nameEn': 'Four of Wands', 'suit': 'wands', 'element': '불', 'upright': '축하, 조화, 가정, 안정', 'reversed': '불안정, 갈등, 축하 지연'},
    {'id': 26, 'name': '완드 5', 'nameEn': 'Five of Wands', 'suit': 'wands', 'element': '불', 'upright': '경쟁, 갈등, 긴장, 도전', 'reversed': '갈등 회피, 내적 갈등, 협력'},
    {'id': 27, 'name': '완드 6', 'nameEn': 'Six of Wands', 'suit': 'wands', 'element': '불', 'upright': '승리, 인정, 성공, 자신감', 'reversed': '지연된 성공, 자만, 실패'},
    {'id': 28, 'name': '완드 7', 'nameEn': 'Seven of Wands', 'suit': 'wands', 'element': '불', 'upright': '방어, 도전, 용기, 끈기', 'reversed': '포기, 압도됨, 불안'},
    {'id': 29, 'name': '완드 8', 'nameEn': 'Eight of Wands', 'suit': 'wands', 'element': '불', 'upright': '빠른 행동, 진전, 소식, 여행', 'reversed': '지연, 좌절, 서두름'},
    {'id': 30, 'name': '완드 9', 'nameEn': 'Nine of Wands', 'suit': 'wands', 'element': '불', 'upright': '회복력, 인내, 경계, 마지막 노력', 'reversed': '소진, 편집증, 포기'},
    {'id': 31, 'name': '완드 10', 'nameEn': 'Ten of Wands', 'suit': 'wands', 'element': '불', 'upright': '부담, 책임, 과중한 짐, 스트레스', 'reversed': '짐 내려놓기, 위임, 소진'},
    {'id': 32, 'name': '완드 페이지', 'nameEn': 'Page of Wands', 'suit': 'wands', 'element': '불', 'upright': '열정, 모험, 호기심, 새 소식', 'reversed': '조급함, 산만함, 계획 부족'},
    {'id': 33, 'name': '완드 나이트', 'nameEn': 'Knight of Wands', 'suit': 'wands', 'element': '불', 'upright': '행동, 열정, 모험, 충동', 'reversed': '무모함, 인내심 부족, 중단'},
    {'id': 34, 'name': '완드 퀸', 'nameEn': 'Queen of Wands', 'suit': 'wands', 'element': '불', 'upright': '자신감, 독립성, 결단력, 카리스마', 'reversed': '질투, 이기심, 공격성'},
    {'id': 35, 'name': '완드 킹', 'nameEn': 'King of Wands', 'suit': 'wands', 'element': '불', 'upright': '리더십, 비전, 기업가정신, 명예', 'reversed': '독단적, 무자비함, 통제욕'},
    
    # 컵 (물의 원소) - 14장
    {'id': 36, 'name': '컵 에이스', 'nameEn': 'Ace of Cups', 'suit': 'cups', 'element': '물', 'upright': '새로운 사랑, 감정, 직관, 영적 체험', 'reversed': '감정 억압, 사랑 거부, 공허함'},
    {'id': 37, 'name': '컵 2', 'nameEn': 'Two of Cups', 'suit': 'cups', 'element': '물', 'upright': '파트너십, 사랑, 조화, 연결', 'reversed': '불균형, 단절, 관계 긴장'},
    {'id': 38, 'name': '컵 3', 'nameEn': 'Three of Cups', 'suit': 'cups', 'element': '물', 'upright': '우정, 축하, 공동체, 기쁨', 'reversed': '과잉, 고립, 관계 문제'},
    {'id': 39, 'name': '컵 4', 'nameEn': 'Four of Cups', 'suit': 'cups', 'element': '물', 'upright': '무관심, 명상, 재평가, 권태', 'reversed': '새로운 기회, 각성, 동기'},
    {'id': 40, 'name': '컵 5', 'nameEn': 'Five of Cups', 'suit': 'cups', 'element': '물', 'upright': '상실, 슬픔, 후회, 실망', 'reversed': '회복, 용서, 앞으로 나아감'},
    {'id': 41, 'name': '컵 6', 'nameEn': 'Six of Cups', 'suit': 'cups', 'element': '물', 'upright': '향수, 순수함, 과거, 어린 시절', 'reversed': '과거에 얽매임, 현실 부정'},
    {'id': 42, 'name': '컵 7', 'nameEn': 'Seven of Cups', 'suit': 'cups', 'element': '물', 'upright': '선택, 환상, 백일몽, 가능성', 'reversed': '현실 직면, 결정, 명확성'},
    {'id': 43, 'name': '컵 8', 'nameEn': 'Eight of Cups', 'suit': 'cups', 'element': '물', 'upright': '떠남, 포기, 탐색, 성장', 'reversed': '두려움, 회피, 정체'},
    {'id': 44, 'name': '컵 9', 'nameEn': 'Nine of Cups', 'suit': 'cups', 'element': '물', 'upright': '만족, 소원 성취, 행복, 성공', 'reversed': '과잉, 탐욕, 불만족'},
    {'id': 45, 'name': '컵 10', 'nameEn': 'Ten of Cups', 'suit': 'cups', 'element': '물', 'upright': '가족 행복, 조화, 만족, 사랑', 'reversed': '가족 갈등, 불화, 이상 붕괴'},
    {'id': 46, 'name': '컵 페이지', 'nameEn': 'Page of Cups', 'suit': 'cups', 'element': '물', 'upright': '창의성, 직관, 호기심, 메시지', 'reversed': '감정 미숙, 비현실적'},
    {'id': 47, 'name': '컵 나이트', 'nameEn': 'Knight of Cups', 'suit': 'cups', 'element': '물', 'upright': '낭만, 매력, 상상력, 이상주의', 'reversed': '비현실적, 변덕, 실망'},
    {'id': 48, 'name': '컵 퀸', 'nameEn': 'Queen of Cups', 'suit': 'cups', 'element': '물', 'upright': '공감, 직관, 양육, 평온', 'reversed': '감정 불안정, 의존성'},
    {'id': 49, 'name': '컵 킹', 'nameEn': 'King of Cups', 'suit': 'cups', 'element': '물', 'upright': '감정 균형, 통제, 지혜, 외교술', 'reversed': '감정 조작, 냉담함'},
    
    # 검 (공기의 원소) - 14장
    {'id': 50, 'name': '검 에이스', 'nameEn': 'Ace of Swords', 'suit': 'swords', 'element': '공기', 'upright': '명확성, 진실, 돌파구, 정신적 명료함', 'reversed': '혼란, 잔인함, 무질서'},
    {'id': 51, 'name': '검 2', 'nameEn': 'Two of Swords', 'suit': 'swords', 'element': '공기', 'upright': '막힌 상황, 회피, 균형, 결정 지연', 'reversed': '결정, 혼란 해소, 정보'},
    {'id': 52, 'name': '검 3', 'nameEn': 'Three of Swords', 'suit': 'swords', 'element': '공기', 'upright': '상처, 슬픔, 배신, 고통', 'reversed': '회복, 용서, 치유'},
    {'id': 53, 'name': '검 4', 'nameEn': 'Four of Swords', 'suit': 'swords', 'element': '공기', 'upright': '휴식, 회복, 명상, 재충전', 'reversed': '소진, 불안, 정체'},
    {'id': 54, 'name': '검 5', 'nameEn': 'Five of Swords', 'suit': 'swords', 'element': '공기', 'upright': '갈등, 패배, 불명예, 승리의 대가', 'reversed': '화해, 용서, 극복'},
    {'id': 55, 'name': '검 6', 'nameEn': 'Six of Swords', 'suit': 'swords', 'element': '공기', 'upright': '전환, 이동, 회복, 탈출', 'reversed': '정체, 저항, 미해결 문제'},
    {'id': 56, 'name': '검 7', 'nameEn': 'Seven of Swords', 'suit': 'swords', 'element': '공기', 'upright': '속임수, 전략, 회피, 비밀', 'reversed': '진실, 정직, 책임'},
    {'id': 57, 'name': '검 8', 'nameEn': 'Eight of Swords', 'suit': 'swords', 'element': '공기', 'upright': '구속, 한계, 피해자 의식, 무력감', 'reversed': '해방, 자유, 통제 회복'},
    {'id': 58, 'name': '검 9', 'nameEn': 'Nine of Swords', 'suit': 'swords', 'element': '공기', 'upright': '불안, 두려움, 악몽, 걱정', 'reversed': '회복, 희망, 불안 해소'},
    {'id': 59, 'name': '검 10', 'nameEn': 'Ten of Swords', 'suit': 'swords', 'element': '공기', 'upright': '끝, 배신, 붕괴, 바닥', 'reversed': '회복, 재생, 최악의 끝'},
    {'id': 60, 'name': '검 페이지', 'nameEn': 'Page of Swords', 'suit': 'swords', 'element': '공기', 'upright': '호기심, 경계, 소식, 진실 추구', 'reversed': '소문, 무례함, 교활함'},
    {'id': 61, 'name': '검 나이트', 'nameEn': 'Knight of Swords', 'suit': 'swords', 'element': '공기', 'upright': '행동, 야망, 결단력, 충동', 'reversed': '무모함, 공격성, 서두름'},
    {'id': 62, 'name': '검 퀸', 'nameEn': 'Queen of Swords', 'suit': 'swords', 'element': '공기', 'upright': '독립성, 명확성, 솔직함, 지성', 'reversed': '냉담함, 잔인함, 편협함'},
    {'id': 63, 'name': '검 킹', 'nameEn': 'King of Swords', 'suit': 'swords', 'element': '공기', 'upright': '권위, 진실, 논리, 윤리', 'reversed': '조작, 잔인함, 냉혹함'},
    
    # 펜타클 (흙의 원소) - 14장
    {'id': 64, 'name': '펜타클 에이스', 'nameEn': 'Ace of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '새로운 기회, 풍요, 번영, 실용성', 'reversed': '기회 상실, 탐욕, 불안정'},
    {'id': 65, 'name': '펜타클 2', 'nameEn': 'Two of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '균형, 적응, 우선순위, 변화', 'reversed': '불균형, 압도됨, 혼란'},
    {'id': 66, 'name': '펜타클 3', 'nameEn': 'Three of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '협력, 기술, 팀워크, 학습', 'reversed': '불협화음, 자만, 기술 부족'},
    {'id': 67, 'name': '펜타클 4', 'nameEn': 'Four of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '통제, 안정, 보수성, 집착', 'reversed': '관대함, 불안정, 변화'},
    {'id': 68, 'name': '펜타클 5', 'nameEn': 'Five of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '어려움, 빈곤, 고립, 걱정', 'reversed': '회복, 지원, 향상'},
    {'id': 69, 'name': '펜타클 6', 'nameEn': 'Six of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '관대함, 자선, 균형, 공유', 'reversed': '빚, 이기심, 불공평'},
    {'id': 70, 'name': '펜타클 7', 'nameEn': 'Seven of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '인내, 투자, 평가, 장기 목표', 'reversed': '조급함, 낭비, 방향 상실'},
    {'id': 71, 'name': '펜타클 8', 'nameEn': 'Eight of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '기술, 헌신, 숙련, 노력', 'reversed': '완벽주의, 지루함, 낮은 품질'},
    {'id': 72, 'name': '펜타클 9', 'nameEn': 'Nine of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '독립, 풍요, 성공, 자급자족', 'reversed': '의존, 과시, 외로움'},
    {'id': 73, 'name': '펜타클 10', 'nameEn': 'Ten of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '유산, 부, 가족, 전통', 'reversed': '재정 손실, 가족 불화'},
    {'id': 74, 'name': '펜타클 페이지', 'nameEn': 'Page of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '야망, 학습, 기회, 계획', 'reversed': '게으름, 비현실적, 산만함'},
    {'id': 75, 'name': '펜타클 나이트', 'nameEn': 'Knight of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '책임감, 신뢰성, 근면, 인내', 'reversed': '정체, 게으름, 완벽주의'},
    {'id': 76, 'name': '펜타클 퀸', 'nameEn': 'Queen of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '양육, 실용성, 풍요, 안정', 'reversed': '물질주의, 질투, 불안정'},
    {'id': 77, 'name': '펜타클 킹', 'nameEn': 'King of Pentacles', 'suit': 'pentacles', 'element': '흙', 'upright': '풍요, 안정, 성공, 실용성', 'reversed': '탐욕, 완고함, 물질주의'},
]

# 스프레드 설정
SPREAD_CONFIG = {
    'one': {
        'name': '원 카드',
        'count': 1,
        'positions': ['오늘의 에너지'],
        'layout': 'row'  # ← row 사용!
    },
    'two': {
        'name': '투 카드',
        'count': 2,
        'positions': ['문제', '해결책'],
        'layout': 'row'  # ← row 사용!
    },
    'three': {
        'name': '쓰리 카드',
        'count': 3,
        'positions': ['과거', '현재', '미래'],
        'layout': 'row'  # ← row 사용!
    },
    'four': {
        'name': '포 카드',
        'count': 4,
        'positions': ['현재 상황', '장애물', '조언', '결과'],
        'layout': 'row'  # ← row 사용!
    },
    'cross': {
        'name': '크로스',
        'count': 5,
        'positions': ['현재 상황','도전/장애','과거의 영향','미래 흐름','조언/핵심 통찰'],
        'layout': 'cross'  # ← 특수 레이아웃
    },
    'celtic': {
        'name': '켈틱 크로스',
        'count': 10,
        'positions': ['현재', '도전', '과거', '미래', '위', '아래', '조언', '외부', '희망/두려움', '결과'],
        'layout': 'celtic'  # ← 특수 레이아웃
    }
}

# 슈트 색상
SUIT_COLORS = {
    'major': 'from-violet-400 to-purple-500',
    'wands': 'from-orange-400 to-red-500',
    'cups': 'from-blue-400 to-cyan-500',
    'swords': 'from-slate-400 to-gray-500',
    'pentacles': 'from-yellow-400 to-amber-500'
}

# 원소 아이콘
ELEMENTS = {
    '불': '🔥',
    '물': '💧',
    '공기': '🌪',
    '흙': '⛰'
}

# python -c "from data import TAROT_DECK; print(len(TAROT_DECK))"
# -> to check if data.py works
# -> must print 78