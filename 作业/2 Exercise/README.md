# TOF-MRA成像和DSA成像图像处理



1. 下载并安装Matlab以及`SPM 12`工具包，将SPM 12添加到Matlab搜索路径

2. 下载`imshow3D`函数

   https://ww2.mathworks.cn/matlabcentral/fileexchange/41334-imshow3d

3. `TOF-MRA`成像和`DSA成像`介绍:

> **TOF-MRA成像**

**时间飞跃法**（Time of Flight, TOF）是一种不打药磁共振血管成像技术。这种技术主要是利用了梯度回波序列中流动血液的流入增强效应（inflow）进行血管成像的，所以又可以叫做流入增强血管成像技术。

>  **DSA成像**

DSA是**数字减影血管造影**（Digital subtraction angiography）的英文缩写，其基本原理是将注入造影剂前后拍摄的两帧X线图像经数字化输入图像计算机，通过减影、增强和再成像过程把血管造影影像上的骨与软组织影像消除来获得清晰的纯血管影像，是电子计算机与常规X线血管造影相结合的一种检查方法。通俗的讲就是将造影剂注入需要检查的血管中，使血管显露原形。然后通过系统处理，使血管显示更加清晰，便于医生诊断或进行手术。

4. 使用任意Dicom看读软件（例如试用版的radiant），查看文件夹中的3D TOF原始DICOM图像；

   ![image-20220923001950372](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923001950372.png)

   使用SPM的图像界面（在Matlab Command window中输入`spm fmri`），将3D TOF原始DICOM图像转换成NIFTI格式文件；使用以下命令，将所得的NIFTI文件中的图像读取到Matlab的Workspace中，并显示。

```matlab
% 读入nii图像并显示
tof_vol = spm_vol(['TOF_nii/Mag.nii.gz' ...
    '']);
tof = imrotate(spm_read_vols(tof_vol), 90);
figure, imshow3D(tof);
```

![image-20220923002030437](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002030437.png)



5. 使用Matlab自带函数`dicomread`，将同一名被试的冠状位（coronal）和矢状位(sagittal) DSA DICOM图像（见文件夹DSA_LVA_cor和DSA_LVA_sag）读到Matlab的Workspace，并使用函数`imshow`显示图像。这两组DSA图像显示的是左侧椎动脉（Left vertebral artery）及其下游分支血管。在Command window中，输入指令`imcontrast`，调整图像灰度显示范围（即窗宽窗位）。

```matlab
X_sag = dicomread('DSA_LVA_sag/Image (0017).dcm');
X_cor = dicomread('DSA_LVA_cor/Image (0017).dcm');

imshow(X_sag)% >>imcontrast调整图像对比度
imshow(X_cor)

```

冠状位图像（DSA_LVA_cor）如下图所示，并调整图中灰度显示范围：

![冠状位图像（DSA_LVA_cor）](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002108966.png)

矢状位图像（DSA_LVA_sag）如下图所示：

![矢状位图像（DSA_LVA_sag）](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002203150.png)

6. 在Matlab中，对**4**中的3D TOF图像分别沿第一维和第二维取最大值（该过程称为最大强度投影，maximum intensity projection, MIP。如果取最小值结果又会怎么样？），并对图像做一定旋转（通常是90度）或左右对调，并显示，使其方向与图**5**中的DSA图像一致。（注：在matlab中，沿某一维取最大值可使用函数`max`，图像旋转可使用函数`imrotate`）

```matlab
% 6.MIP

% 第一维最大值
tof_max_1 = max(tof, [], 1);
% 第二维最大值
tof_max_2 = max(tof, [], 2 );

mip_1 = squeeze(tof_max_1);
mip_1 = imrotate(mip_1, 90);
mip_2 = squeeze(tof_max_2);
mip_2 = fliplr(imrotate(mip_2, 90));

imshow(mip_1)

imshow(mip_2)
```

+ 第一维MIP：

![第一维MIP](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002350119.png)

+ 第二维MIP：

![第二维MIP](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002356817.png)

7. 简述计算机断层成像与投影成像的主要区别。

X射线投影成像是依据X射线的基本特性（穿透作用，感光作用，荧光作用），对探测目标发射X射线，凭借不同密度组织对射线吸收能力不同，来进行成像。X射线投影成像是直接输出X线经过人体衰减之后落在探测器上的影像。CT 的成像原理是应用 X 线束围绕人体的某一部位连续断面扫描，是X线扫描人体一圈后根据X线衰减规律重建（迭代法、反投影法等）成像，是断层层面成像。可以说，投影成像是三维体积重叠在二维平面上的图像，CT是对组织器官扫描得到的多个断层二维图像序列。

8. 使用函数`dicominfo`读取DICOM文件头，分别找出上述TOF图像和DSA图像的空间分辨率（即体素或像素的尺寸）。

> 注：空间分辨率包含在标签`PixelSpacing`或`SpacingBetweenSlices`，或`ImagerPixelSpacing`；
>
> 另外，需要注意的是，这些数值仅表示当前所显示图像的体素或像素大小，并不一定是原始采集分辨率，通常为了提高肉眼观察的效果，成像设备厂商会对原始采集图像进行一定倍数的插值，再保存成Dicom、提供给用户。

```matlab
% 8
X_info = dicominfo('TOF_Dicom/Mag (0001).dcm')
X_sag_info = dicominfo('DSA_LVA_sag/Image (0017).dcm')
X_cor_info = dicominfo('DSA_LVA_cor/Image (0017).dcm')
X_info.PixelSpacing
X_cor_info.PositionerPrimaryAngle
X_sag_info.PositionerPrimaryAngle
```



|                                                        | TOF          | DSA_LVA_cor  | DSA_LVA_sag  |
| ------------------------------------------------------ | ------------ | ------------ | ------------ |
| PixelSpacing/ SpacingBetweenSlices/ ImagerPixelSpacing | 0.37880.3788 | 0.37060.3706 | 0.28600.2860 |

9. DSA Dicom图像中标签DistanceSourceToDetector，DistanceSourceToPatient，PositionerPrimaryAngle和PositionerSecondaryAngle的含义：

+ DistanceSourceToDetector：源头到探测器的距离

+ DistanceSourceToPatient：源头到病人的距离

+ PositionerPrimaryAngle/ PositionerSecondaryAngle：定位器角度。定位器角度的定义与患者相关，零度参考垂直于患者胸部的原点。 Positioner Primary Angle（主角度）定义类似于经度（在赤道平面中）； Positioner Secondary Angle（次角度） 的定义类似于纬度（在矢状面上）。如下图所示：

PositionerPrimaryAngle：

![PositionerPrimaryAngle](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002815791.png)

PositionerSecondaryAngle：

![PositionerSecondaryAngle](https://ossjiyaoliu.oss-cn-beijing.aliyuncs.com/uPic/image-20220923002822256.png)