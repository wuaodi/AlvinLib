clc;clear;

XX = "nautilus"

%% 重定义图片的名字大小和格式
% strcat()函数经常出现在批量处理的时候，这个时候我们需要用到for循环，
% 然后这个函数能够让变量和路径产生一些关系，这个时候我们就可以对其进行批量处理。
imagePath1 = strcat('C:\Users\WU AODI\Desktop\101_ObjectCategories\',XX,'\');    % 原图像位置
% imagePath1 = 'C:\Users\WU AODI\Desktop\101_ObjectCategories\';    % 原图像位置
imagePath2 = 'E:\study\research\1project_DA_classification\satellite_seg\datamake2\negimgs\';    % 重定义后位置

imageFiles = dir(imagePath1);    % 列出当前文件夹中的文件和文件夹  
numFiles = length(imageFiles);    % 获取图片的数量+2的值

%% 方法一，图片顺序可能会乱
tic
for i = 3:numFiles    % matlab 并行 其实和 for 一个用法               
    j = i-2;    % imageFiles 从第三项开始才是图片名字
    disp(j);    % disp() 函数直接将内容输出在 Matlab 命令窗口中  
    imageFile = strcat(imagePath1,imageFiles(i).name);    % 连接字符串
    A = imread(imageFile);    % 读入图片  
%     B = imresize(A, [256 256]);    % 重定义大小 
%     B = imresize(A, 0.5)    % 将图片前两个通道缩放为原来的相应倍数
%     B = repmat(A,[1,1,3]);    % 将单通道图片变为三通道
    B = A;
    imwrite (B, strcat(imagePath2,XX,num2str(j),'.jpg'));    % 保存图片,重定义名字和格式    
%     imwrite (B, strcat(imagePath2,"barrel",num2str(j),'.jpg'));    % 保存图片,重定义名字和格式        
end 
toc



%% 方法二，图片名字有序号，使用序号，不乱序
% tic
% for i = 1:numFiles-2
%     disp(i);    % disp() 函数直接将内容输出在 Matlab 命令窗口中 
%     imageFile = strcat(imagePath1,"frame",num2str(i),'.jpg');
%     A = imread(imageFile);    % 读入图片  
% %     B = imresize(A, [256 256]);    % 重定义大小 
% %     B = imresize(A, 0.5)    % 将图片前两个通道缩放为原来的相应倍数
%     % 将单通道图片变为三通道    
%     if numel(size(A)) == 3
%         B = A;
%     else
%         B = repmat(A,[1,1,3]);    
%     end
%     imwrite (B, strcat(imagePath2,"frame",num2str(i),'.jpg'));    % 保存图片,重定义名字和格式
% end
% toc