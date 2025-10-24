// 페이지 로드 시 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    // 모든 애니메이션 요소에 순차적으로 나타나는 효과 추가
    const animatedElements = document.querySelectorAll('.animate-fade-in');
    animatedElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 0.1}s`;
    });

    // 카드에 호버 사운드 효과 (옵션)
    const cards = document.querySelectorAll('.tarot-card, .spread-card, .card-guide');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });

    // 카드 클릭 시 확대 효과
    const tarotCards = document.querySelectorAll('.tarot-card');
    tarotCards.forEach(card => {
        card.addEventListener('click', function() {
            this.style.transform = 'scale(1.1)';
            setTimeout(() => {
                this.style.transform = '';
            }, 300);
        });
    });

    // 부드러운 스크롤
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 카드 뽑기 버튼 클릭 시 로딩 효과
    const drawButtons = document.querySelectorAll('a[href*="/draw"]');
    drawButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // 로딩 오버레이 생성
            const overlay = document.createElement('div');
            overlay.className = 'fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50';
            overlay.innerHTML = `
                <div class="text-center">
                    <div class="loading mb-4"></div>
                    <p class="text-white text-xl font-semibold">카드를 섞는 중...</p>
                </div>
            `;
            document.body.appendChild(overlay);
        });
    });

    // 네비게이션 활성 상태 표시
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('text-purple-600', 'font-bold');
        }
    });

    // 스크롤 시 헤더에 그림자 추가
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 10) {
            header.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '';
        }
    });

    // 터치 디바이스 감지 및 호버 효과 조정
    if ('ontouchstart' in window) {
        document.body.classList.add('touch-device');
        const hoverElements = document.querySelectorAll('.tarot-card, .spread-card');
        hoverElements.forEach(element => {
            element.addEventListener('touchstart', function() {
                this.style.transform = 'scale(0.95)';
            });
            element.addEventListener('touchend', function() {
                this.style.transform = '';
            });
        });
    }

    // 키보드 단축키
    document.addEventListener('keydown', function(e) {
        // ESC 키로 홈으로 돌아가기
        if (e.key === 'Escape' && window.location.pathname !== '/') {
            window.location.href = '/';
        }
        // G 키로 도감 열기
        if (e.key === 'g' || e.key === 'G') {
            window.location.href = '/guide';
        }
        // H 키로 홈 가기
        if (e.key === 'h' || e.key === 'H') {
            window.location.href = '/';
        }
    });
});

// 콘솔에 디버그 정보 출력
console.log('🌙 타로 리딩 앱이 로드되었습니다.');
console.log('단축키: H(홈), G(도감), ESC(뒤로가기)');