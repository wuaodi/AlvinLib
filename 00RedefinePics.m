clc;clear;

XX = "nautilus"

%% �ض���ͼƬ�����ִ�С�͸�ʽ
% strcat()�����������������������ʱ�����ʱ��������Ҫ�õ�forѭ����
% Ȼ����������ܹ��ñ�����·������һЩ��ϵ�����ʱ�����ǾͿ��Զ��������������
imagePath1 = strcat('C:\Users\WU AODI\Desktop\101_ObjectCategories\',XX,'\');    % ԭͼ��λ��
% imagePath1 = 'C:\Users\WU AODI\Desktop\101_ObjectCategories\';    % ԭͼ��λ��
imagePath2 = 'E:\study\research\1project_DA_classification\satellite_seg\datamake2\negimgs\';    % �ض����λ��

imageFiles = dir(imagePath1);    % �г���ǰ�ļ����е��ļ����ļ���  
numFiles = length(imageFiles);    % ��ȡͼƬ������+2��ֵ

%% ����һ��ͼƬ˳����ܻ���
tic
for i = 3:numFiles    % matlab ���� ��ʵ�� for һ���÷�               
    j = i-2;    % imageFiles �ӵ����ʼ����ͼƬ����
    disp(j);    % disp() ����ֱ�ӽ���������� Matlab �������  
    imageFile = strcat(imagePath1,imageFiles(i).name);    % �����ַ���
    A = imread(imageFile);    % ����ͼƬ  
%     B = imresize(A, [256 256]);    % �ض����С 
%     B = imresize(A, 0.5)    % ��ͼƬǰ����ͨ������Ϊԭ������Ӧ����
%     B = repmat(A,[1,1,3]);    % ����ͨ��ͼƬ��Ϊ��ͨ��
    B = A;
    imwrite (B, strcat(imagePath2,XX,num2str(j),'.jpg'));    % ����ͼƬ,�ض������ֺ͸�ʽ    
%     imwrite (B, strcat(imagePath2,"barrel",num2str(j),'.jpg'));    % ����ͼƬ,�ض������ֺ͸�ʽ        
end 
toc



%% ��������ͼƬ��������ţ�ʹ����ţ�������
% tic
% for i = 1:numFiles-2
%     disp(i);    % disp() ����ֱ�ӽ���������� Matlab ������� 
%     imageFile = strcat(imagePath1,"frame",num2str(i),'.jpg');
%     A = imread(imageFile);    % ����ͼƬ  
% %     B = imresize(A, [256 256]);    % �ض����С 
% %     B = imresize(A, 0.5)    % ��ͼƬǰ����ͨ������Ϊԭ������Ӧ����
%     % ����ͨ��ͼƬ��Ϊ��ͨ��    
%     if numel(size(A)) == 3
%         B = A;
%     else
%         B = repmat(A,[1,1,3]);    
%     end
%     imwrite (B, strcat(imagePath2,"frame",num2str(i),'.jpg'));    % ����ͼƬ,�ض������ֺ͸�ʽ
% end
% toc