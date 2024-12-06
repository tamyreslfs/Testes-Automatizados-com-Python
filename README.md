Testes Automatizados com Python
----------------------------------
Atividade Complementar
----------------------------------

Instruções

1. Você receberá três arquivos Python com classes implementadas.
2. Cada classe contém métodos que possuem bugs.
3. Seu objetivo é:
    °Identificar os bugs nas implementações.
    °Corrigir os métodos para que funcionem conforme esperado.
    °Escrever testes automatizados para verificar se os métodos corrigidos estão funcionando            corretamente.
4. Use a biblioteca unittest ou pytest para criar os testes automatizados.

-----------------------------------

Passo a Passo para Efetuar os Testes

Pré-requisitos:

Ter Python instalado na máquina (versão 3.7 ou superior).
Garantir que todos os arquivos corrigidos e os arquivos de teste estejam na mesma pasta de trabalho.
Estar no diretório onde o projeto foi salvo.
Passos:

Acesse o terminal ou prompt de comando.

Sem Windows, utilize o cmd.
Sem Linux/Mac, utilize o terminal.
Navegue até a pasta do projeto.

Execute os testes automatizados com o comando abaixo:
python -m unittest discover -s tests
Verifique o resultado dos testes no terminal.

Se todos os testes passaram, o resultado será algo como:

.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK

Caso algum teste falhe, a mensagem mostrará o erro específico.
