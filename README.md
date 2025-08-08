
# 🎮 Retro Role Roulette

**픽셀 아트 레트로 룰렛** 스타일의 **1인 1역할 랜덤 배정기**입니다.  
학급, 모임, 프로젝트 팀에서 **중복 없이 역할을 랜덤 배정**할 수 있으며,  
클릭 시 **부드러운 룰렛 GIF 애니메이션**이 재생되어 게임처럼 즐길 수 있습니다.

![roulette](roulette_smooth.gif)

---

## ✨ 주요 기능
- 🕹 **픽셀 아트 레트로 UI** (Press Start 2P 폰트 + 8비트 감성)
- 🎯 **중복 없는 역할 배정** (학생과 역할 목록을 입력하면 1:1 매칭)
- 🎰 **GIF 룰렛 애니메이션** (버튼 클릭 시 2.5초 재생 후 결과 표시)
- 📋 배정 결과 **테이블**로 확인 가능
- 💾 결과 **CSV 다운로드** 가능
- 🔄 **초기화**로 재시작 가능

---

## 📂 프로젝트 구조
```

repo-root/
├── streamlit\_app.py       # 메인 앱 코드
├── roulette\_smooth.gif    # 부드러운 룰렛 GIF
├── requirements.txt       # 필요 패키지 목록
├── README.md
└── docs/
└── screenshot.png     # 실행 화면 캡처 (선택)

````

---

## 🛠 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/username/retro-role-roulette.git
cd retro-role-roulette
````

### 2. 가상환경 (선택)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

`requirements.txt` 내용:

```
streamlit>=1.36.0
pandas
```

### 4. 앱 실행

```bash
streamlit run streamlit_app.py
```

---

## 📖 사용 방법

1. **학생 목록**과 **역할 목록**을 입력합니다.
   (쉼표 또는 줄바꿈으로 구분)
2. `🎯 룰렛 돌리기` 버튼 클릭 → 2.5초 동안 **룰렛 GIF 재생**
3. 애니메이션 종료 후 **학생 → 역할** 확정
4. 테이블에서 전체 배정 확인
5. 필요하면 **CSV로 다운로드**
6. `🔄 초기화` 버튼으로 새 게임 시작

---

## 🎯 예시 화면

| 학생 & 역할 입력            | 룰렛 재생                    | 결과 표시                  |
| --------------------- | ------------------------ | ---------------------- |
| ![입력](docs/input.png) | ![룰렛](docs/roulette.gif) | ![결과](docs/result.png) |

---

## 🧩 커스터마이징

* **역할 목록 변경**: 앱 실행 후 텍스트 입력창 수정
* **룰렛 속도 변경**: `time.sleep(2.5)` 값 수정
* **GIF 교체**: `roulette_smooth.gif` 파일을 다른 디자인으로 교체
* **UI 색상 변경**: 상단 CSS 코드에서 색상 변수 수정

---

## ⚠️ 주의사항

* 웹 브라우저에서 실행되며, 학생/역할 데이터는 서버에 저장되지 않습니다.
* GIF 애니메이션은 Streamlit에서 **일시정지 없이 전체 재생**됩니다.

---

## 📜 라이선스

MIT License
자유롭게 수정, 배포 가능합니다.

```
