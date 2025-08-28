# app_streamlit_intro.py
# -----------------------------------------------------------
# Streamlit 소개/학습 대시보드 (단일 파일)
# - 깃허브에 업로드 후 Streamlit Community Cloud에서 바로 배포
# - 섹션별 개념 설명 + 실습 위젯 + 코드 스니펫 + 공식 문서 링크
# -----------------------------------------------------------

import time
from pathlib import Path

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

# -----------------------------
# 기본 페이지 세팅
# -----------------------------
st.set_page_config(
    page_title="Streamlit 학습 대시보드",
    page_icon="🧊",
    layout="wide",
    menu_items={
        "Get help": "https://docs.streamlit.io/",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "This is a community learning dashboard made with Streamlit.",
    },
)

# 사이드바: 네비게이션
with st.sidebar:
    st.title("📚 Streamlit 학습")
    section = st.radio(
        "섹션 이동",
        [
            "1) 소개 & 시작하기",
            "2) 핵심 문법 살펴보기",
            "3) 레이아웃 & 구성요소",
            "4) 상태 관리 & 캐싱",
            "5) 데이터 시각화 맛보기",
            "6) 파일/이미지/폼",
            "7) 멀티페이지 & URL 파라미터",
            "8) 배포(Community Cloud)",
        ],
        index=0,
    )
    st.divider()
    st.caption(f"🔧 Streamlit version: **{st.__version__}**")
    st.markdown(
        """
**🔗 빠른 링크**
- 홈페이지: https://streamlit.io
- 문서: https://docs.streamlit.io
- 커뮤니티 클라우드: https://streamlit.io/cloud
- 깃허브: https://github.com/streamlit/streamlit
        """
    )

# 공통 유틸: 코드 블럭 토글
def code_box(title: str, code: str, language: str = "python"):
    with st.expander(f"📄 코드 보기: {title}", expanded=False):
        st.code(code, language=language)

# -----------------------------
# 1) 소개 & 시작하기
# -----------------------------
if section == "1) 소개 & 시작하기":
    st.title("🧊 Streamlit이란?")
    cols = st.columns([2, 1])
    with cols[0]:
        st.markdown(
            """
**Streamlit**은 **Python 코드만으로** 데이터 앱/대시보드를 **아주 빠르게** 만드는 오픈소스 프레임워크입니다.  
웹 프론트엔드(HTML/CSS/JS) 지식 없이도, 파이썬 스크립트를 인터랙티브 앱으로 바꿀 수 있어요.

**특징**
- 몇 줄의 코드로 위젯, 차트, 레이아웃 구성
- 파일 업로드/다운로드, 폼 입력, 상태 관리 지원
- `st.cache_data` 캐싱으로 빠른 재계산
- 깃허브 연동하여 **Community Cloud**에서 클릭 한 번으로 배포
            """
        )
    with cols[1]:
        st.info("🔗 공식 리소스")
        st.markdown(
            """
- [홈페이지 바로가기](https://streamlit.io)
- [문서 바로가기](https://docs.streamlit.io)
- [Community Cloud](https://streamlit.io/cloud)
- [GitHub Repo](https://github.com/streamlit/streamlit)
            """
        )

    st.subheader("설치 & 헬로월드")
    st.markdown("로컬에서 체험해 보세요:")
    code_box(
        "설치 및 실행",
        """# 설치
pip install streamlit

# 예제 실행 (Streamlit 내장 데모)
streamlit hello

# 새 앱 만들기
echo "import streamlit as st\nst.title('Hello, Streamlit!')" > app.py
streamlit run app.py
""",
        "bash",
    )

# -----------------------------
# 2) 핵심 문법 살펴보기
# -----------------------------
elif section == "2) 핵심 문법 살펴보기":
    st.title("🔤 핵심 문법(기본 API)")
    st.markdown(
        """
가장 자주 쓰는 함수/패턴을 미니 실습과 함께 익혀보세요.
- 출력: `st.write`, `st.markdown`, `st.title` …
- 위젯: `st.button`, `st.slider`, `st.selectbox`, `st.text_input` …
- 레이아웃: `st.columns`, `st.tabs`, `st.expander`
"""
    )

    demo_cols = st.columns(2)

    with demo_cols[0]:
        st.subheader("출력 & 위젯")
        name = st.text_input("이름을 입력하세요", value="Chloe")
        level = st.slider("학습 난이도", 1, 10, 3)
        ok = st.button("인사하기")
        if ok:
            st.success(f"안녕하세요, {name}님! 학습 난이도 {level}로 시작해볼게요 🙂")

        code_box(
            "기본 출력/위젯",
            """import streamlit as st

st.title("기본 예제")
name = st.text_input("이름을 입력하세요")
level = st.slider("학습 난이도", 1, 10, 3)
if st.button("인사하기"):
    st.success(f"안녕하세요, {name}님! 난이도 {level}로 시작!")
""",
        )

    with demo_cols[1]:
        st.subheader("탭/확장영역")
        t1, t2 = st.tabs(["탭 A", "탭 B"])
        with t1:
            st.write("탭 A 내용")
        with t2:
            st.write("탭 B 내용")

        with st.expander("확장해서 보기"):
            st.write("여기에 자세한 설명이나 코드 등을 넣습니다.")

        code_box(
            "레이아웃 예시",
            """t1, t2 = st.tabs(["탭 A", "탭 B"])
with t1:
    st.write("탭 A")
with t2:
    st.write("탭 B")

with st.expander("자세히"):
    st.write("추가 설명")
""",
        )

