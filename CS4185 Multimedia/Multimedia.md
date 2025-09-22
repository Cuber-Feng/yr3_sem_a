# Multimedia

## Course Information

- [Course Website](https://www.cs.cityu.edu.hk/~rynson/info-mm/mm.html)

## Lec04: Sampling, Multimedia Communications, and Streaming

### Sampling 采样

> 把一幅连续的图像转换成由像素组成的数字图像

- **Sample Theorem**
  - `The sampling theorem states that if the sampling frequency, fs, is greater than twice of the highest frequency component, fh, in the input signal, it will be possible to reconstruct the signal from the sampled data without information loss.`
  - 当我们把一个连续信号（analog signal）转换成离散信号（digital signal）时，需要以一定的频率采样
  - 如果采样频率 fs 足够高，就能从采样点完整重建原始信号，不会丢失信息。
  - fs > 2 × fh
    - fh：输入信号中最高的频率成分（最高频率）
    - fs：采样频率(每秒采多少次)
- Data Rates (The file size for a 4-minute song)
  - Human ears can hear sound in the range of 20Hz to 20KHz. (Hz is the unit of frequency.)
  - The typical sampling rate for audio CD is set to 44.1KHz, and each sample is 2 Bytes in size.
  - The file size for 1 second of the song (stereo) is: `44,100 * 2 * 2 Bytes = 176,400 Bytes`
  - The file size for the whole song is then: `176,400 * 4 * 60 Bytes = 40.4 MB`

- low pass filters
  - Low-pass filter（低通滤波器）是一种信号处理工具，它允许低频信号通过，抑制（或阻挡）高频信号
  - 打電話的時候就會用到
  - Telephone service providers use low pass filters to reduce the input signal frequency from the landline/mobile phones to reduce the bandwidth consumption of each phone

### Network Transmission

- the size of the compressed file is not fixed. It depends on the file content
- CBR（Constant Bit Rate，恒定比特率）
  - 特点：编码过程中比特率保持固定。
  - 优点：
    - 文件大小可预测。
    - 适合实时传输（如直播、语音通话）。
  - 缺点：
    - 复杂场景可能画质下降，因为比特率固定。
  - 应用：流媒体、VoIP。

- VBR（Variable Bit Rate，可变比特率）
  - 特点：根据内容复杂度动态调整比特率。
    - 复杂场景 → 高比特率
    - 简单场景 → 低比特率。
  - 优点：
    - 更高的压缩效率，画质更好。
  - 缺点：
    - 文件大小不可预测
    - 编码和解码更复杂。
  - 应用：高质量音频（MP3 VBR）、视频压缩。

### Quality of Service (QoS)

### Wireless Networks

### Multimedia Streaming

---

## Project

- This assignment can be carried out as **individual or group** projects. The maximum number of members in each group is **3**. With **more students in a group**, slightly **more work and better results are expected**, and the responsibility of each group member needs to be clearly indicated in the report.
