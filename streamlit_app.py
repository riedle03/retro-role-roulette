import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime
# 맨 위 import에 추가
from zoneinfo import ZoneInfo
KST = ZoneInfo("Asia/Seoul")  # 한국 표준시


# -------------------- 기본 설정 --------------------
st.set_page_config(
    page_title="픽셀 레트로 역할 룰렛",
    page_icon="🎮",
)

# 픽셀 아트 스타일
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
html, body, [class*="block-container"]{
  font-family: 'Press Start 2P', system-ui, sans-serif;
  background: #0f172a;
  color: #e5e7eb;
}
.retro-card{
  border: 4px solid #a78bfa;
  border-radius: 12px;
  padding: 18px;
  margin-top: 12px;
  background: linear-gradient(180deg, #0b1220, #111827);
  text-align: center;
}
.big-text {
  font-size: 20px;
  color: #22d3ee;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 픽셀 레트로 역할 룰렛")

# -------------------- 상태 초기화 --------------------
if "students" not in st.session_state:
    st.session_state.students = []
if "roles" not in st.session_state:
    st.session_state.roles = ["팀장", "서기", "자료 조사", "발표자", "시간 관리", "정리 담당"]
if "assignments" not in st.session_state:
    st.session_state.assignments = []

# -------------------- 학생/역할 입력 --------------------
with st.expander("📝 학생 & 역할 목록 입력"):
    student_input = st.text_area("학생 목록 (쉼표 또는 줄바꿈)", height=100)
    role_input = st.text_area("역할 목록 (쉼표 또는 줄바꿈)", 
                               value="팀장, 서기, 자료 조사, 발표자, 시간 관리, 정리 담당",
                               height=80)
    if st.button("목록 저장", type="primary"):
        if student_input.strip():
            st.session_state.students = [
                name.strip() for name in student_input.replace("\n", ",").split(",") if name.strip()
            ]
            st.session_state.roles = [
                role.strip() for role in role_input.replace("\n", ",").split(",") if role.strip()
            ]
            st.success(f"학생 {len(st.session_state.students)}명, 역할 {len(st.session_state.roles)}개 저장 완료!")

# -------------------- 룰렛 실행 --------------------
if st.session_state.students and st.session_state.roles:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎯 룰렛 돌리기", use_container_width=True):
            unassigned_students = [s for s in st.session_state.students if s not in [a["학생"] for a in st.session_state.assignments]]
            unassigned_roles = [r for r in st.session_state.roles if r not in [a["역할"] for a in st.session_state.assignments]]

            if not unassigned_students:
                st.warning("모든 학생이 배정되었습니다!")
            elif not unassigned_roles:
                st.warning("모든 역할이 배정되었습니다!")
            else:
                # 룰렛 GIF 표시
                gif_placeholder = st.empty()
                gif_placeholder.image("roulette_smooth.gif", use_container_width=True)
                time.sleep(2.5)  # GIF 재생 시간
                gif_placeholder.empty()

                # 최종 확정
                selected_student = random.choice(unassigned_students)
                selected_role = random.choice(unassigned_roles)
                # 배정시각 저장 부분 교체
                st.session_state.assignments.append({
                    "학생": selected_student,
                    "역할": selected_role,
                    "배정시각": datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S")
                })


                st.markdown(
                    f"<div class='retro-card'>"
                    f"🎉 <b>{selected_student}</b> 님 → <b>{selected_role}</b> 역할 확정!"
                    f"</div>",
                    unsafe_allow_html=True
                )

    with col2:
        if st.button("🔄 초기화", use_container_width=True):
            st.session_state.assignments = []
            st.success("배정 기록 초기화 완료!")

    # -------------------- 전체 배정 테이블 --------------------
    if st.session_state.assignments:
        df = pd.DataFrame(st.session_state.assignments)
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("💾 배정 결과 다운로드 (CSV)", csv, "assignments.csv", "text/csv")

else:
    st.info("먼저 학생과 역할 목록을 입력하세요.")

# 앱 코드 제일 마지막 부분에 추가
st.markdown(
    """
    <hr style="margin-top:50px; margin-bottom:10px; border: 1px solid #334155;">
    <div style='text-align: center; font-size: 12px; color: #94a3b8;'>
        © 2025 이대형. All rights reserved.<br>
        <a href="https://aicreatorz.netlify.app/" target="_blank" style="color:#22d3ee; text-decoration: none;">
            https://aicreatorz.netlify.app/
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