# -----------------------------
# 3) 레이아웃 & 구성요소
# -----------------------------
elif section == "3) 레이아웃 & 구성요소":
    st.title("📐 레이아웃 & 구성요소")
    st.markdown("컬럼 그리드, 컨테이너, 버튼/알림 등을 조합해 깔끔한 UI를 만듭니다.")

    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.metric("오늘 방문", 123)
    with c2:
        st.metric("전일 대비", "▲ 12%", delta_color="normal")
    with c3:
        st.metric("응답 시간(ms)", 87)

    st.divider()
    left, right = st.columns([2, 1])
    with left:
        st.info("컬럼 내부에 차트/표/텍스트 등 원하는 요소를 배치하세요.")
        df = pd.DataFrame({"x": np.arange(1, 11), "y": np.random.randint(10, 100, 10)})
        st.dataframe(df, use_container_width=True)
    with right:
        st.warning("알림 블록은 정보/경고/성공 등 상태 표현에 유용합니다.")

    code_box(
        "레이아웃 스니펫",
        """col1, col2, col3 = st.columns(3)
with col1: st.metric("A", 100)
with col2: st.metric("B", "▲ 7%")
with col3: st.metric("C", 42)

left, right = st.columns([2,1])
with left: st.dataframe(df)
with right: st.info("정보 블록")
""",
    )

# -----------------------------
# 4) 상태 관리 & 캐싱
# -----------------------------
elif section == "4) 상태 관리 & 캐싱":
    st.title("🧠 상태 관리 & ⚡ 캐싱")
    st.markdown(
        """
- **세션 상태**: `st.session_state`로 사용자 상호작용에 따라 값 유지  
- **캐싱**: 비싼 연산/데이터 로드를 `@st.cache_data`(데이터) / `@st.cache_resource`(리소스)에 캐시
"""
    )

    st.subheader("세션 상태 예제")
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    c_inc, c_dec, c_reset = st.columns(3)
    with c_inc:
        if st.button("➕ 증가"):
            st.session_state.counter += 1
    with c_dec:
        if st.button("➖ 감소"):
            st.session_state.counter -= 1
    with c_reset:
        if st.button("🔄 리셋"):
            st.session_state.counter = 0

    st.success(f"현재 값: {st.session_state.counter}")

    code_box(
        "세션 상태",
        """if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("증가"):
    st.session_state.counter += 1

st.write("카운터:", st.session_state.counter)
""",
    )

    st.subheader("캐싱 예제 (지연 시뮬레이션)")
    @st.cache_data(show_spinner=True)
    def slow_sum(n: int):
        time.sleep(1.5)
        return sum(range(n))

    n = st.slider("합계 범위", 1_000, 200_000, 50_000, step=5_000)
    with st.spinner("계산 중... (캐싱 후엔 매우 빠름)"):
        result = slow_sum(n)
    st.info(f"0부터 {n-1}까지의 합: **{result:,}**")

    code_box(
        "캐싱",
        """import time
@st.cache_data
def slow_fn(n):
    time.sleep(2)
    return n*n
""",
    )

# -----------------------------
# 5) 데이터 시각화 맛보기
# -----------------------------
elif section == "5) 데이터 시각화 맛보기":
    st.title("📊 데이터 & 차트")
    st.markdown("Streamlit 내장 차트 + Altair/Plotly 등 시각화 라이브러리와 잘 어울립니다.")

    # 샘플 데이터
    x = np.arange(0, 100)
    data = pd.DataFrame(
        {
            "x": x,
            "sin": np.sin(x / 10),
            "cos": np.cos(x / 10),
        }
    )

    t_line, t_alt = st.tabs(["line_chart", "Altair"])

    with t_line:
        st.write("간단한 line_chart")
        st.line_chart(data.set_index("x"))

    with t_alt:
        st.write("Altair 라인 차트")
        chart = (
            alt.Chart(data)
            .mark_line()
            .encode(x="x", y="sin")
            .properties(height=300)
        )
        st.altair_chart(chart, use_container_width=True)

    code_box(
        "차트 스니펫",
        """st.line_chart(df)  # 간단
# Altair 예시
import altair as alt
chart = alt.Chart(df).mark_bar().encode(x="x", y="y")
st.altair_chart(chart, use_container_width=True)
""",
    )

