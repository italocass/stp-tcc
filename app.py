import streamlit as st
import time
from datetime import datetime 

# ==========================================
# CONFIGURAÇÃO DA PÁGINA, ESTILOS E MEMÓRIA
# ==========================================
st.set_page_config(page_title="STP | Triagem Preditiva", page_icon="🎯", layout="wide") 

# INICIANDO A MEMÓRIA DO SISTEMA (Impede que a tela resete)
if 'estado_laudo' not in st.session_state:
    st.session_state['estado_laudo'] = None
if 'dados' not in st.session_state:
    st.session_state['dados'] = {}
if 'campos_vazios' not in st.session_state:
    st.session_state['campos_vazios'] = []

st.markdown("""
    <style>
<<<<<<< HEAD
    /* ==============================
       VISUAL GERAL - MAIS COMPACTO
    ============================== */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.1rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
        padding-bottom: 1.2rem;
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
        letter-spacing: -0.3px;
    }

    h1 {
        font-size: 2.05rem !important;
        margin-bottom: 0.1rem !important;
    }

    h3 {
        font-size: 1.22rem !important;
        margin-top: 0.15rem !important;
        margin-bottom: 0.55rem !important;
    }

    h4 {
        font-size: 1.05rem !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0.35rem !important;
    }

    .neon-green {
        color: #00E676;
        font-weight: bold;
    }

    .sub-text {
        color: #A0AEC0;
        font-size: 0.88rem;
        margin-bottom: 8px;
    }

    /* ==============================
       CARDS / CONTAINERS
    ============================== */
    [data-testid="stForm"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #161A23;
        border-radius: 14px;
        border: 1px solid #2D3748;
        padding: 14px 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }

    [data-testid="stVerticalBlockBorderWrapper"] > div {
        gap: 0.35rem !important;
    }

    [data-testid="column"] {
        padding: 0.05rem 0.2rem;
    }

    /* Diminui espaços verticais padrão do Streamlit */
    div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0.35rem;
    }

    div[data-testid="stMarkdownContainer"] {
        line-height: 1.25rem;
    }

    hr {
        margin-top: 0.55rem !important;
        margin-bottom: 0.55rem !important;
    }

    /* ==============================
       FORMULÁRIO / RADIOS
    ============================== */
    div[role="radiogroup"] {
        gap: 0.25rem !important;
    }

    div[role="radiogroup"] > label {
        background-color: #0E1117;
        border: 1px solid #2D3748;
        border-radius: 9px;
        padding: 6px 9px;
        margin-bottom: 4px;
        font-size: 0.86rem;
        line-height: 1.12rem;
        white-space: normal !important;
        word-break: normal !important;
    }

    div[role="radiogroup"] > label:hover {
        border-color: #00E676;
        background-color: #121722;
    }

    input {
        border-radius: 10px !important;
        min-height: 38px !important;
    }

    /* Botões */
    .stButton > button,
    .stDownloadButton > button,
    [data-testid="stFormSubmitButton"] button {
        border-radius: 11px !important;
        min-height: 40px;
        font-weight: 700 !important;
    }

    /* ==============================
       ABAS
    ============================== */
    [data-testid="stTabs"] button {
        font-size: 0.88rem;
        font-weight: 600;
        padding-top: 4px;
        padding-bottom: 7px;
        white-space: normal;
    }

    [data-testid="stTabs"] button[aria-selected="true"] {
        color: #00E676 !important;
        border-bottom-color: #00E676 !important;
    }

    /* ==============================
       MÉTRICAS DO LAUDO
    ============================== */
    [data-testid="stMetric"] {
        background-color: #0E1117;
        border: 1px solid #2D3748;
        border-radius: 12px;
        padding: 10px 12px;
    }

    [data-testid="stMetricLabel"] {
        color: #A0AEC0 !important;
        font-size: 0.82rem !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 1.35rem !important;
        white-space: normal !important;
    }

    [data-testid="stMetricDelta"] {
        font-size: 0.78rem !important;
    }

    /* ==============================
       ALERTAS, EXPANDERS E RESULTADOS
    ============================== */
    [data-testid="stAlert"] {
        border-radius: 10px;
        line-height: 1.25rem;
        padding-top: 0.55rem;
        padding-bottom: 0.55rem;
    }

    [data-testid="stExpander"] {
        border-radius: 12px !important;
        overflow: hidden;
        margin-top: 0.25rem;
        margin-bottom: 0.25rem;
    }

    [data-testid="stExpanderDetails"] {
        background-color: #111827;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    [data-testid="stExpanderDetails"] [data-testid="stAlert"] {
        margin-top: 0px !important;
        margin-bottom: 8px !important;
    }

    .raiox-item {
        font-size: 0.9rem;
        font-weight: bold;
        margin-bottom: 5px !important;
        margin-top: 8px !important;
        display: block;
        color: #E2E8F0;
    }

    p, li, span, div {
        overflow-wrap: break-word;
        word-wrap: break-word;
    }

    /* ==============================
       SIDEBAR
    ============================== */
    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #2D3748;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li {
        font-size: 0.88rem;
        line-height: 1.25rem;
    }

    /* ==============================
       RODAPÉ
    ============================== */
    .footer {
        text-align: center;
        color: #718096;
        font-size: 0.78rem;
        margin-top: 28px;
        padding-top: 12px;
        border-top: 1px solid #2D3748;
    }

    /* ==============================
       RESPONSIVIDADE
    ============================== */
    @media (max-width: 1100px) {
        .block-container {
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }

        h1 {
            font-size: 1.75rem !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.2rem !important;
        }
    }
=======
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    [data-testid="stForm"], [data-testid="stVerticalBlockBorderWrapper"] { background-color: #161A23; border-radius: 12px; border: 1px solid #2D3748; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .neon-green { color: #00E676; font-weight: bold; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .sub-text { color: #A0AEC0; font-size: 0.9rem; margin-bottom: 15px; }
    div[role="radiogroup"] > label { margin-bottom: 5px; font-size: 0.85rem; }
    [data-testid="stTabs"] button { font-size: 1rem; font-weight: 600; padding-bottom: 10px; }
    [data-testid="stTabs"] button[aria-selected="true"] { color: #00E676 !important; border-bottom-color: #00E676 !important; }
    .footer { text-align: center; color: #4A5568; font-size: 0.85rem; margin-top: 50px; padding-top: 20px; border-top: 1px solid #2D3748; }
    .raiox-item { font-size: 0.95rem; font-weight: bold; margin-bottom: 8px !important; margin-top: 12px !important; display: block; color: #E2E8F0; }
    [data-testid="stExpanderDetails"] [data-testid="stAlert"] { margin-top: 0px !important; margin-bottom: 15px !important; }
>>>>>>> 27db395b66d010dcee4f33d0ef63dd6f5318e979
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

col_esq, col_dir = st.columns([0.95, 1.35], gap="large")

with col_esq:
    st.markdown("### 📋 Coleta de Dados Clínicos")
    
    with st.form("form_triagem", border=True):
        nome_atleta = st.text_input("Identificação do Atleta", placeholder="Ex: Nome, Número ou ID do atleta...")
        st.write("")
        
        aba_treino, aba_clinica = st.tabs(["⚡ Parâmetros de Treino", "🩺 Sinais Clínicos"])
        
        with aba_treino:
            st.markdown("**1. Carga de Treino Recente**")
            carga_val = st.radio("Carga", ["Habitual (Estável)", "Aumento Leve", "Pico Súbito (Muito acima do normal)"], index=None, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**2. Nível de Fadiga**")
            fadiga_val = st.radio("Fadiga", ["Recuperado", "Cansaço Leve", "Exaustão / Muito Cansado"], index=None, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**3. Descanso e Pausas**")
            desc_val = st.radio("Descanso", ["Dias de descanso respeitados", "Treinos consecutivos sem pausa"], index=None, label_visibility="collapsed")
            
        with aba_clinica:
            st.markdown("**4. Dor Atual**")
            dor_val = st.radio("Dor", ["Nenhuma", "Leve Desconforto", "Dor Aguda / Limitante"], index=None, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**5. Mobilidade e Flexibilidade**")
            mob_val = st.radio("Mobilidade", ["Normal / Livre", "Restrita / Encurtamento"], index=None, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**6. Qualidade do Sono**")
            sono_val = st.radio("Sono", ["menos que 6", "de 7 a 9", "de 10 a 12"], index=None, label_visibility="collapsed")
            st.write("")
            
            st.markdown("**7. Histórico de Lesão (6 meses)**")
            hist_val = st.radio("Histórico", ["Não", "Sim"], index=None, horizontal=True, label_visibility="collapsed")
            
        st.write("")
        btn_analisar = st.form_submit_button("🩺 GERAR LAUDO DO ATLETA", type="primary", use_container_width=True)

with col_dir:
    st.markdown("### 🎯 Laudo Preditivo Oficial")
    
    # 1. QUANDO O BOTÃO É CLICADO, SALVAMOS TUDO NA MEMÓRIA
    if btn_analisar:
        campos_obrigatorios = {
            "Carga de Treino Recente": carga_val,
            "Nível de Fadiga": fadiga_val,
            "Descanso e Pausas": desc_val,
            "Dor Atual": dor_val,
            "Mobilidade e Flexibilidade": mob_val,
            "Qualidade do Sono": sono_val,
            "Histórico de Lesão (6 meses)": hist_val
        }
        
        campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if valor is None]
        
        if campos_vazios:
            st.session_state['estado_laudo'] = 'erro'
            st.session_state['campos_vazios'] = campos_vazios
        else:
            st.session_state['estado_laudo'] = 'sucesso'
            st.session_state['dados'] = {
                'nome': nome_atleta if nome_atleta else "Atleta Não Identificado",
                'carga': carga_val,
                'fadiga': fadiga_val,
                'desc': desc_val,
                'dor': dor_val,
                'mob': mob_val,
                'sono': sono_val,
                'hist': hist_val,
                'data_hora': datetime.now().strftime("%d/%m/%Y às %H:%M")
            }

    # 2. RENDERIZAMOS A TELA LENDO DA MEMÓRIA (Assim nada some!)
    estado = st.session_state['estado_laudo']

    if estado == 'erro':
        with st.container(border=True):
            st.error("🚨 **Atenção: Preenchimento Incompleto!**")
            st.write("Não é possível gerar um laudo médico preditivo com dados faltantes. Por favor, responda às seguintes perguntas nas abas ao lado:")
            for campo in st.session_state['campos_vazios']:
                st.markdown(f"- 🔴 **{campo}**")
            st.write("")
            st.info("Após preencher os campos acima, clique novamente em 'Gerar Laudo'.")
            
    elif estado == 'sucesso':
        d = st.session_state['dados']
        
        # Só exibe o spinner e o toast quando acabou de clicar no botão
        if btn_analisar:
            with st.spinner(f"Analisando variáveis de {d['nome']}..."):
                time.sleep(0.8)
            st.toast("Laudo gerado com sucesso!", icon="✅")
            
        risco, pontos, justificativa, cor, tipo_alerta = calcular_risco_lesao(
            d['carga'], d['sono'], d['fadiga'], d['hist'], d['dor'], d['mob'], d['desc']
        )
        
        with st.container(border=True):
            st.markdown(f"**Atleta Avaliado:** {d['nome']} <br> <span style='font-size: 0.8rem; color: #A0AEC0;'>📅 Data da Triagem: {d['data_hora']}</span>", unsafe_allow_html=True)
            st.divider()
            
            # CABEÇALHO DO LAUDO
            met1, met2 = st.columns(2)
            with met1:
                st.metric(label="Status Global de Risco", value=risco)
            with met2:
                st.metric(label="Carga Acumulada", value=f"{pontos} Pontos", delta="Sobrecarga", delta_color=cor)
            
            progresso_normalizado = min(pontos / 14.0, 1.0)
            st.progress(progresso_normalizado)
            
            st.divider()
            
            if tipo_alerta == "CRITICO_DOR_MOBILIDADE":
                st.error("**ALERTA CLÍNICO:** Combinação de dor e restrição de mobilidade. **Suspenda os treinos e procure avaliação médica.**", icon="🚨")
            elif tipo_alerta == "AVISO_SÓ_MOBILIDADE":
                st.warning("**AVISO PREVENTIVO:** Restrição de mobilidade detectada. Isso altera a biomecânica. **Considere avaliação preventiva.**", icon="⚠️")
            
            # RAIO-X DAS VARIÁVEIS
<<<<<<< HEAD
            with st.expander("🔬 **Raio-X da Sobrecarga (Detalhes)**", expanded=False):
=======
            with st.expander("🔬 **Raio-X da Sobrecarga (Detalhes)**", expanded=True):
>>>>>>> 27db395b66d010dcee4f33d0ef63dd6f5318e979
                st.markdown("<div class='raiox-item'>Justificativa do Modelo:</div>", unsafe_allow_html=True)
                if risco == "BAIXO":
                    st.success(f"✅ {justificativa}")
                elif risco == "MÉDIO":
                    st.warning(f"🟠 {justificativa}")
                else:
                    st.error(f"🔴 {justificativa}")
                
                st.markdown("<div class='raiox-item'>Mapeamento de Fatores:</div>", unsafe_allow_html=True)
                
                rx_col1, rx_col2 = st.columns(2)
                
                with rx_col1:
                    if d['carga'] == "Pico Súbito (Muito acima do normal)":
                        st.error("⚡ Carga: Pico Súbito")
                    elif d['carga'] == "Aumento Leve":
                        st.warning("⚡ Carga: Aumento Leve")
                    else:
                        st.success("⚡ Carga: Adequada")

                    if d['sono'] == "menos que 6":
                        st.error("🛌 Sono: Deficitário")
                    else:
                        st.success("🛌 Sono: Adequado")
                
                with rx_col2:
                    if d['dor'] == "Dor Aguda / Limitante":
                        st.error("💥 Dor: Aguda Ativa")
                    elif d['dor'] == "Leve Desconforto":
                        st.warning("💥 Dor: Desconforto")
                    else:
                        st.success("💥 Dor: Nenhuma")
                        
                    if d['mob'] == "Restrita / Encurtamento":
                        st.warning("🤸 Mobilidade: Restrita")
                    else:
                        st.success("🤸 Mobilidade: Livre")

            # PLANO DE AÇÃO
            st.markdown("#### 🛠️ Plano de Intervenção Recomendado")
            with st.container(border=True):
                intervencoes = 0
                if risco == "BAIXO" and pontos == 0:
                    st.write("- ✅ **Treino Liberado:** Atleta em perfeitas condições. Manter a planilha atual.")
                    intervencoes += 1
                if d['carga'] == "Pico Súbito (Muito acima do normal)":
                    st.write("- ⚡ **Ajuste de Carga:** O volume de treino está muito alto. Sugere-se uma semana de *Deload* (redução de 30% a 50% da carga).")
                    intervencoes += 1
                if d['sono'] == "menos que 6" or d['fadiga'] == "Exaustão / Muito Cansado":
                    st.write("- 🛌 **Foco em Recovery:** O corpo não está se recuperando a tempo. Priorizar higiene do sono (meta de 8h) e hidratação.")
                    intervencoes += 1
                if d['desc'] == "Treinos consecutivos sem pausa":
                    st.write("- ⏳ **Gestão de Descanso:** Inserir obrigatoriamente 1 a 2 dias de *Rest Day* total no atual microciclo de treinos.")
                    intervencoes += 1
                if d['dor'] != "Nenhuma" or d['mob'] == "Restrita / Encurtamento":
                    st.write("- 🧘 **Protocolo Físico:** Iniciar sessões de mobilidade articular e liberação miofascial antes de qualquer esforço.")
                    intervencoes += 1
                
                if intervencoes == 0:
                    st.write("- ✅ Mantenha o monitoramento diário para garantir a prevenção contínua.")

            # MÓDULO DE VALIDAÇÃO CLÍNICA CONTÍNUA (Agora seguro contra resete)
<<<<<<< HEAD
            with st.expander("🩺 Validação em Cenário Real (Feedback do Especialista)", expanded=False):
=======
            st.markdown("#### 🩺 Validação em Cenário Real (Feedback do Especialista)")
            with st.container(border=True):
>>>>>>> 27db395b66d010dcee4f33d0ef63dd6f5318e979
                st.markdown("<div style='font-size:0.85rem; color:#A0AEC0;'>Seção exclusiva para o Fisioterapeuta/Treinador validar a acurácia do modelo em campo:</div>", unsafe_allow_html=True)
                feedback_modelo = st.radio("O diagnóstico da IA condiz com o estado clínico real do atleta?", ["Sim, 100% de acerto", "Parcialmente correto", "Incorreto / Falso Positivo"], index=None, key="feedback_banca")
                obs_clinica = st.text_input("Observações de campo / Ajustes sugeridos pelo especialista:", placeholder="Ex: Atleta relatou dor tardia muscular comum, não articular...")

            st.write("")
            col_botoes1, col_botoes2 = st.columns(2)
            
            with col_botoes1:
                feedback_txt = feedback_modelo if feedback_modelo else "Não avaliado pelo especialista ainda"
                obs_txt = obs_clinica if obs_clinica else "Nenhuma observação inserida"
                
                texto_relatorio = f"""
======================================
  STP - SISTEMA DE TRIAGEM PREDITIVA
  Laudo de Risco Individual
======================================

ATLETA AVALIADO: {d['nome']}
DATA DA TRIAGEM: {d['data_hora']}

RESULTADO DA TRIAGEM DA IA:
- Risco Detectado: {risco}
- Carga Acumulada: {pontos} pontos

JUSTIFICATIVA DO MODELO LÓGICO:
{justificativa}

======================================
  MÓDULO DE VALIDAÇÃO EM CENÁRIO REAL
======================================
- Validação Clínica: {feedback_txt}
- Notas do Especialista: {obs_txt}

======================================
Gerado eletronicamente por STP (Python)
                """
                st.download_button(
                    label=f"📥 Exportar Prontuário Validado (.txt)",
                    data=texto_relatorio,
                    file_name=f"Laudo_STP_{d['nome']}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            with col_botoes2:
                if st.button("🔄 Avaliar Novo Atleta", use_container_width=True):
                    # Limpa a memória para avaliar o próximo
                    st.session_state['estado_laudo'] = None
                    st.session_state['dados'] = {}
                    st.rerun()
        
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