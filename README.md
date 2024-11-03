# Simulação de Monte Carlo com Apostas

<p align=center> <img src="https://imgb.ifunny.co/images/a7db8851edc8b78890fe356a0e9db1f64f54e9f0764c9cabba7961d88b0e02d4_1.jpg" width=400 /> </p>

Este projeto é uma simulação interativa que utiliza o método de Monte Carlo para modelar o resultado de apostas em um jogo. Ele permite que os usuários ajustem os parâmetros do jogo e visualizem os resultados em um gráfico em tempo real.

## Funcionalidades

- **Apostas Interativas**: Ajuste valores iniciais, montantes de apostas, multiplicadores e probabilidades de vitória.
- **Visualização Gráfica**: Os resultados das apostas são plotados em um gráfico, mostrando a evolução do valor total ao longo das rodadas.
- **Múltiplos Usuários**: Simule apostas de vários usuários simultaneamente.
- **Regressão Móvel Contínua**: Visualize uma linha de regressão móvel para entender melhor as tendências.

## Requisitos

Para executar este projeto, você precisará ter o Python 3 instalado, juntamente com as seguintes bibliotecas:

- `numpy`
- `matplotlib`
- `scipy`

Você pode instalar essas bibliotecas usando `pip`:

```bash
pip install numpy matplotlib scipy
```

## Como Usar

Clone o repositório ou baixe os arquivos do projeto.

Execute o script Python:

bash
```
python src/main.py
```
Ajuste os sliders para definir os parâmetros :
    
- Valor Inicial: O valor inicial de cada usuário.
- Valor de Cada Aposta: O montante que cada usuário aposta a cada rodada.
- Multiplicadores: Os multiplicadores associados às apostas (x1, x2, x3).
- Probabilidades de Vitória: A probabilidade de vitória para cada tipo de aposta.
- Quantidade de Rodadas: O número total de rodadas que cada usuário jogará.
- Quantidade de Usuários: O número de usuários participando da simulação.

Observe o gráfico atualizado em tempo real, que mostra a evolução do valor total ao longo das rodadas.

Estrutura do Código

O código consiste nas seguintes funções principais:

* **monte_carlo(...)**: Simula o resultado de apostas com base nos parâmetros fornecidos e retorna a história de valores e o lucro total.
* **setup_sliders()**: Configura os sliders de controle na interface gráfica para ajustar os parâmetros do jogo.
* **add_continuous_moving_regression**(ax, history_value, window=10): Adiciona uma linha de regressão móvel contínua ao gráfico, para visualização de tendências.
* **update_graph(val, ax, sliders)**: Atualiza o gráfico de acordo com os valores dos sliders.
* **configure_plot_and_sliders()**: Configura o gráfico e os sliders, iniciando a interface.

## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar ou expandir este projeto, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
