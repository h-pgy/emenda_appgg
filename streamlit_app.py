import streamlit as st
import pandas as pd

with st.sidebar:
    with open('README.md') as f:
        text = f.read()
    st.markdown(text)

    st.markdown('#### **Desenvolvido por**: Henrique Pougy')
    col1, col2 = st.columns([0.5, 3])

    with col1:
        st.image('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg', use_column_width=True)
    with col2:
        st.markdown('[linkedin](https://www.linkedin.com/in/henrique-pougy-8a008759?originalSubdomain=br)')


st.title("Resultados da Votação")
st.header("Emendas ao PL XX")


df = pd.read_csv('dados_votacao_final.csv', sep=';', encoding='utf-8')
df['count'] = 1

cols_votos = [
    'Em relação às propostas de recuperação salarial, você:',
    'Em relação à proposta de remoção da cláusula de limite para as cessões sem prejuízo dos vencimentos você:',
    'Em relação à proposta de remoção da cláusula de impedimento de ocupar cargos em comissão durante o estágio probatório você:'
]

def agrupar()