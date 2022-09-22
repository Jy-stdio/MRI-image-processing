import dicom2nifti
 
 
 
if __name__ == '__main__':
    dicom_path = "/Users/liujiyao/Documents/2022课程/医学图像处理/作业/2 Exercise/TOF_Dicom"
    dicom2nifti.convert_directory(dicom_path,'/Users/liujiyao/Documents/2022课程/医学图像处理/作业/2 Exercise/TOF_nii')
 


 
# import SimpleITK as sitk
 
# '''
# 功能：读取filepath下的dcm文件
# 返回值：读取得到的SimpleITK.SimpleITK.Image类   
# 其他说明：  file = sitk.ReadImage(filepath)
#             获取基本信息，大小，像素间距，坐标原点，方向
#             file.GetSize()
#             file.GetOrigin()
#             file.GetSpacing()
#             file.GetDirection()
# '''
# def readdcm(filepath):
#    #filepath = "./T2"
#     series_id = sitk.ImageSeriesReader.GetGDCMSeriesIDs(filepath)
#     series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(filepath, series_id[0])
#     series_reader = sitk.ImageSeriesReader() #读取数据端口
#     series_reader.SetFileNames(series_file_names)  #读取名称
#     images = series_reader.Execute()#读取数据
#     #print(images.GetSpacing())
#     #sitk.WriteImage(images, "T2_1.nii.gz")#保存为nii
#     return images
 
 
# if __name__ == '__main__':
#     filepath =  "./dcm"  #保存路径
#     dcm_images = readdcm(filepath)   #读取文件
#     sitk.WriteImage(dcm_images, "dcm.nii.gz")#保存为nii       

