import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import linregress
from numba import jit

@jit
def monte_carlo(
        initial_value,
        bet_amount,
        multiplier_x1,
        multiplier_x2,
        multiplier_x3,
        win_probability_x1,
        win_probability_x2,
        win_probability_x3,
        n_rounds
):

    now_value = initial_value
    history_value = [initial_value]

    for _ in range(n_rounds):
        event_bet = round(random.random(), 2)

        #Metódo alternativo de if-se
        now_value += (
            -bet_amount if event_bet > win_probability_x1 else
            bet_amount * multiplier_x3 if event_bet <= win_probability_x3 else
            bet_amount * multiplier_x2 if event_bet <= win_probability_x2 else
            bet_amount * multiplier_x1
        )

        history_value.append(now_value)

    profit_total = initial_value - history_value[-1]
    return history_value, profit_total


def setup_sliders():
    y_pos = [0.30, 0.27, 0.24, 0.21, 0.18, 0.15, 0.12, 0.09, 0.06, 0.01]
    sliders = {
        "s_initial_value": Slider(plt.axes([0.2, y_pos[0], 0.65, 0.03]), 'Valor Inicial', 1, 1000, valinit=20),
        "s_bet_amount": Slider(plt.axes([0.2, y_pos[1], 0.65, 0.03]), 'Valor de cada aposta', 1, 50, valinit=15),
        "s_multiplier_x1": Slider(plt.axes([0.3, y_pos[2], 0.65, 0.03]), 'Multiplicador x1', 1.0, 2.0, valinit=1.10),
        "s_multiplier_x2": Slider(plt.axes([0.3, y_pos[3], 0.65, 0.03]), 'Multiplicador x2', 1.0, 2.0, valinit=1.45),
        "s_multiplier_x3": Slider(plt.axes([0.3, y_pos[4], 0.65, 0.03]), 'Multiplicador x3', 1.5, 5.0, valinit=2.50),
        "s_win_probability_x1": Slider(plt.axes([0.3, y_pos[5], 0.65, 0.03]), 'Prob. Vitória x1', 0.10, 1.00, valinit=0.40),
        "s_win_probability_x2": Slider(plt.axes([0.3, y_pos[6], 0.65, 0.03]), 'Prob. Vitória x2', 0.10, 0.50, valinit=0.13),
        "s_win_probability_x3": Slider(plt.axes([0.3, y_pos[7], 0.65, 0.03]), 'Prob. Vitória x3', 0.01, 0.10, valinit=0.02),
        "s_n_rounds": Slider(plt.axes([0.2, y_pos[8], 0.65, 0.03]), 'Quantidade de Rodadas', 10, 1000, valinit=30, valstep=10),
        "s_n_users": Slider(plt.axes([0.2, y_pos[9], 0.65, 0.03]), 'Quantidade de usuários', 1, 400, valinit=1, valstep=1)
    }
    return sliders


def add_continuous_moving_regression(ax, history_value, window=10):
    x_vals = np.arange(len(history_value))
    regression_line = []

    # Calcular a regressão para cada janela móvel de comprimento 'window'
    for i in range(len(history_value)):
        if i < window:
            # Para os primeiros pontos, calcular a regressão na janela disponível
            window_x = x_vals[:i+1]
            window_y = history_value[:i+1]
        else:
            # Usar uma janela deslizante dos últimos 'window' pontos
            window_x = x_vals[i-window+1:i+1]
            window_y = history_value[i-window+1:i+1]

        # Calcular a linha de regressão para a janela atual
        slope, intercept, _, _, _ = linregress(window_x, window_y)
        regression_line.append(slope * x_vals[i] + intercept)

    # Desenhar a linha de regressão contínua
    ax.plot(x_vals, regression_line, color='red', linestyle='--', linewidth=1, label="Regressão Móvel Contínua")


def update_graph(val, ax, sliders):
    initial_value = sliders["s_initial_value"].val
    bet_amount = sliders["s_bet_amount"].val

    multiplier_x1 = sliders["s_multiplier_x1"].val
    multiplier_x2 = sliders["s_multiplier_x2"].val
    multiplier_x3 = sliders["s_multiplier_x3"].val

    win_probability_x1 = sliders["s_win_probability_x1"].val
    win_probability_x2 = sliders["s_win_probability_x2"].val
    win_probability_x3 = sliders["s_win_probability_x3"].val

    n_rounds = int(sliders["s_n_rounds"].val)
    n_users = int(sliders["s_n_users"].val)

    ax.clear()
    for _ in range(n_users):
        history_value, profit_round = monte_carlo(
            initial_value,
            bet_amount,
            multiplier_x1,
            multiplier_x2,
            multiplier_x3,
            win_probability_x1,
            win_probability_x2,
            win_probability_x3,
            n_rounds
        )

        ax.plot(range(n_rounds + 1), history_value)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax.axhline(y=initial_value, color='grey', linestyle='--', linewidth=1)
        # add_continuous_moving_regression(ax, history_value)  # Adicionar linha de regressão
        ax.set_title(f"Lucro da Casa: {profit_round}")
    ax.legend()
    plt.draw()


def configure_plot_and_sliders():
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(left=0.10, bottom=0.4)
    sliders = setup_sliders()

    for slider in sliders.values():
        slider.on_changed(lambda val: update_graph(val, ax, sliders))

    update_graph(None, ax, sliders)
    plt.show()


# Executar a configuração do gráfico e dos sliders
configure_plot_and_sliders()
