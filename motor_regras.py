def calcular_risco_lesao(carga, sono, fadiga, historico, dor_atual, mobilidade, descanso):
    """
    Motor de Regras Oficial do TCC com múltiplos alertas clínicos.
    """
    pontuacao = 0
    gatilhos = []
    
    # Nova Lógica de Alertas Clínicos
    tipo_alerta = None
    if dor_atual != "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "CRITICO_DOR_MOBILIDADE"
    elif dor_atual == "Nenhuma" and mobilidade == "Restrita / Encurtamento":
        tipo_alerta = "AVISO_SÓ_MOBILIDADE"

    # 1. Carga (Frequência e Intensidade)
    if carga == "Pico Súbito (Muito acima do normal)":
        pontuacao += 3
        gatilhos.append("Pico Súbito de Carga")
    elif carga == "Aumento Leve":
        pontuacao += 1
        gatilhos.append("Leve aumento de volume")
        
    # 2. Qualidade do Sono 
    if sono == "menos que 6":
        pontuacao += 2
        gatilhos.append("Sono Insuficiente (< 6h)")
    elif sono == "de 10 a 12":
        pontuacao += 1
        gatilhos.append("Recuperação prolongada (10-12h)")
        
    # 3. Fadiga
    if fadiga == "Exaustão / Muito Cansado":
        pontuacao += 2
        gatilhos.append("Nível alto de fadiga")
    elif fadiga == "Cansaço Leve":
        pontuacao += 1
        gatilhos.append("Fadiga residual")
        
    # 4. Histórico de Lesão
    if historico == "Sim":
        pontuacao += 2
        gatilhos.append("Histórico Lesivo Recente")

    # 5. Dor Atual
    if dor_atual == "Dor Aguda / Limitante":
        pontuacao += 2
        gatilhos.append("Dor Aguda")
    elif dor_atual == "Leve Desconforto":
        pontuacao += 1
        gatilhos.append("Desconforto Muscular/Articular")

    # 6. Mobilidade
    if mobilidade == "Restrita / Encurtamento":
        pontuacao += 1
        gatilhos.append("Mobilidade Restrita")

    # 7. Descanso
    if descanso == "Treinos consecutivos sem pausa":
        pontuacao += 1
        gatilhos.append("Falta de dias de descanso")

    # Limiares de Risco
    if pontuacao <= 3:
        risco = "RISCO BAIXO"
        justificativa = "Sinais estáveis. Treino liberado." if pontuacao == 0 else f"Atenção leve: {', '.join(gatilhos)}."
    elif pontuacao <= 6:
        risco = "RISCO MÉDIO"
        justificativa = f"Alerta Laranja: Risco moderado ativado por {', '.join(gatilhos)}."
    else:
        risco = "RISCO ALTO"
        justificativa = f"ALERTA CRÍTICO: Risco gerado pelo cruzamento de {', '.join(gatilhos)}."

    return risco, pontuacao, justificativa, tipo_alerta

# ==========================================
# TESTE RÁPIDO NO TERMINAL
# ==========================================
if __name__ == "__main__":
    resultado, pontos, explicacao, alerta = calcular_risco_lesao(
        carga="Habitual (Estável)", sono="de 7 a 9", fadiga="Recuperado", 
        historico="Não", dor_atual="Nenhuma", # Sem dor
        mobilidade="Restrita / Encurtamento", # Mas com problema na mobilidade
        descanso="Dias de descanso respeitados"
    )
    print(f"Diagnóstico: {resultado} ({pontos} pontos)")
    print(f"Tipo de Alerta: {alerta}\n")