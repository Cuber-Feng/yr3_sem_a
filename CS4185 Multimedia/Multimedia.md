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

### Network Transmission

### Quality of Service (QoS)

### Wireless Networks

### Multimedia Streaming
