import pandas as pd
import numpy as np


chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.log(np.mean(x - 867)) - 1 / 2 * np.log(np.mean((x - 867) ** 2)/(np.mean(x - 867)) **2) # Ваш ответ
