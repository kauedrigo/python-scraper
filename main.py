import generate_error
import search_error

try:
  generate_error.generate_error()
except (ValueError, ZeroDivisionError, NameError) as e:
  errorType = type(e).__name__
  print(f"Error: {errorType}")
  print(f"Mensagem: {e}")
  print("\npesquisando...")
  search_error.search_error(errorType)
  print("\nPesquisa realizada com sucesso. Leia o arquivo 'answer.txt' para acessar a resposta")