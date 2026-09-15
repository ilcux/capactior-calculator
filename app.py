import re
import streamlit as st

# 誤差代碼對照表
TOLERANCE_MAP = {
    'B': '±0.1 pF',
    'C': '±0.25 pF',
    'D': '±0.5 pF',
    'F': '±1%',
    'G': '±2%',
    'J': '±5%',
    'K': '±10%',
    'M': '±20%',
    'Z': '+80%, -20%',
}

st.title('⚡ 陶瓷電容換算計算機')

# 輸入框
code = st.text_input(
    '請輸入電容代碼（如 102, 681, 104K）：', ''
).upper().strip()

if code:
    # 匹配三位數字 + 可選的英文字母
    match = re.match(r'^(\d)(\d)(\d)([BCDFGJKMZ])?$', code)

    if match:
        d1, d2, mult, tol = match.groups()
        pf_value = (int(d1) * 10 + int(d2)) * (10 ** int(mult))
        nf_value = pf_value / 1000
        uf_value = pf_value / 1000000

        # 顯示換算結果
        st.success('換算成功！')
        col1, col2, col3 = st.columns(3)
        col1.metric('皮法拉 (pF)', f'{pf_value:,} pF')
        col2.metric('納法拉 (nF)', f'{nf_value:g} nF')
        col3.metric('微法拉 (µF)', f'{uf_value:g} µF')

        # 顯示誤差
        tol_text = (
            f'{tol} ({TOLERANCE_MAP[tol]})'
            if tol
            else '未標示 (無)'
        )
        st.info(f'**容許誤差**：{tol_text}')
    else:
        st.error('❌ 格式錯誤！請輸入 3 位數字，如 102 或 104K')

        