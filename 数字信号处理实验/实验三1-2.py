import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
wave = thinkdsp.read_wave('18871__zippi1__sound-bell-440hz.wav')
plt.subplot(231)
plt.title("原音频")
wave.plot()
segment = wave.segment(start=1.1, duration=1)
plt.subplot(232)
plt.title("截取的1s音频")
segment.plot()

spectrum = segment.make_spectrum()
plt.subplot(233)
plt.title("截取的音频频谱")
plt.ylim(0, 1000)
spectrum.plot(high=5000)

spectrum.low_pass(1000)
wave_lp = spectrum.make_wave()
wave_lp.write(filename='wave_lp.wav')
plt.subplot(234)
plt.title("低通滤波1khz后的音频")
plt.ylim(0, 1000)
spectrum.plot(high=5000)
play('wave_lp.wav', flags=1)
time.sleep(5)# 等待5s运行下一条语句

spectrum = segment.make_spectrum()
spectrum.high_pass(4000)
wave_hp = spectrum.make_wave()
wave_hp.write(filename='wave_hp.wav')
plt.subplot(235)
plt.title("高通滤波4khz音频")
plt.ylim(0, 1000)
spectrum.plot(high=5000)
play('wave_hp.wav', flags=1)
time.sleep(5)

spectrum = segment.make_spectrum()
spectrum.band_stop(low_cutoff=1000 ,high_cutoff=4000)
wave_bp = spectrum.make_wave()
wave_bp.write(filename='wave_bp.wav')
plt.subplot(236)
plt.title("带阻滤波1khz~4khz音频")
plt.ylim(0, 1000)
spectrum.plot(high=7000)
play('wave_bp.wav', flags=1)
plt.show()