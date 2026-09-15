import streamlit as st

st.set_page_config(page_title="電子元件換算計算機", page_icon="⚡")

st.title("⚡ 電子元件換算計算機")

# 建立分頁
tab1, tab2 = st.tabs(["陶瓷電容換算", "電阻色環換算"])

# === 分頁一：陶瓷電容 ===
with tab1:
    st.subheader("陶瓷電容代碼換算")
    code = st.text_input("請輸入電容代碼（如 102, 681, 104K）：", "").strip().upper()

    if code:
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
    st.subheader("📋 常用陶瓷電容代碼對照表")
    table_data = {
        "代碼": ["102", "103", "104", "222", "473", "681"],
        "pF (皮法)": ["1,000 pF", "10,000 pF", "100,000 pF", "2,200 pF", "47,000 pF", "680 pF"],
        "nF (納法)": ["1 nF", "10 nF", "100 nF", "2.2 nF", "47 nF", "0.68 nF"],
        "µF (微法)": ["0.001 µF", "0.01 µF", "0.1 µF", "0.0022 µF", "0.047 µF", "0.00068 µF"]
    }
    st.table(table_data)

# === 分頁二：電阻色環 ===
with tab2:
    st.subheader("四色環電阻計算機")
    
    color_values = {
        "黑色 (0)": 0, "棕色 (1)": 1, "紅色 (2)": 2, 
        "橙色 (3)": 3, "黃色 (4)": 4, "綠色 (5)": 5, 
        "藍色 (6)": 6, "紫色 (7)": 7, "灰色 (8)": 8, "白色 (9)": 9
    }
    
    multipliers = {
        "黑色 (×1Ω)": 1, "棕色 (×10Ω)": 10, "紅色 (×100Ω)": 100, 
        "橙色 (×1kΩ)": 1000, "黃色 (×10kΩ)": 10000, "綠色 (×100kΩ)": 100000, 
        "藍色 (×1MΩ)": 1000000, "金色 (×0.1Ω)": 0.1, "銀色 (×0.01Ω)": 0.01
    }
    
    tolerances = {
        "棕色 (±1%)": 1, "紅色 (±2%)": 2, "綠色 (±0.5%)": 0.5, 
        "藍色 (±0.25%)": 0.25, "紫色 (±0.1%)": 0.1, "金色 (±5%)": 5, "銀色 (±10%)": 10
    }

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        b1 = st.selectbox("第一色環", list(color_values.keys()), index=1)
        b2 = st.selectbox("第二色環", list(color_values.keys()), index=0)
    with col_b2:
        b3 = st.selectbox("倍率 (第三色環)", list(multipliers.keys()), index=2)
        b4 = st.selectbox("誤差 (第四色環)", list(tolerances.keys()), index=5)

    val = (color_values[b1] * 10 + color_values[b2]) * multipliers[b3]
    
    if val >= 1_000_000:
        res_str = f"{val / 1_000_000:g} MΩ"
    elif val >= 1_000:
        res_str = f"{val / 1_000:g} kΩ"
    else:
        res_str = f"{val:g} Ω"
        
    st.success(f"✨ 計算阻值：**{res_str}** (誤差: {tolerances[b4]}%)")
