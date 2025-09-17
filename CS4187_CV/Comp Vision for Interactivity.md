## Assessment
- Programming Assignments (50%)  
	- Three Assignments (30%)  
	- One Mini Project & Video-recorded Presentation/Demonstration (20%)  
- Midterm Quiz (10%)
- Final Exam (40%)

## Lecture 1
- Computer Vision is to give computers super human-level perception

## Lecture 2
- Linear Filtering
	- Box Filtering
	- Gaussian Filtering
	- **高斯滤波器**用加权平均值（**越近权重越大**）平滑图像，效果更自然； 而**框式滤波器**用**简单平均值平滑图像**，计算快但边缘处理不如前者
- Non-Linear Filtering
	- Median Filtering
		- **中值滤波**是一种非线性数字滤波技术，常用于图像处理中去除椒盐噪声（salt-and-pepper noise）。与高斯滤波和框式滤波不同，中值滤波不使用加权平均，而是基于统计排序。
		- 中值滤波对于**椒盐噪声**非常有效，因为它能直接将这些异常值（椒盐噪声通常是极高或极低的像素值）替换为周围区域的**代表性中值**。

## Lecture 3
- Kernel/Filter Convolution (卷积)
	- 在图像处理中，**卷积**是一种核心操作，它将一个小的矩阵（称为**核**或**滤波器**）应用于一个更大的矩阵（即**图像**），从而生成一个新的图像。这个过程可以用来实现各种效果，例如模糊、锐化、边缘检测等。
	- 简单来说，你可以把卷积想象成一个“**滑动窗口**”的操作，这个窗口就是你的**核**。
- Edge
	- Boundaries of objects
	- Edge 的来源:
		- 表面法线(surface normal)不连续
		- 深度(depth)不连续
		- 表面颜色(surface color)不连续
		- 照明(illumination)不连续
	- Type of edge
		- Step Edge
			- 一种最理想化的边缘模型，它描述了像素值从一个恒定值**瞬时**地跳变到另一个恒定值
		- Ramp Edge
			- 像素值从一个值**平缓地、渐进地**变化到另一个值
	- Thresholding
		- Standard thresholding
		- Hysteresis thresholding
			- 有两个阈值, 高阈值&低阈值
			- “滞后”过程, 即“**只接受与高阈值边缘相连的弱边缘**”
	- Hough Transform 
		- “投票”机制：
			- **一个点**：图像空间中的一个边缘点，可能属于多条直线。在参数空间中，它 **“投”了多条线**的票，即它在累加器中对应的所有 (θ,ρ) 坐标上都加了 1。
			- **一条线**：图像空间中的一条直线由多个点组成。在参数空间中，这些点都 **“投”了同一条线**的票。因此，对应这条直线的 (θ,ρ) 坐标会在累加器中得到高分，形成一个峰值。