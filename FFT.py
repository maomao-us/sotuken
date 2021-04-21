import numpy as np
import pandas as pd
import csv
from scipy import signal
import matplotlib.pyplot as plt

name1 = "csv_data/nakajima1.csv"
x_label = "Linear Acceleration x (m/s^2)"

df = pd.read_csv(name1)
df = df[x_label]
df = np.array(df)
dt = 0.005
t = np.arange(0, len(df)*dt, dt) # 時間軸
# print(df)

F = np.fft.fft(df)
F_abs=np.abs(F)
# print(F)
F_abs_amp = F_abs / len(F_abs) * 2 # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要

# 周波数軸のデータ作成
fq = np.linspace(0, 1.0/dt, len(F_abs)) # 周波数軸　linspace(開始,終了,分割数)

F_ifft = np.fft.ifft(F) # 逆フーリエ変換(IFFT)
F_ifft_real = F_ifft.real # 実数部

F2 = np.copy(F) # FFT結果コピー
# 周波数でフィルタリング処理
fc = 10 # カットオフ（周波数）
F2[(fq > fc)] = 0 # カットオフを超える周波数のデータをゼロにする（ノイズ除去）

# フィルタリング処理したFFT結果の確認
# FFTの複素数結果を絶対値に変換
F2_abs = np.abs(F2)
# 振幅をもとの信号に揃える
F2_abs_amp = F2_abs / len(F_abs) * 2 # 交流成分はデータ数で割って2倍
F2_abs_amp[0] = F2_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要



# plt.plot(F_abs[:int(len(F_abs)/2)+1])

# plt.plot(F_abs_amp[:int(len(F_abs)/2)+1])

# plt.plot(fq[:int(len(F_abs)/2)+1], F_abs_amp[:int(len(F_abs)/2)+1]) # ナイキスト定数まで表示

# plt.plot(t, df, label="original")

# plt.plot(t, F_ifft_real, c="g", linestyle='--', label='IFFT') # IFFT（逆変換）

# グラフ表示（FFT解析結果）
# plt.plot(fq, F_abs_amp)
# plt.plot(fq, F2_abs_amp, c='r')

# 周波数でフィルタリング（ノイズ除去）-> IFFT
F2_ifft = np.fft.ifft(F2) # IFFT
F2_ifft_real = F2_ifft.real * 2 # 実数部の取得、振幅を元スケールに戻す

plt.plot(t, df, label="original")
# plt.plot(t, F2_ifft_real, c="r", label='filtered')

F3 = np.copy(F) # FFT結果コピー
# 振幅強度でフィルタリング処理
F3 = np.copy(F) # FFT結果コピー
ac = 0.05 # 振幅強度の閾値
F3[(F_abs_amp < ac)] = 0 # 振幅が閾値未満はゼロにする（ノイズ除去）

# 振幅でフィルタリング処理した結果の確認
# FFTの複素数結果を絶対値に変換
F3_abs = np.abs(F3)
# 振幅をもとの信号に揃える
F3_abs_amp = F3_abs / len(F_abs) * 2 # 交流成分はデータ数で割って2倍
F3_abs_amp[0] = F3_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要

# plt.plot(fq, F3_abs_amp, c='orange')

# 振幅強度でフィルタリング（ノイズ除去）-> IFFT
F3_ifft = np.fft.ifft(F3) # IFFT
F3_ifft_real = F3_ifft.real # 実数部の取得
# グラフ（オリジナルとフィルタリングを比較）

plt.plot(t, F3_ifft_real, c="orange", label='filtered')

plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)
plt.legend()
plt.show()