import streamlit as st
import time

# ==========================================
# CONFIGURAÇÃO DA PÁGINA E ESTILOS
# ==========================================
st.set_page_config(page_title="STP | Triagem Preditiva", page_icon="🎯", layout="wide") 

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    [data-testid="stForm"], [data-testid="stVerticalBlockBorderWrapper"] { background-color: #161A23; border-radius: 12px; border: 1px solid #2D3748; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .neon-green { color: #00E676; font-weight: bold; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .sub-text { color: #A0AEC0; font-size: 0.9rem; margin-bottom: 15px; }
    div[role="radiogroup"] > label { margin-bottom: 5px; font-size: 0.85rem; }
    [data-testid="stTabs"] button { font-size: 1rem; font-weight: 600; padding-bottom: 10px; }
    [data-testid="stTabs"] button[aria-selected="true"] { color: #00E676 !important; border-bottom-color: #00E676 !important; }
    .footer { text-align: center; color: #4A5568; font-size: 0.85rem; margin-top: 50px; padding-top: 20px; border-top: 1px solid #2D3748; }
    .raiox-item { font-size: 0.9rem; margin-bottom: -10px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# MOTOR DE REGRAS (O CÉREBRO - INTACTO)
# ==========================================
def calcular_risco_lesao(carga, sono, fadiga, historico, dor_atual, mobilidade, descanso):
    pontuacao = 0
    gatilhos = []
    
    tipo_alerta = None 
    if dor_atual != "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "CRITICO_DOR_MOBILIDADE"
    elif dor_atual == "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "AVISO_SÓ_MOBILIDADE"

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
        pontuacao += 1  
        gatilhos.append("Histórico Lesivo")

    if dor_atual == "Dor Aguda / Limitante":
        pontuacao += 3  
        gatilhos.append("Dor Aguda")
    elif dor_atual == "Leve Desconforto":
        pontuacao += 1
        gatilhos.append("Desconforto")

    if mobilidade == "Restrita / Encurtamento":
        pontuacao += 2  
        gatilhos.append("Mobilidade Restrita")

    if descanso == "Treinos consecutivos sem pausa":
        pontuacao += 1
        gatilhos.append("Falta de descanso")

    if pontuacao <= 3:
        risco = "BAIXO"
        cor = "normal"
        justificativa = "Sinais estáveis. Treino liberado." if pontuacao == 0 else f"Atenção leve: {', '.join(gatilhos)}."
    elif pontuacao <= 6:
        risco = "MÉDIO"
        cor = "off"
        justificativa = f"Risco moderado ativado por {', '.join(gatilhos)}."
    else:
        risco = "ALTO"
        cor = "inverse"
        justificativa = f"Risco crítico gerado por {', '.join(gatilhos)}."

    return risco, pontuacao, justificativa, cor, tipo_alerta

# ==========================================
# MENU LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8112/8112613.png", width=80) 
    st.markdown("## Sobre o STP")
    st.write("O **Sistema de Triagem Preditiva** é um protótipo focado na transparência e interpretabilidade de dados em saúde desportiva.")
    st.divider()
    st.markdown("### 📌 Instruções:")
    st.markdown("""
    1. Identifique o Atleta no campo superior.
    2. Preencha os parâmetros nas abas.
    3. Clique em **Gerar Laudo**.
    4. Analise o Raio-X do Atleta.
    5. Siga o Plano de Intervenção sugerido.
    """)
    st.divider()
    st.markdown("<div style='font-size: 0.8rem; color: #A0AEC0;'>Desenvolvido por:<br>Italo Cassio<br>Thiago Alves<br>João Pedro<br>UNIPÊ - 2026</div>", unsafe_allow_html=True)

# ==========================================
# INTERFACE VISUAL (DASHBOARD INDIVIDUAL)
# ==========================================
st.markdown("<h1 style='text-align: center;'><span class='neon-green'>🎯</span> STP: Triagem Preditiva</h1>", unsafe_allow_html=True)
st.write("") 

col_esq, col_dir = st.columns([1.2, 1.2], gap="large")

with col_esq:
    st.markdown("### 📋 Coleta de Dados Clínicos")
    
    with st.form("form_triagem", border=True):
        
        # --- NOVO CAMPO: NOME DO ATLETA ---
        nome_atleta = st.text_input("Identificação do Atleta", placeholder="Ex: Nome, Número ou ID do atleta...")
        st.write("")
        
        aba_treino, aba_clinica = st.tabs(["⚡ Parâmetros de Treino", "🩺 Sinais Clínicos"])
        
        with aba_treino:
            st.markdown("**1. Carga de Treino Recente**")
            carga_val = st.radio("Carga", ["Habitual (Estável)", "Aumento Leve", "Pico Súbito (Muito acima do normal)"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**2. Nível de Fadiga**")
            fadiga_val = st.radio("Fadiga", ["Recuperado", "Cansaço Leve", "Exaustão / Muito Cansado"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**3. Descanso e Pausas**")
            desc_val = st.radio("Descanso", ["Dias de descanso respeitados", "Treinos consecutivos sem pausa"], label_visibility="collapsed")
            
        with aba_clinica:
            st.markdown("**4. Dor Atual**")
            dor_val = st.radio("Dor", ["Nenhuma", "Leve Desconforto", "Dor Aguda / Limitante"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**5. Mobilidade e Flexibilidade**")
            mob_val = st.radio("Mobilidade", ["Normal / Livre", "Restrita / Encurtamento"], label_visibility="collapsed")
            st.write("")
            
            st.markdown("**6. Qualidade do Sono**")
            sono_val = st.radio("Sono", ["menos que 6", "de 7 a 9", "de 10 a 12"], index=1, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**7. Histórico de Lesão (6 meses)**")
            hist_val = st.radio("Histórico", ["Não", "Sim"], horizontal=True, label_visibility="collapsed")
            
        st.write("")
        btn_analisar = st.form_submit_button("🩺 GERAR LAUDO DO ATLETA", type="primary", use_container_width=True)

with col_dir:
    st.markdown("### 🎯 Laudo Preditivo Oficial")
    if btn_analisar:
        # Se o utilizador não digitar nada, usamos um nome padrão
        identificacao = nome_atleta if nome_atleta else "Atleta Não Identificado"
        
        with st.spinner(f"Analisando variáveis de {identificacao}..."):
            time.sleep(0.8)
            risco, pontos, justificativa, cor, tipo_alerta = calcular_risco_lesao(carga_val, sono_val, fadiga_val, hist_val, dor_val, mob_val, desc_val)
        
        st.toast("Laudo gerado com sucesso!", icon="✅")
        
        with st.container(border=True):
            # --- EXIBE O NOME DO ATLETA NO LAUDO ---
            st.markdown(f"**Atleta Avaliado:** {identificacao}")
            st.divider()
            
            # 1. CABEÇALHO DO LAUDO
            met1, met2 = st.columns(2)
            with met1:
                st.metric(label="Status Global de Risco", value=risco)
            with met2:
                st.metric(label="Carga Acumulada", value=f"{pontos} Pontos", delta="Sobrecarga", delta_color=cor)
            
            progresso_normalizado = min(pontos / 14.0, 1.0)
            st.progress(progresso_normalizado)
            
            st.divider()
            
            # Avisos Clínicos Fortes
            if tipo_alerta == "CRITICO_DOR_MOBILIDADE":
                st.error("**ALERTA CLÍNICO:** Combinação de dor e restrição de mobilidade. **Suspenda os treinos e procure avaliação médica.**", icon="🚨")
            elif tipo_alerta == "AVISO_SÓ_MOBILIDADE":
                st.warning("**AVISO PREVENTIVO:** Restrição de mobilidade detectada. Isso altera a biomecânica. **Considere avaliação preventiva.**", icon="⚠️")
            
            # 2. RAIO-X DAS VARIÁVEIS (Onde o atleta está falhando?)
            with st.expander("🔬 **Raio-X da Sobrecarga (Detalhes)**", expanded=True):
                st.markdown("<p class='raiox-item'><strong>Justificativa do Modelo:</strong></p>", unsafe_allow_html=True)
                if risco == "BAIXO":
                    st.success(f"✅ {justificativa}")
                elif risco == "MÉDIO":
                    st.warning(f"🟠 {justificativa}")
                else:
                    st.error(f"🔴 {justificativa}")
                
                st.write("")
                st.markdown("<p class='raiox-item'><strong>Mapeamento de Fatores:</strong></p>", unsafe_allow_html=True)
                
                if carga_val == "Pico Súbito (Muito acima do normal)":
                    st.error("⚡ Carga de Treino: Crítica (Pico Súbito)")
                elif carga_val == "Aumento Leve":
                    st.warning("⚡ Carga de Treino: Atenção (Aumento Leve)")
                else:
                    st.success("⚡ Carga de Treino: Adequada")

                if sono_val == "menos que 6":
                    st.error("🛌 Recuperação (Sono): Deficitária (< 6h)")
                else:
                    st.success("🛌 Recuperação (Sono): Adequada")
                    
                if dor_val == "Dor Aguda / Limitante":
                    st.error("💥 Quadro Clínico: Dor Aguda Ativa")
                elif dor_val == "Leve Desconforto":
                    st.warning("💥 Quadro Clínico: Desconforto Leve")

            # 3. PLANO DE AÇÃO (Gerado Dinamicamente)
            st.markdown("#### 🛠️ Plano de Intervenção Recomendado")
            with st.container(border=True):
                intervencoes = 0
                if risco == "BAIXO" and pontos == 0:
                    st.write("- ✅ **Treino Liberado:** Atleta em perfeitas condições. Manter a planilha atual.")
                    intervencoes += 1
                if carga_val == "Pico Súbito (Muito acima do normal)":
                    st.write("- ⚡ **Ajuste de Carga:** O volume de treino está muito alto. Sugere-se uma semana de *Deload* (redução de 30% a 50% da carga).")
                    intervencoes += 1
                if sono_val == "menos que 6" or fadiga_val == "Exaustão / Muito Cansado":
                    st.write("- 🛌 **Foco em Recovery:** O corpo não está se recuperando a tempo. Priorizar higiene do sono (meta de 8h) e hidratação.")
                    intervencoes += 1
                if desc_val == "Treinos consecutivos sem pausa":
                    st.write("- ⏳ **Gestão de Descanso:** Inserir obrigatoriamente 1 a 2 dias de *Rest Day* total na atual microciclo de treinos.")
                    intervencoes += 1
                if dor_val != "Nenhuma" or mob_val == "Restrita / Encurtamento":
                    st.write("- 🧘 **Protocolo Físico:** Iniciar sessões de mobilidade articular e liberação miofascial antes de qualquer esforço.")
                    intervencoes += 1
                
                if intervencoes == 0:
                    st.write("- ✅ Mantenha o monitoramento diário para garantir a prevenção contínua.")

            st.write("")
            
            # Exportar Laudo (AGORA INCLUI O NOME DO ATLETA NO TEXTO)
            texto_relatorio = f"""
======================================
  STP - SISTEMA DE TRIAGEM PREDITIVA
  Laudo de Risco Individual
======================================

ATLETA AVALIADO: {identificacao}

RESULTADO DA TRIAGEM:
- Risco Detectado: {risco}
- Carga Acumulada: {pontos} pontos

RESUMO DAS VARIÁVEIS DECLARADAS:
- Carga de Treino: {carga_val}
- Fadiga: {fadiga_val}
- Dor Atual: {dor_val}
- Histórico: {hist_val}
- Sono: {sono_val}h
- Mobilidade: {mob_val}
- Descanso: {desc_val}

JUSTIFICATIVA DO MODELO LÓGICO:
{justificativa}

======================================
Gerado eletronicamente por STP (Python)
            """
            st.download_button(
                label=f"📥 Exportar Laudo de {identificacao} (.txt)",
                data=texto_relatorio,
                file_name=f"Laudo_STP_{identificacao}.txt",
                mime="text/plain",
                use_container_width=True
            )
            
    else:
        with st.container(border=True):
            st.info("Aguardando submissão do formulário...", icon="⏳")
            st.write("Preencha as variáveis clínicas à esquerda para gerar o laudo e o plano de ação.")

# Rodapé Oficial do TCC
st.markdown(
    """
    <div class='footer'>
        <strong>Protótipo desenvolvido para o TCC de Ciência da Computação - UNIPÊ (2026)</strong><br>
        Italo Cassio Severiano | Thiago Alves Candido | João Pedro Lopes
    </div>
    """, 
    unsafe_allow_html=True
)