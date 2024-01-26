import streamlit as st
import pandas as pd

def load_data(uploaded_file):
    try:
        return pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

def find_and_save_duplicates(df1, df2):
    try:
        # Encontrar duplicatas entre as duas planilhas
        linhas_duplicadas = pd.merge(df1, df2, how='inner').drop_duplicates()

        if not linhas_duplicadas.empty:
            # Filtrar duplicatas considerando apenas aquelas que são duplicadas entre as tabelas
            linhas_duplicadas = linhas_duplicadas[df1.columns]

            # Obter a quantidade de linhas duplicadas
            quantidade_duplicadas = len(linhas_duplicadas)

            # Exibir a quantidade de linhas duplicadas
            st.write(f'Quantidade de Linhas Duplicadas: {quantidade_duplicadas}')

            # Exibir exemplos de linhas duplicadas
            st.write("Exemplos de Linhas Duplicadas:")
            st.dataframe(linhas_duplicadas)

            # Salvar as duplicatas em um arquivo Excel
            save_path = 'duplicatas.xlsx'
            linhas_duplicadas.to_excel(save_path, index=False)
            st.success(f'Duplicatas salvas em: {save_path}')
        else:
            # Exibir mensagem se não houver linhas duplicadas
            st.info('Não há linhas duplicadas.')
    except Exception as e:
        st.error(f"Erro ao encontrar e salvar duplicatas: {e}")

def main():
    st.title("Detector de Duplicatas")

    # Solicitar upload da primeira planilha
    uploaded_file1 = st.file_uploader("Faça o upload da primeira planilha (.xlsx)", type=["xlsx"])

    # Solicitar upload da segunda planilha
    uploaded_file2 = st.file_uploader("Faça o upload da segunda planilha (.xlsx)", type=["xlsx"])

    # Verificar se os uploads foram realizados
    if uploaded_file1 is not None and uploaded_file2 is not None:
        # Carregar dados das planilhas
        df1 = load_data(uploaded_file1)
        df2 = load_data(uploaded_file2)

        # Verificar se os dados foram carregados com sucesso
        if df1 is not None and df2 is not None:
            # Encontrar e salvar duplicatas
            find_and_save_duplicates(df1, df2)

if __name__ == "__main__":
    main()

