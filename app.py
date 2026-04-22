import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="STP | Triagem Preditiva", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #161A23; border-radius: 12px; border: 1px solid #2D3748; padding: 20px; }
    .neon-green { color: #00E676; font-weight: bold; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .sub-text { color: #A0AEC0; font-size: 0.9rem; margin-bottom: 15px; }
    div[role="radiogroup"] > label { margin-bottom: 5px; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# MOTOR DE REGRAS (O CÉREBRO)
# ==========================================
def calcular_risco_lesao(carga, sono, fadiga, historico, dor_atual, mobilidade, descanso):
    pontuacao = 0
    gatilhos = []
    
    # Detecção Inteligente de Alertas (Red Flags)
    tipo_alerta = None 
    if dor_atual != "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "CRITICO_DOR_MOBILIDADE"
    elif dor_atual == "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "AVISO_SÓ_MOBILIDADE"

    # Avaliação de Variáveis (ATUALIZADO COM OS PESOS DO TCC)
    if carga == "Pico Súbito (Muito acima do normal)":
        pontuacao += 3
        gatilhos.append("Pico Súbito de Carga")
    elif carga == "Aumento Leve":
        pontuacao += 1
        gatilhos.append("Leve aumento de volume")
        
    if sono == "menos que 6":
        pontuacao += 2
        gatilhos.append("Sono Insuficiente (< 6h)")
    elif sono == "de 10 a 12":
        pontuacao += 1
        gatilhos.append("Recuperação prolongada (10-12h)")
        
    if fadiga == "Exaustão / Muito Cansado":
        pontuacao += 2
        gatilhos.append("Nível alto de fadiga")
    elif fadiga == "Cansaço Leve":
        pontuacao += 1
        gatilhos.append("Fadiga residual")
        
    if historico == "Sim":
        pontuacao += 1  # CORRIGIDO PARA +1
        gatilhos.append("Histórico Lesivo")

    if dor_atual == "Dor Aguda / Limitante":
        pontuacao += 3  # CORRIGIDO PARA +3
        gatilhos.append("Dor Aguda")
    elif dor_atual == "Leve Desconforto":
        pontuacao += 1
        gatilhos.append("Desconforto")

    if mobilidade == "Restrita / Encurtamento":
        pontuacao += 2  # CORRIGIDO PARA +2
        gatilhos.append("Mobilidade Restrita")

    if descanso == "Treinos consecutivos sem pausa":
        pontuacao += 1
        gatilhos.append("Falta de descanso")

    # Diagnóstico Final
    if pontuacao <= 3:
        risco = "RISCO BAIXO"
        cor = "normal"
        justificativa = "Sinais estáveis. Treino liberado. ✅" if pontuacao == 0 else f"Atenção leve: {', '.join(gatilhos)}. 🟡"
    elif pontuacao <= 6:
        risco = "RISCO MÉDIO"
        cor = "off"
        justificativa = f"Alerta Laranja: Risco moderado ativado por {', '.join(gatilhos)}. 🟠"
    else:
        risco = "RISCO ALTO"
        cor = "inverse"
        justificativa = f"ALERTA CRÍTICO: Risco gerado por {', '.join(gatilhos)}. 🔴"

    return risco, pontuacao, justificativa, cor, tipo_alerta

# ==========================================
# INTERFACE VISUAL (DASHBOARD)
# ==========================================
st.markdown("<h1 style='text-align: center;'><span class='neon-green'>🎯</span> STP: Sistema de Triagem Preditiva 🏃‍♂️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;' class='sub-text'>Avaliação Inteligente de Risco de Lesão Desportiva 📊</p>", unsafe_allow_html=True)

col_esq, col_espaco, col_dir = st.columns([1.5, 0.1, 1])

with col_esq:
    st.markdown("### 📋 Variáveis Fisiológicas e Biomecânicas")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("**1. Frequência e Intensidade (Carga) ⚡**")
            carga_val = st.radio("Carga", ["Habitual (Estável)", "Aumento Leve", "Pico Súbito (Muito acima do normal)"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**2. Nível de Fadiga 🔋**")
            fadiga_val = st.radio("Fadiga", ["Recuperado", "Cansaço Leve", "Exaustão / Muito Cansado"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**3. Dor Atual 💥**")
            dor_val = st.radio("Dor", ["Nenhuma", "Leve Desconforto", "Dor Aguda / Limitante"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**4. Histórico de Lesão (6 meses) 🏥**")
            hist_val = st.radio("Histórico", ["Não", "Sim"], horizontal=True, label_visibility="collapsed")

        with c2:
            st.markdown("**5. Qualidade do Sono 🛌**")
            sono_val = st.radio("Sono", ["menos que 6", "de 7 a 9", "de 10 a 12"], index=1, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**6. Mobilidade 🤸**")
            mob_val = st.radio("Mobilidade", ["Normal / Livre", "Restrita / Encurtamento"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**7. Descanso ⏳**")
            desc_val = st.radio("Descanso", ["Dias de descanso respeitados", "Treinos consecutivos sem pausa"], label_visibility="collapsed")
            
    btn_analisar = st.button("GERAR DIAGNÓSTICO", type="primary", use_container_width=True)

with col_dir:
    st.markdown("### 🎯 Resultado da Triagem")
    if btn_analisar:
        risco, pontos, justificativa, cor, tipo_alerta = calcular_risco_lesao(carga_val, sono_val, fadiga_val, hist_val, dor_val, mob_val, desc_val)
        
        with st.container(border=True):
            st.metric(label="Status de Risco Atual", value=risco, delta=f"{pontos} Pontos de Sobrecarga", delta_color=cor)
            st.divider()
            
            # Avisos Clínicos
            if tipo_alerta == "CRITICO_DOR_MOBILIDADE":
                st.error("🚨 **ALERTA CLÍNICO:** A combinação de dores com problemas na mobilidade indica uma possível lesão instalada. **Recomendamos que suspenda os treinos e procure avaliação de um profissional de saúde.**")
            elif tipo_alerta == "AVISO_SÓ_MOBILIDADE":
                st.warning("⚠️ **AVISO PREVENTIVO:** Você relatou uma restrição de mobilidade. Mesmo sem dor, treinar com encurtamentos ou perda de função altera a biomecânica. **Considere a avaliação de um profissional de saúde/fisioterapeuta.**")
            
            st.markdown("#### 🧠 Justificativa Técnica do Modelo")
            if risco == "RISCO BAIXO":
                st.success(justificativa)
            elif risco == "RISCO MÉDIO":
                st.warning(justificativa)
            else:
                st.error(justificativa)
                
            st.markdown("<br><div class='sub-text'>🔍 <i>Modelo baseado nas variáveis oficiais da metodologia do projeto de graduação.</i></div>", unsafe_allow_html=True)
    else:
        with st.container(border=True):
            st.info("⏳ Aguardando submissão...")
            st.write("Preencha as 7 variáveis oficiais à esquerda para obteres a triagem de risco completa.")