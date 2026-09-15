import streamlit as st

st.set_page_config(page_title="陶瓷電容換算計算機", page_icon="⚡")

st.title("⚡ 陶瓷電容換算計算機")

# 輸入區
code = st.text_input("請輸入電容代碼（如 102, 681, 104K）：", "").strip().upper()

if code:
    # 過濾掉結尾的誤差字母（如 K, J, M）
    clean_code = ''.join(filter(str.isdigit, code))
    
    if len(clean_code) == 3:
        digits = clean_code[:2]
        multiplier = int(clean_code[2])
        pf_val = int(digits) * (10 ** multiplier)
        
        uf_val = pf_val / 1_000_000
        nf_val = pf_val / 1_000
        
        st.success("✨ 換算結果：")
        col1, col2, col3 = st.columns(3)
        col1.metric("皮法 (pF)", f"{pf_val:,} pF")
        col2.metric("納法 (nF)", f"{nf_val:g} nF")
        col3.metric("微法 (µF)", f"{uf_val:g} µF")
    else:
        st.error("⚠️ 請輸入有效的 3 位數字電容代碼（例如 104）。")

st.markdown("---")

# 新增常用對照表
st.subheader("📋 常用陶瓷電容代碼對照表")
table_data = {
    "代碼": ["102", "103", "104", "222", "473", "681"],
    "pF (皮法)": ["1,000 pF", "10,000 pF", "100,000 pF", "2,200 pF", "47,000 pF", "680 pF"],
    "nF (納法)": ["1 nF", "10 nF", "100 nF", "2.2 nF", "47 nF", "0.68 nF"],
    "µF (微法)": ["0.001 µF", "0.01 µF", "0.1 µF", "0.0022 µF", "0.047 µF", "0.00068 µF"]
}
st.table(table_data)