# -----------------------------
# 6) 파일/이미지/폼
# -----------------------------
elif section == "6) 파일/이미지/폼":
    st.title("📁 파일 · 🖼 이미지 · 📝 폼")
    up_col, img_col = st.columns(2)
    with up_col:
        st.subheader("파일 업로드")
        up = st.file_uploader("CSV 파일 업로드", type=["csv"])
        if up:
            df = pd.read_csv(up)
            st.success(f"업로드 완료! shape = {df.shape}")
            st.dataframe(df.head(), use_container_width=True)

    with img_col:
        st.subheader("이미지 표시")
        st.image(
            "https://static.streamlit.io/examples/dog.jpg",
            caption="예시 이미지 (공식 샘플)",
        )

    st.divider()
    st.subheader("폼(유효성 검사 예시)")
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            uname = st.text_input("이름*", placeholder="홍길동")
        with c2:
            email = st.text_input("이메일*", placeholder="you@example.com")
        msg = st.text_area("메시지", placeholder="문의 내용을 적어주세요")
        agree = st.checkbox("개인정보 수집 및 이용에 동의합니다.")
        submitted = st.form_submit_button("제출")
        if submitted:
            if not (uname and email and agree):
                st.error("필수 항목을 확인해주세요 (이름/이메일/동의).")
            else:
                st.success("제출 완료! 감사합니다.")

    code_box(
        "파일/폼 스니펫",
        """up = st.file_uploader("CSV", type=["csv"])
if up:
    df = pd.read_csv(up)
    st.dataframe(df)

with st.form("f"):
    name = st.text_input("이름*")
    ok = st.form_submit_button("제출")
""",
    )

# -----------------------------
# 7) 멀티페이지 & URL 파라미터
# -----------------------------
elif section == "7) 멀티페이지 & URL 파라미터":
    st.title("🧭 멀티페이지 & URL 파라미터")
    st.markdown(
        """
- **멀티페이지**: 프로젝트 루트에 `pages/` 폴더를 만들고 `.py` 파일을 추가하면 자동으로 페이지가 생깁니다.  
- **쿼리 파라미터**: `st.query_params`로 URL 파라미터 읽기/쓰기
"""
    )

    qp = st.query_params  # Streamlit 1.32+에서 제공
    st.info(f"현재 URL 파라미터: `{dict(qp)}`")

    st.subheader("파라미터 쓰기 데모")
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        new_name = st.text_input("name 파라미터", qp.get("name", [""])[0])
        if st.button("적용하기"):
            st.query_params.update({"name": new_name})
            st.rerun()
    with p_col2:
        if st.button("파라미터 초기화"):
            st.query_params.clear()
            st.rerun()

    code_box(
        "URL 파라미터",
        """# 읽기
qp = st.query_params
st.write(dict(qp))

# 쓰기/업데이트
st.query_params.update({"tab": "overview"})
st.rerun()
""",
    )

    code_box(
        "멀티페이지 구조",
        """my_app/
├─ app.py            # 메인
└─ pages/
   ├─ 1_데이터_탭.py
   └─ 2_모델_탭.py
# -> 실행 시 사이드바에 자동으로 페이지가 나타납니다.
""",
        "text",
    )

# -----------------------------
# 8) 배포(Community Cloud)
# -----------------------------
elif section == "8) 배포(Community Cloud)":
    st.title("🚀 배포: Streamlit Community Cloud")
    st.markdown(
        """
**가장 쉬운 배포 방법**
1. 깃허브에 이 파일(`app_streamlit_intro.py`)과 `requirements.txt`를 올립니다.  
2. [streamlit.io/cloud](https://streamlit.io/cloud)에 **GitHub** 계정으로 로그인  
3. **Create app** → 레포/브랜치/엔트리포인트(`app_streamlit_intro.py`) 선택 → **Deploy**

**팁**
- 의존성은 `requirements.txt`에 명시 (예: streamlit, pandas, numpy, altair)
- 앱이 느리면 `@st.cache_data` / `@st.cache_resource`로 캐싱 적용
- 로그 확인/재시작/비밀값 관리 등은 Cloud의 앱 관리 화면에서 수행
"""
    )

    code_box(
        "requirements.txt 예시",
        """streamlit>=1.29
pandas>=1.5
numpy>=1.23
altair>=5.0
""",
        "text",
    )

    st.success("모두 준비되었습니다! 깃허브에 올리고 Community Cloud에서 바로 배포해 보세요 🙌")

# -----------------------------
# 푸터
# -----------------------------
st.divider()
st.caption(
    "Made with ❤️ for learning Streamlit.  |  참고: 공식 홈페이지/문서/Community Cloud 가이드"
)
