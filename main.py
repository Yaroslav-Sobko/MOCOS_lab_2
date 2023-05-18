import numpy as np
import warnings
from matplotlib import MatplotlibDeprecationWarning
import matplotlib.pyplot as plt
import time

warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

def fourier_coefficient(x, k):
    N = len(x)
    Ak = np.sum(x * np.cos(2*np.pi*k*np.arange(N)/N))
    Bk = np.sum(x * np.sin(2*np.pi*k*np.arange(N)/N))
    Ck = Ak - 1j*Bk
    num_ops = 4 * N  # кількість операцій
    return Ck, num_ops

def discrete_fourier_transform(x):
    N = len(x)
    C = np.zeros(N, dtype=np.complex128)
    total_ops = 0  # Кількість операцій загалом
    for k in range(N):
        C[k], num_ops = fourier_coefficient(x, k)
        total_ops += num_ops
    print(f"Total number of operations: {total_ops}")
    return C

# генеруємо масив випадкових даних
x = np.random.rand(32)

# час
start_time = time.time()

# обчислюємо ДПФ
C = discrete_fourier_transform(x)

# обчислення спектру амплітуд
amplitude_spectrum = abs(C)

# обчислення спектру фаз
phase_spectrum = np.angle(C)

# побудова графіку спектру амплітуд
plt.figure(figsize=(8, 6))
plt.stem(amplitude_spectrum, use_line_collection=True)
plt.title('пектр амплітуд')
plt.show()

# побудова графіку спектру фаз
plt.figure(figsize=(8, 6))
plt.stem(phase_spectrum, use_line_collection=True)
plt.title('Спектр фаз')
plt.show()

# вивід результатів та часу виконання
for k in range(len(C)):
    print(f"C[{k}] = {C[k]}")

# замір часу в кінці та вивід часу виконання
end_time = time.time()
print(f"Execution time: {end_time - start_time:.5f} seconds")